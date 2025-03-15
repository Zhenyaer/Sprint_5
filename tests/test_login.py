from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from src.config import Config
from src.helpers import SignUpData
from src.locators import Locators


class TestLogin:

    def test_login_main_page(self, driver):

        driver.get(f'{Config.URL}')

        driver.find_element(*Locators.login_in_account_button).click()
        driver.find_element(*Locators.email_field).send_keys(f'{SignUpData.email}')
        driver.find_element(*Locators.password_field).send_keys(f'{SignUpData.password}')
        driver.find_element(*Locators.login_button_1).click()

        WebDriverWait(driver, Config.timeout).until(expected_conditions.element_to_be_clickable
                                                     (Locators.chapter_sauces))

        assert driver.current_url == f'{Config.URL}'

    def test_login_personal_space(self, driver):

        driver.get(f'{Config.URL}')

        driver.find_element(*Locators.account_button).click()
        driver.find_element(*Locators.email_field).send_keys(f'{SignUpData.email}')
        driver.find_element(*Locators.password_field).send_keys(f'{SignUpData.password}')
        driver.find_element(*Locators.login_button_1).click()

        WebDriverWait(driver, Config.timeout).until(expected_conditions.element_to_be_clickable
                                                     (Locators.chapter_sauces))

        assert driver.current_url == f'{Config.URL}'

    def test_login_registration_form(self, driver):

        driver.get(f'{Config.URL}register')

        driver.find_element(*Locators.login_button_2).click()
        driver.find_element(*Locators.email_field).send_keys(f'{SignUpData.email}')
        driver.find_element(*Locators.password_field).send_keys(f'{SignUpData.password}')
        driver.find_element(*Locators.login_button_1).click()

        WebDriverWait(driver, Config.timeout).until(expected_conditions.element_to_be_clickable
                                                     (Locators.chapter_sauces))

        assert driver.current_url == f'{Config.URL}'

    def test_login_password_recovery_form(self, driver):

        driver.get(f'{Config.URL}forgot-password')

        driver.find_element(*Locators.login_button_2).click()
        driver.find_element(*Locators.email_field).send_keys(f'{SignUpData.email}')
        driver.find_element(*Locators.password_field).send_keys(f'{SignUpData.password}')
        driver.find_element(*Locators.login_button_1).click()

        WebDriverWait(driver, Config.timeout).until(expected_conditions.element_to_be_clickable
                                                     (Locators.chapter_sauces))

        assert driver.current_url == f'{Config.URL}'
