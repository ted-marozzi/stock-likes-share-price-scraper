import fbscrape as fb

pageName = "pointsbet"
for i in range(5):
  try:
    pageSoup = fb.getPageSoup(pageName)
    print(fb.getPageLikes(pageName, pageSoup))
    break
  except:
    pass


 
