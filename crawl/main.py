from crawl_rankings import CrawlRankings
from craw_info import CrawlInfo

path = "./data/"

if __name__ == "__main__":
    rankingsCrawler = CrawlRankings(path)
    infoCrawler = CrawlInfo(path, forceUpdate=False)
    rankingsCrawler.crawl(lambda id: infoCrawler.crawl(id))
