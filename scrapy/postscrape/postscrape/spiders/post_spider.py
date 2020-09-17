import scrapy

class PostsSpider(scrapy.Spider):
    name = 'posts'
    
    start_urls = [
        'https://blog.scrapinghub.com/page/1/',
        # 'https://blog.scrapinghub.com/page/2/',
    ]

    # def parse(self, response):
    #     page = response.url.split('/')[-1]
    #     filename = 'posts-%s.html' % page
    #     with open(filename, 'wb') as f:
    #         f.write(response.body)

    def parse(self, response):
        for post in response.css('div.post-item'):
            yield {
                'title': post.css('.post-header h2 a::text')[0].get(),
                'date': post.css('.post-header a::text')[1].get(),
                'author': post.css('.post-header a::text')[2].get(),
                # 'title': post.css('.post-item h2 a::text')[0].get(),
                # 'date': post.css('.post-item a::text')[2].get(),
                # 'author': post.css('.post-item a::text')[3].get(),
                # 'article': post.css('.post-content p::text')[0].get(),
            }
        next_page = response.css('a.next-posts-link::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)