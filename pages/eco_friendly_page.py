from pages.locators import eco_friendly_page_locators as locators
from pages.base_page import BasePage
from typing import Literal


class EcoFriendly(BasePage):
    page_url = '/collections/eco-friendly.html'

    def switch_view_mode_to_list(self):
        self.find(locators.list_mode_switch).click()

    def switch_view_mode_to_grid(self):
        self.find(locators.grid_mode_switch).click()

    def check_active_view_mode_is(self, arg: Literal['grid', 'list']):
        if arg.lower() == 'grid':
            assert 'active' in self.find(locators.grid_mode_switch).get_attribute('class')
        elif arg.lower() == 'list':
            assert 'active' in self.find(locators.list_mode_switch).get_attribute('class')
        else:
            raise NotImplementedError('Entered nonexistent mode name')

    def check_active_sort_type_is_by(self, arg: Literal['name', 'price', 'position']):
        if arg.lower() == 'name':
            assert self.find(locators.sort_by_name).get_attribute('selected'), 'Sort type is not active'
        elif arg.lower() == 'position':
            assert self.find(locators.sort_by_position).get_attribute('selected'), 'Sort type is not active'
        elif arg.lower() == 'price':
            assert self.find(locators.sort_by_price).get_attribute('selected'), 'Sort type is not active'
        else:
            raise NotImplementedError('Entered nonexistent sort type')

    def check_active_sort_direction_is(self, arg: Literal['ascendant', 'descendant']):
        if arg.lower() == 'asc':
            assert 'sort-asc' in self.find(locators.sort_direction_selector).get_attribute('class')
        if arg.lower() == 'desc':
            assert 'sort-desc' in self.find(locators.sort_direction_selector).get_attribute('class')
