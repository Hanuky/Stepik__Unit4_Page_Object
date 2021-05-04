import time
import pytest
from selenium import webdriver
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.base_page import BasePage
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage


class TestUserAddToBasketFromProductPage():
    
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"   
        email = str(time.time()) + "@fakemail.org"
        password = "q123456qwerty"  
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()
    
    def test_user_cant_see_success_message(self, browser):     
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"   
        page = ProductPage(browser, link)
        page.open()
        page.guest_should_not_be_success_message()
    
    @pytest.mark.need_review    
    def test_user_can_add_product_to_basket(self, browser): 
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"   
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket()
        page.check_success_message_after_add_product()
        page.check_price_equals_basket_price()
        page.check_product_name_equals_product_basket_name()

@pytest.mark.xfail   
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"   
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.guest_should_not_be_success_message()

@pytest.mark.xfail    
def test_message_disappeared_after_adding_product_to_basket(browser):     
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"   
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.success_message_should_be_disappeared()

@pytest.mark.need_review    
def test_guest_can_add_product_to_basket(browser): 
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"   
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.check_success_message_after_add_product()
    page.check_price_equals_basket_price()
    page.check_product_name_equals_product_basket_name()

@pytest.mark.need_review     
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    login_page = LoginPage(browser, link)
    login_page.go_to_login_page()
    login_page.should_be_login_page()    

def test_guest_cant_see_success_message(browser):     
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"   
    page = ProductPage(browser, link)
    page.open()
    page.guest_should_not_be_success_message()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review    
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"   
    page = ProductPage(browser, link)
    page.open()
    page.guest_should_be_see_basket_button_on_main_page()
    page.guest_should_be_clik_on_basket_button()
    basket = BasketPage(browser, link)
    basket.not_see_success_message_in_empty_basket()
    basket.should_be_message_basket_empty()          
    