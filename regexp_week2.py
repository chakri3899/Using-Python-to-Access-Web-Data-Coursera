/*problem: Fnding numbers in a haystack 
  visit this url for the problem - https://www.py4e.com/tools/python-data/?PHPSESSID=3b24a1c38c0b20288123ac85b1d1b434 */


import re

hand = open("regex_sum_24962.txt")
x=list()
for line in hand:
     y = re.findall('[0-9]+',line)
     x = x+y

sum=0
for z in x:
    sum = sum + int(z)

print(sum)
