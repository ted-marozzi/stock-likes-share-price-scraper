# Instructions:
1) Make secret.json file for facebook login in root directory
```JSON
{
    "Username": "foo@bar.com",
    "Password": "foobar"
}
```
2) Install chromedriver and add to path, or maybe put it in the root folder idk if that will work though.

    You may need to know your chrome version number

    chrome://settings/help

    to get the correct chrome driver here

    https://chromedriver.chromium.org/downloads

3) Run

```pip install -r requirments.txt```

4) See stockscrape for an example driver program

5) See how I used this bot too perform automated data analytics on google sheets

https://docs.google.com/spreadsheets/d/1fd4rigWrHU5Rq5y7TZr6YR30uVKpme39_r6yaXJBfwI/edit#gid=643877149

6) If you fork this repo a github action will run at 11:55 aest on Mon-Fri and commit results of stockscrap.py to the out directory. It will fail unless you add a valid facebook username to your repo secrets named FB_USER_NAME, and password FB_PASSWORD. This will collect stock data for you every business day without the need to host your own server. You will also need to create a MY_PAT secret containing a personal access token from your github that has repo and workflow permissions
