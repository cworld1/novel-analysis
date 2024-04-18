import spacy
import os
import csv
from wordcloud import WordCloud
from collections import Counter

# 确保加载适用于中文的spaCy模型
nlp = spacy.load("zh_core_web_trf")

def create_wordcloud(text, output_file, font_path):
    """ 根据给定的文本生成词云图，使用特定的中文字体避免乱码 """
    wordcloud = WordCloud(
        width=800,
        height=400,
        background_color='white',
        font_path=font_path  # 指定中文字体路径
    ).generate(text)
    wordcloud.to_file(output_file)

def main():
    input_dir = "/root/HanLP/output_comment"
    output_csv = "/root/HanLP/combined_comments.csv"
    wordcloud_output = "/root/HanLP/output_comment/wordcloud.png"
    font_path = "/usr/share/fonts/truetype/noto/NotoSansCJK-Regular.ttc"  # 示例字体路径

    # 合并文件中的文本内容
    texts = []
    for filename in os.listdir(input_dir):
        if filename.endswith(".txt"):
            with open(os.path.join(input_dir, filename), 'r', encoding='utf-8') as file:
                texts.append(file.read())

    combined_text = " ".join(texts)

    # 使用spaCy处理合并后的文本并统计词频
    doc = nlp(combined_text)
    words = [token.text for token in doc if not token.is_stop and not token.is_punct and not token.is_space]
    word_freq = Counter(words)

    # 保存统计结果到CSV文件
    with open(output_csv, 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Word', 'Frequency'])
        for word, freq in word_freq.items():
            writer.writerow([word, freq])

    # 创建词云
    create_wordcloud(combined_text, wordcloud_output, font_path)
    print("Wordcloud saved to", wordcloud_output)

if __name__ == "__main__":
    main()
