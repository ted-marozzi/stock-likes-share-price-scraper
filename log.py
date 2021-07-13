import csv
from datetime import date
import os

OUT_PATH = "out/"

def log(pageName, numberOfLikes, sharePrice):
    
    _makeOutDirectory(pageName)
    today = date.today()
    logPath = "out/" + pageName + "/" + pageName + ".csv"
    if not isDateLogged(pageName)[0]:
        with open(logPath, "a", newline='') as fileHandle:
            writer = csv.writer(fileHandle)
            writer.writerow([today.strftime("%d/%m/%Y"),
                            str(numberOfLikes), str(sharePrice)])

def isDateLogged(pageName):
    _makeOutDirectory(pageName)
    logPath = OUT_PATH + pageName + "/" + pageName + ".csv"

    lastLine = ""
    try:
        # Check log file for the last line logged
        with open(logPath, "r") as fileHandle:
            lines = fileHandle.read().splitlines()
            lastLine = lines[-1]
    except:
        pass

    today = date.today()
    dateLogged = True

    try:
        dateLogged = lastLine.split(",")[0] == today.strftime("%d/%m/%Y")
    except IndexError:
        dateLogged = False
    return dateLogged, lastLine


def _makeOutDirectory(pageName):

    # Check if / needed
    if not os.path.exists("out"):
        os.makedirs("out")

    # Creates the page folder if needed
    if not os.path.exists(OUT_PATH + pageName):
        os.makedirs(OUT_PATH + pageName)

    csvPath = OUT_PATH + pageName + "/" + pageName + ".csv"
    if not os.path.exists(csvPath):
        with open(csvPath, "a", newline='') as fileHandle:
            writer = csv.writer(fileHandle)
            writer.writerow(
                ["Date", pageName.capitalize() + " Page Likes", "Share Price"])

def writeSoupToFile(pageSoup, pageName):
    with open(OUT_PATH + pageName + "/" + pageName + ".html", "w", encoding="utf=8") as fileHandle:
        fileHandle.write(str(pageSoup))
