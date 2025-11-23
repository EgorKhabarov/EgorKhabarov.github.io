import json
import time
from pathlib import Path

from bs4 import BeautifulSoup
from colorama import init

from _dev.markup import to_markup
from _dev.index_html_generator import generate_buttons
from _dev.utils import (
    repo,
    get_files,
    dict_walk,
    get_git_diff,
    update_svg_badge,
    update_index_json,
    update_updated_json,
    get_git_diff_moved_from_cheat_sheet_dict,
)


update_all = False
dir_name = "cheatsheet"

RESET = "\x1b[0m"
BOLD = "\x1b[1m"
UNDERLINE = "\x1b[4m"
RED = "\x1b[31m"
GREEN = "\x1b[32m"
YELLOW = "\x1b[33m"

init(autoreset=True)
start_time = time.perf_counter()

# get count of all cheat sheets
cheatsheet_list = list(get_files(dir_name, lambda path: path.endswith(".md")))
"""All .md files"""
cheatsheet_count = len(cheatsheet_list)

print(f"Found {UNDERLINE}{BOLD}{cheatsheet_count}{RESET} cheat sheet files")
update_svg_badge(cheatsheet_count)


# get a list of updated cheat sheets
updated_files = cheatsheet_list if update_all \
    else list(get_git_diff(dir_name, lambda path: path.endswith(".md")))
"""Updated .md files"""
updated_files_count = len(updated_files)
print(f"Found {UNDERLINE}{BOLD}{updated_files_count}{RESET} updated files")
update_updated_json(list(map(lambda s: s.removesuffix(".md"), updated_files)))

for updated_file_md in updated_files:
    updated_file = updated_file_md.removesuffix(".md")
    print(f'  {GREEN}Update "{updated_file}"{RESET}')
    cheatsheet_path = f"../cheatsheet/{updated_file}"
    with (
        open(f"{cheatsheet_path}.md", "r", encoding="UTF-8") as markdown_file,
        open(f"{cheatsheet_path}.html", "w", encoding="UTF-8") as html_file,
    ):
        html_file.write(to_markup(markdown_file.read()))


# clean unused **.html files
white_list_html_files = (
    "index.html",
    "index-old.html",
    "index-new.html",
    "cheatsheet_resources/404.html",
    "cheatsheet_resources/buttons.html",
)
unused_files: list[str] = []
incorrect_name_files: list[tuple[str, str, str]] = []
lower_cheatsheet_list: list[str] = [path.lower() for path in cheatsheet_list]
for html_file in get_files(dir_name, lambda path: path.endswith(".html")):
    if html_file in white_list_html_files:
        continue
    markdown_cheatsheet = f"{html_file.removesuffix(".html")}.md"
    # if file names are case-sensitive
    if (
        markdown_cheatsheet not in cheatsheet_list
        and markdown_cheatsheet.lower() in lower_cheatsheet_list
    ):
        index = lower_cheatsheet_list.index(markdown_cheatsheet.lower())
        markdown_cheatsheet = Path(markdown_cheatsheet)
        dirpath = str(markdown_cheatsheet.parent).replace("\\", "/")
        incorrect_filename = f"{markdown_cheatsheet.name.removesuffix(".md")}.html"
        filename = f"{Path(cheatsheet_list[index]).name.removesuffix(".md")}.html"
        incorrect_name_files.append((dirpath, incorrect_filename, filename))
        continue
    if markdown_cheatsheet not in cheatsheet_list:
        unused_files.append(html_file)
unused_files_count = len(unused_files)
print(f"Found {UNDERLINE}{BOLD}{unused_files_count}{RESET} unused files")
for unused_file in unused_files:
    print(f'  {RED}Delete unused file "{unused_file}"{RESET}')
    unused_file_path = Path(f"../cheatsheet/{unused_file}")
    unused_file_path.unlink()
    while not any(unused_file_path.parent.iterdir()):
        directory_name = (
            str(unused_file_path.parent)
            .replace("\\", "/")
            .removeprefix("../cheatsheet/")
        )
        print(f'    {RED}Delete empty directory "{directory_name}"{RESET}')
        unused_file_path.parent.rmdir()
        unused_file_path = unused_file_path.parent
incorrect_name_files_count = len(incorrect_name_files)
print(f"Found {UNDERLINE}{BOLD}{incorrect_name_files_count}{RESET} files with incorrect name")
for dirpath, incorrect_filename, filename in incorrect_name_files:
    print(f'  {YELLOW}Rename {GREEN}"{dirpath}/{incorrect_filename}" {YELLOW}to {GREEN}"{filename}"{RESET}')
    from_path = f"cheatsheet/{dirpath}/{incorrect_filename}"
    to_path = f"cheatsheet/{dirpath}/{filename}"
    repo.git.mv(from_path, to_path)


# update index.json
with open("../cheatsheet/index.json", "r", encoding="UTF-8") as index_json_file:
    index_json: dict[str, str | dict[str, str | dict]] = json.load(index_json_file)
index_json_cheatsheet_list = []
for directory, dirnames, filenames in dict_walk(index_json):
    for filename in filenames:
        if filename in (".",):
            continue
        index_json_cheatsheet_list.append(f"{directory}/{filename}".lstrip("/"))
cheatsheet_set = set(path.removesuffix(".md") for path in cheatsheet_list)
index_json_set = set(
    path
    for path in index_json_cheatsheet_list
    if not path.split("/")[-1].startswith(":")  # links
)
added_cheat_sheets = list(cheatsheet_set - index_json_set)
removed_cheat_sheets = list(index_json_set - cheatsheet_set)
modified_files_count = len(added_cheat_sheets) + len(removed_cheat_sheets)
print(f"Found {UNDERLINE}{BOLD}{modified_files_count}{RESET} differences with index.json")
for added_cheat_sheet in added_cheat_sheets:
    print(f"  {GREEN}Added cheat sheet {added_cheat_sheet}{RESET}")
for removed_cheat_sheet in removed_cheat_sheets:
    print(f"  {RED}Removed cheat sheet {removed_cheat_sheet}{RESET}")
moved_cheat_sheets = get_git_diff_moved_from_cheat_sheet_dict(
    lambda path: path.endswith(".md")
)
index_json = update_index_json(
    index_json, added_cheat_sheets, removed_cheat_sheets, moved_cheat_sheets
)
with open("../cheatsheet/index.json", "w", encoding="UTF-8") as index_json_file:
    json.dump(index_json, index_json_file, indent=4, ensure_ascii=False)


# generate cheatsheet_resources/buttons.html file
buttons_html = generate_buttons(index_json)[0]
with open("../cheatsheet/cheatsheet_resources/buttons.html", "w", encoding="utf-8") as file:
    file.write(BeautifulSoup(buttons_html, "html.parser").prettify())

print(f"Done in {UNDERLINE}{BOLD}{time.perf_counter()-start_time:.2f}{RESET} sec")
