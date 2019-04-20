import json
from libs.crawler import crawl
from libs.instagram.specificPageParser import parse

file = open("../dangstagram_urls")
jsonObj = json.loads(file.read())

print(len(jsonObj))

datetimeParsedInfo = []
for info in jsonObj[0:10]:
    try:
        pageString = crawl(info['key'])
        datetime = parse(pageString)
        info['datetime'] = datetime
        datetimeParsedInfo.append(info)
    except Exception as e:
        print(e)

print(datetimeParsedInfo)










