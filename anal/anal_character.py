import json
from pyecharts.charts import Radar
from pyecharts import options as opts
import random


class FetchCharacter:
    def __init__(self, path="./data", sub_folder="longzu"):
        # Init path
        self.detailed_path = f"{path}/{sub_folder}/longzu_analysis.json"

    def fetch(self, name):
        if name == "longzu":
            with open(self.detailed_path, "r", encoding="utf-8") as file:
                data = json.load(file)
                for item in data:
                    # 调用create_mbti_radar_chart函数并将返回结果存储为mbtiRadar
                    item["mbtiRadar"] = self.create_mbti_radar_chart(item["mbti"])
            return data
        else:
            return {}

    def create_mbti_radar_chart(self, mbti_type):
        # 完整的属性对应关系，包括所有特性及其对立特性
        scores = {"E": 0, "I": 0, "S": 0, "N": 0, "T": 0, "F": 0, "J": 0, "P": 0}
        pairs = {
            "E": "I",
            "I": "E",
            "S": "N",
            "N": "S",
            "T": "F",
            "F": "T",
            "J": "P",
            "P": "J",
        }

        # 只随机生成指定MBTI类型中包含的属性的得分
        for trait in mbti_type:
            if scores[trait] == 0:  # 只有当得分未被设置时才生成
                score = random.randint(51, 100)
                opposite_trait = pairs[trait]
                scores[trait] = score
                scores[opposite_trait] = 100 - score

        # 配置雷达图的指示器，成对出现
        schema = [
            opts.RadarIndicatorItem(name="E", max_=100),
            opts.RadarIndicatorItem(name="S", max_=100),
            opts.RadarIndicatorItem(name="T", max_=100),
            opts.RadarIndicatorItem(name="J", max_=100),
            opts.RadarIndicatorItem(name="I", max_=100),
            opts.RadarIndicatorItem(name="N", max_=100),
            opts.RadarIndicatorItem(name="F", max_=100),
            opts.RadarIndicatorItem(name="P", max_=100),
        ]

        # 雷达图数据
        mbti_scores = [
            scores[trait] for trait in ["E", "S", "T", "J", "I", "N", "F", "P"]
        ]

        # 创建雷达图
        radar_chart = Radar(init_opts=opts.InitOpts(width="600px", height="600px"))
        radar_chart.add_schema(schema=schema, shape="circle")
        radar_chart.add(
            series_name="MBTI Profile",
            data=[mbti_scores],
            linestyle_opts=opts.LineStyleOpts(color="#f9713c"),
            areastyle_opts=opts.AreaStyleOpts(opacity=0.7, color="#f9713c"),
        )
        radar_chart.set_global_opts(
            title_opts=opts.TitleOpts(title="MBTI Profile Radar Chart")
        )
        radar_chart.set_series_opts(label_opts=opts.LabelOpts(is_show=True))

        return radar_chart


# Test
# fetch = FetchCharacter()
# all_character_data = fetch.fetch("longzu")
# print(all_character_data)
