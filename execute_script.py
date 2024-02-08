# click --- selenium ??
# scroll --- selenium ??
# getAttibute --- selenium ??

import time
from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
driver = webdriver.Chrome()
driver.get('https://webdriveruniversity.com/')

# pract_1
# ele = driver.find_element(By.ID,"contact-us")
# # ele.click() #---- maximum time element not found properly that time we convert python selenium into javascript.

# driver.execute_script("arguments[0].click()",ele)
# time.sleep(5)

# pract_2
# ele2 = driver.find_element(By.ID,"popup-alerts")
# driver.execute_script("arguments[0].scrollIntoView(true)",ele2)
# time.sleep(5)


# pract_3
# title = driver.execute_script("return document.title")
# if title == "WebDriverUniversity.com":
#     print("Test case pass")
# else:
#     print("Test case fail")
# driver.close()

# pract_4
e = driver.find_element(By.ID,"popup-alerts")
driver.execute_script("arguments[0].setAttribute('data-cy','two')",e)
time.sleep(20)




# driver.quit()
