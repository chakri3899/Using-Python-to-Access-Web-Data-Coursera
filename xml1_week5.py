#Problem: Extracting data from XML
#visit this url for the problem - https://www.py4e.com/tools/python-data/?PHPSESSID=f2d57a1839533b3bf8e7129dcb08d0e0


import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

input_url = input('enter URL - ')
data = urllib.request.urlopen(input_url).read()

tree = ET.fromstring(data)
counts = tree.findall('comments/comment/count')

sum = 0
for count in counts:
    sum = sum + int(count.text)

print(sum)
