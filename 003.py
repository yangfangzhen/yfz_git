#encoding:utf8
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

dr = webdriver.Chrome()
dr.get('https://www.baidu.com')
locator = (By.CSS_SELECTOR,'#kw')
WebDriverWait(dr,3,0.1).until(EC.visibility_of_element_located(locator))
dr.find_element_by_css_selector('#kw').send_keys('yfz')