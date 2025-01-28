import json
import time
from pathlib import Path

from bs4 import BeautifulSoup
from colorama import init

from _dev.markup import to_markup
from _dev.index_html_generator import generate_buttons
from _dev.utils import get_files, update_svg_badge, get_git_diff, dict_walk, update_index_json


update_all = False
init(autoreset=True)
start_time = time.perf_counter()

# get count of all cheat sheets
cheatsheet_list = list(get_files(lambda path: path.endswith(".md")))
cheatsheet_count = len(cheatsheet_list)

print(f"Found \x1b[4m\x1b[1m{cheatsheet_count}\x1b[0m cheat sheet files")
update_svg_badge(cheatsheet_count)


# get list of updated cheat sheets
updated_files = list((get_files if update_all else get_git_diff)(lambda path: path.endswith(".md")))
updated_files_count = len(updated_files)
print(f"Found \x1b[4m\x1b[1m{updated_files_count}\x1b[0m updated files")

for updated_file_md in updated_files:
    updated_file = updated_file_md.removesuffix(".md")
    print(f'  \x1b[32mUpdate "{updated_file}"\x1b[0m')
    with (
        open(f"../cheatsheet/{updated_file}.md", "r", encoding="UTF-8") as markdown_file,
        open(f"../cheatsheet/{updated_file}.html", "w", encoding="UTF-8") as html_file,
    ):
        html_file.write(to_markup(markdown_file.read()))


# clean unused **.html files
html_cheatsheet_list = list(get_files(lambda path: path.endswith(".html")))
white_list_html_files = (
    "index.html",
    "404.html",
    "_buttons.html",
)
unused_files = []
for html_file in html_cheatsheet_list:
    if html_file in white_list_html_files:
        continue
    markdown_cheatsheet = f"{html_file.removesuffix(".html")}.md"
    if markdown_cheatsheet not in cheatsheet_list:
        unused_files.append(html_file)
unused_files_count = len(unused_files)
print(f"Found \x1b[4m\x1b[1m{unused_files_count}\x1b[0m unused files")
for unused_file in unused_files:
    print(f'  \x1b[31mDelete unused file "{unused_file}"\x1b[0m')
    unused_file_path = Path(f"../cheatsheet/{unused_file}")
    unused_file_path.unlink()
    while not any(unused_file_path.parent.iterdir()):
        directory_name = str(
            unused_file_path.parent
        ).replace("\\", "/").removeprefix("../cheatsheet/")
        print(f'    \x1b[31mDelete empty directory "{directory_name}"\x1b[0m')
        unused_file_path.parent.rmdir()
        unused_file_path = unused_file_path.parent


# update index.json
with open("../cheatsheet/index.json", "r", encoding="UTF-8") as index_json_file:
    index_json: dict[str, str | dict[str, str | dict]] = json.load(index_json_file)
index_json_cheatsheet_list = []
for directory, dirnames, filenames in dict_walk(index_json):
    for filename in filenames:
        if filename in (".",):
            continue
        index_json_cheatsheet_list.append(
            f"{directory}/{filename}".lstrip("/")
        )
cheatsheet_set = set(path.removesuffix(".md") for path in cheatsheet_list)
index_json_set = set(path for path in index_json_cheatsheet_list if not path.split("/")[-1].startswith(":"))
added_cheat_sheets = list(cheatsheet_set - index_json_set)
removed_cheat_sheets = list(index_json_set - cheatsheet_set)
modified_files_count = len(added_cheat_sheets) + len(removed_cheat_sheets)
print(f"Found \x1b[4m\x1b[1m{modified_files_count}\x1b[0m modified files")
if added_cheat_sheets:
    print(f"  \x1b[32mAdded cheat sheets {added_cheat_sheets}\x1b[0m")
if removed_cheat_sheets:
    print(f"  \x1b[31mRemoved cheat sheets {removed_cheat_sheets}\x1b[0m")
index_json = update_index_json(index_json, added_cheat_sheets, removed_cheat_sheets)
with open("../cheatsheet/index.json", "w", encoding="UTF-8") as index_json_file:
    json.dump(index_json, index_json_file, indent=4, ensure_ascii=False)


# generate buttons.html file
with open("../cheatsheet/index.json", "r", encoding="UTF-8") as index_json_file:
    index_json = json.load(index_json_file)
buttons_html = generate_buttons(index_json)[0]
with open("../cheatsheet/_buttons.html", "w", encoding="utf-8") as file:
    file.write(BeautifulSoup(buttons_html, "html.parser").prettify())

print(f"Done in \x1b[4m\x1b[1m{time.perf_counter()-start_time:.2f}\x1b[0m sec")
