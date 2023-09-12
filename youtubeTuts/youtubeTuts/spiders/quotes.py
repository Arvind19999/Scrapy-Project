import scrapy

from ..items import YoutubetutsItem 
from scrapy.utils.response import open_in_browser
from scrapy.http import FormRequest

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    pageNumber = 2
    allowed_domains = ["quotes.toscrape.com"]
    # start_urls = ["https://quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com/login"]

# # By using Xpath selector
#     def parse(self, response):
#         items = response.xpath("//div[@class='quote']")
        
#         for item in items:
#             title = item.xpath(".//span[@class='text']/text()").get()
#             author  = item.xpath(".//span/small[@class='author']/text()").get()
#             tags = item.xpath(".//div[@class='tags']/a/text()").get()
            
#             yield {
#                 "Title" : title,
#                 "Author" : author,
#                 "Tags" : tags
#             }
# By using CSS selector    
    def parse(self, response):
        token = response.css("form input::attr(value)").get()
        
        return FormRequest.from_response(response, formdata={
            "csrf_token"  : token,
            "username" : "admin",
            "password" : "admin"
        },callback= self.startScraping)
        
    def startScraping(self,response):
        open_in_browser(response)
        items = response.css("div.quote")
        content = YoutubetutsItem()
        for item in items:
            # print(item)
            title = item.css(".text::text").extract()
            author = item.css(".author::text").extract()
            tags = item.css(".tag::text").extract()
            content["title"] = title
            content["author"] = author 
            content["tags"] = tags 
            
            yield content            
        #     # yield {
        #     #     "Title" : title,
        #     #     "Author" : author,
        #     #     "Tags" : tags
        #     # }
        # # nextPage = response.css("li.next a::attr(href)").get()
        # nextPage = "https://quotes.toscrape.com/page/"+str(QuotesSpider.pageNumber)+"/"
        
        # if(QuotesSpider.pageNumber < 11):
        #     yield response.follow(nextPage, callback = self.parse)
        #     QuotesSpider.pageNumber += 1
        
        
        
        # print("***************************************" + token)