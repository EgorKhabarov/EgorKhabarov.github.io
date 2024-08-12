/* Скрыть / показать папку */
function toggleDisplay(element) {
    if (element.style.display == "none") {
        element.style.display = "block";
    } else {
        element.style.display = "none";
    }
}

function setDisplayBlock(element) {
    if (element.style.display == "none") {
        element.style.display = "block";
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
    var textArea = document.createElement("textarea");
    textArea.value = text;
    document.body.appendChild(textArea);
    textArea.select();
    document.execCommand("copy");
    textArea.remove();
}

/*Копировать выделенный текст*/
function copyTextFromDiv2() {
    document.execCommand("copy");
}

/*Изменить цвет кнопки справа*/
function changeColor(element) {
    element.style.backgroundColor = "#008000";
    setTimeout(function() {element.style.backgroundColor = "#525252";}, 2000);
}

/*Вставить шпаргалку в нужный элемент*/
function PutHtmlText(html) {
    if (html != "") {
        let FieldElement = document.getElementById("field");

        if (typeof FieldElement.innerText != "undefined") {
            FieldElement.innerHTML = html; // IE8-
        } else {
            FieldElement.textContent = html; // Нормальные браузеры
        }
        document.getElementById("field").scrollTo(0, 0);
    }
}

/*Взять нужную шпаргалку по пути*/
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

/**/
function removeSuffix(str, suffix) {
  if (str.endsWith(suffix)) {
    return str.slice(0, -suffix.length);
  }
  return str;
}

function GET(url) {
    url = removeSuffix(url, "index.md");
    addArgumentToUrl(url);
    if (!url.endsWith(".md")) {
        if (isCtrlPressed) {
            return
        }
        url += "index.md";
    }

    if (need_save_history) {
        if (!(url in history)) {
            cs = getCheatSheat(url);
            if (cs) {
                history[url] = cs
            }
            console.log(`GET "${url}"`)
        } else {
            console.log(`GET history["${url}"]`)
        }
        cheatsheet = history[url];
        if (cheatsheet === undefined) {cheatsheet = '';}
    } else {
        cheatsheet = getCheatSheat(url);
        console.log(`GET "${url}"`)
    }
    PutHtmlText(cheatsheet);
}

function copyCode(button_element) {
    let code_element = button_element.parentElement.parentElement.lastElementChild;

    const pre_element = document.createElement("pre");
    pre_element.innerHTML = code_element.innerHTML;
    if (!isCtrlPressed) {
        const elementsToRemove = pre_element.querySelectorAll(".unselectable");
        elementsToRemove.forEach(element => element.remove());
    }
    const textarea = document.createElement("textarea");
    document.body.appendChild(textarea);
    textarea.value = pre_element.textContent;
    textarea.select();
    document.execCommand("copy");
    document.body.removeChild(textarea);

    let svg = '<svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg">'
    let html1 = svg + '<polyline points="20 6 9 17 4 12"></polyline></svg><text>Copied!</text>';
    let html2 = svg + '<path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text>';

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

function downloadTextFile(text, filename) {
  // Создаем элемент <a> для загрузки файла
  const element = document.createElement("a");
  element.setAttribute("href", "data:text/plain;charset=utf-8," + encodeURIComponent(text));
  element.setAttribute("download", filename);

  // Скрытый элемент <a>, добавляем его в DOM
  element.style.display = "none";
  document.body.appendChild(element);

  // Симулируем щелчок по элементу для загрузки файла
  element.click();

  // Удаляем элемент из DOM
  document.body.removeChild(element);
}

function DownloadCode(button_element, filename) {
    let code_element = button_element.parentElement.parentElement.lastElementChild;

    let text = code_element.textContent
    downloadTextFile(text.split("\n").slice(1).join("\n"), filename);

    let svg1 = '<svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" ';
    let svg2 = 'stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg">';
    let svg = svg1 + svg2;
    delete svg1, svg2;

    let html1 = svg + '<polyline points="20 6 9 17 4 12"></polyline></svg><pre>Download!</pre>';
    let html2 = svg + '<path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><pre>Download code</pre>';

    if (typeof button_element.innerText != "undefined") {
         button_element.innerHTML = html1; // IE8
    } else {
         button_element.textContent = html1; // Нормальные браузеры
    }

    setTimeout(function() {
        if (typeof button_element.innerText != "undefined") {
             button_element.innerHTML = html2; // IE8
        } else {
             button_element.textContent = html2; // Нормальные браузеры
        }
    }, 1000);
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
    var element = document.createElement("a");
    element.setAttribute("href", "data:text/plain;charset=utf-8," + encodeURIComponent(text));
    element.setAttribute("download", filename);

    element.style.display = "none";
    document.body.appendChild(element);

    element.click();

    document.body.removeChild(element);
}

function addArgumentToUrl(arg) {
    const currentUrl = new URL(window.location.href);
    currentUrl.search = arg;
    window.history.pushState({}, "", currentUrl);
}

function getArgumentFromUrl() {
    const currentUrl = new URL(window.location.href);
    return currentUrl.search ? currentUrl.search.substring(1) : null;
}

function removeArgumentFromUrl() {
    let url = new URL(window.location.href);
    url.search = "";
    window.history.replaceState(null, null, url.href);
}

function addSearchArgumentToUrl(arg) {
    const currentUrl = new URL(window.location.href);
    currentUrl.search = arg;
    window.history.pushState({}, "", currentUrl);
}

function getPathWithoutFilename(filePath) {
    filePath = decodeURIComponent(filePath);
    if (filePath.endsWith("/")) {
        return filePath
    }
    const lastSlashIndex = filePath.lastIndexOf("/");
    if (lastSlashIndex !== -1) {
        return filePath.substring(0, lastSlashIndex);
    }
   return "";
}

function toggleStyleDisplayByPath(kpath) {
    let element = document.querySelector(`[kpath="${kpath}"]`);
    element.click();
    let parent = element.parentElement;
    while (parent) {
        setDisplayBlock(parent);
        parent = parent.parentElement;
    }
}

function restoreCheatSheetState(path) {
    let kpath = getPathWithoutFilename(path);
    let kelement = document.querySelector(`[kpath="${kpath}"]`);
    if (!kelement) {
        kpath += "/";
        kelement = document.querySelector(`[kpath="${kpath}"]`);
    }
    // console.log("getPathWithoutFilename", kpath);
    try {
        toggleStyleDisplayByPath(kpath);
    } catch (e) {
        console.log("toggleStyleDisplayByPath(kpath);");
    }

    let vpath = path;
    let velement = document.querySelector(`[vpath="${vpath}"]`);
    if (!velement) {
        vpath += "/";
        velement = document.querySelector(`[vpath="${vpath}"]`);
    }
    // console.log("vpath", vpath);

    const container = document.querySelector(".cheatsheet-buttons");
    if (vpath.endsWith("/")) {
        velement.click();
    }
    velement.focus();
    if (vpath.endsWith("/")) {
        console.log(`click "${vpath}"`)
        velement.click();
    }
    velement.scrollIntoView({ block: "center"});
    container.scrollLeft -= 200;
    GET(path);
}

function performSearch(search_query) {
    console.log("Search:", search_query);
    const searchButtonFolder = document.getElementById("search-button-folder");
    const cheatsheetButtons = document.getElementById("cheatsheet-buttons");
    if (search_query) {
        searchButtonFolder.style.display = "block";
    } else {
        searchButtonFolder.style.display = "none"
    }
    searchButtonFolder.innerHTML = "";

    const s1Array = search_query.toLowerCase().split(" ").filter(item => item !== "");
    function searchElements(element) {
        let results = [];
        for (el of element)
            if (el.tagName === "BUTTON" && el.getAttribute("vpath")) {
                const s2Array = el.getAttribute("vpath").toLowerCase().replace(".md", "").split("/");
                if (s1Array.every(ss1 => s2Array.some(ss2 => ss2.includes(ss1 ? ss1 : null)))) {
                    results.push(el);
                }
            } else {
                results = results.concat(searchElements(el.children));
            }
        return results;
    };
    results = searchElements(Array.from(cheatsheetButtons.children).slice(2));
    console.log("found", results.length, "results")
    if (results.length > 0) {
        results.forEach(element => {
            vpath = element.getAttribute("vpath");
            text = element.textContent.trim().split(" ")[0] + " " + vpath.replace(".md", "");
            text = text.replaceAll(" ", " ").replaceAll("/", "⁠/⁠").replaceAll("-", "⁠-⁠");
            button = document.createElement("button");
            button.textContent = text;  //element.textContent;
            button.classList.add("button");
            button.setAttribute("onclick", "GET('"+`${vpath}`+"');restoreCheatSheetState('"+`${vpath}`+"')");
            button.setAttribute("title", text);
            searchButtonFolder.appendChild(button);
        });
    } else {
        button = document.createElement("button");
        button.textContent = "Nothing found";
        button.classList.add("button");
        button.setAttribute("title", "Nothing found");
        searchButtonFolder.appendChild(button);
    }
}


document.addEventListener("DOMContentLoaded", function() {
    // Проверяем наличие аргумента при загрузке страницы
    const arg = getArgumentFromUrl();
    if (arg) {
        console.log(`Argument found: "${decodeURIComponent(arg)}"`);
        restoreCheatSheetState(decodeURIComponent(arg));
    } else {
        PutHtmlText(getCheatSheat("README.html"))
    }

    const searchInput = document.getElementById("search");
    searchInput.addEventListener("input", function() {
        performSearch(searchInput.value);
    });

    const rpanrResize = document.getElementById("rpanrResize");
    rpanrResize.addEventListener("mousedown", mD)
});
document.addEventListener("keydown", function(event) {if (event.ctrlKey) {isCtrlPressed = true;}});
document.addEventListener("keyup", function(event) {if (!event.ctrlKey) {isCtrlPressed = false;}});
document.addEventListener("click", function(event) {
    if (event.target.tagName === "CODE") {
        const tempInput = document.createElement("input");
        document.body.appendChild(tempInput);
        tempInput.value = event.target.textContent;
        tempInput.select();
        document.execCommand("copy");
        document.body.removeChild(tempInput);
    }
});


let need_save_history = true;
let history = {};
let isCtrlPressed = false;
let ismdwn = 0;


function mD(event) {
    ismdwn = 1;
    document.body.addEventListener("mousemove", mV);
    document.body.addEventListener("mouseup", end);
};

function mV(event) {
    if (ismdwn === 1) {
        cheatsheetButtons = document.getElementById("cheatsheet-buttons");
        cheatsheetButtons.style.flexBasis = event.clientX - 48 + "px";
    } else {
        end()
    }
};

const end = (e) => {
    ismdwn = 0;
    document.body.removeEventListener("mouseup", end);
    rpanrResize.removeEventListener("mousemove", mV);
};
