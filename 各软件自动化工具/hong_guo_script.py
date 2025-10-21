from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as e_conditions
from loguru import logger
import time

def hong_guo_general_content():
    hong_guo_data = {
        'automationName': 'uiautomator2',
        'platformName': 'Android',
        'deviceName': '10ACBY12RX000UA',
        'noReset': True
    }

    options = UiAutomator2Options()
    options.load_capabilities(hong_guo_data)

    hong_guo_driver = webdriver.Remote('http://127.0.0.1:4723', options=options)
    wait = WebDriverWait(hong_guo_driver, 20)

    def hong_guo_launcher():
        logger.info('hong_guo_launcher running...')
        try:
            hong_guo_button = wait.until(e_conditions.presence_of_element_located(
                (AppiumBy.XPATH, '//android.widget.TextView[@text="红果免费短剧"]')))
            hong_guo_button.click()

        except Exception as e:
            logger.error(f'启动红果视频失败:{e}')

    def hong_guo_switch_to_go_earn_cash_page():
        logger.info('hong_guo_switch_to_go_earn_cash_page running...')
        try:
            switch_button = wait.until(
                e_conditions.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@text="赚钱"]')))
            switch_button.click()

        except Exception as e:
            logger.error(f'切换至赚钱页面失败:{e}')

    def inspect_whether_appear_box_welfare():
        logger.info('inspect_whether_appear_box_welfare running...')
        try:
            original_box_position = 'com.lynx.tasm.behavior.ui.text.FlattenUIText[@text="开宝箱得金币"]'
            original_box_button = wait.until(
                e_conditions.presence_of_element_located((AppiumBy.XPATH, original_box_position)))
            original_box_button.click()

            quit_hong_guo_position = '//android.widget.FrameLayout[@resource-id="com.phoenix.read:id/arh"]/android.widget.FrameLayout/com.lynx.tasm.behavior.ui.LynxFlattenUI[36]'
            quit_hong_guo_button = wait.until(
                e_conditions.presence_of_element_located((AppiumBy.XPATH, quit_hong_guo_position)))
            quit_hong_guo_button.click()

        except Exception as e:
            logger.error(f'暂无无宝箱奖励 :{e}')

    def go_to_cash_page():
        logger.info('go_to_cash_page running...')
        try:
            switch_coin_position = '//com.lynx.tasm.behavior.ui.LynxFlattenUI[@text="现金收益"]'
            switch_coin_position_button = wait.until(
                e_conditions.presence_of_element_located((AppiumBy.XPATH, switch_coin_position)))
            switch_coin_position_button.click()

        except Exception as e:
            logger.error(f'转至提现页面失败:{e}')

    def go_back_to_desktop():
        logger.info('go_back_to_desktop running...')
        for command in list(range(1, 7)):
            logger.info(f'这是红果视频的 第{command}次退出...')
            hong_guo_driver.back()
        hong_guo_driver.quit()

    def hong_guo_script_running_sequence():
        hong_guo_launcher()
        hong_guo_switch_to_go_earn_cash_page()
        # inspect_whether_appear_box_welfare()
        go_to_cash_page()
        go_back_to_desktop()

    # if __name__ == '__main__':
    #     hong_guo_script_running_sequence()

    hong_guo_script_running_sequence()


# hong_guo_general_content()