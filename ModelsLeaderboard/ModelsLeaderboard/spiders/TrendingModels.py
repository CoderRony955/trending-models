from ..items import TrendingModels
import scrapy


class TrendingmodelsSpider(scrapy.Spider):
    name = "TrendingModels"
    allowed_domains = ["huggingface.co"]
    start_urls = ["https://huggingface.co/models?sort=trending"]

    def parse(self, response):
        models = response.css("article")
        for model in models:
            trendingmodel = TrendingModels()
            trendingmodel['Name'] = model.css("h4::text").get()

            url = model.css("a::attr(href)").get()
            trendingmodel["URL"] = response.urljoin(url)

            yield response.follow(url, callback=self.parse_model_details, cb_kwargs={'trendingmodel': trendingmodel})

    def parse_model_details(self, response, trendingmodel):
        trendingmodel["Downloads"] = response.css(
            "dl dd::text").get().strip() or "N/A"
        trendingmodel["Type"] = response.css(
            "div:nth-child(1) a div span::text").get()
        trendingmodel["Likes"] = response.css(
            "h1 div:nth-child(3) button:nth-child(2) ::text").get()
        trendingmodel["Language"] = response.css(
            "div:nth-child(1) a:nth-child(4) div span::text").get()
        trendingmodel["Links"] = ["https://huggingface.co" +
                                  link for link in response.css("div:nth-child(1) a::attr(href)").getall()]

        yield trendingmodel
