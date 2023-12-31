from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_URL = (By.CSS_SELECTOR, "#login_url")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class AddGoodToBasket():
    BTN_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    GOOD_TITLE = (By.CSS_SELECTOR, '.product_main h1')
    GOOD_TITLE_IN_BASKET = (By.CSS_SELECTOR, '.alert-success .alertinner strong')
    BTN_VIEW_BASKET = (By.XPATH, '//*[@id="default"]/header/div[1]/div/div[2]/span/a')
    GOOD_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    TOTAL_PRICE = (By.CSS_SELECTOR, '.alert-info .alertinner strong')
    PROMO_BANNER = (By.XPATH, '//div[@id="messages"]/div[1]/div/strong')
    MSG_SUCCESS = (By.XPATH, '//div[@id="messages"]/div[1]')
    PRODUCT_ADD_TO_CARD_MESSAGE = (By.CSS_SELECTOR, '.alert-info .alertinner')


class BasePageLocators():
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class BasketPageLocators():
    GOOD_ITEMS = (By.ID, 'basket_formset')
    BASKET_EMPTY = (By.XPATH, '//div[@id="content_inner"]/p')
