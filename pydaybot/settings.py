# Scrapy settings for pydaybot project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'pydaybot'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['pydaybot.spiders']
NEWSPIDER_MODULE = 'pydaybot.spiders'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)


IMAGES_STORE = '/tmp/pydaybot'
ITEM_PIPELINES = [
    'scrapy.contrib.pipeline.images.ImagesPipeline',
]
