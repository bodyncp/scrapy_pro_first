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
