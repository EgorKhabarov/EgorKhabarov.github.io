/* --- ELEMENTS --- */
const sidebar = document.getElementById("cheatsheet_buttons");
const container = document.getElementById("main-container");
const overlay = document.getElementById("mobile-overlay");
const resizer = document.getElementById("resizer");
const settingsBtn = document.getElementById("settings-btn");
const themeBtn = document.getElementById("theme-btn");
const settingsModal = document.getElementById("settings-modal");
const closeSettingsBtn = document.getElementById("close-settings");
const settingsBackdrop = document.getElementById("settings-backdrop");
const searchInput = document.getElementById("search-input");
const breadcrumbsContainer = document.getElementById("breadcrumbs-row");
const body = document.body;
const folderList = document.querySelector(".folder-list");

let isSettingsOpen = false;

/* --- TREE VIEW LOGIC --- */
// Обработка кликов по дереву файлов
folderList.addEventListener("click", (e) => {

    // 1. Клик по папке (открытие/закрытие)
    const folderItem = e.target.closest(".tree-item.folder");
    if (folderItem) {
        e.stopPropagation(); // Чтобы не триггерить другие события
        toggleFolder(folderItem);
        return;
    }

    // 2. Клик по вертикальной линии (закрытие папки)
    // Проверяем, был ли клик по контейнеру tree-children
    if (e.target.classList.contains("tree-children")) {
        // Вычисляем позицию клика внутри элемента
        const rect = e.target.getBoundingClientRect();
        const clickX = e.clientX - rect.left;

        // Если клик был в зоне левой границы (примерно 15px с учетом padding)
        // Линия border-left (2px) + padding-left (5px) + запас
        if (clickX < 15) {
            e.stopPropagation();
            const parentGroup = e.target.closest(".tree-group");
            if (parentGroup) {
                const folderBtn = parentGroup.querySelector(".tree-item.folder");
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
    if (!childrenContainer || !childrenContainer.classList.contains("tree-children")) return;

    const iconUse = folderItem.querySelector("use");
    let isClosed = childrenContainer.classList.contains("hidden");

    if (forceClose) {
        isClosed = false; // Мы хотим закрыть, значит считаем что сейчас открыто
    }

    if (isClosed) {
        // Открыть
        childrenContainer.classList.remove("hidden");
        iconUse.setAttribute("href", "#icon-folder-open");
        folderItem.setAttribute("data-state", "open");
    } else {
        // Закрыть
        childrenContainer.classList.add("hidden");
        iconUse.setAttribute("href", "#icon-folder");
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
        span.className = "crumb-item";
        span.addEventListener("click", () => console.log(`Navigating to: ${currentFullPath}`));
        breadcrumbsContainer.appendChild(span);
        if (index < pathArray.length - 1) {
            const sep = document.createElement("span");
            sep.textContent = "/";
            sep.className = "crumb-separator";
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
    body.classList.add('no-select');
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
        body.classList.remove('no-select');
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