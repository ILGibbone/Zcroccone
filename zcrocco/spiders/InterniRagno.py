# -*- coding: utf-8 -*-
import scrapy
from zcrocco.items import Interni

class InterniRagno(scrapy.Spider):
	name = 'interniragno'
	start_urls = [
		'https://www.internimagazine.it/guida-fuorisalone-2022/eventi/tag/cocktail/'
	]

	def parse(self, response):
		lista = response.xpath('//a[@class="dw-card-link"]/@href').extract()
		for pagina in lista:
			yield scrapy.Request(pagina, self.parse_pages)

		#scorri
		next_page = response.xpath('//a[@class="next page-numbers"]/@href').extract_first()
		yield scrapy.Request(next_page, callback=self.parse)


	def parse_pages(self, response):
			event_list=[a.attrib['data-description'] for a in response.xpath('//div[@class="dw-card-add-to-calendar"]')]
			result={
			"name":[],
			"cocktails":[],
			"address":[]}
			for ev in event_list:
				if "Cocktail" in ev:
					if not "invito" in ev:
						result["cocktails"].append(ev)
						name = response.xpath("//div[@class='dw-content-espositore']/h2/text()").extract_first()
						result["name"] = name
						address = response.xpath("//div[@class='dw-info-company-text']/a/p/text()").extract_first()
						result["address"] = address
						yield result
