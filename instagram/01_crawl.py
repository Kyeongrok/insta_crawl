import requests
from bs4 import BeautifulSoup
import json

def crawl(url):

    data = requests.get(url)
    print(data, url)
    return data.content

def parse(pageString):
    bsObj = BeautifulSoup(pageString, "html.parser")
    aTag = bsObj.find("div", {"class":"k_Q0X"})

    script = bsObj.find("script", {"type":"application/ld+json"})
    jsonObj = json.loads(script.text)
    print(jsonObj['uploadDate'])

    return {}

url = "https://www.instagram.com/p/BwVoqW7H7b6/"

pageString = crawl(url)
result = parse(pageString)
print(result)
