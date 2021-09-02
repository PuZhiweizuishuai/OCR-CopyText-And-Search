# 截图OCR识别后搜索题目获取答案

## 使用说明

- 1.首先使用运行`python GetMousePositon.py`获取Word文件搜索框位置，运行该程序后，请将鼠标放置到Word的搜索框上，3秒后屏幕上会显示出当前鼠标坐标。

- 2.修改`main.py`的`currentMouseX, currentMouseY`数值，将刚刚屏幕上显示的鼠标位置复制到变量后，例如`currentMouseX, currentMouseY = 46, 275`

- 3.最后`python main.py`运行脚本


## 运行依赖

- 安装[Python3.6+](https://www.python.org/downloads/)， [Adb](https://developer.android.google.cn/studio/command-line/adb)

- 安装 PaddleOCR

```bash
pip install "paddleocr>=2.0.1" # 推荐使用2.0.1+版本
```

- 安装 PaddlePaddle(注意此版本为CPU版本，如需GPU版本请查看[PaddlePaddle文档](https://www.paddlepaddle.org.cn/install/quick?docurl=/documentation/docs/zh/install/pip/windows-pip.html))

```bash
python -m pip install paddlepaddle -i https://mirror.baidu.com/pypi/simple
```

安装完成后您可以使用 `python` 进入python解释器，输入`import paddle` ，再输入 `paddle.utils.run_check()`

如果出现`PaddlePaddle is installed successfully!`，说明您已成功安装。

- 安装 pyperclip 模块，负责操作剪切板

```
pip install pyperclip
```

- 安装 pyautogui 模块，操作鼠标键盘

```bash
pip install pyautogui
```