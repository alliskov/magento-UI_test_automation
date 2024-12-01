from selenium.webdriver.common.by import By

visible_toolbar = '//div[@class="toolbar toolbar-products"][1]'
sort_type_selector = \
    (By.XPATH, f'{visible_toolbar}//select[@id="sorter"]')
sort_by_position = \
    (By.XPATH, f'{visible_toolbar}//select[@id="sorter"]/option[@value="position"]')
sort_by_name = \
    (By.XPATH, f'{visible_toolbar}//select[@id="sorter"]/option[@value="name"]')
sort_by_price = \
    (By.XPATH, f'{visible_toolbar}//select[@id="sorter"]/option[@value="price"]')
sort_direction_selector = \
    (By.XPATH, f'{visible_toolbar}/div[@class="toolbar-sorter sorter"]/a[@data-role="direction-switcher"]')
items_locator = \
    (By.XPATH, '//ol[@class="products list items product-items"]/li')
grid_mode_switch = \
    (By.XPATH, f'{visible_toolbar}//div[@class="modes"]/*[@title="Grid"]')
list_mode_switch = \
    (By.XPATH, f'{visible_toolbar}//div[@class="modes"]/*[@title="List"]')
