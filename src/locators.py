from selenium.webdriver.common.by import By


class Locators:
    email_field = By.NAME, 'name' #Поле "Email" на форме авторизации.
    password_field = By.NAME, 'Пароль' #Поле "Пароль" на форме авторизации.
    login_button_1 = By.XPATH, ".//button[text() = 'Войти']" #Кнопка "Войти".
    login_button_2 = By.CLASS_NAME, 'Auth_link__1fOlj' #Кнопка "Войти".
    login_in_account_button = By.XPATH, ".//button[text() = 'Войти в аккаунт']" #Кнопка "Войти в аккаунт".
    registration_button = By.XPATH, './/button[text() = "Зарегистрироваться"]' #Кнопка "Зарегистрироваться".
    name_reg_field = By.XPATH, ".//label[text()='Имя']//parent::*/input" #Поле "Имя" на форме регистрации.
    email_reg_field = By.XPATH, ".//label[text()='Email']//parent::*/input" #Поле "email" на форме регистрации.
    p_incorrect_password = By.XPATH, './/p[@class="input__error text_type_main-default"]' #Текст "Некорретный пароль".
    account_button = By.XPATH, ".//p[text()='Личный Кабинет']" #Кнопка личный кабинет.
    constructor_button = By.XPATH, ".//p[text()='Конструктор']" #Кнопка "Конструктор".
    logo_button = By.XPATH, ".//div[@class='AppHeader_header__logo__2D0X2']" #Кнопка "Логотип"
    logout_button = By.CSS_SELECTOR, '.Account_button__14Yp3' #Кнопка "Выйти".
    chapter_buns = By.XPATH, './/span[text() = "Булки"]/..' #Раздел "Булки".
    chapter_sauces = By.XPATH, './/span[text() = "Соусы"]/..' #Раздел "Соусы".
    chapter_toppings = By.XPATH, './/span[text() = "Начинки"]/..' #Раздел "Начинки".
    active_chapter = By.XPATH, (".//div[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc "
                                "pt-4 pr-10 pb-4 pl-10 noselect']/span") #Активный раздел конструктора бургера.
