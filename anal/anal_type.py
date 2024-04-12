import csv

# Plot
from pyecharts import options as opts
from pyecharts.charts import Bar, Pie

from anal.anal_helper import convert_wan


class AnalType:

    def __init__(self, path="./data", file="books.csv") -> None:
        self.path = path
        self.file = file

    def anal(self, shape="bar"):
        type_popularity = {}
        type_counts = {}

        # Read data from CSV file
        # data = []
        with open(f"{self.path}/{self.file}", "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                pop = convert_wan(row["Popularity"])
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
            draw = self.draw_bar(type_counts, type_popularity, context)
        elif shape == "pie":
            # Draw pie plot
            context = {"title": "Composition of Novel Types"}
            draw = self.draw_pie(type_counts, context)
        else:
            return None

        return draw

    def draw_bar(self, type_counts: dict, type_popularity: dict, context):
        # Calculate mean popularity
        for key in type_popularity:
            type_popularity[key] /= type_counts[key]
        type_popularity = dict(
            sorted(type_popularity.items(), key=lambda x: x[1], reverse=True)
        )
        # for key, value in type_popularity:
        #     print(key, value)

        # Create bar plot
        bar = (
            Bar()
            .add_xaxis(list(type_popularity.keys()))
            .add_yaxis(context["ylabel"], list(type_popularity.values()))
            .set_global_opts(
                title_opts=opts.TitleOpts(title=context["title"]),
                xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=45)),
                datazoom_opts=opts.DataZoomOpts(),
            )
        )
        return bar

    def draw_pie(self, type_counts: dict, context):
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
        # explode = [
        #     0.1 if i == max(sizes) else 0 for i in sizes
        # ]  # Only explode the largest slice

        # Plot
        pie = (
            Pie()
            .add(
                "",
                [list(z) for z in zip(labels, sizes)],
                radius=["40%", "75%"],
            )
            .set_global_opts(
                title_opts=opts.TitleOpts(title=context["title"]),
                legend_opts=opts.LegendOpts(
                    orient="vertical", pos_top="15%", pos_left="2%"
                ),
            )
        )

        return pie


# Test
# anal_type = AnalType()
# anal_type.anal(shape="bar").render()
