# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

# import sqlite3
import mysql.connector



 
class YoutubetutsPipeline:
    def __init__(self):
        self.creatConnection()
        self.createTable()
    
    def creatConnection(self):
        self.conn = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "SHa.arvind*99#",
            database = "myquotes"
        )
        self.curr = self.conn.cursor()
        
    def createTable(self):
        self.curr.execute(''' drop table if exists quote''')
        self.curr.execute('''create table quote(title text, author text, tags text)''')
        
    def process_item(self, item, spider):
        self.storeDb(item)
        return item
    
    
    def storeDb(self,item):
        self.curr.execute('''insert into quote values(%s,%s,%s)''',(
            item["title"][0],
            item["author"][0],
            item["tags"][0],
        ))
        
        self.conn.commit()
