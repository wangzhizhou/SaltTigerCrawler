from beautifulscraper import BeautifulScraper
import re

  
def getUrls(tag = None):
    scraper = BeautifulScraper()
    site = "https://salttiger.com" + ("" if tag == None else "/tag/%s" % tag.lower())
    body = scraper.go(site)  

    articles = body.select('article')
    totalPages = body.select('div.wp-pagenavi span.pages')[0].text
    pattern = re.compile(r'(\d+)')
    counts = int(re.findall(pattern,totalPages)[-1])    
    for article in articles:
        header = article.select('h1.entry-title')[0].text
        link = article.select('div.entry-content p')[0].select('a')[-1]['href']
        print('%s - %s' % (header,link))

if __name__ == '__main__':
    getUrls()