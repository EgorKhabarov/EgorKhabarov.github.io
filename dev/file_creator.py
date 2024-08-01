import os
import re

import markdown
import requests
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter

from dev.data import DICT
from dev.html_generator import get_id
from dev.utils import set_unselectable, r, print_progress_bar


cheatsheet_count = r(DICT)
formatter = HtmlFormatter(style="default")


def code_block_callback(match):
    code_block = match.group(2)
    language = (
        match.group(1)
        .strip("```")
        .removeprefix('<pre><code class="language-')
        .strip('">')
    )

    if language == "":
        _language, language = "text", "text"
    elif language == "regexp":
        _language = "text"
    elif language == "csv":
        _language = "python"
    elif language == "python-console":
        _language = "pycon"
    else:
        _language = language

    lexer = get_lexer_by_name(_language, stripall=True)

    highlighted_code = highlight(code_block, lexer, formatter).strip()

    if (
        _language in ("python", "pycon")
        and (
            '<span class="o">&gt;&gt;&gt;</span> ' in highlighted_code
            or '<span class="gp">&gt;&gt;&gt; </span>' in highlighted_code
            or '<span class="o">>>></span> ' in highlighted_code
            or '<span class="gp">>>> </span>' in highlighted_code
        )
    ):
        highlighted_code = set_unselectable(highlighted_code, "\n")

    code_id = get_id(language+highlighted_code, True)
    btn = (
        """
<button class="copy-button-2"
        id="code{code_id}_2b"
        onclick="DownloadCode(code{code_id}, code{code_id}_2b, '{code_block}')">
    <svg stroke="currentColor"
         fill="none"
         stroke-width="2"
         viewBox="0 0 24 24"
         stroke-linecap="round"
         stroke-linejoin="round"
         class="h-4 w-4"
         height="1em"
         width="1em"
         xmlns="http://www.w3.org/2000/svg">
      <path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path>
      <rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect>
    </svg>
    <text>Download code</text>
  </button>
""".format(
            code_id=code_id,
            code_block=code_block.strip().splitlines()[0].removeprefix("#file ")
        ).strip()
        if code_block.strip().startswith("#file ")
        else ""
    )
    return """
<div class="code-element">
<div class="lang-line">
  <text>{lang}</text>
  <button class="copy-button"
          id="code{index}b"
          onclick="copyCode(code{index}, code{index}b)">
    <svg stroke="currentColor"
         fill="none"
         stroke-width="2"
         viewBox="0 0 24 24"
         stroke-linecap="round"
         stroke-linejoin="round"
         class="h-4 w-4"
         height="1em"
         width="1em"
         xmlns="http://www.w3.org/2000/svg">
      <path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path>
      <rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect>
    </svg>
    <text>Copy code</text>
  </button>
  {btn}
</div>
<div class="code" id="code{index}">{code}</div>
</div>
""".strip().format(
        lang=language,
        code=highlighted_code,
        index=code_id,
        btn=btn,
    )


def url_shortener(url):
    url = url[0]

    if url == "http://www.w3.org/2000/svg":
        return url

    return f"<a href='{url}' target='_blank'>{url}</a>"


def to_markup(markdown_text):
    # r"(http?s?://\S+)"
    markdown_text = re.sub(
        r"((?:http|https|\w+)://[^\"\'\n ]+)", url_shortener, markdown_text
    )

    # Регулярное выражение для поиска блоков кода
    code_block_pattern = re.compile(
        r"(?si)(```[a-z+#-]*|<pre><code class=\"language-[a-z+#-]*\">)"
        r"(.*?)"
        r"(```|</code></pre>)"
    )

    # Замена блоков кода на подсвеченный HTML
    highlighted_html = code_block_pattern.sub(code_block_callback, markdown_text)

    # Обработка остальной разметки
    md_extensions = [
        "markdown.extensions.tables",
        "markdown.extensions.fenced_code",
        "markdown.extensions.codehilite",
    ]
    final_html = markdown.markdown(highlighted_html, extensions=md_extensions)

    return final_html


def create_files_and_folders(dictionary, directory=".", x=0, y=cheatsheet_count-1):
    """
    Рекурсивная функция, которая создает файлы и папки для каждого ключа-значения в словаре.

    :param dictionary: Словарь, который нужно воссоздать в виде файлов и папок
    :param directory: Директория, в которой нужно создать файлы и папки (по умолчанию - текущая директория)
    :param x:
    :param y:
    """
    for key, value in dictionary.items():
        key_path = os.path.join(directory, key)
        print_progress_bar(x, y, "create_files_and_folders", key_path)

        if isinstance(value, str):
            key_path += ".md"

        if isinstance(value, dict):
            # Если значение - словарь, создаем папку и вызываем функцию рекурсивно
            os.makedirs(key_path, exist_ok=True)
            x = create_files_and_folders(value, key_path, x)
        else:
            x += 1
            # Если значение - строка, создаем файл с содержимым строки
            with open(key_path, "w", encoding="utf-8") as f:
                f.write(to_markup(value.strip()))

    return x


def create_files():
    create_files_and_folders(DICT, "../cheatsheet")

    content = requests.get(
        f"https://img.shields.io/badge/{cheatsheet_count}%20cheatsheet-brightgreen",
        {
            "style": "flat",
            "logo": "github",
            "label": "GitHub Pages",
        },
    ).content.decode()

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
