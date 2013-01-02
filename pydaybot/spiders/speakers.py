from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from pydaybot.loaders import SpeakerLoader


class SpeakersSpider(BaseSpider):
    name = "speakers"
    allowed_domains = ["eventioz.com"]
    start_urls = (
        'https://eventioz.com/events/python-day-uruguay-2011/speakers',
    )

    def parse(self, response):
        hxs = HtmlXPathSelector(response=response)
        for sel in hxs.select('//div[@id="speakers_list"]//div[@class="row-fluid"]'):
            il = SpeakerLoader(selector=sel)
            il.add_xpath('name', './/div/h2/text()')
            il.add_xpath('image_urls', './/ul[@class="thumbnails"]//img/@src')
            il.add_xpath('description', './/div/p//text()')
            yield il.load_item()
