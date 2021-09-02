# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

class ZcroccoPipeline(object):


	def process_item(self, item, spider):
		def discrimine(giorno):
			discrimine="cocktail"
			if discrimine not in item.get(giorno):
				item[giorno]=""
		settimana=["lunedi","martedi","mercoledi","giovedi","venerdi","sabato"]
		for giorno in settimana:
			discrimine(giorno)		
		return item
