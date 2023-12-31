import scrapy
# a library contains modules to be used in the code
# without the necessity of rewriting.
from ..items import QuotetutorialItem

class QuoteSpider(scrapy.Spider):
    # a class is a model which describes the attributes (variables)
    # and methods ( the way the code will behave)
    name = 'quotes'
    start_urls = [
        'https://quotes.toscrape.com/'
    ]

    def parse(self, response):
        # parsing is transforming one thing on another.

        items = QuotetutorialItem()

        all_div_quotes = response.css('div.quote')

        for quotes in all_div_quotes:

            title = quotes.css('span.text::text').extract()
            author = quotes.css('.author::text').extract()
            tag = quotes.css('.tag::text').extract()
        # in this case, I am transforming a css tag

            items['title'] = title
            items['author'] = author
            items['tag'] = tag
        # here I am storing the data in the temporary container

            yield items
        # yield is used in generators functions. basically I am generating
        # a dictionary with the tag and values contained in the container items

        next_page = response.css('li.next a::attr(href)').get()

        # here I am getting the button "next" wich take me to the next page

        if next_page is not None:
            yield response.follow(next_page, callback= self.parse)


        # and now what I am saying is, if the next page is not empty, go to the next page
        # then call de method parse and crawl the new page. for now on the scrpit will follow
        # this loop until the next page be an empty page
