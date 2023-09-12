import scrapy

#Scrapping the data from Single page
class WorldometersSpider(scrapy.Spider):
    name = "worldometers"
    allowed_domains = ["www.worldometers.info"]
    start_urls = ["https://www.worldometers.info/world-population/population-by-country"]

    def parse(self, response):
        title = response.xpath('//h1/text()').get()
        countries = response.xpath('//td/a')
        
        for country in countries:
            Text = country.xpath('.//text()').get()
            Link = country.xpath('.//@href').get()
            #Absolute method of URL join 
            # absolutUrl = f'https://www.worldometers.info{Link}'
            # absolutUrl = response.urljoin(Link)
            #Absolute URL to return values
            # yield scrapy.Request(url = absolutUrl)
            
            # Relative URL to join and return values
            yield response.follow(url = Link)
            
            #Realtive method of URL join
            # yield {
            #     'Text' : Text,
            #     'Link' : Link
            # }