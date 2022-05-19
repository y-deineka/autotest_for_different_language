import time

def test_guest_should_see_buy_button(browser):

    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    #time.sleep(30)                                   #Уберите знак "#" в начале строки, чтобы активировать задержку


    button_add_to_basket = browser.find_elements_by_id("add_to_basket_form")

    assert button_add_to_basket, 'Такой кнопки на странице нет'