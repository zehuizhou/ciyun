#!/usr/bin/env python
# coding=utf-8
import os
import jieba
import numpy as np
from PIL import Image
from wordcloud import WordCloud, STOPWORDS
import collections  # 词频统计库
import re
import csv

CURDIR = os.path.abspath(os.path.dirname(__file__))
PICTURE = os.path.join(CURDIR, 'ciyun2.jpg')
FONT = os.path.join(CURDIR, 'simsun.ttc')

add_word_list = ['江山娇', '红旗漫', '如何治疗', '死透', '一座塔', '无聊瞎直播', '语料快闪', '恩施生活', '身边事', '水润', '快闪店', '快闪店', 'pop-up', 'POP-UP',
                 'L秒拍视频', '秒拍', '低幼化', '大宗商品']
for word in add_word_list:
    jieba.add_word(word)


def cut_the_words():
    with open('data.csv', 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        column = [row[3] for row in reader]
        content = ''.join(column)

    words_list = jieba.cut(content, cut_all=False)
    return ' '.join(words_list)


def create_worlds_cloud():
    background = np.array(Image.open(PICTURE))
    stopwords = set(STOPWORDS)

    # 读取文件
    with open('ciyun.txt', encoding='utf-8') as f:
        string_data = f.read()  # 读出整个文件

    # 文本预处理
    pattern = re.compile(u'\t|\n|\.|-|:|;|\)|\(|\?|"')  # 定义正则表达式匹配模式
    string_data = re.sub(pattern, '', string_data)  # 将符合模式的字符去除

    # 文本分词
    seg_list_exact = jieba.cut(string_data, cut_all=True)  # 精确模式分词

    object_list = []
    with open('哈工大停用词表.txt', 'r', encoding='utf-8') as f:
        content = f.read().splitlines()
        remove_words = content
    remove_words = remove_words + [u'的', u'，', u'和', u'是', u'随着', u'对于', u'对', u'等', u'能', u'都', u'。', u' ', u'、', u'中', u'在', u'了',
                    u'通常', u'如果', u'我们', u'死', u'不平', u'很', u'北', u'看完', u'人', u'我', u'看', u'不',
                    u'有', u'被', u'也', u'！', u'小', u'美美', u'就', u'微', u'店', u'', u'她', u'他', u'烊'
                    , u'千', u'玺', u'一座', u'一个', u'这', u'一个', u'易', u'陈', u'一个', u'念', u'他们'
                    , u'雀', u'戏', u'##', u'念', u'百', u'L', u'念', u'念', '日', '月', '2', '网', '新', '转发', '晚',
                                   'O', '链接', '哈哈哈哈', '丽', '热', '邓', '搜', '全文', '收起', 'd', '元', '拍',
                                   '快', '大宗', '闪', '说', '红旗', '领', '茜', '靳', '加', '包', '东', '聊', '价', '复制', '博',
                                   '太', '祥', '秒', '志', '江山', '+1']  # 自定义去除词库

    for word in seg_list_exact:  # 循环读出每个分词
        if word not in remove_words:  # 如果不在去除词库中
            object_list.append(word)  # 分词追加到列表

    # 词频统计
    word_counts = collections.Counter(object_list)  # 对分词做词频统计
    word_counts_top10 = word_counts.most_common(10000)  # 获取前10最高频的词
    print(word_counts_top10)  # 输出检查

    wc = WordCloud(background_color="white",
                   mask=background,
                   stopwords=stopwords,
                   font_path=FONT,
                   max_words=200,  # 最多显示词数
                   # max_font_size=100  # 字体最大值
                   )
    wc.generate_from_frequencies(word_counts)
    wc.to_file('girl.png')
    return word_counts_top10


def save_data(file_name, data_list):
    """
    保存数据
    :param file_name: 文件名，不需要加后缀
    :param data_list: 写入的值,格式：[[],[],[],[],[]]
    :return:
    """
    f_name = file_name + ".csv"
    f = open(f_name, "w", newline="", encoding="utf-8")
    c = csv.writer(f)
    for i in data_list:
        c.writerow(i)


if __name__ == '__main__':
    data = create_worlds_cloud()
    save_data(file_name='词频统计', data_list=data)

