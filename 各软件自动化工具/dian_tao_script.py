import time

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as e_conditions
from loguru import logger


def dian_tao_general_content():
    options = UiAutomator2Options()
    options.load_capabilities({
        'automationName': 'uiautomator2',
        'platformName': 'Android',
        'deviceName': '10ACBY12RX000UA',
        'noReset': True
    })

    dian_tao_launcher = webdriver.Remote('http://127.0.0.1:4723', options=options)
    wait = WebDriverWait(dian_tao_launcher, 30)

    def start_dian_tao_application():
        logger.info('start_dian_tao_application running.....')
        try:
            tian_tao_button = wait.until(
                e_conditions.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@text="点淘"]')))
            tian_tao_button.click()

        except Exception as e:
            logger.error(f'点淘软件启动失败:{e}')

    def switch_to_welfare_page():
        logger.info('switch_to_welfare_page running.....')
        try:
            welfare_button = wait.until(e_conditions.presence_of_element_located(
                (AppiumBy.XPATH, '//android.widget.ImageView[@resource-id="com.taobao.live:id/gold_common_image"]')))
            welfare_button.click()

        except Exception as e:
            logger.error(f'跳转福利页面失败! :{e}')

    def go_back_to_desktop():

        logger.info('go_back_to_desktop running.....')
        for command in list(range(0,6)):
            logger.info("这是点淘的 第 {} 次返回".format(command))
            dian_tao_launcher.back()
        dian_tao_launcher.quit()

    def dian_tao_script_running_sequence():
        start_dian_tao_application()
        switch_to_welfare_page()
        ######需滑动页面#####
        print()
        ######需滑动页面#####
        go_back_to_desktop()

    dian_tao_script_running_sequence()

# dian_tao_general_content()