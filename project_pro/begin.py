#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/22 19:50
# @Author  : NCP
# @File    : begin.py
# @Software: PyCharm
import os, sys
sys_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(sys_dir)

from scrapy import cmdline

cmdline.execute("scrapy crawl spider_first".split())
# cmdline.execute("scrapy crawl spider_first -L WARNING".split())