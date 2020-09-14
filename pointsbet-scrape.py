import fbscrape as fb
import asxscrape as asx



for i in range(5):
  

  
  try:
    pageName = "pointsbet"
    pageSoup = fb.getPageSoup(pageName)
    print(fb.getPageLikes(pageName, pageSoup))

    break
  except:
    pass


 
