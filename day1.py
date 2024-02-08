import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# arrangment
# driver= webdriver.Chrome(executable_path="C:\selenium driver\chromedriver_win32\chromedriver106\chromedriver.exe")
s=Service("C:\selenium driver\chromedriver_win32\chromedriver106\chromedriver.exe")
driver=webdriver.Chrome(service=s)
driver.get("http://demo.automationtesting.in/Register.html")
driver.maximize_window()
time.sleep(5)
# Action

driver.find_element(By.XPATH,"//input[@ng-model='FirstName']").send_keys("shivani")
driver.find_element(By.XPATH,"//input[@ng-model='LastName']").send_keys("hedau")
driver.find_element(By.XPATH,"//textarea[@ng-model='Adress']").send_keys("pardi")
driver.find_element(By.XPATH,"//input[@ng-model='EmailAdress']").send_keys("shivanihedau@gmail.com")


# assertion