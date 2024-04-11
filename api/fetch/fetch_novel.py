import os
import random

from fetch.fetch_helper import get_content


class FetchNovel:
    def __init__(self, path="./data", sub_folder="book_info") -> None:
        # Init path
        self.detailed_path = f"{path}/{sub_folder}"

    def fetch(self, choose: str):
        # Randomly choose one book
        if choose == "random":
            books = [
                f
                for f in os.listdir(self.detailed_path)
                if os.path.isfile(os.path.join(self.detailed_path, f))
            ]
            if not books:
                print("No books found!")
                return None
            choose = random.choice(books)
        # Choose the book by the id
        elif choose is None:
            print("No book id provided!")
            return None

        novel = get_content(os.path.join(self.detailed_path, f"{choose}.json"))
        return novel["bookInfo"]


# Test
fetch_novel = FetchNovel()
info = fetch_novel.fetch(choose="random")
print(info)
