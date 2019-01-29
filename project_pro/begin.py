#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/22 19:50
# @Author  : NCP
# @File    : begin.py
# @Software: PyCharm

from scrapy import cmdline
cmdline.execute("scrapy crawl spider_first --nolog".split())