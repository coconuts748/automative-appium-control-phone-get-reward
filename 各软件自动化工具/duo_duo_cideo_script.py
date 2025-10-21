from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as e_conditions
from loguru import logger
import time

def duo_duo_general_content():
    hong_guo_data = {
        'automationName': 'uiautomator2',
        'platformName': 'Android',
        'deviceName': '10ACBY12RX000UA',
        'noReset': True
    }

    options = UiAutomator2Options()
    options.load_capabilities(hong_guo_data)

    duo_duo_driver = webdriver.Remote('http://127.0.0.1:4723', options=options)
    wait = WebDriverWait(duo_duo_driver, 20)

    def duo_duo_launcher():
        logger.info('duo_duo_launcher running...')
        try:
            duo_duo_video_location = '//android.widget.TextView[@text="多多赚钱短剧"]'
            duo_duo_video_button = wait.until(
                e_conditions.presence_of_element_located((AppiumBy.XPATH, duo_duo_video_location)))
            duo_duo_video_button.click()

        except Exception as e:
            logger.error(f'启动多多视频失败:{e}')

    def close_ad_window():
        logger.info('close_ad_window running...')
        try:
            duo_duo_driver.back()
            time.sleep(4)
            duo_duo_driver.back()
        except Exception as e:
            logger.error(f'弹出广告弹幕处理失败:{e}')

    def switch_take_money_page():
        logger.info('switch_take_money_page running...')
        try:
            switch_location = '(//android.widget.ImageView[@resource-id="com.fec.ddzqdj:id/bottom_navigation_view_icon"])[3]'
            switch_button = wait.until(e_conditions.element_to_be_clickable((AppiumBy.XPATH, switch_location)))
            switch_button.click()

        except Exception as e:
            logger.error(f'跳转至赚钱页面失败:{e}')

    def check_whether_daily_log_condition():
        logger.info('check_whether_daily_log_condition running...')
        try:
            judge_condition = wait.until(e_conditions.presence_of_element_located(
                (AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.fec.ddzqdj:id/btn_sign"]')))
            if judge_condition.get_attribute('text') == '去签到':
                judge_condition.click()

            else:
                logger.info('今日已完成签到!')

        except Exception as e:
            logger.error(f'签到流程错误 :{e}')

    def enter_refine_cash_page():
        logger.info('enter_refine_cash_page running...')
        try:
            refine_location = '//android.widget.TextView[@resource-id="com.fec.ddzqdj:id/btn_withdraw"]'
            refine_button = wait.until(e_conditions.presence_of_element_located((AppiumBy.XPATH, refine_location)))
            refine_button.click()

        except Exception as e:
            logger.error(f'跳转至提现页面错误:{e}')

    def go_back_to_desktop():
        logger.info('go_back_to_desktop running...')
        for command in list(range(1, 10)):
            logger.info(f'这是多多视频的 第{command}次退出...')
            duo_duo_driver.back()
        duo_duo_driver.quit()

    def duo_duo_video_script_running_sequence():
        duo_duo_launcher()
        close_ad_window()
        switch_take_money_page()
        check_whether_daily_log_condition()
        enter_refine_cash_page()
        go_back_to_desktop()

    # if __name__ == '__main__':
    #     duo_duo_video_script_running_sequence()

    duo_duo_video_script_running_sequence()

# duo_duo_general_content()