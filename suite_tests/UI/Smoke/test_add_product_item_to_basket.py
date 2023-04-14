from suite_tests.pom.sign_in_pom import *
from suite_tests.pom.dashboard_pom import *
from suite_tests.pom.catalog_pom import *
from suite_tests.pom.cookie_modal_pom import *

@pytest.mark.usefixtures('setup')
@pytest.mark.SmokeUI
class TestAddProductItems:

    def test_add_product_to_basket(self):
        expected_result = "Produit ajouté au panier"
        cookie = CookieModal_POM(self.driver)
        cookie.setup_cookie_modal_true()

        login = SignIn_POM(self.driver)
        login.set_login()
        login.set_password()

        dashboard = Dashboard_POM(self.driver)
        dashboard.create_car_tab_by_reg_number()

        catalog = Catalog_POM(self.driver)
        catalog.go_to_first_catalog_element()
        catalog.go_to_first_catalog_element()


        #add notification pom + test displaying assert ()
        #go to basket and check: choice product item is displayed and make api relalculation