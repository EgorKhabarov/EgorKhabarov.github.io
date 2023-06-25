import os
from data import DICT
index = 0

def buttons(dictionary: dict, directory=""):
    text = ""
    for key, value in dictionary.items():
        title = key
        key_path = os.path.join(directory, key)

        for i in ("\\", "/", "(", ")", "=", ",", ".", "-", "#", " ", "+"): key = key.replace(i, "")
        key = key.split(maxsplit=1)[0]

        if isinstance(value, dict):
            # Если значение - словарь, создаем папку и вызываем функцию рекурсивно
            # os.makedirs(key_path, exist_ok=True)
            # create_files_and_folders(value, directory=key_path)
            global index
            index += 1

            val = buttons(value, key_path)[0]
            text += """    <button onclick="showText({name});" class="button">{title}</button>
    <div id="{name}" style="display:none;" class="button-folder">
{text}
</div>
""".format(name=f"{key}{index}", title="📂&nbsp;" + title.replace(" ", "&nbsp;"), text=val, url=title)
            # //window.location.href = '{url}';
        else:
            print(key_path)
            text += """<button onclick="GET('cheatsheet/{name}');" class="button">{title}</button>\n""".format(
                name=key_path.replace("\\", "&#x2f;") + ".md",
                title="📄&nbsp;" + title.replace(" ", "&nbsp;")
            )
    return text, directory

with open("cheatsheet/style.css", "r", encoding="utf-8") as file:
    css_code = file.read()

with open("cheatsheet/script.js", "r", encoding="utf-8") as file:
    js_code = file.read()

result = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <link rel="icon" type="image/png" href="http://s1.iconbird.com/ico/2013/12/505/w450h4001385925290Contact.png">
    <title>Шпаргалка</title>
    <style>
        {css_code}
    </style>
    <script>
        {js_code}
    </script>
</head>
<body>
    <div class="cheatsheet-buttons">
        {buttons(DICT)[0]}
    </div>

    <pre id="field" class="cheatsheet-field">Нажмите на кнопку с темой, чтобы увидеть здесь объяснение</pre>

    <div>
        <button id="FontSizeSize" class="control-button" style="padding-left: 12px;">12px</button>
        <button onclick="changeFontSize(field, '+')" class="control-button" style="padding-left: 25px;">+</button>
        <button onclick="changeFontSize(field, '-')" class="control-button"  style="padding-left: 27px;">-</button>
        <button onclick="changeFontSize(field, '=')" class="control-button">Default</button>
        <button id="COPY" onclick="copyTextFromDiv(field); changeColor(COPY)" class="control-button" style="padding-left: 12px;">Copy</button>
        <button id="COPY2" onclick="copyTextFromDiv2(); changeColor(COPY2)" class="control-button" style="padding-left: 2px;">Copy selected</button>
    </div>
</body>
</html>
"""

with open("cheatsheet/index.html", "w", encoding="utf-8") as file:
    file.write(result)
