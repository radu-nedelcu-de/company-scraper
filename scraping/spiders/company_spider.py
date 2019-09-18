import time
import uuid

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from scraping.spiders.company_sources import company_sources


class CompanySpider(CrawlSpider):
    name = 'CompanySpider'
    results_file = 'scraping_results'
    allowed_domains = [
        url.split('www.')[1] for url in company_sources
    ]
    start_urls = [
        'http://' + url for url in company_sources
    ]

    rules = (
        Rule(LinkExtractor(), callback='parse_item', follow=True),
    )

    custom_settings = {
        'DOWNLOAD_TIMEOUT': 3,
    }

    def parse_item(self, response):
        yield {
            'html': response.text,
            'url': response.url,
            'mid': str(uuid.uuid4()),
            'scraping_time': time.time()
        }


