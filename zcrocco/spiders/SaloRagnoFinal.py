# -*- coding: utf-8 -*-
import scrapy
from zcrocco.items import Serata

class SaloRagno(scrapy.Spider):
	name = 'saloragno'
	start_urls = [
		'https://www.fuorisalone.it/it/2022/eventi'
	]

	def parse(self, response):
		lista=response.xpath('//a[@class="col-xs-12 nopadding item_related_link event_box_item special"]/@href').extract()
		print(len(lista))
		for pagina in lista:
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
			serata=Serata()
			serata['nome']=response.xpath('//h1[@class="event_title strong col-xs-12 col-md-9 col-lg-8 nopadding"]/text()').get()
			serata['luogo']=response.xpath('//a[@class="link-indirizzo-location"]/text()').get()
			try:
				serata['lunedi']=response.xpath("/html/body/div/main/article/div[2]/div/div/div[2]/div[1]/div[2]/text()").extract()[1].encode("utf-8").strip()
				serata['lunediora']=response.xpath("/html/body/div/main/article/div[2]/div/div/div[2]/div[1]/div[2]/span/text()").get().encode("utf-8").strip()
			except:
				serata['lunedi']=""
				serata['lunediora']=""
			try:
				serata['martedi']=response.xpath("/html/body/div/main/article/div[2]/div/div/div[2]/div[2]/div[2]/text()").extract()[1].encode("utf-8").strip()
				serata['martediora']=response.xpath("/html/body/div/main/article/div[2]/div/div/div[2]/div[2]/div[2]/span/text()").get().encode("utf-8").strip()
			except:
				serata['martedi']=""
				serata['martediora']=""
			try:
				serata['mercoledi']=response.xpath("/html/body/div/main/article/div[2]/div/div/div[2]/div[3]/div[2]/text()").extract()[1].encode("utf-8").strip()
				serata['mercolediora']=response.xpath("/html/body/div/main/article/div[2]/div/div/div[2]/div[3]/div[2]/span/text()").get().encode("utf-8").strip()
			except:
				serata['mercoledi']=""
				serata['mercolediora']=""
			try:
				serata['giovedi']=response.xpath("/html/body/div/main/article/div[2]/div/div/div[2]/div[4]/div[2]/text()").extract()[1].encode("utf-8").strip()
				serata['giovediora']=response.xpath("/html/body/div/main/article/div[2]/div/div/div[2]/div[4]/div[2]/span/text()").get().encode("utf-8").strip()
			except:
				serata['giovedi']=""
				serata['giovediora']=""
			try:
				serata['venerdi']=response.xpath("/html/body/div/main/article/div[2]/div/div/div[2]/div[5]/div[2]/text()").extract()[1].encode("utf-8").strip()
				serata['venerdiora']=response.xpath("/html/body/div/main/article/div[2]/div/div/div[2]/div[5]/div[2]/span/text()").get().encode("utf-8").strip()
			except:
				serata['venerdi']=""
				serata['venerdiora']=""
			try:
				serata['sabato']=response.xpath("/html/body/div/main/article/div[2]/div/div/div[2]/div[6]/div[2]/text()").extract()[1].encode("utf-8").strip()
				serata['sabatoora']=response.xpath("/html/body/div/main/article/div[2]/div/div/div[2]/div[6]/div[2]/span/text()").get().encode("utf-8").strip()
			except:
				serata['sabato']=""
				serata['sabatoora']=""
			yield serata
