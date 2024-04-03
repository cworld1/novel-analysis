import os
import requests
from bs4 import BeautifulSoup


class CrawlAuthor:
    url = "https://www.hongxiu.com/book"
    headers = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2.1 Safari/605.1.15",
        "Cookie": "traffic_utm_referer=https%3A//baidu.com/; landing_page=/; _csrfToken=hvHCmVgFbWDa0O1VEOYIS5BQnpfn2rk3AC4nPP8w; fuid=660bb66c74dbb; newstatisticUUID=1712043628_888611462",
    }

    filename = "authors.csv"

    def __init__(self, path="./data/") -> None:
        # Init path
        self.path = path
        self.detailed_path = path + "book_info/"
        os.makedirs(self.detailed_path, exist_ok=True)

    def crawl_data(self, id) -> str:
        # Request the page
        resp = requests.get(url=f"{self.url}/{id}", headers=self.headers).text.encode(
            "UTF-8"
        )
        soup = BeautifulSoup(resp, "html.parser")

        # Select the module content
        module_content = soup.select(".author-state > .info-wrap")[0]
        # Get author img link & level tag
        img_box_div = soup.select(".img-box")[0]
        img_link = img_box_div.img["src"]
        level_tag = img_box_div.p.text.strip()
        # Get author name
        name = module_content.h3.text.strip()
        # Get total wrap info
        wrap_li = module_content.select(".total-wrap")[0].find_all("li")
        total_works, total_words, total_days = [li.p.text.strip() for li in wrap_li]
        text = f"{id}, {name}, {total_works}, {total_words}, {total_days}, {level_tag}, {img_link}"
        # print(text)
        return text

    def crawl(self, ids, callback=None):
        for id in ids:
            file = open(self.path + self.filename, "w", encoding="utf-8")
            file.write(
                f"BookId,Name,TotalWorks,TotalWords,TotalDays,LevelTag,ImgLink\n"
            )

            text = self.crawl_data(id)
            file.write("%s\n" % text)
            if callback is not None:
                callback(id)
        file.close()


# Test
crawler = CrawlAuthor()
crawler.crawl([8263527304935303])
# crawler.crawl(lambda id: print(id))
