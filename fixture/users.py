# -*- coding: utf-8 -*-
import time

from selenium.webdriver.common.by import *
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait as ww
from pathlib import Path
from datetime import datetime


date = datetime.today().strftime('%m-%d-%y %H-%M-%S')
filename = 'TestFullPage_' + date + ".png"
path = Path(Path.home(), 'Desktop', 'screenshots_smoke', filename)


class UserHelper:

    def __init__(self, app):
        self.app = app

    def open_create_window(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, u"//a[contains(text(),'Пользователь')]").click()
        wd.find_element(By.XPATH, "//button[@title = 'Создать']").click()

    def fill_users_form(self, user):
        wd = self.app.wd
        # ниже пытаюсь получить родительский элемент обёртки и все дочерние div и input
        ww(wd, 30).until(ec.element_to_be_clickable((By.XPATH, "//div[@class='modals-wrapper']")))
        modalcontainer = wd.find_element(By.XPATH, "//div[@class='modals-wrapper']")
        modaldialog = modalcontainer.find_element(By.XPATH, ".//div[@class='modal-dialog']")
        modalcontent = modaldialog.find_element(By.XPATH, "//div[@class='modal-content ui-draggable "
                                                          "ui-draggable-handle']"
                                                )
        modalbody = modalcontent.find_element(By.XPATH, "//div[@class='modal-body ']")
        try:
            # получаем поле Название и прокидываем в него данные из теста
            input_name = modalbody.find_element(By.XPATH, "//input[@placeholder='Название']")
            input_name.click()
            input_name.clear()
            input_name.send_keys(user.uname)
            # получаем поле Логин и прокидываем в него данные из теста
            input_login = modalbody.find_element(By.XPATH, "//input[@placeholder='Логин']")
            input_login.click()
            input_login.clear()
            input_login.send_keys(user.ulogin)
            # получаем поле Е-мейл и прокидываем в него данные из теста
            input_email = modalbody.find_element(By.XPATH, "//input[@placeholder='E-мейл']")
            input_email.click()
            input_email.clear()
            input_email.send_keys(user.uemail)
            # получаем поле Телефон и прокидываем в него данные из теста
            input_phone = modalbody.find_element(By.XPATH, "//input[@placeholder='Телефон']")
            input_phone.click()
            input_phone.clear()
            input_phone.send_keys(user.uphone)
            # жмакаем на Создать
            modalbody.find_element(By.XPATH, "//button[@class='btn btn-success  js-ok ']").click()
        except Exception as ex:
            print(ex)
        finally:
            time.sleep(2)
            wd.find_element_by_tag_name('body').screenshot(str(path))

    def check_usergroup(self):
        wd = self.app.wd
        wd.get('http://192.168.124.56/#user/127/edit')
        ww(wd, 30).until(ec.presence_of_all_elements_located((
            By.XPATH, '//*[@id="project-main-region"]/div/div[2]/div/div/div[2]/div/div[3]')))
        wd.find_element(By.XPATH, '//*[@id="project-main-region"]/div/div[2]/div/div/div[2]/div/div[3]').click()

