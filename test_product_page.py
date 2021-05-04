import pytest
from selenium import webdriver
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.base_page import BasePage
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage

"""
@pytest.mark.parametrize('number_link', ["offer0", "offer1", "offer2", "offer3", "offer4", "offer5", "offer6", pytest.param("offer7", marks=pytest.mark.xfail), "offer8", "offer9"])
def test_guest_can_add_product_to_basket(browser, number_link):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo={number_link}"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_in_basket()
    page.solve_quiz_and_get_code()
    page.chek_success_message_after_add_product()
    page.chek_price_equals_basket_price()
    page.chek_product_name_equal_product_basket_name()
@pytest.mark.xfail   
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"   
    page = ProductPage(browser, link)
    page.open()
    page.add_product_in_basket()
    page.guest_should_not_be_success_message()
def test_guest_cant_see_success_message(browser):     
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"   
    page = ProductPage(browser, link)
    page.open()
    page.guest_should_not_be_success_message()
@pytest.mark.xfail    
def test_message_disappeared_after_adding_product_to_basket(browser):     
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"   
    page = ProductPage(browser, link)
    page.open()
    page.add_product_in_basket()
    page.guest_should_disappeared_be_success_message()
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()   
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    login_page = LoginPage(browser, link)
    login_page.go_to_login_page()
    login_page.should_be_login_page()
"""    
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"   
    page = ProductPage(browser, link)
    page.open()
    page.guest_shoul_be_see_basket_button_on_main_page()
    page.guest_shoul_be_clik_on_basket_button()
    basket = BasketPage(browser, link)
    basket.should_be_not_see_success_message_in_empty_basket()
    basket.should_be_see_message_basket_empty()
