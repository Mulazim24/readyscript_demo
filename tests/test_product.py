class TestProduct:
    def test_add_product_to_cart(self, product, product_name, product_price):
        product.open_exist_product_page()
        product.check_product_h1(product_name)
        product.check_product_img()
        product.click_to_cart_btn()
        product.should_be_modal_cart_modal_form()
        product.check_product_in_cart(product_name, product_price)
        product.check_cart_upper_right_corner(product_price)

    def test_delete_product_from_cart(self, product, pre_add_product_to_cart):
        product.click_delete_product_from_cart_btn()
        product.not_should_be_modal_cart_modal_form()
        product.check_cart_upper_right_corner_is_empty()

    def test_add_product_to_favorite(self, catalog, remove_favorite):
        catalog.open_catalog_for(brand='digma')
        catalog.click_favorite_btn()
        catalog.check_favorite_btn_is_active()
        catalog.check_favorite_icon()
        catalog.check_favorite_count()
