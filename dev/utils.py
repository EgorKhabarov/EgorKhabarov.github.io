from pygments import highlight
from pygments.formatters.html import HtmlFormatter
from pygments.lexers import get_lexer_by_name


def escape_markdown(content: str) -> str:
    # parse = re.sub(r"([_*\[\]()~`>\#\+\-=|\.!])", r"\\\1", content)
    # reparse = re.sub(r"\\\\([_*\[\]()~`>\#\+\-=|\.!])", r"\1", parse)
    # return reparse
    return content.replace("__", "&#95;&#95;")


def set_unselectable(text: str, sep: str = "\n"):
    l = []

    for line in text.split(sep):
        if line.startswith('<div class="highlight"><pre><span></span><span class="o">&gt;&gt;&gt;</span> '):
            line = (
                '<div class="highlight"><pre><span></span>'
                '<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span>'
            ) + line.removeprefix(
                '<div class="highlight"><pre><span></span><span class="o">&gt;&gt;&gt;</span> '
            )
        elif line.startswith('<span class="o">&gt;&gt;&gt;</span> '):
            line = '<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span>' + line.removeprefix(
                '<span class="o">&gt;&gt;&gt;</span> ')
        elif line.startswith('<div class="highlight"><pre><span></span><span class="o">...</span> '):
            line = (
                '<div class="highlight"><pre><span></span>'
                '<span class="unselectable"><span class="o">...</span> </span>'
            ) + line.removeprefix(
                '<div class="highlight"><pre><span></span><span class="o">...</span> '
            )
        elif line.startswith('<span class="o">...</span> '):
            line = '<span class="unselectable"><span class="o">...</span> </span>' + line.removeprefix(
                '<span class="o">...</span> ')
        else:
            line = f'<span class="unselectable">{line}</span>'

        l.append(line)

    return sep.join(l)


def to_table_code_py(code_block: str) -> str:
    lang = "python"
    code_block = code_block  # html.escape(code_block).replace("\n", "<br>")
    formatter = HtmlFormatter(style="default")
    lexer = get_lexer_by_name(lang, stripall=True)
    highlighted_code = (
        highlight(code_block, lexer, formatter).strip().replace("\n", "<br>")
    )

    if (
        lang == "python"
        and '<span class="o">&gt;&gt;&gt;</span> ' in highlighted_code
    ):
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
