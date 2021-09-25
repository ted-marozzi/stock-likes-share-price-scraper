import fbscrape as fb
import yahooscrape as yahoo
import log

stockToScrape = [
                # AU Stocks
                {"name":"pointsbet", "ticker":"PBH", "regionCode": "AX"},
                {"name":"ZipAU", "ticker":"Z1P", "regionCode": "AX"},
                {"name":"mineralresourceslimited", "ticker":"MIN", "regionCode": "AX"},
                {"name":"afterpay.it", "ticker":"APT", "regionCode": "AX"},
                {"name":"coles", "ticker":"COL", "regionCode": "AX"},
                {"name":"Wesfarmers-Resources-Limited-228765013813567", "ticker":"WES", "regionCode": "AX"},
                # US Stocks
                {"name":"TESLAOfficialPage", "ticker":"TSLA", "regionCode": ""}
                ]

for i in range(5):
    try:

        for stock in stockToScrape:
            likes = fb.getPageLikes(stock["name"], fb.getPageSoup(stock["name"]))
            sharePrice = yahoo.getSharePrice(yahoo.getStockSoup(stock["ticker"], regionCode=stock["regionCode"]))
            log.log(stock["name"], likes, sharePrice)

        break
    except Exception as e:
        print(e)
