import os
import re
from pathlib import Path

import markdown
import requests
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter
from pygments.util import ClassNotFound

from _dev.data import DICT
from _dev.utils import set_unselectable, print_progress_bar


formatter = HtmlFormatter(style="default")


def code_block_callback(match: re.Match) -> str:
    code_block, language = match["code"], match["md_lang"] or match["pre_lang"] or ""
    code_block = code_block.replace("<mark>", "==").replace('<mark style="">', "==").replace("</mark>", "==")
    if "@" in language:
        language, filename = language.split("@", maxsplit=1)
    else:
        filename = ""

    if language == "":
        _language, language = "text", "text"
    elif language in ("regex", "regexp"):
        _language = "text"
    elif language == "csv":
        _language = "python"
    elif language == "python-console":
        _language = "pycon"
    else:
        _language = language

    try:
        lexer = get_lexer_by_name(_language, stripall=True)
    except ClassNotFound:
        _language = "text"
        lexer = get_lexer_by_name(_language, stripall=True)

    highlighted_code = highlight(code_block, lexer, formatter).strip()

    if _language in ("python", "pycon") and (
        '<span class="o">&gt;&gt;&gt;</span> ' in highlighted_code
        or '<span class="gp">&gt;&gt;&gt; </span>' in highlighted_code
        or '<span class="o">>>></span> ' in highlighted_code
        or '<span class="gp">>>> </span>' in highlighted_code
    ):
        highlighted_code = set_unselectable(highlighted_code, "\n")

    highlighted_code = highlighted_code.replace("`", "&#x60;")
    copy_svg = '<svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg>'
    download_svg = '<svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 3v4a1 1 0 0 1-1 1H5m5 4-2 2 2 2m4-4 2 2-2 2m5-12v16a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V7.914a1 1 0 0 1 .293-.707l3.914-3.914A1 1 0 0 1 9.914 3H18a1 1 0 0 1 1 1Z"/></svg>'

    copy_btn = f'<button class="copy_code_button" onclick="CopyCode(this)">{copy_svg}<text class="unselectable">Copy code</text></button>'
    download_btn = (
        f'<button class="download_code_button" onclick="DownloadCode(this, `{filename}`)">{download_svg}<text class="unselectable" title="{filename}">Download code</text></button>'
        if filename
        else ""
    )
    return f'<div class="code_element"><div class="lang_line"><text>{language}</text>{copy_btn}{download_btn}</div><div class="code language-{_language}">{highlighted_code}</div></div>'


def wikilink_func(match: re.Match) -> str:
    path = match.group(1)
    cheatsheet_name = path.rsplit("/", 1)[-1].removesuffix(".md").replace("%20", " ")
    return f'<a target="_self" href="?{path}" class="wikilink">{cheatsheet_name}</a>'


def to_markup(markdown_text: str):
    # WikiLinks
    highlighted_html = re.sub(
        r"\[\[([^\n\]]+)]]",
        wikilink_func,
        markdown_text
    )
    # <mark>
    highlighted_html = re.sub(
        r"==(?:\{(?P<style>.*?)})?(?P<mark>[^=\n]+?)==",
        lambda m: f'<mark style="{m["style"] or ""}">{m["mark"]}</mark>',
        highlighted_html,
    )
    # Замена блоков кода на подсвеченный HTML
    highlighted_html = re.sub(
        r"(?si)((`{3,})(?P<md_lang>[a-z+#@._\d-]*)|<pre><code class=\"language-(?P<pre_lang>[a-z+#-]*)\">)"
        r"(?P<code>.*?)"
        r"(\2|</code></pre>)",
        code_block_callback,
        highlighted_html,
    )

    # Обработка остальной разметки
    md_extensions = [
        "markdown.extensions.tables",
        "markdown.extensions.fenced_code",
    ]
    return markdown.markdown(highlighted_html, extensions=md_extensions)


def create_files_and_folders(dictionary, directory: str = "../cheatsheet", x: int = 0, y: int = 0):
    """
    Рекурсивная функция, которая создает файлы и папки для каждого ключа-значения в словаре.

    :param dictionary: Словарь, который нужно воссоздать в виде файлов и папок
    :param directory: Директория, в которой нужно создать файлы и папки (по умолчанию - текущая директория)
    :param x:
    :param y:
    """
    generate_html = False

    for key, value in dictionary.items():
        key_path = os.path.join(directory, key)
        print_progress_bar(x, y, "create cheatsheets", key_path.replace("\\", "/"))
        key_path_html = key_path

        if isinstance(value, str):
            key_path_html = key_path + ".html"
            key_path += ".md"

        if isinstance(value, dict):
            # Если значение - словарь, создаем папку и вызываем функцию рекурсивно
            os.makedirs(key_path, exist_ok=True)
            x = create_files_and_folders(value, key_path, x, y)
        else:
            x += 1
            # Если значение - строка, создаем файл с содержимым строки
            if generate_html:
                with open(key_path_html, "w", encoding="utf-8") as f:
                    f.write(to_markup(value.strip()))
                with open(key_path, "w", encoding="utf-8") as f:
                    f.write(value.strip())
            else:
                with open(key_path, "w", encoding="utf-8") as f:
                    f.write(to_markup(value.strip()))

    for directory, dirnames, filenames in os.walk("../cheatsheet"):
        for dirname in dirnames:
            dir_path = os.path.join(directory, dirname)
            # Если директория пустая, удаляем ее
            if not os.listdir(dir_path):
                os.rmdir(dir_path)
                # print(f"Удалена пустая директория: {dir_path}")
    return x


def create_files(cheatsheet_count: int, additional_path: str = ""):
    dictionary = DICT
    directory = Path("../cheatsheet")

    if additional_path:
        directory = directory.joinpath(additional_path)
        for path in additional_path.strip("/").split("/"):
            dictionary = dictionary[path]

    create_files_and_folders(dictionary, directory=str(directory), y=cheatsheet_count - 1)

    try:
        content = requests.get(
            f"https://img.shields.io/badge/{cheatsheet_count}%20cheatsheet-brightgreen",
            {
                "style": "flat",
                "logo": "github",
                "label": "GitHub Pages",
            },
        ).content.decode()
    except requests.exceptions.ConnectionError:
        pass
    else:
        with open("../cheatsheet/cheatsheet_badge.svg", "w", encoding="utf-8") as file_readme:
            file_readme.write(content)


def create_file(keys: tuple[str]):
    filepath = f"cheatsheet\\" + "\\".join(keys) + ".md"
    os.makedirs(filepath.rsplit("\\", maxsplit=1)[0], exist_ok=True)
    value = DICT
    for key in keys:
        value = value[key]

    with open(filepath, "w", encoding="utf-8") as file:
        file.write(to_markup(value.strip()))
