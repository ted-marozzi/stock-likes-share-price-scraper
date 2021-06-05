import fbscrape as fb
import asxscrape as asx
import log

for i in range(5):

    try:
        pageName = "pointsbet"
        likes  = fb.getPageLikes(pageName, fb.getPageSoup(pageName))
        sharePrice = asx.getSharePrice(asx.getAsxSoup("PBH"))
        log.log(pageName, likes, sharePrice)

        pageName = "ZipAU"
        likes  = fb.getPageLikes(pageName, fb.getPageSoup(pageName))
        sharePrice = asx.getSharePrice(asx.getAsxSoup("Z1P"))
        log.log(pageName, likes, sharePrice)

        break
    except Exception as e:
        print(e)
