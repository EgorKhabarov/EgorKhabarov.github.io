import os
import re

import markdown
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter

from data import DICT


index = 0

def url_shortener(url):
    return (
        lambda url_: url_ if url_ == "http://www.w3.org/2000/svg" else f"<a href='{url_}' target='_blank'>{url_}</a>"
    )(url[0])

def to_markup(markdown_text):
    markdown_text = re.sub(r"(http?s?://[^\"\'\n ]+)", url_shortener, markdown_text) # r"(http?s?://\S+)"

    # Регулярное выражение для поиска блоков кода
    code_block_pattern = re.compile(r'(```[a-z+#-]*|<pre><code class="language-[a-z+#-]*">)(.*?)(```|</code></pre>)',
                                    re.DOTALL | re.IGNORECASE)

    # Форматтер Pygments
    formatter = HtmlFormatter(style='default')

    def code_block_callback(match):
        code_block = match.group(2)
        language = match.group(1).strip('```').removeprefix('<pre><code class="language-').strip('">')

        if language == "":
            _language, language = "text", "text"
        elif language == "regexp":
            _language = "text"
        elif language == "csv":
            _language = "python"
        elif language == "python-console":
            _language = "python"
        # elif language == "row":
        #     return """<div class="row">{}</div>""".format(code_block.strip())
        else:
            _language = language
        lexer = get_lexer_by_name(_language, stripall=True)

        highlighted_code = highlight(code_block, lexer, formatter)

        global index
        index += 1

        return "".join(line.strip() for line in """
<div class="code-element">
    <div class="lang-line">
      <text>{lang}</text>
      <button class="copy-button" id="code{index}b" onclick="copyCode(code{index}, code{index}b)">
        <svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg">
          <path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path>
          <rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect>
        </svg>
        <text>Copy code</text>
      </button>
    </div>
    <div class="code" id="code{index}">{code}</div>
</div>
        """.strip().splitlines()).format(lang=language, code=highlighted_code.strip(), index=index)

    # Замена блоков кода на подсвеченный HTML
    highlighted_html = code_block_pattern.sub(code_block_callback, markdown_text)

    # Обработка остальной разметки
    md_extensions = ['markdown.extensions.tables']
    final_html = markdown.markdown(highlighted_html, extensions=md_extensions)

    return final_html

def create_files_and_folders(dictionary, directory="."):
    """
    Рекурсивная функция, которая создает файлы и папки для каждого ключа-значения в словаре.

    :param dictionary: словарь, который нужно воссоздать в виде файлов и папок
    :param directory: директория, в которой нужно создать файлы и папки (по умолчанию - текущая директория)
    """
    for key, value in dictionary.items():
        if isinstance(value, str): key += ".md"
        key_path = os.path.join(directory, key)

        if isinstance(value, dict):
            # Если значение - словарь, создаем папку и вызываем функцию рекурсивно
            os.makedirs(key_path, exist_ok=True)
            create_files_and_folders(value, directory=key_path)
        else:
            # Если значение - строка, создаем файл с содержимым строки
            with open(key_path, "w", encoding="utf-8") as f:
                f.write(to_markup(value.strip()))

create_files_and_folders(DICT, "cheatsheet")
