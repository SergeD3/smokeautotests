# -*- coding: utf-8 -*-
import time
from selenium import webdriver
from selenium.webdriver.common.by import *


class Aplcs:

    def __init__(self):
        self.wd = webdriver.Chrome('C:/Users/Серж/PycharmProjects/smokeautotests/chromedriver/chromedriver.exe')
        self.wd.implicitly_wait(30)

    def open_page(self):
        wd = self.wd
        wd.get(url="http://192.168.124.56/#login")
        time.sleep(2)

    def login(self, user_name, pass_word):
        wd = self.wd
        wd.find_element(By.NAME, "login").clear()
        wd.find_element(By.NAME, "login").send_keys(user_name)
        wd.find_element(By.NAME, "password").clear()
        wd.find_element(By.NAME, "password").send_keys(pass_word)
        wd.find_element(By.XPATH, "//button[@type='submit']").click()
        wd.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(2)

    def logout(self):
        wd = self.wd
        wd.find_element(By.LINK_TEXT, 'Smoke_autotest robot').click()
        wd.find_element(By.LINK_TEXT, 'Выйти').click()
        time.sleep(5)

    def destroy(self):
        wd = self.wd
        wd.quit()
