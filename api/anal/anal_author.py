import csv, json
import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols
from pyecharts.charts import Bar, Scatter
from pyecharts import options as opts
import matplotlib.pyplot as plt
from anal_helper import set_font

class AnalAuthor:
    def __init__(self, path="./data", interaction=True):
        self.path = path
        if not interaction:
            import matplotlib
            matplotlib.use("Agg")
        set_font()

    def anal(self):
        authors_books = {}
        with open(f"{self.path}/authors.csv", "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if None in row.values() or "" in row.values():
                    continue
                primary_book_path = f"{self.path}/rank_book_info/{row['BookId']}.json"
                additional_books_paths = [f"{self.path}/author_book_info/{bookId}.json" for bookId in row["Books"].split(";")]
                authors_books[row["Name"]] = [primary_book_path] + additional_books_paths

        analysis_data = self.anal_authors_genre_pop(authors_books)
        analysis_df = pd.DataFrame(analysis_data)
        self.draw_genre_popularity_bar(analysis_df)
        self.draw_wordcount_popularity_scatter(analysis_df)

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
                        genre_key = (book_info["categoryName"], book_info["subCategoryName"])
                        genre_counts[genre_key] = genre_counts.get(genre_key, 0) + 1
                except FileNotFoundError:
                    print(f"File not found: {book_path}")
                    continue
            preferred_genre = max(genre_counts, key=genre_counts.get) if genre_counts else None
            analysis_data.append({
                "Name": author,
                "AverageWords": total_words / books_count if books_count else 0,
                "PreferredGenreStr": ", ".join(preferred_genre) if preferred_genre else "N/A",
                "AveragePopularity": total_collect_count / books_count if books_count else 0,
            })
        return analysis_data

    def draw_genre_popularity_bar(self, analysis_data):
        avg_pop_by_genre = analysis_data.groupby("PreferredGenreStr")["AveragePopularity"].mean().sort_values(ascending=False)
        bar = (Bar()
               .add_xaxis(list(avg_pop_by_genre.index))
               .add_yaxis("Average Popularity", list(avg_pop_by_genre.values))
               .set_global_opts(title_opts=opts.TitleOpts(title="Average Popularity by Genre"),
                                xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-45)),
                                yaxis_opts=opts.AxisOpts(name="Average Collect Count")))
        bar.render("genre_popularity_bar.html")
    
    def draw_wordcount_popularity_scatter(self, analysis_data):
        word_counts = analysis_data["AverageWords"].tolist()
        popularities = analysis_data["AveragePopularity"].tolist()
        correlation = np.corrcoef(word_counts, popularities)[0, 1]
        print("Correlation coefficient between word count and popularity:", correlation)
        scatter = (Scatter()
                   .add_xaxis(word_counts)
                   .add_yaxis("Popularity", popularities)
                   .set_global_opts(title_opts=opts.TitleOpts(title="Relationship between Word Count and Popularity"),
                                    xaxis_opts=opts.AxisOpts(name="Word Count"),
                                    yaxis_opts=opts.AxisOpts(name="Average Collect Count")))
        scatter.render("wordcount_popularity_scatter.html")

# Test
anal_author = AnalAuthor()
anal_author.anal()
