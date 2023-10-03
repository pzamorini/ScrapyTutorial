# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

# we can store data on items containers and after transform in json/xml/csv files
# or, we can also store in items containers, send to one pipeline and finally store in a SQL/MONGO database


class QuotetutorialPipeline:
    def process_item(self, item, spider):
        return item
