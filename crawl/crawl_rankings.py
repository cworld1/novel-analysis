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
        self.path = path
        os.makedirs(self.path, exist_ok=True)

    def crawl(self, callback=None):
        resp = requests.get(url=self.url, headers=self.headers).text.encode("UTF-8")

        # 在首页中解析出章节的标题和详情页的url
        # 1.实例化BeautifulSoup对象，需要将页面源码数据加载到该对象中
        soup = BeautifulSoup(resp, "html.parser")
        # 2.解析章节标题和详情页的url
        module_content = soup.select(".main-content-wrap > .rank-body > .rank-list")
        # return

        file = open(self.path + self.filename, "w", encoding="utf-8")
        file.write(f"Category,Rank,Title,BookId,Link\n")

        for content in module_content:
            element = content.find()
            if element.name != "h3":
                continue

            # Get category
            category = element.text.strip()
            # print(category)

            li_list = element.find_next_sibling("div").ul

            # 在这里对 ul_element 进行处理，例如提取其中的文本或链接等
            for li in li_list.find_all("li"):
                # print(li)
                rank = li.span.text
                title = li.a.text.strip()
                url = li.a["href"]
                id = url.split("/")[-1]
                file.write(
                    f"{category},{rank},{title},{id},https://www.hongxiu.com{url}\n"
                )
                if callback is not None:
                    callback(id)

        file.close()


crawler = CrawlRankings()
crawler.crawl()
# crawler.crawl(lambda id: print(id))
