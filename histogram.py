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

with open('data.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    column = [row[4] for row in reader]
    print(column)
    print(len(column))

counts = Counter(column)
k = counts.most_common(len(counts))

x = []
y = []

for i in k:
    x.append(i[0])
    y.append(i[1])
plt.rcParams['font.sans-serif'] = ['SimHei']  # 步骤一（替换sans-serif字体）
plt.title('评价统计', FontProperties=font)
a = plt.bar(x, y)
autolabel(a)

plt.savefig("filename.png")
plt.show()
