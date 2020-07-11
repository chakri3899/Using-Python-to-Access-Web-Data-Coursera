import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

html = urllib.request.urlopen( 'http://py4e-data.dr-chuck.net/comments_493057.html').read()
soup = BeautifulSoup(html, 'html.parser')

sum = 0
count = 0
tags = soup('span')
for tag in tags:
    count = count + 1
    sum = sum + int(tag.contents[0])
print(count)
print(sum)
