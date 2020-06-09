import pandas
import matplotlib.pyplot as plt
import csv

f = open('测试成绩统计.csv')
c = csv.reader(f)
data_list = [i for i in c]
f.close()

ret_list = []
for k,data in enumerate(data_list):
    if k == 0:
        data.append('平均成绩')
        ret_list.append(data)
        continue
    sum_score = 0
    for s_k,tmp in enumerate(data):
        if s_k == 0:
            continue
        sum_score += int(tmp)
    avg_score = sum_score / 8.0
    data.append(avg_score)
    ret_list.append(data)
f = open('统计平均成绩.csv','w',newline='')
c = csv.writer(f)
for data in ret_list:
    c.writerow(data)
f.close()

f = open('统计平均成绩.csv','r')
c = csv.reader(f)
score_list = [i for i in c]
f.close()
x_list = ['60分以下','60-70分','70-80分','80-90分','90分以上']
y_list = [0,0,0,0,0]
for k,data in enumerate(score_list):
    if k == 0:
        continue
    score = float(data[-1])
    if score < 60:
        y_list[0] += 1
    elif score >= 60 and score < 70:
        y_list[1] += 1
    elif score >= 70 and score < 80:
        y_list[2] += 1
    elif score >= 80 and score < 90:
        y_list[3] += 1
    else:
        y_list[4] += 1
print('平均成绩中60分以下的有{}人，60-70分的有{}人，70-80分的有{}人，80-90分的有{}人，90分以上的有{}人'.format(y_list[0],y_list[1],y_list[2],y_list[3],y_list[4]))
plt.rcParams['font.sans-serif'] = ['KaiTi']
for i in range(len(y_list)):
    plt.text(i,y_list[i],y_list[i])
plt.xlabel('平均分')
plt.ylabel('人数')
plt.xticks((range(len(x_list))), x_list)
plt.yticks(range(25))
plt.title('成绩平均分各分数段柱状图')
plt.bar(x_list,y_list,align='center',color='red')
plt.savefig('各个分数段人数.png')
plt.show()


