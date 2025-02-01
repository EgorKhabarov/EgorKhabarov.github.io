import os
import json
import yaml
from collections import UserDict
from typing import Generator, Any, Callable

import git
import requests
from bs4 import BeautifulSoup


try:
    repo: git.Repo = git.Repo(r"..")
except git.exc.InvalidGitRepositoryError:
    raise

try:
    branch: str = repo.active_branch.name
except TypeError:
    branch = repo.head.commit.hexsha[:8]


def set_unselectable(text: str, sep: str = "\n"):
    lines = []
    text_list = text.split(sep)
    text_list_len = len(text_list)
    text_list_iterator = iter(text_list)
    n = 0

    for line in text_list_iterator:
        if line.startswith("</pre></div>"):
            lines.append(line)
            continue

        if line.startswith('<span class="go">') and line.endswith("</span>"):
            line_list = [line]
            while (
                n + 1 <= text_list_len
                and text_list[n + 1].startswith('<span class="go">')
                and text_list[n + 1].endswith("</span>")
            ):
                line_list.append(next(text_list_iterator))
                n += 1
            try:
                nextline = next(text_list_iterator)
                n += 1
            except StopIteration:
                nextline = "</span>"
            else:
                if nextline.startswith(
                    (
                        '<span class="o">&gt;&gt;&gt;</span> ',
                        '<span class="gp">&gt;&gt;&gt; </span>',
                        '<span class="o">>>></span> ',
                        '<span class="gp">>>> </span>',
                        '<span class="o">&gt;&gt;&gt;</span>',
                        '<span class="gp">&gt;&gt;&gt;</span>',
                        '<span class="o">>>></span>',
                        '<span class="gp">>>></span>',
                    )
                ):
                    nextline = '<span class="o">&gt;&gt;&gt; </span></span>{}'.format(
                        nextline.removeprefix('<span class="o">&gt;&gt;&gt;</span> ')
                        .removeprefix('<span class="gp">&gt;&gt;&gt; </span>')
                        .removeprefix('<span class="o">>>></span> ')
                        .removeprefix('<span class="gp">>>> </span>')
                        .removeprefix('<span class="o">&gt;&gt;&gt;</span>')
                        .removeprefix('<span class="gp">&gt;&gt;&gt;</span>')
                        .removeprefix('<span class="o">>>></span>')
                        .removeprefix('<span class="gp">>>></span>')
                    )
                else:
                    nextline = f"</span>{nextline}"
            line = f'<span class="unselectable">{sep.join(line_list)}{sep}{nextline}'
        elif line.startswith(
            (
                '<div class="highlight"><pre><span></span><span class="o">&gt;&gt;&gt;</span> ',
                '<div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span>',
                '<div class="highlight"><pre><span></span><span class="o">>>></span> ',
                '<div class="highlight"><pre><span></span><span class="gp">>>> </span>',
            )
        ):
            line = (
                '<div class="highlight"><pre><span></span>'
                '<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span>'
            ) + line.removeprefix(
                '<div class="highlight"><pre><span></span><span class="o">&gt;&gt;&gt;</span> '
            ).removeprefix(
                '<div class="highlight"><pre><span></span><span class="gp">&gt;&gt;&gt; </span>'
            ).removeprefix(
                '<div class="highlight"><pre><span></span><span class="o">>>></span> '
            ).removeprefix(
                '<div class="highlight"><pre><span></span><span class="gp">>>> </span>'
            )
        elif line.startswith(
            (
                '<span class="o">&gt;&gt;&gt;</span> ',
                '<span class="gp">&gt;&gt;&gt; </span>',
                '<span class="o">>>></span> ',
                '<span class="gp">>>> </span>',
            )
        ):
            line = (
                '<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span>'
                + line.removeprefix('<span class="o">&gt;&gt;&gt;</span> ')
                .removeprefix('<span class="gp">&gt;&gt;&gt; </span>')
                .removeprefix('<span class="o">>>></span> ')
                .removeprefix('<span class="gp">>>> </span>')
            )
        elif line.startswith(
            (
                '<div class="highlight"><pre><span></span><span class="o">...</span> ',
                '<div class="highlight"><pre><span></span><span class="gp">... </span>',
            )
        ):
            line = (
                '<div class="highlight"><pre><span></span>'
                '<span class="unselectable"><span class="o">...</span> </span>'
            ) + line.removeprefix(
                '<div class="highlight"><pre><span></span><span class="o">...</span> '
            ).removeprefix(
                '<div class="highlight"><pre><span></span><span class="gp">... </span>'
            )
        elif line.startswith(
            (
                '<span class="o">...</span> ',
                '<span class="gp">... </span>',
            )
        ):
            line = (
                '<span class="unselectable"><span class="o">...</span> </span>'
                + line.removeprefix('<span class="o">...</span> ').removeprefix(
                    '<span class="gp">... </span>'
                )
            )
        else:
            line = f'<span class="unselectable">{line}</span>'

        lines.append(line)
        n += 1

    return sep.join(lines)


def get_files(
    filter_func: Callable[[str], bool] = lambda p: True
) -> Generator[str, Any, None]:
    return (
        path.replace("\\", "/").removeprefix("../cheatsheet/")
        for directory, dirnames, filenames in os.walk("../cheatsheet")
        for filename in filenames
        if (path := os.path.join(directory, filename)) and None or filter_func(path)
    )


def get_git_diff(
    filter_func: Callable[[str], bool] = lambda p: True
) -> Generator[str, Any, None]:
    for diff in repo.head.commit.diff(None):
        if (
            not diff.deleted_file
            and diff.b_path.startswith(r"cheatsheet/")
            and filter_func(diff.b_path)
        ):
            yield diff.b_path.removeprefix("cheatsheet/")
    for diff_path in repo.untracked_files:
        if diff_path.startswith(r"cheatsheet/") and filter_func(diff_path):
            yield diff_path.removeprefix("cheatsheet/")


def get_git_diff_moved_from_cheat_sheet_dict(
    filter_func: Callable[[str], bool] = lambda p: True
) -> dict[str, str]:
    return {
        diff.b_path.removeprefix("cheatsheet/")
        .removesuffix(".md"): diff.a_path.removeprefix("cheatsheet/")
        .removesuffix(".md")
        for diff in repo.head.commit.diff(None)
        if (
            not diff.deleted_file
            and diff.b_path.startswith(r"cheatsheet/")
            and filter_func(diff.b_path)
        )
    }


def get_sorted_cheat_sheets_list(index_json):
    files = []

    def recurse(directory: dict[str, str | dict[str, str | dict]], path: str = ""):
        for key, value in directory.items():
            if isinstance(value, dict):
                recurse(value, f"{path}/{key}")
            else:
                files.append(f"{path}/{key}".strip("/"))

    recurse(index_json)
    return files


def update_svg_badge(cheatsheet_count: int = 0):
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
        with open("../cheatsheet/cheatsheet_resources/badge.svg", "w", encoding="utf-8") as file:
            file.write(content)


def dict_walk(
    d: dict[str, str | dict[str, str | dict]],
    __now_dir: tuple[str, ...] = (),
):
    """
    for directory, dirnames, filenames in dict_walk(...):

    :param d:
    :param __now_dir:
    :return:
    """
    directory = "/".join(__now_dir)
    dirnames, dirs, filenames = [], [], []
    for k, v in d.items():
        if isinstance(v, dict):
            dirs.append((k, v))
            dirnames.append(k)
        else:
            filenames.append(k)
    yield directory, dirnames, filenames
    if dirs:
        for k, v in dirs:
            yield from dict_walk(v, __now_dir + (k,))


class PathDict(UserDict):
    def __setitem__(self, key: str, value: str):
        if "/" not in key:
            return super().__setitem__(key, value)
        path, key = key.rsplit("/", maxsplit=1)
        self.__getitem__(path, _is_dir=True)[key] = value

    def __delitem__(self, key: str):
        # Удаляет значение или директорию по ключу
        # Если ключ простой то удаляем обычным методом
        if "/" not in key:
            return super().__delitem__(key)
        parent_dir, value = key.rsplit("/", maxsplit=1)
        del self.__getitem__(parent_dir, _is_dir=True)[value]
        while len(self.__getitem__(parent_dir, _is_dir=True).keys()) == 0:
            parent_dir, *value = parent_dir.rsplit("/", maxsplit=1)
            if not value:
                del self.__getitem__("", _is_dir=True)[parent_dir]
                break
            del self.__getitem__(parent_dir, _is_dir=True)[value[0]]

    def __getitem__(self, key: str, _is_dir: bool = False):
        if not key:
            return self.data
        if "/" not in key:
            if _is_dir:
                return super().setdefault(key, {})
            return super().__getitem__(key)
        *path, key = key.split("/")
        temp = self.data
        for p in path:
            temp = temp.setdefault(p, {})
        if _is_dir:
            return temp.setdefault(key, {})
        return temp.setdefault(key, "")

    def exist(self, key: str) -> bool:
        temp = self.data
        for p in key.split("/"):
            try:
                temp = temp[p]
            except KeyError:
                return False
        return True


def update_index_json(
    index_json: dict[str, str | dict[str, str | dict]],
    added_cheat_sheets: list[str],
    removed_cheat_sheets: list[str],
    moved_from_cheat_sheets_dict: dict[str, str],
) -> dict[str, str | dict[str, str | dict]]:
    sorted_cheat_sheets_list = get_sorted_cheat_sheets_list(index_json)

    key_func = get_index_decorator(sorted_cheat_sheets_list)
    added_cheat_sheets = sorted(
        added_cheat_sheets,
        key=lambda key: key_func(moved_from_cheat_sheets_dict.get(key)),
    )
    removed_cheat_sheets = sorted(removed_cheat_sheets, key=key_func)

    path_dict = PathDict(index_json)

    for added_cheat_sheet in added_cheat_sheets:
        if not path_dict.exist(added_cheat_sheet):
            value = ""
            added_from_cheat_sheet = moved_from_cheat_sheets_dict.get(added_cheat_sheet)
            if added_from_cheat_sheet and path_dict.exist(added_from_cheat_sheet):
                value = path_dict[added_from_cheat_sheet]

            path_dict[added_cheat_sheet] = value

    for removed_cheat_sheet in removed_cheat_sheets:
        del path_dict[removed_cheat_sheet]

    return path_dict.data


def get_index_decorator(iterable: list):
    def wrapper(key):
        try:
            return iterable.index(key)
        except ValueError:
            return None

    return wrapper


def add_metadata(path_: str, metadata: dict) -> None:
    with open("../cheatsheet/index.json", "r", encoding="UTF-8") as index_json_file:
        index_json: dict[str, str | dict[str, str | dict]] = json.load(index_json_file)
    path_dict = PathDict(index_json)
    if not path_dict.exist(path_):
        print(f'\x1b[31mThis path is not exist "{path_}"\x1b[0m')
        return None
    result_metadata = yaml.safe_load(path_dict[path_]) or {}
    string_result_metadata = json.dumps(result_metadata, indent=4, ensure_ascii=False)
    print(f'\x1b[31mPath "{path_}"\x1b[0m')
    print(f"\x1b[33mNow metadata\x1b[0m {string_result_metadata}")

    color = metadata.get("color") or None
    tags = (
        [
            str(tag)
            for tag__ in metadata.get("tags")
            if str(tag__)
            for tag_ in tag__.strip().splitlines()
            if str(tag_)
            for tag in tag_.split(" ")
            if str(tag)
        ]
        if any(metadata.get("tags", ()))
        else None
    )
    if not (color or tags):
        print("\x1b[31mNo new metadata\x1b[0m")
        return None

    if color:
        result_metadata["color"] = color

    if tags:
        result_tags = set(tags)
        if (
            "tags" in result_metadata
            and result_metadata["tags"]
            and isinstance(result_metadata["tags"], str)
        ):
            result_tags |= set(result_metadata["tags"].split(" "))
        string_tags = " ".join(result_tags)
        result_metadata["tags"] = string_tags

    string_result_metadata = json.dumps(result_metadata, indent=4, ensure_ascii=False)
    print(f"\x1b[32mNew metadata\x1b[0m {string_result_metadata}")
    if input('\x1b[31mTo approve, write "y" or "yes": \x1b[0m') in ("y", "yes"):
        path_dict[path_] = yaml.safe_dump(
            result_metadata, sort_keys=False, allow_unicode=True, indent=4
        )
        with open("../cheatsheet/index.json", "w", encoding="UTF-8") as index_json_file:
            json.dump(path_dict.data, index_json_file, indent=4, ensure_ascii=False)
        print("\x1b[32mMetadata updated successfully\x1b[0m")


def get_h_tags(path_: str) -> list[str]:
    with open(f"../cheatsheet/{path_}.html", "r", encoding="UTF-8") as file:
        soup = BeautifulSoup(file.read(), "html.parser")
    return [
        heading.text for heading in soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"])
    ]
