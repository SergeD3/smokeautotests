# -*- coding: utf-8 -*-
import time
from selenium import webdriver
from selenium.webdriver.common.by import *
from fixture.session import SessionHelper
from fixture.users import UserHelper


class Aplcs:

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.headless = True
        self.wd = webdriver.Chrome('C:/Users/Серж/PycharmProjects/smokeautotests/chromedriver/chromedriver.exe',
                                   options=options
                                   )
        self.wd.implicitly_wait(10)
        self.session = SessionHelper(self)
        self.users = UserHelper(self)

    def open_page(self):
        wd = self.wd
        wd.get(url="http://192.168.124.56/#login")
        time.sleep(1)

    def destroy(self):
        wd = self.wd
        wd.quit()
