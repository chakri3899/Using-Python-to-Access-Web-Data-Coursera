#Problem: Following Links in Python
#visit this url for the problem - https://www.py4e.com/tools/python-data/?PHPSESSID=207feca20cd7793ea3313f498a2e6724


import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

input_url = input('enter URL - ')
open_url = urllib.request.urlopen(input_url).read()

soup = BeautifulSoup(open_url, 'html.parser')
tags = soup('a')

count = 7
for i in range (count):
    pose = 18
    for tag in tags:
        pose -= 1
        if pose == 0:
            print(tag.get('href', None))
            print(tag.contents[0])
            new_link = tag.get('href', None)
            open_url = urllib.request.urlopen(new_link).read()
            soup = BeautifulSoup(open_url, 'html.parser')
            tags = soup('a')
