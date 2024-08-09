import os
import re
import html

import markdown
import requests
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter

from dev.data import DICT
from dev.utils import set_unselectable, print_progress_bar


formatter = HtmlFormatter(style="default")


def h_func(m: re.Match):
    h_num = m.group("h_num")
    h_content = m.group("h_content")
    h_content_id = html.escape(h_content.replace(" ", ""))
    if "<a" in h_content:
        return f'<h{h_num}>{h_content}</h{h_num}>'
    return f'<h{h_num} id="{h_content_id}">{h_content}</h{h_num}>'


def code_block_callback(match):
    code_block = match.group(2)
    language = (
        match.group(1)
        .strip("```")
        .removeprefix('<pre><code class="language-')
        .strip('">')
    )
    if "@" in language:
        language, filename = language.split("@", maxsplit=1)
    else:
        filename = ""

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

    if _language in ("python", "pycon") and (
        '<span class="o">&gt;&gt;&gt;</span> ' in highlighted_code
        or '<span class="gp">&gt;&gt;&gt; </span>' in highlighted_code
        or '<span class="o">>>></span> ' in highlighted_code
        or '<span class="gp">>>> </span>' in highlighted_code
    ):
        highlighted_code = set_unselectable(highlighted_code, "\n")

    copy_btn = """
<button class="copy-button"
        onclick="copyCode(this)">
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
""".strip()
    download_btn = (
        """
<button class="copy-button-2"
        onclick="DownloadCode(this, '{filename}')">
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
""".format(filename=filename).strip()
        if filename
        else ""
    ).strip()
    return """
<div class="code-element">
    <div class="lang-line">
        <text>{lang}</text>
        {copy_btn}
        {download_btn}
    </div>
    <div class="code">{code}</div>
</div>
""".format(
        lang=language,
        code=highlighted_code,
        copy_btn=copy_btn,
        download_btn=download_btn,
    ).strip()


def to_markup(markdown_text):
    # Регулярное выражение для поиска блоков кода
    code_block_pattern = re.compile(
        r"(?si)(```[a-z+#@._-]*|<pre><code class=\"language-[a-z+#-]*\">)"
        r"(.*?)"
        r"(```|</code></pre>)"
    )

    # Замена блоков кода на подсвеченный HTML
    highlighted_html = code_block_pattern.sub(code_block_callback, markdown_text)

    # Обработка остальной разметки
    md_extensions = [
        "markdown.extensions.tables",
        "markdown.extensions.fenced_code",
    ]
    final_html = markdown.markdown(highlighted_html, extensions=md_extensions)

    # Добавляем всем ссылкам target="_blank"
    final_html = final_html.replace('<a href="', '<a target="_blank" href="')

    # Добавляем всем тегам h тегам id с содержимым
    return re.sub(r"(?s)<h(?P<h_num>[1-6])>(?P<h_content>.+?)</h(?P=h_num)>", h_func, final_html)


def create_files_and_folders(dictionary, directory=".", x=0, y=0):
    """
    Рекурсивная функция, которая создает файлы и папки для каждого ключа-значения в словаре.

    :param dictionary: Словарь, который нужно воссоздать в виде файлов и папок
    :param directory: Директория, в которой нужно создать файлы и папки (по умолчанию - текущая директория)
    :param x:
    :param y:
    """
    for key, value in dictionary.items():
        if key.startswith("::link::"):
            continue

        key_path = os.path.join(directory, key)
        print_progress_bar(x, y, "create cheatsheets", key_path)

        if isinstance(value, str):
            key_path += ".md"

        if isinstance(value, dict):
            # Если значение - словарь, создаем папку и вызываем функцию рекурсивно
            os.makedirs(key_path, exist_ok=True)
            x = create_files_and_folders(value, key_path, x, y)
        else:
            x += 1
            # Если значение - строка, создаем файл с содержимым строки
            with open(key_path, "w", encoding="utf-8") as f:
                f.write(to_markup(value.strip()))

    return x


def create_files(cheatsheet_count: int):
    create_files_and_folders(DICT, "../cheatsheet", y=cheatsheet_count - 1)

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


def create_file(keys: tuple[str]):
    filepath = f"cheatsheet\\" + "\\".join(keys) + ".md"
    os.makedirs(filepath.rsplit("\\", maxsplit=1)[0], exist_ok=True)
    value = DICT
    for key in keys:
        value = value[key]

    with open(filepath, "w", encoding="utf-8") as file:
        file.write(to_markup(value.strip()))
