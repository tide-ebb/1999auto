import tkinter as tk
import pyautogui as pa
import threading
import time
import cv2
import numpy as np


#控制函数
#截屏并识别图像，返回坐标
def find_screen(template_path, threshold=0.8):
    template = cv2.imread(template_path, cv2.IMREAD_COLOR)
    screen = np.array(pa.screenshot())
    screen = cv2.cvtColor(screen, cv2.COLOR_RGB2BGR)

    result = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    if max_val >= threshold:
        h, w, _ = template.shape
        top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)
        center_x = top_left[0] + w // 2
        center_y = top_left[1] + h // 2
        return center_x, center_y
    else:
        return None


def click_on_image(template_path, threshold=0.8):
    location = find_screen(template_path, threshold)
    if location:
        x, y = location
        pa.click(x, y,2,duration=1)
        print(f"Clicked at coordinates: ({x}, {y})")
    else:
        print("Image not found on the screen.")
        time.sleep(5)
        click_again_image(template_path)


def click_again_image(template_path, threshold=0.8):
    location = find_screen(template_path, threshold)
    if location:
        x, y = location
        pa.click(x, y, 2,duration=1)
        print(f"Clicked at coordinates: ({x}, {y})")
    else:
        print("again.")
        time.sleep(10)
        click_on_image(template_path)


class auto:
    def __init__(self, root):
        self.root = root
        self.root.title("重返未来：1999 日常自动")
        self.root.geometry("500x500")

        # 正在进行显示标签
        self.label = tk.Label(root, text="正在进行： ", font=("Arial", 14))
        self.label.pack(pady=20)



    def manor(self):
        # 打开荒原
        click_on_image('manor.png')
        time.sleep(10)

        # 尘微与厘
        click_on_image('experience.png')
        time.sleep(5)

        click_on_image('coin.png')
        time.sleep(5)

        # 好感
        click_on_image('opinion.png')
        time.sleep(5)

        # 工厂
        # 收取
        click_on_image('pro.png')
        time.sleep(5)

        click_on_image('gain.png')
        time.sleep(5)

        # ？
        pa.click(button='right')
        time.sleep(5)

        click_on_image('mojinghouse.png')
        time.sleep(3)

        click_on_image('redact.png')
        time.sleep(2)

        # 休息安置
        click_on_image('remove.png')
        time.sleep(1)

        # 第五个工作魔精的位置
        pa.click(840, 890, 5, 0.7)
        time.sleep(1)

        pa.click(button='middle')
        time.sleep(1)

        click_on_image('production.png')
        time.sleep(1.5)

        click_on_image('batchpro.png')
        time.sleep(1.5)

        click_on_image('batchput.png')
        time.sleep(1.5)

        click_on_image('batchmojing.png')
        time.sleep(1.5)

        pa.moveTo(540, 600)
        pa.mouseDown(button='left')
        pa.dragTo(1400, 600, duration=1)
        pa.mouseUp(button='left')
        time.sleep(3)

        pa.click(button='middle', clicks=3, interval=2)
        time.sleep(1.5)
        pa.click(button='right')

        # 按钮
        b1 = tk.Button(root, text='荒原', width=20, height=3, command=manor)
        b1.pack()

    def start(self):
        self.root.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    app = auto(root)
