import requests
from bs4 import BeautifulSoup

def crawl(url):

    data = requests.get(url)
    print(data, url)
    return data.content

def parse(pageString):
    bsObj = BeautifulSoup(pageString, "html.parser")
    print(bsObj)
    aTag = bsObj.find("div", {"class":"k_Q0X"})
    print(aTag)
    return {}

url = "https://www.instagram.com/p/BwVoqW7H7b6/"

pageString = crawl(url)
result = parse(pageString)
print(result)
