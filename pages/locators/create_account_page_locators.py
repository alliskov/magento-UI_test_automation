from selenium.webdriver.common.by import By

first_name_input = (By.XPATH, '//input[@id="firstname"]')
last_name_input = (By.XPATH, '//input[@id="lastname"]')
email_input = (By.XPATH, '//input[@id="email_address"]')
password_input = (By.XPATH, '//input[@id="password"]')
password_confirmation_input = (By.XPATH, '//input[@id="password-confirmation"]')
password_strength_meter_container = (By.XPATH, '//div[@id="password-strength-meter-container"]')
password_strength_meter = (By.XPATH, '//div[@id="password-strength-meter"]//span')
create_button = \
    (By.XPATH, '//button[(@type="submit") and (@title="Create an Account")]')
first_name_requirement_warning = \
    (By.XPATH, '//div[(@for="firstname") and (text()="This is a required field.")]')
last_name_requirement_warning = \
    (By.XPATH, '//div[(@for="lastname") and (text()="This is a required field.")]')
email_requirement_warning = \
    (By.XPATH, '//div[(@for="email_address") and (text()="This is a required field.")]')
password_requirement_warning = \
    (By.XPATH, '//div[(@for="password") and (text()="This is a required field.")]')
password_confirmation_requirement_warning = \
    (By.XPATH, '//div[(@for="password-confirmation") and (text()="This is a required field.")]')
