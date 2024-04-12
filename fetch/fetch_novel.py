import os
import random

from fetch.fetch_helper import get_content


class FetchNovel:
    def __init__(self, path="./data", sub_folder="book_info") -> None:
        # Init path
        self.detailed_path = f"{path}/{sub_folder}"

    def fetch(self, choose: str, count: int = 1):
        # Randomly choose one book
        if choose == "random":
            total_books = [
                f
                for f in os.listdir(self.detailed_path)
                if os.path.isfile(os.path.join(self.detailed_path, f))
            ]
            if not total_books:
                print("No books found!")
                return None
            # Randomly choose count number of books
            books = random.sample(total_books, count)
        # Choose the book by the id
        elif choose is not None:
            books = [f"{choose}.json"]
        else:
            print("No book id provided!")
            return []

        books_infos = [
            get_content(os.path.join(self.detailed_path, book))["bookInfo"]
            for book in books
        ]
        # Only get each book's first info
        return books_infos


# Test
# fetch_novel = FetchNovel(sub_folder="author_book_info")
# info = fetch_novel.fetch(choose="random")
# print(info)
