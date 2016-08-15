# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html
import scrapy
from scrapy.item import Item, Field

class TutorialItem(Item):
    # define the fields for your item here like:
    # name = Field()
	title = scrapy.Field()
	issue_date = scrapy.Field()
	content = scrapy.Field()
	download_url = scrapy.Field()