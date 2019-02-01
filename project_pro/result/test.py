#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/31 8:34
# @Author  : NCP
# @File    : test.py
# @Software: PyCharm

import re
import json
import lxml
import requests
from lxml import etree

# with open('result.json', 'r', encoding='utf-8')as fr:
#     data = json.loads(fr.read())
#
#
# for i in data:
#     if re.match('.*成都.*', i[0]):
#         print(i)
# header = {
#         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'
#         }
#
# data = requests.get("http://www.ccgp-sichuan.gov.cn/view/staticpags/shiji_jggg/4028868768694fc001689cd265a93807.html", headers=header)
# data.encoding = 'utf-8'
# data_str = data.text
#
# origin = etree.HTML(data_str)
# content = origin.xpath("//table[@class='table']/tbody/tr/td[2]/text()")
# for i in content:
#     if re.search('.*中标金额.*', i):
#         print(i)
# print(content)



