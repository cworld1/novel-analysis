import spacy
from transformers import pipeline
from collections import defaultdict, Counter
from pyecharts.charts import Graph
from pyecharts import options as opts
import os
from transformers import pipeline

# # 禁用SSL证书验证（警告：不安全）
# os.environ['PYTHONHTTPSVERIFY'] = '0'

# self.sentiment_analyzer = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")

class RelationshipSentimentAnalyzer:
    def __init__(self, characters_info):
        self.nlp = spacy.load('zh_core_web_trf')
        self.sentiment_analyzer = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")
        self.characters_info = characters_info
        os.environ['PYTHONHTTPSVERIFY'] = '0'
        self.sentiment_analyzer = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")
    
    def analyze_text(self, text):
        doc = self.nlp(text)
        relationships = defaultdict(lambda: defaultdict(list))
        character_list = {alias: name for name, aliases in self.characters_info.items() for alias in aliases}

        for sent in doc.sents:
            characters_in_sent = [character_list[ent.text] for ent in sent.ents if ent.label_ == 'PERSON' and ent.text in character_list]
            for character in characters_in_sent:
                for other_character in characters_in_sent:
                    if character != other_character:
                        sentiment_result = self.sentiment_analyzer(sent.text[:512])[0]  # Only process the first 512 chars
                        relationships[(character, other_character)]['sentences'].append(sent.text)
                        relationships[(character, other_character)]['sentiments'].append(sentiment_result['label'])

        return relationships

    def visualize_relationships(self, relationships):
        nodes = [{"name": name} for name in self.characters_info.keys()]
        links = []
        for (src, tgt), info in relationships.items():
            sentiment_count = Counter(info['sentiments'])
            most_common_sentiment, _ = sentiment_count.most_common(1)[0]
            links.append({"source": src, "target": tgt, "value": most_common_sentiment})
        
        graph = Graph()
        graph.add("", nodes, links, repulsion=5000)
        graph.set_global_opts(title_opts=opts.TitleOpts(title="Character Relationships"))
        graph.render("relationship_graph.html")

# 示例用法
characters_info = {
    "路明非": ["路明", "路明非"],
    "楚子航": ["楚子航"],
    "凯撒": ["凯撒", "恺撒·加图索"],
    "诺诺": ["诺诺"],
    "芬格尔": ["芬格尔"],
    "古德里安": ["古德里安"],
    "龙皇尼特霍格": ["龙皇尼特霍格"],
    "曼施坦因": ["曼施坦因"],
    "龙王诺顿": ["龙王诺顿"]
}

analyzer = RelationshipSentimentAnalyzer(characters_info)

# 读取指定文件进行分析
with open("/root/HanLP/龙族Ⅰ火之晨曦.txt", 'r', encoding='utf-8') as file:
    text = file.read()

relationships = analyzer.analyze_text(text)
analyzer.visualize_relationships(relationships)
