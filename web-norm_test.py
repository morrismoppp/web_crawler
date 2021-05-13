# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 00:24:13 2021

@author: M10817021
"""

from bs4 import BeautifulSoup
import requests
import cloudscraper

'''網頁爬蟲'''
scraper = cloudscraper.create_scraper()
res = scraper.get("https://www.dcard.tw/f/sex/")
#print(res.content)
soup = BeautifulSoup(res.content, "html.parser")
#print(soup.prettify())  #輸出排版後的HTML內容

titles = soup.find_all("img", referrerpolicy="no-referrer")
ans=[]
for title in titles:
    ans.append(title.get("src"))
#    print(title.get("src"))

for i in range(len(ans)):
    image_url=ans[i]
    try:
        r = requests.get(image_url) 
    except:
        continue
    with open('C:/Users/M10817021/Desktop/webnorm/%d.png'%(i+1),'wb') as f: 
        f.write(r.content)
