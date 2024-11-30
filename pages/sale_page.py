from pages.locators import sale_page_locators as locators
from pages.base_page import BasePage


class SalePage(BasePage):
    page_url = '/sale.html'
    tab = locators.sale_tab_on_panel

    def check_deal_categories_visibility(self):
        women = self.find(locators.women_deals_category)
        men = self.find(locators.men_deals_category)
        gear = self.find(locators.gear_deals_category)
        assert women.is_displayed(), 'Women deals category is not visible'
        assert men.is_displayed(), 'Men deals category is not visible'
        assert gear.is_displayed(), 'Gear deals category is not visible'

    def check_main_promo_link_is(self, reference_link):
        current_link = self.find(locators.main_promo).get_attribute('href')
        assert current_link == reference_link, \
            f'Returned main promo link {current_link} while expected {reference_link}'
