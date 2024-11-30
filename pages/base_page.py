from selenium.webdriver.remote.webdriver import WebDriver
from pages.locators import base_page_locators as locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    base_url = 'https://magento.softwaretestingboard.com'
    page_url = None
    tab = None

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)

    def open_page(self):
        if self.page_url:
            self.driver.get(f'{self.base_url}{self.page_url}')
        else:
            raise NotImplementedError('Page url was not specified')

    def find(self, locator: tuple):
        return self.driver.find_element(*locator)

    def find_all(self, locator: tuple):
        return self.driver.find_elements(*locator)

    def check_tab_title_is(self, title):
        assert self.driver.title == title

    def check_page_headline_is(self, headline):
        assert self.find(locators.headline_locator).text == headline

    def check_search_field_placeholder_text_is(self, reference_text):
        current_text = self.find(locators.search_field).get_attribute('placeholder')
        assert current_text == reference_text, \
            f'Returned placeholder text {current_text} while expected {reference_text}'

    def check_search_field_max_number_of_symbols_is(self, reference_number):
        current_number = self.find(locators.search_field).get_attribute('maxlength')
        assert current_number == reference_number, \
            f'Returned number {current_number} while expected {reference_number}'

    def fill_search_field_with_value(self, value):
        self.find(locators.search_field).send_keys(value)

    def check_search_button_is_disabled(self):
        assert self.find(locators.search_button).get_attribute('disabled'), 'Search button is not disabled'

    def check_search_button_is_enabled(self):
        self.wait.until(EC.element_to_be_clickable(self.find(locators.search_button)))
        assert not self.find(locators.search_button).get_attribute('disabled'), 'Search button is not enabled'

    def check_tab_marked_as_active(self):
        assert 'active' in self.find(self.tab).get_attribute('class'), 'Tab does not have class "active"'
