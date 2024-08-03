import sys

from pygments import highlight
from pygments.formatters.html import HtmlFormatter
from pygments.lexers import get_lexer_by_name



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


def escape_markdown(content: str) -> str:
    # parse = re.sub(r"([_*\[\]()~`>\#\+\-=|\.!])", r"\\\1", content)
    # reparse = re.sub(r"\\\\([_*\[\]()~`>\#\+\-=|\.!])", r"\1", parse)
    # return reparse
    return content.replace("__", "&#95;&#95;")


def set_unselectable(text: str, sep: str = "\n"):
    lines = []

    for line in text.split(sep):
        if line.startswith("</pre></div>"):
            lines.append(line)
            continue

        if line.startswith(
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

    return sep.join(lines)


def to_table_code(lang: str, code: str):
    formatter = HtmlFormatter(style="default")
    lexer = get_lexer_by_name(lang, stripall=True)
    highlighted_code = highlight(code, lexer, formatter).strip().replace("\n", "<br>")

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


def to_table_code_py(code: str) -> str:
    return to_table_code("python", code)


def to_table_code_java(code: str) -> str:
    return to_table_code("java", code)


def check_dict_keys(d: dict, c: int = 0) -> bool | int:
    for k, v in d.items():
        print_progress_bar(c, 0, "counting cheatsheets", k)
        if (
            (not k)
            or k == "."
            or "\x00" in k
            or set(k) & set("\\/:*?'\"<>|")
            or k in reserved_filenames
        ):
            return False
        if isinstance(v, dict):
            res = check_dict_keys(v, c)
            if res is False:
                return False
            c = res
        else:
            c += 1
    return c


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
        f"\r[{arrow:<{bar_length}}][{name:<21}][{int(progress * 100):>3}%] >>> {text: <100}"
    )
    sys.stdout.flush()
