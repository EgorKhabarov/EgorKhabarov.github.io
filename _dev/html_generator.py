import os

from bs4 import BeautifulSoup

from _dev.data import DICT
from _dev.utils import print_progress_bar


id_dict = []


def buttons(
    dictionary: dict,
    directory: str = "",
    x: int = 0,
    y: int = 0,
) -> tuple[str, str, int]:
    text_list = []
    for key, value in dictionary.items():
        print_progress_bar(x, y, "create index.html", f"{directory}\\{key}")
        title = key.replace(" ", "&nbsp;").replace("-", "&#8288;-&#8288;")

        if key.startswith("::link::"):
            key = key.removeprefix("::link::")
            name = key.replace("\\", "&#x2f;") + ".md"
            text_list.append(
                (
                    '<button onclick="GET(\'{name}\');restoreCheatSheetState(\'{name2}\')" class="button" '
                    'vpath="{vpath}" title="{title}">{title}</button>\n'
                ).format(
                    name=name,
                    vpath=f"{key}.md".strip("/"),
                    title=f"🔗&nbsp;{title.removeprefix('::link::')}",
                    name2=name.removesuffix(".md") + "index.md" if name.endswith("/.md") else name,
                )
            )
            continue

        if key == "index":
            x += 1
            continue

        # print(f"{directory}\\{key}")

        key_path = os.path.join(directory, key)
        directory_e = directory.replace("\\", "/").strip("/")

        if isinstance(value, dict) and "index" in value:
            val, _, x = buttons(value, key_path, x, y)
            text_list.append(
                (
                    '<button class="button" onclick="toggleDisplay(this.nextElementSibling);GET(\'{csname}\');" '
                    'kpath="{kpath}" vpath="{vpath}" title="{title}">{title}</button>'
                    '<div class="button-folder" style="display:none;">{text}</div>'
                ).format(
                    kpath=f"{directory_e}/{key}".strip("/") + "/",
                    title=f"📂&nbsp;{title}",
                    text=val,
                    vpath=f"{directory_e}/{key}/",
                    csname=key_path.replace("\\", "&#x2f;") + "/index.md",
                )
            )
        elif isinstance(value, dict):
            val, _, x = buttons(value, key_path, x, y)
            text_list.append(
                (
                    '<button class="button" onclick="toggleDisplay(this.nextElementSibling);" '
                    'kpath="{kpath}" title="{title}">{title}</button>'
                    '<div class="button-folder" style="display:none;">{text}</div>'
                ).format(
                    kpath=f"{directory_e}/{key}".strip("/"),
                    title=f"📂&nbsp;{title}",
                    text=val,
                )
            )
        else:
            x += 1
            text_list.append(
                (
                    '<button onclick="GET(\'{name}\');" class="button" '
                    'vpath="{vpath}" title="{title}">{title}</button>\n'
                ).format(
                    name=key_path.replace("\\", "&#x2f;") + ".md",
                    vpath=f"{directory_e}/{key}.md".strip("/"),
                    title=f"📄&nbsp;{title}",
                )
            )
    return "".join(text_list), directory, x


def generate_index_html(cheatsheet_count: int):
    result = f"""
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Шпаргалка</title>
        <link rel="icon" type="image/png" href="icon.png">
        <link rel="stylesheet" href="./styles.css">
        <script src="./script.js"></script>
    </head>
    <body>
        <div id="cheatsheet-buttons" class="cheatsheet-buttons">
            <div class="search-container">
                <input id="search" type="text" class="search-input" placeholder="🔎 Поиск">
            </div>
            <div id="search-button-folder" class="button-folder" style="display:none;">
            
            </div>
            {buttons(DICT, y=cheatsheet_count - 1)[0]}
        </div>
        <pre id="field" class="cheatsheet-field">Нажмите на кнопку с темой, чтобы увидеть здесь объяснение</pre>
        <div>
            <button id="FontSizeSize"     class="control-button" style="padding-left: 12px;" onclick="changeFontSize(field, '=')">12px</button>
            <button                       class="control-button" style="padding-left: 25px;" onclick="changeFontSize(field, '+')">+</button>
            <button                       class="control-button" style="padding-left: 27px;" onclick="changeFontSize(field, '-')">-</button>
            <button id="COPY"             class="control-button" style="padding-left: 12px;" onclick="copyTextFromDiv(field);changeColor(COPY)">Copy</button>
            <button id="COPY2"            class="control-button" style="padding-left: 2px;"  onclick="copyTextFromDiv2();changeColor(COPY2)">Copy selected</button>
            <button id="removeargfromurl" class="control-button" style="padding-left: 28px;" onclick="removeArgumentFromUrl();window.location.reload();changeColor(removeargfromurl)">/</button>
        </div>
    </body>
</html>
"""
    with open("../cheatsheet/index.html", "w", encoding="utf-8") as file:
        file.write(BeautifulSoup(result, "html.parser").prettify())
