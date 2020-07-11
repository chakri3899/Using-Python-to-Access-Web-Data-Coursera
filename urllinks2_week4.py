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
