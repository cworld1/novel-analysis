import csv, platform
import matplotlib.pyplot as plt


class AnalType:
    file = "books.csv"

    def __init__(self, path="./data") -> None:
        self.path = path
        if platform.system() == "Darwin":
            # macOS
            plt.rcParams["font.family"] = "Arial Unicode MS"
        elif platform.system() == "Windows":
            # Windows
            plt.rcParams["font.family"] = "SimHei"
        else:
            # Other system
            plt.rcParams["font.family"] = "Arial"

    # Function to convert '万' to number
    def convert_wan(self, popularity) -> int:
        if "万" in popularity:
            return int(float(popularity.replace("万", "")) * 10000)
        return int(popularity)

    def anal_draw(self, data: dict, context: dict):
        # Create bar plot
        plt.figure(figsize=(10, 6))
        plt.bar(
            list(data.keys()),
            list(data.values()),
            color="skyblue",
        )
        plt.title(context["title"])
        plt.xlabel(context["xlabel"])
        plt.ylabel(context["ylabel"])
        plt.xticks(rotation=45)
        plt.tight_layout()

        # Show plot
        plt.show()

    def anal(self):
        type_popularity = {}
        type_counts = {}

        # Read data from CSV file
        # data = []
        with open(f"{self.path}/{self.file}", "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                pop = self.convert_wan(row["Popularity"])
                # row["Popularity"] = pop
                # data.append(row)

                # Calculate total popularity and count for each type
                if row["Type"] not in type_popularity:
                    type_popularity[row["Type"]] = pop
                    type_counts[row["Type"]] = 1
                else:
                    type_popularity[row["Type"]] += pop
                    type_counts[row["Type"]] += 1

        # print(type_counts)
        # Calculate mean popularity
        for key in type_popularity:
            type_popularity[key] /= type_counts[key]
        # 对 type_popularity 进行排序
        type_popularity = dict(
            sorted(type_popularity.items(), key=lambda x: x[1], reverse=True)
        )
        # for key, value in type_popularity:
        #     print(key, value)

        # Draw the plot
        context = {
            "title": "Mean Popularity by Type",
            "xlabel": "Type",
            "ylabel": "Mean Popularity",
        }
        self.anal_draw(type_popularity, context)


# Test
anal_type = AnalType()
anal_type.anal()
