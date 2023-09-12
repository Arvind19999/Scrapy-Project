import scrapy
import json

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com/api/quotes?page=1"]

    def parse(self, response):
        # print(response.body)
        jsonResponse = json.loads(response.body)
        quotes = jsonResponse.get("quotes")
        # print(/quotes)
        for quote in quotes:
            yield {
                "Author" : quote.get("author").get("name"),
                "Tags" : quote.get("tags"),
                "Quote" : quote.get("text"),
                }
            
        hasNext = jsonResponse.get("has_next")
        if hasNext:
            nextPageNumber = jsonResponse.get("page") + 1
            
            yield scrapy.Request(
                url = f"https://quotes.toscrape.com/api/quotes?page={nextPageNumber}",
                callback=self.parse,
            )
            
            
