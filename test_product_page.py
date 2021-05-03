import pytest
from selenium import webdriver
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.base_page import BasePage
from .pages.product_page import ProductPage

@pytest.mark.parametrize('number_link', ["offer0", "offer1", "offer2", "offer3", "offer4", "offer5", "offer6", pytest.param("offer7", marks=pytest.mark.xfail), "offer8", "offer9"])
def test_guest_can_add_product_to_basket(browser, number_link):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo={number_link}"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_promo_in_basket()
    page.solve_quiz_and_get_code()
    page.chek_success_message_after_add_product()
    page.chek_price_equals_basket_price()
    page.chek_product_name_equal_product_basket_name()