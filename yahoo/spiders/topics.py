# note.nkmk.me - Python, Scrapyの使い方（Webクローリング、スクレイピング）
# https://note.nkmk.me/python-scrapy-tutorial/
# 単独のページをスクレイピングする例

# https://ai-inter1.com/python-scrapy-for-begginer/

import scrapy
from yahoo.items import Headline, YahooJapanItem, AllTopics

class TopicsSpider(scrapy.Spider):
    name = 'topics'
    allowed_domains = ['yahoo.co.jp']
    start_urls = ['https://yahoo.co.jp/']

    # トップページのニューストピックスの詳細ページのヘッドライン・本文・URL を取得する処理
    def parse_detail(self, response):
        item_detail = YahooJapanItem()
        item_detail['headline'] = response.xpath('//p[@class="sc-ehMMwX eJusCb"]/text()').get()
        item_detail['body'] = response.xpath('//p[@class="sc-ftesFE gXITtf highLightSearchTarget"]/text()').get()
        item_detail['url'] = response.url
        yield item_detail

    # ニューストピックス一覧のカテゴリ名・ヘッドライン・URL を取得する処理
    def parse_topics_all(self, response):
        topics = response.xpath('//li[@data-ual-view-type="list"]')

        for topic in topics:
            item_all = AllTopics()
            item_all['category'] = topic.xpath('./parent::ul/parent::div//a/text()').get()
            item_all['headline'] = topic.xpath('./a/text()').get()
            item_all['url'] = topic.xpath('./a/@href').get()
            yield item_all

    def parse(self, response):
        # topics = response.xpath('//article[@class="QLtbNZwO-lssuRUcWewbd"]')
        # print(f'■ topics:{topics}')  # 確認用

        # トップページ上のニュースのヘッドラインとその URL を取得する処理
        # for topic in topics:
        #     # print(f'■ topic:{topic}')  # 確認用
        #     item = YahooJapanItem()
        #     item['headline'] = topic.xpath('.//h1/span/text()').get()
        #     item['url'] = topic.xpath('./a/@href').get()
        #     yield item

        # トップページ上のニュースの詳細ページに遷移して、ヘッドライン・URL・本文を取得する処理を呼び出す
        # detail_urls = response.xpath('//article[@class="QLtbNZwO-lssuRUcWewbd"]/a/@href').getall()
        # print(f'■ detail_urls:{detail_urls}')  # 確認用
        # 
        # for detail_url in detail_urls:
        #     print(f'■ detail_url:{detail_url}')  # 確認用
        #     yield response.follow(url = detail_url, callback = self.parse_detail)

        # ニューストピックス一覧ページに遷移して、カテゴリ名・ヘッドライン・URL を取得する処理を呼び出す
        yield response.follow(url = 'https://news.yahoo.co.jp/topics', callback = self.parse_topics_all)
        