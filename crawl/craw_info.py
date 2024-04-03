import os
import requests
import json


class CrawlInfo:
    url = "https://appapi.hongxiu.com/api/v3/book/info"
    headers = {
        "Host": "appapi.hongxiu.com",
        "Cookie": "appId=41; areaId=4; channel=appstore; qimei=+psPuwp3Th9neFAS0O3iFYfy8XgZ/UlijYHF2jp7iIhespUMicdyRAu3SNjphRI0; ywguid=-999; ywkey=",
        "Connection": "keep-alive",
        "userInfo": "sOahvFEA4eoIk2aH2OqoQnQ8f7W6xcJCxsSZp7-dGi_Qp-QvpKxjMA==",
        "Accept": "application/json",
        "deviceInfo": "teT3g/YElb1PONleoS8/Q/vjER6v4CjtzvNvR0fLzvMvujU0BXaM9gbetgqb6vBC4U+2qaWpCdahsm3bOP53Q9knUAtGUx9Q2WQ/0e8V2KztZhybMDVYeHWD7VfPIdBihEx5hWWI734WNTxuBrUkRikDr04Gv2Jc7XSRgtOGQVlKsP4Kh3LsCxeS+r/sjYWI",
        "User-Agent": "readx/8.29.80 (iPhone; iOS 16.1.2; Scale/2.00)",
        "Accept-Language": "en-US;q=1, zh-Hans-US;q=0.9",
        "s": "LoveTagAB=0,YQFinishedAIAB=1,LoveFinishedAIAB=1,contentSourceType=1,MembershipGuideIsTheWeb=1,HXYQTabRec=1,YqTagAB=1,loveNewBookAB=1,ChannelMembershipGuideIsTheWeb=1,NewRechargeSDK4=0,newUserFeedTop=1,newUserBottomRecommend=1,yqNewBookAB=1,newUserPreload=1,HXYQLOV_RANK_AB=0,newUserReliefStationV2=1,newUserReliefStation=1,HXLoveTab=1,NewRechargeSDK=0,card_exit=1,HotRankDayAB=0,NewRechargeSDK2=0,vip_day=0",
        "Accept-Encoding": "gzip, deflate, br",
    }
    forceUpdate = False

    def __init__(self, path="./data/", forceUpdate=False) -> None:
        # Init path
        self.detailed_path = path + "book_info/"
        os.makedirs(self.detailed_path, exist_ok=True)
        self.forceUpdate = forceUpdate

    def crawl_data(self, id, i) -> json:
        # Request the page
        response = requests.get(
            url=f"{self.url}?bookId={id}&screen={i}", headers=self.headers
        )
        if response.status_code != 200:
            print(f"GET request faild{response.status_code}")
            return

        # Get the JSON data
        book_info = response.json()
        if book_info["msg"] != "成功":
            print(book_info["msg"])
            return

        return book_info["data"]

    def deep_merge_dicts(self, dict1, dict2):
        """
        Deep merge dict2 into dict1
        """
        for key, value in dict2.items():
            if key in dict1:
                if isinstance(dict1[key], dict) and isinstance(value, dict):
                    self.deep_merge_dicts(dict1[key], value)
                elif value is not None:
                    dict1[key] = value
            else:
                dict1[key] = value

    def crawl(self, id: str):
        # Check if the file already exists (only when forceUpdate is False)
        file_path = os.path.join(self.detailed_path, f"{id}.json")
        if not self.forceUpdate and os.path.exists(file_path):
            return

        # Get the data from the two screens and merge them
        data1 = self.crawl_data(id, 2)
        data2 = self.crawl_data(id, 1)
        merged_data = data1.copy()
        self.deep_merge_dicts(merged_data, data2)

        # Write the data to the file
        json_data = json.dumps(
            merged_data, indent=4, ensure_ascii=False
        )  # indent=4 for pretty print, optional
        with open(file_path, "w") as file:
            file.write(json_data)
        print("File write:", file_path)


# Test
crawler = CrawlInfo()
crawler.crawl("8263527304935303")
