import config, time
from src.locators.subscribe_locators import SubscribeLocators
from src.ui import WebUI
from selenium.webdriver.common.keys import Keys


class Subscribe(WebUI):

    locators = SubscribeLocators()

    def search_group(self, group_name=None):
        group_name = group_name or config.group_name
        self.send_data_to_field(locator=self.locators.search_input, data=group_name)
        time.sleep(5)
        group_a = self.driver.find_elements(
            self.locators.searched_group_a[0], self.locators.searched_group_a[1].format(group_name)
        )
        self.wait_button_and_click(button=group_a[0])


    def open_followers_win(self):
        self.wait_button_and_click(button_locator=self.locators.followers_a)
        self.wait.wait_present_all_element_located(self.locators.followers_btns)


    def check_error_message(self):
        flag = False
        error_header_h3 = self.driver.find_elements(*self.locators.error_header_h3)
        if len(error_header_h3) > 0:
            self.wait_button_and_click(button_locator=self.locators.error_modal_ok_btn)
            flag = True
        return flag



    def repeat_subscribe_click(self, button, time_out):
        if button.is_enabled():
            try:
                self.wait_button_and_click(button=button)
                res = self.check_error_message()
                if res:
                    time.sleep(time_out)
            except Exception:
                return False
            if button.text == "Follow":
                try:
                    self.wait_button_and_click(button=button)
                    if button.text == "Follow":
                        res = self.check_error_message()
                        if res:
                            time.sleep(time_out)
                        return False
                except Exception:
                    time.sleep(time_out)


    def subscribe_followers(self, time_out):
        #all_btns = self.driver.find_elements(*self.locators.followers_btns)
        follow_btns = self.driver.find_elements(*self.locators.follow_btns)
        while len(follow_btns) == 0:
            #all_btns[-1].send_keys(Keys.PAGE_DOWN)
            self.driver.execute_script("document.querySelector('.isgrP').scrollTop = document.querySelector('.isgrP').scrollHeight;")
            follow_btns = self.driver.find_elements(*self.locators.follow_btns)
            #all_btns = self.driver.find_elements(*self.locators.followers_btns)
        for i in range(len(follow_btns)):
            self.repeat_subscribe_click(button=follow_btns[i], time_out=time_out)
        self.subscribe_followers(time_out=time_out)
