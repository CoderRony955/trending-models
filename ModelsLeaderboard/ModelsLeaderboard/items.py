# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ModelsleaderboardItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class TrendingModels(scrapy.Item):
    Name = scrapy.Field()
    URL = scrapy.Field()
    Downloads = scrapy.Field()
    Type = scrapy.Field()
    Likes = scrapy.Field()
    Language = scrapy.Field()
    Links = scrapy.Field()
    
    
