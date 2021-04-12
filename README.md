# Joist

**Joist** is a website template builder written in Python.

## Overview

Joist can create simple, mobile-responsive website templates through a command-line interface.

The purpose of Joist is to create the skeleton of a basic website very quickly. The user can put together pages from modules and templates. Joist also creates a default stylesheet and a custom stylesheet.

## How to use

You must have at least Python 3.6.5 to use Joist. The steps below assume that you're running Joist as a script instead of as a compiled executable.

1. Open a command-line interface
2. Navigate to the directory where you downloaded Joist.
3. Run Joist by typing `python3 joist.py` (Mac / Linux) or `python joist.py` (Windows).
4. Follow prompts to create filename, choose whether you want to build from a template/modules, and how many modules you want.
5. Type `Help` whenever you want a list of options.
6. Select elements or templates until the program quits.

## Expected output

Once you create your website, four files should appear in the directory where you downloaded and ran Joist:

* NameOfYourFile.html
* style.css
* customStyle.css
* navStyle.css

The *NameOfYourFile.html* file is your web page.

The *style.css* file is your Joist stylesheet with all of Joist's default styles.

The *customStyle.css* file is a blank stylesheet for you to create custom styles outside the default Joist stylesheet.

The *navStyle.css* file is a file that contains all the styles for the navigation bar.

## How is Joist organized?

Joist is organized into different modules that help build the web pages:

| File           | Description                                              |
|----------------|----------------------------------------------------------|
| joist.py       | Main script                                              |
| lib\jhead.py   | Built out the head/end of the HTML document              |
| lib\jModule.py | Contains the HTML modules used for building the web page |
| lib\jPage.py   | Combines modules from jModule to create templates        |
| jStyle.py      | Contains the stylesheets used to make the site look good |

## Goals

| Goal                  | Description                                                                                                                                  | Implemented? |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------------------|--------------|
| Create CSS templates  | The user should be able to choose from multiple CSS templates to significantly alter the style of the website.                               | No           |
| Create site templates | Site templates have been implemented sort of, but there should be a wide variety of sites the user can choose from.                          | No           |
| Create a custom nav   | Right now, Joist uses [LuxBar](https://github.com/balzss/luxbar), which is really nice, but it would be better if we had something original. | No           |
| Create a slide show   | Right now, there is no slideshow module. This is something we need to implement as it's very basic website design.                           | No           |
| Create GUI            | An eventual goal of mine as a programmer is to move beyond command line interfaces and make a GUI.                                           | No           |

## Versions

| Version | Codename | Date           |
|---------|----------|----------------|
| 0.7     |          | 03 - 07 - 2019 |
| 0.6     |          | 06 - 16 - 2018 |
| 0.5     |          | 05 - 11 - 2018 |
| 0.4     |          | 05 - 08 - 2018 |
| 0.3     |          | 05 - 07 - 2018 |
| 0.2     |          | 05 - 07 - 2018 |
| 0.1     |          | 05 - 04 - 2018 |
