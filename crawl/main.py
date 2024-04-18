from crawl.crawl_rankings import CrawlRankings
from crawl.craw_info import CrawlInfo
from crawl.crawl_author import CrawlAuthor

path = "./data"  # path where the data will be stored
rank_book_folder = "rank_book_info"  # ranks' book info stored folder
author_book_folder = "author_book_info"  # the authors' book info stored folder
forceUpdate = False  # whether to force update the data


def crawl():
    rankingsCrawler = CrawlRankings(path)
    infoBookCrawler = CrawlInfo(path, rank_book_folder, forceUpdate=forceUpdate)
    # infoAuthorCrawler = CrawlInfo(path, author_book_folder, forceUpdate=forceUpdate)
    # authorCrawler = CrawlAuthor(path)

    # Crawl the rankings
    ids = rankingsCrawler.crawl(
        lambda id: (
            # Crawl the book info
            infoBookCrawler.crawl(id),
        )
    )
    # Crawl the author info and the author's books
    # authorCrawler.crawl(ids, lambda book: infoAuthorCrawler.crawl(book)),

from flask import Flask, jsonify
from datetime import datetime
import os

app = Flask(__name__)

def crawl_time():
    filename = "./data/last_refresh_time.txt"
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    # 读取上次刷新时间
    try:
        with open(filename, "r") as file:
            last_refresh_time = file.read().strip()
    except FileNotFoundError:
        last_refresh_time = "Never"

    # 更新当前刷新时间
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(filename, "w") as file:
        file.write(current_time)
    
    return last_refresh_time


if __name__ == "__main__":
    crawl()
