from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from pages.base_page import Page

class Header(Page):
    CURESKIN_SEARCH_ICON = (By.CSS_SELECTOR, "#shopify-section-header > sticky-header > header > search-modal > details > summary")
    POPUP_CLOSE = (By.CSS_SELECTOR, '.popup-close')
    SEARCH_FIELD = (By.CSS_SELECTOR, '#Search-In-Modal')

    def click_search_icon(self):
        self.click(*self.CURESKIN_SEARCH_ICON)

    def close_popup(self):
        self.wait_for_element_click(*self.POPUP_CLOSE)

    def input_search_text(self, text):
        self.input_text(text, *self.SEARCH_FIELD)

