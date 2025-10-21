import time

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as e_conditions
from loguru import logger

def bai_du_general_content():
    options = UiAutomator2Options()
    options.load_capabilities({
        'automationName': 'uiautomator2',
        'platformName': 'Android',
        'deviceName': '10ACBY12RX000UA',
        'noReset': True
    })

    baidu_driver = webdriver.Remote('http://127.0.0.1:4723', options=options)
    wait = WebDriverWait(baidu_driver, 30)

    def bai_du_launcher():
        logger.info('bai_du_launcher running...')
        try:
            bai_du_application_button = wait.until(e_conditions.presence_of_element_located(
                (AppiumBy.XPATH, '//android.widget.TextView[@text="百度极速版"]')))
            bai_du_application_button.click()

        except Exception as e:
            logger.error(f'启动百度极速版失败:{e}')

    def switch_to_cash_page():
        logger.info('switch_to_cash_page running...')
        try:
            switch_button = wait.until(e_conditions.presence_of_element_located((AppiumBy.XPATH,
                                                                                 '//android.widget.FrameLayout[@resource-id="com.baidu.searchbox.lite:id/obfuscated"]')))
            switch_button.click()

        except Exception as e:
            logger.error(f'转至领现金页面失败:{e}')

    def whether_appear_box_reward():
        logger.info('whether_appear_box_reward running...')
        try:
            quit_box_location = [(872, 478)]
            box_location = [(964, 2199)]

            time.sleep(1)
            baidu_driver.tap(box_location)

            time.sleep(1)

            time.sleep(1)
            baidu_driver.tap(quit_box_location)


        except Exception as e:
            logger.error(f'宝箱操作错误! :{e}')

    def enter_get_cash_page():
        logger.info('enter_get_cash_page running...')
        try:
            get_cash_position = [(880,344)]
            baidu_driver.tap(get_cash_position)

        except Exception as e:
            logger.error(f'进入提现页面失败! :{e}')

    def go_back_to_desktop():
        logger.info('go_back_to_desktop running...')
        for command in list(range(0,8)):
            logger.info(f'这是百度极速版的第 {command} 次退出')
            baidu_driver.back()
        baidu_driver.quit()

    def bai_du_script_running_sequence():
        bai_du_launcher()
        switch_to_cash_page()
        ###签到页面未完成(自动弹出)###
        print()
        ###签到页面未完成(自动弹出)###
        # whether_appear_box_reward()
        enter_get_cash_page()
        time.sleep(3)
        go_back_to_desktop()



    # if __name__ == '__main__':
    #     bai_du_script_running_sequence()

    bai_du_script_running_sequence()

# bai_du_general_content()