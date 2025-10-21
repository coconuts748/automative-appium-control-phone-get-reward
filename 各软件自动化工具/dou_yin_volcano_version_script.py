import time

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as e_conditions
from loguru import logger

def dou_yin_volcano_general_content():
    options = UiAutomator2Options()
    options.load_capabilities({
        'automationName': 'uiautomator2',
        'platformName': 'Android',
        'deviceName': '10ACBY12RX000UA',
        'noReset': True
    })

    dou_yin_volcano_driver = webdriver.Remote('http://127.0.0.1:4723', options=options)
    wait = WebDriverWait(dou_yin_volcano_driver, 30)

    def dou_yin_volcano_launcher():
        logger.info('dou_yin_volcano_launcher running...')
        try:
            dou_yin_volcano_button = wait.until(e_conditions.presence_of_element_located(
                (AppiumBy.XPATH, '//android.widget.TextView[@text="抖音火山版"]')))
            dou_yin_volcano_button.click()

        except Exception as ex:
            logger.error(f'抖音火山版启动失败 :{ex}')

    def switch_to_welfare_page():
        logger.info('switch_to_welfare_page running...')
        try:
            time.sleep(1)
            logger.info('暂停视频中....')
            time.sleep(5)
            suspend_video_position = [(780, 813)]
            dou_yin_volcano_driver.tap(suspend_video_position)

            logger.info('进入福利中心中....')
            switch_page_button = wait.until(e_conditions.presence_of_element_located(
                (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="com.ss.android.ugc.live:id/dl="]')))
            switch_page_button.click()

        except Exception as ex:
            logger.error(f'跳转至福利详细页面错误 :{ex}')

    def inspect_whether_appear_award_box():
        logger.info('inspect_whether_appear_award_box running...')
        try:
            logger.info('进行宝箱领取流程中....')
            awarding_box_position = [(919, 177)]
            quit_award_box_position = [(542, 1724)]
            dou_yin_volcano_driver.tap(awarding_box_position)
            time.sleep(3)
            dou_yin_volcano_driver.tap(quit_award_box_position)

        except Exception as ex:
            logger.error(f'宝箱流程操作出错:{ex}')

    def go_to_refine_coin_page():
        logger.info('go_to_refine_coin_page running...')
        try:
            dou_yin_volcano_button_position = [(900, 400)]
            time.sleep(1)
            dou_yin_volcano_driver.tap(dou_yin_volcano_button_position)


        except Exception as ex:
            logger.error(f'跳转至提现页面错误:{ex}')

    def go_back_to_desktop():
        logger.info('go_back_to_desktop running...')
        for i in list(range(1, 10)):
            logger.info('这是抖音火山版的第 {} 次退出'.format(i))
            dou_yin_volcano_driver.back()
        dou_yin_volcano_driver.quit()


    def dou_yin_volcano_script_running_sequence():
        dou_yin_volcano_launcher()
        switch_to_welfare_page()
        # inspect_whether_appear_award_box()
        go_to_refine_coin_page()
        go_back_to_desktop()

    # if __name__ == '__main__':
    #     dou_yin_volcano_script_running_sequence()

    dou_yin_volcano_script_running_sequence()

# dou_yin_volcano_general_content()
