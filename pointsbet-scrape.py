import fbscrape as fb
import asxscrape as asx


CHROMEDRIVER_PATH = 'C:/bin/chromedriver_win32/chromedriver.exe'

for i in range(5):

  try:
    pageName = "pointsbet"
    pageSoup = fb.getPageSoup(pageName)
    print(fb.getPageLikes(pageName, pageSoup))
    break
  except:
    print("Probably chrome driver path")


 
