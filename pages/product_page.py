from .base_page import BasePage
from .locators import AddGoodToBasket


class ProductPage(BasePage):
    def add_good_to_basket(self):
        self.browser.find_element(*AddGoodToBasket.BTN_TO_BASKET).click()

    def get_good_title(self):
        good_title = self.browser.find_element(*AddGoodToBasket.GOOD_TITLE).text
        return good_title

    def get_good_title_in_basket(self):
        good_title_in_basket = self.browser.find_element(*AddGoodToBasket.GOOD_TITLE_IN_BASKET).text
        return good_title_in_basket

    def get_good_price(self):
        good_price = self.browser.find_element(*AddGoodToBasket.GOOD_PRICE).text
        return good_price

    def get_total_price(self):
        total_price = self.browser.find_element(*AddGoodToBasket.TOTAL_PRICE).text
        return total_price

    def open_basket(self):
        self.browser.find_element(*AddGoodToBasket.BTN_VIEW_BASKET).click()

    def should_be_button_basket(self):
        assert self.is_element_present(*AddGoodToBasket.BTN_TO_BASKET), "Button basket is not presented"
