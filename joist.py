from lib import jHead, jModule, jStyle
import os.path, time

def pageBuilder():
    
    # User chooses file name
    
    fileName = input('> Type a file name: ')
    
    # Joist opens file name
    
    pageBuild = open(fileName, 'w+')
    
    # Joist checks for pre-existing CSS folder. If none, it creates one along with default styles.

    cssCheck = os.listdir('./')
    cssDirectory = str('css')
    if cssDirectory in cssCheck:
        os.chdir('./css')
        print("> Skipping default CSS file creation.")
    else:
        print("> Creating default style sheet.")
        os.mkdir('./css')
        os.chdir('./css')
        styleSheet = open('style.css', 'w+')
        styleSheet.write(jStyle.jStyle)
        styleSheet.close()

    # Joist checks for pre-existing custom CSS file. If none, it creates one.

    customCssCheck = os.listdir('./')
    customCssFile = str('customStyle.css')
    
    if customCssFile in customCssCheck:
        print("> Skipping custom CSS file creation.")
    else:
        print("> Creating blank custom style sheet.")
        customStyleSheet = open('customStyle.css', 'w+')
        customStyleSheet.write(jStyle.jCustomStyle)
        customStyleSheet.close()
    
    # Joist checks for pre-existing navigation CSS file. If none, it creates one.

    navCssCheck = os.listdir('./')
    navCssFile = str('navStyle.css')
    
    if navCssFile in navCssCheck:
        print("> Skipping navigation CSS file creation.")
    else:
        print("> Creating navigation style sheet.")
        navStyleSheet = open('navStyle.css', 'w+')
        navStyleSheet.write(jStyle.jNavStyle)
        navStyleSheet.close()
    
    # User choose number of elements on page
    
    while True:
        try:
            pageElements = int(input('> Choose number of elements: '))
            break
        except ValueError:
            print('> Please provide an integer value.')
    
    # Joist writes document head from jHead
    
    pageBuild.write(jHead.jHead)
    
    # Loop for user to choose the selected number of page elements from jModule
    
    while pageElements > 0:
        pageInput = input("> Please choose an element. Type 'Help' for options: ")
        if pageInput == 'n1':
            pageBuild.write(jModule.navigation)
            pageElements = pageElements - 1
            continue
        elif pageInput == 'h1':
            pageBuild.write(jModule.hero)
            pageElements = pageElements - 1
            continue
        elif pageInput == 'h2':
            pageBuild.write(jModule.slideShow)
            pageElements = pageElements - 1
            continue
        elif pageInput == 't1':
            pageBuild.write(jModule.oneColumnText)
            pageElements = pageElements - 1
            continue
        elif pageInput == 't2':
            pageBuild.write(jModule.twoColumnText)
            pageElements = pageElements - 1
            continue
        elif pageInput == 't3':
            pageBuild.write(jModule.threeColumnText)
            pageElements = pageElements - 1
            continue
        elif pageInput == 't4':
            pageBuild.write(jModule.fourColumnText)
            pageElements = pageElements - 1
            continue
        elif pageInput == 't5':
            pageBuild.write(jModule.menu)
            pageElements = pageElements - 1
            continue
        elif pageInput == 'i1':
            pageBuild.write(jModule.textImage)
            pageElements = pageElements - 1
            continue
        elif pageInput == 'i2':
            pageBuild.write(jModule.imageText)
            pageElements = pageElements - 1
            continue
        elif pageInput == 'i3':
            pageBuild.write(jModule.image)
            pageElements = pageElements - 1
            continue
        elif pageInput == 'i4':
            pageBuild.write(jModule.textFullImage)
            pageElements = pageElements - 1
            continue
        elif pageInput == 'i5':
            pageBuild.write(jModule.fullImageText)
            pageElements = pageElements - 1
            continue
        elif pageInput == 'p1':
            pageBuild.write(jModule.portfolio)
            pageElements = pageElements - 1
            continue
        elif pageInput == 'c1':
            pageBuild.write(jModule.threeColumnCta)
            pageElements = pageElements - 1
            continue
        elif pageInput == 'c2':
            pageBuild.write(jModule.threeColumnCtaWithImages)
            pageElements = pageElements - 1
            continue
        elif pageInput == 'all' or pageInput == 'All' or pageInput == 'ALL':
            pageBuild.write(jModule.templateAll)
            pageElements = pageElements - pageElements
        elif pageInput == 'help' or pageInput == "Help":
            print('> | ELEMENT OPTION                  | VALUE  |')
            print('> |---------------------------------|--------|')
            print('> | Navigation                      | n1     |')
            print('> | Hero                            | h1     |')
            print('> | Slideshow                       | h2     |')
            print('> | One-column text                 | t1     |')
            print('> | Two-column text                 | t2     |')
            print('> | Three-column text               | t3     |')
            print('> | Four-column text                | t4     |')
            print('> | Menu                            | t5     |')
            print('> | Text, image                     | i1     |')
            print('> | Image, text                     | i2     |')
            print('> | Image                           | i3     |')
            print('> | Text, full image                | i4     |')
            print('> | Full image, text                | i5     |')
            print('> | Portfolio                       | p1     |')
            print('> | Three-column CTA                | c1     |')
            print('> | Three-column CTA w/images       | c2     |')
        elif pageInput == 'exit' or pageInput == 'Exit' or pageInput == 'quit' or pageInput == 'Quit' or pageInput == 'stop' or pageInput == 'Stop':
            sys.exit("> Goodbye!")
        else:
            print("Please choose a valid option.")
    
    # Joist writes body closing tags from jHead
    
    pageBuild.write(jHead.jBodyEnd)
    
    # Joist writes time stamp from jHead

    # pageBuild.write(jHead.timeStamp)

    # Joist write HTML closing tags from jHead
    
    pageBuild.write(jHead.jHtmlEnd)

    # Joist closes file
    
    pageBuild.close()

pageBuilder()