import csv, json
import numpy as np
import pandas as pd
from pyecharts.charts import Bar, Scatter
from pyecharts import options as opts
from pyecharts.charts import HeatMap


class AnalAuthor:
    primary_book_folder = "rank_book_info"
    additional_books_folder = "author_book_info"

    def __init__(self, path="./data", file="authors.csv") -> None:
        self.path = path
        self.file = file

    def anal(self, shape="bar"):
        authors_books = {}

        with open(f"{self.path}/{self.file}", "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if None in row.values() or "" in row.values():
                    continue
                primary_book_path = (
                    f"{self.path}/{self.primary_book_folder}/{row['BookId']}.json"
                )
                additional_books_paths = [
                    f"{self.path}/{self.additional_books_folder}/{bookId}.json"
                    for bookId in row["Books"].split(";")
                ]
                authors_books[row["Name"]] = [
                    primary_book_path
                ] + additional_books_paths

        analysis_data = self.anal_authors_genre_pop(authors_books)
        analysis_df = pd.DataFrame(analysis_data)

        if shape == "bar":
            # Draw bar plot
            context = {
                "title": "Average Popularity by Preferred Genre",
                "xlabel": "Preferred Genre",
                "ylabel": "Average Collect Count",
            }
            draw = self.draw_genre_popularity_bar(analysis_df, context)
        elif shape == "scatter":
            # Draw scatter plot
            draw = self.draw_wordcount_popularity_scatter(analysis_df)
        elif shape =="heat":
            #Draw heat map
            context = {
                "title": "Novel Author Popularity Heatmap",
                "xlabel": "AuthorName",
                "ylabel": "Popularities Count",
            }
            draw = self.draw_author_popularity_heatmap(analysis_df,context)
        else:
            return None
        
        return draw

    def anal_authors_genre_pop(self, authors_books):
        analysis_data = []
        for author, books_paths in authors_books.items():
            total_words = 0
            genre_counts = {}
            total_collect_count = 0
            books_count = 0
            for book_path in books_paths:
                try:
                    with open(book_path, "r", encoding="utf-8") as file:
                        data = json.load(file)
                        book_info = data["bookInfo"]
                        total_words += book_info.get("wordsCount", 0)
                        total_collect_count += book_info.get("collectCount", 0)
                        books_count += 1
                        genre_key = (
                            book_info["categoryName"],
                            book_info["subCategoryName"],
                        )
                        genre_counts[genre_key] = genre_counts.get(genre_key, 0) + 1
                except FileNotFoundError:
                    print(f"File not found: {book_path}")
                    continue
            preferred_genre = (
                max(genre_counts, key=genre_counts.get) if genre_counts else None
            )
            analysis_data.append(
                {
                    "Name": author,
                    "AverageWords": total_words / books_count if books_count else 0,
                    "PreferredGenreStr": (
                        ", ".join(preferred_genre) if preferred_genre else "N/A"
                    ),
                    "AveragePopularity": (
                        total_collect_count / books_count if books_count else 0
                    ),
                }
            )
        return analysis_data

    def draw_genre_popularity_bar(self, analysis_data, context):
        avg_pop_by_genre = (
            analysis_data.groupby("PreferredGenreStr")["AveragePopularity"]
            .mean()
            .sort_values(ascending=False)
        )
        bar = (
            Bar()
            .add_xaxis(list(avg_pop_by_genre.index))
            .add_yaxis(context["ylabel"], list(avg_pop_by_genre.values))
            .set_global_opts(
                title_opts=opts.TitleOpts(title=context["title"]),
                xaxis_opts=opts.AxisOpts(
                    name=context["xlabel"], axislabel_opts=opts.LabelOpts(rotate=-45)
                ),
                yaxis_opts=opts.AxisOpts(name=context["ylabel"]),
                datazoom_opts=opts.DataZoomOpts(),
            )
        )
        return bar

    def draw_wordcount_popularity_scatter(self, analysis_data):
        word_counts = analysis_data["AverageWords"].tolist()
        popularities = analysis_data["AveragePopularity"].tolist()
        correlation = np.corrcoef(word_counts, popularities)[0, 1]
        #print("Correlation coefficient between word count and popularity:", correlation)
        print(analysis_data)
        scatter = (
            Scatter()
            .add_xaxis(word_counts)
            .add_yaxis("Popularity", popularities)
            .set_global_opts(
                title_opts=opts.TitleOpts(
                    title="Relationship between Word Count and Popularity"
                ),
                xaxis_opts=opts.AxisOpts(name="Word Count"),
                yaxis_opts=opts.AxisOpts(name="Average Collect Count"),
            )
        )
        return scatter

    def draw_author_popularity_heatmap(self, analysis_data, context):
        # 计算平均收藏量的范围，用于设置热力图的颜色映射范围
        min_popularity = analysis_data["AveragePopularity"].min()
        max_popularity = analysis_data["AveragePopularity"].max()

        heatmap_data = []
        for _, row in analysis_data.iterrows():
            # 将收藏量取整
            popularity = int(round(row["AveragePopularity"]))
            heatmap_data.append(
                [row["Name"], row["PreferredGenreStr"], popularity]
            )
        heatmap = (
            HeatMap()
            .add_xaxis(analysis_data["Name"].tolist())
            .add_yaxis(
                context["ylabel"],
                analysis_data["PreferredGenreStr"].tolist(),
                heatmap_data,
                label_opts=opts.LabelOpts(is_show=True, position="inside"),
            )
            .set_global_opts(
                visualmap_opts=opts.VisualMapOpts(min_=min_popularity, max_=max_popularity),
                title_opts=opts.TitleOpts(title=context["title"]),
                xaxis_opts=opts.AxisOpts(name=context["xlabel"]),
                yaxis_opts=opts.AxisOpts(name=context["ylabel"]),
            )
        )
        heatmap.width = "1200px"
        heatmap.height = "800px"
        return heatmap




# Test
anal_author = AnalAuthor()
# anal_author.anal(shape="bar").render("genre_popularity_bar.html")
# anal_author.anal(shape="scatter").render("wordcount_popularity_scatter.html")
anal_author.anal(shape="heat").render("Author_popularity_heatmap.html")