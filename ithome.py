#-*- coding: utf-8 -*-
import requests
import re
from bs4 import BeautifulSoup
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
def removeDuplicates(links):
    one = []
    for check in links:
        if check not in one:
            one.append(check)
    return one
def removetext(text):
    o=[]
    for good in text:
        if good not in o:
            o.append(good)
    return o
def removesummary(summary):
    n=[]
    for ok in summary:
        if ok not in n:
            n.append(ok)
    return n
res=requests.get("https://www.ithome.com.tw/security",headers=headers)
soup = BeautifulSoup(res.text, "html.parser")
links=[]
text=[]
summary=[]
for item in soup.select('.summary'):
    summary.append(item.text)
for item in soup.select('.channel-item'):
    for link in item.findAll("a", href=re.compile("^(/news/)")):
        links.append(link.attrs['href'])
        text.append(link.text)

links = removeDuplicates(links)
text = removetext(text)
summary= removesummary(summary)
text.pop(0)
for i in range(0, len(links)):
    print("==========================================================")
    print("https://www.ithome.com.tw"+links[i])
    print(text[i])



        
    
    
    



          


    
   
     
