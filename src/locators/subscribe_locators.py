from selenium.webdriver.common.by import By

class SubscribeLocators:

    search_input = (By.XPATH, "//input[@placeholder='Search']")
    searched_group_a = (By.XPATH, "//div/a[contains(@href, '{0}')]")
    followers_a = (By.XPATH, "//li/a[contains(@href, 'followers')]")
    followers_btns = (By.XPATH, "//h1[text()='Followers']/../../..//li//button")
    followers_list_ul = (By.XPATH, "//h1[text()='Followers']/../../..//ul")
    follow_h1 = (By.XPATH, "//h1[text()='Followers']")
    follow_btns = (By.XPATH, "//li//button[text()='Follow']")
    error_header_h3 = (By.XPATH, "//*[text()='Action Blocked']")
    error_modal_ok_btn = (By.XPATH, "//*[text()='Action Blocked']/../..//button[text()='OK']")