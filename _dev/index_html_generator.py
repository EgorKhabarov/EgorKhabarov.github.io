import os

import yaml
from bs4 import BeautifulSoup


old_folder_img = """
<img src="cheatsheet_resources/folders/{color}.svg" alt="folder_{color}">
""".strip()
old_tag_img = """
<img src="cheatsheet_resources/tags/{color}.svg" alt="tag_{color}">
""".strip()
old_link_img = """
<img src="cheatsheet_resources/links/{color}.svg" alt="link_{color}">
""".strip()

old_link_button = """
<button vpath="{vpath}" class="link_button" title="{title}">{svg}{title}</button>
""".strip()
old_cheatsheet_button = """
<button vpath="{vpath}"{tags} class="cheatsheet_button" title="{title}">{svg}{title}</button>
""".strip()
old_folder_button = """
<button kpath="{kpath}" class="folder_button" title="{title}">{svg}{title}</button>
<div class="buttons_folder" style="display:{css_display};">{buttons_folder_data}</div>
""".strip()
old_folder_cheatsheet_button = """
<button kpath="{kpath}" vpath="{vpath}" class="folder_cheatsheet_button" title="{title}">{svg}{title}</button>
<div class="buttons_folder" style="display:{css_display};">{buttons_folder_data}</div>
""".strip()

default_value: dict = {}
old_css_colors = {
    "yellow": "color:rgb(249, 197, 83)",
    "green": "color:rgb(60, 194, 58)",
    "white": "color:rgb(218, 218, 218)",
    "pink": "color:rgb(253, 99, 148)",
    "red": "color:rgb(224, 53, 52)",
    "lblue": "color:rgb(132, 184, 249)",
    "dblue": "color:rgb(20, 114, 248)",
    "violet": "color:rgb(140, 88, 133)",
    "brown": "color:rgb(131, 83, 51)",
}


def format_old_folder_svg(color: str) -> str:
    if color not in old_css_colors:
        color = "folder"
    return old_folder_img.format(color=color)


def format_old_tag_svg(color: str) -> str:
    if color not in old_css_colors:
        color = "tag"
    return old_tag_img.format(color=color)


def format_old_link_svg(color: str) -> str:
    if color not in old_css_colors:
        color = "folder"
    return old_link_img.format(color=color)


def format_old_link_button(title: str, svg: str, vpath: str) -> str:
    return old_link_button.format(
        title=title,
        svg=svg,
        vpath=vpath,
    )


def format_old_cheatsheet_button(title: str, svg: str, vpath: str, tags: str) -> str:
    return old_cheatsheet_button.format(
        title=title,
        svg=svg,
        vpath=vpath,
        tags=f' search-tags="{tags}"' if tags else "",
    )


def format_old_folder_button(
    title: str,
    svg: str,
    kpath: str,
    css_display: str,
    buttons_folder_data: str,
) -> str:
    return old_folder_button.format(
        title=title,
        svg=svg,
        kpath=kpath,
        css_display=css_display,
        buttons_folder_data=buttons_folder_data,
    )


def format_old_folder_cheatsheet_button(
    title: str,
    svg: str,
    kpath: str,
    vpath: str,
    css_display: str,
    buttons_folder_data: str,
) -> str:
    return old_folder_cheatsheet_button.format(
        title=title,
        svg=svg,
        kpath=kpath,
        vpath=vpath,
        css_display=css_display,
        buttons_folder_data=buttons_folder_data,
    )


def generate_old_buttons(dictionary: dict, directory: str = "") -> tuple[str, str]:
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
            svg = format_old_link_svg(color=color)
            title = (
                value.removesuffix("index")
                if value.endswith("/index")
                else value.removesuffix("")
            )
            text_list.append(format_old_link_button(title=title, svg=svg, vpath=value))
            continue

        key_path = os.path.join(directory, key)
        directory_e = directory.replace("\\", "/").strip("/")

        if isinstance(value, dict) and "index" in value:
            buttons_folder_data = generate_old_buttons(value, key_path)[0]
            kpath = f"{directory_e}/{key}".strip("/")
            vpath = f"{directory_e}/{key}/index".strip("/")
            svg = format_old_folder_svg(color=current_metadata.get("color", "yellow"))
            css_display = "block" if current_metadata.get("folder-open") else "none"
            text_list.append(
                format_old_folder_cheatsheet_button(
                    title=title,
                    svg=svg,
                    kpath=kpath,
                    vpath=vpath,
                    css_display=css_display,
                    buttons_folder_data=buttons_folder_data,
                )
            )
        elif isinstance(value, dict):
            buttons_folder_data = generate_old_buttons(value, key_path)[0]
            kpath = f"{directory_e}/{key}".strip("/")
            svg = format_old_folder_svg(color=current_metadata.get("color", "yellow"))
            css_display = "block" if current_metadata.get("folder-open") else "none"
            text_list.append(
                format_old_folder_button(
                    title=title,
                    svg=svg,
                    kpath=kpath,
                    css_display=css_display,
                    buttons_folder_data=buttons_folder_data,
                )
            )
        else:
            vpath = f"{directory_e}/{key}".lstrip("/")
            svg = format_old_tag_svg(color=current_metadata.get("color", "white"))
            tags = current_metadata.get("tags")
            text_list.append(
                format_old_cheatsheet_button(
                    title=title,
                    svg=svg,
                    vpath=vpath,
                    tags=tags,
                )
            )
    return "".join(text_list), directory


# noqa


new_css_colors = {
    "default": ' style="color: var(--color-file-default);"',
    "yellow":  ' style="color: var(--color-file-yellow);"',
    "green":   ' style="color: var(--color-file-green);"',
    "pink":    ' style="color: var(--color-file-pink);"',
    "red":     ' style="color: var(--color-file-red);"',
    "lblue":   ' style="color: var(--color-file-lblue);"',
    "dblue":   ' style="color: var(--color-file-dblue);"',
    "violet":  ' style="color: var(--color-file-violet);"',
    "brown":   ' style="color: var(--color-file-brown);"',
}

new_folder_img = """
<svg viewBox="0 0 24 24"{color}><use href="#icon-folder"/></svg>
""".strip()
new_tag_img = """
<svg viewBox="0 0 24 24"{color}><use href="#icon-file"/></svg>
""".strip()
new_cheatsheet_button = """
<div class="tree-item file" title="{title}">{svg}{title}</div>
""".strip()
new_folder_button = """
<div class="tree-group">
<div class="tree-item folder" data-state="closed" title="{title}">{svg}{title}</div>
<div class="tree-children hidden">{buttons_folder_data}</div>
</div>
""".strip().replace("\n", "")


def format_new_folder_svg(color: str) -> str:
    if color not in new_css_colors:
        color = ""
    else:
        color = new_css_colors[color]
    return new_folder_img.format(color=color)


def format_new_tag_svg(color: str) -> str:
    if color not in new_css_colors:
        color = ""
    else:
        color = new_css_colors[color]
    return new_tag_img.format(color=color)


def format_new_cheatsheet_button(title: str, svg: str, vpath: str, tags: str) -> str:
    return new_cheatsheet_button.format(
        title=title,
        svg=svg,
        vpath=vpath,
        tags=f' search-tags="{tags}"' if tags else "",
    )


def format_new_folder_button(
    title: str,
    svg: str,
    kpath: str,
    css_display: str,
    buttons_folder_data: str,
) -> str:
    return new_folder_button.format(
        title=title,
        svg=svg,
        kpath=kpath,
        css_display=css_display,
        buttons_folder_data=buttons_folder_data,
    )


def generate_new_buttons(dictionary: dict, directory: str = "") -> tuple[str, str]:
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
            # path = f"{directory}/{key.removeprefix(":")}".replace("\\", "/").lstrip("/")
            # with open(f"../cheatsheet/{path}.link", "r", encoding="UTF-8") as link_file:
            #     value = link_file.read().strip()
            # color = current_metadata.get("color", "white")
            # # if not color:
            # #     color = metadata.get(
            # #         value.removesuffix("index") if value.endswith("/index") else value,
            # #         default_value,
            # #     ).get("color", "white")
            # svg = format_link_svg(color=color)
            # title = (
            #     value.removesuffix("index")
            #     if value.endswith("/index")
            #     else value.removesuffix("")
            # )
            # text_list.append(format_link_button(title=title, svg=svg, vpath=value))
            continue

        key_path = os.path.join(directory, key)
        directory_e = directory.replace("\\", "/").strip("/")

        # if isinstance(value, dict) and "index" in value:
        #     buttons_folder_data = generate_new_buttons(value, key_path)[0]
        #     kpath = f"{directory_e}/{key}".strip("/")
        #     vpath = f"{directory_e}/{key}/index".strip("/")
        #     svg = format_folder_svg(color=current_metadata.get("color", "yellow"))
        #     css_display = "block" if current_metadata.get("folder-open") else "none"
        #     text_list.append(
        #         format_folder_cheatsheet_button(
        #             title=title,
        #             svg=svg,
        #             kpath=kpath,
        #             vpath=vpath,
        #             css_display=css_display,
        #             buttons_folder_data=buttons_folder_data,
        #         )
        #     ) el
        if isinstance(value, dict):
            buttons_folder_data = generate_new_buttons(value, key_path)[0]
            kpath = f"{directory_e}/{key}".strip("/")
            svg = format_new_folder_svg(color=current_metadata.get("color", "yellow"))
            css_display = "block" if current_metadata.get("folder-open") else "none"
            text_list.append(
                format_new_folder_button(
                    title=title,
                    svg=svg,
                    kpath=kpath,
                    css_display=css_display,
                    buttons_folder_data=buttons_folder_data,
                )
            )
        else:
            vpath = f"{directory_e}/{key}".lstrip("/")
            svg = format_new_tag_svg(color=current_metadata.get("color", "default"))
            tags = current_metadata.get("tags")
            text_list.append(
                format_new_cheatsheet_button(
                    title=title,
                    svg=svg,
                    vpath=vpath,
                    tags=tags,
                )
            )
    return "".join(text_list), directory


def prettify_index_html():
    with open("../cheatsheet/index-old.html", "r", encoding="UTF-8") as file:
        index_html = file.read()
    with open("../cheatsheet/index-old.html", "w", encoding="UTF-8") as file:
        file.write(BeautifulSoup(index_html, "html.parser").prettify())
