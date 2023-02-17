import random
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

def return_title_site():
    driver = webdriver.Chrome()
    driver.get("https://www.twitter.com/")
    driver.find_element(by=By.PARTIAL_LINK_TEXT, value="S'inscrire").click()
    title = driver.title
    print(title)
    driver.close()
    return title
    
return_title_site()