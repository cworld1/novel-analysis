import os
import random
from fetch.fetch_helper import get_content


class FetchNovel:
    def __init__(self, path="./data", sub_folder="book_info") -> None:
        # Init path
        self.detailed_path = f"{path}/{sub_folder}"

    def fetch(self, choose: str, count: int = 1):
        while True:
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

            books_infos = []
            output_comment_anal_filenames = [
                filename.split(".")[0]  # 去除 .txt 后缀
                for filename in os.listdir("./data/output_comment_anal")
            ]

            for book in books:
                full_content = get_content(os.path.join(self.detailed_path, book))[
                    "bookInfo"
                ]
                selected_content = {
                    "bookId": full_content["bookId"],
                    "bookName": full_content["bookName"],
                    "authorName": full_content["authorName"],
                }
                # 如果书籍 ID 在 output_comment_anal 文件名中，则添加到 books_infos 中
                if selected_content['bookId'] in output_comment_anal_filenames:
                    books_infos.append(selected_content)
                    return books_infos  # 如果符合条件，则直接返回


# Test
# fetch_novel = FetchNovel(sub_folder="author_book_info")
# info = fetch_novel.fetch(choose="random")
# print(info)
