import requests
from lxml import html
import time
import random
import re
import csv

etree = html.etree

# 全局的cookie，如果cookie过期了就修改下
cookie = 'bid="P6c5c7SdD3w"; ll="118172"; gr_user_id=fcd78f58-405d-4b35-a899-3b329e1bf917; _vwo_uuid_v2=D56EE26105876EE3AC3D4478816AA711B|4954256576cb3089bb2eed5430b1344a; push_doumail_num=0; push_noty_num=0; __utmv=30149280.20803; ct=y; douban-profile-remind=1; douban-fav-remind=1; __utmz=30149280.1577327526.28.13.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmc=30149280; ap_v=0,6.0; __utma=30149280.1397345246.1575978668.1577341657.1577343904.30; dbcl2="208034392:xXtlReIDvNg"; ck=rGai; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1577344563%2C%22https%3A%2F%2Faccounts.douban.com%2Fpassport%2Flogin%22%5D; _pk_ses.100001.8cb4=*; __utmt=1; _pk_id.100001.8cb4=2b01f89a590b449c.1576025283.13.1577344573.1576834951.; __utmb=30149280.4.10.1577343904'

# 通用的header，有些网址需求的Host可能不一样，所以有些网站要重新写header
common_header = {'Host': 'movie.douban.com',
                 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
                 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                 'Cookie': cookie}


def comment_spider(url):
    data_list = []

    comment_html = requests.get(url=url, headers=common_header).content.decode()
    time.sleep(random.randint(0, 3))
    html_c = etree.HTML(comment_html)
    comment_item = html_c.xpath("//div[@id='comments']/div[@class='comment-item']/div[@class='comment']")

    for item in comment_item:
        # 这个comment-time后面有个空字符，坑了我好久，T T
        datetime = item.xpath("./h3/span[@class='comment-info']/*[@class='comment-time ']/@title")[0]
        user_name = item.xpath("./h3/span[@class='comment-info']/a/text()")[0]
        user_url = item.xpath("./h3/span[@class='comment-info']/a/@href")[0]
        user_id = re.findall(".*people/(.*)/", user_url)[0] if re.findall(".*people/(.*)/", user_url) else ''
        comment = item.xpath("./p/span/text()")[0] if item.xpath("./p/span/text()") else ''
        start = item.xpath("./h3/span[@class='comment-info']/span[2]/@title")[0]

        if '20' in start:
            start = '未评分'
        vote = item.xpath("./h3/span/span[@class='votes']/text()")[0]

        movice_id = re.findall(".*subject/(.*)/", url)[0]
        movice_name = html_c.xpath("//div[@id='content']/h1/text()")[0].replace(' 短评', '')

        data = [user_id, user_name, datetime, comment, start, vote, movice_id, movice_name]
        data_list.append(data)  # 用来后续存数据用
    print(f'该页短论个数{len(data_list)},短评列表：{data_list}')
    return data_list


def save_data(file_name, data_list):
    """
    保存数据
    :param file_name: 文件名，不需要加后缀
    :param data_list: 写入的值,格式：[[],[],[],[],[]]
    :return:
    """
    f_name = file_name + ".csv"
    with open(f_name, "a", newline="", encoding="utf-8") as f:
        c = csv.writer(f)
        for i in data_list:
            c.writerow(i)



def main():
    # 每一页20条短评，总共25页
    url = 'https://movie.douban.com/subject/30166972/comments?start={}&limit=20&sort=new_score&status=P'
    for page in range(0, 25):
        new_page = url.format(page * 20)
        print(f'正在爬电影：{new_page}的第{page + 1}页的评论')
        data = comment_spider(new_page)
        time.sleep(random.randint(3, 6))
        save_data('data', data)


if __name__ == '__main__':
    main()
