import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook
import pandas as pd
import numpy as np
from crawl_author import CrawlAuthor

base_url = 'https://www.hongxiu.com/category/f1_f1_f1_f1_f1_f1_0_'
page_count = 50  # 爬取的总页数

# 创建Excel
workbook = Workbook()
sheet = workbook.active


crawler=CrawlAuthor()

ids=[]

# 设置表头
sheet['A1'] = '名称'
sheet['B1'] = '作者'
sheet['C1'] = '类型'
sheet['D1'] = '是否完结'
sheet['E1'] = '人气'
sheet['F1'] = '简介'
sheet['G1']='bookid'

row = 2  # 从第二行开始写入数据

# 循环遍历每一页
for page in range(1, page_count + 1):
    url = base_url + str(page)

    # 发送HTTP请求获取页面内容
    response = requests.get(url)
    content = response.text

    # 使用BeautifulSoup解析HTML内容
    soup = BeautifulSoup(content, 'html.parser')

    # 找到小说列表所在的HTML元素
    novel_list = soup.find_all('div', class_='book-info')

    # 遍历小说列表，提取所需信息
    for novel in novel_list:
        
        bookid=novel.find('a')["href"].split("/")[-1]
        ids.append(bookid)
        # 提取小说名称
        name = novel.find('h3').a.text.strip()

        # 提取作者
        author = novel.find('h4').a.text.strip()

        # 提取类型
        category = novel.find('span', class_='org').text.strip()

        # 提取是否完结
        is_complete = novel.find('span', class_='pink').text.strip()

        # 提取人气
        popularity = novel.find('span', class_='blue').text.strip()

        # 提取简介
        intro = novel.find('p', class_='intro').text.strip()
        
        

        # 将提取的数据写入Excel
        sheet['A' + str(row)] = name
        sheet['B' + str(row)] = author
        sheet['C' + str(row)] = category
        sheet['D' + str(row)] = is_complete
        sheet['E' + str(row)] = popularity
        sheet['F' + str(row)] = intro
        sheet['G'+str(row)]=bookid

        row += 1

# 保存Excel文件
file_path = './data2.xlsx'
workbook.save(file_path)
crawler.crawl(ids=ids)



# print('数据已成功保存到Excel文件：', file_path)