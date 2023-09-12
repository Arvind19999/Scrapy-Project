import scrapy

#Scrapy with multipage
class WorldometersmultpagesSpider(scrapy.Spider):
    name = "worldometersMultPages"
    allowed_domains = ["www.worldometers.info"]
    start_urls = ["https://www.worldometers.info/world-population/population-by-country"]

    def parse(self, response):
        title = response.xpath('//h1/text()').get()
        countries = response.xpath('//td/a')
        
        for country in countries:
            countryName = country.xpath('.//text()').get()
            link = country.xpath('.//@href').get()
        
            yield response.follow(url = link, callback = self.parseCountry,meta={'Country' : countryName})
            
    def parseCountry(self,response):
        Country = response.request.meta["Country"]
        # response.xpath('(//table[@class ="table table-striped table-bordered table-hover table-condensed table-list"])[1]/tbody/tr')
        rows = response.xpath('(//table[contains(@class,"table")])[1]/tbody/tr')
        for row in rows:
            year = row.xpath('.//td[1]/text()').get()
            population = row.xpath('.//td[2]/strong/text()').get()
            
            yield {
                'Country' : Country,
                'Year' : year,
                'Population' : population
            }
            # yield {
            # 'Text' : text,
            # 'Link' : link
            # }
