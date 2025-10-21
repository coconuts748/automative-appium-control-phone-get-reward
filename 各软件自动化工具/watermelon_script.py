from appium.options.android import UiAutomator2Options
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as e_conditions
from loguru import logger
import time

def watermelon_general_content():
    necessary_data = {
        'automationName': 'uiautomator2',
        'platformName': 'Android',
        'deviceName': '10ACBY12RX000UA',
        'noReset': True
    }

    options = UiAutomator2Options()
    options.load_capabilities(necessary_data)

    watermelon = webdriver.Remote('http://127.0.0.1:4723', options=options)
    wait = WebDriverWait(watermelon, 20)

    def watermelon_launch():
        logger.info('watermelon launch started......')
        try:
            application_button = wait.until(e_conditions.presence_of_element_located(
                (AppiumBy.XPATH, '//android.widget.TextView[@text="西瓜视频"]')))
            application_button.click()

        except Exception as e:
            logger.error(f'启动西瓜视频失败 :{e}')

    def switch_to_cash_page():
        logger.info('switch_to_cash_page started......')
        try:
            switch_button = wait.until(e_conditions.presence_of_element_located(
                (AppiumBy.XPATH, '//android.widget.RelativeLayout[@content-desc=" 标签"]')))
            switch_button.click()

        except Exception as e:
            logger.error(f'跳转至“赚钱”页面失败:{e}')

    def whether_appear_award_box():  # unsure whether reliable....
        logger.info('inspect_whether_appear_awarding started......')
        try:
            time.sleep(2)
            enter_box_position = [(908, 2123)]
            watermelon.tap(enter_box_position)

            time.sleep(2)

            quit_box_position = [(880, 802)]
            watermelon.tap(quit_box_position)

        except Exception as e:
            logger.info(f'宝箱位置定位失败: {e}')

    def whether_compete_daily_login():
        logger.info('whether_compete_daily_login started......')
        try:
            time.sleep(1)
            daily_button_location = [(933, 833)]
            watermelon.tap(daily_button_location)

            time.sleep(1)
            get_award_button_location = [(545, 1361)]
            watermelon.tap(get_award_button_location)

            time.sleep(1)
            quit_award_button_location = [(84, 168)]
            watermelon.tap(quit_award_button_location)

        except Exception as e:
            logger.info(f'签到错误 :{e}')

    def take_cash_into_package():
        logger.info('take_cash_into_package started......')
        try:
            time.sleep(1)
            cash_button_location = [(894, 419)]
            watermelon.tap(cash_button_location)

        except Exception as e:
            logger.error(f'提取页面错误! :{e}')

    def go_back_to_desktop():
        logger.info('go_back_to_desktop running...')
        for command in list(range(1, 10)):
            logger.info(f'这是西瓜视频的 第{command}次退出...')
            watermelon.back()
        watermelon.quit()

    def watermelon_running_sequence():
        watermelon_launch()
        switch_to_cash_page()
        whether_appear_award_box()
        whether_compete_daily_login()
        take_cash_into_package()
        go_back_to_desktop()

    # if __name__ == '__main__':
    #     watermelon_running_sequence()

    watermelon_running_sequence()

# watermelon_general_content()