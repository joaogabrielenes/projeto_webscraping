import scrapy


class NotebookSpider(scrapy.Spider):
    name = "notebook"
    allowed_domains = ["kabum.com.br"]
    start_urls = ["https://www.kabum.com.br"]
    count_page = 1
    max_page = 1

    def parse(self, response):
        products = response.css('article.sc-27518a44-3.hLEhJe.productCard')

        for product in products:
            
            yield{
                'brand': product.css('span.sc-d79c9c3f-0.nlmfp.sc-27518a44-9.iJKRqI.nameCard::text').get(),
                'cupom': product.css('span.text-xxs.uppercase.overflow-hidden.text-ellipsis.whitespace-nowrap::text').get()
            } 

