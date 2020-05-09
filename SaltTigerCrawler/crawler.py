#coding=utf-8
from beautifulscraper import BeautifulScraper
import re

class SaltTigerCrawler:
    number = 0
    def getUrls(self, tag = None):
        scraper = BeautifulScraper()
        site = "https://salttiger.com/" + ("" if tag == None else "tag/%s/" % tag.lower())
        body = scraper.go(site)  
        
        articles = body.select('article')   
        for article in articles:
            self.parse_meta_info(article)

        totalPages = body.select('div.wp-pagenavi span.pages')[0].text
        pattern = re.compile(r'(\d+)')
        counts = int(re.findall(pattern,totalPages)[-1])  

        for i in range(2,counts + 1):

            url = site + ("page/%d/" % i)
            body = scraper.go(url)
            articles = body.select('article')

            for article in articles:
                self.parse_meta_info(article)


    def parse_meta_info(self, article):
        header = article.select('h1.entry-title')[0].text.strip()
        meta_info = article.select('div.entry-content p')[0]
        links = meta_info.select('a')
        image_url = meta_info.select('img')[0]['src']
        content_text = "".join(article.select('div.entry-content p')[0].text.strip().split('\n')[-1].split()).split(u"：")[-1]
        if len(links) > 0:
            link = links[-1]['href']
        else:
            link = "Not Found Download link"

        self.number = self.number + 1
        print('(%d)\nTitle: %s\nCover: %s\nBaiduYun: %s\nCode: %s\n' %(self.number, header, image_url, link, content_text if len(content_text) == 4 else "None"))

if __name__ == '__main__':
    SaltTigerCrawler().getUrls('kotlin')