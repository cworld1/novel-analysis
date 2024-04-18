import json, random
from pyecharts.charts import Radar, Graph
from pyecharts import options as opts


class AnalCharacter:
    showTitle = False

    def __init__(self, path="./data", sub_folder="longzu"):
        # Init path
        self.detailed_path = f"{path}/{sub_folder}/longzu_analysis.json"

    def anal(self, name: str, shape: str, callback=None):
        if name == "longzu":
            if shape == "graph":
                context = {
                    "title": "Character Relationship Graph",
                }
                draw = self.draw_relationship_graph(context)
                return draw.dump_options_with_quotes()
            elif shape == "radar":
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
            .set_series_opts(label_opts=opts.LabelOpts(is_show=True))
        )
        if self.showTitle:
            radar.set_global_opts(title_opts=opts.TitleOpts(title=context["title"]))

        if callback:
            callback(radar)

        return radar

    def draw_relationship_graph(self, context: dict):
        # 定义人物及其关系，确保关系与小说情节一致
        self.characters = {
            "路明非": [
                "路鸣泽",
                "恺撒",
                "楚子航",
                "诺诺",
                "芬格尔",
                "龙皇尼特霍格",
                "龙王诺顿",
                "赵孟华",
                "曼施坦因",
                "古德里安",
            ],
            "路鸣泽": ["路明非", "芬格尔"],
            "恺撒": ["路明非", "楚子航", "诺诺", "龙皇尼特霍格", "龙王诺顿"],
            "楚子航": [
                "路明非",
                "诺诺",
                "恺撒",
                "古德里安",
                "曼施坦因",
                "龙皇尼特霍格",
                "龙王诺顿",
            ],
            "诺诺": ["楚子航", "路明非", "恺撒", "曼施坦因", "古德里安"],
            "芬格尔": ["路明非", "路鸣泽", "恺撒", "楚子航"],
            "陈雯雯": ["路明非", "赵孟华"],
            "赵孟华": ["陈雯雯", "路明非"],
            "古德里安": ["恺撒", "路明非", "楚子航", "曼施坦因", "诺诺", "恺撒"],
            "曼施坦因": ["路明非", "曼施坦因", "古德里安", "楚子航", "恺撒", "诺诺"],
            "龙皇尼特霍格": ["路明非", "楚子航", "恺撒", "龙王诺顿"],
            "龙王诺顿": ["龙皇尼特霍格", "楚子航", "恺撒", "路明非"],
        }

        # 定义关系类型
        self.relations = {
            ("路明非", "路鸣泽"): "兄弟",
            ("路明非", "路鸣泽"): "兄弟",
            ("路明非", "恺撒"): "竞争关系",
            ("路明非", "恺撒"): "竞争关系",
            ("路明非", "陈雯雯"): "友好",
            ("路明非", "楚子航"): "好友",
            ("楚子航", "路明非"): "好友",
            ("楚子航", "凯撒"): "竞争关系",
            ("楚子航", "曼施坦因"): "学生-教师",
            ("路明非", "诺诺"): "亲近",
            ("诺诺", "路明非"): "亲近",
            ("诺诺", "芬格尔"): "亲近",
            ("诺诺", "楚子航"): "亲近",
            ("路明非", "芬格尔"): "教师-学生",
            ("芬格尔", "路明非"): "同盟",
            ("芬格尔", "楚子航"): "好友",
            ("芬格尔", "恺撒"): "好友",
            ("芬格尔", "诺诺"): "好友",
            ("芬格尔", "诺诺"): "好友",
            ("芬格尔", "路鸣泽"): "好友",
            ("路鸣泽", "芬格尔"): "同盟",
            ("路明非", "曼施坦因"): "学生-教师",
            ("路明非", "古德里安"): "学生-教师",
            ("曼施坦因", "路明非"): "教师-学生",
            ("曼施坦因", "楚子航"): "教师-学生",
            ("曼施坦因", "凯撒"): "教师-学生",
            ("曼施坦因", "诺诺"): "教师-学生",
            ("曼施坦因", "芬格尔"): "教师-学生",
            ("古德里安", "路明非"): "教师-学生",
            ("古德里安", "楚子航"): "教师-学生",
            ("古德里安", "恺撒"): "教师-学生",
            ("古德里安", "诺诺"): "教师-学生",
            ("古德里安", "芬格尔"): "教师-学生",
            ("曼施坦因", "古德里安"): "好友",
            ("古德里安", "曼施坦因"): "好友",
            ("陈雯雯", "赵孟华"): "情侣",
            ("赵孟华", "陈雯雯"): "情侣",
            ("赵孟华", "路明非"): "竞争关系",
            ("陈雯雯", "路明非"): "友好",
            ("恺撒", "路明非"): "同盟",
            ("恺撒", "诺诺"): "情侣",
            ("恺撒", "楚子航"): "竞争关系",
            ("恺撒", "龙皇尼特霍格"): "敌视",
            ("恺撒", "古德里安"): "学生-教师",
            ("恺撒", "曼施坦因"): "学生-教师",
            ("路明非", "龙皇尼特霍格"): "敌视",
            ("龙皇尼特霍格", "恺撒"): "敌视",
            ("龙皇尼特霍格", "路明非"): "敌视",
            ("龙皇尼特霍格", "楚子航"): "敌视",
            ("楚子航", "龙皇尼特霍格"): "敌视",
            ("楚子航", "古德里安"): "学生-教师",
            ("楚子航", "曼施坦因"): "学生-教师",
            ("龙王诺顿", "楚子航"): "敌视",
            ("龙王诺顿", "恺撒"): "敌视",
            ("龙王诺顿", "路明非"): "敌视",
            ("龙王诺顿", "龙皇尼特霍格"): "从属关系",
        }

        # 定义阵营颜色
        self.camp_colors = {
            "路明非": "#1f78b4",  # 主角营
            "路鸣泽": "#1f78b4",
            "恺撒": "#1f78b4",
            "楚子航": "#1f78b4",
            "诺诺": "#1f78b4",
            "芬格尔": "#1f78b4",
            "陈雯雯": "#1f78b4",
            "赵孟华": "#1f78b4",
            "古德里安": "#a6cee3",  # 中立或复杂关系
            "曼施坦因": "#a6cee3",
            "龙皇尼特霍格": "#e31a1c",  # 敌对阵营
            "龙王诺顿": "#e31a1c",
        }
        nodes = [
            {
                "name": name,
                "symbolSize": 50,
                "itemStyle": {"color": self.camp_colors.get(name, "#c2c2c2")},
            }
            for name in self.characters.keys()
        ]
        links = []
        for source, targets in self.characters.items():
            for target in targets:
                if (source, target) in self.relations:
                    links.append(
                        {
                            "source": source,
                            "target": target,
                            "value": self.relations[(source, target)],
                        }
                    )
                elif (target, source) in self.relations:
                    links.append(
                        {
                            "source": source,
                            "target": target,
                            "value": self.relations[(target, source)],
                        }
                    )

        graph = (
            Graph()
            .add(
                series_name="",
                nodes=nodes,
                links=links,
                layout="force",
                repulsion=5000,
                linestyle_opts=opts.LineStyleOpts(curve=0.2),
                label_opts=opts.LabelOpts(is_show=True, position="right", font_size=12),
            )
            .set_global_opts(title_opts=opts.TitleOpts(title=context["title"]))
        )

        return graph


# Test
# anal_character = AnalCharacter()
# anal_character.anal("longzu", shape="radar", callback=lambda x: x.render("longzu_mbti_radar.html"))
