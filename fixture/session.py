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
        time.sleep(1)

    def logout(self):
        wd = self.app.wd
        wd.find_element(By.ID, 'project-menu').click()
        wd.find_element(By.XPATH, '//*[@id="project-menu"]/ul/li[8]/a').click()
        time.sleep(3)