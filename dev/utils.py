import sys

from pygments import highlight
from pygments.formatters.html import HtmlFormatter
from pygments.lexers import get_lexer_by_name


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


def r(d: dict, c: int = 0) -> int:
    for k, v in d.items():
        if isinstance(v, dict):
            c = r(v, c)
        else:
            c += 1
    return c


def print_progress_bar(x: int, y: int, name: str, text: str = None):
    bar_length = 50
    progress = x / y
    arrow = "█" * int(progress * bar_length)
    spaces = " " * (bar_length - len(arrow))
    text = text.removeprefix("../cheatsheet").strip("/").strip("\\")
    sys.stdout.write(
        f"\r[{arrow}{spaces}][{name:<24}][{int(progress * 100):>3}%] >>> {text: <100}"
    )
    sys.stdout.flush()
