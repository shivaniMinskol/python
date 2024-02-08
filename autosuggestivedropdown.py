# import time
# from selenium import  webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select
#
#
# driver = webdriver.Chrome()
# driver.get("https://webdriveruniversity.com/Autocomplete-TextField/autocomplete-textfield.html")
#
# actualTitle = driver.title
# expectedTitle = "WebDriver | Contact Us"
# #assert  actualTitle == expectedTitle
# if(actualTitle == expectedTitle):
#     print("Testcase pass")
# else:
#     print("Test case fail")
#
# driver.find_element(By.ID,"myInput").send_keys("A")
# elements = driver.find_elements(By.CSS_SELECTOR, "#myInputautocomplete-list  > div")
# for element in elements:
#     if element.text == "Almond":
#             element.click()
#             driver.find_element(By.ID, "submit-button").click()
#             if "Almond" in  driver.current_url:
#                 print("Testcase pass")
#             else:
#                 print("Testcase fail")
#             break
#
#
# driver.find_element(By.ID,"myInput").clear()
# driver.find_element(By.ID,"myInput").send_keys("G")
# elements = driver.find_elements(By.CSS_SELECTOR, "#myInputautocomplete-list  > div")
# for element in elements:
#     if element.text == "Grapes":
#             element.click()
#             driver.find_element(By.ID, "submit-button").click()
#             if "Grapes" in  driver.current_url:
#                 print("Testcase pass")
#             else:
#                 print("Testcase fail")
#             break
#
#
# driver.close()

from selenium import webdriver
from selenium.webdriver.common.by import By

driver= webdriver.Chrome()
driver.get("https://webdriveruniversity.com/Autocomplete-TextField/autocomplete-textfield.html")

# actualltitel=driver.title
# expectedtitle="WebDriver | Contact Us"

# inputelement=driver.find_element(By.ID,"myInput")
# inputelement.send_keys("A")
#
# autosugg_element=driver.find_elements(By.CSS_SELECTOR,"#myInputautocomplete-list >div")
#
# for i in autosugg_element:
#     if i.text == "lmond":
#         i.click()
#         driver.find_element(By.ID,"submit-button").click()
#         if "Almond" in driver.current_url:
#             print("test case pass")
#         else:
#             print("test case fail")
# ------------------------------------------------------------------------

inputelement=driver.find_element(By.ID,"myInput")
inputelement.send_keys("G")

autosugg_element=driver.find_elements(By.CSS_SELECTOR,"#myInputautocomplete-list >div")

for i in autosugg_element:
    if i.text == "rapes":
        i.click()
        driver.find_element(By.ID,"submit-button").click()
        if "Grapes" in driver.current_url:
            print("test case pass")
        else:
            print("test case fail")


driver.close()












