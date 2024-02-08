import pytest
# from selenium import  webdriver
#
# # we can not create objec
#
# driver= webdriver.Chrome()
# driver.get("")
#
# # def test_script():
# ---------------------------------------------------
# pip install selenium
# pip install webdriver-manager
# pip install pytest
# py.test
# pytest -v
# file name shoud have "test" as prefix or suffix
# test case should start with word "test"
# pytest.mark.login
# pytest -m "login"


def test_less():
    number = 100
    assert  number < 100

def test_less_equal():
    number = 100
    assert number <= 100

def test_name():
    first_name = "shivani"
    assert  first_name == "shivani"
