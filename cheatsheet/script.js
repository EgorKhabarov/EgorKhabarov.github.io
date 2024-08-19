/* python str.removesuffix */
function removeSuffix(str, suffix) {
  if (str.endsWith(suffix)) {
    return str.slice(0, -suffix.length);
  }
  return str;
}

/* Style */
function changeActiveButton(element) {
    for (el of document.getElementsByClassName("active_button")) {
        el.classList.remove("active_button")
    }
    element.classList.add("active_button");
}

/* Style.Display */
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
function DisplayCheatSheet(vpath) {
    delAnchor();

    isFolderCheatSheet = vpath.endsWith("/");
    vpath = isFolderCheatSheet ? vpath + "index.md" : removeSuffix(vpath, "/");
    kpath = getPathWithoutFilename(vpath);

    console.log(`vpath = "${vpath}"`);
    console.log(`kpath = "${kpath}"`);

    // Раскрываем все родительские папки
    element = document.querySelector(`[kpath="${kpath}"]`);
    setDisplayBlock(element.nextElementSibling) // Раскрываем папку с шпаргалкой
    parent = element.parentElement;
    while (parent) {
        setDisplayBlock(parent);
        parent = parent.parentElement;
    }

    velement = document.querySelector(`[vpath="${vpath}"]`);
    if (!velement) {
        return PutHtmlText();
    }

    changeActiveButton(velement);
    velement.scrollIntoView({block: "center"});
    cheatsheet_buttons.scrollLeft -= 200;
    GET(vpath);
}

/* Settings */
function loadSettings() {
    const settings = localStorage.getItem("settings");
    return settings ? JSON.parse(settings) : {
        "settings_search_regex": false,
        "settings_search_register_independence": true,
        "settings_search_full_path": true,
        "settings_search_show_full_path": true,
    };
}
function saveSettings(settings) {
    localStorage.setItem(
        "settings",
        JSON.stringify(settings)
    );
}
function applySettings(settings) {
    for (const [key, value] of Object.entries(settings)) {
        const element = document.getElementById(key);
        if (element) element.checked = value;
    }
}

/* Anchor */
function getAnchor() {
    const url = new URL(window.location.href);
    return url.hash ? url.hash.slice(1) : null;
}
function delAnchor() {
    const url = new URL(window.location.href);
    url.hash = "";
    window.history.pushState({}, "", url.toString());
}
function setAnchor(anchor) {
    const url = new URL(window.location.href);
    url.hash = anchor ? `#${anchor}` : "";
    window.history.pushState({}, "", url.toString());
}

/* URL Path */
function getArgumentFromUrl() {
    const currentUrl = new URL(window.location.href);
    return currentUrl.search ? currentUrl.search.substring(1) : null;
}
function addArgumentToUrl(arg) {
    const currentUrl = new URL(window.location.href);
    currentUrl.search = arg;
    window.history.pushState({}, "", currentUrl);
}
function removeArgumentFromUrl() {
    let url = new URL(window.location.href);
    url.search = "";
    window.history.replaceState(null, null, url.href);
}

/* Title */
function changeTitle(title) {
    console.log(`title: "${title}"`);
    result = "Шпаргалка";
    if (title) {
        result += ": " + title;
    }
    document.getElementsByTagName("title")[0].textContent = result;
}

/* Path */
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
function getPathFilename(filePath) {
    filePath = decodeURIComponent(filePath).trim("/");
    const lastSlashIndex = filePath.lastIndexOf("/");
    if (lastSlashIndex !== -1) {
        return filePath.substring(lastSlashIndex + 1);
    }
   return "";
}

/* Copy Download Code */
function CopyCode(button_element) {
    let code_element = button_element.parentElement.parentElement.lastElementChild;

    const pre_element = document.createElement("pre");
    pre_element.innerHTML = code_element.innerHTML;
    if (!isCtrlPressed) {
        pre_element.querySelectorAll(".unselectable").forEach(
            element => element.remove()
        );
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
function DownloadCode(button_element, filename) {
    let code_element = button_element.parentElement.parentElement.lastElementChild;

    let text = code_element.textContent.split("\n").slice(1).join("\n");
    const element = document.createElement("a");
    element.setAttribute("href", "data:text/plain;charset=utf-8," + encodeURIComponent(text));
    element.setAttribute("download", filename);
    element.style.display = "none";
    document.body.appendChild(element);
    element.click();
    document.body.removeChild(element);

    let download_html = '<svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 3v4a1 1 0 0 1-1 1H5m5 4-2 2 2 2m4-4 2 2-2 2m5-12v16a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V7.914a1 1 0 0 1 .293-.707l3.914-3.914A1 1 0 0 1 9.914 3H18a1 1 0 0 1 1 1Z"/></svg><text>Download code</text>'
    let downloaded_html = '<svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><polyline points="20 6 9 17 4 12"></polyline></svg><text>Download!</text>';

    if (typeof button_element.innerText != "undefined") {
         button_element.innerHTML = downloaded_html; // IE8
    } else {
         button_element.textContent = downloaded_html; // Нормальные браузеры
    }

    setTimeout(function() {
        if (typeof button_element.innerText != "undefined") {
             button_element.innerHTML = download_html; // IE8
        } else {
             button_element.textContent = download_html; // Нормальные браузеры
        }
    }, 1000);
}

/* FontSize */
function changeFontSize(action) {
    let currentSize = parseFloat(getComputedStyle(cheatsheet_field).fontSize);

    if (action === "+") {
        cheatsheet_field.style.fontSize = (currentSize + 2) + "px";
        currentSize += 2
    } else if (action === "-") {
        if (currentSize < 3) return
        cheatsheet_field.style.fontSize = (currentSize - 2) + "px";
        currentSize -= 2
    } else if (action === "=") {
        cheatsheet_field.style.fontSize = 12 + "px";
        currentSize = 12
    }

    if (typeof font_size_button.innerText != "undefined") {
        font_size_button.innerText = currentSize + "px"; // IE8-
    } else {
        font_size_button.textContent = currentSize + "px"; // Нормальные браузеры
    }
}

/* Search */
function performSearch(empty) {
    search_query = empty ? "" : search_input.value;

    if (search_query) {
        search_button_folder.style.display = "block";
    } else {
        search_button_folder.style.display = "none"
    }
    if (!search_query) {return}
    console.log("Search:", search_query);
    search_button_folder.innerHTML = "";
    s1Array = [];

    if (settings["settings_search_regex"]) {
        for (el of search_query.split(" ").filter(item => item !== "")) {
            try {
                s1Array.push(new RegExp(el, settings["settings_search_register_independence"] ? "i" : ""));
                search_input.style.color = "#AFB1B3";
            } catch (e) {
                search_input.style.color = "#ff0000";
            }
        }
    } else {
        search_input.style.color = "#AFB1B3";
        if (settings["settings_search_register_independence"]) {
            search_query = search_query.toLowerCase()
        };
        s1Array = search_query.split(" ").filter(item => item !== "")
    }
    console.log(s1Array);

    function searchElements(element) {
        let results = [];
        for (el of element)
            if (el.tagName === "BUTTON" && el.getAttribute("vpath")) {
                vpath = el.getAttribute("vpath");
                if (settings["settings_search_register_independence"]) {
                    vpath = vpath.toLowerCase();
                }
                let s2Array = vpath.replace(".md", "").split("/");
                if (!settings["settings_search_full_path"]) {
                    slc1 =  s2Array.slice(-1)
                    if (slc1[0] === "index") {
                        s2Array = s2Array.slice(-2, -1);
                    } else {
                        s2Array = s2Array.slice(-1);
                    }
                };
                if (s1Array.every(ss1 => s2Array.some(ss2 =>
                    settings["settings_search_regex"] ? ss2.match(ss1) : ss2.includes(ss1 ? ss1 : null)
                ))) {
                    results.push(el);
                }
            } else {
                results = results.concat(searchElements(el.children));
            }
        return results;
    };
    results = searchElements(Array.from(cheatsheet_buttons.children).slice(2));
    console.log("found", results.length, "results")
    if (results.length > 0) {
        console.log(results.map(item => item.getAttribute("vpath")));
        results.forEach(element => {
            vpath = element.getAttribute("vpath");
            title = removeSuffix(removeSuffix(vpath, ".md"), "/⁠index");

            button = document.createElement("button");
            if (settings["settings_search_show_full_path"]) {
                button.innerHTML = element.firstElementChild.outerHTML + title;
            } else {
                button.innerHTML = element.innerHTML;
            }
            button.classList.add("button", "unselectable");
            button.setAttribute("search_vpath", vpath);
            button.setAttribute("onclick", "onclickSearchButton(this);");
            button.setAttribute("title", title);
            search_button_folder.appendChild(button);
        });
    } else {
        button = document.createElement("button");
        button.textContent = "Nothing found";
        button.classList.add("button");
        button.setAttribute("title", "Nothing found");
        search_button_folder.appendChild(button);
    }
}

/* Скачать нужную шпаргалку по пути */
function getCheatSheet(url) {
    var xhr = new XMLHttpRequest();
    xhr.open("GET", url, false); // Используется синхронный запрос
    xhr.send();

    if (xhr.status === 200) {
        return xhr.responseText;
    } else {
        return "";
    }
}

/* Вставить шпаргалку */
function PutHtmlText(html) {
    if (!html) {
        html = '<img alt="404.png" src="404.png">';
    }

    if (typeof cheatsheet_field.innerText != "undefined") {
        cheatsheet_field.innerHTML = html; // IE8-
    } else {
        cheatsheet_field.textContent = html; // Нормальные браузеры
    }
    cheatsheet_field.scrollTo(0, 0);
    processingCheatSheet();
}

/* Получить и разместить шпаргалку по пути */
function GET(url) {
    url = removeSuffix(url, "index.md");
    addArgumentToUrl(url);
    if (!url.endsWith(".md") && !url.endsWith(".html")) {
        if (isCtrlPressed) {
            return
        }
        url += "index.md";
    }

    if (need_save_history) {
        if (!(url in history)) {
            cs = getCheatSheet(url);
            if (cs) {
                history[url] = cs
            }
            console.log(`GET "${url}"`)
        } else {
            console.log(`GET history["${url}"]`)
        }
        cheatsheet = history[url];
        if (cheatsheet === undefined) {cheatsheet = "";}
    } else {
        cheatsheet = getCheatSheet(url);
        console.log(`GET "${url}"`)
    }
    PutHtmlText(cheatsheet);
}

/* Markdown */
function processingCheatSheet() {
    cheatsheet_field.querySelectorAll("a").forEach(a => {
        if (!a.target) {a.target="_blank";}
    });
    h_elements = cheatsheet_field.querySelectorAll("h1, h2, h3, h4, h5, h6");
    h_elements.forEach(header => {
        let id = header.textContent.trim()
            .toLowerCase()
            .replace(/\s+/g, "-")
            // .replace(/[^\w\-]+/g, "")
            .replace(/\-\-+/g, "-")
            .replace(/^-+/, "")
            .replace(/-+$/, "");
        header.id = id;
        header.innerHTML = `${header.innerHTML}<a class="anchor" href="#${id}"><svg style="width: .6em;height: .9em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13.213 9.787a3.391 3.391 0 0 0-4.795 0l-3.425 3.426a3.39 3.39 0 0 0 4.795 4.794l.321-.304m-.321-4.49a3.39 3.39 0 0 0 4.795 0l3.424-3.426a3.39 3.39 0 0 0-4.794-4.795l-1.028.961"></path></svg></a>`;
    });
};

/* onclick */
function onclickFolderButton(element) {
    toggleDisplay(
        element.nextElementSibling
    );
}
function onclickFolderCheatSheetButton(element) {
    delAnchor();
    changeActiveButton(element);
    toggleDisplay(element.nextElementSibling);

    let vpath = element.getAttribute("vpath");

    changeTitle(getPathFilename(vpath));
    GET(vpath);
}
function onclickCheatSheetButton(element) {
    delAnchor();
    changeActiveButton(element);

    let vpath = element.getAttribute("vpath");

    changeTitle(getPathFilename(vpath));
    GET(vpath);
}
function onclickLinkButton(element) {
    delAnchor();

    let vpath = element.getAttribute("vpath");

    DisplayCheatSheet(vpath);
    changeTitle(getPathFilename(vpath));
    GET(vpath);
}
function onclickSearchButton(element) {
    delAnchor();

    let vpath = element.getAttribute("search_vpath");

    DisplayCheatSheet(vpath);
    changeTitle(getPathFilename(vpath));
    GET(vpath);
    performSearch(true);

}


document.addEventListener("DOMContentLoaded", function() {
    // Аргументы URL
    const arg = decodeURIComponent(getArgumentFromUrl());
    if (arg !== "null") {
        console.log(`Argument found: "${arg}"`);
        DisplayCheatSheet(arg);
    } else {
        PutHtmlText(getCheatSheet("README.html"));
    }

    // Якорь
    const anchor = getAnchor();
    if (anchor) {
        console.log(`Anchor found: "${anchor}"`);
        anchor_element = document.getElementById(anchor)
        if (anchor_element) anchor_element.scrollIntoView({block: "start"});
    }

    // Поиск
    search_input.addEventListener("input", function() {performSearch()});

    // Изменялка размеров #cheatsheet_buttons и #cheatsheet_field
    rpanrResize.addEventListener("mousedown", mD);
    rpanrResize.addEventListener("touchstart", mD);
    // Для избежания бага с прикреплённым к курсору элемента rpanrResize
    window.addEventListener("mouseup", end)


    settings_button.addEventListener("click", () => {settings_overlay.style.display = "block";settings_popup.style.display = "block";});
    settings_overlay.addEventListener("click", () => {settings_overlay.style.display = "none";settings_popup.style.display = "none";});
    settings_ok_button.addEventListener("click", () => {settings_overlay.style.display = "none";settings_popup.style.display = "none";});
    settings_reset_button.addEventListener("click", () => {
        settings["settings_search_regex"] = false;
        settings["settings_search_register_independence"] = true;
        settings["settings_search_full_path"] = true;
        settings["settings_search_show_full_path"] = true;
        saveSettings(settings);
        applySettings(settings);
        performSearch(searchInput.value);
    });

    applySettings(settings);
    settings_popup.childNodes.forEach((element) => {
        if (element.tagName === "INPUT") {
            element.addEventListener("change", (event) => {
                settings[element.id] = event.target.checked;
                console.log(`settings["${element.id}"] = "${event.target.checked}"`);
                saveSettings(settings);
                performSearch();
            });
        }
    });
});
document.addEventListener("keydown", function(event) {if (event.ctrlKey) {isCtrlPressed = true;}});
document.addEventListener("keyup", function(event) {if (!event.ctrlKey) {isCtrlPressed = false;}});
document.addEventListener("click", function(event) {
    console.log(event.target, event.target.id);
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
let settings = loadSettings();


/* rpanrResize */
function mD(event) {
    event.preventDefault(); // Предотвращаем стандартное поведение браузера
    ismdwn = 1;
    document.body.addEventListener("mousemove", mV);
    document.body.addEventListener("mouseup", end);
    document.body.addEventListener("touchmove", mV);
    document.body.addEventListener("touchend", end);
}

function mV(event) {
    let clientX;
    if (event.type === "mousemove" || event.type === "mouseup") {
        clientX = event.clientX;
    } else if (event.type === "touchmove") {
        clientX = event.touches[0].clientX;
    }

    if (ismdwn === 1) {
        cheatsheet_buttons.style.flexBasis = clientX - 19 + "px"; //  - 48
    } else {
        end();
    }
}

function end() {
    ismdwn = 0;
    document.body.removeEventListener("mousemove", mV);
    document.body.removeEventListener("mouseup", end);
    document.body.removeEventListener("touchmove", mV);
    document.body.removeEventListener("touchend", end);
}
