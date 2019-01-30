# -*- coding: utf-8 -*-

import re
import scrapy
import json
import settings
from extra.conf import url_data_count, desc_url, header_parse, key, key2, key3, key4, time_key, time_key_new, grep_title
from spiders.utils import public_func
from items import ProjectProItem


class SpiderFirstSpider(scrapy.Spider):
    name = 'spider_first'
    new_url = []
    # allowed_domains = ['http://www.ccgp-sichuan.gov.cn']
    header_url_list = url_data_count['urls']
    start_urls = header_url_list
    header = settings.USER_AGENT

    def parse(self, response):
        current_request_url = response.url
        # 每页文章中的下级文章内容链接
        header_data = header_parse(response)
        # 验证页面是否为空
        if header_data:
            # 获取首页的页码数
            header_page_num = response.xpath("//div[@class='page-cell']").extract_first()
            header_page_num = ''.join(re.findall('页次:(.*) </div>', header_page_num))
            pageup = int(header_page_num.split('/')[-1])
            for page in range(pageup):
                # 每一个地市的所有页的URL
                page += 1
                # for page_url in self.start_urls:
                #     page_header_url = "%s&%s=%s" % (page_url, 'curPage', page)
                # 拼接每页中标公告的URL
                current_request_url_new = "%s&%s=%s" % (current_request_url, 'curPage', page)
                yield scrapy.Request(current_request_url_new, callback=self.parse_many_page, headers={"User-Agent": self.header})

    def parse_many_page(self, response):
        print(response.url)
        header_data = header_parse(response)
        article_url = desc_url + header_data
        yield scrapy.Request(article_url, callback=self.parse_page, headers={"User-Agent": self.header})

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
        return item