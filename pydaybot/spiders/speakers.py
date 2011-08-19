from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from pydaybot.items import SpeakerItem


class SpeakersSpider(BaseSpider):
    name = "speakers"
    allowed_domains = ["eventioz.com"]
    start_urls = (
            'https://eventioz.com/events/python-day-uruguay-2011/speakers',
        )

    def parse(self, response):
        hxs = HtmlXPathSelector(response=response)
        for sel in hxs.select('//div[@class="speaker_container"]'):
            item = SpeakerItem()
            item['name'] = sel.select('.//div[@class="speaker_name"]/text()').extract()[0].strip()
            item['image'] = sel.select('.//div[@class="speaker_image"]/img/@src').extract()[0].strip()
            item['description'] = sel.select('.//div[@class="speaker_description"]').extract()[0].strip()
            yield item
