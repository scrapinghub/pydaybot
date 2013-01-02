from scrapy.contrib.loader import XPathItemLoader
from scrapy.contrib.loader.processor import MapCompose, Join, Identity
from w3lib.html import remove_tags, unquote_markup
from .items import SpeakerItem


class SpeakerLoader(XPathItemLoader):
    default_item_class = SpeakerItem
    default_input_processor = MapCompose(remove_tags, unquote_markup, unicode.strip)
    default_output_processor = Join()

    image_urls_out = Identity()
