import time

from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as e_conditions
from loguru import logger

def dou_yin_general_script():
    options = UiAutomator2Options()
    options.load_capabilities({
        'automationName': 'uiautomator2',
        'platformName': 'Android',
        'deviceName': '10ACBY12RX000UA',
        'noReset': True
    })

    dou_yin_launcher = webdriver.Remote('http://127.0.0.1:4723', options=options)
    wait = WebDriverWait(dou_yin_launcher, 30)

    def enter_dou_yin_application(dou_yin_name):
        logger.info("enter dou_yin_application running......")
        try:
            dou_yin = wait.until((e_conditions.presence_of_element_located(
                (AppiumBy.XPATH, f'//android.widget.TextView[@text="{dou_yin_name}"]'))))
            dou_yin.click()

        except Exception as q:
            logger.error(f'软件启动失败{q}')

    def switch_to_get_cash_page():
        logger.info("switch to get cash page running......")
        try:
            switch_button = wait.until(e_conditions.presence_of_element_located(
                (AppiumBy.XPATH, '//android.widget.ImageView[@resource-id="com.ss.android.ugc.aweme.lite:id/d-t"]')))
            switch_button.click()

        except Exception as s:
            logger.error(f'/d“去赚钱”/d元素未找到:{s}')

    def check_whether_appear_award_box():
        logger.info("check whether appear award box running......")
        try:
            if wait.until(e_conditions.presence_of_element_located(
                    (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="点击领"]'))).get_attribute(
                    'content-desc') == '点击领':
                logger.info('当前宝箱可领取....')
                logger.info('宝箱领取中....')
                award_box = wait.until(e_conditions.presence_of_element_located(
                    (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="点击领"]')))
                award_box.click()

                time.sleep(1)
                dou_yin_launcher.back()

        except Exception as q:
            logger.info(f'无宝箱可领:{q}')

    def check_whether_contain_book_coin():
        logger.info("check whether contain book coin running......")
        try:

            if '已预约' not in wait.until(e_conditions.presence_of_element_located(
                    (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc]'))):
                get_coin_button_source = wait.until(e_conditions.presence_of_element_located((AppiumBy.XPATH,
                                                                                              '//android.widget.HorizontalScrollView/android.widget.LinearLayout/android.view.ViewGroup/android.view.ViewGroup[3]')))
                get_coin_button_source.click()

                time.sleep(1)
                dou_yin_launcher.back()

        except Exception as q:
            logger.info(f'预定金币暂不能领取:{q}')

    def get_salary_page():
        logger.info("get salary page running......")
        logger.info("正在进入提现页面.....")
        try:
            get_cash_button = wait.until(e_conditions.presence_of_element_located((AppiumBy.XPATH,
                                                                                   '//androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[6]')))
            get_cash_button.click()
        except Exception as q:
            logger.error(f'提现页面未找到:{q}')

    def go_back_to_main_page():
        logger.info('go_back_to_main_page running......')
        try:
            for command in list(range(1, 10)):
                logger.info(f'这是抖音极速版的第 {command} 次退出')
                dou_yin_launcher.back()


        except Exception as q:
            logger.error(f'返回桌面失败{q}')

    def prepare_dou_yin_running_script(running_douyin_name):
        enter_dou_yin_application(dou_yin_name=running_douyin_name)
        switch_to_get_cash_page()
        check_whether_appear_award_box()
        check_whether_contain_book_coin()
        get_salary_page()

        go_back_to_main_page()

    def dou_yin_running_sequence():
        prepare_dou_yin_running_script(running_douyin_name='抖音极速版')
        logger.info('抖音极速版运行完毕.....')
        prepare_dou_yin_running_script(running_douyin_name='Ⅱ·抖音极速版')
        logger.info('Ⅱ·抖音极速版运行完毕.....')
        dou_yin_launcher.quit()
    # if __name__ == '__main__':
    #     dou_yin_running_sequence()

    dou_yin_running_sequence()

# dou_yin_general_script()
