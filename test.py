import os
# 1. 先打印实际拼接的路径，确认是否正确
img_path = "./pic/4re.png"
print("实际路径：", img_path)
print("路径是否存在：", os.path.exists(img_path))
print("是否是文件：", os.path.isfile(img_path))

# 2. 推荐使用绝对路径（避免相对路径坑）
abs_path = os.path.abspath(img_path)
print("绝对路径：", abs_path)
print("绝对路径是否存在：", os.path.exists(abs_path))