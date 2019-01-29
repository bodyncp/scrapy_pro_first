# -*- coding: utf-8 -*-

import re
import scrapy
import requests
import settings
from extra.conf import url_data_count, desc_url
from items import ProjectProItem


class SpiderFirstSpider(scrapy.Spider):
    name = 'spider_first'
    # allowed_domains = ['http://www.ccgp-sichuan.gov.cn']
    header_url_list = url_data_count['urls']
    start_urls = header_url_list

    def parse(self, response):
        header_data = response.xpath("//div[@class='warpper']/div[@class='list-info']/div[@class='info']/ul/li/a/@href").extract_first()

        if header_data:
            # 获取首页的页码数
            header_page_num = response.xpath("//div[@class='page-cell']").extract_first()
            header_page_num = ''.join(re.findall('页次:(.*) </div>', header_page_num))
            pageup = int(header_page_num.split('/')[-1])
            for page in range(pageup):
                # 每一个地市的所有页的URL
                page += 1

            # 拼接中标公告的URL
            article_url = desc_url+header_data
            yield scrapy.Request(article_url, callback=self.parse_page)

    def parse_many_page(self, response):
        pass

    def parse_page(self, response):
        item = ProjectProItem()
        article_data = response.text
        # print(article_data)

