import os

from bs4 import BeautifulSoup

from dev.data import DICT
from dev.utils import print_progress_bar


id_dict = []


def buttons(
    dictionary: dict,
    directory: str = "",
    x: int = 0,
    y: int = 0,
) -> tuple[str, str, int]:
    text_list = []
    for key, value in dictionary.items():
        if key.startswith("link:"):
            key = key.removeprefix("link:")
            name = key.replace("\\", "&#x2f;") + ".md"
            text_list.append(
                (
                    '<button onclick="GET(\'{name}\');restoreCheatSheetState(\'{name2}\')" class="button" '
                    'vpath="{vpath}">{title}</button>\n'
                ).format(
                    name=name,
                    vpath=f"{key}.md".strip("/"),
                    title="🔗&nbsp;" + key.replace(" ", "&nbsp;"),
                    name2=name.removesuffix(".md") + "index.md" if name.endswith("/.md") else name,
                )
            )
            continue

        print_progress_bar(x, y, "create index.html", f"{directory}\\{key}")

        if key == "index":
            x += 1
            continue

        # print(f"{directory}\\{key}")

        key_path = os.path.join(directory, key)
        directory_e = directory.replace("\\", "/").strip("/")

        if isinstance(value, dict) and "index" in value:
            val, _, x = buttons(value, key_path, x, y)
            kpath = f"{directory_e}/{key}".strip("/")
            text_list.append(
                (
                    '<button class="button" onclick="toggleDisplay(this.nextElementSibling);GET(\'{csname}\');" '
                    'kpath="{kpath}" vpath="{vpath}">{title}</button>'
                    '<div class="button-folder" style="display:none;">{text}</div>'
                ).format(
                    kpath=f"{kpath}/",
                    title="📂&nbsp;" + key.replace(" ", "&nbsp;"),
                    text=val,
                    vpath=f"{directory_e}/{key}/",
                    csname=key_path.replace("\\", "&#x2f;") + "/index.md",
                )
            )
        elif isinstance(value, dict):
            val, _, x = buttons(value, key_path, x, y)
            kpath = f"{directory_e}/{key}".strip("/")
            text_list.append(
                (
                    '<button class="button" onclick="toggleDisplay(this.nextElementSibling);" '
                    'kpath="{kpath}">{title}</button>'
                    '<div class="button-folder" style="display:none;">{text}</div>'
                ).format(
                    kpath=kpath,
                    title="📂&nbsp;" + key.replace(" ", "&nbsp;"),
                    text=val,
                )
            )
        else:
            x += 1
            text_list.append(
                (
                    '<button onclick="GET(\'{name}\');" class="button" '
                    'vpath="{vpath}">{title}</button>\n'
                ).format(
                    name=key_path.replace("\\", "&#x2f;") + ".md",
                    vpath=f"{directory_e}/{key}.md".strip("/"),
                    title="📄&nbsp;" + key.replace(" ", "&nbsp;"),
                )
            )
    return "".join(text_list), directory, x


def generate_index_html(cheatsheet_count: int):
    result = f"""
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <link rel="icon" type="image/png" href="icon.png">
        <title>Шпаргалка</title>
        <link rel="stylesheet" href="./styles.css">
        <script src="./script.js"></script>
    </head>
    <body>
        <div class="cheatsheet-buttons">
            {buttons(DICT, y=cheatsheet_count - 1)[0]}
        </div>
        <pre id="field" class="cheatsheet-field">
            Нажмите на кнопку с темой, чтобы увидеть здесь объяснение
        </pre>
        <div>
            <button id="FontSizeSize"
                    class="control-button"
                    onclick="changeFontSize(field, '=')"
                    style="padding-left: 12px;">12px</button>
            <button onclick="changeFontSize(field, '+')"
                    class="control-button"
                    style="padding-left: 25px;">+</button>
            <button onclick="changeFontSize(field, '-')"
                    class="control-button"
                    style="padding-left: 27px;">-</button>
            <button id="COPY"
                    onclick="copyTextFromDiv(field);
                    changeColor(COPY)"
                    class="control-button"
                    style="padding-left: 12px;">Copy</button>
            <button id="COPY2"
                    onclick="copyTextFromDiv2();
                    changeColor(COPY2)"
                    class="control-button"
                    style="padding-left: 2px;">Copy selected</button>
            <button id="removeargfromurl"
                    onclick="removeArgumentFromUrl();window.location.reload();changeColor(removeargfromurl)"
                    class="control-button"
                    style="padding-left: 28px;">/</button>
        </div>
    </body>
</html>
"""
    with open("../cheatsheet/index.html", "w", encoding="utf-8") as file:
        file.write(BeautifulSoup(result, "html.parser").prettify())
