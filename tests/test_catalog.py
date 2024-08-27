from configs import TabletBrands


class TestCatalog:
    def test_transition_and_display_products_in_catalog_for_digma(self, main, catalog, product_price):
        main.open_main_page()
        main.click_catalog_menu()
        main.should_be_catalog_dropdown()
        main.hover_mouse_over_electronic_category()
        main.hover_mouse_over_tablet_category()
        main.click_on_digma()
        catalog.check_catalog_h1(TabletBrands.DIGMA.value)
        catalog.check_catalog_cards()
        catalog.check_product_img_available()
        catalog.check_product_title(TabletBrands.DIGMA.value)
        catalog.check_product_price(product_price)
