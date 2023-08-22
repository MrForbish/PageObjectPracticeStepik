import time
import pytest

from .pages.product_page import ProductPage
from .pages.base_page import BasePage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage


# @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                                   pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
# @pytest.mark.need_review
# def test_guest_can_add_product_to_basket(browser, link):
#     page = ProductPage(browser, link)
#     page.open()
#     page.add_good_to_basket()  # добавляем товар в корзину
#     BasePage.solve_quiz_and_get_code(page)
#     assert page.promo_banner_is_correct(), f'Ссылка {link} некорректна'
#
#     good_title = page.get_good_title()  # получаем название товара
#     good_price = page.get_good_price()  # получаем цену товара
#
#     page.open_basket()  # переходим в корзину
#
#     total_price = page.get_total_price()  # получаем цену товара в корзине
#     good_title_in_basket = page.get_good_title_in_basket()  # получаем название товара в корзине
#     assert good_title == good_title_in_basket, f"Good was not added to cart"
#     assert good_price == total_price, f"Price varies!"
#
#
# def test_guest_should_see_login_link_on_product_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_be_login_link()
#
#
# @pytest.mark.need_review
# def test_guest_can_go_to_login_page_from_product_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.go_to_login_page()
#
#
# @pytest.mark.need_review
# def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
#     page = BasketPage(browser, link)
#     page.open()
#     # page.add_good_to_basket() можно добавить товар и проверить с товаром в корзине
#     page.open_basket()
#     page.check_basket_empty()
#     page.check_goods_exists()


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        email = str(time.time()) + "@fakemail.org"
        password = '123456gfaqq'
        page = LoginPage(browser, link)
        page.open()
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        page = ProductPage(browser, link)
        page.open()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7"
        page = ProductPage(browser, link)
        page.open()
        page.add_good_to_basket()
