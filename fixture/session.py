import sys
import time

from selenium.webdriver.common.by import *
from datetime import datetime
from pathlib import Path
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

date = datetime.today().strftime('%m-%d-%y %H-%M-%S')
filename = 'TestFullPage_' + date + ".png"
path = Path(Path.home(), 'Desktop', 'screenshots_smoke', filename)


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, user_name, pass_word):
        wd = self.app.wd
        WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.NAME, "login")))
        full_body = wd.find_element(By.TAG_NAME, "body")
        wd.find_element(By.NAME, "login").clear()
        wd.find_element(By.NAME, "login").send_keys(user_name)
        wd.find_element(By.NAME, "password").clear()
        wd.find_element(By.NAME, "password").send_keys(pass_word)
        wd.find_element(By.XPATH, "//button[@type='submit']").click()
        wd.find_element(By.XPATH, "//button[@type='submit']").click()
        # пытаемся обработать исключения, если они есть
        try:
            # проверка на наличие проблем со входом
            print('до ожидания...')
            time.sleep(1)
            WebDriverWait(wd, 20).until(EC.element_to_be_clickable((
                By.XPATH, "//li[@title='Пользователь']"
            )))
            print('после')
            assert wd.current_url == 'http://192.168.124.56/#project/', 'wrong page'
            assert len(full_body.find_elements(
                By.XPATH, "//div[@class='alertify-notifier ajs-bottom ajs-right']")) == 0, 'we have some ' \
                                                                                           'problem with auth(ban)'
        except Exception as ex:
            print(ex)
            sys.exit()
        except TimeoutError:
            print('Timeout error, bro')
        finally:
            wd.find_element(By.TAG_NAME, 'body').screenshot(str(path))

    def logout(self):
        wd = self.app.wd
        wd.find_element(By.ID, 'project-menu').click()
        WebDriverWait(wd, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="project-menu"]/ul/li[8]/a')))
        wd.find_element(By.XPATH, '//*[@id="project-menu"]/ul/li[8]/a').click()
