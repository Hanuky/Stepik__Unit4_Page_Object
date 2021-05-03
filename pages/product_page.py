from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
from .login_page import LoginPage

class ProductPage(BasePage):

    PAGE_SLUG = '/?promo=newYear'

    def add_product_promo_in_basket(self):
        add_basket = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        add_basket.click()
    def chek_success_message_after_add_product(self):
        assert self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is nor presented"
    def should_be_promo_url(self): 
        assert self.PAGE_SLUG in self.browser.current_url, "Product promo page url is wrong"    