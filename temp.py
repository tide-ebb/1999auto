import tkinter as tk

# 主窗口初始化
root = tk.Tk()
root.title("功能模块选择")
root.geometry("400x500")  # 设置窗口大小，可根据需要调整

# 字体配置（你原代码中用到的font_config，这里给出示例）
font_config = ("微软雅黑", 12)

# 定义模块名称映射（英文key: 中文显示文本），便于维护
module_mapping = {
    "manor": "荒原",
    "xinxiang": "心相",
    "gold": "金币",
    "mote": "微尘",
    "act": "活动",
    "record_player": "唱片机",
    "task": "任务",
    "gold_re": "金币循环",
    "mote_re": "微尘循环",
    "fight": "战斗循环"
    # "421": "421模块"  # 如果需要启用，取消注释即可
}

# 初始化选中状态的字典
selected_modules = {key: tk.BooleanVar() for key in module_mapping.keys()}

# 创建模块选择的框架
frame_modules = tk.Frame(root)
frame_modules.pack(pady=10, padx=20, fill="x")

# 循环创建复选框，替代重复的代码
for key, text in module_mapping.items():
    cb = tk.Checkbutton(
        frame_modules,
        text=text,
        variable=selected_modules[key],
        font=font_config
    )
    cb.pack(anchor="center", pady=2)

# 示例：获取选中状态的函数（方便你后续使用）
def get_selected_modules():
    """返回所有被选中的模块名称列表"""
    selected = []
    for key, var in selected_modules.items():
        if var.get():
            selected.append(key)
    return selected

# 测试按钮（可选，用于验证选中状态）
def show_selected():
    # global selected_modules
    selected = get_selected_modules()
    print("选中的模块：", selected)

    for key in selected:
        selected_modules[key].set(False)

test_btn = tk.Button(root, text="查看选中的模块", command=show_selected, font=font_config)
test_btn.pack(pady=20)

# 启动主循环
root.mainloop()