import logging

import utils.custom_logger as cl
from base.basepage import BasePage


class HomeNavigation(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.homePage_locators = self.pageLocators('HomePage')

    def goToLoginPage(self):
        self.elementClick(*self.locator(self.homePage_locators, 'link_login'))

    def isAt(self):
        header_login = self.getElementList(*self.locator(self.homePage_locators, 'link_login'))
        if len(header_login) > 0:
            return True
        return False
