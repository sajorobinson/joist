# Joist

**Joist** is a website template builder written in Python.

## Overview

Joist can create beautiful, simple, and mobile-responsive website templates through a command-line interface.

The purpose of Joist is not to create ready-to-publish websites. Rather, the purpose of Joist is to create the skeleton a website very quickly.

Once Joist creates the skeleton of the website, the web designer can quickly alter it to their needs. Joist lessens the need to set up a website's basic structure and style.

Joist is good for creating basic websites in HTML, CSS, and JavaScript. It's also good for creating rapid prototypes of websites.

Joist is not designed for creating complete, ready-to-publish websites. It's goal is to make the web design process easier by reducing some of the grunt work.

## Use

You must have at least Python 3.6.5 to use Joist.

1. Open a command-line interface.
2. Navigate to the directory where you downloaded Joist.
3. Type the following command: `python3 joist.py`.
4. Joist will ask you for a file name. Input a filename in the following format: `file_name.html`.
5. Joist will ask you how many elements you want on your website. Provide an integer value.
6. Joist will ask you to choose elements for your website. Type `Help` for a list of options.
7. Input element choices into the command-line interface until the program closes.

## Output

Once you create your website, four files should appear in the directory where you downloaded and ran Joist:

* index.html
* style.css
* customStyle.css
* navStyle.css

The *index.html* file is your web page.

The *style.css* file is your Joist stylesheet with all of Joist's default styles.

The *customStyle.css* file is a blank stylesheet for you to create custom styles outside the default Joist stylesheet.

The **navStyle.css** file is a file that contains all the styles for the navigation bar.

## Structure

Joist is organized into four parts:

* *joist.py*
* lib
    * *jHead.py*
    * *jModule.py*
    * *jStyle.py*

### joist.py

*Joist.py* is the main file of Joist. It drives the user interface and functions that write the web and CSS pages.

### lib

The lib folder contains all of the module files for Joist.

Each module of Joist contains some HTML, CSS, or JavaScript that can be written on the page.

#### jHead.py

The module *jHead.py* contains variables for the head of the HTML document, the closing tags, and a time stamp to record when the web file was created.

#### jModule.py

The module *jModule.py* contains variables for all of the sections of the HTML document.

#### jStyle.py

The module *jStyle.py* contains variables for the default Joist stylesheet and the custom, blank user style sheet.

## Versions

| Version           | Codename                 | Date              |
|-------------------|--------------------------|-------------------|
| 0.6               |                          | 06 - 16 - 2018    |
| 0.5               |                          | 05 - 11 - 2018    |
| 0.4               |                          | 05 - 08 - 2018    |
| 0.3               |                          | 05 - 07 - 2018    |
| 0.2               |                          | 05 - 07 - 2018    |
| 0.1               |                          | 05 - 04 - 2018    |

## Retrospective

My goal for this project was to create a tool I could use to quickly make simple websites.

When I set out to work on this project, I decided that most of my work would be writing HTML and CSS that could be altered quickly enough for templating but full-featured enough to be used out of the box.

The default style sheets for this project represent one template for the underlying HTML, which is logically structured into rows, columns, and modules. I'm happy enough with the command line interface for this project. My future work on this project will be to create new templates for it. When I learn more about Python, I may revisit this project to give it a UI.

This project is there first where I've focused significantly on modularity. When I was first learning Python, I tended to put everything into one file. Anecdotally, I found that putting my page modules, style modules, etc, in different places helped me conceptualize the project better as a whole.
