# Scrapy settings for pydaybot project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'pydaybot'

SPIDER_MODULES = ['pydaybot.spiders']
NEWSPIDER_MODULE = 'pydaybot.spiders'

HTTPCACHE_ENABLED = 1

IMAGES_STORE = 'images'
ITEM_PIPELINES = [
    'scrapy.contrib.pipeline.images.ImagesPipeline',
]

#IMAGES_MIN_HEIGHT = 200
