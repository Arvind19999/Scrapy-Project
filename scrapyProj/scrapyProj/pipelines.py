# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import logging
import pymongo
import sqlite3

# Pipeline to MongoDB
# class MongodbPypeline:
#     collectionName = "transcripts"
    
#     def open_spider(self,spider):
#         self.client = pymongo.MongoClient("mongodb+srv://shaaarun1971:root@cluster0.8fryrgo.mongodb.net/?retryWrites=true&w=majority")
#         self.db = self.client["My_Database"]
#         # logging.warning("Spider open -Pipelines")
        
        
#     def close_spider(self,spider):
#         self.connection.close()
#         # logging.warning("Spider Close -Pipelines")
        
#     def process_item(self, item, spider):
#         self.db[self.collectionName].insert(item)
#         return item
    
    
 
# Pipeline to SQL 
class SQLitePipeline:
    def open_spider(self,spider):
        self.connection = sqlite3.connect("transcript.db")
        self.c = self.connection.cursor()
        #query
        try:
            self.c.execute('''
                       CREATE TABLE transcripts(
                           Title TEXT,
                           Description TEXT,
                           Url TEXT
                       )
                       ''')
            self.connection.commit()
        except sqlite3.OperationalError:
            pass
        # logging.warning("Spider open -Pipelines")
        
        
    def close_spider(self,spider):
        self.connection.close()
        # logging.warning("Spider Close -Pipelines")
        
    def process_item(self, item, spider):
        self.c.execute('''
                       INSERT INTO  transcripts(Title,Description,Url)
                       VALUES(?,?,?)
                       ''',(
                           item.get("Title"),
                           item.get("Description"),
                           item.get("Url")
                       ))
        self.connection.commit()
        return item
        # self.db[self.collectionName].insert(item)
        # return item

