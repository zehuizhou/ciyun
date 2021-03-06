from snownlp import SnowNLP
import pandas as pd


def update_csv_row(csv_name):
    data = pd.read_csv(csv_name, encoding='utf_8_sig', )
    data[u'评论内容'] = data[u'评论内容'].astype(str)
    data[u'情感得分'] = data[u'评论内容'].apply(lambda x: SnowNLP(x).sentiments)
    data.to_csv(csv_name, index=False, encoding='utf_8_sig')


if __name__ == '__main__':
    update_csv_row('评论.csv')
