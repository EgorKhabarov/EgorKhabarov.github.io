import os

import markdown
import requests
from _dev.data import DICT
from _dev.utils import print_progress_bar


def to_markup(markdown_text):
    # Обработка остальной разметки
    md_extensions = [
        "markdown.extensions.tables",
        "markdown.extensions.fenced_code",
    ]
    return markdown.markdown(markdown_text, extensions=md_extensions)


def create_files_and_folders(dictionary, directory: str = ".", x: int = 0, y: int = 0):
    """
    Рекурсивная функция, которая создает файлы и папки для каждого ключа-значения в словаре.

    :param dictionary: Словарь, который нужно воссоздать в виде файлов и папок
    :param directory: Директория, в которой нужно создать файлы и папки (по умолчанию - текущая директория)
    :param x:
    :param y:
    """
    for key, value in dictionary.items():
        if key.startswith("::link::"):
            continue

        key_path = os.path.join(directory, key)
        print_progress_bar(x, y, "create cheatsheets", key_path)

        if isinstance(value, str):
            key_path += ".md"

        if isinstance(value, dict):
            # Если значение - словарь, создаем папку и вызываем функцию рекурсивно
            os.makedirs(key_path, exist_ok=True)
            x = create_files_and_folders(value, key_path, x, y)
        else:
            x += 1
            # Если значение - строка, создаем файл с содержимым строки
            with open(key_path, "w", encoding="utf-8") as f:
                f.write(to_markup(value.strip()))

    return x


def create_files(cheatsheet_count: int):
    create_files_and_folders(DICT, "../cheatsheet", y=cheatsheet_count - 1)

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
        with open("../cheatsheet/README.html", "w", encoding="utf-8") as file_readme:
            file_readme.write(
                f"""
<h1>egorkhabarov.github.io/cheatsheet</h1>

{content}

<!--
https://img.shields.io/badge/{cheatsheet_count}%20cheatsheet-brightgreen?style=flat&logo=github&label=GitHub Pages
-->
""".strip()
            )


def create_file(keys: tuple[str]):
    filepath = f"cheatsheet\\" + "\\".join(keys) + ".md"
    os.makedirs(filepath.rsplit("\\", maxsplit=1)[0], exist_ok=True)
    value = DICT
    for key in keys:
        value = value[key]

    with open(filepath, "w", encoding="utf-8") as file:
        file.write(to_markup(value.strip()))
