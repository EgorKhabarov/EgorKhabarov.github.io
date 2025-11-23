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
    }
}

/* --- BREADCRUMBS --- */
let currentPath = ["root"];
renderBreadcrumbs(currentPath);

function renderBreadcrumbs(pathArray) {
    breadcrumbsContainer.innerHTML = "";
    let accumulatedPath = [];
    pathArray.forEach((part, index) => {
        accumulatedPath.push(part);
        const currentFullPath = accumulatedPath.join("/");
        const span = document.createElement("span");
        span.textContent = part;
        span.className = "crumb_item";
        span.addEventListener("click", () => console.log(`Navigating to: ${currentFullPath}`));
        breadcrumbsContainer.appendChild(span);
        if (index < pathArray.length - 1) {
            const sep = document.createElement("span");
            sep.textContent = "/";
            sep.className = "crumb_separator";
            breadcrumbsContainer.appendChild(sep);
        }
    });
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
    sidebar.style.transform = `translateX(0%)`;
    overlay.style.opacity = 1;
    overlay.style.pointerEvents = "auto";
    sidebarOpen = true;
}
function closeSidebar() {
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























(function load_folder_list() {
    /*
    fetch("cheatsheet_resources/buttons_new.html")
        .then(response => response.text())
        .then(data => document.getElementById("folder_list").innerHTML = data);
    */
    css_colors = {
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
    function formatCheatsheetButton(title, svg) {
        return `<div class="tree_item file" title="${title}">${svg}<span class="label">${title}</span></div>`;
    }
    function formatFolderButton(title, svg, buttons_folder_data) {
        return `<div class="tree_group"><div class="tree_item folder" data-state="closed" title="{title}">${svg}<span class="label">${title}</span></div><div class="tree_children hidden">${buttons_folder_data}</div></div>`;
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
                textList.push(formatFolderButton(title, svg, buttonsFolderData));

            } else {
                // --- file/tag ---
                const vpath = `${directoryE}/${key}`.replace(/^\/+/, "");
                const svg = formatTagSvg(currentMetadata.color || "default");
                const tags = currentMetadata.tags;
                textList.push(formatCheatsheetButton(title, svg));
            }
        }
        return [textList.join(""), directory];
    }

    fetch("index.json")
        .then(response => response.json())
        .then(json_data => {
            document.getElementById("folder_list").innerHTML = generateButtons(json_data)[0];
    });
})();


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



