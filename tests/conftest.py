import pytest


@pytest.fixture(scope='function')
def product_price():
    """В реальной системе получали бы тут цену из базы или апи"""
    digma_price = '9 680 р.'
    return digma_price


@pytest.fixture(scope='function')
def product_name():
    """В реальной системе получали бы тут название из базы или апи"""
    product_name = 'Планшет Digma iDx10 8Gb'
    return product_name


@pytest.fixture(scope='class')
def pre_add_product_to_cart(product):
    """Добавляем через UI, на реальном проекте лучше сделать добавление через API"""
    product.open_exist_product_page()
    product.click_to_cart_btn()
    product.should_be_modal_cart_modal_form()


@pytest.fixture(scope='class')
def remove_favorite(catalog):
    """
    Убираем из избранного, чтобы повторный тест не падал
    На реальном проекте удаляли бы из избранного через API
    """
    yield
    catalog.click_favorite_btn()
