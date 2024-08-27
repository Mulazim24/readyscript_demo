import inspect
from typing import Union

from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

POLL_FREQUENCY = 0.3  # частота запросов каждые POLL_FREQUENCY секунд
TIMEOUT = 30


class BasePage:
    def __init__(self, browser):
        self.browser = browser
        self.action = ActionChains(self.browser)

    def open_page(self, page: str) -> None:
        self.browser.get(page)

    def find_element(self, how: str, what: str) -> WebElement:
        """
        Ищем элемент на странице
        :param how: какую стратегию By локатора используем
                    пример: By.XPATH/By.ID/By.NAME и т.д
        :param what: локатор элемента
        :return: найденный веб элемент
        """
        called_from = inspect.stack()[1].function
        element = WebDriverWait(self.browser, timeout=TIMEOUT, poll_frequency=POLL_FREQUENCY).until(
            EC.presence_of_element_located((how, what)),
            message=f"Не удалось найти элемент по локатору: {how, what}\n"
                    f"В методе {called_from}")
        return element

    def find_elements(self, how: str, what: str) -> list[WebElement]:
        """
        Ищем элементы на странице
        :param how: какую стратегию By локатора используем
                    пример: By.XPATH/By.ID/By.NAME и т.д
        :param what: локатор элемента
        :return: список найденных веб элементов
        """
        called_from = inspect.stack()[1].function
        elements = WebDriverWait(self.browser, timeout=TIMEOUT, poll_frequency=POLL_FREQUENCY).until(
            EC.presence_of_all_elements_located((how, what)),
            message=f"Не удалось найти элемент по локатору: {how, what}\n"
                    f"В методе {called_from}")
        return elements

    def click(self, how: str, what: str) -> None:
        """
        Нажимаем на элемент
        :param how: какую стратегию By локатора используем
                    пример: By.XPATH/By.ID/By.NAME и т.д
        :param what: локатор элемента
        """
        called_from = inspect.stack()[1].function
        element = WebDriverWait(self.browser, timeout=TIMEOUT, poll_frequency=POLL_FREQUENCY).until(
            EC.element_to_be_clickable((how, what)),
            message=f"Не удалось нажать на элемент по локатору: {how, what}\n"
                    f"В методе {called_from}")
        element.click()

    def is_visible(self, how, what) -> bool:
        """Элемент есть в DOM и виден
        :param how: какую стратегию By локатора используем
                    пример: By.XPATH/By.ID/By.NAME и т.д
        :param what: локатор элемента
        """
        called_from = inspect.stack()[1].function
        element = WebDriverWait(self.browser, timeout=TIMEOUT, poll_frequency=POLL_FREQUENCY).until(
            EC.visibility_of_element_located((how, what)),
            message=f"Элемент по локатору не отображается: {how, what}\n"
                    f"Метод: {called_from}")
        return element.is_displayed()

    def is_not_visible(self, how, what) -> bool:
        """
        Элемента нет в DOM и не виден
        :param how: 
        :param what: 
        """
        element = WebDriverWait(self.browser, timeout=TIMEOUT, poll_frequency=POLL_FREQUENCY).until(
            EC.invisibility_of_element_located((how, what)),
            message=f"Элемент по локатору отображается: {how, what}")
        return True if element else False

    def get_text(self, how, what) -> str:
        """
        Получить текст элемента
        :param how:
        :param what:
        """
        element = self.find_element(how, what)
        return element.text

    def insert_text(self, how, what, value) -> None:
        """
        Вставить текст
        :param how:
        :param what:
        :param value:
        """
        element = self.find_element(how, what)
        element.clear()
        element.send_keys(str(value))

    def hover_mouse_over(self, how: str, what: str) -> None:
        """
        Ищем элементы на странице
        :param how: какую стратегию By локатора используем
                    пример: By.XPATH/By.ID/By.NAME и т.д
        :param what: локатор элемента
        """
        element = self.find_element(how, what)
        self.action.move_to_element(element).perform()

    def get_attribute(self, how, what, attribute: str) -> Union[str, None]:
        """
        Получить атрибут элемента
        :param how:
        :param what:
        :param attribute: атрибут
        """
        element = self.find_element(how, what)
        return element.get_attribute(attribute)
