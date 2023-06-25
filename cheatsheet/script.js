
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
    return PutHtmlText(getCheatSheat(url))
}
