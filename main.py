# -*- coding: utf-8 -*-

# @Author  : Pu Zhiwei
# @Time    : 2021-09-02 20:29

from PIL import Image
import os
import matplotlib.pyplot as plt
from paddleocr import PaddleOCR, draw_ocr
from paddleocr.paddleocr import main
import pyperclip
import pyautogui
import time
import webbrowser
import urllib.parse


# 鼠标位置
currentMouseX, currentMouseY = 60, 282

# 截图获取当前题目
def pull_screenshot():
    os.system('adb shell screencap -p /sdcard/screenshot.png')
    os.system('adb pull /sdcard/screenshot.png .')

# 移动鼠标到搜索框搜索
def MoveMouseToSearch():
    # duration 参数，移动时间，即用时0.1秒移动到对应位置
    pyautogui.moveTo(currentMouseX, currentMouseY, duration=0.1)
    # 左键点击
    pyautogui.click()
    pyautogui.click()
    # 模拟组合键，粘贴
    pyautogui.hotkey('ctrl', 'v')

# 扩充问题
def AddText(list, length, text):
    if length >= 3:
        return text + list[3]
    
# 打开浏览器
def open_webbrowser(question):
    webbrowser.open('https://baidu.com/s?wd=' + urllib.parse.quote(question))

        

# 显示所识别的题目
def ShowAllQuestionText(list):
    text = ""
    for str in list:
        text += str
    print(text)



if __name__ == "__main__":
    while True:
        print("\n\n请将鼠标放在Word的搜索框上，三秒后脚本将自动获取Word搜索框位置！\n\n")
        # 延时三秒输出鼠标位置
        time.sleep(3)
        # 获取当前鼠标位置
        currentMouseX, currentMouseY = pyautogui.position()
        print('当前鼠标位置为: {0} , {1}'.format(currentMouseX, currentMouseY))
        start = input("按y键程序开始运行，按其他键重新获取搜索框位置：")
        if start == 'y':
            break

    while True:
        t = time.perf_counter()
        pull_screenshot()
        img = Image.open("./screenshot.png")
        # 切割问题区域
        # (起始点的横坐标，起始点的纵坐标，宽度，高度）
        question  = img.crop((10, 400, 1060, 1000))
        # 保存问题区域
        question.save("./question.png")


        # 加载 PaddleOCR
        # Paddleocr目前支持中英文、英文、法语、德语、韩语、日语，可以通过修改lang参数进行切换
        # 参数依次为`ch`, `en`, `french`, `german`, `korean`, `japan`。

        # 自定义模型地址
        # det_model_dir='./inference/ch_ppocr_server_v2.0_det_train', 
        #                rec_model_dir='./inference/ch_ppocr_server_v2.0_rec_pre',
        #                cls_model_dir='./inference/ch_ppocr_mobile_v2.0_cls_train',
        ocr = PaddleOCR(use_angle_cls=False, 
                        lang="ch", 
                        show_log=False
                        )  # need to run only once to download and load model into memory
        img_path = 'question.png'
        result = ocr.ocr(img_path, cls=False)

        questionList = [line[1][0] for line in result]
        length = len(questionList)
        text = ""
        if length < 1:
            text = questionList[0]
        elif length == 2:
            text = questionList[1]
        else:
            text = questionList[1] + questionList[2]

        print('\n\n')
        ShowAllQuestionText(questionList)
        # 将结果写入剪切板
        pyperclip.copy(text)
        # 点击搜索
        MoveMouseToSearch()
        
        # 计算时间
        print('\n\n')
        end_time3 = time.perf_counter()
        print('用时: {0}'.format(end_time3 - t))
        
        go = input('输入回车继续运行,输入 e 打开浏览器搜索，输入 a 增加题目长度，输入 n 结束程序运行： ')
        if go == 'n':
            break
  
        if go == 'a':
            text = AddText(questionList, length, text)
            pyperclip.copy(text)
            # 点击搜索
            MoveMouseToSearch()
            stop = input("输入回车继续")
        elif go == 'e':
            # 打开浏览器
            open_webbrowser(text)
            stop = input("输入回车继续")
            
    


        print('\n------------------------\n\n')
