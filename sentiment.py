from snownlp import SnowNLP
import csv

with open('data.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    column = [row[3] for row in reader]


# 情感分析
def sentiment(content):
    s = SnowNLP(str(content))
    return s.sentiments

sentiment_list = []
for comment in column:
    score = sentiment(comment)
    sentiment_list.append(score)

print(sentiment_list)

# 重新生成数据
with open("data.csv", 'r', newline="", encoding="utf-8") as f:
    reader = csv.reader(f)
    newdata = []
    i = -1
    for row in reader:
        row.append(sentiment_list[i+1])
        print(row)
        newdata.append(row)
        i += 1

# 重新写入数据
with open("data.csv", 'w', newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    c = csv.writer(f)
    for i in newdata:
        c.writerow(i)
