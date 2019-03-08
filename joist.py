# EXPLANATION: Joist is a website template builder written in Python (3.6).

from lib import jHead, jModule, jStyle, jPage
import os.path, time, sys


def pageBuilder():

    fileName = input("> Type a file name: ")

    pageBuild = open(fileName, "w+")

    pageBuild.write(jHead.jHead)

    cssCheck = os.listdir("./")
    cssDirectory = "css"
    if cssDirectory in cssCheck:
        os.chdir("./css")
        print("> Skipping default CSS file creation.")
    else:
        print("> Creating default style sheet.")
        os.mkdir("./css")
        os.chdir("./css")
        styleSheet = open("style.css", "w+")
        styleSheet.write(jStyle.jStyle)
        styleSheet.close()

    customCssCheck = os.listdir("./")
    customCssFile = "customStyle.css"

    if customCssFile in customCssCheck:
        print("> Skipping custom CSS file creation.")
    else:
        print("> Creating blank custom style sheet.")
        customStyleSheet = open("customStyle.css", "w+")
        customStyleSheet.write(jStyle.jCustomStyle)
        customStyleSheet.close()

    navCssCheck = os.listdir("./")
    navCssFile = "navStyle.css"

    if navCssFile in navCssCheck:
        print("> Skipping navigation CSS file creation.")
    else:
        print("> Creating navigation style sheet.")
        navStyleSheet = open("navStyle.css", "w+")
        navStyleSheet.write(jStyle.jNavStyle)
        navStyleSheet.close()

    buildTypeInput = input(
        "> Would you like to choose a page template [1] or build a page? [2] "
    )

    if buildTypeInput == "1":

        templateList = dir(jPage)

        pageBuilt = 1

        while pageBuilt > 0:

            pageInput = input("> Please choose a template. Type 'Help' for options: ")

            if pageInput in templateList:
                templateChoice = getattr(jPage, pageInput, None)
                pageBuild.write(templateChoice)
                pageBuilt = pageBuilt - 1
                continue
            elif pageInput == "help" or pageInput == "Help" or pageInput == "HELP":
                print("> Please choose from one of the options.")
                print(sorted(templateList[8:]))
                continue
            elif pageInput == "exit" or pageInput == "Exit" or pageInput == "EXIT":
                sys.exit("Goodbye!")
            else:
                print("> Please choose a valid element. ")

    elif buildTypeInput == "2":

        while True:
            try:
                pageElements = int(input("> Choose number of elements: "))
                break
            except ValueError:
                print("> Please provide an integer value.")

        while pageElements > 0:

            pageInput = input("> Please choose an element. Type 'Help' for options: ")

            elementList = dir(jModule)

            if pageInput in elementList:
                elementChoice = getattr(jModule, pageInput, None)
                pageBuild.write(elementChoice)
                pageElements = pageElements - 1
                continue
            elif pageInput == "help" or pageInput == "Help" or pageInput == "HELP":
                print("> Please choose from one of the options.")
                print(sorted(elementList)[8:])
                continue
            elif pageInput == "exit" or pageInput == "Exit" or pageInput == "EXIT":
                sys.exit("Goodbye!")
            else:
                print("> Please choose a valid element. ")

    pageBuild.write(jHead.jBodyEnd)

    pageBuild.write(jHead.timeStamp)

    pageBuild.write(jHead.jHtmlEnd)

    pageBuild.close()


pageBuilder()
