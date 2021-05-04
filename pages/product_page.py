from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
from .login_page import LoginPage
from .locators import MainPageLocators


class ProductPage(BasePage):

    PAGE_SLUG = '/?promo=newYear'

    def chek_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
    
    def chek_product_basket_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_BASKET_NAME).text
    
    def chek_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRICE).text 
    
    def chek_product_price_in_basket(self):
        return self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text           
    
    def add_product_in_basket(self):
        add_basket = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        add_basket.click()
    
    def chek_success_message_after_add_product(self):
        assert self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is nor presented"
    
    def should_be_promo_url(self): 
        assert self.PAGE_SLUG in self.browser.current_url, "Product promo page url is wrong" 
    
    def chek_price_equals_basket_price(self):
        assert self.chek_product_price() == self.chek_product_price_in_basket(), "Product price or product price in basket not equals"
    
    def chek_product_name_equal_product_basket_name(self): 
        assert self.chek_product_name() == self.chek_product_basket_name(), "Product name or product name in basket not equals" 
   
    def guest_should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented"
   
    def guest_should_disappeared_be_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented"
        