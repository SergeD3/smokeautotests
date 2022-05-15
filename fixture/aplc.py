# -*- coding: utf-8 -*-
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

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
        self.wd.set_page_load_timeout(40)
        self.session = SessionHelper(self)
        self.users = UserHelper(self)

    def open_page(self, page_link):
        wd = self.wd
        wd.get(url=page_link)
        wd.set_window_size(1366, 768)

    def destroy(self):
        wd = self.wd
        wd.quit()

    def take_screen(self, _path):
        wd = self.wd
        time.sleep(3)
        wd.find_element(By.TAG_NAME, 'body').screenshot(str(_path))
