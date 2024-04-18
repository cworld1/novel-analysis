from pyecharts.charts import Pie, Line
from pyecharts import options as opts
import random
from datetime import datetime, timedelta

# 随机生成情感分析结果
def fake_sentiment_analysis():
    positive = random.random()
    neutral = random.random() * (1 - positive)
    negative = 1 - positive - neutral
    return positive * 100, neutral * 100, negative * 100

# 创建情感分析饼图
def create_pie_chart(positive, neutral, negative):
    chart = Pie()
    chart.add("Sentiment", [("Positive", positive), ("Neutral", neutral), ("Negative", negative)])
    chart.set_global_opts(title_opts=opts.TitleOpts(title="Sentiment Analysis Pie Chart"))
    chart.set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c:.2f}%"))
    return chart

# 生成情感得分的时间序列数据
def generate_sentiment_data(num_days, trend_type="random"):
    sentiments = []
    if trend_type == "high_to_low":
        base_score = 80
        sentiments = [base_score - ((base_score-50)/num_days) * i + random.uniform(-5, 5) for i in range(num_days)]
    elif trend_type == "low_to_high":
        base_score = 20
        sentiments = [base_score + ((80-base_score)/num_days) * i + random.uniform(-5, 5) for i in range(num_days)]
    elif trend_type == "steady":
        base_score = 50 + random.uniform(-5, 5)  # 基本分数加随机波动
        sentiments = [base_score + random.uniform(-2, 2) for _ in range(num_days)]
    elif trend_type == "sudden_spike":
        sentiments = [30 + random.uniform(-5, 5) for _ in range(num_days // 2)]
        sentiments += [70 + random.uniform(-5, 5) for _ in range(num_days // 2, num_days)]
    else:  # Random variation
        sentiments = [random.uniform(30, 70) for _ in range(num_days)]
    return sentiments

# 创建情感得分时间序列图
def create_line_chart(dates, sentiments):
    chart = Line()
    chart.add_xaxis(dates)
    chart.add_yaxis("Sentiment Score", sentiments)
    chart.set_global_opts(title_opts=opts.TitleOpts(title="Sentiment Score Over Time"))
    return chart

# 处理评论生成图表
def process_sentiment_over_time(start_date, num_days, trend_type="random"):
    dates = [(start_date + timedelta(days=i)).strftime("%Y-%m-%d") for i in range(num_days)]
    sentiments = generate_sentiment_data(num_days, trend_type)
    
    # 创建饼图和时间序列图
    pie_chart = create_pie_chart(*fake_sentiment_analysis())
    line_chart = create_line_chart(dates, sentiments)

    # 保存图表
    pie_chart.render("sentiment_pie_chart.html")
    line_chart.render("sentiment_line_chart.html")

# 主函数
if __name__ == "__main__":
    start_date = datetime.now() - timedelta(days=90)  # 从今天起算，过去三个月
    num_days = 90  # 过去三个月的数据
    process_sentiment_over_time(start_date, num_days, trend_type="random")  # 可以更改trend_type来展示不同的趋势
