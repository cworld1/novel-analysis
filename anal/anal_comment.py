import csv
import random
from datetime import datetime, timedelta
from pyecharts import options as opts
from pyecharts.charts import WordCloud, Pie, Line


class AnalComment:
    def __init__(self, path="./data", comment_file="comment_frequency.csv"):
        self.path = path
        self.comment_file = comment_file

    def anal(self, shape="wordcloud"):
        if shape == "wordcloud":
            return self.generate_wordcloud()
        elif shape == "pie":
            return self.create_pie_chart()
        elif shape == "line":
            return self.create_line_chart(30, "random")
        else:
            return None

    def generate_wordcloud(self):
        with open(f"{self.path}/{self.comment_file}", "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            data = [row for row in reader if int(row["Frequency"]) > 10]
        words = [(row["Word"], int(row["Frequency"])) for row in data]
        wordcloud = WordCloud()
        wordcloud.add(
            "WordCloud of Comments",
            words,
            shape="circle",
            word_size_range=[18, 66],
        ).set_global_opts(
            title_opts=opts.TitleOpts(title="WordCloud of Comments"),
            tooltip_opts=opts.TooltipOpts(is_show=True),
        )
        return wordcloud

    def create_pie_chart(self):
        positive, neutral, negative = self.fake_sentiment_analysis()
        pie_chart = Pie()
        pie_chart.add(
            "Sentiment",
            [("Positive", positive), ("Neutral", neutral), ("Negative", negative)],
        )
        return pie_chart

    def create_line_chart(self, num_days, trend_type):
        start_date = datetime.now() - timedelta(days=num_days)
        dates = [
            (start_date + timedelta(days=i)).strftime("%Y-%m-%d")
            for i in range(num_days)
        ]
        sentiments = self.generate_sentiment_data(num_days, trend_type)
        line_chart = Line()
        line_chart.add_xaxis(dates)
        line_chart.add_yaxis("Sentiment Score", sentiments)
        return line_chart

    def fake_sentiment_analysis(self):
        positive = random.random()
        neutral = random.random() * (1 - positive)
        negative = 1 - positive - neutral
        return positive * 100, neutral * 100, negative * 100

    def generate_sentiment_data(self, num_days, trend_type="random"):
        sentiments = []
        if trend_type == "high_to_low":
            base_score = 80
            sentiments = [
                base_score - ((base_score - 50) / num_days) * i + random.uniform(-5, 5)
                for i in range(num_days)
            ]
        elif trend_type == "low_to_high":
            base_score = 20
            sentiments = [
                base_score + ((80 - base_score) / num_days) * i + random.uniform(-5, 5)
                for i in range(num_days)
            ]
        elif trend_type == "steady":
            base_score = 50 + random.uniform(-5, 5)
            sentiments = [base_score + random.uniform(-2, 2) for _ in range(num_days)]
        elif trend_type == "sudden_spike":
            sentiments = [30 + random.uniform(-5, 5) for _ in range(num_days // 2)]
            sentiments += [
                70 + random.uniform(-5, 5) for _ in range(num_days // 2, num_days)
            ]
        else:
            sentiments = [round(random.uniform(30, 70), 2) for _ in range(num_days)]

        return sentiments


# 示例用法
# anal_comment = AnalComment()
# wordcloud_chart = anal_comment.anal(shape="wordcloud")
# wordcloud_chart.render("wordcloud_comments.html")
# pie_chart = anal_comment.anal(shape="pie")
# pie_chart.render("sentiment_pie_chart.html")
# line_chart = anal_comment.anal(shape="line")
# line_chart.render("sentiment_line_chart.html")
