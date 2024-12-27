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
default_value = {}


def buttons(
    dictionary: dict,
    directory: str = "",
    metadata: dict = None,
    x: int = 0,
    y: int = 0,
) -> tuple[str, str, int]:
    text_list = []
    for key, value in dictionary.items():
        title = key.replace(" ", "&nbsp;").replace("-", "&#8288;-&#8288;")
        path = f"{directory}/{key}".replace("\\", "/").lstrip("/")
        print_progress_bar(x, y, "create index.html", path)
        if isinstance(value, dict):
            path += "/"

        current_metadata = metadata.get(path, default_value)

        if key.startswith("link-") and key.removeprefix("link-").isdigit():
            x += 1
            color = current_metadata.get("color")
            if not color:
                color = metadata.get(
                    value.removesuffix("index") if value.endswith("/index") else value,
                    default_value,
                ).get("color", "white")
            svg = link.format(color=color)
            title = value.removesuffix("index") if value.endswith("/index") else value.removesuffix("")
            text_list.append(
                f'<button vpath="{value}" onclick="onclickLinkButton(this);" title="{title}">{svg}{title}</button>\n'
            )
            continue

        if key == "index":
            x += 1
            continue

        #  print(f"{directory}/{key}".strip("/"))

        key_path = os.path.join(directory, key)
        directory_e = directory.replace("\\", "/").strip("/")

        if isinstance(value, dict) and "index" in value:
            val, _, x = buttons(value, key_path, metadata, x, y)
            kpath = f"{directory_e}/{key}".strip("/")
            vpath = f"{directory_e}/{key}/index"
            svg = folder.format(color=current_metadata.get("color", "yellow"))
            display = "block" if current_metadata.get("folder-open") else "none"
            text_list.append(
                f'<button kpath="{kpath}" vpath="{vpath}" '
                f'onclick="onclickFolderCheatSheetButton(this);" title="{title}">{svg}{title}</button>'
                f'<div class="button_folder" style="display:{display};">{val}</div>'
            )
        elif isinstance(value, dict):
            val, _, x = buttons(value, key_path, metadata, x, y)
            kpath = f"{directory_e}/{key}".strip("/")
            svg = folder.format(color=current_metadata.get("color", "yellow"))
            display = "block" if current_metadata.get("folder-open") else "none"
            text_list.append(
                f'<button kpath="{kpath}" '
                f'onclick="onclickFolderButton(this)" title="{title}">{svg}{title}</button>'  
                f'<div class="button_folder" style="display:{display};">{val}</div>'
            )
        else:
            x += 1
            vpath = f"{directory_e}/{key}".lstrip("/")
            svg = tag.format(color=current_metadata.get("color", "white"))
            text_list.append(
                f'<button vpath="{vpath}" '
                f'onclick="onclickCheatSheetButton(this);'
                f'" title="{title}">{svg}{title}</button>\n'
            )
    return "".join(text_list), directory, x


def generate_index_html(cheatsheet_count: int, metadata: dict):
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
        <style id="settings_css"></style>
        <style id="css_markdown_preview"></style>
        <div id="cheatsheet_buttons">
            <div class="search_container">
                <input id="search_input" type="text" class="search_input unselectable" placeholder="🔎 Поиск">
            </div>
            <div id="search_button_folder" class="button_folder unselectable" style="display:none;"></div>
            {buttons(DICT, metadata=metadata, y=cheatsheet_count - 1)[0]}
        </div>
        <div id="rpanrResize">&nbsp;</div>
        <pre id="cheatsheet_field">Нажмите на кнопку с темой</pre>
        <div id="cheatsheet_control_buttons">
            <button onclick="removeArgumentFromUrl();delAnchor();window.location.reload();">
                <!-- <img src="icon.png" width="24" height="24"/> -->
                <svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m4 12 8-8 8 8M6 10.5V19a1 1 0 0 0 1 1h3v-3a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v3h3a1 1 0 0 0 1-1v-8.5"/></svg>
            </button>
            <button id="font_size_button" onclick="changeFontSize('=')">12px</button>
            <button onclick="changeFontSize('+')"><svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 12h14m-7 7V5"/></svg></button>
            <button onclick="changeFontSize('-')"><svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 12h14"/></svg></button>
            <button id="settings_button"><svg aria-hidden="true" class="w-6 h-6 text-gray-800 dark:text-white" fill="none" height="24" viewbox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg"><path d="M20 6H10m0 0a2 2 0 1 0-4 0m4 0a2 2 0 1 1-4 0m0 0H4m16 6h-2m0 0a2 2 0 1 0-4 0m4 0a2 2 0 1 1-4 0m0 0H4m16 6H10m0 0a2 2 0 1 0-4 0m4 0a2 2 0 1 1-4 0m0 0H4" stroke="currentColor" stroke-linecap="round" stroke-width="2"></path></svg></button>
            <button id="fullscreen_button"><svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 8h.01M9 8h.01M12 8h.01M4 11h16M4 19h16a1 1 0 0 0 1-1V6a1 1 0 0 0-1-1H4a1 1 0 0 0-1 1v12a1 1 0 0 0 1 1Z"/></svg></button>
            <button onclick="copy(decodeURIComponent(window.location.href).replaceAll(' ', '%20'))"><svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13.213 9.787a3.391 3.391 0 0 0-4.795 0l-3.425 3.426a3.39 3.39 0 0 0 4.795 4.794l.321-.304m-.321-4.49a3.39 3.39 0 0 0 4.795 0l3.424-3.426a3.39 3.39 0 0 0-4.794-4.795l-1.028.961"/></svg></button>
        </div>
        <div id="settings_overlay" class="overlay"></div>
        <div id="settings_popup" class="popup">
            <h3 style="margin-top: 0px;margin-bottom: 6px;">Search</h3>
            <input type="checkbox" id="settings_search_regex" style="width: 13px;height: 13px;">
            Поиск по регулярным выражениям<br>
            <input type="checkbox" id="settings_search_register_independence" style="width: 13px;height: 13px;">
            Регистронезависимость поиска<br>
            <input type="checkbox" id="settings_search_full_path" style="width: 13px;height: 13px;">
            Поиск по всему пути (default вкл) /<br>
            <svg width="20" height="13"></svg>
            Поиск по имени шпаргалки (выкл)<br>
            <input type="checkbox" id="settings_search_show_full_path" style="width: 13px;height: 13px;">
            Показывать весь путь до шпаргалки<br>
            <input type="checkbox" id="settings_css_markdown_preview" style="width: 13px;height: 13px;" onclick="css_markdown_preview_func(this)">
            CSS предпросмотр Markdown<br>
            <h3 style="margin-top: 0px;margin-bottom: 6px;">CSS</h3>
            <textarea id="settings_css_textarea" oninput="settings.settings_css=this.value;settings_css.innerHTML=this.value;saveSettings(settings)" rows="7"></textarea>
            <button id="settings_reset_button">Reset</button>
            <button id="settings_ok_button">Ok</button>
        </div>
    </body>
</html>
"""
    with open("../cheatsheet/index.html", "w", encoding="utf-8") as file:
        file.write(BeautifulSoup(result, "html.parser").prettify())
