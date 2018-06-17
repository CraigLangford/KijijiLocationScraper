import scrapy


class QuotesSpider(scrapy.Spider):
    name = "addresses"

    start_urls = ['https://www.kijiji.ca/b-apartments-condos/city-of-toronto/c37l1700273r5.0?ad=offering&price=1200__2150']

    def parse(self, response):
        # follow links to author pages
        for href in response.css('.enable-search-navigation-flag'):
            yield response.follow(href, self.parse_apartment)

        # follow pagination links
        for href in response.xpath('//a[contains(text(), "Next")]'):
            yield response.follow(href, self.parse)

    def parse_apartment(self, response):
        def extract_with_css(query):
            return response.css(query).extract_first().strip()

        def extract_address():
            return response.xpath("//span[contains(@class, 'address-')]/text()").extract_first()

        yield {
            'title': extract_with_css('title::text'),
            'address': extract_address(),
            'url': response.url,
        }
