# -*- coding: utf-8 -*-
import time
from selenium import webdriver
from fixture.session import SessionHelper
from fixture.users import UserHelper
from pathlib import Path

path = Path(Path.home(), 'PycharmProjects', 'smokeautotests', 'chromedriver', 'chromedriver.exe')


class Aplcs:

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.headless = False
        self.wd = webdriver.Chrome(path, options=options)
        self.wd.implicitly_wait(15)
        self.session = SessionHelper(self)
        self.users = UserHelper(self)

    def open_page(self):
        wd = self.wd
        wd.get(url="http://192.168.124.56/#login")
        wd.set_window_size(1366, 768)

    def destroy(self):
        wd = self.wd
        wd.quit()
