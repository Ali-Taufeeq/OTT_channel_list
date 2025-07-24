import time

import pytest
from selenium import webdriver

from Page_object.Page3 import Channel_Table
from Page_object.Page1 import News_drop
from Page_object.Page2 import Live_tv


@pytest.mark.usefixtures("browser")
class TestLogin_001:

    def test_sign_btn(self):
        click_sign =News_drop(self.driver)
        click_sign.news_dropdown()

    def test_credential(self):
        credit = Live_tv(self.driver)
        credit.Badi_khabar()

    def test_channels(self):
        channel_list = Channel_Table(self.driver)
        channel_list.channel_guide()












