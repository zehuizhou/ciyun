import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from collections import Counter
import csv


# 设置柱状图上面的值
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x()+rect.get_width()/1.5-0.2, 1.03*height, '%s' % int(height))


font = FontProperties(fname=r"simsun.ttc", size=20)

# 指定图像的宽和高，单位为英寸，dpi参数指定绘图对象的分辨率，即每英寸多少个像素，缺省值为80
fig = plt.figure(figsize=(20, 8), dpi=80)

k = [('少年', 164), ('真的', 152), ('好', 145), ('冬雨', 127), ('世界', 126), ('校园', 120), ('保护', 117), ('没有', 108), ('希望', 104), ('演技', 95)]

x = []
y = []

for i in k:
    x.append(i[0])
    y.append(i[1])
plt.rcParams['font.sans-serif'] = ['SimHei']  # 步骤一（替换sans-serif字体）
plt.title('词频统计', FontProperties=font)
a = plt.bar(x, y)
autolabel(a)
plt.show()
