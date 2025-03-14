from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from src.config import Config
from src.helpers import SignUpData
from src.locators import Locators


class TestConstructor:

    def test_transition_to_constructor_page_button(self, driver):

        driver.get(f'{Config.URL}login')
        driver.find_element(*Locators.email_field).send_keys(f'{SignUpData.email}')
        driver.find_element(*Locators.password_field).send_keys(f'{SignUpData.password}')
        driver.find_element(*Locators.login_button_1).click()

        WebDriverWait(driver, Config.timeout).until(expected_conditions.element_to_be_clickable
                                                    (Locators.chapter_sauces))

        driver.find_element(*Locators.account_button).click()

        WebDriverWait(driver, Config.timeout).until(expected_conditions.element_to_be_clickable
                                                    (Locators.logout_button))

        driver.find_element(*Locators.constructor_button).click()

        WebDriverWait(driver, Config.timeout).until(expected_conditions.element_to_be_clickable
                                                    (Locators.chapter_sauces))

        assert driver.current_url == f'{Config.URL}'

    def test_transition_to_constructor_page_logo(self, driver):

        driver.get(f'{Config.URL}login')

        driver.find_element(*Locators.email_field).send_keys(f'{SignUpData.email}')
        driver.find_element(*Locators.password_field).send_keys(f'{SignUpData.password}')
        driver.find_element(*Locators.login_button_1).click()

        WebDriverWait(driver, Config.timeout).until(expected_conditions.element_to_be_clickable
                                                    (Locators.chapter_sauces))

        driver.find_element(*Locators.account_button).click()

        WebDriverWait(driver, Config.timeout).until(expected_conditions.element_to_be_clickable
                                                    (Locators.logout_button))

        driver.find_element(*Locators.logo_button).click()

        WebDriverWait(driver, Config.timeout).until(expected_conditions.element_to_be_clickable
                                                    (Locators.chapter_sauces))

        assert driver.current_url == f'{Config.URL}'
