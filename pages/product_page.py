from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):

    def add_to_basket(self):
        button_add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        button_add_to_basket.click()

    def should_be_see_confirm(self):
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME)
        approve_buy = self.browser.find_element(*ProductPageLocators.APPROVE_NAME)

        assert book_name.text in approve_buy.text, f'В тексте {approve_buy} нет названия {book_name}'

        price = self.browser.find_element(*ProductPageLocators.PRICE)
        approve_price = self.browser.find_element(*ProductPageLocators.APPROVE_PRICE)

        assert price.text in approve_price.text, f'В тексте {approve_price} нет цены {price}'
