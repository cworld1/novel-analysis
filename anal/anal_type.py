import csv, platform
import matplotlib
import matplotlib.pyplot as plt


class AnalType:
    file = "books.csv"
    color = "skyblue"
    colors = "GnBu"

    def __init__(self, path="./data", interaction=True) -> None:
        self.path = path
        if not interaction:
            matplotlib.use("Agg")

        # Set font for different systems (to support Chinese)
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

    def draw_bar(self, type_counts: dict, type_popularity: dict, context, callback):
        # Calculate mean popularity
        for key in type_popularity:
            type_popularity[key] /= type_counts[key]
        type_popularity = dict(
            sorted(type_popularity.items(), key=lambda x: x[1], reverse=True)
        )
        # for key, value in type_popularity:
        #     print(key, value)

        # Create bar plot
        plt.figure(figsize=(10, 6))
        plt.bar(
            list(type_popularity.keys()),
            list(type_popularity.values()),
            color=self.color,
        )
        plt.title(context["title"])
        plt.xlabel(context["xlabel"])
        plt.ylabel(context["ylabel"])
        plt.xticks(rotation=45)
        plt.tight_layout()

        # Do with the plot
        callback()
        plt.close()

    def draw_pie(self, type_counts: dict, context, callback):
        # Data to plot
        labels = []
        sizes = []
        other_size = 0  # Size for 'Other' category
        total = sum(type_counts.values())

        # Move lower data to 'Other' category
        for key, count in type_counts.items():
            if (count / total) * 100 >= 3:
                labels.append(key)
                sizes.append(count)
            else:
                other_size += count
        if other_size > 0:
            labels.append("其他")
            sizes.append(other_size)

        # Highlight the biggest slice
        explode = [
            0.1 if i == max(sizes) else 0 for i in sizes
        ]  # Only explode the largest slice

        # Plot
        colormap = matplotlib.colormaps[self.colors].resampled(len(sizes))
        plt.figure(figsize=(8, 8))
        plt.pie(
            sizes,
            explode=explode,
            labels=labels,
            colors=colormap(range(len(sizes))),
            autopct=lambda p: "{:.1f}%".format(p) if p >= 3 else "",
            shadow=True,
            startangle=140,
        )
        plt.axis("equal")  # equal aspect ratio ensures that pie is drawn as a circle.
        plt.title(context["title"])
        plt.tight_layout()

        # Do with the plot
        callback()
        plt.close()

    def anal(self, shape="bar", callback=lambda: plt.show()):
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

        if shape == "bar":
            # Draw bar plot
            context = {
                "title": "Mean Popularity by Type",
                "xlabel": "Type",
                "ylabel": "Mean Popularity",
            }
            self.draw_bar(type_counts, type_popularity, context, callback)

        elif shape == "pie":
            # Draw pie plot
            context = {"title": "Composition of Novel Types"}
            self.draw_pie(type_counts, context, callback)


# Test
# anal_type = AnalType()
# anal_type.anal(shape="pie", callback=lambda: plt.show())
