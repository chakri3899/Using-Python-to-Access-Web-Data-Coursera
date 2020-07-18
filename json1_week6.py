#Problem: Exrtacting data from JSON
#visit this url for the problem - https://www.py4e.com/tools/python-data/?PHPSESSID=23736cf4e1a89ea59a71ff0c28f49979


import urllib.request, urllib.parse, urllib.error
import json

url = input("enter url - ")

data = urllib.request.urlopen(url).read()

js = json.loads(data)

sum = 0
for item in js['comments']:
    x = item['count']
    sum = sum + int(x)
print(sum)
