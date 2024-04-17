import jieba
import jieba.posseg as pseg
import random
from pyecharts import options as opts
from pyecharts.charts import Graph


class AnalCharacter:
    def __init__(self, file_path):
        self.file_path = file_path

    def extract_main_characters(self, top_n=6):
        with open(self.file_path, 'r', encoding='utf-8') as file:
            text = file.read()

        # 使用jieba进行词性标注
        words = pseg.cut(text)

        # 提取词性为人名（nr）的词
        names = [word for word, flag in words if flag == 'nr']

        # 统计词频
        name_count = {}
        for name in names:
            name_count[name] = name_count.get(name, 0) + 1

        # 按词频降序排序
        sorted_name_count = sorted(name_count.items(), key=lambda x: x[1], reverse=True)

        # 提取出现频率最高的前top_n个词作为主要人物
        top_characters = [name for name, count in sorted_name_count[:top_n]]

        return top_characters

    def create_relationship_graph(self, top_characters):
        relations = {}
        with open(self.file_path, 'r', encoding='utf-8') as file:
            text = file.read()

            # 按段落划分，假设在同一段落中出现的人物具有共现关系
            lst_para = text.split('\n')
            for paragraph in lst_para:
                for name_0 in top_characters:
                    if name_0 in paragraph:
                        for name_1 in top_characters:
                            if name_1 in paragraph and name_0 != name_1:
                                relations[(name_0, name_1)] = relations.get((name_0, name_1), 0) + 1

        max_rela = max(relations.values())
        relations = {k: v / max_rela for k, v in relations.items()}

        nodes = [{"name": name, "symbolSize": 30} for name in top_characters]
        links = [{"source": k[0], "target": k[1], "value": v} for k, v in relations.items()]

        graph = (
            Graph(init_opts=opts.InitOpts(width="1000px", height="600px"))
            .add(
                "",
                nodes=nodes,
                links=links,
                layout="force",
                repulsion=800,
                linestyle_opts=opts.LineStyleOpts(width=2, opacity=1),
                label_opts=opts.LabelOpts(is_show=True, position="right", font_size=12),
            )
            .set_global_opts(title_opts=opts.TitleOpts(title="Character Relationship Graph"))
        )

        graph.render("relationship_graph.html")


# 示例用法
file_path = "E:/ProgramsHW/shixi/novel_analysis/anal/longzu.txt"  # 替换成你的文件路径
relation = CharacterRelationship(file_path)
top_characters = relation.extract_main_characters(top_n=6)
relation.create_relationship_graph(top_characters)
