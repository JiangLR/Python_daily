# -*- coding: utf-8 -*-
import re
import scrapy

class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/114493/']


    def parse(self, response):
        # 提取文章具体字段
        title = response.xpath('//div[@class="entry-header"]/h1/text()').extract_first("")

        create_date = response.xpath('//p[@class="entry-meta-hide-on-mobile"]/text()').extract()[0]. \
            strip().replace('·', '').strip()

        praise_nums = int(response.xpath("//span[contains(@class, 'vote-post-up')]/h10/text()").extract()[0])

        fav_nums = response.xpath("//span[contains(@class, 'bookmark-btn')]/text()").extract()[0]

        match_re = re.match('.*?(\d+).*', fav_nums)
        if match_re:
            fav_nums = int(match_re.group(1))
        else:
            fav_nums = 0

        comments_nums = response.xpath("//a[@href='#article-comment']/span/text()").extract()[0]
        match_re = re.match('.*?(\d+).*', comments_nums)
        if match_re:
            comments_nums = int(match_re.group(1))
        else:
            comments_nums = 0

        content = response.xpath("//div[@class='entry']").extract()[0]

        tag_list = response.xpath('//p[@class="entry-meta-hide-on-mobile"]/a/text()').extract()
        tag_list = [element for element in tag_list if not element.strip().endswith('评论')]
        tags = ','.join(tag_list)

        # # -------------------------------------------------------
        # # 通过css选择器提取字段
        # title = response.css('.entry-header h1::text').extract()[0]
        # create_date = response.css('p.entry-meta-hide-on-mobile::text').extract()[0]. \
        #     strip().replace('·', '').strip()
        # praise_nums = response.css(".vote-post-up h10::text").extract()[0]
        # fav_nums = response.css(".bookmark-btn::text").extract()[0]
        # match_re = re.match(".*?(\d+).*", fav_nums)
        # if match_re:
        #     fav_nums = int(match_re.group(1))
        # else:
        #     fav_nums = 0
        #
        # comment_nums = response.css("a[href='#article-comment'] span::text").extract()[0]
        # match_re = re.match(".*?(\d+).*", comment_nums)
        # if match_re:
        #     comment_nums = int(match_re.group(1))
        # else:
        #     comment_nums = 0
        #
        # content = response.css("div.entry").extract()[0]
        #
        # tag_list = response.css("p.entry-meta-hide-on-mobile a::text").extract()
        # tag_list = [element for element in tag_list if not element.strip().endswith("评论")]
        # tags = ",".join(tag_list)

        pass
