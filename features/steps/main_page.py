from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@given('Open main page')
def open_cureskin(context):
    context.app.main_page.open_main()


@when('Close a pop up')
def close_popup(context):
    context.app.header.close_popup()


@when('Click on search icon in the header')
def click_search_icon(context):
    context.app.header.click_search_icon()


@when('Input text {text} into search field')
def input_search_text(context, text):
    context.app.header.input_search_text(text)

