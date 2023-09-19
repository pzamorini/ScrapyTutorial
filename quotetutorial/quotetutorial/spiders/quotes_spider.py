import scrapy
# a library contains modules to be used in the code
# without the necessity of rewriting.

class QuoteSpider(scrapy.Spider):
    # a class is a model which describes the attributes (variables)
    # and methods ( the way the code will behave)
    name = 'quotes'
    start_urls = [
        'https://quotes.toscrape.com/'
    ]

    def parse(self, response):
        # parsing is transforming one thing on another.
        all_div_quotes = response.css('div.quote')

        for quotes in all_div_quotes:

            title = quotes.css('span.text::text').extract()
            author = quotes.css('.author::text').extract()
            tag = quotes.css('.tag::text').extract()
        # in this case, I am transforming a css tag
            yield {
                'title': title,
                'author': author,
                'tag': tag
        }
        # yield is used in generators functions. basically I am generating
        # a dictionary with the tag as key, and the title as value.