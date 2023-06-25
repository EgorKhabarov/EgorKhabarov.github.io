import os

from bs4 import BeautifulSoup

from data import DICT


index = 0

def buttons(dictionary: dict, directory=""):
    text = ""
    for key, value in dictionary.items():
        title = key
        key_path = os.path.join(directory, key)

        for i in ("\\", "/", "(", ")", "=", ",", ".", "-", "#", " ", "+"):
            key = key.replace(i, "")

        key = key.split(maxsplit=1)[0]

        if isinstance(value, dict):
            global index
            index += 1

            val = buttons(value, key_path)[0]
            text += """<button onclick="showText({name});" class="button">{title}</button>
<div id="{name}" style="display:none;" class="button-folder">{text}</div>""".format(
                name=f"{key}{index}",
                title="📂&nbsp;" + title.replace(" ", "&nbsp;"),
                text=val,
                url=title)
        else:
            # print(key_path)
            text += """<button onclick="GET('{name}');" class="button">{title}</button>\n""".format(
                name=key_path.replace("\\", "&#x2f;") + ".md",
                title="📄&nbsp;" + title.replace(" ", "&nbsp;")
            )
    return text, directory

with (open("cheatsheet/style.css", "r", encoding="utf-8") as style,
      open("cheatsheet/script.js", "r", encoding="utf-8") as script):
    css_code = style.read().strip()
    js_code = script.read().strip()

result = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <link rel="icon" type="image/png" href="icon.png">
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
        <!-- <button class="control-button" onclick="togglePopup()">
            <svg viewBox="0 0 24 24" preserveAspectRatio="xMidYMid meet" focusable="false" class="style-scope yt-icon" style="pointer-events: none; display: block; width: 100%; height: 100%;">
                <g class="style-scope yt-icon">
                    <path d="M20.87,20.17l-5.59-5.59C16.35,13.35,17,11.75,17,10c0-3.87-3.13-7-7-7s-7,3.13-7,7s3.13,7,7,7c1.75,0,3.35-0.65,4.58-1.71 l5.59,5.59L20.87,20.17z M10,16c-3.31,0-6-2.69-6-6s2.69-6,6-6s6,2.69,6,6S13.31,16,10,16z" class="style-scope yt-icon"></path>
                </g>
            </svg>
        </button> ->
    </div>
    <!-- <div id="popupElement" class="popup-container" style="display: none;background-color: #3c3f41;">
        <form onsubmit="handleSearch(event)" style="width: 270px;">
            <input type="text" id="searchInput" maxlength="50" style="background-color: #525252;color: #AFB1B3;">
            <button type="submit" style="background-color: #525252;color: #AFB1B3;">Поиск</button>
        </form>
        <span class="close-button" onclick="togglePopup()" style="z-index: 8;">❌</span>
        <div class="search-list"></div>
    </div> -->
</body>
</html>
"""

with open("cheatsheet/index.html", "w", encoding="utf-8") as file:
    file.write(BeautifulSoup(result, "html.parser").prettify())
