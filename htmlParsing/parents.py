from urllib.request import urlopen
from bs4 import BeautifulSoup
"""When scraping pages, you will likely discover that you need to find parents of tags
less frequently than you need to find their children or siblings."""

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html.read(), 'html.parser')

print(bs.find('img',
             {'src':'../img/gifts/img1.jpg'}).parent.previous_sibling.get_text())

"""
    The image location is slected first, select the parent of the tag secondly, 
    select the previous_sibling of the td tag, select the text within the tag.
"""

"""This will print the price of the object represented by the image at the location"""