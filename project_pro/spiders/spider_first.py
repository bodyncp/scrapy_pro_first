# -*- coding: utf-8 -*-

import re
import scrapy
from project_pro.extra.conf import cj_url, desc_url, key, key2, key3, key4, time_key, time_key_new, grep_title
from project_pro.spiders.utils import public_func
from project_pro.items import ProjectProItem


class SpiderFirstSpider(scrapy.Spider):
    name = 'spider_first'
    new_url = []
    # allowed_domains = ['http://www.ccgp-sichuan.gov.cn']
    start_urls = cj_url

    def parse(self, response):
        current_request_url = response.url
        # 获取首页的页码数
        header_page_num = response.xpath("//div[@class='page-cell']").extract_first()
        header_page_num = ''.join(re.findall('页次:(.*) </div>', header_page_num))
        header_page_num = header_page_num[2::]
        pageup = ""
        for num in header_page_num:
            if num != ",":
                pageup += num
        print(pageup)
        for page in range(int(pageup)):
            # 每一个地市的所有页的URL
            page += 1
            # 拼接每页中标公告的URL
            current_request_url_new = "%s&%s=%s" % (current_request_url, 'curPage', page)
            yield scrapy.Request(current_request_url_new, callback=self.parse_many_page)

    def parse_many_page(self, response):
        # 选择出每页URL中的下级文章链接列表
        print(response.url)
        header_data_list = response.xpath("//div[@class='warpper']/div[@class='list-info']/div[@class='info']/ul/li/a/@href").extract()
        for header_data in header_data_list:
            article_url = desc_url + header_data
            yield scrapy.Request(article_url, callback=self.parse_page)

    def parse_page(self, response):
        print('2',response.url)
        item = ProjectProItem()
        article_data = response.text

        if re.search(key, article_data):
            public_func(re, key, time_key, article_data, grep_title, time_key_new, item)

        elif re.search(key2, article_data):
            public_func(re, key2, time_key, article_data, grep_title, time_key_new, item)

        elif re.search(key3, article_data):
            public_func(re, key3, time_key, article_data, grep_title, time_key_new, item)

        elif re.search(key4, article_data):
            public_func(re, key4, time_key, article_data, grep_title, time_key_new, item)

        yield item

