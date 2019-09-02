# -*- coding: utf-8 -*-
import scrapy
from ..items import ShiyanlouItem


class CoursesSpider(scrapy.Spider):
    name = 'courses'
    
    @property
    def start_urls(self):
        url_list = [
                'https://github.com/shiyanlou?tab=repositories',
                'https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK0MjAxNy0wNi0wN1QwMDowNjo1M1rOBZKSjQ%3D%3D&tab=repositories',
                'https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK5MjAxNS0wMS0zMVQyMDoyMDowMiswODowMM4BzHi1&tab=repositories',
                'https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK5MjAxNC0xMi0wNFQwMDoxNzo1MyswODowMM4BpCnu&tab=repositories',
                'https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK5MjAxNC0wOS0xNlQxMDowNjowMyswODowMM4Bb3Ud&tab=repositories']

        return url_list

    def parse(self, response):
        for course in response.css('li.col-12'):
            item = ShiyanlouItem({
                'name': course.css('a::text').extract_first().strip(),
                'update_time': course.css('relative-time::attr(datetime)').extract_first()
                })
            print(item)
            yield item
