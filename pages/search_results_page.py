from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from pages.base_page import Page

class SearchResults(Page):
    PRODUCT_TITLE = (By.CSS_SELECTOR, 'li.grid__item')


    def find_elements(self):
       elements = self.driver.find_elements(*self.PRODUCT_TITLE)
       for i in elements[:3]:
           assert i.text, 'Got no SPF'

