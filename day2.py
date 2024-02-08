import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# arrangement
# action
# assertion

driver = webdriver.Chrome()
driver.get("http://www.webdriveruniversity.com/Contact-Us/contactus.html")

# finding the single element
ele1 = driver.find_element(By.CSS_SELECTOR, 'h2[name="contactme"]').is_displayed()
if ele1:
    print("Testcase Pass")
else:
    print("Testcase Fail")

# finding multiple elements
ele2 = len(driver.find_elements(By.CSS_SELECTOR, 'input[type="text"]'))
if ele2 == 3:
    print("Testcase Passed!")
else:
    print("Testcase Failed")

# ClassName
ele3 = len(driver.find_elements(By.CLASS_NAME, "feedback-input"))
if ele3 == 4:
    print("Testcase Passed!")
else:
    print("Testcase Failed")

# ID
ele4 = driver.find_element(By.ID, 'contact_form').is_displayed()
if ele4:
    print("Testcase Passed!")
else:
    print("Testcase Failed")

# Tag Name
ele5 = driver.find_element(By.TAG_NAME, 'h2').is_displayed()
if ele5:
    print("Testcase Passed!")
else:
    print("Testcase Failed")


# Name
ele6 = driver.find_element(By.NAME, 'first_name').is_displayed()
if ele6:
    print("Testcase Passed!")
else:
    print("Testcase Failed")

# Xpath
ele7 = driver.find_element(By.XPATH, '//*[@id="contact_form"]/input[1]').is_displayed()
if ele7:
    print("Testcase Passed!")
else:
    print("Testcase Failed")