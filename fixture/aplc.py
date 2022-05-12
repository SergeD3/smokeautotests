# -*- coding: utf-8 -*-
from selenium import webdriver
from fixture.session import SessionHelper
from fixture.users import UserHelper
from pathlib import Path

path = Path(Path.home(), 'PycharmProjects', 'smokeautotests', 'chromedriver', 'chromedriver.exe')


class Aplcs:

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.headless = True
        self.wd = webdriver.Chrome(path, options=options)
        self.wd.implicitly_wait(10)
        self.session = SessionHelper(self)
        self.users = UserHelper(self)

    def open_page(self, page_link):
        wd = self.wd
        wd.get(url=page_link)
        wd.set_window_size(1366, 768)

    def destroy(self):
        wd = self.wd
        wd.quit()
