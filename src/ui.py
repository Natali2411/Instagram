from src.wait import Wait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import *
import time


class WebUI():

    def __init__(self, driver):
        self.driver = driver
        self.wait = Wait(self.driver)


    def move_to_element(self, element):
        action = ActionChains(self.driver)
        action.move_to_element(element)
        action.perform()
        #self.wait_loader_disappear()


    def send_data_to_field(self, element=None, data=None, locator=None):
        if locator:
            self.wait.wait_present_element_located(locator)
            element = self.driver.find_element(*locator)
            self.move_to_element(element=element)
            element.clear()
            element.send_keys(data)
        else:
            self.move_to_element(element=element)
            element.clear()
            element.send_keys(data)


    def wait_button_and_click(self, button_locator=None, button=None):
        # self.wait_loader_disappear()
        if button:
            self.move_to_element(element=button)
            self.wait.wait_until_element_visible(element=button)
        elif button_locator:
            self.wait.wait_present_element_located(button_locator)
            self.wait.wait_until_element_clickable(button_locator)
            button = button or self.driver.find_element(*button_locator)
            self.move_to_element(element=button)
        try:
            button.click()
        except WebDriverException:
            self.driver.execute_script("arguments[0].click();", button)
        #self.wait_loader_disappear()
        time.sleep(2)