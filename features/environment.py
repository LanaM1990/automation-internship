from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.wait import WebDriverWait
#from selenium.webdriver.support.events import EventFiringWebDriver
from app.application import Application
#from support.logger import logger, MyListener

# Allure command:
# behave -f allure_behave.formatter:AllureFormatter -o test_results/features/tests/product_page.feature
#allure serve test_results/
def browser_init(context):
    #test_name
    """
    :param context: Behave context
    :param test_name: scenario.name
    """
    service = Service('/Users/svetlanamikolenko/PycharmProjects/automation-internship/chromedriver')
    # service = Service('/Users/svetlanamikolenko/PycharmProjects/automation-internship/geckodriver')
    # service = Service('/Users/svetlanamikolenko/Desktop/automation/python-selenium-automation/geckodriver')
    context.driver = webdriver.Chrome(service=service)
    # context.driver = webdriver.Firefox(service=service)
    # context.driver = webdriver.Safari()

    # HEADLESS MODE ####
    # options = webdriver.ChromeOptions()
    # options = webdriver.FirefoxOptions()
    # options.add_argument('--headless')
    # options.add_argument('--window-size=1920,1080')
    # options.add_argument('--disable-gpu')
    # options.add_argument('--no-sandbox')
    # options.add_argument('--disable-dev-shm-usage')
    # # context.driver = webdriver.Chrome(
    # #     options=options,
    # #     service=service
    # # )
    # context.driver = webdriver.Firefox(
    #     options=options,
    #     service=service
    # )

    ## EventFiringWebDriver - log file ###
    ## for drivers ###
    # context.driver = EventFiringWebDriver(
    #     webdriver.Chrome(service=service),
    #     MyListener()
    # )
    #
    # for browerstack ###
    # Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings

    # desired_cap = {
    #     'browserName': 'Firefox',
    #     'bstack:options': {
    #     'os': 'Windows',
    #     'osVersion': '11',
    #     'sessionName': test_name
    #     }
    # }
    # bs_user = 'lanamikolenko_0qvtwj'
    # bs_key = 'Cc4pkzwnwUaT4mnsfuUq'
    # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    # context.driver = webdriver.Remote(url, desired_capabilities=desired_cap)

    ### MOBILE ######
    mobile_emulation = {"deviceName": "Nexus 5"}
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    context.driver = webdriver.Chrome(executable_path='/chromedriver.exe', chrome_options=chrome_options)

    context.driver.wait = WebDriverWait(context.driver, 10)
    #context.app = Application(driver=context.driver)
    context.app = Application(context.driver)
    context.driver.maximize_window()
    context.driver.implicitly_wait(4)


def before_scenario(context, scenario):
    # logger.info(f'Started scenario:{scenario.name}')
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    # logger.info(f'Started step:{step}')
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()

