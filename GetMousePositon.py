# -*- coding: utf-8 -*-

# @Author  : Pu Zhiwei
# @Time    : 2021-09-02 20:29
# @desc    : 获取需要点击的鼠标位置

import pyautogui

import time

# 延时三秒输出鼠标位置
time.sleep(3)

# 获取当前鼠标位置
currentMouseX, currentMouseY = pyautogui.position()


print(currentMouseX, currentMouseY)


