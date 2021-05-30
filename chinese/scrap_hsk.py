import scrapy
from scrapy.crawler import CrawlerProcess

start_url = 'http://hanzidb.org/character-list/general-standard?page='

class KanjiSpider(scrapy.Spider):
    name = 'kanjispider'
    start_urls = [start_url + str(i + 1) for i in range(82)]

    def parse(self, response):
        table = response.css("table")
        for row in table.css("tr"):
            yield {'character': row.xpath('td[1]//text()').extract_first(),
                   'pinyin': row.xpath('td[2]//text()').extract_first(),
                   'definition': row.xpath('td[3]//text()').extract_first(),
                   'radical_all': row.xpath('td[4]//text()').extract_first(),
                   'radical': row.xpath('td[4]//a//text()').extract_first(),
                   'stroke_count': row.xpath('td[5]//text()').extract_first(),
                   'hsk_level': row.xpath('td[6]//text()').extract_first(),
                   'standard': row.xpath('td[7]//text()').extract_first(),
                   'frequency_rank': row.xpath('td[8]//text()').extract_first(),
                   }


process = CrawlerProcess(settings={
    "FEEDS": {
        "items.json": {"format": "json"},
    },
})
process.crawl(KanjiSpider)
process.start()