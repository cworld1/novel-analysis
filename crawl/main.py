from crawl_rankings import CrawlRankings
from craw_info import CrawlInfo

path = "./data/"  # path where the data will be stored
forceUpdate = False  # whether to force update the data

if __name__ == "__main__":
    rankingsCrawler = CrawlRankings(path)
    infoCrawler = CrawlInfo(path, forceUpdate=forceUpdate)
    rankingsCrawler.crawl(lambda id: infoCrawler.crawl(id))
