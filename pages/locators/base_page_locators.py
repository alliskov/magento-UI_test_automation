from selenium.webdriver.common.by import By

headline_locator = (By.XPATH, '//h1/span')
search_field = (By.XPATH, '//input[@id="search"]')
search_button = (By.XPATH, '//button[(@type="submit") and (@title="Search")]')
tab_panel = (By.XPATH, '//nav[@class="navigation"]/ul')
