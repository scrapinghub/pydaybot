# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field


class SpeakerItem(Item):
    name = Field()
    description = Field()
    image = Field()
    image_urls = Field()
