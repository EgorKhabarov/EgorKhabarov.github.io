import os

folder_path = "../cheatsheet"

for foldername, _, filenames in os.walk(folder_path):
    for filename in filenames:
        if filename.endswith(".md"):
            os.remove(os.path.join(foldername, filename))
            # print(f"Файл удален: {os.path.join(foldername, filename)}")

import html_generator
import file_creator
