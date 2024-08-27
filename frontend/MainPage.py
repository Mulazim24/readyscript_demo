from frontend.BasePage import BasePage
from frontend.locators import MainPageLocator
from configs import SHOP_URL


class MainPage(BasePage):
    def open_main_page(self):
        self.open_page(SHOP_URL)

    def click_catalog_menu(self):
        assert self.is_visible(*MainPageLocator.CATALOG_BTN), 'Нет синей кнопки Каталог на главной странице'
        self.click(*MainPageLocator.CATALOG_BTN)

    def should_be_catalog_dropdown(self):
        assert self.is_visible(*MainPageLocator.CATALOG_DROPDOWN_MENU), 'Раскрывающийся список каталогов не отображается'

    def hover_mouse_over_electronic_category(self):
        assert self.is_visible(*MainPageLocator.ELECTRONIC_SECTION), 'В раскрывающемся списке каталогов нет раздела Электроника'
        self.hover_mouse_over(*MainPageLocator.ELECTRONIC_SECTION)

    def hover_mouse_over_tablet_category(self):
        assert self.is_visible(*MainPageLocator.TABLET_SECTION), 'В раскрывающемся списке подкаталогов нет раздела Планшеты'
        self.hover_mouse_over(*MainPageLocator.TABLET_SECTION)

    def click_on_digma(self):
        assert self.is_visible(*MainPageLocator.DIGMA_CATALOG), 'В раскрывающемся списке планшетов нет модели Digma'
        self.click(*MainPageLocator.DIGMA_CATALOG)
