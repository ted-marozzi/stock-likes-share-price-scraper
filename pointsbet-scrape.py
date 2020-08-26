import fbscrape as fb

pageName = "pointsbet"

pageSoup = fb.getPageSoup(pageName)


print(fb.getPageLikes(pageName, pageSoup))



