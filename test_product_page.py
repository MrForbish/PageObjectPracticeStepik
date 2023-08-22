from .pages.product_page import ProductPage
from .pages.base_page import BasePage


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.add_good_to_basket() # добавляем товар в корзину
    BasePage.solve_quiz_and_get_code(page)

    good_title = page.get_good_title() # получаем название товара
    good_price = page.get_good_price() # получаем цену товара

    page.open_basket() # переходим в корзину

    total_price = page.get_total_price() # получаем цену товара в корзине
    good_title_in_basket = page.get_good_title_in_basket() # получаем название товара в корзине
    assert good_title == good_title_in_basket, f"Good was not added to cart"
    assert good_price == total_price, f"Price varies!"

