# -*- coding: utf-8 -*-
import scrapy
from ..items import ShiyanlouItem


class CoursesSpider(scrapy.Spider):
    name = 'courses'
    
    @property
    def start_urls(self):
        url_list = ['https://github.com/shiyanlou?tab=repositories',]

        return url_list

    def parse(self, response):
        for course in response.css('li.col-12'):
            item = ShiyanlouItem ({
                'name': course.css('a::text').extract_first().strip(),
                'update_time': course.css('relative-time::attr(datetime)').extract_first(),
                })
            course_url = course.css('h3 a::attr(href)').extract_first()
            full_course_url = response.urljoin(course_url)
            request = scrapy.Request(full_course_url, self.parse_author)
            request.meta['item'] = item
            yield request
        url = response.css('div.BtnGroup a::attr(href)').extract()[-1]
        yield response.follow(url, callback=self.parse)

    def parse_author(self, response):
        item = response.meta['item']
        ext = response.css('ul.numbers-summary span::text').extract()
        # 如果是空仓库，ext 就是空列表，通不过 if 判断
        if ext:
            item['commits'] = ext[0]
            item['branches'] = ext[1]
            item['releases'] = ext[2]
        yield item

        
