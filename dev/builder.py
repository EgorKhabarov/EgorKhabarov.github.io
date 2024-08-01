from time import time

start_time = time()  # noqa

import os  # noqa

from dev.html_generator import generate_index_html  # noqa
from dev.file_creator import create_files, cheatsheet_count  # noqa
from dev.utils import print_progress_bar  # noqa


folder_path = "../cheatsheet"
x = 0

for foldername, _, filenames in os.walk(folder_path):
    for filename in filenames:
        if filename.endswith(".md"):
            x += 1
            path = os.path.join(foldername, filename)
            print_progress_bar(x, cheatsheet_count, "delete old cheatsheet", path)
            os.remove(path)

print()
generate_index_html()
print()
create_files()
print(f"\nГенерация шпаргалки заняла: {time()-start_time:.2f} sec")
