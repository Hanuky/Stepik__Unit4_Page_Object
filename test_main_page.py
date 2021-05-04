import pytest
from selenium import webdriver
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.base_page import BasePage
from .pages.basket_page import BasketPage
"""
def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current.url)
    login_page.should_be_login_page
def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()
"""    
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):    
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link) 
    page.open()
    page.guest_shoul_be_see_basket_button_on_main_page()
    page.guest_shoul_be_clik_on_basket_button()
    basket = BasketPage(browser, link)
    basket.should_be_not_see_success_message_in_empty_basket()
    basket.should_be_see_message_basket_empty()