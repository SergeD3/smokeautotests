import sys
import time
from selenium.webdriver.common.by import *
from datetime import datetime
from pathlib import Path

date = datetime.today().strftime('%m-%d-%y %H-%M-%S')
filename = 'TestFullPage_' + date + ".png"
path = Path(Path.home(), 'Desktop', 'screenshots_smoke', filename)


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, user_name, pass_word):
        wd = self.app.wd
        wd.set_window_size(1366, 768)
        full_body = wd.find_element(By.TAG_NAME, "body")
        wd.find_element(By.NAME, "login").clear()
        wd.find_element(By.NAME, "login").send_keys(user_name)
        wd.find_element(By.NAME, "password").clear()
        wd.find_element(By.NAME, "password").send_keys(pass_word)
        wd.find_element(By.XPATH, "//button[@type='submit']").click()
        wd.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(3)
        # пытаемся обработать исключения, если они есть
        try:
            # проверка на наличие проблем со входом
            assert len(full_body.find_elements(By.XPATH, ".//div[@class='alertify-notifier ajs-bottom ajs-right']")) == 0 \
                and wd.current_url == 'http://192.168.124.56/#project/', 'we have some problem with auth'
        except Exception as ex:
            print('Problem: ' + '\n', ex)
            wd.find_element(By.TAG_NAME, 'body').screenshot(str(path))
            sys.exit()
        else:
            wd.find_element(By.TAG_NAME, 'body').screenshot(str(path))
            time.sleep(2)

    def logout(self):
        wd = self.app.wd
        wd.find_element(By.ID, 'project-menu').click()
        wd.find_element(By.XPATH, '//*[@id="project-menu"]/ul/li[8]/a').click()