import scrapy
import json


class ReviewSpider(scrapy.Spider):
    name = "review"

    # Set up user agent
    custom_settings = {
        'USER_AGENT': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"
    }

    def start_requests(self):
        # Read cookies exported from Kameleo browser profile
        with open('../3-bypass-cloudflare-turnstile-with-Kameleo/cf_clearance_cookie.json', 'r') as file:
            json_data = file.read()
        cookies_list = json.loads(json_data)

        # Convert to Scrapy format
        cookies = {cookie["name"]: cookie["value"] for cookie in cookies_list}

        # Add cookies to the request
        yield scrapy.Request(
            url="https://www.indeed.com/cmp/Burger-King/reviews",
            cookies=cookies,
            callback=self.parse
        )

    def parse(self, response):
        self.logger.info(f"User-Agent used: {response.request.headers['User-Agent']}")
        review_titles = response.css('h2[data-testid="title"] span::text').getall()
        yield {"Review titles": review_titles}