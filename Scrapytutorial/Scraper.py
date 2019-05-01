import scrapy
import parser

class SportSpider(scrapy.Spider):
    name = "Sport_spider"
    start_urls = ['https://www.goal.com/en-us/transfer-news']

    def parse(self, response):
        SET_SELECTOR = '.type-article'
        for sport in response.css(SET_SELECTOR):

            NAME_SELECTOR = 'h3 ::text'
            LINK_SELECTOR = "a ::attr(href)"
            print("https://www.goal.com" + sport.css(LINK_SELECTOR).extract_first())

'''
            yield {
                'name': sport.css(NAME_SELECTOR).extract_first(),
                'link': "https://www.goal.com" + sport.css(LINK_SELECTOR).extract_first()
            }
            '''
