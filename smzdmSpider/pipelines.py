# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from .items import ZongHeItems
import pymongo
from pymongo import IndexModel, ASCENDING
import pymysql as mysql
from .settings import MYSQL_DB, MYSQL_HOST, MYSQL_PASSWORD, MYSQL_USERNAME


class SmzdmspiderPipeline(object):
    def __init__(self):
        super(SmzdmspiderPipeline, self).__init__()
        my_db = mysql.connect(host=MYSQL_HOST, user=MYSQL_USERNAME, passwd=MYSQL_PASSWORD, db=MYSQL_DB)
        self.cursor = my_db.cursor()

    def process_item(self, item, spider):
        """ZongHe Spider"""
        if isinstance(item, ZongHeItems):
            insert_sql = """INSERT INTO `zong_he` (title, tag, image, discounts, description, goods, """ \
                """bads, stars, comments, time, provider, purchase_link)""" \
                """ VALUES (%s,%s,%s,%s,%s,%d,%d,%d,%d,%s,%s,%s);""" \
                         % (item['title'], item['tag'], item['image'], item['discounts'], item['description'],
                            item['goods'], item['bads'], item['stars'], item['comments'], item['time'],
                            item['provider'], item['purchase_link'])

            self.cursor.execute("""LOCK TABLES `zong_he` WRITE;""")
            self.cursor.execute(insert_sql)
            self.cursor.execute("""UNLOCK TABLES;""")

            print("综合模块爬到了1条信息")

    def __del__(self):
        self.cursor.close()
