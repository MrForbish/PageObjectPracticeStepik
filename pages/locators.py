from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_URL = (By.CSS_SELECTOR, "#login_url")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class AddGoodToBasket():
    BTN_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    GOOD_TITLE = (By.XPATH, "//*[@id='content_inner']/article/div[1]/div[2]/h1")
    GOOD_TITLE_IN_BASKET = (By.XPATH, '//*[@id="basket_formset"]/div/div/div[2]/h3/a')
    BTN_VIEW_BASKET = (By.XPATH, '//*[@id="default"]/header/div[1]/div/div[2]/span/a')
    GOOD_PRICE = (By.XPATH, '//div[@id="content_inner"]/article/div[1]/div[2]/p[1]')
    TOTAL_PRICE = (By.XPATH, '//div[@id="basket_totals"]/table/tbody/tr[10]/td/h3')
