# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class Serata(scrapy.Item):
    nome=scrapy.Field()
    luogo=scrapy.Field()
    lunedi=scrapy.Field()
    lunediora=scrapy.Field()
    martedi=scrapy.Field()
    martediora=scrapy.Field()
    mercoledi=scrapy.Field()
    mercolediora=scrapy.Field()
    giovedi=scrapy.Field()
    giovediora=scrapy.Field()
    venerdi=scrapy.Field()
    venerdiora=scrapy.Field()
    sabato=scrapy.Field() 
    sabatoora=scrapy.Field()  
