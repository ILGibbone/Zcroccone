# -*- coding: utf-8 -*-
import scrapy

class SaloRagno(scrapy.Spider):
	name = 'saloragno'
	start_urls = [
		'https://www.fuorisalone.it/it/2022/eventi'
	]

	def parse(self, response):
		lista=response.xpath('//a[@class="col-xs-12 nopadding item_related_link event_box_item base"]/@href').extract()
		print(len(lista))
		for pagina in lista:
			if "fuorisalone.it" in pagina:
				print(f'pagina is {pagina}')
				yield scrapy.Request(pagina, self.parse_pages)

		#scorri
		next_page = response.xpath('//a[@rel="next"]/@href').extract_first()
		if next_page is not None:
			next_page = response.urljoin(next_page)
			print(f'next page is{next_page}')
			yield scrapy.Request(next_page, callback=self.parse)

	def parse_pages(self, response):
		a=response.xpath('//div[@class="ora_palinsesto"]').re('cocktail')
		if not a:
			print('nulla')
		else:
			result={
				"name":[],
				"cocktails":[],
				"address":[]}
			result['name']=response.xpath('//h1[@class="event_title strong col-xs-12 col-md-9 col-lg-8 nopadding"]/text()').get()
			result['address']=response.xpath('//a[@class="link-indirizzo-location"]/text()').get()
			giorni = response.css(".giorno_palinsesto")
			for giorno in giorni:
				if "cocktail" in giorno.extract():
					data = (giorno.xpath("div[@class='data_palinsesto']/text()").extract()[1].strip())
					ora = (giorno.xpath("div[@class='ora_palinsesto']/span/text()").extract_first().strip())
					data_ora= data+" "+ora
					result["cocktails"].append(data_ora)
			yield result
