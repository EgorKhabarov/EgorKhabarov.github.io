from time import time

from _dev.json_maker import make_clear_json

start_time = time()  # noqa

import os  # noqa

from _dev.data import DICT  # noqa
from _dev.html_generator import generate_index_html  # noqa
from _dev.file_creator import create_files  # noqa
from _dev.utils import print_progress_bar, check_dict_keys  # noqa


ADDITIONAL_PATH = """

""".strip().strip("/").replace("\n", "/")+"/"

assert ADDITIONAL_PATH == "" or ADDITIONAL_PATH.endswith("/")
ADDITIONAL_PATH = ADDITIONAL_PATH.removesuffix("/")

if ADDITIONAL_PATH:
    print(f"\x1b[1m\x1b[31mCheatsheets are updated only in this directory: \x1b[32m\"{ADDITIONAL_PATH}\"\x1b[0m")

cheatsheet_count, error = check_dict_keys(DICT)
if error and not error[-1]:
    error[-1] = "<empty name>"
assert cheatsheet_count is not False, f"\"{'/'.join(error)}\""
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
        # if filename.endswith((".md", ".html")) and filename != "index.html":
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
print(f"\n\x1b[31m\x1b[1m{cheatsheet_count}\x1b[0m cheatsheets in \x1b[31m\x1b[1m{time()-start_time:.2f}\x1b[0m sec")
