from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')

class ProductPageLocators():
    ADD_TO_BASKET = (By.ID, 'add_to_basket_form')
    BOOK_NAME = (By.TAG_NAME, 'h1')
    APPROVE_NAME = (By.XPATH, '//*[@id="messages"]/div[1]/div')
    PRICE = (By.CSS_SELECTOR, 'p.price_color')
    APPROVE_PRICE = (By.XPATH, '//*[@id="messages"]/div[3]/div/p[1]/strong')

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class BasketPageLocators():
    GO_TO_BASKET_BUTTON = (By.XPATH, '//*[@id="default"]/header/div[1]/div/div[2]/span/a')

