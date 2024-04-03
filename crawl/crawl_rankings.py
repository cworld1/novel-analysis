import os
import requests
from bs4 import BeautifulSoup


class CrawlRankings:
    url = "https://www.hongxiu.com/rank"
    headers = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2.1 Safari/605.1.15",
        "Cookie": "traffic_utm_referer=https%3A//baidu.com/; landing_page=/; _csrfToken=hvHCmVgFbWDa0O1VEOYIS5BQnpfn2rk3AC4nPP8w; fuid=660bb66c74dbb; newstatisticUUID=1712043628_888611462",
    }
    filename = "ranking.csv"

    def __init__(self, path="./data/") -> None:
        # Init path
        self.path = path
        os.makedirs(self.path, exist_ok=True)

    def crawl(self, callback=None):
        # Request the page
        resp = requests.get(url=self.url, headers=self.headers)
        soup = BeautifulSoup(resp.text, "html.parser")

        # Select the module content
        module_content = soup.select(".main-content-wrap > .rank-body > .rank-list")

        file = open(self.path + self.filename, "w", encoding="utf-8")
        # Write the header
        file.write(f"Category,Rank,Title,BookId,Link\n")

        for content in module_content:
            element = content.find()
            if element.name != "h3":
                continue
            # Get category
            category = element.get_text(strip=True)
            # print(category)

            # For each category, get the ul list
            li_list = element.find_next_sibling("div").ul
            for li in li_list.find_all("li"):
                # print(li)
                rank = li.span.get_text(strip=True)
                title = li.a.text.get_text(strip=True)
                url = li.a["href"]
                id = url.split("/")[-1]
                file.write(
                    f"{category},{rank},{title},{id},https://www.hongxiu.com{url}\n"
                )

                # If callback is not None, call it (eg, to crawl the book info)
                if callback is not None:
                    callback(id)

        file.close()


# Test
crawler = CrawlRankings()
crawler.crawl()
# crawler.crawl(lambda id: print(id))
