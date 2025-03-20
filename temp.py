
import pyautogui as pa
import cv2
import tkinter as tk
import numpy as np
import time



# pa.click(910,210,clicks=3, interval=3)
# time.sleep(1)
# pa.click(button="right",clicks=1)
# pa.click(910, 210, clicks=4, interval=3)

def Admission():
    print(5)

def play():
    print(1)









# 总开关
def start(selected_modules):
    if selected_modules["play"] == True:
        print()
    if "manor" in selected_modules:
        print(selected_modules["manor"].get())
    if "xinxiang" in selected_modules:
        print(2)
    if selected_modules["Admission"].get() == True:
        Admission()


# 窗口
root = tk.Tk()
root.title("重返未来：1999 日常自动")
root.geometry("400x300+1+1")

# 变量
var = tk.StringVar(value="等待中...")

selected_modules = {"play": tk.BooleanVar(),
                    "manor": tk.BooleanVar(),
                    "xinxiang": tk.BooleanVar(),
                    "Admission":tk.BooleanVar()
                    }

# 状态标签
label = tk.Label(root, textvariable=var, font=("Arial", 14))
label.pack(pady=20)

# 模块选择
tk.Checkbutton(root, text="荒原", variable=selected_modules["manor"]).pack(anchor=tk.W)
tk.Checkbutton(root, text="心相", variable=selected_modules["xinxiang"]).pack(anchor=tk.W)
tk.Checkbutton(root, text="", variable=selected_modules["materials"]).pack(anchor=tk.W)
tk.Checkbutton(root, text="", variable=selected_modules["record_player"]).pack(anchor=tk.W)
tk.Checkbutton(root, text="", variable=selected_modules["task"]).pack(anchor=tk.W)



# 启动按钮
b0 = tk.Button(root, text="Start", width=20, height=3, command=lambda: start(selected_modules))
b0.pack()

# 进入消息循环
root.mainloop()

