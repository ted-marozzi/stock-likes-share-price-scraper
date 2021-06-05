# Instructions:
1) Make secret.json file for facebook login in root directory

{
    "Username": "foo@bar.com",
    "Password": "foobar"
}

2) Install chromedriver and pass the path to functions required

    You may need to know your chrome version number

    chrome://settings/help

    to get the correct chrome driver here

    https://chromedriver.chromium.org/downloads

    Then add chromedriver exe to path, or maybe put it in the root folder idk if that will work though.

3)
    pip install the following packages: selenium, bs4, matplotlib

Ex below:
```

for i in range(5):

    try:
        # This is the page name of the url on facebook
        pageName = "pointsbet"
        likes  = fb.getPageLikes(pageName, fb.getPageSoup(pageName))
        sharePrice = asx.getSharePrice(asx.getAsxSoup(
            "https://www.asx.com.au/asx/share-price-research/company/PBH"))
        log.log(pageName, likes, sharePrice)
        break
    except Exception as e:
        print(e)

```
