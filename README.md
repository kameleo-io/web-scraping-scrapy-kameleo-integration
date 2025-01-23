# Scrapy & Kameleo Integration for web scraping

These examples help to showcase how to gather data efficiently from websites with advanced anti-bot protection like [Cloudflare](https://cloudflare.com/) Turnstile.

## 1-showcase-the-speed-of-scrapy

- I use [Scrapy](https://pypi.org/project/Scrapy/) to gather data from [quotes.toscrape.com](https://quotes.toscrape.com/) website.
- The spider go over the 10 pages of data in 2.6 second ensuring a really effective technique.

## 2-compare-speed-with-headless-browser

- In the second example I use [Playwright](https://playwright.dev/) to scrape the same dataset form the [quotes.toscrape.com](https://quotes.toscrape.com/) website.
- The headless browser renders the page this makes the scraping slower. It takes about 6.4 second.

---
Headless browsers come handy when you scrape data from websites with heavy javascript. When data is protected by anti-bot systems, the best you can do is to utilize an anti-detect browser. [Kameleo](https://kameleo.io/web-scraping?utm_medium=github_readme&utm_campaign=scrapy_kameleo_integration) provides an undetectable web automation browser. This is not an open-source solution, however the team provides unlimited fresh fingerprints, and ensures that their custom-built browsers (Chroma and Junglefox) are constantly updated to ensure, you stay on top of the anti-bot game without tiring maintenance overhead.

In the second part of the demo we try to scrape data from the [review page of BurgerKing on indeed.com](https://www.indeed.com/cmp/Burger-King/reviews).

If you try to open the page, you will see the [Cloudflare turnstile](https://www.cloudflare.com/application-services/products/turnstile/)
![Cloudflare Turnstile](./readme-res/indeed-com-with-cloudflare-turnstyle.png)

Most headless Chrome browsers fail to bypass this protection layer.
> According to Pierluigi Vinciguerra from [The Web Scraping Club](https://substack.thewebscraping.club/p/how-to-bypass-cloudflare-turnstile?utm_source=kameleo_github&utm_campaign=scrapy_kameleo) 4 out of 5 open-source headless browsers absolutely fail to pass Cloudflare turnstile. And when you find a working solution it is not guaranteed that it will stay like that.    

[Kameleo](https://kameleo.io/web-scraping?utm_medium=github_readme&utm_campaign=scrapy_kameleo_integration) is an anti-detect browser specialized for web scraping. Kameleo is constantly tested against anti-bot systems. Updates are quickly deployed to ensure you don't need to maintain your code to keep a high success rate.

---

## 3-bypass-cloudflare-turnstile-with-Kameleo

- Kameleo launches its undetected chrome (called Chroma) with a fresh fingerprint.
- It simply bypasses the Cloudflare Turnstile and loads the BurgerKing review page on indeed.com
- We export the `cf_clearance` cookie which is our "pass for future cloudflare cookies"

## 4-add-cf_clearance-cookie-to-scrapy

- Scrapy wouldn't be able to scrape the data from the BurgerKing review page due to an `unauthorized` error message caused by the protection by Cloudflare.
![Unauthorized error message caused by Cloudflare Turnstile](./readme-res/unauthorized-error-message-caused-by-cloudflare-turnstile.png)
- So I add the `cf_clearance` cookie to the request.
- Note that I also need to set up the same `user-agent` for Scrapy that I used with Kameleo to get the `cf_clearance` cookie.
- This ensures I can do effective scraping behind Cloudflare's protection layer 