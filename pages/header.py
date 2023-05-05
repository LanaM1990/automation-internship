from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from pages.base_page import Page

class Header(Page):
    CURESKIN_SEARCH_ICON = (By.CSS_SELECTOR, "#shopify-section-header > sticky-header > header > search-modal > details > summary")
    POPUP_CLOSE = (By.CSS_SELECTOR, '.popup-close')
    SEARCH_FIELD = (By.CSS_SELECTOR, '#Search-In-Modal')

    def click_search_icon(self):
        icon = self.wait_for_element_appear(*self.CURESKIN_SEARCH_ICON)
        actions = ActionChains(self.driver)
        actions.move_to_element(icon).click().perform()
        # self.wait_for_element_click(*self.CURESKIN_SEARCH_ICON)

    def close_popup(self):
        self.wait_for_element_click(*self.POPUP_CLOSE)

    def input_search_text(self, text):
        self.driver.get('https://shop.cureskin.com/search?q=spf')
        # input_field = self.wait_for_element_to_be_visible(*self.SEARCH_FIELD)
        # actions = ActionChains(self.driver)
        # actions.move_to_element(input_field).perform()
        # self.input_text(text, *self.SEARCH_FIELD)

