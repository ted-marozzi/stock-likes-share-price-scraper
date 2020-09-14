############################################################################


from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup


def getAsxSoup(url):

    #CHROMEDRIVER_PATH = '/usr/lib/chromium-browser/chromedriver'
    CHROMEDRIVER_PATH = 'C:/bin/chromedriver_win32/chromedriver.exe'
    WINDOW_SIZE = "1920,1080"

    chrome_options = Options()  
    chrome_options.add_argument("--headless")  
    chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
    #chrome_options.binary_location = CHROME_PATH

    
    driver = webdriver.Chrome(CHROMEDRIVER_PATH, options=chrome_options)
    print(url)
    driver.get(url)
    try:
        WebDriverWait(driver, 45).until(EC.presence_of_element_located((By.CSS_SELECTOR,"span.ng-binding")))
    except:
        print("Exception")

    finally:
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        driver.quit()
        return soup
        

def getSharePrice(asx_soup):
    sharePrice = asx_soup.find_all("span", {"class": "ng-binding"})

    sharePrice = [_.text for _ in sharePrice]
    sharePrice = sharePrice[1]

    return sharePrice

#############################################################
