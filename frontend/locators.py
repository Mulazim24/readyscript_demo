from selenium.webdriver.common.by import By


class UserLocators:
    PERSONAL_ACCOUNT_BTN = (By.XPATH, '//a[@data-bs-reference="parent"]')
    SING_IN_BTN = (By.XPATH, '(//a[@data-bs-reference="parent"]/following-sibling::ul/li)[1]/a')
    USER_FIO = (By.XPATH, '//div[contains(@class, "justify-content-end")]//a[@class="head-bar__link"]//span')


class LoginFormLocator:
    LOGIN_FORM = (By.XPATH, '//div[contains(@class, "show")]//div[@class="modal-content"]')
    LOGIN_INPUT = (By.NAME, 'login')
    PASS_INPUT = (By.NAME, 'pass')
    LOGIN_BNT = (By.XPATH, '//form[@action="/auth/"]//button[@type="submit"]')
    CLOSE_FORM = (By.XPATH, '//button[contains(@class, "modal-close")]')


class MainPageLocator:
    CATALOG_BTN = (By.XPATH, '//button[contains(@class, "head-catalog-btn")]')
    CATALOG_DROPDOWN_MENU = (By.XPATH, '//div[@class="container"]/parent::div[contains(@class, "head-dropdown-catalog")]')
    ACTIVE_CATALOG = (By.XPATH, '//a[contains(@class, "head-dropdown-catalog__category_active")]')
    ELECTRONIC_SECTION = (By.XPATH, '//a[@href="/catalog/elektronika/" and @class="head-dropdown-catalog__category"]')
    TABLET_SECTION = (By.XPATH, '//a[@href="/catalog/planshety/" and @class="head-dropdown-catalog__subcat-list-item"]')
    ACTIVE_SUBCATALOG = (By.XPATH, '//a[contains(@class, "head-dropdown-catalog__subcat-list-item_active")]')
    DIGMA_CATALOG = (By.XPATH, '//a[@href="/catalog/digma/"]')


class CatalogPageLocator:
    CATALOG_H1 = (By.TAG_NAME, 'h1')
    CATALOG_MAIN_DIV = (By.ID, 'products')
    CATALOG_ITEM_DIV = (By.XPATH, '//div[@class="item-card__inner"]')
    PRODUCT_IMG = (By.XPATH, '//div[@class="item-card__inner"]//img')
    PRODUCT_TITLE = (By.XPATH, '//div[@class="item-card__inner"]//a[contains(@class, "item-card__title")]')
    PRODUCT_PRICE = (By.XPATH, '//div[@class="item-card__inner"]//div[@class="item-product-price__new-price"]')
    ADD_TO_CART_BTN = (By.XPATH, '//div[@class="item-product-cart-action"]//button')
    FAVORITE_BTN = (By.XPATH, '//div[@class="item-card__inner"]//a[contains(@class, "rs-favorite")]')
    IN_FAVORITE_BTN = (By.XPATH, '//div[@class="item-card__inner"]//a[contains(@class, "rs-in-favorite")]')


class ModalCartLocator:
    CART_FORM = (By.XPATH, '//div[@class="modal-content"]')
    PRODUCT_IMG = (By.XPATH, '//div[@class="modal-content"]//a[@class="modal-cart-item__img"]//img')
    PRODUCT_NAME = (By.XPATH, '//div[@class="modal-content"]//a[@class="modal-cart-item__title"]')
    PRODUCT_AMOUNT = (By.XPATH, '//div[@class="cart-amount__input"]/input')
    PRICE_PER_PRODUCT = (By.XPATH, '//span[@class="modal-cart-item__price"]')
    TOTAL_PRODUCT_PRICE = (By.XPATH, '//div[text()="Итого:"]/following-sibling::div')
    GO_TO_CART_BTN = (By.XPATH, '//div[@class="modal-content"]//a[text()="Перейти в корзину"]')
    DELETE_PRODUCT_IN_CART_BTN = (By.XPATH, '//div[@class="modal-content"]//a[contains(@class, "modal-cart-item__delete")]')
    CLOSE_CART_FORM_BTN = (By.XPATH, '//div[@class="modal-content"]//button[@aria-label="Close"]')


class CartIconLocator:
    """Корзина в верхнем правом углу"""
    CART = (By.ID, 'rs-cart')
    PRODUCT_PRICE = (By.XPATH, '//span[contains(@class, "cart__price")]')
    PRODUCT_COUNT = (By.XPATH, '//a[@id="rs-cart"]//span[contains(@class, "rs-cart-items-count")]')


class FavoriteIconLocator:
    FAVORITE = (By.XPATH, '//div[@class="head-main"]//a[contains(@class, "rs-favorite-block")]')
    ACTIVE_FAVORITE = (By.XPATH, '//div[@class="head-main"]//a[contains(@class, "rs-favorite-block active")]')
    FAVORITE_COUNT = (By.XPATH, '//div[@class="head-main"]//a[contains(@class, "rs-favorite-block active")]//span[contains(@class, "rs-favorite-items-count")]')


class CardPageLocator:
    ITEM_TITLE = (By.XPATH, '//a[contains(@class, "cart-checkout-item__title")]')
    DELETE_ITEM_BTN = (By.XPATH, '//a[contains(@class, "cart-checkout-item__del")]')
    ITEM_PRICE = (By.XPATH, '(//div[@class="cart-checkout-item__bar"]//span)[1]')
    ITEM_AMOUNT = (By.XPATH, '//div[@class="cart-checkout-item__bar"]//input')


class ProductPageLocator:
    H1 = (By.TAG_NAME, 'h1')
    GALLERY = (By.XPATH, '//div[@class="product-gallery"]')
    MAIN_IMG = (By.XPATH, '(//div[contains(@class, "swiper-slide-active")])[1]//img')
    PRICE = (By.XPATH, '//div[contains(@class, "item-product-price_prod")]//div[@class="item-product-price__new-price"]')
    ADD_TO_CART_BTN = (By.XPATH, '(//div[@class="item-product-cart-action"]//button)[1]')


class BreadcrumbLocator:
    BREADCRUMB = (By.XPATH, '//nav[@class="breadcrumb"]//li[last()]')
