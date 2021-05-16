import csv
from datetime import date
import os

OUT_PATH = "out/"


def log(pageName, numberOfLikes, sharePrice):
    _makeOutDirectory(pageName)
    today = date.today()
    logPath = "out/" + pageName + "/" + pageName + ".csv"

    with open(logPath, "a", newline='') as fileHandle:

        writer = csv.writer(fileHandle)
        writer.writerow([today.strftime("%d/%m/%Y"),
                        str(numberOfLikes), str(sharePrice)])
        dateLogged = False


def isDateLogged(pageName):
    _makeOutDirectory(pageName)
    logPath = OUT_PATH + pageName + "/" + pageName + ".csv"
    # Create the file if needed
    with open(logPath, "a") as fileHandle:
        pass
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
    lastLine = ""
    try:
        dateLogged = lastLine.split(",")[0].split(
            '\n')[0] == today.strftime("%d/%m/%Y")

    except IndexError:
        with open(logPath, "a", newline='') as fileHandle:

            writer = csv.writer(fileHandle)
            writer.writerow(
                [pageName.capitalize() + " Page Likes", "Date", "Share Price"])

            dateLogged = False
    
    return dateLogged, lastLine


def _makeOutDirectory(pageName):
    # Check if / needed
    if not os.path.exists("out"):
        os.makedirs("out")

    # Creates the page folder if needed
    if not os.path.exists(OUT_PATH + pageName):
        os.makedirs(OUT_PATH + pageName)




def _writeSoupToFile(pageSoup, pageName):
    with open(OUT_PATH + pageName + "/" + pageName + ".html", "w", encoding="utf=8") as fileHandle:
        fileHandle.write(str(pageSoup))
