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
