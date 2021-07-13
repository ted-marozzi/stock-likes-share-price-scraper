import fbscrape as fb
import asxscrape as asx
import nysescrape as nyse
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

        pageName = "mineralresourceslimited"
        likes  = fb.getPageLikes(pageName, fb.getPageSoup(pageName))
        sharePrice = asx.getSharePrice(asx.getAsxSoup("MIN"))
        log.log(pageName, likes, sharePrice)

        pageName = "afterpay.it"
        likes  = fb.getPageLikes(pageName, fb.getPageSoup(pageName))
        sharePrice = asx.getSharePrice(asx.getAsxSoup("APT"))
        log.log(pageName, likes, sharePrice)
        
        pageName = "TESLAOfficialPage"
        likes  = fb.getPageLikes(pageName, fb.getPageSoup(pageName))
        sharePrice = nyse.getSharePrice(nyse.getNyseSoup("TSLA"))
        log.log(pageName, likes, sharePrice)    

        break
    except Exception as e:
        print(e)
