# Web scaping imports
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

import time
import json
import csv

from matplotlib import pyplot as plt

from datetime import date

import log

import asxscrape as asx



# Logs into facebook
def _FBLogin(username, password, pageName, chromedriverPath='/usr/lib/chromium-browser/chromedriver', headless=True):
    # Path to your chromedriver.exe
    # CHROMEDRIVER_PATH = 'C:/bin/chromedriver_win32/chromedriver.exe'
    WINDOW_SIZE = "1920,1080"

    chromeOptions = Options()

    # Should open window or not?
    if headless:
        chromeOptions.add_argument("--headless")

    chromeOptions.add_argument("--window-size=%s" % WINDOW_SIZE)
    chromeOptions.add_argument("disable-notifications")
    # Opens page and fills in form
    driver = webdriver.Chrome(chromedriverPath, options=chromeOptions)
    pageName = '/' + pageName
    driver.get("https://www.facebook.com" + pageName)
    driver.find_element_by_xpath('//input[@id="email"]').send_keys(username)
    driver.find_element_by_xpath('//input[@id="pass"]').send_keys(password)
    driver.find_element_by_xpath('//input[@value="Log In"]').click()

    return driver


def _printLoginTest(driver):

    if "logout" in driver.page_source:
        print("Login succeded")
        return True
    else:
        print("Login failed")
        return False




# Need a json file in directory with Username and Password fields
def _getSecretKeys():
    with open('secret.json') as fileHandle:
        return json.load(fileHandle)

# Works as of 31/07/2020


def getPageLikes(pageName, pageSoup, chromedriverPath='/usr/lib/chromium-browser/chromedriver'):

    dateLogged, lastLine = log.isDateLogged(pageName)

    if(dateLogged):
        return lastLine.split(", ")[0]
    else:

        elementToScrape = "span"
        classNumLikes = "oo9gr5id"

        indexNumLikes = 0

        # Extract number of page likes
        numberOfLikesArr = pageSoup.find_all(
            elementToScrape, class_=classNumLikes)
        print(numberOfLikesArr)
        numbers = []
        for ele in numberOfLikesArr:

            ele = ele.text.split(' ')[0]
            ele = ele.replace(",", "")

            if ele.isnumeric():

                numbers.append(int(ele))

        numbers.sort(reverse=True)

        numberOfLikes = numbers[0]

        return numberOfLikes


def getPageSoup(pageName, maxScroll=1, headless=True, chromedriverPath='/usr/lib/chromium-browser/chromedriver'):

    # Get Authentifaction
    secret = _getSecretKeys()

    # Likes

    xpath = "/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div[4]/div[2]/div/div[1]/div[2]/div[1]/div/div/div/div[2]/div[5]/div[1]/div/div/div[2]/div/div/span/span[1]"

    # Login to browser
    driver = _FBLogin(secret["Username"], secret["Password"], pageName,
                      headless=headless, chromedriverPath=chromedriverPath)

    trys = 0
    while(not _printLoginTest(driver) and trys < 5):
        driver = _FBLogin(
            secret["Username"], secret["Password"], pageName, headless=headless)
        trys += 1

    # Try getting xpath element if not specified scroll and wait as neccassary
    try:

        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, xpath)))
    except:
        print("Element not located, still attempting scrape anyway.")

    SCROLL_PAUSE_TIME = 1
    RETRYS = 3

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
        if new_height == last_height and iterCount == RETRYS:
            break
        elif new_height == last_height:
            print("Retry", iterCount + 1, "for scroll", i)
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
#


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

    # TODO =>
    # Lucas:
    #   More decriptive errors and print info
    #   Make averging function
    #
    # Ted:
    #   make pip installable
    #   scrape profiles
    #   make pip install dependacies, and secret .json
    #   tell users how to install chrome driver, make fn smaller name, make module package make sense
    #   update read me
    #
