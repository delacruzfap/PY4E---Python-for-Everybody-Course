import urllib.request, urllib.error, urllib.parse
import ssl
import json

# Ignore certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url: ')
# sample data = http://py4e-data.dr-chuck.net/comments_42.json
# actual data = http://py4e-data.dr-chuck.net/comments_245544.json
data = urllib.request.urlopen(url, context=ctx).read()
info = json.loads(data)
comments = info['comments']

counter = 0
number_list = list()
for counts in comments:
    number = counts['count']
    number_list.append(number)
    counter = counter + 1

print('Retrieving', url, '...')
print('Retrieved:', len(data), 'characters')
print('Count:', counter)
print('Sum:', sum(number_list))


