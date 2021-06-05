from urllib.request import urlopen
from bs4 import BeautifulSoup
"""urllib(means you don't have to instll anything extra to run this example) is stadard python library and imports only the function urlopen
        and contains funcitons for requesting data across the web."""

"""urlopen is used to open a remote objects across a network and read it.
        it can read HTML files, image files and another files with esase"""

#Check packages installed 
"""pip freeze"""

#installing Beautifulsoup
"""pip install Beautifulsoup4"""
html = urlopen('http://pythonscraping.com/pages/page1.html')
print(html.read())