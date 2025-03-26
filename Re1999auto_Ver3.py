import pyautogui as pa
import cv2
import tkinter as tk
import numpy as np
import time



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



#启动
def play():
    global var
    var = "启动游戏"
    label.config(text="正在进行： " + f"{var}")

    #启动
    click_on_image('./pic/m.png')

    time.sleep(20)

    click_on_image('./pic/1999.png')

    time.sleep(25)

    click_on_image('./pic/play.png')

    time.sleep(10)

    # 每日签到
    pa.click(910,210,clicks=3, interval=3)
    time.sleep(1)
    pa.click(button="right",clicks=1)
    pa.click(910, 210, clicks=4, interval=3)


    # 活动签到

    # 公告关闭

    var = "已完成"
    label.config(text="正在进行： " + f"{var}")




#荒原
def manor():
    global var
    var = "荒原"
    label.config(text="正在进行： " + f"{var}")
    #打开荒原
    click_on_image('./pic/manor.png')
    time.sleep(10)

    #尘微与厘
    click_on_image('./pic/experience.png')
    time.sleep(5)

    click_on_image('./pic/coin.png')
    time.sleep(5)

    #好感
    click_on_image('./pic/opinion.png')
    time.sleep(5)

    #工厂
    #收取
    click_on_image('./pic/pro.png')
    time.sleep(5)

    click_on_image('./pic/gain.png')
    time.sleep(5)

    # ？
    pa.click(button='right')
    time.sleep(5)

    click_on_image('./pic/mojinghouse.png')
    time.sleep(3)

    click_on_image('./pic/redact.png')
    time.sleep(2)

    #休息安置
    click_on_image('./pic/remove.png')
    time.sleep(1)

    # 第五个工作魔精的位置
    pa.click(840, 890, 5, 0.7)
    time.sleep(1)

    pa.click(button='middle')
    time.sleep(1)

    click_on_image('./pic/production.png')
    time.sleep(1.5)

    click_on_image('./pic/batchpro.png')
    time.sleep(1.5)

    click_on_image('./pic/batchput.png')
    time.sleep(1.5)

    click_on_image('./pic/batchmojing.png')
    time.sleep(1.5)

    pa.moveTo(540, 600)
    pa.mouseDown(button='left')
    pa.dragTo(1400, 600, duration=1)
    pa.mouseUp(button='left')
    time.sleep(3)

    pa.click(button='middle', clicks=3, interval=2)
    time.sleep(1.5)
    pa.click(button='right')
    time.sleep(5)

    var = "已完成"
    label.config(text="正在进行： " + f"{var}")

#心相
def xinxiang():
    global var
    var = "心相"
    label.config(text="正在进行： " + f"{var}")
    #进入
    click_on_image('./pic/entrance.png')
    time.sleep(2)

    click_on_image('./pic/resource.png')
    time.sleep(2)

    click_on_image('./pic/volition.png')
    time.sleep(2)

    click_on_image('./pic/volition07.png')
    time.sleep(2)

    click_on_image('./pic/letsgo.png')
    time.sleep(5)

    #开始战斗
    click_on_image('./pic/3re.png')
    time.sleep(45)

    click_on_image('./pic/victory.png')
    time.sleep(5)
    #返回主界面
    pa.click(button='right')
    time.sleep(5)

    var = "已完成"
    label.config(text="正在进行： " + f"{var}")



#金币
def gold():
    global var
    var = "金币"
    label.config(text="正在进行： " + f"{var}")
    #进入
    click_on_image('./pic/entrance.png')
    time.sleep(2)

    click_on_image('./pic/resource.png')
    time.sleep(2)

    #金币
    click_on_image('./pic/gcoin.png')
    time.sleep(2)

    click_on_image('./pic/gcoin06.png')
    time.sleep(2)

    click_on_image('./pic/letsgo.png')
    time.sleep(5)

    #开始战斗
    click_on_image('./pic/3re.png')
    time.sleep(30)

    click_on_image('./pic/victory.png')
    time.sleep(5)

    click_on_image('./pic/3re.png')
    time.sleep(30)

    click_on_image('./pic/victory.png')
    time.sleep(5)

    #返回主界面
    pa.click(button='right')
    time.sleep(5)

    var = "已完成"
    label.config(text="正在进行： " + f"{var}")



#循环（金币）
def gold_re():
    global var
    var = "金币循环"
    label.config(text="正在进行： " + f"{var}")
    #进入
    click_on_image('./pic/entrance.png')
    time.sleep(2)

    click_on_image('./pic/resource.png')
    time.sleep(2)

    #金币
    click_on_image('./pic/gcoin.png')
    time.sleep(2)

    click_on_image('./pic/gcoin06.png')
    time.sleep(2)

    click_on_image('./pic/letsgo.png')
    time.sleep(5)

    #开始战斗
    click_on_image('./pic/3re.png')
    time.sleep(30)

    click_on_image('./pic/victory.png')
    time.sleep(5)

    click_on_image('./pic/3re.png')
    time.sleep(30)

    click_on_image('./pic/victory.png')
    time.sleep(5)

    #返回主界面
    pa.click(button='right')
    time.sleep(5)

    var = "已完成"
    label.config(text="正在进行： " + f"{var}")

    gold_re()


#微尘
def mote():
    global var
    var = "微尘"
    label.config(text="正在进行： " + f"{var}")

    # 进入
    click_on_image('./pic/entrance.png')
    time.sleep(2)
    click_on_image('./pic/resource.png')
    time.sleep(2)

    # 微尘
    click_on_image("./pic/mote.png")
    time.sleep(2)

    click_on_image('./pic/mote06.png')
    time.sleep(2)

    click_on_image('./pic/letsgo.png')
    time.sleep(5)

    # 开始战斗
    click_on_image('./pic/3re.png')
    time.sleep(30)

    click_on_image('./pic/victory.png')
    time.sleep(5)

    click_on_image('./pic/3re.png')
    time.sleep(30)

    click_on_image('./pic/victory.png')
    time.sleep(5)

    # 返回主界面
    pa.click(button='right')
    time.sleep(5)

    var = "已完成"
    label.config(text="正在进行： " + f"{var}")


#（循环）微尘
def mote_re():
    global var
    var = "微尘"
    label.config(text="正在进行： " + f"{var}")

    # 进入
    click_on_image('./pic/entrance.png')
    time.sleep(2)
    click_on_image('./pic/resource.png')
    time.sleep(2)

    # 微尘
    click_on_image("./pic/mote.png")
    time.sleep(2)

    click_on_image('./pic/mote06.png')
    time.sleep(2)

    click_on_image('./pic/letsgo.png')
    time.sleep(5)

    # 开始战斗
    click_on_image('./pic/3re.png')
    time.sleep(30)

    click_on_image('./pic/victory.png')
    time.sleep(5)

    click_on_image('./pic/3re.png')
    time.sleep(30)

    click_on_image('./pic/victory.png')
    time.sleep(5)

    # 返回主界面
    pa.click(button='right')
    time.sleep(5)

    var = "已完成"
    label.config(text="正在进行： " + f"{var}")

    mote_re()


#材料
def chapter4act21():
    global var
    var = "421"
    label.config(text="正在进行： " + f"{var}")
    #进入
    click_on_image('./pic/entrance.png')
    time.sleep(2)

    #拖动
    pa.mouseDown(200,520,button="left")
    pa.dragTo(1730,520,duration=3)
    pa.mouseUp(button="left")
    time.sleep(2)

    #章节
    click_on_image('./pic/chapter4.png')
    time.sleep(2)

    #拖动
    pa.mouseDown(200, 820, button="left")
    pa.dragTo(1730, 820, duration=3)
    pa.mouseUp(button="left")
    time.sleep(2)

    #21
    click_on_image('./pic/421.png')
    time.sleep(2)

    #厄运
    pa.click(1630,400,1,duration=1)
    time.sleep(2)

    click_on_image('./pic/misgo.png')
    time.sleep(5)

    #开始战斗
    click_on_image('./pic/4re.png')
    time.sleep(40)

    click_on_image('./pic/victory.png')
    time.sleep(5)

    #返回主界面
    pa.click(button='right')
    time.sleep(5)

    var = "已完成"
    label.config(text="正在进行： " + f"{var}")



#唱片机
def record_player():
    global var
    var = "唱片机"
    label.config(text="正在进行： " + f"{var}")
    # 进入
    time.sleep(2)
    pa.click(button='right')
    time.sleep(2)
    #领取
    click_on_image('./pic/rerecord.png')
    time.sleep(7)
    # 返回主界面
    pa.click(button='right')
    time.sleep(5)

    var = "已完成"
    label.config(text="正在进行： " + f"{var}")


#任务
def task():
    global var
    var = "任务"
    label.config(text="正在进行： " + f"{var}")
    # 进入
    click_on_image('./pic/task.png')
    time.sleep(3)
    #领取
    click_on_image('./pic/allre.png')
    time.sleep(5)
    pa.click(button='right')
    time.sleep(3)

    click_on_image('./pic/weekact.png')
    time.sleep(1)
    click_on_image('./pic/allre.png')
    time.sleep(5)
    pa.click(button='right')
    time.sleep(3)

    # 返回主界面
    pa.click(button='right')
    time.sleep(5)

    var = "任务已完成"
    label.config(text="正在进行： " + f"{var}")




#活动


#总开关
def start_select(selected_modules):
    if selected_modules["manor"].get() == True:
        manor()
    if selected_modules["xinxiang"].get() == True:
        xinxiang()
    if selected_modules["gold"].get() == True:
        gold()
    if selected_modules["mote"].get() == True:
        mote()
    if selected_modules["record_player"].get() == True:
        record_player()
    if selected_modules["task"].get() == True:
        task()
    if selected_modules["gold_re"].get() == True:
        gold_re()
    if selected_modules["mote_re"].get() == True:
        mote_re()



#总开关
def Start():
    play()
    manor()
    xinxiang()
    gold()
    record_player()
    task()

    global var
    var = "结束"
    label.config(text="正在进行： " + f"{var}")

#跳过游戏启动与开始界面的游戏过程
def playing():

    manor()
    xinxiang()
    gold()
    record_player()
    task()

    global var
    var = "结束"
    label.config(text="正在进行： " + f"{var}")


#窗口


root = tk.Tk()
root.title("重返未来：1999 日常自动")
root.geometry("400x550+1510+90")



#变量
var = " "

selected_modules = {
                    "manor": tk.BooleanVar(),
                    "xinxiang": tk.BooleanVar(),
                    "gold": tk.BooleanVar(),
                    "mote": tk.BooleanVar(),
                    "record_player": tk.BooleanVar(),
                    "task":tk.BooleanVar(),
                    "gold_re": tk.BooleanVar(),
                    "mote_re": tk.BooleanVar(),
                    }


# def v():
#     global var
#     var = "v"
#     label.config(text="正在进行： "+f"{var}")


# 模块选择

tk.Checkbutton(root, text="荒原", variable=selected_modules["manor"]).pack()
tk.Checkbutton(root, text="心相", variable=selected_modules["xinxiang"]).pack()
tk.Checkbutton(root,text="金币",variable=selected_modules["gold"]).pack()
tk.Checkbutton(root,text="微尘",variable=selected_modules["mote"]).pack()
tk.Checkbutton(root, text="唱片机", variable=selected_modules["record_player"]).pack()
tk.Checkbutton(root, text="任务", variable=selected_modules["task"]).pack()
tk.Checkbutton(root,text="金币循环",variable=selected_modules["gold_re"]).pack()
tk.Checkbutton(root,text="微尘循环",variable=selected_modules["mote_re"]).pack()


#标签

label = tk.Label(root, text="正在进行： "+f"{var}", font=("Arial", 14))
label.pack(pady=20)



#按钮

# b0 = tk.Button(root,text='Start',width=20,height=3,command=Start)
# b0.pack()

# b1 = tk.Button(root, text="Play", width=20, height=3, command=play)
# b1.pack()
#
# b2 = tk.Button(root, text="Playing", width=20, height=3, command=playing)
# b2.pack()

# b3 = tk.Button(root,text='manor',width=20,height=3,command=manor)
# b3.pack()
#
# b4 = tk.Button(root,text='xinxiang',width=20,height=3,command=xinxiang)
# b4.pack()

#b5 = tk.Button(root,text='materials_re',width=20,height=3,command=materials_re)
#b5.pack()

b6 = tk.Button(root,text="421",width=10, height=1, command=chapter4act21)
b6.pack()

b7 = tk.Button(root, text="Start_select", width=20, height=3, command=lambda: start_select(selected_modules))
b7.pack()


# 进入消息循环
root.mainloop()

