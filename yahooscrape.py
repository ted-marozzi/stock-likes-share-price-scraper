from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

def getStockSoup(ticker, regionCode="", headless=True):

    if regionCode!="":
        regionCode = "." + regionCode
    url = "https://au.finance.yahoo.com/quote/" + ticker + regionCode

    chromeOptions = Options()

        # Should open window or not?
    if headless:
        chromeOptions.add_argument("--headless")

    WINDOW_SIZE = "1920,1080"
    chromeOptions.add_argument("--window-size=%s" % WINDOW_SIZE)
    chromeOptions.add_argument("disable-notifications")
    chromeOptions.add_argument("--no-sandbox")
    chromeOptions.add_argument("--disable-dev-shm-usage")


    driver = webdriver.Chrome(options=chromeOptions)
    driver.get(url)

    # Try getting xpath element if not specified scroll and wait as necessary
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="quote-header-info"]/div[3]/div[1]/div/fin-streamer[1]')))
    except:
        pass
    finally:
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        driver.quit()

    return soup

def getSharePrice(stockSoup: BeautifulSoup):
    sharePrice = stockSoup.find("fin-streamer", {'data-test':"qsp-price"}).text.strip().replace(",", "")
    print("The share price is", sharePrice)

    return float(sharePrice)

if __name__ == '__main__':

    # Page name is the string in the ur of page after www.facebook.com/
    soup = getStockSoup("TSLA")
    print(getSharePrice(soup))
