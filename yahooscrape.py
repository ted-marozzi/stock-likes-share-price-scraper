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

    WINDOW_SIZE = "1920,1080"

    chromeOptions = Options()

        # Should open window or not?
    if headless:
        chromeOptions.add_argument("--headless")
    chromeOptions.add_argument("--window-size=%s" % WINDOW_SIZE)
    chromeOptions.add_argument("disable-notifications")

    driver = webdriver.Chrome(options=chromeOptions)
    driver.get(url)

    # Try getting xpath element if not specified scroll and wait as necessary
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "")))
    except:
        pass
    finally:
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        driver.quit()

    return soup

def getSharePrice(stockSoup):
    sharePrice = stockSoup.find_all("span", class_= "Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)")
    sharePrice = [_.text for _ in sharePrice]
    sharePrice = sharePrice[0]
    print("The share price is", sharePrice)

    return float(sharePrice)

if __name__ == '__main__':

    # Page name is the string in the ur of page after www.facebook.com/
    soup = getStockSoup("TSLA")
    print(getSharePrice(soup))