import re
import json

from scrapy.selector import Selector
try:
    from scrapy.spider import Spider
except:
    from scrapy.spider import BaseSpider as Spider
from scrapy.utils.response import get_base_url
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor as sle
from scrapy.contrib.linkextractors import LinkExtractor
from babaSR.items import BabasrItem

class BabaSpider(CrawlSpider):
    name = "babaSR"
    allowed_domains = ["douban.com"]
    start_urls = [
        "http://book.douban.com/tag/"
    ]
    rules = [
        Rule(sle(allow=("/subject/\d+/?$")), callback='parse_2'),
        Rule(sle(allow=("/tag/[^/]+/?$", )), follow=True),
        Rule(sle(allow=("/tag/$", )), follow=True),
    ]
    
    def parse(self, response):
        hxs = Selector(response)  
        items = []  
      
        newurls = hxs.xpath('//a/@href').extract()
        validurls = []  
        for url in newurls:   
            if True:  
                validurls.append(url)  
                
            items.extend([self.make_requests_from_url(url).replace(callback=self.parse) for url in validurls])  

            sites = hxs.xpath('//ul/li')  
            items = []  
            for site in sites:  
                item = BabasrItem()
                item['title'] = site.select('a/text()').extract()  
                item['link'] = site.select('a/@href').extract()  
                item['desc'] = site.select('text()').extract()  
                items.append(item)  
            return items  
