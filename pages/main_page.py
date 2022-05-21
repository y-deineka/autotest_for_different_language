from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from .locators import MainPageLocators
from .login_page import LoginPage


class MainPage(BasePage):

    def go_to_login_page(self):
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()

    def should_be_login_link(self):
        assert self.browser.find_element(*MainPageLocators.LOGIN_LINK), "Login link is not presented"




