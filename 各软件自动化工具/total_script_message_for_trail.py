from appium.webdriver.common.appiumby import AppiumBy
from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.support import expected_conditions as e_conditions
from selenium.webdriver.support.ui import WebDriverWait
import time

options = UiAutomator2Options()
options.load_capabilities({
    'automationName' : 'uiautomator2',
    'platformName' : 'Android',
    'deviceName' : '10ACBY12RX000UA',
    'noReset': True
})

launcher = webdriver.Remote('http://127.0.0.1:4723',options=options)
wait = WebDriverWait(launcher, 180)

try:
    applications = launcher.find_elements(AppiumBy.XPATH,'//android.widget.TextView')
    print(len(applications))
    for i in applications:
        application_name = i.get_attribute('text')
        print(application_name)
        print('+++====-----')


except Exception as e:
    print(e)
