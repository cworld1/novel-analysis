import os
import random
from fetch.fetch_helper import get_content


class FetchNovel:
    def __init__(self, path="./data", sub_folder="book_info") -> None:
        # Init path
        self.detailed_path = f"{path}/{sub_folder}"
        self.comment_path = "./data/output_comment_anal"

    def fetch(self, choose: str, count: int = 1):
        result_count = 0  # 记录已获取的结果数量
        result = []  # 存储结果的列表

        while result_count < count:
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
                # Randomly choose count number of books or remaining books
                remaining_count = count - result_count
                selected_books = random.sample(total_books, remaining_count)
            # Choose the book by the id
            elif choose is not None:
                selected_books = [f"{choose}.json"]
            else:
                print("No book id provided!")
                return []

            for book in selected_books:
                full_content = get_content(os.path.join(self.detailed_path, book))[
                    "bookInfo"
                ]
                selected_content = {
                    "bookId": full_content["bookId"],
                    "bookName": full_content["bookName"],
                    "authorName": full_content["authorName"],
                    "comments": []  # 存储评论内容的列表
                }
                
                # 根据书籍 ID 构建评论文件名
                comment_filename = f"{selected_content['bookId']}.txt"
                comment_file_path = os.path.join(self.comment_path, comment_filename)
                
                # 如果评论文件存在，则读取评论内容并添加到结果中
                if os.path.isfile(comment_file_path):
                    with open(comment_file_path, 'r', encoding='utf-8') as file:
                        comments = file.read().splitlines()
                        selected_content["comments"] = comments
                    result.append(selected_content)
                    result_count += 1  # 更新已获取的结果数量

                    # 如果已获取的结果数量等于 count，则直接返回结果
                    if result_count == count:
                        return result

        return result  # 返回结果列表，即使未达到 count 也返回

# Test
# fetch_novel = FetchNovel(sub_folder="author_book_info")
# info = fetch_novel.fetch(choose="random")
# print(info)
