import os
from dotenv import load_dotenv

load_dotenv()

LOGIN = os.getenv("LOGIN")
PASSWORD = os.getenv("PASSWORD")


class TestLogin:
    def test_existing_user_can_login(self, login):
        login.open_login_page()
        login.click_personal_account_btn()
        login.click_sing_in_btn()
        login.should_be_login_form()
        login.enter_login(login=LOGIN)
        login.enter_password(password=PASSWORD)
        login.click_login_btn()
        login.not_should_be_login_form()
        login.check_user_is_authorized()
