#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/29 19:56
# @Author  : NCP
# @File    : conf.py
# @Software: PyCharm

import os
import json

with open(os.path.join(os.path.dirname(__file__),'city_town.json'), 'r', encoding='utf-8')as fr:
    url_data_count = json.loads(fr.read())

desc_url = "http://www.ccgp-sichuan.gov.cn"

key = '<td.*>(.*?中国电信.*?)</td>'
key2 = '<td.*>(.*?中国联通.*?)</td>'
key3 = '<td.*>(.*?中国移动.*?)</td>'
key4 = '<td.*>(.*?广播电视网络.*?)</td>'
time_key = '<span> 系统发布时间：(.*)</span>'
time_key_new = '<p class="time">系统发布时间：(.*)</p>'
grep_title = '<h1>(.*公告.*?)</h1>'


def header_parse(response):
    header_data = response.xpath("//div[@class='warpper']/div[@class='list-info']/div[@class='info']/ul/li/a/@href").extract_first()
    return header_data


