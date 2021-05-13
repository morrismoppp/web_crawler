from selenium import webdriver
import time
from bs4 import BeautifulSoup
import requests
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.instagram.com/'target_account_name'/")
time.sleep(5)
# login 
driver.find_element_by_class_name("sqdOP.L3NKy.y3zKF").click()
time.sleep(5)
driver.find_element_by_name("username").send_keys("ur username")
driver.find_element_by_name("password").send_keys("ur password")
time.sleep(5)
driver.find_elements_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div')[0].click()
time.sleep(5)
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/div/button')))
driver.find_elements_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')[0].click()
time.sleep(5)
# scrolldown the web page
js="var action=document.documentElement.scrollTop=10000"
ans = []
limit=100
for i in range(limit):    
    driver.execute_script(js)
    time.sleep(2)
    soup = BeautifulSoup(driver.page_source,"lxml")
    s=soup.find_all(class_="KL4Bh")
    ans.append(s)
# check if captured src is repeat
res=[]
for i in range(limit):
    a = ans[i]
    for j in range(len(a)):
        if a[j] in res:
            continue
        else:
            res.append(a[j])
# save to ur local folder
for i in range(len(res)):
    src = res[i].img.get('src')
    img = requests.get(src)
    with open('./img/%d.png'%(i+1),'wb') as f:
        f.write(img.content)
driver.close()
