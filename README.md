# Web scraping in python

This is a small project, that **collects data from a website and then saves them to a json file**.

## Description

Parsed URL: https://www.hyperia.sk/kariera/

The program finds all job offers in the URL and gains more information by opening hyperlinks *("viac info")*.

It finds information about the title, salary, location, contract type and contact and saves them to the *data.json* file.


## Libraries

Libraries used for this project: **BeautifulSoup4**, **urllib.request**

Beautiful Soup is a Python library for parsing HTML and XML documents.

Urllib is a python 3 package for opening and reading URL-s.

## Install required packages

These are included in the *requirements.txt* file. You can install them by the help of the following command:

`pip install -r requirements.txt`

## Execute program
You can execute python script in command line typing
`py main.py`


