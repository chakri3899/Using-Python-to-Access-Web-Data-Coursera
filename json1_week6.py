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
