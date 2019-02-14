# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from project_pro.spiders.utils import all_zb_data_dict
from project_pro.spiders.utils import base_dir
import pymysql
import os
import json


class ProjectProPipeline(object):
    def process_item(self, item, spider):
        return item

    def close_spider(self, spider, item):
        print(all_zb_data_dict)
        print('items', item)
        with open(os.path.join(base_dir, 'result', 'result.json'), 'w', encoding='utf-8') as fw:
            fw.write(json.dumps(all_zb_data_dict))


class MysqlWritePipeline(object):

    conn = None
    cursor = None

    def open_spider(self,spider):
        print('开始爬虫')
        #链接数据库
        self.conn = pymysql.Connect(host='127.0.0.1',port=3306,user='zgdx_cra',password='zgdx_cra',db='scrapy_data')
    #编写向数据库中存储数据的相关代码
    def process_item(self, item, spider):
        #1.链接数据库
        #2.执行sql语句
        sql = 'insert into qiubai values("%s","%s","%s")'% (item['title'],item['content'], item['time'])
        self.cursor = self.conn.cursor()
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()
        #3.提交事务
        return item

    def close_spider(self,spider):
        print('爬虫结束')
        self.cursor.close()
        self.conn.close()