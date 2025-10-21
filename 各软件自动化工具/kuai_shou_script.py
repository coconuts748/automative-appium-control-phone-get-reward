from appium.webdriver.common.appiumby import AppiumBy
from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.common import ElementNotInteractableException
from selenium.webdriver.support import expected_conditions as e_conditions
from selenium.webdriver.support.ui import WebDriverWait
import time
from loguru import logger

def kuai_shou_general_content():
    options = UiAutomator2Options()
    options.load_capabilities({
        'automationName': 'uiautomator2',
        'platformName': 'Android',
        'deviceName': '10ACBY12RX000UA',
        'noReset': True
    })

    kuai_shou_launcher = webdriver.Remote('http://127.0.0.1:4723', options=options)
    wait = WebDriverWait(kuai_shou_launcher, 30)

    #####0000进入软件0000######
    def enter_application(kuai_shou_name):
        logger.info("enter application running.......")
        application = kuai_shou_launcher.find_element(AppiumBy.XPATH,
                                                      f'//android.widget.TextView[@text="{kuai_shou_name}"]')
        application.click()

    #####0000进入软件0000######

    #####1111跳转至‘去赚钱’选项1111######
    def switch_to_go_to_take_cash():
        logger.info('switch_to_go_to_take_cash running.......')
        switch_button = wait.until(e_conditions.presence_of_element_located(
            (AppiumBy.XPATH, '//android.widget.CheckedTextView[@text="去赚钱"]')))
        switch_button.click()

    #####1111跳转至‘去赚钱’选项1111######

    #####3333提现操作3333######
    def get_cash():
        logger.info('get_cash running.......')
        try:
            get_cash_button = wait.until(
                e_conditions.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@text="领现金"]')))
            get_cash_button.click()

            ######后续#######
            print()
            ######后续#######

        except Exception as e:
            logger.info(f'提现元素定位失败:{e}')

    #####3333提现操作3333######

    ########2222提示弹幕与宝箱情况2222###########
    def check_whether_ad_page_condition():
        logger.info('check_whether_ad_page_condition running.......')
        try:
            if wait.until(e_conditions.presence_of_element_located(
                    (AppiumBy.XPATH, '//android.widget.TextView[@text="翻倍任务开启"]'))).get_attribute(
                    'text') == '翻倍任务开启':  # 可能弹出翻倍弹幕.....
                ad_close_button = wait.until(e_conditions.presence_of_element_located(
                    (AppiumBy.XPATH, '//android.view.View[.//android.widget.Image]')))

                ad_close_button.click()  # 关闭第一个弹幕....

        except Exception as a:
            logger.info(f'无第一个弹幕:{a}')

    def check_whether_appear_award_box():
        logger.info('check_whether_appear_award_box running.......')
        try:
            if '可领' in wait.until(e_conditions.presence_of_element_located(
                    (AppiumBy.XPATH, '//android.view.View[.//android.widget.Button[@text]]'))).get_attribute('text'):
                kuai_shou_launcher.find_element(AppiumBy.XPATH,
                                                '//android.view.View[.//android.widget.Button[@text]]').click()

                quit_ad_button = wait.until(e_conditions.presence_of_element_located(
                    (AppiumBy.XPATH, '//android.view.View[.//android.widget.Image]')))
                quit_ad_button.click()  # 返回“去赚钱”页面
        except Exception as b:
            logger.info(f'无宝箱奖励:{b}')

    ########2222提示弹幕与宝箱情况2222###########



    def go_back_to_desktop():
        logger.info('go_back_to_desktop running...')
        for command in list(range(1, 10)):
            logger.info(f'这是快手的 第{command}次退出...')
            kuai_shou_launcher.back()

    def prepare_kuai_shou_running_script(kuai_shou_detail_name):
        enter_application(kuai_shou_name=kuai_shou_detail_name)
        switch_to_go_to_take_cash()
        check_whether_ad_page_condition()
        check_whether_appear_award_box()
        get_cash()
        time.sleep(3)
        go_back_to_desktop()

    def kuai_shou_running_sequence():
        prepare_kuai_shou_running_script(kuai_shou_detail_name='快手极速版')
        prepare_kuai_shou_running_script(kuai_shou_detail_name='Ⅱ·快手极速版')
        kuai_shou_launcher.quit()

    # if __name__ == '__main__':
    #     kuai_shou_running_sequence()
    kuai_shou_running_sequence()

# kuai_shou_general_content()



