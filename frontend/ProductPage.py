import requests
from frontend.BasePage import BasePage
from frontend.locators import ProductPageLocator, ModalCartLocator, CartIconLocator
from configs import SHOP_URL, Digma_iDx10


class ProductPage(BasePage):
    def open_exist_product_page(self):
        prodict_page = f'{SHOP_URL}{Digma_iDx10}'
        self.open_page(prodict_page)

    def check_product_img(self):
        main_img_src = self.get_attribute(*ProductPageLocator.MAIN_IMG, 'src')
        response = requests.get(main_img_src)
        assert response.status_code == 200, (f'Картинка товара недоступна.'
                                             f'Статус код: {response.status_code}\nURL картинки: {main_img_src}')

    def check_product_h1(self, product_name: str):
        h1_text = self.get_text(*ProductPageLocator.H1)
        assert product_name == h1_text, f'Ждали h1 страницы: {product_name}, получили: {h1_text}'

    def check_product_price(self, price: str):
        product_price_ui = self.get_text(*ProductPageLocator.PRICE)
        assert price == product_price_ui, f'Ждали цену продукта: {price}, получили: {product_price_ui}'

    def click_to_cart_btn(self):
        assert self.is_visible(*ProductPageLocator.ADD_TO_CART_BTN), 'Нет кнопки "В корзину" на странице товара'
        self.click(*ProductPageLocator.ADD_TO_CART_BTN)

    def should_be_modal_cart_modal_form(self):
        assert self.is_visible(*ModalCartLocator.CART_FORM), 'После нажатия на кнопку "В корзину", окно корзины не отображается'

    def not_should_be_modal_cart_modal_form(self):
        assert self.is_not_visible(*ModalCartLocator.CART_FORM), 'Окно корзины продолжает отображаться после закрытия'

    def check_product_in_cart(self, name: str, price: str):
        product_name_ui = self.get_text(*ModalCartLocator.PRODUCT_NAME)
        product_price_ui = self.get_text(*ModalCartLocator.PRICE_PER_PRODUCT)
        product_total_price_ui = self.get_text(*ModalCartLocator.TOTAL_PRODUCT_PRICE)
        assert product_name_ui == name, f'Ждали название продукта: {name}, получили: {product_name_ui}'
        assert product_price_ui == price, f'Ждали цену продукта: {price}, получили: {product_price_ui}'
        assert product_total_price_ui == price, f'Ждали итоговую цену продукта: {price}, получили: {product_total_price_ui}'

    def close_cart_form(self):
        assert self.is_visible(*ModalCartLocator.CLOSE_CART_FORM_BTN), 'Нет кнопки "крестик" для закрытия окна корзины'
        self.click(*ModalCartLocator.CLOSE_CART_FORM_BTN)
        self.not_should_be_modal_cart_modal_form()

    def check_cart_upper_right_corner(self, price: str):
        price_ui = self.get_text(*CartIconLocator.PRODUCT_PRICE)
        assert price_ui == price, f'Ждали цену продукта: {price}, получили: {price_ui}'

    def check_cart_upper_right_corner_is_empty(self):
        price_ui = self.get_text(*CartIconLocator.PRODUCT_PRICE)
        assert price_ui == '', f'Ждали пустую цену продукта, получили: {price_ui}'

    def click_delete_product_from_cart_btn(self):
        assert self.is_visible(*ModalCartLocator.DELETE_PRODUCT_IN_CART_BTN)
        self.click(*ModalCartLocator.DELETE_PRODUCT_IN_CART_BTN)
