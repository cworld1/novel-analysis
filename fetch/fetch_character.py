import json

class FetchCharacter:
    def __init__(self, path="./data", sub_folder="longzu"):
        # Init path
        self.detailed_path = f"{path}/{sub_folder}/analysis.jsonc"


    def fetch(self, name):
        if name == "longzu":
            with open(self.detailed_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
            return data
        else:
            return {}

#test
# fetch = FetchCharacter()
# # 获取全部角色数据
# all_character_data = fetch.fetch("longzu")
# # 打印全部角色数据
# print(all_character_data)
