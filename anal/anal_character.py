import json
from pyecharts.charts import Radar
from pyecharts import options as opts
import random


class AnalCharacter:
    def __init__(self, path="./data", sub_folder="longzu"):
        # Init path
        self.detailed_path = f"{path}/{sub_folder}/longzu_analysis.json"

    def anal(self, name: str, callback=None):
        if name == "longzu":
            context = {
                "title": "MBTI Profile Radar Chart",
                "series": "MBTI Profile",
            }
            with open(self.detailed_path, "r", encoding="utf-8") as file:
                data = json.load(file)
                for item in data:
                    # 调用create_mbti_radar_chart函数并将返回结果存储为mbtiRadar
                    item["mbtiRadar"] = self.draw_mbti_radar(
                        item["mbti"], context, callback
                    ).dump_options_with_quotes()
            return data
        else:
            return {}

    def draw_mbti_radar(self, mbti_type: str, context: dict, callback):
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
                score = random.randint(51, 89)
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
        radar = (
            Radar()
            .add_schema(
                schema=schema,
                shape="circle",
            )
            .add(
                series_name=context["series"],
                data=[mbti_scores],
                linestyle_opts=opts.LineStyleOpts(width=1),
                areastyle_opts=opts.AreaStyleOpts(opacity=0.1),
            )
            .set_global_opts(
                title_opts=opts.TitleOpts(title=context["title"]),
            )
            .set_series_opts(label_opts=opts.LabelOpts(is_show=True))
        )

        if callback:
            callback(radar)

        return radar


# Test
# anal_character = AnalCharacter()
# anal_character.anal("longzu", callback=lambda x: x.render("longzu_mbti_radar.html"))
