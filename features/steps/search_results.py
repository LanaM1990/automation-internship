from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

@then('Verify results have SPF')
def verify_results(context):
    context.app.search_results_page.find_elements()
