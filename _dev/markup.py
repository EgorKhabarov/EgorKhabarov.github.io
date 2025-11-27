import re

import markdown
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter
from pygments.util import ClassNotFound

from _dev.utils import set_unselectable


formatter = HtmlFormatter(style="default")


def code_block_callback(match: re.Match) -> str:
    code_block, language = match["code"], match["md_lang"] or match["pre_lang"] or ""
    code_block = (
        code_block.replace("<mark>", "==")
        .replace('<mark style="">', "==")
        .replace("</mark>", "==")
    )
    if "@" in language:
        language, filename = language.split("@", maxsplit=1)
        language = language.strip()
        filename = filename.strip()
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

    regex_comma_color_span = re.compile(r'<span class="p">,</span>')

    highlighted_code = regex_comma_color_span.sub(lambda m: '<span class="k">,</span>', highlighted_code)
    highlighted_code = highlighted_code.replace("`", "&#x60;")

    copy_svg = '<svg width="1.2em" height="1.2em" viewBox="0 0 24 24"><use href="#copy_code_svg"/></svg>'
    download_svg = '<svg width="1.2em" height="1.2em" viewBox="0 0 24 24"><use href="#download_code_svg"/></svg>'

    copy_btn = f'<button class="copy_code_button" onclick="CopyCode(this)">{copy_svg}<text class="unselectable">Copy code</text></button>'
    download_btn = (
        f'<button class="download_code_button" onclick="DownloadCode(this, `{filename}`)">{download_svg}<text class="unselectable" title="{filename}">Download code</text></button>'
        if filename
        else ""
    )
    return f'<div class="code_element"><div class="lang_line"><text>{language}</text>{copy_btn}{download_btn}</div><div class="code language-{_language}">{highlighted_code}</div></div>'


def wikilink_func(match: re.Match) -> str:
    path = match.group(1)
    if path.endswith("/"):
        cheatsheet_name = path.strip("/").rsplit("/", 1)[-1]
    else:
        cheatsheet_name = path.rsplit("/", 1)[-1].removesuffix(".md")
    cheatsheet_name = cheatsheet_name.replace("%20", " ")
    return f'<a target="_self" href="?{path}" class="wikilink">{cheatsheet_name}</a>'


def to_markup(markdown_text: str):
    # WikiLinks
    highlighted_html = re.sub(
        r"\[\[([^\n\]]+)]]",
        wikilink_func,
        markdown_text,
    )
    # <mark>
    highlighted_html = re.sub(
        r"==(?:\{(?P<style>.*?)})?(?P<mark>[^=\n]+?)==",
        lambda m: f'<mark style="{m["style"] or ""}">{m["mark"]}</mark>',
        highlighted_html,
    )
    # Замена блоков кода на подсвеченный HTML
    highlighted_html = re.sub(
        r"(?si)((`{3,})(?P<md_lang>[a-z+#@._\d -]*)|<pre><code class=\"language-(?P<pre_lang>[a-z+# -]*)\">)"
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
