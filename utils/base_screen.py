# ==========================
#  Basic page
# ==========================
import sys

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

ELEMENT_DISPLAY_TIMER = 20
ENTER_KEY_EVENT = 66


class BaseScreen:
    def __init__(self, driver):
        self.driver = driver
        self.elements = {}
        self.elements_name = {}
        self._user = None
        self._logger = None
        self._screenshot_path = "../reports/screenshots/"
        self.device_width = self.driver.get_window_size()['width']
        self.device_height = self.driver.get_window_size()['height']

    def find_element(self, *loc):
        try:
            WebDriverWait(self.driver, ELEMENT_DISPLAY_TIMER).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except Exception as e:
            raise e

    def fetch_elements_name(self, *loc):
        try:
            WebDriverWait(self.driver, ELEMENT_DISPLAY_TIMER).until(EC.visibility_of_element_located(loc))
            self.elements = self.driver.find_elements(*loc)
            if self.elements == None:
                return None
            for i in range(self.elements.__len__()):
                element_name_tmp = self.elements[i].text
                if element_name_tmp != None:
                    self.elements_name[i] = element_name_tmp
                else:
                    sys.stdout.write("STDOUT: find search result name is null. \n")
            return self.elements_name
        except Exception as e:
            raise e

    def find_clickable_element(self, *loc):
        try:
            WebDriverWait(self.driver, ELEMENT_DISPLAY_TIMER).until(EC.element_to_be_clickable(loc))
            return self.driver.find_element(*loc)
        except Exception as e:
            raise e

    def find_the_specific_clickable_element(self, index, *loc):
        try:
            WebDriverWait(self.driver, ELEMENT_DISPLAY_TIMER).until(EC.element_to_be_clickable(loc))
            self.elements = self.driver.find_elements(*loc)
            if self.elements == None:
                return None
            for i in range(self.elements.__len__()):
                if index == i:
                    return self.elements[index]
            self.fail("STDOUT:basepage === Can't find specific tapable element, index is %d. \n" % index)
        except Exception as e:
            raise e

    def find_first_element_name(self, *loc):
        try:
            WebDriverWait(self.driver, ELEMENT_DISPLAY_TIMER).until(EC.element_to_be_clickable(loc))
            self.elements = self.driver.find_elements(*loc)
            if self.elements == None:
                return None
            return self.elements[0].get_attribute("text")
        except Exception as e:
            raise e

    def send_keys(self, value, *loc):
        try:
            self.find_element(*loc).clear()
            self.find_element(*loc).send_keys(value)
        except AttributeError as e:
            raise e

    def is_element_found(self, *loc):
        try:
            WebDriverWait(self.driver, ELEMENT_DISPLAY_TIMER).until(EC.visibility_of_element_located(loc))
            return True
        except TimeoutException:
            return False

    def is_clickable_element_found(self, *loc):
        try:
            WebDriverWait(self.driver, ELEMENT_DISPLAY_TIMER).until(EC.element_to_be_clickable(loc))
            return True
        except TimeoutException:
            return False

    def send_enter_key(self):
        try:
            self.driver.keyevent(ENTER_KEY_EVENT)
        except Exception as e:
            raise e

    def save_screenshot(self, name):
        self.driver.save_screenshot(name)

    def wait_for_visible(self, *loc):
        try:
            WebDriverWait(self.driver, ELEMENT_DISPLAY_TIMER).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except Exception as e:
            raise e

    def wait_for_not_visible(self, *loc):
        try:
            WebDriverWait(self.driver, ELEMENT_DISPLAY_TIMER).until(EC.invisibility_of_element(*loc))
            return self.driver.find_element(*loc)
        except Exception as e:
            raise e
