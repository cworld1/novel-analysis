import spacy
import re
from collections import Counter
import os

# 加载spaCy中文模型
nlp = spacy.load('zh_core_web_trf')

# 创建EntityRuler并添加规则
ruler = nlp.add_pipe("entity_ruler", before="ner")
patterns = [
    {"label": "PERSON", "pattern": "路明非"},
    {"label": "PERSON", "pattern": "路鸣泽"},
    {"label": "PERSON", "pattern": "诺诺"},
    {"label": "PERSON", "pattern": "陈墨瞳"},
    {"label": "PERSON", "pattern": "陈雯雯"},
    {"label": "PERSON", "pattern": "楚子航"},
    {"label": "PERSON", "pattern": "恺撒·加图索"},
    {"label": "PERSON", "pattern": "恺撒"},
    {"label": "PERSON", "pattern": "芬格尔"}
]
ruler.add_patterns(patterns)

# 读取小说文本
input_path = "/root/HanLP/龙族Ⅰ火之晨曦.txt"
output_directory = "/root/HanLP/output_chapters"

# 确保输出目录存在
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

with open(input_path, 'r', encoding='utf-8') as file:
    data = file.read()

# 使用正则表达式找到所有的章节起始点，并分割章节
chapter_titles = re.findall(r'(第[一二三四五六七八九十百千万\d]+幕 [^\n]*)', data)
chapters = re.split(r'第[一二三四五六七八九十百千万\d]+幕 [^\n]*', data)[1:]

# 确保章节和标题数量匹配
assert len(chapters) == len(chapter_titles)

# 逐章执行NER并统计人物
for index, (title, chapter) in enumerate(zip(chapter_titles, chapters), 1):
    print(f"Processing {title}...")
    doc = nlp(chapter)
    characters = [ent.text for ent in doc.ents if ent.label_ == 'PERSON']
    character_counter = Counter(characters)

    # 保存每章的统计结果到文件
    output_path = os.path.join(output_directory, f"chapter_{index}_characters.csv")
    with open(output_path, 'w', encoding='utf-8') as f:
        for character, count in character_counter.items():
            f.write(f"{character},{count}\n")

    print(f"Saved {title} results to {output_path}")
