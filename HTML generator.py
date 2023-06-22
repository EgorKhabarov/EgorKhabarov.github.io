import os
from data import DICT

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

            val = buttons(value, key_path)[0]
            text += """    <button onclick="
showText({name});
//window.location.href = '{url}';
" class="trigger">{title}</button>
    <div id="{name}" style="display:none;" class="button-field">
{text}
</div>
""".format(name=key, title="📂&nbsp;" + title.replace(" ", "&nbsp;"), text=val, url=title)
        else:
            # Если значение - строка, создаем файл с содержимым строки
            # with open(key_path, "w", encoding="utf-8") as f:
            #     f.write(value.strip())
            print(key_path)
            text += """<button onclick="
                PutHtmlText(getCheatSheat('{name}'));
            " class="trigger">{title}</button>""".format(
                name=key_path.replace("\\", "&#x2f;") + ".txt",
                title="📄&nbsp;" + title.replace(" ", "&nbsp;")
            )
    return text, directory

css_code = """

/*Закругления у таблиц*/
th:first-child {border-top-left-radius: .375rem;}
th:last-child {border-top-right-radius: .375rem;}
tr:last-child td:first-child {border-bottom-left-radius: .375rem;}
tr:last-child td:last-child {border-bottom-right-radius: .375rem;}

th {
  /*font-weight: normal;*/
  padding: 10px 15px;
  background-color: #46494b;
}
td {
  border-top: 1px solid #46494b;
  padding: 10px 15px;
  background-color: #3c3f41;
}
tr:hover td {
  background: #46494b;
}

// Цвета ссылок
a:link    {color: #539bf5;}
a:active  {color: #6ba4e9;}
a:visited {color: #539bf5;}

::-webkit-scrollbar {
    width: 8px;
    height: 8px;
    background-color: #393939;
}
::-webkit-scrollbar-thumb {
    border-radius: 10px;
    background-color: #505050;
}


body {
    background: #393939;
    color: #F1F1F1;
    margin: 0px;
    padding: 20px;
    display: flex;
    flex-direction: row;
    border: 0px solid;
    border-radius: 10px;
    max-height: 94vh;
}
.div-column {
    display: flex;
    flex-direction: row;
    border: 0px solid;
    border-radius: 10px;
    height: 84vh;
    width: 300px; //max-content;
    background-color: #191919;
    padding: 20px;
    flex-direction: column;
    overflow-y: auto;
}
.trigger {
    //max-
    width: 350px;
    font-size: 1em;
    display: flex;
    align-items: center;
    margin: 8px 0;
    padding: 0 20px;
    padding-left: 10px;
    min-height: 45px;
    border: 1px solid #2B2B2B;// #000000;
    border-radius: 10px;
    background-color: #323232;//#C0C0C0;
    color: #AFB1B3;//#C0C0C0;//#212121;
    transition: background-color 0.2s ease-out;
}
.trigger:hover {
    background-color: #424242;
}
.trigger:active {
    background-color: #525252;
}
.trigger:focus {
    background-color: #999999;
    color: #252525;
}
.code-str-2 {
    display: flex;
    //max-height: 860px;
    //max-height: 100vh;
    height: 84vh;
    width: 100%;
    border: 0px solid;
    padding: 20px;
    border-radius: 10px;
    background-color: #2B2B2B;
    color: #AAAAAA;
    font-size: 12px;
    margin: 0px 0px 0px 0px;
    overflow-y: auto;
    flex-direction: column;

    //background-color: #3c3f41;
    //color: #bbbbbb;
}
.code-in-code {
    display: flex;
    //height: max-content;
    flex-direction: column;
    width: max-content; // 550px;
    // padding: 10px;
    // // //color: #AAAAAA;
    // background-color: #1B1B1B;
    // // border: 0px solid;
    // // border-radius: 5px;
    // // flex-direction: row;
    // // padding:1rem 1rem 1rem 1rem;
    // // //overflow-y:auto;
    // // white-space:pre-wrap!important;
    // // //background-color: #1B1B1B;
    // border-radius:.0rem .0rem .375rem .375rem;
    --tw-bg-opacity:1;background-color:rgba(0,0,0,var(--tw-bg-opacity));
    margin-bottom:1rem;
    border-radius:.375rem;
}
.copy-code-in-code {
    background-color: #5A5A5A;
    border: 0px solid;
    border-radius: 5px;
    color: #AAAAAA;
    //margin-right: 99%;
    font-size: 10px;
    width: max-content;
    max-height: 25px;
    transform: rotate(0deg);
}
.copy-code-in-code:hover {background-color: #ffffff;}
.button-field {
    //min-height: 24px;
    height: max-content;
    //min-width: 70px;
    width: 0px; //initial; //max-content;
    border: 0px solid;
    border-radius: 10px;
    padding-left: 10px;
    background-color: #505050; //#AFB1B3; //#343434;
    color: #AAAAAA;
    margin: -3px 0px 8px 2px;
}
.MB {
    height: 64px;
    width: 64px;
    font-size: 1em;
    display: flex;
    align-items: center;
    margin: 0px 0px 4px 8px;

    min-height: 45px;
    border: 1px solid #2B2B2B;
    border-radius: 10px;
    background-color: #525252;
    color: #AFB1B3;
    transition: background-color 0.5s ease-out;
}
.MB:hover {background-color: #424242;}
.MB:active {background-color: #323232;}


.highlight-code         {color:#A9B7C6;}
.highlight-keyword      {color:#CC7832;}
.highlight-arg          {color:#AA4926;}
.highlight-digit        {color:#5897BB;}
.highlight-default-func {color:#8888C6;}

.highlight-func         {color:#FFC66D;}
.highlight-decorator    {color:#BBB529;}
.highlight-definition   {color:#B200B2;}
.highlight-self         {color:#94558D;}
.highlight-comment      {color:hsla(0,0%,100%,.5)}
.highlight-comment span {color:hsla(0,0%,100%,.5)!important;}
.highlight-comment span1 {color:hsla(0,0%,100%,.5)!important;}


.highlight-text         {color:#529755!important;}.highlight-text span {color:#529755!important;}
.highlight-binary-text  {color:#A5C261;}.highlight-binary-text span {color:#A5C261!important;}





.code-in-code {
    --tw-bg-opacity:1;background-color:rgba(0,0,0,var(--tw-bg-opacity));
    margin-bottom:1rem;
    border-radius:.375rem;
}
.top-line {
    height: max-content;
    //height: 15px; // max-content;
    border-radius:.375rem .375rem .0rem .0rem;
    display:flex;
    align-items:center;
    position:relative;
    tw-text-opacity:1;color:rgba(217,217,227,var(--tw-text-opacity));
    tw-bg-opacity:1;background-color:rgba(52,53,65,var(--tw-bg-opacity));
    padding-left:1rem;padding-right:1rem;
    padding-bottom:.35rem;padding-top:.35rem;
    font-size:.75rem;line-height:.75rem;
    font-family:Söhne,ui-sans-serif,system-ui,-apple-system,Segoe UI,Roboto,Ubuntu,Cantarell,Noto Sans,sans-serif,Helvetica Neue,Arial,Apple Color Emoji,Segoe UI Emoji,Segoe UI Symbol,Noto Color Emoji;
}
.top-button {
    display:flex;
    margin-left:auto;
    gap:.5rem;
    background-color:rgba(52,53,65);border:0;color:#D9D9E3;
}
.top-button:hover {background-color: #424242;}
.top-button:active {background-color: #323232;}
.code-line {
    padding:1rem 1rem 1rem 1rem;
    overflow-y:auto;
    white-space:pre-wrap!important;
    background-color: #1B1B1B;
    border-radius:.0rem .0rem .375rem .375rem;

    background-color: #272727;
}



"""
js_code = """
function showText(element) {
    if (element.style.display == "none") {
        element.style.display = "block";
    } else {element.style.display = "none";}}

function showButton(element) {
    if (element.style.display == "none") {
        element.style.display = "block";
    } else {element.style.display = "none";}}

function PutText(text) {
    //let text = element.innerText;
    let FieldElement = document.getElementById("field");
    if (typeof FieldElement.innerText != 'undefined') {
        FieldElement.innerText = text; // IE8-
    } else {FieldElement.textContent = text; // Нормальные браузеры
    }
    document.getElementById('field').scrollTo(999999, document.getElementById('field').scrollHeight);
    }

function PutHtmlText(html) {
    //let html = element.innerHTML;

    let FieldElement = document.getElementById("field");

    //if (typeof FieldElement.innerText != 'undefined') {

    FieldElement.innerHTML = html; // IE8-

    //} else {
    //    FieldElement.textContent = html; // Нормальные браузеры
    //}
    document.getElementById('field').scrollTo(0, 0);


    replaceCodeElement()
    }

function changeFontSizePlus(element) {
    let currentSize = parseFloat(getComputedStyle(element).fontSize);
    element.style.fontSize = (currentSize + 2) + "px";
    ok()}

function changeFontSizeMinus(element) {
    let currentSize = parseFloat(getComputedStyle(element).fontSize);
    element.style.fontSize = (currentSize - 2) + "px";
    ok()}

function changeFontSizeDefault(element) {
    let currentSize = parseFloat(getComputedStyle(element).fontSize);
    element.style.fontSize = 12 + "px";
    ok()}

function ok() {
    let currentSize = parseFloat(getComputedStyle(field).fontSize);
    let FontSizeElement = document.getElementById("FontSizeSize");
    if (typeof FontSizeElement.innerText != 'undefined') {
        FontSizeElement.innerText = (currentSize) + "px"; // IE8-
    } else {FontSizeElement.textContent = (currentSize) + "px"; // Нормальные браузеры
    }
}
function copyTextFromDiv(element) {
    var text = element.innerText;
    console.log(text);
    //copyTextToClipboard(text);
    var textArea = document.createElement("textarea");
    textArea.value = text;
    document.body.appendChild(textArea);
    textArea.select();
    document.execCommand("copy");
    textArea.remove();
    //alert("Copied the text: " + text);
}
function copyTextFromDiv3(element) {
    //var text = element.innerHTML;
    var text = document.getElementById(element).innerText.slice(0, -9);
    console.log(text);
    var textArea = document.createElement("textarea");
    textArea.value = text;
    document.body.appendChild(textArea);
    textArea.select();
    document.execCommand("copy");
    textArea.remove();
}
function changeColor(element) {
    element.style.backgroundColor = "#008000";
    setTimeout(function() {element.style.backgroundColor = "#525252";}, 2000);
}
function copyTextFromDiv2() {
    document.execCommand('copy');
}





function addTextToURL(inputText) {
    var currentURL = window.location.href;

    if (currentURL.indexOf('?') !== -1) {
        // Удаляем все параметры после '?'
        currentURL = currentURL.substring(0, currentURL.indexOf('?'));
    }

    var newURL = currentURL + '?path=' + encodeURIComponent(inputText);
    history.replaceState({}, document.title, newURL);
}

function getTextFromURL() {
    var urlParams = new URLSearchParams(window.location.search);
    var pathParam = urlParams.get('path');
    console.log(pathParam);
}

function getCheatSheat(url) {
    var xhr = new XMLHttpRequest();
    xhr.open("GET", url, false); // Используется синхронный запрос
    xhr.send();
    if (xhr.status === 200) {
        return xhr.responseText;
    } else {
        return "";
    }
}




function re12placeCodeElement() {
  // Находим элемент <pre> с указанным идентификатором
  var preElement = document.getElementById("field");

  // Получаем содержимое <code> внутри <pre>
  var codeContent = preElement.querySelector("code").innerText;

  // Получаем язык из класса <code> (например, "language-python")
  var lang = preElement.querySelector("code").className.split("-")[1];

  // Создаем новый элемент <div> с классами и заменяемыми значениями
  var newCodeElement = document.createElement("div");
  newCodeElement.className = "code-in-code";
  newCodeElement.innerHTML = `
<div class="code-in-code">
    <div class="top-line">${lang}<button class="top-button"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg">
    <path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button>
    </div>
    <div class="code-line">
        <div class="language-python; highlight-code">${codeContent}</div>
    </div>
</div>
  `;

  // Заменяем элемент <pre> на новый элемент <div>
  preElement.parentNode.replaceChild(newCodeElement, preElement);
}












function replaceCodeElements() {
  // Находим элемент <pre> с указанным идентификатором
  var preElement = document.getElementById("field");

  // Получаем все элементы <pre><code> внутри <pre id="field">
  var codeElements = preElement.querySelectorAll("pre");

  // Проходимся по каждому элементу <pre><code> и заменяем его содержимое
  codeElements.forEach(function(codeElement) {
    // Получаем содержимое <code>
    var codeContent = codeElement.innerText;

    // Получаем язык из класса <code> (например, "language-python")
    var lang = codeElement.className.split("-")[1];

    // Создаем новый элемент <div> с классами и заменяемыми значениями
    var newCodeElement = document.createElement("div");
    newCodeElement.className = "code-in-code";
    newCodeElement.innerHTML = `
<div class="code-in-code">
    <div class="top-line">${lang}<button class="top-button"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg">
    <path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button>
    </div>
    <div class="code-line">
        <div class="language-python; highlight-code">${codeContent}</div>
    </div>
</div>
    `;

    // Заменяем элемент <pre><code> на новый элемент <div>
    codeElement.parentNode.parentNode.replaceChild(newCodeElement, codeElement.parentNode);
  });
}
"""

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
    <div class="div-column">
        {buttons(DICT)[0]}
    </div>

    <pre id="field" class="code-str-2">Нажмите на кнопку с темой, чтобы увидеть здесь объяснение</pre>

    <div class="div-column-1">
        <button id="FontSizeSize" class="MB" style="padding-left: 12px;">12px</button>
        <button onclick="changeFontSizePlus(field)" class="MB" style="padding-left: 25px;">+</button>
        <button onclick="changeFontSizeMinus(field)" class="MB"  style="padding-left: 27px;">-</button>
        <button onclick="changeFontSizeDefault(field)" class="MB">Default</button>
        <button id="COPY" onclick="copyTextFromDiv(field); changeColor(COPY)" class="MB" style="padding-left: 12px;">Copy</button>
        <button id="COPY2" onclick="copyTextFromDiv2(); changeColor(COPY2)" class="MB" style="padding-left: 2px;">Copy selected</button>
    </div>
</body>
</html>
"""

with open("cheatsheet/index.html", "w", encoding="utf-8") as file:
    file.write(result)
