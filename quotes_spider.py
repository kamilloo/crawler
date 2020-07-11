import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    def start_requests(self):
        url = 'https://katalog.infoludek.pl/kategoria/gabinety_kosmetyczne/61'
        yield scrapy.Request(url, self.parse)

    def parse(self, response):
        for quote in response.css('div.entry_result'):
           yield {
                'text': quote.css('h4 a::text').get(),
                'author': quote.css('div.entry_data').xpath('text()').getall()[1].strip(),
           }

        next_pages = response.css('div.paginator a::attr(href)').getall()
        for page in next_pages:
            yield response.follow(page, self.parse)


