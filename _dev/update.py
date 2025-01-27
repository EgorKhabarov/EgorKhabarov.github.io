import json
import time

from bs4 import BeautifulSoup

from _dev.markup import to_markup
from _dev.index_html_generator import generate_buttons
from _dev.utils import get_files, update_svg_badge, get_git_diff


start_time = time.perf_counter()

# get count of all cheat sheets
cheatsheet_list = list(get_files(lambda path: path.endswith(".md")))
cheatsheet_count = len(cheatsheet_list)

print(f"Found {cheatsheet_count} cheat sheet files")
update_svg_badge(cheatsheet_count)


# get list of updated cheat sheets
updated_files = list(get_git_diff(lambda path: path.endswith(".md")))
updated_files_count = len(updated_files)
print(f"Found {updated_files_count} updated files")

for updated_file_md in updated_files:
    updated_file = updated_file_md.removesuffix(".md")
    print(f'  Update "{updated_file}"')
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
print(f"Found {unused_files_count} unused files")
for unused_file in unused_files:
    print(f'    Delete unused file "{unused_file}"')
    ...


# generate buttons.html file
with open("../cheatsheet/index.json", "r", encoding="UTF-8") as index_json_file:
    index_json = json.load(index_json_file)
with open("../cheatsheet/metadata.json", "r", encoding="UTF-8") as metadata_json_file:
    metadata_json = json.load(metadata_json_file)
buttons_html = generate_buttons(index_json, metadata_json)[0]
with open("../cheatsheet/_buttons.html", "w", encoding="utf-8") as file:
    file.write(BeautifulSoup(buttons_html, "html.parser").prettify())

print(f"Done in {time.perf_counter()-start_time:.2f} sec")
