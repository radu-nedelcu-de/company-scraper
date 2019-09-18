from dragnet import extract_content
from scrapy.exceptions import DropItem


class TextExtractor:
    def process_item(self, item, _):
        text = extract_content(item['html'])

        if text:
            item['text'] = text
        else:
            raise DropItem

        return item