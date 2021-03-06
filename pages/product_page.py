from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):


    PAGE_SLUG = '/?promo=newYear'

    def check_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def check_product_basket_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_BASKET_NAME).text

    def check_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRICE).text

    def check_product_price_in_basket(self):
        return self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text

    def add_product_to_basket(self):
        add_basket = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        add_basket.click()

    def check_success_message_after_add_product(self):
        assert self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is not presented"

    def should_be_promo_url(self):
        assert self.PAGE_SLUG in self.browser.current_url, "Product promo page url is wrong"

    def check_price_equals_basket_price(self):
        assert self.check_product_price() == self.check_product_price_in_basket(), "Product price and product price in basket not equals"

    def check_product_name_equals_product_basket_name(self):
        assert self.check_product_name() == self.check_product_basket_name(), "Product name and product name in basket not equals"

    def guest_should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented"

    def success_message_should_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented"
