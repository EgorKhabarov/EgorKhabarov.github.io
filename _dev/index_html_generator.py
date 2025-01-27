import os

import yaml
from bs4 import BeautifulSoup


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

link_button = """
<button vpath="{vpath}" onclick="onclickLinkButton(this);" title="{title}">{svg}{title}</button>
"""
cheatsheet_button = """
<button vpath="{vpath}" onclick="onclickCheatSheetButton(this);" title="{title}">{svg}{title}</button>
"""
folder_button = """
<button kpath="{kpath}" onclick="onclickFolderButton(this)" title="{title}">{svg}{title}</button>  
<div class="button_folder" style="display:{css_display};">{button_folder_data}</div>
"""
folder_cheatsheet_button = """
<button kpath="{kpath}" vpath="{vpath}" onclick="onclickFolderCheatSheetButton(this);" title="{title}">{svg}{title}</button>
<div class="button_folder" style="display:{css_display};">{button_folder_data}</div>
"""
default_value = {}


def format_link_button(title: str, svg: str, vpath: str) -> str:
    return link_button.format(
        title=title,
        svg=svg,
        vpath=vpath,
    )


def format_cheatsheet_button(title: str, svg: str, vpath: str) -> str:
    return cheatsheet_button.format(
        title=title,
        svg=svg,
        vpath=vpath,
    )


def format_folder_button(title: str, svg: str, kpath: str, css_display: str, button_folder_data: str) -> str:
    return folder_button.format(
        title=title,
        svg=svg,
        kpath=kpath,
        css_display=css_display,
        button_folder_data=button_folder_data,
    )


def format_folder_cheatsheet_button(title: str, svg: str, kpath: str, vpath: str, css_display: str, button_folder_data: str) -> str:
    return folder_cheatsheet_button.format(
        title=title,
        svg=svg,
        kpath=kpath,
        vpath=vpath,
        css_display=css_display,
        button_folder_data=button_folder_data,
    )


def generate_buttons(dictionary: dict, directory: str = "") -> tuple[str, str]:
    text_list = []
    for key, value in dictionary.items():
        if key in ("index", "."):
            continue

        title = key.replace(" ", "&nbsp;").replace("-", "&#8288;-&#8288;")
        path = f"{directory}/{key}".replace("\\", "/").lstrip("/")
        if isinstance(value, dict):
            path += "/"

        current_metadata_str = value if isinstance(value, str) else str(value.get("."))
        current_metadata = yaml.safe_load(current_metadata_str)
        if isinstance(current_metadata, str | None):
            current_metadata = default_value

        if key.startswith(":") and key.removeprefix(":"):
            path = f"{directory}/{key.removeprefix(":")}".replace("\\", "/").lstrip("/")
            with open(f"../cheatsheet/{path}.link", "r", encoding="UTF-8") as link_file:
                value = link_file.read().strip()
            color = current_metadata.get("color", "white")
            # if not color:
            #     color = metadata.get(
            #         value.removesuffix("index") if value.endswith("/index") else value,
            #         default_value,
            #     ).get("color", "white")
            svg = link.format(color=color)
            title = value.removesuffix("index") if value.endswith("/index") else value.removesuffix("")
            text_list.append(format_link_button(title=title, svg=svg, vpath=value))
            continue

        #  print(f"{directory}/{key}".strip("/"))

        key_path = os.path.join(directory, key)
        directory_e = directory.replace("\\", "/").strip("/")

        if isinstance(value, dict) and "index" in value:
            button_folder_data = generate_buttons(value, key_path)[0]
            kpath = f"{directory_e}/{key}".strip("/")
            vpath = f"{directory_e}/{key}/index"
            svg = folder.format(color=current_metadata.get("color", "yellow"))
            css_display = "block" if current_metadata.get("folder-open") else "none"
            text_list.append(
                format_folder_cheatsheet_button(
                    title=title,
                    svg=svg,
                    kpath=kpath,
                    vpath=vpath,
                    css_display=css_display,
                    button_folder_data=button_folder_data,
                )
            )
        elif isinstance(value, dict):
            button_folder_data = generate_buttons(value, key_path)[0]
            kpath = f"{directory_e}/{key}".strip("/")
            svg = folder.format(color=current_metadata.get("color", "yellow"))
            css_display = "block" if current_metadata.get("folder-open") else "none"
            text_list.append(
                format_folder_button(
                    title=title,
                    svg=svg,
                    kpath=kpath,
                    css_display=css_display,
                    button_folder_data=button_folder_data,
                )
            )
        else:
            vpath = f"{directory_e}/{key}".lstrip("/")
            svg = tag.format(color=current_metadata.get("color", "white"))
            text_list.append(
                format_cheatsheet_button(
                    title=title,
                    svg=svg,
                    vpath=vpath,
                )
            )
    return "".join(text_list), directory


def prettify_index_html():
    with open("../cheatsheet/index.html", "r", encoding="utf-8") as file:
        index_html = file.read()
    with open("../cheatsheet/index.html", "w", encoding="utf-8") as file:
        file.write(BeautifulSoup(index_html, "html.parser").prettify())
