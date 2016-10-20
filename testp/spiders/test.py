import scrapy
from ..items import TestItem

class TestSpider1a(scrapy.Spider):
    name = "test1ax"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
    ]

    def __init__(self, *args, **kwargs):
        print args
        print kwargs
        super(TestSpider1a, self).__init__(*args, **kwargs)

    def parse(self, response):
        item = TestItem()
        item['name'] = '1a-k3'
        item['url'] = response.url
        return item

class TestSpider1b(scrapy.Spider):
    name = "test1bx"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
    ]

    def parse(self, response):
        item['name'] = '1b-k3'
        item['url'] = response.url
        return item

class TestSpider1c(scrapy.Spider):
    name = "test1c"
    allowed_domains = ['productlibrary.brandbank.com']

    start_urls = [
        'https://productlibrary.brandbank.com/products/detail/949211',

    ]

    def parse(self, request):
        return []

class TestSpider1d(scrapy.Spider):
    name = "test1d"
    allowed_domains = ['productlibrary.brandbank.com']

    start_urls = [
        'https://productlibrary.brandbank.com/products/detail/949211',

    ]

    def parse(self, request):
        return []

class TestSpider1e(scrapy.Spider):
    name = "test1e"
    allowed_domains = ['productlibrary.brandbank.com']

    start_urls = [
        'https://productlibrary.brandbank.com/products/detail/949211',

    ]

    def parse(self, request):
        return []

class TestSpider1e(scrapy.Spider):
    name = "test1e"
    allowed_domains = ['productlibrary.brandbank.com']

    start_urls = [
        'https://productlibrary.brandbank.com/products/detail/949211',

    ]

    def parse(self, request):
        return []

class TestSpider1f(scrapy.Spider):
    name = "test1f"
    allowed_domains = ['productlibrary.brandbank.com']

    start_urls = [
        'https://productlibrary.brandbank.com/products/detail/949211',

    ]

    def parse(self, request):
        return []

class TestSpider1z(scrapy.Spider):
    name = "test1z"
    allowed_domains = ['productlibrary.brandbank.com']

    start_urls = [
        'https://productlibrary.brandbank.com/products/detail/949211',

    ]

    def parse(self, request):
        return []


class TestSpider1slow(scrapy.Spider):
    name = "test1slow"
    allowed_domains = ['productlibrary.brandbank.com']
    custom_settings = {
        "DOWNLOAD_DELAY": 5,
        "CONCURRENT_REQUESTS_PER_DOMAIN": 2
    }

    start_urls = [
        'https://productlibrary.brandbank.com/products/detail/949211',
    ] * 1000

    def parse(self, request):
        return []
