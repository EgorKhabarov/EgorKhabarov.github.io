import os
import hashlib

from bs4 import BeautifulSoup

from dev.data import DICT
from dev.utils import r, print_progress_bar


cheatsheet_count = r(DICT)
id_dict = []


def get_id(data: str, noprint: bool = False):
    h = hashlib.md5(data.encode()).hexdigest()
    attempt = 0

    while h in id_dict:
        attempt += 1
        data = f"{data}{attempt}"
        h = hashlib.md5(data.encode()).hexdigest()

    id_dict.append(h)

    if attempt != 0 and not noprint:
        print(attempt)

    return h


def buttons(
    dictionary: dict,
    directory: str = "",
    x: int = 0,
    y: int = cheatsheet_count - 1,
) -> tuple[str, str, int]:
    text_list = []
    for key, value in dictionary.items():
        print_progress_bar(x, y, "generate index.html", f"{directory}\\{key}")

        if key == "index":
            x += 1
            continue

        # print(f"{directory}\\{key}")

        title = key
        key_path = os.path.join(directory, key)

        for i in ("\\", "/", "(", ")", "=", ",", ".", "-", "#", " ", "+"):
            key = key.replace(i, "")

        key = key.split(maxsplit=1)[0]
        directory_e = directory.replace("\\", "/").strip("/")

        if isinstance(value, dict) and "index" in value:
            val, _, x = buttons(value, key_path, x)
            kpath = f"{directory_e}/{title}".strip("/")
            text_list.append(
                (
                    "<button onclick='toggleDisplay({name});GET(\"{csname}\");' "
                    "class='button' kpath='{kpath}' vpath='{vpath}'>{title}</button>"
                    "<div id='{name}' style='display:none;' class='button-folder'>{text}</div>"
                ).format(
                    name=f"{key}{get_id(key + val)}",
                    kpath=f"{kpath}/",
                    title="📂&nbsp;" + title.replace(" ", "&nbsp;"),
                    text=val,
                    vpath=f"{directory_e}/{title}/",
                    csname=key_path.replace("\\", "&#x2f;") + "/index.md",
                )
            )
        elif isinstance(value, dict):
            val, _, x = buttons(value, key_path, x)
            kpath = f"{directory_e}/{title}".strip("/")
            text_list.append(
                (
                    "<button onclick='toggleDisplay({name});' "
                    "class='button' kpath='{kpath}'>{title}</button>"
                    "<div id='{name}' style='display:none;' class='button-folder'>{text}</div>"
                ).format(
                    name=f"{key}{get_id(key+val)}",
                    kpath=kpath,
                    title="📂&nbsp;" + title.replace(" ", "&nbsp;"),
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
                    vpath=f"{directory_e}/{title}.md",
                    title="📄&nbsp;" + title.replace(" ", "&nbsp;"),
                )
            )
    return "".join(text_list), directory, x


def generate_index_html():
    result = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <link rel="icon" type="image/png" href="icon.png">
    <title>Шпаргалка</title>
    <link rel="stylesheet" href="cheatsheet/styles.css">
    <script src="cheatsheet/script.js"></script>
</head>
<body>
    <div class="cheatsheet-buttons">
        {buttons(DICT)[0]}
    </div>

    <pre id="field" class="cheatsheet-field">Нажмите на кнопку с темой, чтобы увидеть здесь объяснение</pre>

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
    <script>
        PutHtmlText(getCheatSheat("README.html"))
    </script>
</body>
</html>
"""

    with open("../cheatsheet/index.html", "w", encoding="utf-8") as file:
        file.write(BeautifulSoup(result, "html.parser").prettify())
