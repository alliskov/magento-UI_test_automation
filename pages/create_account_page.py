from pages.locators import create_account_page_locators as locators
from pages.base_page import BasePage
from typing import Literal
from faker import Faker


class CreateAccount(BasePage):
    page_url = '/customer/account/create'
    first_name = None
    last_name = None
    email = None
    password = None
    confirm_password = None

    def fulfill_registration_form(self,
                                  first_name=None,
                                  last_name=None,
                                  email=None,
                                  password=None,
                                  confirm_password=None):
        self.first_name = first_name if first_name else Faker().first_name()
        self.last_name = last_name if last_name else Faker().last_name()
        self.email = email if email else Faker().email()
        self.find(locators.first_name_input).send_keys(self.first_name)
        self.find(locators.last_name_input).send_keys(self.last_name)
        self.find(locators.email_input).send_keys(self.email)
        if not password:
            self.password = Faker().password(special_chars=True,
                                             digits=True,
                                             upper_case=True,
                                             lower_case=True,
                                             length=15)
            self.find(locators.password_input).send_keys(self.password)
        elif password == 'empty':
            self.password = None
        else:
            self.password = password
            self.find(locators.password_input).send_keys(self.password)
        self.confirm_password = confirm_password if confirm_password else self.password
        if self.confirm_password:
            self.find(locators.password_confirmation_input).send_keys(self.confirm_password)

    def fill_registration_form_with_empty_field(self,
                                                arg: Literal[
                                                    'first_name',
                                                    'last_name',
                                                    'email',
                                                    'password',
                                                    'password_confirmation']):
        user_data = {'first_name': 'John',
                     'last_name': 'Doe',
                     'email': 'john@doe.com',
                     'password': '12345qwE',
                     'password_confirmation': '12345qwE'
                     }
        if not arg == 'first_name':
            self.find(locators.first_name_input).send_keys(user_data.get('first_name'))
        if not arg == 'last_name':
            self.find(locators.last_name_input).send_keys(user_data.get('last_name'))
        if not arg == 'email':
            self.find(locators.email_input).send_keys(user_data.get('email'))
        if not arg == 'password':
            self.find(locators.password_input).send_keys(user_data.get('password'))
        if not arg == 'password_confirmation':
            self.find(locators.password_confirmation_input).send_keys(user_data.get('password_confirmation'))

    def click_create_button(self):
        self.find(locators.create_button).click()

    def check_warning_message_under_field(self,
                                          arg: Literal[
                                              'first_name',
                                              'last_name',
                                              'email',
                                              'password',
                                              'password_confirmation']):
        print(f'Получил ARG = {arg}')
        if arg == 'first_name':
            assert self.find(locators.first_name_requirement_warning).is_displayed(), \
                f'Warning message for field {arg} not found'
        elif arg == 'last_name':
            assert self.find(locators.last_name_requirement_warning).is_displayed(), \
                f'Warning message for field {arg} not found'
        elif arg == 'email':
            assert self.find(locators.email_requirement_warning).is_displayed(), \
                f'Warning message for field {arg} not found'
        elif arg == 'password':
            assert self.find(locators.password_requirement_warning).is_displayed(), \
                f'Warning message for field {arg} not found'
        elif arg == 'password_confirmation':
            assert self.find(locators.password_confirmation_requirement_warning).is_displayed(), \
                f'Warning message for field {arg} not found'
        else:
            raise NotImplementedError('Entered nonexistent field name')

    def check_password_strength_meter_text(self, text):
        assert self.find(locators.password_strength_meter).text == text, \
            f'Returned text {self.find(locators.password_strength_meter).text} while expected {text}'
