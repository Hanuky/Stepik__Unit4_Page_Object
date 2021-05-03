from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")   
    REGISTER_FROM = (By.CSS_SELECTOR, "#registr_form")  

class ProductPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")   
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div .alert-success .alertinner strong") 