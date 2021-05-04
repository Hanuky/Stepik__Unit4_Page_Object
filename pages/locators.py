from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")   
    REGISTER_FROM = (By.CSS_SELECTOR, "#register_form") 
    INPUT_REGISTRATION_EMAIL =  (By.CSS_SELECTOR, "input#id_registration-email") 
    INPUT_REGISTRATION_PASSWORD =  (By.CSS_SELECTOR, "input#id_registration-password1") 
    INPUT_REGISTRATION_PASSWORD_CONFIRM =  (By.CSS_SELECTOR, "input#id_registration-password2") 
    REGISTER_BUTTON = (By.CSS_SELECTOR, "div.register_form button.btn")


class ProductPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")   
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div .alert-success .alertinner strong") 
    PRICE = (By.CSS_SELECTOR, ".product_page .price_color")
    BASKET_PRICE = (By.CSS_SELECTOR, "div .alert-info .alertinner strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, "#content_inner h1")
    PRODUCT_BASKET_NAME = (By.CSS_SELECTOR, "div .alert-success .alertinner strong")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BUSKET_BUTTON = (By.CSS_SELECTOR, ".basket-mini a.btn-default")    
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLokators():
    EMPTY_BASKET_MASSAGE = (By.CSS_SELECTOR, "div#content_inner p")