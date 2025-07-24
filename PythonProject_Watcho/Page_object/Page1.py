import time

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class News_drop:
    def __init__(self,driver):
        self.driver = driver
        self.news = (By.LINK_TEXT,"Live TV")
        self.drop_dwm = (By.LINK_TEXT,"Channels")

    def news_dropdown(self):
        time.sleep(10)
        self.driver.find_element(*self.news).click()
        self.driver.find_element(*self.drop_dwm).click()

