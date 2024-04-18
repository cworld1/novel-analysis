from crawl_rankings import CrawlRankings
from craw_info import CrawlInfo
from crawl_author import CrawlAuthor

path = "./data"  # path where the data will be stored
rank_book_folder = "rank_book_info"  # ranks' book info stored folder
author_book_folder = "author_book_info"  # the authors' book info stored folder
forceUpdate = False  # whether to force update the data


def crawl():
    rankingsCrawler = CrawlRankings(path)
    infoBookCrawler = CrawlInfo(path, rank_book_folder, forceUpdate=forceUpdate)
    infoAuthorCrawler = CrawlInfo(path, author_book_folder, forceUpdate=forceUpdate)
    authorCrawler = CrawlAuthor(path)

    # Crawl the rankings
    ids = rankingsCrawler.crawl(
        lambda id: (
            # Crawl the book info
            infoBookCrawler.crawl(id),
        )
    )
    # Crawl the author info and the author's books
    # authorCrawler.crawl(ids, lambda book: infoAuthorCrawler.crawl(book)),


if __name__ == "__main__":
    crawl()
