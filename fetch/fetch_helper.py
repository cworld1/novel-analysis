import json


def get_content(file_path):
    with open(file_path, "r", encoding="utf-8") as json_file:
        file_content = json_file.read()
    return json.loads(file_content)

