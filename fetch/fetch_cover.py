import os
import random
import base64


class FetchCover:
    def __init__(self, path="./data", sub_folder="covers") -> None:
        # Init path
        self.detailed_path = f"{path}/{sub_folder}"

    def fetch(self, count: int = 3):
        # Get all image files in the folder
        image_files = [
            f
            for f in os.listdir(self.detailed_path)
            if os.path.isfile(os.path.join(self.detailed_path, f))
        ]
        for img_file in image_files:
            print(os.path.join(self.detailed_path, img_file))

        # Randomly select 'count' number of images
        selected_images = random.sample(image_files, min(count, len(image_files)))

        # Load image content and encode with Base64
        images_base64 = []
        for img_file in selected_images:
            img_path = os.path.join(self.detailed_path, img_file)
            with open(img_path, "rb") as f:
                image_bytes = f.read()
                image_base64 = base64.b64encode(image_bytes).decode("utf-8")
                images_base64.append(image_base64)

        return images_base64
