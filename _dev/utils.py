import sys
from pathlib import Path
from typing import Generator, Any, Callable

import git
from pygments import highlight
from pygments.formatters.html import HtmlFormatter
from pygments.lexers import get_lexer_by_name


try:
    repo: git.Repo = git.Repo(r"..")
except git.exc.InvalidGitRepositoryError:
    raise

try:
    branch: str = repo.active_branch.name
except TypeError:
    branch = repo.head.commit.hexsha[:8]


# TODO удалить
reserved_filenames = [
    filename
    for filenames in map(
        lambda l: (l, l + "."),
        """
CON
PRN
AUX
NUL
COM1
COM2
COM3
COM4
COM5
COM6
COM7
COM8
COM9
LPT1
LPT2
LPT3
LPT4
LPT5
LPT6
LPT7
LPT8
LPT9
CLOCK$
CONIN$
CONOUT$
COM0
PRN0
LPT0
""".strip().splitlines()
    )
    for filename in filenames
]


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
                        nextline
                        .removeprefix('<span class="o">&gt;&gt;&gt;</span> ')
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


# TODO удалить
def to_table_code(lang: str, code: str):
    formatter = HtmlFormatter(style="default")
    lexer = get_lexer_by_name(lang, stripall=True)
    highlighted_code = highlight(code, lexer, formatter).strip().replace("\n", "<br>").replace("|", "&#x7c;")

    if lang == "python" and '<span class="o">&gt;&gt;&gt;</span> ' in highlighted_code:
        highlighted_code = set_unselectable(highlighted_code, "<br>")

    result = rf"""
<div class="code" style="border-radius:.375rem .375rem;">
<div class="highlight">
<pre>
{highlighted_code}
</pre>
</div>
</div>
""".strip().replace(
        "\n", ""
    )
    return result


# TODO удалить
def to_table_code_py(code: str) -> str:
    return to_table_code("python", code)


# TODO удалить
def to_table_code_java(code: str) -> str:
    return to_table_code("java", code)


# TODO удалить
def to_table_code_sql(code: str) -> str:
    return to_table_code("sql", code)


def check_dict_keys(d: dict, c: int = 0, path: list = None) -> tuple[bool | int, list | None]:
    """
    Рекурсивно обходит словарь и проверяет ключи на правила именования файлов и папок в файловой системе
    TODO удалить

    :param d:
    :param c:
    :param path:
    :return:
    """
    if path is None:
        path = []

    for k, v in d.items():
        print_progress_bar(c, 0, "counting cheatsheets", k)
        path.append(k)
        if (
            (not k)
            or k == "."
            or "\x00" in k
            or set(k) & set("\\/:*?'\"<>|")
            or k in reserved_filenames
        ):
            return False, path
        if isinstance(v, dict):
            res, errors = check_dict_keys(v, c, path)
            if res is False:
                return False, errors
            c = res
        else:
            c += 1
        path.pop()
    return c, None


def print_progress_bar(x: int, y: int, name: str, text: str = None):
    bar_length = 50

    if y == 0:
        y = 100

    progress = x / y
    arrow = ("█" * int(progress * bar_length))
    if len(arrow) > bar_length:
        arrow = arrow[:bar_length]
    text = text.removeprefix("../cheatsheet").strip("/").strip("\\")
    sys.stdout.write(
        f"\r[{arrow:<{bar_length}}][{name:<20}][{int(progress * 100):>3}%][{x:>3}/{y:>3}] >>> {text: <100}"
    )
    sys.stdout.flush()


def get_git_diff(
    filter_func: Callable[[str], bool] = lambda p: True,
    type_func: type[str | Path] = str,
) -> Generator[str | Path, Any, None]:
    return (
        type_func(diff.a_path)
        for diff in repo.head.commit.diff(None)
        if diff.a_path.startswith(r"cheatsheet/") and filter_func(diff.a_path)
    )

