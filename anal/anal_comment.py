import csv

# Plot
from pyecharts import options as opts
from pyecharts.charts import WordCloud


class AnalComment:

    def __init__(self, path="./data", file="comment_frequency.csv") -> None:
        self.path = path
        self.file = file

    def anal(self, shape="wordcloud"):
        with open(f"{self.path}/{self.file}", "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            # data = list(reader)
            data = [row for row in reader if int(row["Frequency"]) > 10]

        if shape == "wordcloud":
            # Draw wordcloud plot
            context = {
                "title": "WordCloud of Comments",
            }
            draw = self.draw_wordcloud(data, context)
        # elif shape == "pie":
        #     # Draw pie plot
        #     context = {"title": "Composition of Novel Types"}
        #     draw = self.draw_pie(type_counts, context)
        else:
            return None

        return draw

    def draw_wordcloud(self, data: dict, context):
        words = [(row["Word"], int(row["Frequency"])) for row in data]
        # print(words)

        c = (
            WordCloud()
            .add(
                context["title"],
                words,
                shape="circle",
                word_size_range=[18, 66],
            )
            .set_global_opts(
                title_opts=opts.TitleOpts(title=context["title"]),
                tooltip_opts=opts.TooltipOpts(is_show=True),
            )
        )

        return c


# Test
# anal_comment = AnalComment()
# anal_comment.anal(shape="wordcloud").render("wordcloud_custom_mask_image.html")
