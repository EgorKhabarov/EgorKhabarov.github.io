from time import time

start_time = time()  # noqa

import os  # noqa

from dev.data import DICT  # noqa
from dev.html_generator import generate_index_html  # noqa
from dev.file_creator import create_files  # noqa
from dev.utils import print_progress_bar, check_dict_keys  # noqa


cheatsheet_count = check_dict_keys(DICT)
assert cheatsheet_count is not False
print()

folder_path = "../cheatsheet"
x = 0
print_progress_bar(0, cheatsheet_count, "delete old cheatsheet", "")


def g(path: str):
    r = DICT
    for k in path.removeprefix("../cheatsheet").strip("/").strip("\\").removesuffix(".md").split("\\"):
        r = r[k]
    return r


for foldername, _, filenames in os.walk(folder_path):
    for filename in filenames:
        if filename.endswith(".md"):
            x += 1
            path = os.path.join(foldername, filename)
            try:
                g(path)
            except KeyError:
                print_progress_bar(x, cheatsheet_count, "delete old cheatsheet", path)
                os.remove(path)

print()
generate_index_html(cheatsheet_count)
print()
create_files(cheatsheet_count)
print(f"\n{cheatsheet_count} cheatsheets in {time()-start_time:.2f} sec")
