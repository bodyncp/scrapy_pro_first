#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/29 19:56
# @Author  : NCP
# @File    : conf.py
# @Software: PyCharm


# with open(os.path.join(os.path.dirname(__file__),'city_town.json'), 'r', encoding='utf-8')as fr:
#     url_data_count = json.loads(fr.read())

cj_url = [
    "http://www.ccgp-sichuan.gov.cn/CmsNewsController.do?method=search&chnlCodes=8a817ecb39add7c40139ae0b9sj3166&chnlNames=\u6210\u4EA4\u516C\u544A&years=2018&title=&startTime=&endTime=&distin_like=510000&province=510000&city=&town=&provinceText=\u56DB\u5DDD\u7701&cityText=\u8BF7\u9009\u62E9&townText=\u8BF7\u9009\u62E9&pageSize=10&searchResultForm=search_result_anhui.ftl",
    "http://www.ccgp-sichuan.gov.cn/CmsNewsController.do?method=search&chnlCodes=8a817eb738e5e70c0138e66e141c0ea1&chnlNames=\u4E2D\u6807\u516C\u544A&years=2018&title=&startTime=&endTime=&distin_like=510000&province=510000&city=&town=&provinceText=\u56DB\u5DDD\u7701&cityText=\u8BF7\u9009\u62E9&townText=\u8BF7\u9009\u62E9&pageSize=10&searchResultForm=search_result_anhui.ftl"
]

desc_url = "http://www.ccgp-sichuan.gov.cn"

key = '<td.*>(.*?中国电信.*?)</td>'
key2 = '<td.*>(.*?中国联通.*?)</td>'
key3 = '<td.*>(.*?中国移动.*?)</td>'
key4 = '<td.*>(.*?广播电视网络.*?)</td>'
time_key = '<span> 系统发布时间：(.*)</span>'
time_key_new = '<p class="time">系统发布时间：(.*)</p>'
grep_title = '<h1>(.*公告.*?)</h1>'




