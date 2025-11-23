/* --- ELEMENTS --- */
const sidebar = document.getElementById("cheatsheet_buttons");
const container = document.getElementById("main_container");
const overlay = document.getElementById("mobile_overlay");
const resizer = document.getElementById("resizer");
const settingsBtn = document.getElementById("settings_btn");
const themeBtn = document.getElementById("theme_btn");
const settingsModal = document.getElementById("settings_modal");
const closeSettingsBtn = document.getElementById("close_settings");
const settingsBackdrop = document.getElementById("settings_backdrop");
const searchInput = document.getElementById("search_input");
const breadcrumbsContainer = document.getElementById("breadcrumbs_row");
const body = document.body;
const folderList = document.querySelector(".folder_list");

let isSettingsOpen = false;

/* --- TREE VIEW LOGIC --- */
// Обработка кликов по дереву файлов
folderList.addEventListener("click", (e) => {

    // 1. Клик по папке (открытие/закрытие)
    const folderItem = e.target.closest(".tree_item.folder");
    if (folderItem) {
        e.stopPropagation(); // Чтобы не триггерить другие события
        toggleFolder(folderItem);
        return;
    }

    // 2. Клик по вертикальной линии (закрытие папки)
    // Проверяем, был ли клик по контейнеру tree_children
    if (e.target.classList.contains("tree_children")) {
        // Вычисляем позицию клика внутри элемента
        const rect = e.target.getBoundingClientRect();
        const clickX = e.clientX - rect.left;

        // Если клик был в зоне левой границы (примерно 15px с учетом padding)
        // Линия border_left (2px) + padding_left (5px) + запас
        if (clickX < 15) {
            e.stopPropagation();
            const parentGroup = e.target.closest(".tree_group");
            if (parentGroup) {
                const folderBtn = parentGroup.querySelector(".tree_item.folder");
                if (folderBtn) {
                    toggleFolder(folderBtn, true); // force close
                }
            }
        }
    }
});

// Функция переключения папки
function toggleFolder(folderItem, forceClose = false) {
    // Находим следующий элемент (контейнер с детьми)
    const childrenContainer = folderItem.nextElementSibling;
    if (!childrenContainer || !childrenContainer.classList.contains("tree_children")) return;

    const iconUse = folderItem.querySelector("use");
    let isClosed = childrenContainer.classList.contains("hidden");

    if (forceClose) {
        isClosed = false; // Мы хотим закрыть, значит считаем что сейчас открыто
    }

    if (isClosed) {
        // Открыть
        childrenContainer.classList.remove("hidden");
        // iconUse.setAttribute("href", "#icon_folder_open");
        folderItem.setAttribute("data-state", "open");
    } else {
        // Закрыть
        childrenContainer.classList.add("hidden");
        // iconUse.setAttribute("href", "#icon_folder");
        folderItem.setAttribute("data-state", "closed");
        folderItem.nextElementSibling.querySelectorAll('[data-state="open"]').forEach(e => {
            console.log(e);
            e.setAttribute("data-state", "closed");
            e.nextElementSibling.classList.add("hidden");
        })
    }
}

/* --- BREADCRUMBS --- */
function renderBreadcrumbs(url) {
    breadcrumbsContainer.innerHTML = "";
    let accumulatedPath = [];
    const pathArray = url.split("/");
    pathArray.forEach((part, index) => {
        accumulatedPath.push(part);
        const currentFullPath = accumulatedPath.join("/");
        const span = document.createElement("span");
        span.textContent = part;
        span.className = "crumb_item";
        span.addEventListener("click", () => {
            console.log(`Navigating to: ${currentFullPath}`, index, pathArray.length);
            closeAllKeyButtons();
            openSidebar();
            const button = (index === pathArray.length - 1)
                ? displayValueButton(currentFullPath)
                : displayKeyButton(currentFullPath);
            button.classList.add("pulse-bg");
            setTimeout(function() {
                button.classList.remove("pulse-bg");
            }, 1000);
        });
        breadcrumbsContainer.appendChild(span);
        if (index < pathArray.length - 1) {
            const sep = document.createElement("span");
            sep.textContent = "/";
            sep.className = "crumb_separator";
            breadcrumbsContainer.appendChild(sep);
        }
    });
    //breadcrumbsContainer.lastElementChild.classList = null;
}

/* --- THEME TOGGLE --- */
let isDark = true;
themeBtn.addEventListener("click", () => {
    isDark = !isDark;
    if (isDark) {
        document.documentElement.setAttribute("data-theme", "dark");
    } else {
        document.documentElement.removeAttribute("data-theme");
    }
});

/* --- SEARCH --- */
searchInput.addEventListener("input", (e) => {
    console.log("Search input:", e.target.value);
});

/* --- RESIZE FIX --- */
window.addEventListener("resize", () => {
    if (window.innerWidth > 768) {
        sidebar.style.transform = "";
        sidebar.style.transition = "";
        overlay.style.opacity = "";
        overlay.style.pointerEvents = "";
        sidebarOpen = false;
        isDraggingSidebar = false;
    }
});

/* --- RESIZER LOGIC (MOUSE & TOUCH) --- */
let isResizing = false;

function startResize(e) {
    if (e.type === 'touchstart') e.preventDefault();

    isResizing = true;
    resizer.classList.add('active');
    body.classList.add('no_select');
}

function doResize(clientX) {
    if (!isResizing) return;
    const containerRect = container.getBoundingClientRect();
    const newWidth = clientX - containerRect.left;
    let percentage = (newWidth / containerRect.width) * 100;
    if (percentage < 10) percentage = 10;
    if (percentage > 70) percentage = 70;
    document.documentElement.style.setProperty('--sidebar-width', `${percentage}%`);
}

function stopResize() {
    if (isResizing) {
        isResizing = false;
        resizer.classList.remove('active');
        body.classList.remove('no_select');
    }
}

resizer.addEventListener('mousedown', startResize);
document.addEventListener('mousemove', (e) => doResize(e.clientX));
document.addEventListener('mouseup', stopResize);

resizer.addEventListener('touchstart', startResize, { passive: false });
document.addEventListener('touchmove', (e) => {
    if (isResizing) {
        e.preventDefault();
        doResize(e.touches[0].clientX);
    }
}, { passive: false });
document.addEventListener('touchend', stopResize);

/* --- MOBILE DRAWER --- */
let startX = 0;
let isDraggingSidebar = false;
let sidebarOpen = false;
const EDGE_THRESHOLD = 30;
function isMobile() { return window.innerWidth <= 768; }
function updateSidebarPosition(translateX) {
    sidebar.style.transform = `translateX(${translateX}%)`;
    const opacity = 1 - (Math.abs(translateX) / 100);
    overlay.style.opacity = opacity;
    overlay.style.pointerEvents = opacity > 0 ? "auto" : "none";
}
function openSidebar() {
    if (!isMobile()) return;
    sidebar.style.transform = `translateX(0%)`;
    overlay.style.opacity = 1;
    overlay.style.pointerEvents = "auto";
    sidebarOpen = true;
}
function closeSidebar() {
    if (!isMobile()) return;
    sidebar.style.transform = `translateX(-100%)`;
    overlay.style.opacity = 0;
    overlay.style.pointerEvents = "none";
    sidebarOpen = false;
}
function handleStart(clientX) {
    if (!isMobile() || isSettingsOpen) return;
    startX = clientX;
    if (!sidebarOpen && startX < EDGE_THRESHOLD) {
        isDraggingSidebar = true;
        sidebar.classList.add("swiping");
    } else if (sidebarOpen) {
        isDraggingSidebar = true;
        sidebar.classList.add("swiping");
    }
}
function handleMove(clientX, preventDefaultFn) {
    if (!isDraggingSidebar || !isMobile() || isSettingsOpen) return;
    const diff = clientX - startX;
    const sidebarRect = sidebar.getBoundingClientRect();
    const sidebarWidthPx = sidebarRect.width || (window.innerWidth * 0.85);
    let translatePercent;
    if (!sidebarOpen) {
        let moveX = Math.min(Math.max(0, diff), sidebarWidthPx);
        let percentMoved = (moveX / sidebarWidthPx) * 100;
        translatePercent = -100 + percentMoved;
    } else {
        let moveX = Math.max(diff, -sidebarWidthPx);
        if (moveX > 0) moveX = 0;
        let percentMoved = (Math.abs(moveX) / sidebarWidthPx) * 100;
        translatePercent = -percentMoved;
    }
    if (Math.abs(diff) > 5 && preventDefaultFn) preventDefaultFn();
    updateSidebarPosition(translatePercent);
}
function handleEnd(clientX) {
    if (!isDraggingSidebar || !isMobile() || isSettingsOpen) return;
    isDraggingSidebar = false;
    sidebar.classList.remove("swiping");
    const endX = clientX;
    const sidebarRect = sidebar.getBoundingClientRect();
    const sidebarWidthPx = sidebarRect.width || (window.innerWidth * 0.85);
    if (!sidebarOpen) {
        if (endX > sidebarWidthPx / 3) openSidebar(); else closeSidebar();
    } else {
        if (startX - endX > sidebarWidthPx / 3) closeSidebar(); else openSidebar();
    }
}

document.addEventListener("touchstart", (e) => handleStart(e.touches[0].clientX), {passive: false});
document.addEventListener("touchmove", (e) => handleMove(e.touches[0].clientX, () => {if (e.cancelable) {e.preventDefault();}}), {passive: false});
document.addEventListener("touchend", (e) => handleEnd(e.changedTouches[0].clientX));
document.addEventListener("mousedown", (e) => {if (e.button === 0) handleStart(e.clientX);});
document.addEventListener("mousemove", (e) => handleMove(e.clientX, null));
document.addEventListener("mouseup", (e) => {if (e.button === 0) handleEnd(e.clientX);});

overlay.addEventListener("click", () => {if (sidebarOpen) closeSidebar();});
function toggleSettings(show) {
    isSettingsOpen = show;
    if (show) settingsModal.classList.add("active");
    else settingsModal.classList.remove("active");
}
settingsBtn.addEventListener("click", () => toggleSettings(true));
closeSettingsBtn.addEventListener("click", () => toggleSettings(false));
settingsBackdrop.addEventListener("click", () => toggleSettings(false));



















function load_cheatsheet(url) {
    fetch(url)
        .then(response => response.text())
        .then(text => {
            cheatsheet_field.innerHTML = text;
            processingCheatSheet();
            cheatsheet_field.scrollTo(0, 0);
        });
}
function closeAllKeyButtons() {
    folderList.querySelectorAll('[data-state="open"]').forEach(e => {
        e.setAttribute("data-state", "closed");
        e.nextElementSibling.classList.add("hidden");
    })
}
function displayKeyButton(url) {
    const pathArray = url.split("/");
    pathArray.pop();
    while (pathArray.length) {
        const kpath = pathArray.join("/");
        const parent_directory = folderList.querySelector(`[data-kpath="${kpath}"]`).nextElementSibling;
        parent_directory.previousElementSibling.setAttribute("data-state", "open");
        parent_directory.classList.remove("hidden");
        pathArray.pop();
    }
    let button = folderList.querySelector(`[data-kpath="${url}"]`);
    console.log(url, button);
    button.scrollIntoView({block: "center"});
    return button;
}
function displayValueButton(url) {
    const pathArray = url.split("/");
    pathArray.pop();
    while (pathArray.length) {
        const kpath = pathArray.join("/");
        const parent_directory = folderList.querySelector(`[data-kpath="${kpath}"]`).nextElementSibling;
        parent_directory.previousElementSibling.setAttribute("data-state", "open");
        parent_directory.classList.remove("hidden");
        pathArray.pop();
    }
    let button = folderList.querySelector(`[data-vpath="${url}"]`);
    button.scrollIntoView({block: "center"});
    return button;
}
function setup_cheatsheet(url_) {
    const url = url_.trim("/");
    console.log(`Load "${url}.html"`)
    load_cheatsheet(url);
    renderBreadcrumbs(url);
    addArgumentToUrl(url);
    closeSidebar();

    changeActiveButton(displayValueButton(url));
}







(function load_folder_list() {
    /*
    fetch("cheatsheet_resources/buttons_new.html")
        .then(response => response.text())
        .then(data => folderList.innerHTML = data);
    */
    const css_colors = {
        "default": ' style="color: var(--color-file-default);"',
        "yellow":  ' style="color: var(--color-file-yellow);"',
        "green":   ' style="color: var(--color-file-green);"',
        "pink":    ' style="color: var(--color-file-pink);"',
        "red":     ' style="color: var(--color-file-red);"',
        "lblue":   ' style="color: var(--color-file-lblue);"',
        "dblue":   ' style="color: var(--color-file-dblue);"',
        "violet":  ' style="color: var(--color-file-violet);"',
        "brown":   ' style="color: var(--color-file-brown);"',
    };

    function parseSimpleYaml(yamlStr) {
        const result = {};
        for (const line of yamlStr.split(/\r?\n/)) {
            const trimmed = line.trim();
            if (!trimmed || trimmed.startsWith("#")) continue;

            const idx = trimmed.indexOf(":");
            if (idx === -1) continue;

            const key = trimmed.slice(0, idx).trim();
            let val = trimmed.slice(idx + 1).trim();

            if (val === "true") val = true;
            else if (val === "false") val = false;
            else if (!isNaN(val) && val !== "") val = Number(val);

            result[key] = val;
        }
        return result;
    }

    function formatFolderSvg(color) {
        const result_color = (color in css_colors) ? css_colors[color] : "";
        return `<svg viewBox="0 0 24 24"${result_color}><use href="#icon_folder"/></svg>`;
    }
    function formatTagSvg(color) {
        const result_color = (color in css_colors) ? css_colors[color] : "";
        return `<svg viewBox="0 0 24 24"${result_color}><use href="#icon_file"/></svg>`;
    }
    function formatCheatsheetButton(title, svg, vpath) {
        return `<div class="tree_item file" title="${vpath}" data-vpath="${vpath}">${svg}<span class="label">${title}</span></div>`;
    }
    function formatFolderButton(title, svg, kpath, buttons_folder_data) {
        return `<div class="tree_group"><div class="tree_item folder" data-state="closed" title="${kpath}" data-kpath="${kpath}">${svg}<span class="label">${title}</span></div><div class="tree_children hidden">${buttons_folder_data}</div></div>`;
    }

    function generateButtons(dictionary, directory = "") {
        const textList = [];
        for (const [key, value] of Object.entries(dictionary)) {
            if (key === "index" || key === ".") continue;
            let title = key.replace(/ /g, "&nbsp;").replace(/-/g, "&#8288;-&#8288;");
            let path = `${directory}/${key}`.replace(/\\/g, "/").replace(/^\/+/, "");
            if (typeof value === "object" && value !== null) {
                path += "/";
            }

            // --- metadata parsing ---
            let currentMetadataStr = typeof value === "string" ? value : String(value["."]);
            let currentMetadata = {};
            if (currentMetadataStr !== "") {
                currentMetadata = parseSimpleYaml(currentMetadataStr);
            }
            if (typeof currentMetadata === "string" || currentMetadata == null) {
                currentMetadata = {};
            }
            // --- skip link (Python commented) ---
            if (key.startsWith(":") && key.slice(1)) {
                continue;
            }

            const keyPath = directory ? `${directory}/${key}` : key;
            const directoryE = directory.replace(/\\/g, "/").replace(/^\/+|\/+$/g, "");

            // --- folder ---
            if (typeof value === "object" && value !== null) {
                const buttonsFolderData = generateButtons(value, keyPath)[0];
                const kpath = `${directoryE}/${key}`.replace(/^\/+/, "");
                const svg = formatFolderSvg(currentMetadata.color || "yellow");
                const cssDisplay = currentMetadata["folder_open"] ? "block" : "none";
                textList.push(formatFolderButton(title, svg, kpath, buttonsFolderData));

            } else {
                // --- file/tag ---
                const vpath = `${directoryE}/${key}`.replace(/^\/+/, "");
                const svg = formatTagSvg(currentMetadata.color || "default");
                const tags = currentMetadata.tags;
                textList.push(formatCheatsheetButton(title, svg, vpath));
            }
        }
        return [textList.join(""), directory];
    }

    fetch("index.json")
        .then(response => response.json())
        .then(json_data => {
            folderList.innerHTML = generateButtons(json_data)[0];
            setup_folder_list_buttons();
        });
})();
function setup_folder_list_buttons() {
    folderList.querySelectorAll(".file").forEach(e => {
        //e.click();
        e.addEventListener("click", function(event) {
            // const textList = [e.textContent];//.parentElement.firstElementChild.textContent
            // while (e.parentElement !== folderList) {
            //     console.log(e);
            //     textList.push(e.parentElement.parentElement.firstChild.textContent);
            //     e = e.parentElement.parentElement;
            // }
            // const text = textList.reverse().join("/");
            // console.log(text);
            const vpath = e.getAttribute("data-vpath")
            setup_cheatsheet(vpath);
        })
    });
    folderList.querySelectorAll(".folder").forEach(e => {
    //e.click();
    });
    let vpath = getPathFilename(getArgumentFromUrl());
    if (vpath === null || vpath === "null") {
        vpath = "README";
    }
    setup_cheatsheet(vpath);
}

let isCtrlPressed = false;
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









function removeSuffix(str, suffix) {
  if (str.endsWith(suffix)) {
    return str.slice(0, -suffix.length);
  }
  return str;
}
function removePrefix(str, prefix) {
    return str.startsWith(prefix) ? str.slice(prefix.length) : str;
}
function removePrefixIgnoreCase(str, prefix) {
    return str.toLowerCase().startsWith(prefix.toLowerCase()) ? str.slice(prefix.length) : str;
}

function changeActiveButton(element) {
    for (el of folderList.getElementsByClassName("tree_item_active")) {
        el.classList.remove("tree_item_active")
    }
    element.classList.add("tree_item_active");
}

function processingBlockQuote(blockquote) {
    if (blockquote.firstChild.textContent.toLowerCase().startsWith("[!note]\n")) {
        blockquote.classList.add("blockquote-note");
        // class="unselectable"
        // textContent
        blockquote.firstChild.innerHTML = `<p class="blockquote-alerts-p" style="color: #478be6;"><svg class="blockquote-alerts-svg" viewBox="0 0 16 16" version="1.1" aria-hidden="true"><path d="M0 8a8 8 0 1 1 16 0A8 8 0 0 1 0 8Zm8-6.5a6.5 6.5 0 1 0 0 13 6.5 6.5 0 0 0 0-13ZM6.5 7.75A.75.75 0 0 1 7.25 7h1a.75.75 0 0 1 .75.75v2.75h.25a.75.75 0 0 1 0 1.5h-2a.75.75 0 0 1 0-1.5h.25v-2h-.25a.75.75 0 0 1-.75-.75ZM8 6a1 1 0 1 1 0-2 1 1 0 0 1 0 2Z"/></svg>Note</p>` + removePrefixIgnoreCase(blockquote.firstChild.innerHTML, "[!note]\n");
        blockquote.style.paddingBottom = "6px";
        blockquote.style.marginTop = "12px";
    } else if (blockquote.firstChild.textContent.toLowerCase().startsWith("[!tip]\n")) {
        blockquote.classList.add("blockquote-tip");
        blockquote.firstChild.innerHTML = `<p class="blockquote-alerts-p" style="color: #57ab5a;"><svg class="blockquote-alerts-svg" viewBox="0 0 16 16" version="1.1" aria-hidden="true"><path d="M8 1.5c-2.363 0-4 1.69-4 3.75 0 .984.424 1.625.984 2.304l.214.253c.223.264.47.556.673.848.284.411.537.896.621 1.49a.75.75 0 0 1-1.484.211c-.04-.282-.163-.547-.37-.847a8.456 8.456 0 0 0-.542-.68c-.084-.1-.173-.205-.268-.32C3.201 7.75 2.5 6.766 2.5 5.25 2.5 2.31 4.863 0 8 0s5.5 2.31 5.5 5.25c0 1.516-.701 2.5-1.328 3.259-.095.115-.184.22-.268.319-.207.245-.383.453-.541.681-.208.3-.33.565-.37.847a.751.751 0 0 1-1.485-.212c.084-.593.337-1.078.621-1.489.203-.292.45-.584.673-.848.075-.088.147-.173.213-.253.561-.679.985-1.32.985-2.304 0-2.06-1.637-3.75-4-3.75ZM5.75 12h4.5a.75.75 0 0 1 0 1.5h-4.5a.75.75 0 0 1 0-1.5ZM6 15.25a.75.75 0 0 1 .75-.75h2.5a.75.75 0 0 1 0 1.5h-2.5a.75.75 0 0 1-.75-.75Z"/></svg>Tip</p>` + removePrefixIgnoreCase(blockquote.firstChild.innerHTML, "[!tip]\n");
        blockquote.style.paddingBottom = "6px";
        blockquote.style.marginTop = "12px";
    } else if (blockquote.firstChild.textContent.toLowerCase().startsWith("[!important]\n")) {
        blockquote.classList.add("blockquote-important");
        blockquote.firstChild.innerHTML = `<p class="blockquote-alerts-p" style="color: #986ee2;"><svg class="blockquote-alerts-svg" viewBox="0 0 16 16" version="1.1" aria-hidden="true"><path d="M0 1.75C0 .784.784 0 1.75 0h12.5C15.216 0 16 .784 16 1.75v9.5A1.75 1.75 0 0 1 14.25 13H8.06l-2.573 2.573A1.458 1.458 0 0 1 3 14.543V13H1.75A1.75 1.75 0 0 1 0 11.25Zm1.75-.25a.25.25 0 0 0-.25.25v9.5c0 .138.112.25.25.25h2a.75.75 0 0 1 .75.75v2.19l2.72-2.72a.749.749 0 0 1 .53-.22h6.5a.25.25 0 0 0 .25-.25v-9.5a.25.25 0 0 0-.25-.25Zm7 2.25v2.5a.75.75 0 0 1-1.5 0v-2.5a.75.75 0 0 1 1.5 0ZM9 9a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"/></svg>Important</p>` + removePrefixIgnoreCase(blockquote.firstChild.innerHTML, "[!important]\n");
        blockquote.style.paddingBottom = "6px";
        blockquote.style.marginTop = "12px";
    } else if (blockquote.firstChild.textContent.toLowerCase().startsWith("[!warning]\n")) {
        blockquote.classList.add("blockquote-warning");
        blockquote.firstChild.innerHTML = `<p class="blockquote-alerts-p" style="color: #c69026;"><svg class="blockquote-alerts-svg" viewBox="0 0 16 16" version="1.1" aria-hidden="true"><path d="M6.457 1.047c.659-1.234 2.427-1.234 3.086 0l6.082 11.378A1.75 1.75 0 0 1 14.082 15H1.918a1.75 1.75 0 0 1-1.543-2.575Zm1.763.707a.25.25 0 0 0-.44 0L1.698 13.132a.25.25 0 0 0 .22.368h12.164a.25.25 0 0 0 .22-.368Zm.53 3.996v2.5a.75.75 0 0 1-1.5 0v-2.5a.75.75 0 0 1 1.5 0ZM9 11a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z"/></svg>Warning</p>` + removePrefixIgnoreCase(blockquote.firstChild.innerHTML, "[!warning]\n");
        blockquote.style.paddingBottom = "6px";
        blockquote.style.marginTop = "12px";
    } else if (blockquote.firstChild.textContent.toLowerCase().startsWith("[!caution]\n")) {
        blockquote.classList.add("blockquote-caution");
        blockquote.firstChild.innerHTML = `<p class="blockquote-alerts-p" style="color: #e5534b;"><svg class="blockquote-alerts-svg" viewBox="0 0 16 16" version="1.1" aria-hidden="true"><path d="M4.47.22A.749.749 0 0 1 5 0h6c.199 0 .389.079.53.22l4.25 4.25c.141.14.22.331.22.53v6a.749.749 0 0 1-.22.53l-4.25 4.25A.749.749 0 0 1 11 16H5a.749.749 0 0 1-.53-.22L.22 11.53A.749.749 0 0 1 0 11V5c0-.199.079-.389.22-.53Zm.84 1.28L1.5 5.31v5.38l3.81 3.81h5.38l3.81-3.81V5.31L10.69 1.5ZM8 4a.75.75 0 0 1 .75.75v3.5a.75.75 0 0 1-1.5 0v-3.5A.75.75 0 0 1 8 4Zm0 8a1 1 0 1 1 0-2 1 1 0 0 1 0 2Z"/></svg>Caution</p>` + removePrefixIgnoreCase(blockquote.firstChild.innerHTML, "[!caution]\n");
        blockquote.style.paddingBottom = "6px";
        blockquote.style.marginTop = "12px";
    }
}

function processingCheatSheet() {
    cheatsheet_field.querySelectorAll("a").forEach(a => {
        if (
            a.target == ""
            && a.getAttribute("href")[0] !== "#"
            && a.getAttribute("href")[0] !== "?"
        ) {
            a.target="_blank";
        }
    });
    cheatsheet_field.querySelectorAll("thead").forEach(thead => {
        if (thead.textContent.trim() == "") {
            thead.remove();
        }
    });
    cheatsheet_field.querySelectorAll("blockquote").forEach(blockquote => {
        blockquote.innerHTML = blockquote.innerHTML.replaceAll(">\n<", "><").replaceAll(">\n    <", "><").trim();
        if (blockquote.textContent.length > 100) {
            blockquote.setAttribute("expandable", "")
        }
        processingBlockQuote(blockquote);
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
        //svg = `<svg style="width: .6em;height: .9em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13.213 9.787a3.391 3.391 0 0 0-4.795 0l-3.425 3.426a3.39 3.39 0 0 0 4.795 4.794l.321-.304m-.321-4.49a3.39 3.39 0 0 0 4.795 0l3.424-3.426a3.39 3.39 0 0 0-4.794-4.795l-1.028.961"></path></svg>`;
        header.innerHTML = `<a class="anchor" href="#${id}">${header.innerHTML}</a>`;
    });

    return; // TODO
    if (h_elements.length !== 0) {
        // TODO cheatsheet_field.innerHTML += `<div id="h_list_button" state="off" class="control_button"><svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-width="2" d="M9 8h10M9 12h10M9 16h10M4.99 8H5m-.02 4h.01m0 4H5"/></svg></div>`;
        breadcrumbs_row.innerHTML += `<div id="h_list_button" state="off" class="icon_btn"><svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-width="2" d="M9 8h10M9 12h10M9 16h10M4.99 8H5m-.02 4h.01m0 4H5"/></svg></div>`;
        h_list = document.createElement("div");
        h_list.id = "h_list";

        // pre_element = document.createElement("pre");
        // pre_element.innerHTML = `<span style="color: rgb(255, 0, 0);">H1</span>&nbsp;<span class="h_list_sel"><svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="14" height="14" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m5 15 7-7 7 7"/></svg></span>`;
        // pre_element.setAttribute("onclick", "cheatsheet_field.scrollTo(0, 0);");
        // h_list.appendChild(pre_element);

        min_header = Math.min(...Array.from(h_elements).map((header) => {return Number(header.tagName[1])}));

        h_elements.forEach(header => {
            h_num = Number(header.tagName[1]);
            color = {
                1: "rgb(255,   0,   0)",
                2: "rgb(250, 115,   0)",
                3: "rgb(255, 250,   0)",
                4: "rgb(  0, 255,   0)",
                5: "rgb(  0, 160, 245)",
                6: "rgb(221,   0, 242)",
            }[h_num];
            indent = {
                1: "",
                2: "&nbsp;".substring((min_header * 6) - 6),
                3: "&nbsp;&nbsp;".substring((min_header * 6) - 6),
                4: "&nbsp;&nbsp;&nbsp;".substring((min_header * 6) - 6),
                5: "&nbsp;&nbsp;&nbsp;&nbsp;".substring((min_header * 6) - 6),
                6: "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;".substring((min_header * 6) - 6),
            }[h_num];
            pre_element = document.createElement("pre");
            //style = header.id === getAnchor() ? `background-color: rgb(75, 75, 75)` : ""; // style="${style}"
            pre_element.innerHTML = `${indent}<span style="color: ${color}">${header.tagName}</span>&nbsp;<span class="h_list_sel">${header.textContent}</span>`;
            pre_element.setAttribute("onclick", `document.getElementById("${header.id}").scrollIntoView({block: "start"})`);
            h_list.appendChild(pre_element);
        });
        cheatsheet_field.appendChild(h_list);

        function f1 () {
            // h_list_button.style.borderTopLeftRadius = "0";
            // h_list_button.style.borderBottomLeftRadius = "0";
            // h_list_button.style.backgroundColor = "rgb(25, 25, 25)";
            h_list.style.display = "block";
            // h_list.style.borderTopRightRadius = "0";
        }
        function f2 () {
            // h_list_button.style.borderTopLeftRadius = "";
            // h_list_button.style.borderBottomLeftRadius = "";
            // h_list_button.style.backgroundColor = "#525252";
            h_list.style.display = "none";
            // h_list.style.borderBottomRightRadius = "";
        }
        function f3 () {
            if (h_list_button.getAttribute("state") === "on") {
                h_list_button.addEventListener("mouseover", f1);
                h_list_button.addEventListener("mouseout", f2);
                h_list       .addEventListener("mouseover", f1);
                h_list       .addEventListener("mouseout", f2);

                h_list_button.addEventListener("touchstart", f1);
                h_list_button.addEventListener("touchend", f2);
                h_list       .addEventListener("touchstart", f1);
                h_list       .addEventListener("touchend", f2);

                h_list_button.setAttribute("state", "off");
            } else {
                // h_list_button.style.borderTopLeftRadius = "0";
                // h_list_button.style.borderBottomLeftRadius = "0";
                // h_list_button.style.backgroundColor = "rgb(25, 25, 25)";
                h_list.style.display = "block";
                // h_list.style.borderTopRightRadius = "0";

                h_list_button.removeEventListener("mouseover", f1);
                h_list_button.removeEventListener("mouseout", f2);
                h_list       .removeEventListener("mouseover", f1);
                h_list       .removeEventListener("mouseout", f2);

                h_list_button.removeEventListener("touchstart", f1);
                h_list_button.removeEventListener("touchend", f2);
                h_list       .removeEventListener("touchstart", f1);
                h_list       .removeEventListener("touchend", f2);

                h_list_button.setAttribute("state", "on");
            }
        }
        h_list_button.addEventListener("mouseover", f1);
        h_list_button.addEventListener("mouseout", f2);
        h_list.addEventListener("mouseover", f1);
        h_list.addEventListener("mouseout", f2);
        h_list_button.addEventListener("click", f3);
    }
};









/* Anchor */
function getAnchor() {
    const url = new URL(window.location.href);
    return url.hash ? decodeURIComponent(url.hash.slice(1)) : null;
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
    filePath = decodeURIComponent(filePath).trim("/");
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
    return filePath;
    // const lastSlashIndex = filePath.lastIndexOf("/");
    // if (lastSlashIndex !== -1) {
    //     return filePath.substring(lastSlashIndex + 1);
    // }
    // return "";
}

/* Copy Download Code */
function copy(text) {
    const textarea = document.createElement("textarea");
    document.body.appendChild(textarea);
    textarea.value = text;
    textarea.select();
    document.execCommand("copy");
    document.body.removeChild(textarea);
}
function CopyCode(button_element) {
    let code_element = button_element.parentElement.parentElement.lastElementChild;

    const pre_element = document.createElement("pre");
    pre_element.innerHTML = code_element.innerHTML;
    if (!isCtrlPressed) {
        pre_element.querySelectorAll(".unselectable").forEach(
            element => element.remove()
        );
    }
    copy(pre_element.textContent);

    svg = '<svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg">'
    html1 = svg + '<polyline points="20 6 9 17 4 12"></polyline></svg><text class="unselectable">Copied!</text>';
    html2 = svg + '<path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text class="unselectable">Copy code</text>';

    button_element.innerHTML = html1;

    setTimeout(function() {
        button_element.innerHTML = html2;
    }, 1000);
}
function DownloadCode(button_element, filename) {
    code_element = button_element.parentElement.parentElement.lastElementChild;

    text = code_element.textContent;//.split("\n").slice(1).join("\n");
    const element = document.createElement("a");
    element.setAttribute("href", "data:text/plain;charset=utf-8," + encodeURIComponent(text));
    element.setAttribute("download", filename);
    element.style.display = "none";
    document.body.appendChild(element);
    element.click();
    document.body.removeChild(element);

    download_html = `<svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 3v4a1 1 0 0 1-1 1H5m5 4-2 2 2 2m4-4 2 2-2 2m5-12v16a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V7.914a1 1 0 0 1 .293-.707l3.914-3.914A1 1 0 0 1 9.914 3H18a1 1 0 0 1 1 1Z"/></svg><text class="unselectable" title="${filename}">Download code</text>`;
    downloaded_html = `<svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><polyline points="20 6 9 17 4 12"></polyline></svg><text class="unselectable" title="${filename}">Download!</text>`;

    button_element.innerHTML = downloaded_html;

    setTimeout(function() {
        button_element.innerHTML = download_html;
    }, 1000);
}



