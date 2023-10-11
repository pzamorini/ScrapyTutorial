# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

# we can store data on items containers and after transform in json/xml/csv files
# or, we can also store in items containers, send to one pipeline and finally store in a SQL/MONGO database

import sqlite3


class QuotetutorialPipeline(object):
    def __init__(self):
        self.create_connection()
        self.create_table()


# method to create a connection

    def create_connection(self):
        self.coon = sqlite3.connect("myquotes.db")
        self.curr = self.coon.cursor()

# here I am creating a table
    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS quotes_tb""")
        # in the line above, I am saying is "if the table already exists, drop."
        self.curr.execute("""CREATE TABLE quotes_tb
                        (title TEXT,
                        author TEXT,
                        tag TEXT)""")

# In the next two steps, I am creating functions to process and storage the items
    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        # in the tutorial that I watched, the guy adds the 0 to be a str, not a list
        # if it is a list, the code returns a error
        self.curr.execute("""INSERT INTO quotes_tb VALUES (?, ?, ?) """, (
            item['title'][0],
            item['author'][0],
            item['tag'][0]
        ))
        self.coon.commit()
