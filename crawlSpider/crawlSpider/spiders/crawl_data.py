import scrapy


class Crawl_data(scrapy.Spider):
    name = "crawl_data"

    def start_requests(self):
        urls = [
           "https://www.google.co.in/search?q=Prime+Air+in+US-WA-Seattle&ibp=htl;jobs"
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        yield {'body':response.body}

