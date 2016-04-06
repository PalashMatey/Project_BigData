import urllib.request

#x = urllib.request.urlopen('https://en.wikipedia.org/wiki/Wikipedia:Random')
#print(x.read())

import urllib.parse

url = 'https://en.wikipedia.org/wiki/'
values = {'Wikipedia':'Random'}

data = urllib.parse.urlencode(values)
data = data.encode('utf-8')
req = urllib.request.Request(url,data)
resp = urllib.request.urlopen(req)
respData = resp.read()
print(respData)
