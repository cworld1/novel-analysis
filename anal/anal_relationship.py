import jieba
import jieba.posseg as pseg
import random
from pyecharts import options as opts
from pyecharts.charts import Graph
import os


class AnalCharacter:
    def __init__(self, path="./data", sub_folder="longzu",filename="longzu_content.txt"):
        self.file_path = os.path.join(path, sub_folder,filename)

    def extract_main_characters(self, top_n=6):
        with open(self.file_path, 'r', encoding='utf-8') as file:
            text = file.read()

        words = pseg.cut(text)
        names = [word for word, flag in words if flag == 'nr']

        name_count = {}
        for name in names:
            name_count[name] = name_count.get(name, 0) + 1

        sorted_name_count = sorted(name_count.items(), key=lambda x: x[1], reverse=True)

        top_characters = [name for name, count in sorted_name_count[:top_n]]

        return top_characters

    def generate_relationship_graph(self, shape, top_n=6):
        if shape == "relationship":
            top_characters = self.extract_main_characters(top_n=top_n)
            graph_options = self.create_relationship_graph(top_characters)
            return graph_options
        else:
            return None

    def create_relationship_graph(self, top_characters):
        relations = {}
        with open(self.file_path, 'r', encoding='utf-8') as file:
            text = file.read()

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

        return graph
# 示例用法
# anal_character = AnalCharacter()
# anal_character.generate_relationship_graph(shape="relationship").render()
