from time import time

from _dev.json_maker import make_clear_json

start_time = time()  # noqa

import os  # noqa

from _dev.data import DICT  # noqa
from _dev.html_generator import generate_index_html  # noqa
from _dev.file_creator import create_files  # noqa
from _dev.utils import print_progress_bar, check_dict_keys  # noqa


ADDITIONAL_PATH = ""

cheatsheet_count = check_dict_keys(DICT)
assert cheatsheet_count is not False
print()

folder_path = "../cheatsheet"
x = 0
print_progress_bar(0, cheatsheet_count, "delete cheatsheet", "")


def g(path_: str):
    r = DICT
    for k in path_.removeprefix("../cheatsheet").strip("/").strip("\\").removesuffix(".md").split("\\"):
        r = r[k]
    return r


for foldername, _, filenames in os.walk(folder_path):
    for filename in filenames:
        if filename.endswith(".md"):
            path = os.path.join(foldername, filename)
            try:
                g(path)
            except KeyError:
                x += 1
                print_progress_bar(x, cheatsheet_count, "delete cheatsheet", path)
                os.remove(path)

print()
create_files(cheatsheet_count, ADDITIONAL_PATH)
print()
metadata = make_clear_json()
generate_index_html(cheatsheet_count, metadata)
print(f"\n{cheatsheet_count} cheatsheets in {time()-start_time:.2f} sec")
