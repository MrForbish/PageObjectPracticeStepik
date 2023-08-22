from .base_page import BasePage
from .locators import BasketPageLocators, AddGoodToBasket


class BasketPage(BasePage):
    def check_goods_exists(self):
        assert self.is_element_present(*BasketPageLocators.GOOD_ITEMS), "Basket empty"

    def check_basket_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY), "Goods exists"

    def add_good_to_basket(self):
        self.browser.find_element(*AddGoodToBasket.BTN_TO_BASKET).click()
