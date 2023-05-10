# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Headline(scrapy.Item):
    title = scrapy.Field()
    body = scrapy.Field()

class YahooJapanItem(scrapy.Item):
    headline = scrapy.Field()
    url = scrapy.Field()
    body = scrapy.Field()
    category = scrapy.Field()

class AllTopics(scrapy.Item):
    headline = scrapy.Field()
    url = scrapy.Field()
    category = scrapy.Field()

class YahooJapanNewsDetailItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    date = scrapy.Field()

# フィールドを定義していない（例：category）と下記のエラーになる
# KeyError: 'YahooJapanItem does not support field: category'
