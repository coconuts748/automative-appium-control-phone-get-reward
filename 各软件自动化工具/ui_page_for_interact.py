from 已完成.各软件自动化工具.bai_du_script import bai_du_general_content
from 已完成.各软件自动化工具.dian_tao_script import dian_tao_general_content
from 已完成.各软件自动化工具.dou_yin_script import dou_yin_general_script
from 已完成.各软件自动化工具.dou_yin_volcano_version_script import dou_yin_volcano_general_content
from 已完成.各软件自动化工具.duo_duo_cideo_script import duo_duo_general_content
from 已完成.各软件自动化工具.hong_guo_script import hong_guo_general_content
from 已完成.各软件自动化工具.kuai_shou_script import kuai_shou_general_content
from 已完成.各软件自动化工具.watermelon_script import watermelon_general_content
from 已完成.各软件自动化工具.control_all_scripts_frame import control_all_scripts_frame
import tkinter as tk
from tkinter import messagebox,ttk
from loguru import logger
import time

local_time  = time.asctime(time.localtime(time.time()))

class MainPage:
    def __init__(self):
        logger.info('初始主界面运行中....')

        def ask_whether_quit_main_page():
            if messagebox.askyesno('提示','是否确认退出?'):
                main_original_root.destroy()

        main_original_root = tk.Tk()
        main_original_root.title('主界面菜单 ')
        main_original_root.geometry('300x200')
        main_original_root.update_idletasks()


        ttk.Label(main_original_root,text='点击上面的按钮即可进行相对应的进程...').grid(row=23,column=0,columnspan=50)
        ttk.Label(main_original_root,text=f'当前时间为:{local_time}').grid(row=25,column=0,columnspan=50)

        single_bai_du_process = ttk.Button(main_original_root,text='百度极速版',command=bai_du_general_content)
        single_bai_du_process.grid(row=3,column=0,columnspan=6,rowspan=3)

        single_dian_tao_process = ttk.Button(main_original_root,text='点淘',command=dian_tao_general_content)
        single_dian_tao_process.grid(row=3,column=100,columnspan=6,rowspan=3)

        single_dou_yin_process = ttk.Button(main_original_root,text='抖音极速版',command=dou_yin_general_script)
        single_dou_yin_process.grid(row=7,column=0,columnspan=6,rowspan=3)

        single_dou_yin_volcano_process = ttk.Button(main_original_root,text='抖音火山版',command=dou_yin_volcano_general_content)
        single_dou_yin_volcano_process.grid(row=7,column=100,columnspan=6,rowspan=3)

        single_duo_duo_volcano_process = ttk.Button(main_original_root,text='多多视频',command=duo_duo_general_content)
        single_duo_duo_volcano_process.grid(row=11,column=0,columnspan=6,rowspan=3)

        single_hong_guo_process = ttk.Button(main_original_root,text='红果视频',command=hong_guo_general_content)
        single_hong_guo_process.grid(row=11,column=100,columnspan=6,rowspan=3)

        single_kuai_shou_process = ttk.Button(main_original_root,text='快手',command=kuai_shou_general_content)
        single_kuai_shou_process.grid(row=16,column=0,columnspan=6,rowspan=3)

        single_watermelon_process = ttk.Button(main_original_root,text='西瓜视频',command=watermelon_general_content)
        single_watermelon_process.grid(row=16,column=100,columnspan=6,rowspan=3)

        single_control_all_process = ttk.Button(main_original_root,text='统一运行',command=control_all_scripts_frame)
        single_control_all_process.grid(row=19,column=0,columnspan=6,rowspan=3)

        whether_quit_main_page = ttk.Button(main_original_root,text='退出',command=ask_whether_quit_main_page)
        whether_quit_main_page.grid(row=19,column=100,columnspan=6,rowspan=3)

        main_original_root.mainloop()

main_page = MainPage()

