# -*- coding: utf-8 -*-
import scrapy
import json
from scrapy.exceptions import CloseSpider
class BooksSpider(scrapy.Spider):
    name = 'books'
    allowed_domains = ['openlibrary.org']
    start_urls = ['https://openlibrary.org/subjects/picture_books.json?limit=12']

    INCREMENTED_BY = 12
    offset = 12

    def parse(self, response):
        if response.status == 400:
            raise CloseSpider('Reached the last page...')

        resp = json.loads(response.body)
        ebooks = resp.get('works')
        for ebook in ebooks:
            yield{
                'title': ebook.get('title'),
                'subject' : ebook.get('subject')
            }

        self.offset += self.INCREMENTED_BY
        yield scrapy.Request(
            url = f'https://openlibrary.org/subjects/picture_books.json?limit={self.offset}',
            callback= self.parse
        )