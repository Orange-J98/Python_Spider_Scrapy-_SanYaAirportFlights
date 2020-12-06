import scrapy

class EnterPortItem(scrapy.Item):
    #航班号
    flight_num = scrapy.Field()
    #始发地
    origin = scrapy.Field()
    #接机楼
    terminal = scrapy.Field()
    #预计时间
    time_pre = scrapy.Field()
    #实际时间
    time_real = scrapy.Field()
    #状态
    status = scrapy.Field()


class LeavePortItem(scrapy.Item):
    #航班号
    flight_num = scrapy.Field()
    #始发地
    destination = scrapy.Field()
    #接机楼
    terminal = scrapy.Field()
    #预计时间
    time_pre = scrapy.Field()
    #实际时间
    time_real = scrapy.Field()
    #状态
    status = scrapy.Field()