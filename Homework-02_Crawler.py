# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 12:21:14 2020

@author: alienware

Homework-2: 利用爬虫抓取数据
"""
print('----Homework_2---')
from bs4 import BeautifulSoup
import requests
import pandas as pd

def analyse(soup):
# 找到完整的投诉信息框
    temp = soup.find('div', class_="tslb_b")
    # 制作DataFrame
    List = pd.DataFrame(columns = ['投诉编号', '投诉品牌', '投诉车系', '投诉车型', '问题简述', '典型问题', '投诉时间', '投诉状态'])
    tr_list = temp.find_all('tr')
    for tr in tr_list:
        temp = {}
        td_list = tr.find_all('td')
        if len(td_list) > 0:
            投诉编号, 投诉品牌, 投诉车系, 投诉车型, 问题简述, 典型问题, 投诉时间, 投诉状态 = \
                td_list[0].text, td_list[1].text, td_list[2].text, td_list[3].text, td_list[4].text, td_list[5].text, td_list[6].text, td_list[7].text,
            temp['投诉编号'], temp['投诉品牌'], temp['投诉车系'], temp['投诉车型'], temp['问题简述'], temp['典型问题'], temp['投诉时间'], temp['投诉状态'] = \
                投诉编号, 投诉品牌, 投诉车系, 投诉车型, 问题简述, 典型问题, 投诉时间, 投诉状态,
            List = List.append(temp, ignore_index=True)
    return List

page_num = 10
base_url = 'http://www.12365auto.com/zlts/0-0-0-0-0-0_0-0-0-0-0-0-0-'
Car = pd.DataFrame(columns = ['投诉编号', '投诉品牌', '投诉车系', '投诉车型', '问题简述', '典型问题', '投诉时间', '投诉状态'])
for i in range(page_num):
    request_url = base_url + str(i+1) + '.shtml'
    # 得到页面的内容 #
    headers={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}
    html=requests.get(request_url,headers=headers,timeout=10)
    content = html.text
    soup = BeautifulSoup(content, 'html.parser')
    print(soup.title)
    print(soup.title.string)
    List = analyse(soup)
    print(List)
    Car = Car.append(List)

Car.to_csv('Car_Complain_List.csv', index = False)