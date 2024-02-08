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
# username.send_keys("standard_user")
# password.send_keys("secret_sauce")
# logiButton.click()
#
# url = driver.current_url
# print(url)
# if "inventory" in url:
#     print("Testcase pass")
# else:
#     print("Testcase pass")
#
# driver.quit()

# Test case 2
#
# driver.get("https://www.saucedemo.com/v1/")
# username = driver.find_element(By.ID,"user-name")
# password = driver.find_element(By.ID,"password") # method 2
# logiButton = driver.find_element(By.ID,"login-button")
#
# username.send_keys("standard_user")
# password.send_keys("secret_sauce")
# logiButton.click()
# strB = driver.title
# print(strB)
# if strB == "Swag Labs":
#     print("Test case pass")
# else:
#     print("Test case fail")
# driver.quit()

#back()

# Test case 3
# driver.get("https://www.saucedemo.com/v1/")
# username = driver.find_element(By.ID,"user-name")
# password = driver.find_element(By.ID,"password") # method 2
# logiButton = driver.find_element(By.ID,"login-button")
#
# username.send_keys("standard_user")
# password.send_keys("secret_sauce")
# logiButton.click()
#
# dashBoardUrl = driver.current_url
# print(dashBoardUrl)
# driver.back()
# loginUrl = driver.current_url
# print(loginUrl)
# if dashBoardUrl != loginUrl:
#     print("Test case pass")
# else:
#     print("Test case fail")


#forward()
driver.get("https://www.saucedemo.com/v1/")
driver.get('https://www.google.com')
driver.back()
driver.forward()
googleUrl = driver.current_url
if "google" in googleUrl:
    print("Test case pass")
else:
    print("Test case fail")

driver.quit()

# navigators:-
# Webdriver
# get()
# title
# current_url
# back()
# forward()
# find_element
