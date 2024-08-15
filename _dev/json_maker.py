import os
import json

from _dev.utils import print_progress_bar


def setdefault_path(new_meta_json, old_meta_json, key_list: list[str]) -> dict:
    """
    Заполняет новый пустой словарь данными из файловой системы
    Вызывает функцию get_path для получения возможных данных из старого словаря old_meta_json

    :param new_meta_json: Новый словарь
    :param old_meta_json: Старый словарь
    :param key_list: Список ключей (путь только до папки, без названий файлов)
    :return:
    """
    now_meta = new_meta_json
    for key in key_list:
        now_meta = now_meta.setdefault(key, [get_meta(old_meta_json, key_list, "folder"), {}])[1]

        # try:
        #     now_meta = now_meta[key][1]
        # except KeyError:
        #     now_meta[key] = [{}, {}]
        #     now_meta = now_meta[key][1]
    return now_meta


def get_meta(meta_json, key_list: list[str], mode: str) -> dict:
    """
    Получение возможных мета данных из старого json либо пустой словарь

    :param meta_json:
    :param key_list:
    :param mode:
    :return:
    """
    # if len(key_list) == 1:
    #     if mode == "folder":
    #         return meta_json[key_list[0]][0]
    #     else:
    #         return meta_json[key_list[0]]

    *key_list, last_element = key_list
    now_meta = meta_json
    try:
        for key in key_list:
            now_meta = now_meta[key][1]
        if mode == "folder":
            return now_meta[last_element][0]
        return now_meta[last_element]
    except KeyError:
        return {}


def make_json(cheatsheet_count: int):
    x = 0

    with open("meta.json", "r", encoding="UTF-8") as file:
        try:
            old_meta_json = json.load(file)
        except json.decoder.JSONDecodeError:
            old_meta_json = {}

    meta_json = {}

    for directory, dirnames, filenames in os.walk("../cheatsheet"):
        directory = directory.replace("\\", "/").removeprefix("../cheatsheet/")

        if x < 1:
            x += 1
            continue

        now_meta = setdefault_path(meta_json, old_meta_json, directory.split("/"))

        for dirname in dirnames:
            now_meta[dirname] = now_meta.get(
                dirname,
                [get_meta(old_meta_json, directory.split("/") + [dirname], "folder"), {}],
            )
            print_progress_bar(x, cheatsheet_count, "make json", f"{directory}/{dirname}/")

        for filename in filenames:
            if filename == "index.md":
                continue
            if filename.endswith(".md"):
                now_meta[filename.removesuffix(".md")] = now_meta.get(
                    filename.removesuffix(".md"),
                    get_meta(old_meta_json, directory.split("/") + [filename.removesuffix(".md")], "value"),
                )
                x += 1
                print_progress_bar(x, cheatsheet_count, "make json", f"{directory}/{filename}")

    with open("meta.json", "w", encoding="UTF-8") as file:
        json.dump(meta_json, file, indent=4, ensure_ascii=False)

    return meta_json


def clear_json():
    pass


if __name__ == "__main__":
    make_json(1)
