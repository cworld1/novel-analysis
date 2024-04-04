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

    def __init__(self, path="./data") -> None:
        # Init path
        self.path = path
        os.makedirs(self.path, exist_ok=True)

    def crawl_data(self, from_id, callback) -> str:
        # Request the page
        resp = requests.get(url=f"{self.url}/{from_id}", headers=self.headers)
        soup = BeautifulSoup(resp.text, "html.parser")

        # Select the module content
        module_content = soup.select_one(".author-state > .info-wrap")
        if module_content is None:
            return f"{from_id},,,,,,,"

        # Get infos
        img_box_div = module_content.find("div", class_="img-box")
        img_link = img_box_div.img["src"]
        level_tag = img_box_div.p.get_text(strip=True)
        name = module_content.h3.get_text(strip=True)
        wrap_li = module_content.find("div", class_="total-wrap").find_all("li")
        total_works, total_words, total_days = [
            li.p.get_text(strip=True) for li in wrap_li
        ]
        # Get books
        books_div = module_content.find("div", class_="other-works")
        if books_div is None:
            books = []
        else:
            books_li = books_div.div.ul.find_all("li")
            books = [li["class"][0][4:] for li in books_li]

        if callback is not None:
            print(f"Callback for author: {name} (from bookid: {from_id})")
            for id in books:
                print(f"Callback for author: {name} (from each book id: {id})")
                callback(id)

        return f'{from_id},{name},{total_works},{total_words},{total_days},{level_tag},"{img_link}",{";".join(books)}'

    def crawl(self, ids: list, callback=None):
        file = open(f"{self.path}/{self.filename}", "w", encoding="utf-8")
        file.write(
            f"BookId,Name,TotalWorks,TotalWords,TotalDays,LevelTag,ImgLink,Books\n"
        )

        for id in ids:
            text = self.crawl_data(id, callback)
            file.write("%s\n" % text)

        file.close()


# Test
crawler = CrawlAuthor()
crawler.crawl([8263527304935303, 17536776207350304])
# crawler.crawl(lambda id: print(id))
