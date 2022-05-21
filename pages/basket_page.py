from pages.base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):

    def go_to_basket(self):
        button_go_to_basket = self.browser.find_element(*BasketPageLocators.GO_TO_BASKET_BUTTON)
        button_go_to_basket.click()


