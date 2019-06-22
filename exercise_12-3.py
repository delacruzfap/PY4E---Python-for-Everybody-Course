# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
count = int(input('Enter count: '))
pos = int(input('Enter position: '))

print('Retrieving:', url)

i = 0
while i < count:
    i = i + 1
    # print(i)
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve all of the anchor tags, get link, and store in a list
    tags = soup('a')
    tags_list = list()
    tags_list.append(url)

    for tag in tags:
        tags_list.append(tag.get('href', None))
    url = tags_list[pos]
    print('Retrieving:', url)

