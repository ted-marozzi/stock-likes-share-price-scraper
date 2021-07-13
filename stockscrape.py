import fbscrape as fb
import yahooscrape as yahoo
import log

for i in range(5):
    try:
        pageName = "pointsbet"
        likes  = fb.getPageLikes(pageName, fb.getPageSoup(pageName))
        sharePrice = yahoo.getSharePrice(yahoo.getStockSoup("PBH"))
        log.log(pageName, likes, sharePrice)

        pageName = "ZipAU"
        likes  = fb.getPageLikes(pageName, fb.getPageSoup(pageName))
        sharePrice = yahoo.getSharePrice(yahoo.getStockSoup("Z1P"))
        log.log(pageName, likes, sharePrice)

        pageName = "mineralresourceslimited"
        likes  = fb.getPageLikes(pageName, fb.getPageSoup(pageName))
        sharePrice = yahoo.getSharePrice(yahoo.getStockSoup("MIN"))
        log.log(pageName, likes, sharePrice)

        pageName = "afterpay.it"
        likes  = fb.getPageLikes(pageName, fb.getPageSoup(pageName))
        sharePrice = yahoo.getSharePrice(yahoo.getStockSoup("APT"))
        log.log(pageName, likes, sharePrice)
        
        pageName = "TESLAOfficialPage"
        likes  = fb.getPageLikes(pageName, fb.getPageSoup(pageName))
        sharePrice = yahoo.getSharePrice(yahoo.getStockSoup("TSLA"))
        log.log(pageName, likes, sharePrice)    

        break
    except Exception as e:
        print(e)
