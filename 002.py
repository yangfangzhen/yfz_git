from selenium import webdriver
from selenium.webdriver.common.by import By

dr = webdriver.Chrome()

dr.get('https://www.baidu.com')
dr.find_element(By.CSS_SELECTOR,'#kw').send_keys('杨芳振')