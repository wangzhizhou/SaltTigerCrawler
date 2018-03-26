from beautifulscraper import BeautifulScraper
import re

  
def getUrls(tag = None):
    scraper = BeautifulScraper()
    site = "https://salttiger.com/" + ("" if tag == None else "tag/%s/" % tag.lower())
    body = scraper.go(site)  
    n = 0
    articles = body.select('article')   
    for article in articles:
        header = article.select('h1.entry-title')[0].text
        
        links = article.select('div.entry-content p')[0].select('a')
        if len(links) > 0:
            link = links[-1]['href']
        else:
            link = "Not Found Download link"
            
        n = n + 1
        print('(%d)%s - %s' % (++n,header,link))

    totalPages = body.select('div.wp-pagenavi span.pages')[0].text
    pattern = re.compile(r'(\d+)')
    counts = int(re.findall(pattern,totalPages)[-1])  

    for i in range(2,counts + 1):

        url = site + ("page/%d/" % i)
        body = scraper.go(url)
        articles = body.select('article')

        for article in articles:
            header = article.select('h1.entry-title')[0].text

            links = article.select('div.entry-content p')[0].select('a')
            if len(links) > 0:
                link = links[-1]['href']
            else:
                link = "Not Found Download link"

            n = n + 1
            print('(%d)%s - %s' % (++n,header,link))
    

if __name__ == '__main__':
    getUrls()