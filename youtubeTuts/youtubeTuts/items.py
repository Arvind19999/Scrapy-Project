# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
# import sqlite3
# 
class YoutubetutsItem(scrapy.Item):
    title = scrapy.Field()
    author =  scrapy.Field()
    tags =  scrapy.Field()
