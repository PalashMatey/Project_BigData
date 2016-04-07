import urllib.request

import re
import urllib.parse
#x = urllib.request.urlopen('https://en.wikipedia.org/wiki/Wikipedia:Random')
x = urllib.request.urlopen('https://en.wikipedia.org/wiki/Village')
respData = x.read()
#paragraphs = re.findall(r'<p>(.*?)<\p>',str(respData))
paragraphs = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', str(respData))
#print(paragraphs)
for para in paragraphs:
	#print(para)
	y = urllib.request.urlopen(str(para))
	break
print('\n\n\n')

resp = y.read()
paragraphs1 = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', str(resp))
print(paragraphs1)
#values = {'Wikipedia':'Random'}

#data = urllib.parse.urlencode(values)
#data = data.encode('utf-8')
#req = urllib.request.Request(url,data)
#resp = urllib.request.urlopen(req)
#respData = resp.read()
#print(respData)











'''
Understanding Regular Expressions
\d: any number
\D: anything but a number
\s: a space
\S: anything but a space
\w:Any character
\W:anything but a character
. : specific letter,any character. Except a new line
\b : the white space around words
\. : a period

Modifiers
(Looking for this amount or type of numbers)
{x,y} : Expection 1-3 \d{1,3}
= : Match 1 or more
? : Match 0 or 1
* : Match 0 or more
$ : Match the end of the string
^ : Match the beginning of a string
| : either or 
[]: range or 'variance' [A-Z]
{x} : Expecting x amount of data

White Space Characters
(characters you may not see)

\n : new line
\s : space
\t : tab
\f : form feed




import re

exampleString =''Jessica is 15 years old, and Daniel is 27 years old.Edward is 97 years old, and his grandfather, Oscar, is 102. ''
ages = re.findall(r'\d{1,3}',exampleString)
names = re.findall(r'[A-Z][a-z]*',exampleString)

print(ages)
print(names)

x = 0
ageDict = {}
for name in names:
	ageDict[name] = ages[x]
	x = x + 1

print(ageDict)
'''
