from markdown import markdown
from data import DICT
import os

def url_shortener(url):
    return (
        lambda url_: url_ if url_ == "http://www.w3.org/2000/svg" else f"<a href='{url_}' target='_blank'>{url_}</a>"
    )(url[0])

def to_markup(text):
    text = markdown(text.strip("\n").strip(" ").replace("<", "&lt;"), extensions=['tables', 'fenced_code']
                    ).replace("<p>", "").replace("</p>", "").strip()
    return text

def create_files_and_folders(dictionary, directory="."):
    """
    Рекурсивная функция, которая создает файлы и папки для каждого ключа-значения в словаре.

    :param dictionary: словарь, который нужно воссоздать в виде файлов и папок
    :param directory: директория, в которой нужно создать файлы и папки (по умолчанию - текущая директория)
    """
    for key, value in dictionary.items():
        if isinstance(value, str): key += ".txt"
        key_path = os.path.join(directory, key)

        if isinstance(value, dict):
            # Если значение - словарь, создаем папку и вызываем функцию рекурсивно
            os.makedirs(key_path, exist_ok=True)
            create_files_and_folders(value, directory=key_path)
        else:
            # Если значение - строка, создаем файл с содержимым строки
            with open(key_path, "w", encoding="utf-8") as f:
                f.write(to_markup(value.strip()))

create_files_and_folders(DICT, "cheatsheet")
