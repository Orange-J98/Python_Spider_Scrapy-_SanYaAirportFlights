import scrapy

from Project1.FlightItems import FlightItem
class MySpider(scrapy.Spider):
    #用于区别Spider
    name = "MySpider"
    #允许访问的域
    allowed_domains = ["data.carnoc.com"]
    #爬取的地址
    start_urls = ["http://data.carnoc.com/corp/airport/syx__airportflight.html"]
    #爬取方法
    def parse(self, response):
        # 实例化一个容器保存爬取的信息
        item = FlightItem()
        #入港
        for box in response.xpath('//*[@id="icefable1"]/li'):
            item['flight_num'] = box.xpath('./span[1]/text()').extract()[0]
            item['flight_city'] = box.xpath('./span[2]/text()').extract()[0]
            item['terminal'] = box.xpath('./span[3]/text()').extract()[0]
            item['time_pre'] = box.xpath('./span[4]/text()').extract()[0]
            item['time_real'] = box.xpath('./span[5]/text()').extract()[0]
            item['status'] = box.xpath('./span[6]/text()').extract()[0]
            yield item
        item2 = FlightItem()
        #出港
        for box in response.xpath('//*[@id="icefable2"]/li'):
            item2['flight_num'] = box.xpath('./span[1]/text()').extract()[0]
            item2['flight_city'] = box.xpath('./span[2]/text()').extract()[0]
            item2['terminal'] = box.xpath('./span[3]/text()').extract()[0]
            item2['time_pre'] = box.xpath('./span[4]/text()').extract()[0]
            item2['time_real'] = box.xpath('./span[5]/text()').extract()[0]
            item2['status'] = box.xpath('./span[6]/text()').extract()[0]
            yield item2

