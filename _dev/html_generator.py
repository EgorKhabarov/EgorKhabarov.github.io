import os

from bs4 import BeautifulSoup

from _dev.data import DICT
from _dev.utils import print_progress_bar


id_dict = []
folder = """
<svg class="{color}" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="22" height="20" fill="currentColor" viewBox="2 0 26 24">
  <path fill-rule="evenodd" d="M4 4a2 2 0 0 0-2 2v12a2 2 0 0 0 .087.586l2.977-7.937A1 1 0 0 1 6 10h12V9a2 2 0 0 0-2-2h-4.532l-1.9-2.28A2 2 0 0 0 8.032 4H4Zm2.693 8H6.5l-3 8H18l3-8H6.693Z" clip-rule="evenodd"/>
</svg>
""".strip()
tag = """
<svg class="{color}" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="22" height="20" fill="currentColor" viewBox="2 0 26 24">
  <path d="M7.833 2c-.507 0-.98.216-1.318.576A1.92 1.92 0 0 0 6 3.89V21a1 1 0 0 0 1.625.78L12 18.28l4.375 3.5A1 1 0 0 0 18 21V3.889c0-.481-.178-.954-.515-1.313A1.808 1.808 0 0 0 16.167 2H7.833Z"/>
</svg>
""".strip()
link = """
<svg class="{color}" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="20" height="18" fill="none" viewBox="2 0 26 24">
  <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13.213 9.787a3.391 3.391 0 0 0-4.795 0l-3.425 3.426a3.39 3.39 0 0 0 4.795 4.794l.321-.304m-.321-4.49a3.39 3.39 0 0 0 4.795 0l3.424-3.426a3.39 3.39 0 0 0-4.794-4.795l-1.028.961"/>
</svg>
""".strip()


def get_path(meta_json, key_list: list[str], mode: str) -> dict:
    if len(key_list) == 1:
        if mode == "folder":
            return meta_json[key_list[0]][0]
        else:
            return meta_json[key_list[0]]

    *key_list, last_element = key_list
    now_meta = meta_json
    for key in key_list:
        now_meta = now_meta[key][1]
    if mode == "folder":
        return now_meta[last_element][0]
    return now_meta[last_element]


def buttons(
    dictionary: dict,
    directory: str = "",
    meta_json: dict = None,
    x: int = 0,
    y: int = 0,
) -> tuple[str, str, int]:
    text_list = []
    for key, value in dictionary.items():
        print_progress_bar(x, y, "create index.html", f"{directory}\\{key}")
        title = key.replace(" ", "&nbsp;").replace("-", "&#8288;-&#8288;")
        meta = get_path(
            meta_json,
            (directory.replace("\\", "/") + "/" + key.removesuffix("index")).strip("/").split("/"),
            mode="folder" if isinstance(value, dict) else "value",
        )

        if key.startswith("link-") and key.removeprefix("link-").isdigit():
            vpath = value

            color = meta.get("color")
            if not color:
                try:
                    path = vpath.removesuffix("/index.md") if vpath.endswith("/index.md") else vpath.removesuffix(".md")
                    try:
                        color = get_path(meta_json, path.split("/"), mode="value").get("color")
                    except AttributeError:
                        color = get_path(meta_json, path.split("/"), mode="folder").get("color")
                    if not color:
                        raise KeyError
                except KeyError:
                    color = "white"
            svg = link.format(color=color)
            title = vpath.removesuffix("index.md") if vpath.endswith("/index.md") else vpath.removesuffix(".md")
            text_list.append(
                f'<button class="button unselectable" vpath="{vpath}" '
                f'onclick="'
                f'GET(this.getAttribute(`vpath`));restoreCheatSheetState(this.getAttribute(`vpath`));delAnchor();'
                f'" title="{title}">{svg}{title}</button>\n'
            )
            continue

        if key == "index":
            x += 1
            continue

        #  print(f"{directory}/{key}".strip("/"))

        key_path = os.path.join(directory, key)
        directory_e = directory.replace("\\", "/").strip("/")

        if isinstance(value, dict) and "index" in value:
            val, _, x = buttons(value, key_path, meta_json, x, y)
            kpath = f"{directory_e}/{key}/"
            vpath = f"{directory_e}/{key}/index.md"
            svg = folder.format(color=meta.get("color", "yellow"))
            text_list.append(
                f'<button class="button unselectable" kpath="{kpath}" vpath="{vpath}" '
                f'onclick="'
                f'GET(this.getAttribute(`vpath`));toggleDisplay(this.nextElementSibling);delAnchor();'
                f'" title="{title}">{svg}{title}</button>'
                f'<div class="button-folder" style="display:none;">{val}</div>'
            )
        elif isinstance(value, dict):
            val, _, x = buttons(value, key_path, meta_json, x, y)
            kpath = f"{directory_e}/{key}".strip("/")
            svg = folder.format(color=meta.get("color", "yellow"))
            text_list.append(
                f'<button class="button unselectable" kpath="{kpath}" '
                f'onclick="'
                f'toggleDisplay(this.nextElementSibling);'
                f'" title="{title}">{svg}{title}</button>'  
                f'<div class="button-folder" style="display:none;">{val}</div>'
            )
        else:
            x += 1
            vpath = f"{directory_e}/{key}.md".strip("/")
            svg = tag.format(color=meta.get("color", "white"))
            text_list.append(
                f'<button class="button unselectable" vpath="{vpath}" '
                f'onclick="'
                f'GET(this.getAttribute(`vpath`));delAnchor();'
                f'" title="{title}">{svg}{title}</button>\n'
            )
    return "".join(text_list), directory, x


def generate_index_html(cheatsheet_count: int, meta_json: dict):
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
                <input id="search" type="text" class="search-input unselectable" placeholder="🔎 Поиск">
            </div>
            <div id="search-button-folder" class="button-folder unselectable" style="display:none;"></div>
            {buttons(DICT, meta_json=meta_json, y=cheatsheet_count - 1)[0]}
        </div>
        <div id="rpanrResize">&nbsp;</div>
        <pre id="field" class="cheatsheet-field">Нажмите на кнопку с темой, чтобы увидеть здесь объяснение</pre>
        <div>
            <button id="FontSizeSize"     class="control-button unselectable" style="padding-left: 12px;" onclick="changeFontSize(field, '=')">12px</button>
            <button                       class="control-button unselectable" style="padding-left: 25px;" onclick="changeFontSize(field, '+')">+</button>
            <button                       class="control-button unselectable" style="padding-left: 27px;" onclick="changeFontSize(field, '-')">-</button>
            <button id="COPY"             class="control-button unselectable" style="padding-left: 12px;" onclick="copyTextFromDiv(field);changeColor(COPY)">Copy</button>
            <button id="COPY2"            class="control-button unselectable" style="padding-left: 2px;"  onclick="copyTextFromDiv2();changeColor(COPY2)">Copy selected</button>
            <button id="removeargfromurl" class="control-button unselectable" style="padding-left: 28px;" onclick="removeArgumentFromUrl();delAnchor();window.location.reload();changeColor(removeargfromurl)">/</button>
        </div>
    </body>
</html>
"""
    with open("../cheatsheet/index.html", "w", encoding="utf-8") as file:
        file.write(BeautifulSoup(result, "html.parser").prettify())
