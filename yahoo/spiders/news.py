import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import logging

from yahoo.items import Headline  # items.py に定義した Headline クラスをインポート

class NewsSpider(CrawlSpider):
    name = 'news'
    allowed_domains = ['news.yahoo.co.jp']
    start_urls = ['https://news.yahoo.co.jp/']

    rules = (
        # Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),  # 元の記述はコメントアウト
        # トピックスの詳細ページを開く
        # a 要素までを指定すれば、自動的に @href 属性の値を取得してくれる。
        # ■ @href を追加するとエラーになるが、@href を付ける場合はどう書けばいいのか？
        # Rule(LinkExtractor(restrict_xpaths='//div[@class="sc-fhiYOA lmAaIt"]//li/a'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        logging.info(response.url)

        # トピックスの詳細ページからタイトルと本文を抽出する
        item = Headline()
        item['title'] = response.xpath('//article//span//p/text()').get()
        item['body'] = response.xpath('//p[@class="sc-ftesFE gXITtf highLightSearchTarget"]/text()').get()

        yield item