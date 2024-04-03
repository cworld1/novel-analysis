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

    def draw_bar(self, type_counts: dict, type_popularity: dict, context: dict):

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
            color="skyblue",
        )
        plt.title(context["title"])
        plt.xlabel(context["xlabel"])
        plt.ylabel(context["ylabel"])
        plt.xticks(rotation=45)
        plt.tight_layout()

        # Show plot
        plt.show()
    def draw_pie(self, type_counts: dict, custom_colors: list):
        # Data to plot
        labels = []
        sizes = []
        other_size = 0  # Size for 'Other' category
        total = sum(type_counts.values())

        for key, count in type_counts.items():
            if (count / total) * 100 >= 3:
                labels.append(key)
                sizes.append(count)
            else:
                other_size += count

        # If there is 'Other' data, add it
        if other_size > 0:
            labels.append('其他')
            sizes.append(other_size)

        # Prepare custom colors for the plot
        if len(custom_colors) >= len(labels):
            colors = custom_colors[:len(labels)]
        else:
            colors = custom_colors + ['grey'] * (len(labels) - len(custom_colors))  # Fill up with grey if not enough colors
        
        explode = [0.1 if i == max(sizes) else 0 for i in sizes]  # Only explode the largest slice
        
        # Plot
        plt.figure(figsize=(8, 8))
        plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct=lambda p: '{:.1f}%'.format(p) if p >= 3 else '',
                shadow=True, startangle=140)
        plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        plt.title('Composition of Novel Types')
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

        # Draw the plot
        context = {
            "title": "Mean Popularity by Type",
            "xlabel": "Type",
            "ylabel": "Mean Popularity",
        }
        self.draw_bar(type_counts, type_popularity, context)
# Define the custom colors
        custom_colors = ["#FFE45E", "#78AA8D", "#8F7C7B", "#8C845A", "#FF6A5E", "#5EFFA2", "#655EFF"]

        # Draw the pie chart with custom colors
        self.draw_pie(type_counts, custom_colors)
    


# Test
anal_type = AnalType()
anal_type.anal()
