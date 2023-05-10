import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from yahoo.items import YahooJapanNewsDetailItem


class NewsCrawlDetailSpider(CrawlSpider):
    name = 'news_crawl_detail'
    allowed_domains = ['yahoo.co.jp']
    start_urls = ['http://news.yahoo.co.jp/']

    rules = (
        # Yahoo!ニュースのトップページにあるトピック（8個）のリンクを開く。ページ遷移のみで追加処理はしない。
        # callback を指定しない場合、follow 省略時は True（再帰的にクローリングする）となる
        Rule(LinkExtractor(restrict_xpaths='//div[@class="sc-liPmeQ dqfgPl"]//a[@data-ual-gotocontent="true"]'), ),
        # トピックの詳細ページの「…記事全文を読む」のリンクを開く。記事全文ページに対して parse_item の処理をする。
        # callback を指定する場合、follow 省略時は False（再帰的にクローリングしない）となる
        Rule(LinkExtractor(restrict_xpaths='//p[@class="sc-efEzrW khDHLt"]/a'), callback='parse_item')
    )

    def parse_item(self, response):
        item = YahooJapanNewsDetailItem()
        item['url'] = response.url
        item['title'] = response.xpath('//article//h1/text()').get()
        item['date'] = response.xpath('//p[@class="sc-exkUMo bOWzsQ"]/time/text()').getall()
        return item