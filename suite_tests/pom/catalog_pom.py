import time
from selenium.webdriver import Keys
from base.seleniumbase import SeleniumBase
from base.static_info import *


class Catalog_POM(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.driver.get('https://test.autodoc.pro/fr/catalog')
        self.first_catalog_element_class = 'ant-card-meta-description'
        self.add_product_button_css = 'td[title="Ajouter"] button'
        self.add_product_notification_class = 'ant-notification-notice-content'

        self.last_navigation_name = "text--fno_"

    def go_to_first_catalog_element(self):
        count = 0
        first_catalog_item = self.is_visible('class_name', self.first_catalog_element_class,
                                             'First catalog element visibility')
        first_catalog_item_text = first_catalog_item.text
        first_catalog_item.click()
        last_navigation_name_text = self.is_visible('class_name', self.last_navigation_name,
                                                    'First catalog element visibility').text
        if first_catalog_item_text == last_navigation_name_text and count < 10:
            self.go_to_first_catalog_element(self)
            count = +1
        else:
            count = 0
            return self.driver

    def add_first_product_item_to_basket(self):
        first_catalog_item = self.is_visible('css', self.add_product_button_css,
                                             'First listing product item visibility')
        first_catalog_item.click()
        notification_text = self.is_visible('class_name', self.add_product_notification_class,
                        'Add product notification element visibility').text
        return self.driver

