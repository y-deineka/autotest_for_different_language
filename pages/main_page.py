from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MainPage(BasePage):

    def go_to_login_page(self):
        browser = self.browser
        login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()

    def should_be_login_link(self):
        self.browser.find_element(By.CSS_SELECTOR, "#login_link_invalid")
