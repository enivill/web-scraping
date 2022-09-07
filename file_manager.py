import json


class FileManager:

    def __init__(self):
        """creates an empty json file '[]'
        if exists deletes it's content
        """
        with open("files/data.json", "w", encoding='utf8') as json_file:
            json.dump(json.loads('[]'), json_file, indent=4)

    def write_file(self, dictionary: dict) -> None:
        """Saves one job offer at a time"""
        with open("files/data.json", "r+", encoding='utf8') as json_file:
            # First we load existing data into a dict.
            file_data: list = json.load(json_file)
            # Join new_data with file_data
            file_data.append(dictionary)
            # Sets file's current position at offset.
            json_file.seek(0)
            # convert back to json.
            json.dump(file_data, json_file, indent=4, ensure_ascii=False)
