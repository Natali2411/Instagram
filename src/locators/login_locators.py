from selenium.webdriver.common.by import By

class LoginLocators:

    user_name_input = (By.NAME, "username")
    password_input = (By.NAME, "password")
    login_btn = (By.XPATH, "//button[@type='submit']")