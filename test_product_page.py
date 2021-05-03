import pytest
from selenium import webdriver
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.base_page import BasePage
from .pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_promo_url()
    page.add_product_promo_in_basket()
    page.solve_quiz_and_get_code()
    page.chek_success_message_after_add_product()