
import cv2

# #查看版本
# print(cv2.getVersionString())
#
# image = cv2.imread("3re.png")
# #print(image.shape)
# #打印出的（121，83，3）121和83为横行和纵列，3为原色
#
# #显示opencv读取到的数据，显示到一个窗口
# cv2.imshow("image",image)
# #让窗口停留，并等待键盘输入
# cv2.waitKey()


import cv2
import numpy as np
import pyautogui as pa
import time

#find
#def find(t,threshold=0.8)
pic = cv2.imread(t,cv2.IMREAD_COLOR)
screen = np.array(pa.screenshot())
screen = cv2.cvtColor(screen, cv2.COLOR_RGB2BGR)


# 截屏并识别图像，返回坐标
def find_screen(template_path, threshold=0.8):
    template = cv2.imread(template_path, cv2.IMREAD_COLOR)
    if template is None:
        raise ValueError(f"Template image not found at {template_path}")

    screen = np.array(pa.screenshot())
    screen = cv2.cvtColor(screen, cv2.COLOR_RGB2BGR)

    result = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(result)

    if max_val >= threshold:
        h, w, _ = template.shape
        top_left = max_loc
        center_x = top_left[0] + w // 2
        center_y = top_left[1] + h // 2
        return center_x, center_y
    else:
        return None


# 点击图像
def click_on_image(template_path, threshold=0.8, max_attempts=3, retry_delay=5):
    attempt = 0
    while attempt < max_attempts:
        location = find_screen(template_path, threshold)
        if location:
            x, y = location
            pa.click(x, y, clicks=2, duration=1)
            print(f"Clicked at coordinates: ({x}, {y})")
            return
        else:
            print("Image not found on the screen. Retrying...")
            time.sleep(retry_delay)
            attempt += 1

    print("Max attempts reached. Image not found.")

#def action():



#def character():

# click_on_image("c1.png")
# time.sleep(1)
# click_on_image("quniangletsgo.png")
# time.sleep(1)
# click_on_image("jump.png")
# time.sleep(1)
# click_on_image("confirm.png")

click_on_image("c2.png")
time.sleep(1)
click_on_image("quniangletsgo.png")
time.sleep(1)
click_on_image("jump.png")
time.sleep(1)
click_on_image("confirm.png")

#条件，识别是否有剧情然后跳过
if

click_on_image("c3.png")
time.sleep(1)
click_on_image("quniangletsgo.png")
time.sleep(1)
click_on_image("jump.png")
time.sleep(1)
click_on_image("confirm.png")

click_on_image("c4.png")
time.sleep(1)
click_on_image("quniangletsgo.png")
time.sleep(1)
click_on_image("jump.png")
time.sleep(1)
click_on_image("confirm.png")

click_on_image("c5.png")
time.sleep(1)
click_on_image("quniangletsgo.png")
time.sleep(1)
click_on_image("jump.png")
time.sleep(1)
click_on_image("confirm.png")

click_on_image("c6.png")
time.sleep(1)
click_on_image("quniangletsgo.png")
time.sleep(1)
click_on_image("jump.png")
time.sleep(1)
click_on_image("confirm.png")

click_on_image("c7.png")
time.sleep(1)
click_on_image("quniangletsgo.png")
time.sleep(1)
click_on_image("jump.png")
time.sleep(1)
click_on_image("confirm.png")

click_on_image("c8.png")
time.sleep(1)
click_on_image("quniangletsgo.png")
time.sleep(1)
click_on_image("jump.png")
time.sleep(1)
click_on_image("confirm.png")
