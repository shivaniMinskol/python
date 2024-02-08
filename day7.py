from selenium import  webdriver
from  selenium.webdriver.common.by import By
driver = webdriver.Chrome()
#driver = webdriver.Firefox()

# id , class , name , linkText , partialLinkText,cssSelector,xpath. tagName
# get()

# Testcase 1

# driver.get("https://www.saucedemo.com/v1/") # get() -- method1
# username = driver.find_element(By.ID,"user-name")
# password = driver.find_element(By.ID,"password") # method 2
# logiButton = driver.find_element(By.ID,"login-button")
#