import config
from src.locators.login_locators import LoginLocators
from src.ui import WebUI

class Login(WebUI):

    locators = LoginLocators()

    def login(self, email=None, password=None):
        email = email or config.email
        password = password or config.password
        self.send_data_to_field(locator=self.locators.user_name_input, data=email)
        self.send_data_to_field(locator=self.locators.password_input, data=password)
        self.wait_button_and_click(button_locator=self.locators.login_btn)
