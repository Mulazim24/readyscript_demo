import requests
from frontend.BasePage import BasePage
from frontend.locators import CatalogPageLocator, FavoriteIconLocator
from configs import SHOP_URL


class CatalogPage(BasePage):
    def open_catalog_for(self, *, brand: str = ''):
        catalog_page = f'{SHOP_URL}/catalog/{brand}/'
        self.open_page(catalog_page)

    def check_catalog_h1(self, brand: str):
        h1_ui = self.get_text(*CatalogPageLocator.CATALOG_H1).strip()
        assert brand == h1_ui, f'Ждали h1 страницы: {brand}, получили: {h1_ui}'

    def check_product_title(self, title: str):
        product_title_ui = self.get_text(*CatalogPageLocator.PRODUCT_TITLE)
        assert title in product_title_ui, f'В названии продукта "{product_title_ui}" нет слова "{title}"'

    def check_product_price(self, price: str):
        product_price_ui = self.get_text(*CatalogPageLocator.PRODUCT_PRICE)
        assert price == product_price_ui, f'Ждали цену продукта: {price}, получили: {product_price_ui}'

    def check_catalog_cards(self):
        assert self.is_visible(*CatalogPageLocator.CATALOG_MAIN_DIV), 'На странице каталога нет блока с товарами'
        assert self.is_visible(*CatalogPageLocator.CATALOG_ITEM_DIV), 'На странице каталога нет карточки товара'

    def check_product_img_available(self):
        img_src = self.get_attribute(*CatalogPageLocator.PRODUCT_IMG, 'src')
        response = requests.get(img_src)
        assert response.status_code == 200, (f'Картинка товара недоступна.'
                                             f'Статус код: {response.status_code}\nURL картинки: {img_src}')

    def click_favorite_btn(self):
        assert self.is_visible(*CatalogPageLocator.FAVORITE_BTN), 'Нет кнопки "В избранное" для продукта'
        self.click(*CatalogPageLocator.FAVORITE_BTN)

    def check_favorite_btn_is_active(self):
        assert self.is_visible(*CatalogPageLocator.IN_FAVORITE_BTN), 'Кнопка "В избранное" неактивна для продукта (не красная)'

    def check_favorite_icon(self):
        assert self.is_visible(*FavoriteIconLocator.ACTIVE_FAVORITE), 'Иконка "Избранное" в вернем правом углу не активна'

    def check_favorite_count(self):
        assert self.is_visible(*FavoriteIconLocator.FAVORITE_COUNT), 'Количество продуктов в избранном не отображается'
        favorite_count = self.get_text(*FavoriteIconLocator.FAVORITE_COUNT)
        assert int(favorite_count) == 1, f'Ждали в избранном 1 продукт, получили: {favorite_count}'
