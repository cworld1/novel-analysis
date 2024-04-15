from flask import send_file
import os
import random
import csv


class FetchBanner:
    def __init__(
        self, path="./data", sub_folder="banner_img", csv_folder="banners.csv"
    ) -> None:
        # Init path
        self.detailed_path = os.path.join(path, sub_folder)
        self.csv_file_path = os.path.join(path, csv_folder)

    def fetch_banner_info(self):
        # Open the CSV file
        with open(self.csv_file_path, newline="", encoding="GBK") as csvfile:
            reader = csv.DictReader(csvfile)
            banners_info = []

            # Read contents and convert to array
            for row in reader:
                banner_info = {
                    "id": row["id"],
                    "link": row["Link"],
                    "description": row["Desc"],
                }
                banners_info.append(banner_info)
        return banners_info

    def fetch_banner(self, image_id):
        image_path = os.path.join(self.detailed_path, f"{image_id}.jpg")
        if not os.path.exists(image_path):
            return "Error: Image not found", 404
        return send_file(image_path, mimetype="image/jpeg")
