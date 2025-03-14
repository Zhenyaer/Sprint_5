from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from src.config import Config
from src.helpers import SignUpData
from src.helpers import RandomEmail
from src.locators import Locators


class TestRegistration:

    def test_registration_correct(self, driver):

        driver.get(f'{Config.URL}register')

        driver.find_element(*Locators.name_reg_field).send_keys(f'{SignUpData.name}')
        driver.find_element(*Locators.email_reg_field).send_keys(f'{RandomEmail.email}')
        driver.find_element(*Locators.password_field).send_keys(f'{SignUpData.password}')
        driver.find_element(*Locators.registration_button).click()

        WebDriverWait(driver, Config.timeout).until(expected_conditions.element_to_be_clickable
                                                     (Locators.login_button_1))

        assert driver.current_url == f'{Config.URL}login'

    def test_registration_incorrect_password(self, driver):

        driver.get(f'{Config.URL}register')

        driver.find_element(*Locators.name_reg_field).send_keys(f'{SignUpData.name}')
        driver.find_element(*Locators.email_reg_field).send_keys(f'{RandomEmail.email}')
        driver.find_element(*Locators.password_field).send_keys(f'{SignUpData.incorrect_password}')
        driver.find_element(*Locators.registration_button).click()

        WebDriverWait(driver, Config.timeout).until(expected_conditions.presence_of_element_located
                                                     (Locators.p_incorrect_password))

        assert (driver.find_element(*Locators.p_incorrect_password).text == 'Некорректный пароль')
