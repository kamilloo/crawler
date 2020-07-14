import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    url = 'https://katalog.trojmiasto.pl/moda_i_uroda/salony_kosmetyczne'
    def start_requests(self):
        yield scrapy.Request(self.url, self.parse)

    def parse(self, response):
        for quote in response.css('div.basic-information'):

           yield {
                'title': quote.css('h1 a span::text').get(),
                'www': quote.css('div.wrap dl.ob-details dd.www').xpath('a/@href').getall(),
           }

        pages = response.css('li.page-step').xpath('a')
        page = list(filter(lambda x: x.xpath('@title').get() == 'następna', pages))[0]
        if page is not None:
            next_pages = page.xpath('@href').get()
            if next_pages is not None:
                page = self.url + next_pages
                yield response.follow(page, self.parse)


