import pandas as pd
import matplotlib.pyplot as plt
import json,platform
import seaborn as sns
import statsmodels.api as sm
from statsmodels.formula.api import ols
import numpy as np

df=pd.read_csv('./data/authors.csv')
df.dropna(subset=['Name', 'Books', 'TotalWords', 'TotalDays'], inplace=True)
df['BooksCount'] = df['Books'].apply(lambda x: len(x.split(';')) if pd.notna(x) else 0)
df['TotalWords'] = df['TotalWords'].str.replace('万', '').astype(float) * 10000
total_authors = df['Name'].nunique()

#引入json
authors_books = {}
for _, row in df.iterrows():
    # 主书籍路径
    primary_book_path = f"./data/book_info/{row['BookId']}.json"
    # 附加书籍路径
    additional_books_paths = [f"./data/author_book_info/{bookId}.json" for bookId in row['Books'].split(';') if pd.notna(row['Books'])]
    # 将主书籍路径和附加书籍路径合并
    all_books_paths = [primary_book_path] + additional_books_paths
    authors_books[row['Name']] = all_books_paths
#分析书籍

class Analauthor:
    def __init__(self, df, authors_books):
        self.df = df
        self.authors_books = authors_books
        # self.authors_preferences = None  # 初始化一个属性来存储作者偏好分析的结果

        # 设置字体，以支持中文显示（针对不同操作系统）
        if platform.system() == "Darwin":  # macOS
            plt.rcParams["font.family"] = "Arial Unicode MS"
        elif platform.system() == "Windows":  # Windows
            plt.rcParams["font.family"] = "SimHei"
        else:  # 其他系统
            plt.rcParams["font.family"] = "Arial"


    def analyze_authors_genre_and_popularity(self):
        """
        分析每个作者的创作类型偏好，并存储结果到类属性中。
        """
        analysis_data = []
        for author, books_paths in self.authors_books.items():
            total_words = 0
            genre_counts = {}
            total_collect_count = 0
            books_count = 0
            for book_path in books_paths:
                try:
                    with open(book_path, 'r', encoding='utf-8') as file:
                        data = json.load(file)
                        book_info = data['bookInfo']
                        #累计字数
                        total_words+=book_info.get('wordsCount', 0)
                        # 累加收藏数
                        total_collect_count += book_info.get('collectCount', 0)
                        books_count += 1
                        
                        genre_key = (book_info['categoryName'], book_info['subCategoryName'])
                        #分类
                        genre_counts[genre_key] = genre_counts.get(genre_key, 0) + 1
                except FileNotFoundError:
                    print(f"File not found: {book_path}")
                    continue
            preferred_genre = max(genre_counts, key=genre_counts.get) if genre_counts else None
            author_data = {
                'Name': author,
                'AverageWords': total_words / books_count if books_count else 0,
                'PreferredGenreStr': ', '.join(preferred_genre) if preferred_genre else 'N/A',
                'AveragePopularity': total_collect_count / books_count if books_count else 0
            }
            analysis_data.append(author_data)
        self.authors_preferences = pd.DataFrame(analysis_data)  # 存储分析结果
        return self.authors_preferences

    def visualize_genre_popularity_wordcount_relationship(self):
        if self.authors_preferences is None:
            print("No author preferences data found. Run analyze_authors_genre_and_popularity first.")
            return
        
        # Use OLS model for ANOVA
        model = ols('AveragePopularity ~ C(PreferredGenreStr)', data=self.authors_preferences).fit()
        anova_results = sm.stats.anova_lm(model, typ=2)
        print("ANOVA results for genre and popularity:\n", anova_results)
        
        plt.figure(figsize=(12, 6))
        sns.barplot(x='AveragePopularity', y='PreferredGenreStr', data=self.authors_preferences, ci=None)
        plt.title('Average Popularity by Genre')
        plt.xlabel('Average Collect Count')
        plt.ylabel('Genre')
        plt.tight_layout()
        plt.show()

        correlation = np.corrcoef(self.authors_preferences['AverageWords'], self.authors_preferences['AveragePopularity'])[0, 1]
        print("Correlation coefficient between word count and popularity: ", correlation)

        plt.figure(figsize=(10, 6))
        sns.scatterplot(x='AverageWords', y='AveragePopularity', data=self.authors_preferences)
        plt.title('Relationship between Word Count and Popularity')
        plt.xlabel('Word Count')
        plt.ylabel('Collect Count')
        plt.tight_layout()
        plt.show()
# worknum_authors=df.groupby('Name')['Books'].sum()
# wordnum_authors=df.groupby('Name')['TotalWords'].median()
# createday_authors=df.groupby('Name')['TotalDays'].median()
# df1=analyze_authors_genre_and_popularity(df,authors_books)
# df2=analyze_authors_genre_preferences(authors_books)
# visualize_genre_popularity_wordcount_relationship(df1)

anal_author = Analauthor(df,authors_books)
df1=anal_author.analyze_authors_genre_and_popularity()
print(df1)
anal_author.visualize_genre_popularity_wordcount_relationship()
