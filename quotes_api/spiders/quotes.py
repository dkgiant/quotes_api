# -*- coding: utf-8 -*-
import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.topscarpe.com']
    start_urls = ['http://quotes.topscarpe.com/']

    def parse(self, response):
        pass
