from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError

from bs4 import BeautifulSoup

"""urllib(means you don't have to instll anything extra to run this example) is stadard python library and imports only the function urlopen
        and contains funcitons for requesting data across the web."""

"""urlopen is used to open a remote objects across a network and read it.
        it can read HTML files, image files and another files with esase"""

#Check packages installed 
"""pip freeze"""

#installing packages
"""
pip install Beautifulsoup4
pip install lxml
pip install html5lib

"""
#about lxml 
"""lxml has some advantages ove html.parser in that it is generally better at parsing'messy"or malformed HTML code.
    it fixes problems like uncloded tags, tags that improperly nested."""
html = urlopen('http://pythonscraping.com/pages/page1.html')
# bs = BeautifulSoup(html.read(), 'html.parser')
# bs = BeautifulSoup(html.read(), 'lxml')
# bs = BeautifulSoup(html.read(), 'html5lib')
#read() is used in order to get th
# e HTML content of the page.
# print(bs.h1)



def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bs = BeautifulSoup(html.read(), 'html.parser')
        title = bs.body.h1
    except AttributeError as e:
        return None
    return title

title = getTitle('http://www.pythonscraping.com/pages/page1.html')
if title == None:
    print('Title could not be found')
else:
    print(title)