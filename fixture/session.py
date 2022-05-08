import time
from selenium.webdriver.common.by import *


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, user_name, pass_word):
        wd = self.app.wd
        wd.find_element(By.NAME, "login").clear()
        wd.find_element(By.NAME, "login").send_keys(user_name)
        wd.find_element(By.NAME, "password").clear()
        wd.find_element(By.NAME, "password").send_keys(pass_word)
        wd.find_element(By.XPATH, "//button[@type='submit']").click()
        wd.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(2)

    def logout(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, 'Smoke_autotest robot').click()
        wd.find_element(By.LINK_TEXT, 'Выйти').click()
        time.sleep(5)