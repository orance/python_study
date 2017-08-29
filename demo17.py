import re
test = "site sea sue sweet see case sse ssee loses 321312343289"
m = re.findall(r"\bs\S*?e\b",test)
n = re.findall(r"\d+",test)
if m and n:
    print m
    print n
else:
    print 'not match'
