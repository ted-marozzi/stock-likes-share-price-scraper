# Web scaping imports
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import json
import csv
from matplotlib import pyplot as plt
from datetime import date
import log

# Logs into facebook
def _FBLogin(username, password, headless=True):

    WINDOW_SIZE = "1920,1080"

    chromeOptions = Options()

    # Should open window or not?
    if headless:
        chromeOptions.add_argument("--headless")
    chromeOptions.add_argument("--window-size=%s" % WINDOW_SIZE)
    chromeOptions.add_argument("disable-notifications")

    # Opens page and fills in form
    driver = webdriver.Chrome(options=chromeOptions)



    driver.get("https://www.facebook.com/")
    driver.save_screenshot("1.png")

    driver.find_element_by_id('email').send_keys(username)
    driver.find_element_by_id('pass').send_keys(password)
    driver.find_element_by_id('pass').send_keys(Keys.ENTER)
    driver.save_screenshot("2.png")

    return driver


def _printLoginTest(driver):
    if "logout" in driver.page_source:
        print("Login succeeded")
        return True
    else:
        print("Login failed")
        return False




# Need a json file in directory with Username and Password fields
def _getSecretKeys():
    with open('secret.json') as fileHandle:

        return json.load(fileHandle)

# Works as of 31/07/2020
def getPageLikes(pageName, pageSoup):
    dateLogged, lastLine = log.isDateLogged(pageName)
    print("Date logged is:", dateLogged)
    if(dateLogged):
        numberOfLikes = lastLine.split(",")[1]
    else:
        elementToScrape = "span"
        classNumLikes = "oo9gr5id"
        indexNumLikes = 0

        # Extract number of page likes
        numberOfLikesArr = pageSoup.find_all(elementToScrape, class_=classNumLikes)
        numbers = []


        for ele in numberOfLikesArr:
            ele = ele.text.split(' ')[0]
            ele = ele.replace(",", "")
            if ele.isnumeric():
                numbers.append(int(ele))

        print("potential numbers:", numberOfLikesArr)

        numbers.sort(reverse=True)
        print("Numbers:", numbers)
        numberOfLikes = numbers[0]
    print(pageName, "page has", numberOfLikes, "likes")

    return numberOfLikes


def getPageSoup(pageName, maxScroll=0, headless=True):

    # Get Authentication
    secret = _getSecretKeys()

    # Likes
    xpath = "/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div[4]/div[2]/div/div[1]/div[2]/div[1]/div/div/div/div[2]/div[5]/div[1]/div/div/div[2]/div/div/span/span[1]"

    # Login to browser
    driver = _FBLogin(secret["Username"], secret["Password"], headless=headless)
    # attempts = 0
    # while(not _printLoginTest(driver) and attempts < 5):
    #     driver = _FBLogin(secret["Username"], secret["Password"], headless=headless)
    #     attempts += 1
    driver.save_screenshot("3.png")
    try:
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "")))
    except:
        pass
    finally:
        driver.save_screenshot("4.png")
        driver.get("https://www.facebook.com/" + pageName)

    # Try getting xpath element if not specified scroll and wait as necessary
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "")))
    except:
        pass
    driver.save_screenshot("5.png")
    SCROLL_PAUSE_TIME = 2
    RETRIES = 3

    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    for i in range(maxScroll):
        print("Num Scrolls:", i)
        iterCount = 0
        # Scroll down to bottom
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height and iterCount == RETRIES:
            break
        elif new_height == last_height:
            iterCount += 1
            i -= 1
        last_height = new_height
    pageSoup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()

    return pageSoup

# Function by https://gist.github.com/SanthoshBala18
def _strToNum(x):
    total_stars = 0
    num_map = {'K': 1000, 'M': 1000000, 'B': 1000000000, 'k': 1000}
    if x.isdigit():
        total_stars = int(x)
    else:
        if len(x) > 1:
            total_stars = float(x[:-1]) * num_map.get(x[-1].upper(), 1)

    return int(total_stars)

def plotLikes(pageName, postLikesList):

    # plt.bar(range(len(postLikesList)), postLikesList)
    plt.plot(postLikesList)
    plt.xlabel("Post number")
    plt.ylabel('Number of likes')
    plt.title(pageName + " likes per post over time.")
    plt.savefig("out/" + pageName + "/" + pageName + ".png")
    plt.clf()

# Extracts the post likes from a facebook page soup
def getPagePostLikes(pageName, pageSoup):
    elementToScrape = "span"
    classNumLikes = "pcp91wgn"

    # Extract number of page likes
    postLikesList = pageSoup.find_all(elementToScrape, class_=classNumLikes)
    del postLikesList[1::2]

    # Delete every second starting at 2nd element
    for i in range(len(postLikesList)):
        postLikesList[i] = _strToNum(postLikesList[i].text)
    postLikesList = list(reversed(postLikesList))
    print(postLikesList)

    return postLikesList

def greedyScrapePage(pageName):
    pageSoup = getPageSoup(pageName, maxScroll=50)
    pagePostLikesList = getPagePostLikes(pageName, pageSoup)
    pageLikes = getPageLikes(pageName, pageSoup)
    plotLikes(pageName, pagePostLikesList)

    return pageLikes, pagePostLikesList

if __name__ == '__main__':

    # Page name is the string in the ur of page after www.facebook.com/
    pageName = "pointsbet"
    pageSoup = getPageSoup(pageName, headless=False)

    #pageSoup = BeautifulSoup(open("out/pointsbet/pointsbet.html"), "html.parser")
    print(getPageLikes(pageName, pageSoup))
