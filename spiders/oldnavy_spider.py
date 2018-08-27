import scrapy

class OldnavyScraping(scrapy.Spider):
    # identifies the spider
    name        = "oldnavy"

    # This list uses by default implementation of start_requests() method
    start_urls  = ["https://oldnavy.gap.com/"];
    # New Arrivals section
    def parse(self, response):
        header      =  response.css('div.new-arrivals-container div.new-arrivals-ctas h3 a::text').extract();
        menuList    = [];
        for quote in response.css('div.new-arrivals-container div.new-arrivals-ctas ul.horiz_list li'):
            menuList.append(
                {
                    'menu_url': quote.css('a::attr(href)').extract(),
                    'menu_name': quote.css('a::text').extract()
                }
            )

        yield {
            'header': header,
            'menu'  : menuList
        }