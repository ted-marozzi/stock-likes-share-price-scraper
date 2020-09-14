import fbscrape as fb
import asxscrape as asx


pageName = "pointsbet"
pageSoup = fb.getPageSoup(pageName)
print(fb.getPageLikes(pageName, pageSoup))

"""
for i in range(5):
  

  
  try:
    pageName = "pointsbet"
    pageSoup = fb.getPageSoup(pageName)
    print(fb.getPageLikes(pageName, pageSoup))

    break
  except:
    pass


 

"""