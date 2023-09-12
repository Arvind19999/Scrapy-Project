import scrapy


class AudibleSpider(scrapy.Spider):
    name = "audible"
    allowed_domains = ["www.audible.com"]
    start_urls = ["https://www.audible.com/search"]
    
    # def startRequest(self):
    #     yield scrapy.Request(url ='https://www.audible.com/search' , callback= self.parse,
    #                   headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'})

    def parse(self, response):
        # products = response.xpath('//div[@class="adbl-impression-container "]/div/span[2]/ul/li')
        # products = response.xpath('//div[@class="adbl-impression-container "]/div/span[2]/ul/li//div[contains(@class,"bc-col-12")]')
        divList = response.xpath('//div[@class="adbl-impression-container "]/div/span[2]/ul/li/div/div/div')
        mainList = divList.xpath('.//div[contains(@class,"bc-col-6")]/div/div/span/ul')
        for product in mainList:
            title = product.xpath('.//li/h3/a/text()').get()
            author = product.xpath('.//li/span/a/text()').get()
            narattedBy = product.xpath('.//li[contains(@class,"narratorLabel")]/span/a/text()').getall()
            length = product.xpath('.//li[contains(@class,"runtimeLabel")]/span/text()').get()
            releaseDate = product.xpath('.//li[contains(@class,"releaseDateLabel")]/span/text()').get()
            language = product.xpath('.//li[contains(@class,"languageLabel")]/span/text()').get()
            ratings = product.xpath('.//li[contains(@class,"ratingsLabel")]/span/text()').get()
            yield{
                'Title' :title,
                'Author' : author,
                'NarratedBy' : narattedBy,
                'RunTime' : length,
                'ReleaseDate' : releaseDate,
                'Language' : language,
                'Ratings' : ratings,
                'User-Agent' : response.request.headers['User-Agent']
                 
            }
            
        pagination = response.xpath('.//span/ul[contains(@class,"pagingElements")]')
        next_page_url = pagination.xpath('.//li/span[contains(@class,"nextButton")]/a/@href').get()


        if(next_page_url):
            yield response.follow(url=next_page_url, callback = self.parse,
                                  headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'})
