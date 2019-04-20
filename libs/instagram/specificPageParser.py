from bs4 import BeautifulSoup
import json

def parse(pageString):
    bsObj = BeautifulSoup(pageString, "html.parser")
    aTag = bsObj.find("div", {"class":"k_Q0X"})

    script = bsObj.find("script", {"type":"application/ld+json"})
    jsonObj = json.loads(script.text)

    return jsonObj['uploadDate']


