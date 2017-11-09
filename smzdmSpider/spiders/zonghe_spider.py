"""Created by xetra f han"""

from ..YDHP import YDHP_ScrapySystem, YDHP_ScrapyRequester
import scrapy
import json
from bs4 import BeautifulSoup
from .. import xpaths as X
from .. import items as I

json_response = str()


class ZongHe(scrapy.Spider):
    name = "zong_he_pachong"
    example_url = "http://search.smzdm.com/?c=home&s=%28&p="

    current_page_num = 0
    reach_the_end = False

    def start_requests(self):
        yield self.requester.scrapy_requests(self.example_url + str(self.current_page_num), self.callback_parse)

    def callback_parse(self, response):
        if response.xpath(X.ZH_card).extract() is None:
            self.reach_the_end = True

        try:
            for card in response.xpath(X.ZH_card).extract():
                """把每个卡片解析出来"""
                item = I.ZongHeItems()
                item['tag'] = card.xpath(X.ZH_tag).extract_first()
                item['image'] = card.xpath(X.ZH_image).extract_first()
                item['title'] = card.xpath(X.ZH_title).extract_first()
                item['discounts'] = card.xpath(X.ZH_discounts).extract_first()
                item['description'] = card.xpath(X.ZH_description).extract_first()
                item['goods'] = int(card.xpath(X.ZH_goods).extract_first())
                item['bads'] = int(card.xpath(X.ZH_bads).extract_first())
                item['stars'] = int(card.xpath(X.ZH_stars).extract_first())
                item['comments'] = int(card.xpath(X.ZH_comments).extract_first())
                item['time'] = card.xpath(X.ZH_time).extract_first()
                item['provider'] = card.xpath(X.ZH_provider).extract_first()
                item['purchase_link'] = card.xpath(X.ZH_purchase_link).extract_first()
                yield item
        except:
            YDHP_ScrapySystem.ScrapySystem.what_the_fxxk("Xpath of `card` went down")

        if not self.reach_the_end:
            self.current_page_num += 1
            yield self.requester.scrapy_requests(self.example_url + str(self.current_page_num), self.callback_parse)

        if self.reach_the_end:
            print("爬虫综合模块跑完了，总共爬了%s个页面" % (self.current_page_num))

    def __init__(self):
        super(ZongHe, self).__init__()
        self.requester = YDHP_ScrapyRequester.ScrapyRequester()
