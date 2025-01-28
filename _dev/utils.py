import os
from collections import UserDict
from typing import Generator, Any, Callable

import git
import requests


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
        with open("../cheatsheet/cheatsheet_badge.svg", "w", encoding="utf-8") as file:
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
) -> dict[str, str | dict[str, str | dict]]:
    path_dict = PathDict(index_json)

    for added_cheat_sheet in added_cheat_sheets:
        if not path_dict.exist(added_cheat_sheet):
            path_dict[added_cheat_sheet] = ""

    for removed_cheat_sheet in removed_cheat_sheets:
        del path_dict[removed_cheat_sheet]

    return path_dict.data
