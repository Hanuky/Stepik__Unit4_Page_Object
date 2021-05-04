from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.browser.current_url in "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/", "Wrong login page url"
    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented" 
    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FROM), "Regiter form is not presented" 
    def register_new_user(self, email, password):   
        registration_email = self.browser.find_element(*LoginPageLocators.INPUT_REGISTRATION_EMAIL)
        registration_email.send_keys(email)
        registration_password = self.browser.find_element(*LoginPageLocators.INPUT_REGISTRATION_PASSWORD)
        registration_password.send_keys(password)
        registration_password_confirm = self.browser.find_element(*LoginPageLocators.INPUT_REGISTRATION_PASSWORD_CONFIRM)
        registration_password_confirm.send_keys(password)
        click_register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        click_register_button.click()