import time


class UserHelper:

    def __init__(self, app):
        self.app = app

    def open_create_user(self):
        wd = self.app.wd
        wd.find_element_by_xpath(u"//a[contains(text(),'Пользователь')]").click()
        time.sleep(1)
        wd.find_element_by_xpath("//div[@id='project-main-region']/div/div[2]/div/div/div[2]/div/div/div["
                                 "2]/div/button[2]/span").click()
        # wd.find_element_by_id("name-view1021").click()
        # wd.find_element_by_id("name-view1021").clear()
        # wd.find_element_by_id("name-view1021").send_keys("some_name")
        # wd.find_element_by_id("login-view1030").clear()
        # wd.find_element_by_id("login-view1030").send_keys("some_login")
        # wd.find_element_by_id("email-view1039").click()
        # wd.find_element_by_id("email-view1039").clear()
        # wd.find_element_by_id("email-view1039").send_keys("some_email@email.ru")
        # wd.find_element_by_id("phone-view1048").click()
        # wd.find_element_by_id("phone-view1048").clear()
        # wd.find_element_by_id("phone-view1048").send_keys("777777777777")
        # wd.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='Отменить'])["
        #                          u"1]/following::button[1]").click()
        time.sleep(1)