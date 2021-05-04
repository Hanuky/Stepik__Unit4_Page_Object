from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
from .locators import BasketPageLokators

class BasketPage(BasePage):
    def should_be_not_see_success_message_in_empty_basket(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Basket not empty!!!" 
    def should_be_see_message_basket_empty(self):
        assert self.is_element_present(*BasketPageLokators.EMPTY_BASKET_MASSAGE), "Basket not empty!!!"     

