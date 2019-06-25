import urllib.request, urllib.parse, urllib.error
import ssl
import xml.etree.ElementTree as ET

# Ignore certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
# sample data = http://py4e-data.dr-chuck.net/comments_42.xml
# actual data = http://py4e-data.dr-chuck.net/comments_245543.xml

html = urllib.request.urlopen(url, context=ctx).read()
tree = ET.fromstring(html)
lst = tree.findall('comments/comment')

print('Retrieving', url)
counter = 0
count_list = list()
for item in lst:
    counter = counter + 1
    count = int(item.find('count').text)
    count_list.append(count)

print('Retrieved', len(html), 'characters')
print('Count:', counter)
print('Sum:', sum(count_list))