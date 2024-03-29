
/* Скрыть / показать папку */
function showText(element) {
    if (element.style.display == "none") {
        element.style.display = "block";
    } else {
        element.style.display = "none";
    }
}


/* Изменение размера шрифта */
function changeFontSize(element, action) {
    let currentSize = parseFloat(getComputedStyle(element).fontSize);

    if (action === "+") {
        element.style.fontSize = (currentSize + 2) + "px";
        currentSize += 2
    } else if (action === "-") {
        element.style.fontSize = (currentSize - 2) + "px";
        currentSize -= 2
    } else if (action === "=") {
        element.style.fontSize = 12 + "px";
        currentSize = 12
    }

    let FontSizeElement = document.getElementById("FontSizeSize");

    if (typeof FontSizeElement.innerText != 'undefined') {
        FontSizeElement.innerText = currentSize + "px"; // IE8-
    } else {
        FontSizeElement.textContent = currentSize + "px"; // Нормальные браузеры
    }
}


/* Копирование всего текста */
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

/*Копировать выделенный текст*/
function copyTextFromDiv2() {
    document.execCommand('copy');
}

/*Изменить цвет кнопки*/
function changeColor(element) {
    element.style.backgroundColor = "#008000";
    setTimeout(function() {element.style.backgroundColor = "#525252";}, 2000);
}


/*Взять нужную шпаргалку по пути*/
function PutHtmlText(html) {
    if (html != "") {
        let FieldElement = document.getElementById("field");

        if (typeof FieldElement.innerText != 'undefined') {
            FieldElement.innerHTML = html; // IE8-
        } else {
            FieldElement.textContent = html; // Нормальные браузеры
        }
        document.getElementById('field').scrollTo(0, 0);
    }
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

function GET(url) {
    console.log(url)
    return PutHtmlText(getCheatSheat(url))
}


/* Для обработки консольного кода */
function processPythonConsoleText(text) {
  const lines = text.split('\n');
  const userInputLines = [];

  for (let i = 0; i < lines.length; i++) {
    const line = lines[i].trim();

    if (line.startsWith('>>> ') || line.startsWith('... ')) {
      userInputLines.push(line.slice(4));
    } else if (line !== '') {
      userInputLines.push('\n');
    }
  }

  return userInputLines.join('');
}

function copyCode(element, elementButton) {
    const textarea = document.createElement('textarea');
    textarea.value = element.textContent;
    document.body.appendChild(textarea);
    textarea.select();
    document.execCommand('copy');
    document.body.removeChild(textarea);

    let svg1 = '<svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" ';
    let svg2 = 'stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg">';
    let svg = svg1 + svg2;
    delete svg1, svg2;

    let html1 = svg + '<polyline points="20 6 9 17 4 12"></polyline></svg><pre>Copied!</pre>';
    let html2 = svg + '<path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><pre>Copy code</pre>';

    if (typeof elementButton.innerText != 'undefined') {
         elementButton.innerHTML = html1; // IE8
    } else {
         elementButton.textContent = html1; // Нормальные браузеры
    }

    setTimeout(function() {
        if (typeof elementButton.innerText != 'undefined') {
             elementButton.innerHTML = html2; // IE8
        } else {
             elementButton.textContent = html2; // Нормальные браузеры
        }
    }, 1000);
}
function downloadTextFile(text, filename) {
  // Создаем элемент <a> для загрузки файла
  const element = document.createElement('a');
  element.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(text));
  element.setAttribute('download', filename);

  // Скрытый элемент <a>, добавляем его в DOM
  element.style.display = 'none';
  document.body.appendChild(element);

  // Симулируем щелчок по элементу для загрузки файла
  element.click();

  // Удаляем элемент из DOM
  document.body.removeChild(element);
}
function DownloadCode(element, button_element, filename) {
    let text = element.textContent
    console.log(element.textContent)
    downloadTextFile(text.split('\n').slice(1).join('\n'), filename);


    let svg1 = '<svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" ';
    let svg2 = 'stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg">';
    let svg = svg1 + svg2;
    delete svg1, svg2;

    let html1 = svg + '<polyline points="20 6 9 17 4 12"></polyline></svg><pre>Download!</pre>';
    let html2 = svg + '<path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><pre>Download code</pre>';

    if (typeof button_element.innerText != 'undefined') {
         button_element.innerHTML = html1; // IE8
    } else {
         button_element.textContent = html1; // Нормальные браузеры
    }

    setTimeout(function() {
        if (typeof button_element.innerText != 'undefined') {
             button_element.innerHTML = html2; // IE8
        } else {
             button_element.textContent = html2; // Нормальные браузеры
        }
    }, 1000);
}

/*

<svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg">
  <polyline points="20 6 9 17 4 12"></polyline>
</svg>
<pre>Copied!</pre>


<svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg">
  <path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path>
  <rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect>
</svg>
<pre>Copy code</pre>

*/

function togglePopup() {
    var popup = document.getElementById("popupElement");
    if (popup.style.display === "none") {
        popup.style.display = "block";
    } else {
        popup.style.display = "none";
    }
}

function handleSearch(event) {
    event.preventDefault(); // Предотвращает отправку формы при нажатии Enter
    var searchInput = document.getElementById("searchInput");
    var query = searchInput.value.trim(); // Удаляет начальные и конечные пробелы

    if (query.length > 0 && query.length <= 100) {
        console.log("Поисковый запрос:", query);
    }

    // searchInput.value = ""; // Очищает поле поиска после отправки запроса
}

function downloadFile(text, filename) {
    var element = document.createElement('a');
    element.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(text));
    element.setAttribute('download', filename);

    element.style.display = 'none';
    document.body.appendChild(element);

    element.click();

    document.body.removeChild(element);
}
