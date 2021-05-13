# -*- coding: utf-8 -*-
"""
Created on Mon May 10 19:12:57 2021

@author: M10817021
"""

from selenium import webdriver
import time
from bs4 import BeautifulSoup
import requests
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.instagram.com/ww0205ww/")
time.sleep(5)
driver.find_element_by_class_name("sqdOP.L3NKy.y3zKF").click()
time.sleep(5)
driver.find_element_by_name("username").send_keys("morris85morris85@yahoo.com.tw")
driver.find_element_by_name("password").send_keys("mo3040700")
time.sleep(5)
driver.find_elements_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div')[0].click()
time.sleep(5)
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/div/button')))
driver.find_elements_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')[0].click()
time.sleep(5)
js="var action=document.documentElement.scrollTop=10000"
ans = []
limit=100
for i in range(limit):    
    driver.execute_script(js)
    time.sleep(2)

    soup = BeautifulSoup(driver.page_source,"lxml")
    s=soup.find_all(class_="KL4Bh")
    ans.append(s)

res=[]
for i in range(limit):
    a = ans[i]
    for j in range(len(a)):
        if a[j] in res:
            continue
        else:
            res.append(a[j])

for i in range(len(res)):
    src = res[i].img.get('src')
    img = requests.get(src)

    with open('./img/%d.png'%(i+1),'wb') as f:
        f.write(img.content)
driver.close()