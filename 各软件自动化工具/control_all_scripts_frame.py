from 已完成.各软件自动化工具.bai_du_script import bai_du_general_content
from 已完成.各软件自动化工具.dian_tao_script import dian_tao_general_content
from 已完成.各软件自动化工具.dou_yin_script import dou_yin_general_script
from 已完成.各软件自动化工具.duo_duo_cideo_script import duo_duo_general_content
from 已完成.各软件自动化工具.hong_guo_script import hong_guo_general_content
from 已完成.各软件自动化工具.kuai_shou_script import kuai_shou_general_content
from 已完成.各软件自动化工具.watermelon_script import watermelon_general_content
from 已完成.各软件自动化工具.dou_yin_volcano_version_script import dou_yin_volcano_general_content
from loguru import logger
import time


all_running_scripts_sequences = []

def control_all_scripts_frame():
    try:
        logger.info('快手运行中.....')
        kuai_shou_general_content()
    except Exception as e:
        logger.error(e)
    try:
        logger.info('抖音极速版运行中....')
        dou_yin_general_script()
    except Exception as e:
        logger.error(e)
    try:
        logger.info('抖音火山版运行中....')
        dou_yin_volcano_general_content()
    except Exception as e:
        logger.error(e)
    try:
        logger.info('西瓜视频运行中....')
        watermelon_general_content()
    except Exception as e:
        logger.error(e)
    try:
        logger.info('百度极速版运行中....')
        bai_du_general_content()
    except Exception as e:
        logger.error(e)
    try:
        logger.info('多多视频运行中....')
        duo_duo_general_content()
    except Exception as e:
        logger.error(e)
    try:
        logger.info('红果视频运行中....')
        hong_guo_general_content()
    except Exception as e:
        logger.error(e)
    try:
        logger.info('点淘运行中....')
        dian_tao_general_content()
    except Exception as e:
        logger.error(e)
    logger.info('所有脚本进程已完成!!')

# control_all_scripts_frame()
