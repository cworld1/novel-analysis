import csv, json

# Data processing
import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols

# Plot
import matplotlib.pyplot as plt
import matplotlib

from api.api_helper import convert_wan, set_font


class AnalAuthor:
    file = "authors.csv"

    def __init__(self, path="./data", interaction=True) -> None:
        self.path = path
        # Hide ui if needed
        if not interaction:
            matplotlib.use("Agg")
        # Set font for different systems (to support Chinese)
        set_font()

    def anal(self, callback=lambda: plt.show()):
        # data = []
        authors_books = {}
        with open("./data/authors.csv", "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if None in row.values() or "" in row.values():  # 判断是否存在空数据
                    continue

                primary_book_path = f"./data/rank_book_info/{row['BookId']}.json"
                additional_books_paths = [
                    f"./data/author_book_info/{bookId}.json"
                    for bookId in row["Books"].split(";")
                ]
                all_books_paths = [primary_book_path] + additional_books_paths
                authors_books[row["Name"]] = all_books_paths

                # words = convert_wan(row["TotalWords"])
                # row["TotalWords"] = words
                # row["BooksCount"] = len(row["Books"].split(";"))

                # data.append(row)

        # print(data)
        # print(authors_books)
        authors_genre_pop = self.anal_authors_genre_pop(authors_books)
        # print(authors_genre_pop)
        self.draw_genre_pop_wordcount_rs(pd.DataFrame(authors_genre_pop))

    def anal_authors_genre_pop(self, authors_books):
        """
        分析每个作者的创作类型偏好，并存储结果到类属性中。
        """
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
                        # 累计字数
                        total_words += book_info.get("wordsCount", 0)
                        # 累加收藏数
                        total_collect_count += book_info.get("collectCount", 0)
                        books_count += 1

                        genre_key = (
                            book_info["categoryName"],
                            book_info["subCategoryName"],
                        )
                        # 分类
                        genre_counts[genre_key] = genre_counts.get(genre_key, 0) + 1
                except FileNotFoundError:
                    print(f"File not found: {book_path}")
                    continue
            preferred_genre = (
                max(genre_counts, key=genre_counts.get) if genre_counts else None
            )
            author_data = {
                "Name": author,
                "AverageWords": total_words / books_count if books_count else 0,
                "PreferredGenreStr": (
                    ", ".join(preferred_genre) if preferred_genre else "N/A"
                ),
                "AveragePopularity": (
                    total_collect_count / books_count if books_count else 0
                ),
            }
            analysis_data.append(author_data)
        return analysis_data

    def draw_genre_pop_wordcount_rs(self, analysis_data):
        # Use OLS model for ANOVA
        model = ols(
            "AveragePopularity ~ C(PreferredGenreStr)", data=analysis_data
        ).fit()
        anova_results = sm.stats.anova_lm(model, typ=2)
        print("ANOVA results for genre and popularity:\n", anova_results)

        avg_pop_by_genre = analysis_data.groupby("PreferredGenreStr")[
            "AveragePopularity"
        ].mean()

        plt.figure(figsize=(12, 6))
        plt.barh(avg_pop_by_genre.index, avg_pop_by_genre)

        plt.title("Average Popularity by Genre")
        plt.xlabel("Average Collect Count")
        plt.ylabel("Genre")
        plt.tight_layout()
        plt.show()

        correlation = np.corrcoef(
            analysis_data["AverageWords"],
            analysis_data["AveragePopularity"],
        )[0, 1]
        print(
            "Correlation coefficient between word count and popularity: ", correlation
        )

        plt.figure(figsize=(10, 6))
        plt.scatter(analysis_data["AverageWords"], analysis_data["AveragePopularity"])
        plt.title("Relationship between Word Count and Popularity")
        plt.xlabel("Word Count")
        plt.ylabel("Collect Count")
        plt.tight_layout()
        plt.show()


# worknum_authors=df.groupby('Name')['Books'].sum()
# wordnum_authors=df.groupby('Name')['TotalWords'].median()
# createday_authors=df.groupby('Name')['TotalDays'].median()
# df1=analyze_authors_genre_and_popularity(df,authors_books)
# df2=analyze_authors_genre_preferences(authors_books)
# visualize_genre_popularity_wordcount_relationship(df1)

# Test
anal_author = AnalAuthor()
anal_author.anal()
