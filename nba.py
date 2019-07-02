#-*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
    
res = requests.get("http://www.espn.com/nba/standings",
                   headers=headers)
soup = BeautifulSoup(res.text, "html.parser")

t = ""
table = soup.select(".hide-mobile")
print("Eastern Conference\n====================================================================================")
for i in range(0, 15):
    t += str(i+1)+" "+table[i].text+":\t"
    for j in range(0, 13):
        score = soup.select(".stat-cell")[i*13+j].text
        t += score+" "
    print(t)
    t=""
print("\nWestern Conference\n=====================")
for i in range(15, 30):
    t += str(i-14)+" "+table[i].text+":\t"
    for j in range(0, 13):
        score = soup.select(".stat-cell")[i*13+j].text
        t += score+" "
    print(t)
    t = ""
    










