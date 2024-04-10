# import platform


# Function to convert '万' to number
def convert_wan(count) -> int:
    if "万" in count:
        return int(float(count.replace("万", "")) * 10000)
    return int(count)


# def set_font():
#     # Set font for different systems (to support Chinese)
#     if platform.system() == "Darwin":
#         # macOS
#         plt.rcParams["font.family"] = "Arial Unicode MS"
#     elif platform.system() == "Windows":
#         # Windows
#         plt.rcParams["font.family"] = "SimHei"
#     else:
#         # Other system
#         plt.rcParams["font.family"] = "Arial"
