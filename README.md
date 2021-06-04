# Instructions:
1) Make secret.json file for fb login in root directory

{
    "Username": "foo@bar.com"
    "Password": "foobar"
}

2) Install chromedriver and pass the path to functions required

https://chromedriver.chromium.org/downloads


Ex below:
```
CHROMEDRIVER_PATH = 'C:/bin/chromedriver_win32/chromedriver.exe'
for i in range(5):

    try:
        pageName = "pointsbet"
        likes  = fb.getPageLikes(pageName, fb.getPageSoup(pageName, chromedriverPath=CHROMEDRIVER_PATH), chromedriverPath=CHROMEDRIVER_PATH)
        sharePrice = asx.getSharePrice(asx.getAsxSoup(
            "https://www.asx.com.au/asx/share-price-research/company/PBH", chromedriverPath=CHROMEDRIVER_PATH))
        log.log(pageName, likes, sharePrice)
        break
    except Exception as e:
        print(e)

```
