import scrapy

class PostsSpider(scrapy.Spider):
    name = 'posts'
    
    start_urls = [
        'https://www.underwatertimes.com/',
    ]
    
    


    def parse(self, response):
       
        for post in response.css('.breakingnews'):
            yield {
                # 'title': post.css('#left a::text')[0].get(),
                'img_title': post.xpath('//*[@id="clm1"]/div/p[1]')[0].get(),
                # 'date': post.css('.post-header a::text')[1].get(),
                # 'title': post.xpath('//*[@id="clm1"]/div/p[1]/a')[1].get(),
                # 'img': post.css('div a img')[3].get(),
                # 'author': post.css('.post-header a::text')[2].get(),
                # 'title': post.css('.post-item h2 a::text')[0].get(),
                # 'date': post.css('.post-item a::text')[2].get(),
                # 'author': post.css('.post-item a::text')[3].get(),
                # 'article': post.css('.post-content p::text')[0].get(),
            }

            
        # next_page = response.xpath('//*[@id="archive_pages"]/a[1]"]').get()
        # if next_page is not None:
        #     next_page = response.urljoin(next_page)
        #     yield scrapy.Request(next_page, callback=self.parse)

        
