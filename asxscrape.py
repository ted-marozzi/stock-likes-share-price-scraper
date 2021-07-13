############################################################################


from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup


def getAsxSoup(ticker):
    url = "https://www2.asx.com.au/markets/company/" + ticker
    WINDOW_SIZE = "1920,1080"
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
    driver = webdriver.Chrome(options=chrome_options)

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

def getSharePrice(asx_soup):
    sharePrice = asx_soup.find_all("dl", class_= "dl-lg")

    sharePrice = [_.text for _ in sharePrice]
    sharePrice = sharePrice[0]
    sharePrice = sharePrice.split()
    sharePrice = sharePrice[5]

    return sharePrice




if __name__ == '__main__':

    # Page name is the string in the ur of page after www.facebook.com/
    pageName = "pointsbet"
    soup = getAsxSoup("https://www2.asx.com.au/markets/company/PBH")

    print(getSharePrice(soup))


#############################################################


