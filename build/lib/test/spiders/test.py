import scrapy
from ..items import TestItem

class TestSpider(scrapy.Spider):
    name = "test"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
    ]

    def parse(self, response):
        item = TestItem()
        item['name'] = 'a'
        return item
