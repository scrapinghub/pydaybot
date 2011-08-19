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
        for sel in hxs.select('//div[@class="speaker_container"]'):
            il = SpeakerLoader(selector=sel)
            il.add_xpath('name', './/div[@class="speaker_name"]/text()')
            il.add_xpath('image', './/div[@class="speaker_image"]/img/@src')
            il.add_xpath('description', './/div[@class="speaker_description"]/*')
            yield il.load_item()
