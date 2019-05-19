import scrapy

class ItcastSpider(scrapy.Spider):
    name = "itcast"
    allowed_domains = ["http://www.baidu.com"]
    strt_urls = ['http://www.itcast.cn/']

    def parse(self, response):
        print (response.body)
        pass


if __name__ == "__main__":
    itemct = ItcastSpider()