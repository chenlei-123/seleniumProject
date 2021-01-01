import selenium
from selenium import webdriver
import time


def test_selenium():
    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com")
    time.sleep(4)
