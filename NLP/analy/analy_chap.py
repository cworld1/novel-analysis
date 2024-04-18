import spacy
import re
import os
from collections import Counter

def extract_text_for_character(chapter, character_aliases, nlp):
    """
    在单个章节中提取包含指定角色别名的句子。
    Args:
        chapter (str): 章节的文本内容。
        character_aliases (dict): 每个主角色名到其别名列表的映射。
        nlp (object): 已加载的spaCy模型。
    Returns:
        dict: 每个角色相关的句子列表。
    """
    doc = nlp(chapter)
    related_sentences = {name: [] for name in character_aliases}

    for sent in doc.sents:
        for character, aliases in character_aliases.items():
            if any(ent.text in aliases for ent in sent.ents if ent.label_ == 'PERSON'):
                related_sentences[character].append(sent.text.strip())

    return related_sentences

def main():
    # 加载spaCy中文模型
    nlp = spacy.load('zh_core_web_trf')

    # 定义小说的路径和output目录
    novel_path = "/root/HanLP/龙族Ⅰ火之晨曦.txt"
    output_directory = "/root/HanLP/character_analysis"
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # 读取小说文本
    with open(novel_path, 'r', encoding='utf-8') as file:
        data = file.read()

    # 使用正则表达式找到所有的章节起始点，并分割章节
    chapter_titles = re.findall(r'(第[一二三四五六七八九十百千万\d]+幕 [^\n]*)', data)
    chapters = re.split(r'第[一二三四五六七八九十百千万\d]+幕 [^\n]*', data)[1:]  # 忽略第一个匹配前的文本

  
    assert len(chapters) == len(chapter_titles)

    # 定义人物及其别名
    character_aliases = {
        "路明非": ["路明", "路明非", "路","路明非鞠躬"],
        "路鸣泽": ["路鸣泽", "鸣泽"],
        "诺诺": ["诺诺","诺诺满脸","诺诺捏","诺诺微","墨瞳", "陈墨瞳"],
        "楚子航": ["楚子航","楚子航像","楚子航会","楚子航黄金色","楚子航喊"],
        "恺撒": ["恺撒", "恺撒·加图索","凯撒站","凯撒冰","凯撒冰","凯撒垂"],
        "芬格尔":["芬格尔·冯·弗林斯","芬格尔","芬格尔不解"]
    }

    # 逐章执行NER并统计人物相关句子
    for index, (title, chapter) in enumerate(zip(chapter_titles, chapters), 1):
        print(f"Processing {title}...")
        related_texts = extract_text_for_character(chapter, character_aliases, nlp)

        for character, sentences in related_texts.items():
            if sentences:  # 如果有相关句子，保存到文件
                chapter_path = os.path.join(output_directory, f"{title.replace(' ', '_')}")
                os.makedirs(chapter_path, exist_ok=True)
                with open(os.path.join(chapter_path, f"{character}.txt"), 'w', encoding='utf-8') as f:
                    f.write("\n".join(sentences))
                print(f"Saved related texts for {character} in {title}")

if __name__ == "__main__":
    main()
