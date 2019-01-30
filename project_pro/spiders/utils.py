#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/30 11:20
# @Author  : NCP
# @File    : utils.py
# @Software: PyCharm


import os
import json

base_dir = os.path.dirname(os.path.dirname(__file__))
all_zb_data_dict = []
all_cj_data_dict = []


def public_func(re, key, time_key, article_data, grep_title, time_key_new, item):
    data_title = re.findall(grep_title, article_data)[0]
    data_content = re.findall(key, article_data)[0]
    try:
        date_time = re.findall(time_key, article_data)[0]
    except Exception:
        date_time = re.findall(time_key_new, article_data)[0]

    print(data_title, data_content, date_time)
    item['title'] = data_title
    item['content'] = data_content
    item['time'] = date_time
    all_zb_data_dict.append((data_title, data_content, date_time))
    with open(os.path.join(base_dir, 'result', 'result.json'), 'w', encoding='utf-8') as fw:
        fw.write(json.dumps(all_zb_data_dict))