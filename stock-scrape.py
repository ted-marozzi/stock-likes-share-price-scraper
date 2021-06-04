import fbscrape as fb
import asxscrape as asx
import log

CHROMEDRIVER_PATH = 'C:/bin/chromedriver_win32/chromedriver.exe'


for i in range(5):

    try:
        pageName = "pointsbet"
        likes  = fb.getPageLikes(pageName, fb.getPageSoup(pageName))
        sharePrice = asx.getSharePrice(asx.getAsxSoup(
            "https://www2.asx.com.au/markets/company/PBH"))
        log.log(pageName, likes, sharePrice)
        
        
        pageName = "ZipAU"
        likes  = fb.getPageLikes(pageName, fb.getPageSoup(pageName))
        sharePrice = asx.getSharePrice(asx.getAsxSoup(
            "https://www2.asx.com.au/markets/company/Z1P"))
        log.log(pageName, likes, sharePrice)
        
        break
    except Exception as e:
        print(e)
