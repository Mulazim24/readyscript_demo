from frontend.BasePage import BasePage
from frontend.locators import UserLocators, LoginFormLocator
from configs import SHOP_URL


class LoginElement(BasePage):
    def open_login_page(self):
        self.open_page(SHOP_URL)

    def click_personal_account_btn(self):
        assert self.is_visible(*UserLocators.PERSONAL_ACCOUNT_BTN), 'Нет кнопки Личный кабинет'
        self.click(*UserLocators.PERSONAL_ACCOUNT_BTN)

    def click_sing_in_btn(self):
        assert self.is_visible(*UserLocators.SING_IN_BTN), 'Нет кнопки Вход'
        self.click(*UserLocators.SING_IN_BTN)

    def should_be_login_form(self):
        assert self.is_visible(*LoginFormLocator.LOGIN_FORM), 'Форма авторизации не отображается'
        assert self.is_visible(*LoginFormLocator.LOGIN_INPUT), 'В форме авторизации нет поля ввода логина'
        assert self.is_visible(*LoginFormLocator.PASS_INPUT), 'В форме авторизации нет поля ввода пароля'
        assert self.is_visible(*LoginFormLocator.LOGIN_BNT), 'В форме авторизации нет кнопки Войти'

    def enter_login(self, login: str):
        self.insert_text(*LoginFormLocator.LOGIN_INPUT, '')

    def enter_password(self, password: str):
        self.insert_text(*LoginFormLocator.PASS_INPUT, '')

    def click_login_btn(self):
        self.click(*LoginFormLocator.LOGIN_BNT)

    def not_should_be_login_form(self):
        """Проверяем, что после логина форма авторизации не отображается"""
        assert self.is_not_visible(*LoginFormLocator.LOGIN_FORM), 'Форма авторизации отображается после авторизации'

    def check_user_is_authorized(self, first_name: str = 'Тест', second_name: str = 'Тестов'):
        user_ui = self.get_text(*UserLocators.USER_FIO)
        user = f'{first_name} {second_name}'
        assert user == user_ui, f'Ждали авторизованного пользователя: {user}, получили: {user_ui}'
