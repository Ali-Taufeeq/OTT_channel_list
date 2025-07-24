import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Live_tv:
    def __init__(self,driver):
        self.driver = driver
        self.genre = (By.CLASS_NAME,"subscriptionBanner_widgetTitle__M3keA")

    def Badi_khabar(self):
        time.sleep(5)
        self.driver.find_element(*self.genre).click()
