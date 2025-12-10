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
const breadcrumbsContainer = document.getElementById("breadcrumbs_content");
const body = document.body;
const folderList = document.getElementById("folder_list");
const folderSearchList = document.getElementById("folder_search_list");

const sidebarInput = document.getElementById("search_input");
const sidebarClear = document.getElementById("sidebar_clear");
const mainInput = document.getElementById("main_search_input");
const mainInputResultCount = document.getElementById("floating_search_result_count");
const mainClear = document.getElementById("main_clear");
const sidebarToggleBtn = document.getElementById("sidebar_toggle");
const tocSidebarToggleBtn = document.getElementById("toc_toggle");



/* Generic Sidebar */
class Drawer {
    constructor(elementId, overlayId, side = "left", resizer = null, edgeThreshold = 80) {
        this.el = document.getElementById(elementId);
        this.overlay = document.getElementById(overlayId);
        this.side = side; // "left" or "right"
        this.resizer = resizer;

        this.isOpen = false;
        this.isDragging = false;
        this.startX = 0;
        this.startY = 0;
        this.axisLocked = null; // "x" | "y" | null
        this.edgeThreshold = edgeThreshold; // px from edge to start swipe

        // Bind methods
        this.handleStart = this.handleStart.bind(this);
        this.handleMove = this.handleMove.bind(this);
        this.handleEnd = this.handleEnd.bind(this);
        this.handleClickOverlay = this.handleClickOverlay.bind(this);

        this.initListeners();
    }

    initListeners() {
        // Touch events
        document.addEventListener("touchstart", (e) => {
            // Ignore if dragging resize
            if (e.target.classList.contains("resizer")) return;
            if (e.touches[0].clientY < headerHeight) return;
            this.handleStart(e.touches[0].clientX, e.touches[0].clientY);
        }, {passive: false});

        document.addEventListener("touchmove", (e) => {
            // Ignore if dragging resize
            if (e.target.classList.contains("resizer")) return;
            this.handleMove(e.touches[0].clientX, e.touches[0].clientY, () => e.preventDefault());
        }, {passive: false});

        document.addEventListener("touchend", (e) => {
            this.handleEnd(e.changedTouches[0].clientX);
        });

        document.addEventListener("mousedown", (e) => {
            if (e.button !== 0) return;
            if (e.clientY < headerHeight) return;
            this.handleStart(e.clientX, e.clientY);
        });
        document.addEventListener("mousemove", (e) => {this.handleMove(e.clientX, e.clientY);});
        document.addEventListener("mouseup", (e) => {if (e.button === 0) this.handleEnd(e.clientX);});

        this.overlay.addEventListener("click", this.handleClickOverlay);
    }

    handleStart(x, y) {
        if (!isMobile() || isSettingsOpen) return;
        if (nowDrawer === null || nowDrawer === this) {} else return;

        this.startX = x;
        this.startY = y;
        this.axisLocked = null;
        const func = () => {
            this.isDragging = true;
            this.el.classList.add("swiping");
            nowDrawer = this;
            body.classList.add("no_select");
        }

        // Logic depends on side
        if (this.side === "left") {
            if (!this.isOpen && x < this.edgeThreshold) {
                func();
            } else if (this.isOpen) {
                // If open, drag anywhere starts drag (usually to close)
                // But need to distinguish between left and right drawer if both open?
                // Overlay click handles close, drag handles swipe back
                func();
            }
        } else { // Right side
            const winW = window.innerWidth;
            this.startX = x;
            if (!this.isOpen && x > winW - this.edgeThreshold) {
                func();
            } else if (this.isOpen) {
                func();
            }
        }
    }

    handleMove(x, y, preventDefault) {
        if (!this.isDragging || !isMobile() || isSettingsOpen) return;

        const dx = x - this.startX;
        const dy = y - this.startY;

        // Detect axis once
        if (this.axisLocked === null) {
            if (Math.abs(dx) > 10) {
                this.axisLocked = "x"; // swipe drawer
            } else if (Math.abs(dy) > 10) {
                this.axisLocked = "y"; // scrolling - disable drawer
                this.isDragging = false;
                nowDrawer = null;
                this.el.classList.remove("swiping");
                body.classList.remove("no_select");
                return;
            } else {
                return; // still undecided
            }
        }

        if (this.axisLocked === "y") return;

        const winW = window.innerWidth;
        const w = this.el.getBoundingClientRect().width || winW * 0.85;
        const diff = x - this.startX;
        let translatePct = 0;

        if (this.side === "left") {
            // Opening: diff > 0. Closing: diff < 0.
            if (!this.isOpen) {
                let move = Math.min(Math.max(0, diff), w);
                translatePct = (move / w) * 100 - 100; // -100 to 0
            } else {
                let move = Math.min(0, Math.max(diff, -w));
                translatePct = (move / w) * 100; // 0 to -100
            }
        } else { // Right
            // Opening: diff < 0 (drag left). Closing: diff > 0.
            if (!this.isOpen) {
                let move = Math.min(0, Math.max(diff, -w)); // Negative values
                translatePct = 100 + (move / w) * 100; // 100 to 0
            } else {
                let move = Math.max(0, Math.min(diff, w));
                translatePct = (move / w) * 100; // 0 to 100
            }
        }

        if (Math.abs(diff) > 5 && preventDefault) {
            preventDefault();
        }

        this.el.style.transform = `translateX(${translatePct}%)`;

        // Opacity logic (shared)
        // 0% translate (open) -> opacity 1. +/-100% translate (closed) -> opacity 0
        let op = 1 - (Math.abs(translatePct) / 100);
        if (!this.isOpen && this.side === "left") op = (100 + translatePct) / 100;
        if (!this.isOpen && this.side === "right") op = (100 - translatePct) / 100;
        if (this.isOpen) op = 1 - (Math.abs(translatePct) / 100); // Works for left(neg) and right(pos) close moves

        this.overlay.style.opacity = Math.max(0, Math.min(1, op));
        this.overlay.style.pointerEvents = op > 0 ? "auto" : "none";
    }

    handleEnd(x) {
        if (!this.isDragging || !isMobile() || isSettingsOpen) return;
        this.isDragging = false;
        this.el.classList.remove("swiping");
        body.classList.remove("no_select");

        const w = this.el.getBoundingClientRect().width;
        const diff = x - this.startX;
        const threshold = w / 3;

        let shouldOpen = this.isOpen;

        if (this.side === "left") {
            if (!this.isOpen && diff > threshold) shouldOpen = true;
            else if (this.isOpen && diff < -threshold) shouldOpen = false;
        } else {
            if (!this.isOpen && diff < -threshold) shouldOpen = true;
            else if (this.isOpen && diff > threshold) shouldOpen = false;
        }

        if (shouldOpen) this.open();
        else this.close();
    }

    open() {
        if (!isMobile() || isSettingsOpen) return;
        if (nowDrawer === null || nowDrawer === this) {} else return;
        nowDrawer = this;
        this.el.style.transform = "translateX(0%)";
        this.overlay.style.opacity = 1;
        this.overlay.style.pointerEvents = "auto";
        this.isOpen = true;
    }

    close() {
        if (!isMobile() || isSettingsOpen || nowDrawer !== this) return;
        nowDrawer = null;
        const tx = this.side === "left" ? "-100%" : "100%";
        this.el.style.transform = `translateX(${tx})`;
        this.overlay.style.opacity = 0;
        this.overlay.style.pointerEvents = "none";
        this.isOpen = false;
    }

    toggle(display_class = null) {
        if (isMobile()) {
            if (this.isOpen) {
                this.close();
            } else {
                if (nowDrawer !== null && nowDrawer !== this) {
                    nowDrawer.close();
                }
                this.open();
            }
        } else {
            if (display_class) {
                const isDisplayed = this.el.classList.contains("display_none");
                localStorage.setItem(display_class, isDisplayed ? "flex" : "none");
                document.documentElement.style.setProperty(display_class, isDisplayed ? "flex" : "none");
            }
            this.el.classList.toggle("display_none");
            this.resizer.resizer.classList.toggle("display_none");
        }
    }

    handleClickOverlay() {
        if (this.isOpen) {
            this.close();
        }
    }
}

class PanelResizer {
    constructor(resizerId, containerId, varName, direction = "left") {
        this.resizer = document.getElementById(resizerId);
        this.container = document.getElementById(containerId);
        this.varName = varName; // CSS variable to update
        this.direction = direction; // "left" (resize left panel) or "right" (resize right panel)
        this.isResizing = false;

        // Constraints
        this.minPanel = 10; // %
        this.maxPanel = 40; // % (Total 100 - 30 center - 10 other min = 60 max, but let's be safe)

        this.init();
    }

    init() {
        const start = (e) => {
            if (e.type === "touchstart") e.preventDefault();
            this.isResizing = true;
            this.resizer.classList.add("active");
            body.classList.add("no_select");
        };

        const move = (clientX) => {
            if (!this.isResizing) return;
            const rect = this.container.getBoundingClientRect();
            let pct;

            if (this.direction === "left") {
                // Left sidebar width based on mouse X from left
                pct = ((clientX - rect.left) / rect.width) * 100;
            } else {
                // Right sidebar width based on mouse distance from right
                pct = ((rect.right - clientX) / rect.width) * 100;
            }

            // Constraints
            if (pct < this.minPanel) pct = this.minPanel;
            if (pct > this.maxPanel) pct = this.maxPanel; // 70 max if single, but here we have 2 sidebars

            document.documentElement.style.setProperty(this.varName, `${pct}%`);
        };

        const end = () => {
            if (this.isResizing) {
                this.isResizing = false;
                this.resizer.classList.remove("active");
                body.classList.remove("no_select");
                localStorage.setItem(this.varName, document.documentElement.style.getPropertyValue(this.varName))
            }
        };

        // Mouse
        this.resizer.addEventListener("mousedown", start);
        document.addEventListener("mousemove", (e) => move(e.clientX));
        document.addEventListener("mouseup", end);

        // Touch
        this.resizer.addEventListener("touchstart", start, {passive:false});
        document.addEventListener("touchmove", (e) => {
            if (this.isResizing) {
                e.preventDefault();
                move(e.touches[0].clientX);
            }
        }, {passive:false});
        document.addEventListener("touchend", end);
    }
}


function isMobile() {
    return window.innerWidth <= 768;
}


/* --- INITIALIZATION --- */
// Resizers
const leftResizer = new PanelResizer("resizer_left", "main_container", "--sidebar-left-width", "left");
const rightResizer = new PanelResizer("resizer_right", "main_container", "--sidebar-right-width", "right");
const resizer_list = [leftResizer, rightResizer];

// Drawers
const leftDrawer = new Drawer("cheatsheet_buttons", "mobile_overlay", "left", leftResizer);
const rightDrawer = new Drawer("toc_sidebar", "mobile_overlay", "right", rightResizer);
let nowDrawer = null;
const drawer_list = [leftDrawer, rightDrawer];
sidebarToggleBtn.addEventListener("click", () => leftDrawer.toggle("--sidebar-left-display"));
tocSidebarToggleBtn.addEventListener("click", () => rightDrawer.toggle("--sidebar-right-display"));




function setupClearButton(input, btn) {
    btn.addEventListener("click", () => {
        input.value = "";
        input.focus();
        input.dispatchEvent(new Event("input"));
    });
}
setupClearButton(sidebarInput, sidebarClear);
setupClearButton(mainInput, mainClear);

close_floating_search_btn.onclick = closeMainSearch;

function calcHeaderHeight() {
    const style = getComputedStyle(document.documentElement);
    const height1 = parseInt(removeSuffix(style.getPropertyValue("--header-row-height"), "px"));
    const height2 = parseInt(removeSuffix(style.getPropertyValue("--header-row-breadcrumbs-height"), "px"));
    return height1 + height2;
}
let headerHeight = calcHeaderHeight();

/* --- RESIZE FIX --- */
window.addEventListener("resize", () => {
    headerHeight = calcHeaderHeight();

    if (isMobile()) {
        drawer_list.forEach(d => {
            d.el.classList.remove("display_none");
        })
        resizer_list.forEach(r => {
            r.resizer.classList.remove("display_none");
        })
    } else {
        drawer_list.forEach(d => {
            d.el.style.transform = "";
            d.el.style.transition = "";
        })
        overlay.style.opacity = "";
        overlay.style.pointerEvents = "";
        if (nowDrawer) {
            nowDrawer.close();
            nowDrawer.isOpen = false;
            nowDrawer.isDragging = false;
        }
        nowDrawer = null;
    }
});


(function load_sidebar_width() {
    resizer_list.forEach(r => {
        let sidebar_width = localStorage.getItem(r.varName);
        if (sidebar_width === null) {
            sidebar_width = getComputedStyle(document.documentElement).getPropertyValue(r.varName);
            localStorage.setItem(r.varName, sidebar_width);
        }
        document.documentElement.style.setProperty(r.varName, sidebar_width.replace(/\..+(?=%)/, ""));
    });
    [
        ["--sidebar-left-display", cheatsheet_buttons, leftResizer],
        ["--sidebar-right-display", toc_sidebar, rightResizer],
    ].forEach(args => {
        c = args[0];
        e = args[1];
        r = args[2];

        let sidebar_display = localStorage.getItem(c);
        if (sidebar_display === null) {
            sidebar_display = getComputedStyle(document.documentElement).getPropertyValue(c);
            localStorage.setItem(c, sidebar_display);
        }
        document.documentElement.style.setProperty(c, sidebar_display);
        if (sidebar_display === "none") {
            e.classList.toggle("display_none");
            r.resizer.classList.toggle("display_none");
        }
    });
})();


/* --- KEYBOARD SHORTCUTS --- */
document.addEventListener("keydown", (e) => {
    // Ctrl + Shift + F -> Sidebar Search
    if (e.ctrlKey && e.shiftKey && e.code === "KeyF") {
        e.preventDefault();
        nowDrawer?.close();
        leftDrawer.open();
        const selection = window.getSelection().toString();
        sidebarInput.focus();
        if (selection && !selection.includes("\n")) {
            sidebarInput.value = selection;
            sidebarInput.dispatchEvent(new Event("input"));
        }
        sidebarInput.select();
        return;
    }

    // Ctrl + F -> Main Search
    if (e.ctrlKey && e.code === "KeyF") {
        e.preventDefault();
        floating_search.style.display = "flex";
        const selection = window.getSelection().toString();
        mainInput.focus();
        if (selection && !selection.includes("\n")) {
            mainInput.value = selection;
            mainInput.dispatchEvent(new Event("input"));
        } else if (last_search.length > 1) {
            mainInput.value = last_search;
            mainInput.dispatchEvent(new Event("input"));
            mainInput.select();
        }
        return;
    }

    // Ctrl + i -> Main Search
    if (e.ctrlKey && !e.shiftKey && e.code === "KeyI") {
        e.preventDefault();
        toggleSettings(!isSettingsOpen);
        return;
    }

    // Esc
    if (e.key === "Escape") {
        e.preventDefault();
        if (isSettingsOpen) {
            toggleSettings(false)
            return;
        }
        if (isMobile() && nowDrawer) {
            nowDrawer?.close();
            return;
        }
        if (floating_search.style.display === "flex") {
            closeMainSearch();
            return;
        }
        if (search_input.value) {
            closeSearch();
            return;
        }
        return;
    }

    // Alt + > || Alt + < -> Next selection | Prev selection
    if (floating_search.style.display === "flex"
        && e.altKey
        && (
            e.code === "Comma"
            || e.code === "Period"
        )
    ) {
        e.preventDefault();
        e.code === "Comma" ? prevHighlight() : nextHighlight();
        return;
    }
});


open_search_button.addEventListener("click", () => {
    if (floating_search.style.display === "none") {
        floating_search.style.display = "flex";
        mainInput.focus();
    } else {
        closeMainSearch();
    }
})


let isSettingsOpen = false;

function toggleFolder(folderItem, forceClose = false, cascadeClose = true) {
    const childrenContainer = folderItem.nextElementSibling;
    if (!childrenContainer || !childrenContainer.classList.contains("tree_children")) return;

    const iconUse = folderItem.querySelector("use");
    let isClosed = childrenContainer.classList.contains("hidden");

    if (forceClose) {
        isClosed = false;
    }

    if (isClosed) {
        childrenContainer.classList.remove("hidden");
        // iconUse.setAttribute("href", "#icon_folder_open");
        folderItem.setAttribute("data-state", "open");
    } else {
        childrenContainer.classList.add("hidden");
        // iconUse.setAttribute("href", "#icon_folder");
        folderItem.setAttribute("data-state", "closed");
        if (cascadeClose) {
            folderItem.nextElementSibling.querySelectorAll('[data-state="open"]').forEach(e => {
                e.setAttribute("data-state", "closed");
                e.nextElementSibling.classList.add("hidden");
            })
        }
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
        const span = document.createElement("a");
        span.textContent = part;
        span.className = "crumb_item";
        if (index === pathArray.length - 1) span.href = "?"+currentFullPath;
        span.addEventListener("click", (e) => {
            e.preventDefault();
            console.log(`Navigating to: ${currentFullPath}`);
            closeSearch();
            closeAllKeyButtons();
            nowDrawer?.close();
            leftDrawer.open();
            const button = (index === pathArray.length - 1)
                ? displayValueButton(currentFullPath)
                : displayKeyButton(currentFullPath);
            pulseHighlight(button);
        });
        breadcrumbsContainer.appendChild(span);
        if (index < pathArray.length - 1) {
            const sep = document.createElement("span");
            sep.textContent = "/";
            sep.className = "crumb_separator";
            breadcrumbsContainer.appendChild(sep);
        }
    });

    const anchor = urlArgs.getAnchor();
    if (anchor) {
        const sep = document.createElement("span");
        sep.textContent = "#";
        sep.className = "crumb_separator";
        breadcrumbsContainer.appendChild(sep);

        breadcrumbsContainer.appendChild(sep);
        const span = document.createElement("span");

        let anchor_tmp = anchor.toLowerCase().replaceAll("-", " ");
        span.textContent = anchor_tmp.slice(0, 1).toUpperCase()+anchor_tmp.slice(1);

        span.className = "crumb_item";
        span.addEventListener("click", () => {
            console.log(`Navigating to: #${anchor}`);
            const anchor_element = document.getElementById(anchor);
            if (anchor_element) {
                anchor_element.scrollIntoView({block: "start", behavior: "smooth"});
            }
            const anchor_toc_element = document.getElementById(`--toc--${anchor}`);
            if (anchor_toc_element) {
                anchor_toc_element.scrollIntoView({block: "start"});
                pulseHighlight(anchor_toc_element);
            }
        });
        breadcrumbsContainer.appendChild(span);
    }
}
function pulseHighlight(element, milliseconds=1000) {
    element.classList.add("pulse_bg");
    setTimeout(function() {
        element.classList.remove("pulse_bg");
    }, milliseconds);
}

/* --- THEME TOGGLE --- */
let isDark = true;
themeBtn.addEventListener("click", () => {
    isDark = !isDark;
    const themeColorMeta = document.querySelector('meta[name="theme-color"]');
    if (isDark) {
        document.documentElement.setAttribute("data-theme", "dark");
        themeColorMeta.setAttribute("content", "#1E1E1E");
        settings.theme = "dark";
        saveSettings(settings);
    } else {
        document.documentElement.removeAttribute("data-theme");
        themeColorMeta.setAttribute("content", "#FFFFFF");
        settings.theme = "light";
        saveSettings(settings);
    }
});

/* --- FULL-TEXT SEARCH --- */
let idx = null;
let docs = null;
let indexPromise = null;


async function loadIndexLazy() {
    if (idx) return;

    console.log('Load "cheatsheet_resources/search-index.json.gz"');
    let response = await fetch("cheatsheet_resources/search-index.json.gz");
    let data = null;
    try {
        data = await response.json();
    } catch (e) {
        response = await fetch("cheatsheet_resources/search-index.json.gz");
        const ds = new DecompressionStream("gzip");
        const decompressedStream = response.body.pipeThrough(ds);
        const text = await new Response(decompressedStream).text();
        data = JSON.parse(text);
    }

    idx = lunr.Index.load(data.index);
    docs = data.docs;
}
async function searchQuery(text) {
    if (!text.trim()) return [];

    if (typeof lunr === "undefined") {
        console.warn("lunr is not loaded!");
        return null;
    }
    if (!idx) await loadIndexLazy();
    const results = idx.search(text); // [{ref, score}, ...]
    return results.map(r => docs.find(d => d.i === r.ref));
}
function prepareQuery(q) {
    q = q.trim();
    q = q.replace(/:/g, " ");

    // ~
    q = q.replace(/~+(?!$|\d)/g, "");
    if (q.match(/(?<=~.{2,}).+(?=$)/g)) {
        q = q.replace(/\~+/g, "");
    }
    if (q.endsWith("~")) {
        q += "1";
    }

    // ^
    q = q.replace(/\^+(?!$|\d)/g, "");
    if (q.match(/(?<=\^.{2,}).+(?=$)/g)) {
        q = q.replace(/\^+/g, "");
    }
    if (q.endsWith("^")) {
        q += "1";
    }
    return q.replace(/\s+/g, " ").trim();
}
function debounce(fn, ms) {
    let timer;
    return function(...args) {
        clearTimeout(timer);
        timer = setTimeout(() => fn.apply(this, args), ms);
    };
}
function buildTree(paths) {
    const tree = {};

    paths.forEach(path => {
        const parts = path.split("/");
        let current = tree;

        parts.forEach((part, i) => {
            if (!current[part]) {
                current[part] = (i === parts.length - 1) ? "" : {};
            }
            current = current[part];
        });
    });

    return tree;
}
searchInput.addEventListener("input", debounce(async (e) => {
    const search_query = e.target.value;
    console.log("Search:", search_query, " || ", prepareQuery(search_query));
    if (search_query) {
        folderList.style.display = "none";
        folderSearchList.style.display = "block";
    } else {
        closeSearch();
        return;
    }

    urlArgs.setParam("s", search_query);
    let results = null;
    try {
        results = await searchQuery(prepareQuery(search_query));
        if (results.length === 0) {
            results = await searchQuery(`*${prepareQuery(search_query)}*`);
        }
        if (results.length === 0) {
            results = await searchQuery(`${prepareQuery(search_query)}~1`);
        }
    } catch (e) {
        console.error(e);
    }
    if (results === null) {
        folderSearchList.style.display = "flex";
        folderSearchList.style.alignItems = "center";
        folderSearchList.style.justifyContent = "center";
        folderSearchList.style.color = "red";
        folderSearchList.textContent = "An error occurred";
        searchInput.style.border = "1px solid red";
        return;
    }
    searchInput.style.border = null;
    generateButtons(buildTree(results.map(r => r.f)), folderSearchList, false);
    folderSearchList.querySelectorAll('[data-state="closed"]').forEach(e => {
        e.setAttribute("data-state", "open");
        e.nextElementSibling.classList.remove("hidden");
    })
    folderSearchList.querySelectorAll(".file").forEach(e => {
        e.onclick = async function(event) {
            urlArgs.setAnchor(null);
            const vpath = e.getAttribute("data-vpath")
            await setup_cheatsheet(vpath, false, false);

            floating_search.style.display = "flex";
            mainInput.value = search_query.trim();
            setTimeout(function() {
                mainInput.dispatchEvent(new Event("input"));
            }, 300);
        }
    });
    folderSearchList.querySelectorAll(".file").forEach(e => {
        const url = e.getAttribute("data-vpath");
        const e2 = folderList.querySelector(`[data-vpath="${url}"]`);
        if (e && e2) {
            e.firstChild.style.color = e2.firstChild.style.color;
        }
    });

    if (search_query && !folderSearchList.innerHTML) {
        folderSearchList.style.display = "flex";
        folderSearchList.style.alignItems = "center";
        folderSearchList.style.justifyContent = "center";
        folderSearchList.style.color = null;
        folderSearchList.textContent = "No results";
    } else if (folderSearchList.innerHTML !== "No results") {
        folderSearchList.style.alignItems = null;
        folderSearchList.style.justifyContent = null;
    } else {
        folderSearchList.style.display = null;
        folderSearchList.style.alignItems = null;
        folderSearchList.style.justifyContent = null;
        folderSearchList.style.color = null;
        folderSearchList.innerHTML = "";
    }
}, 500));
function closeSearch() {
    folderList.style.display = "block";
    folderSearchList.style.display = "none";
    folderSearchList.style.display = null;
    folderSearchList.style.alignItems = null;
    folderSearchList.style.justifyContent = null;
    folderSearchList.innerHTML = "";
    searchInput.value = "";
    searchInput.style.border = null;
    urlArgs.setParam("s", null);
}



function toggleSettings(show) {
    isSettingsOpen = show;
    if (show) settingsModal.classList.add("active");
    else settingsModal.classList.remove("active");
}
settingsBtn.addEventListener("click", () => toggleSettings(true));
closeSettingsBtn.addEventListener("click", () => toggleSettings(false));
settingsBackdrop.addEventListener("click", () => toggleSettings(false));



















let cheatsheet_cache = {};
async function load_cheatsheet(url) {
    let text = "";

    if (url in cheatsheet_cache) {
        text = cheatsheet_cache[url];
    } else {
        console.log(`Load "${url}.html"`)
        try {
            const response = await fetch(`${url}.html`);
            const tmp_text = await response.text();

            if (tmp_text.startsWith("<!-- 404.html -->")) {
                cheatsheet_field.innerHTML = `Sorry, this page isn't available`;
                cheatsheet_field.setAttribute("data-cheatsheet-path", "error-404");
                cheatsheet_cache[url] = null;
                return false;
            }

            if (tmp_text.trim() === "") {
                cheatsheet_field.innerHTML = `This page is empty`;
                cheatsheet_field.setAttribute("data-cheatsheet-path", "error-empty");
                cheatsheet_cache[url] = "";
                return true;
            }

            cheatsheet_cache[url] = tmp_text;
            text = tmp_text;
        } catch (e) {
            return false;
        }
    }

    if (text === null) {
        cheatsheet_field.innerHTML = `Sorry, this page isn't available`;
        cheatsheet_field.setAttribute("data-cheatsheet-path", "error-404");
        return true;
    }

    if (text === "") {
        cheatsheet_field.innerHTML = `This page is empty`;
        cheatsheet_field.setAttribute("data-cheatsheet-path", "error-empty");
        return true;
    }

    cheatsheet_field.innerHTML = text;
    cheatsheet_field.setAttribute("data-cheatsheet-path", url);
    processingCheatSheet();

    const anchor = urlArgs.getAnchor();
    if (anchor) {
        console.log(`Anchor found: "${anchor}"`);
        const anchor_element = document.getElementById(anchor);
        if (anchor_element) {
            anchor_element.scrollIntoView({block: "start"});
        }
        const anchor_toc_element = document.getElementById(`--toc--${anchor}`);
        if (anchor_toc_element) {
            anchor_toc_element.scrollIntoView({block: "start"});
            pulseHighlight(anchor_toc_element);
        }
    }
    return true;
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
    button.scrollIntoView({block: "center"});
    return button;
}
function displayValueButton(url, scrollIntoActive = true) {
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
    if (scrollIntoActive) {
        button?.scrollIntoView({block: "center"});
    }
    return button;
}
async function setup_cheatsheet(url_, setActive = true, scrollIntoActive = true) {
    const url = url_.trim("/");
    console.log(`Setup "${url}"`)
    renderBreadcrumbs(url);
    urlArgs.setMain(url);
    nowDrawer?.close();
    closeMainSearch();
    changeTitle(getPath(url));
    cheatsheet_field_container.scrollTo(0, 0);
    let successfully = await load_cheatsheet(url);

    if (successfully && setActive) {
        changeActiveButton(
            displayValueButton(url, scrollIntoActive)
        );
    }
}





function generateButtonsOnClick(event) {
    const cascadeClose = false;
    // 1. Click on a folder (open/close)
    const folderItem = event.target.closest(".tree_item.folder");
    if (folderItem) {
        event.stopPropagation();
        toggleFolder(folderItem, false, cascadeClose);
        return;
    }

    // 2. Click on the vertical line (close the folder)
    // Checking if there was a click on the tree_children container
    if (event.target.classList.contains("tree_children")) {
        // Calculate the click position within an element
        const rect = event.target.getBoundingClientRect();
        const clickX = event.clientX - rect.left;

        // If the click was in the left border area (approximately 15px taking into account padding)
        // Line border_left (2px) + padding_left (5px) + margin
        if (clickX < 15) {
            event.stopPropagation();
            const parentGroup = event.target.closest(".tree_group");
            if (parentGroup) {
                const folderBtn = parentGroup.querySelector(".tree_item.folder");
                if (folderBtn) {
                    toggleFolder(folderBtn, true, cascadeClose); // force close
                }
            }
        }
    }
}
function generateButtonsOnClickCascade(event) {
    const cascadeClose = true;
    // 1. Click on a folder (open/close)
    const folderItem = event.target.closest(".tree_item.folder");
    if (folderItem) {
        event.stopPropagation();
        toggleFolder(folderItem, false, cascadeClose);
        return;
    }

    // 2. Click on the vertical line (close the folder)
    // Checking if there was a click on the tree_children container
    if (event.target.classList.contains("tree_children")) {
        // Calculate the click position within an element
        const rect = event.target.getBoundingClientRect();
        const clickX = event.clientX - rect.left;

        // If the click was in the left border area (approximately 15px taking into account padding)
        // Line border_left (2px) + padding_left (5px) + margin
        if (clickX < 15) {
            event.stopPropagation();
            const parentGroup = event.target.closest(".tree_group");
            if (parentGroup) {
                const folderBtn = parentGroup.querySelector(".tree_item.folder");
                if (folderBtn) {
                    toggleFolder(folderBtn, true, cascadeClose); // force close
                }
            }
        }
    }
}
function generateButtons(json_data, element, cascadeClose = true) {
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
    function formatCheatsheetButton(title, svg, vpath, tags) {
        const dataTags = tags !== null && tags !== "" ? `data-search-tags="${tags}"` : "";
        return `<div class="tree_item file" title="${vpath}" data-vpath="${vpath}"${dataTags}>${svg}<span class="label">${title}</span></div>`;
    }
    function formatFolderButton(title, svg, kpath, display, buttons_folder_data) {
        const kstate = display ? "open" : "closed";
        const vstate = display ? "" : " hidden";
        return `<div class="tree_group"><div class="tree_item folder" data-state="${kstate}" title="${kpath}" data-kpath="${kpath}">${svg}<span class="label">${title}</span></div><div class="tree_children${vstate}">${buttons_folder_data}</div></div>`;
    }

    function __generateButtons(dictionary, directory = "") {
        const textList = [];
        for (const [key, value] of Object.entries(dictionary)) {
            if (key === ".") continue;
            //if (key === "index" || key === ".") continue;
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
                const buttonsFolderData = __generateButtons(value, keyPath)[0];
                const kpath = `${directoryE}/${key}`.replace(/^\/+/, "");
                const svg = formatFolderSvg(currentMetadata.color || "yellow");
                const display = currentMetadata["folder_open"];
                textList.push(formatFolderButton(title, svg, kpath, display, buttonsFolderData));

            } else {
                // --- file/tag ---
                const vpath = `${directoryE}/${key}`.replace(/^\/+/, "");
                const svg = formatTagSvg(currentMetadata.color || "default");
                const tags = currentMetadata.tags;
                textList.push(formatCheatsheetButton(title, svg, vpath, tags));
            }
        }
        return [textList.join(""), directory];
    }

    element.innerHTML = __generateButtons(json_data)[0];
    element.removeEventListener("click", cascadeClose ? generateButtonsOnClickCascade : generateButtonsOnClick);
    element.addEventListener("click", cascadeClose ? generateButtonsOnClickCascade : generateButtonsOnClick);
}

function init() {  // load_folder_list
    fetch("index.json")
        .then(response => response.json())
        .then(async (json_data) => {
            generateButtons(json_data, folderList);

            folderList.querySelectorAll(".file").forEach(e => {
                e.onclick = async function(event) {
                    urlArgs.setAnchor(null);
                    const vpath = e.getAttribute("data-vpath")
                    await setup_cheatsheet(vpath, true, false);
                };
            });

            const vpath = urlArgs.getMain() || "README";
            await setup_cheatsheet(vpath, true, true);

            const s_param = urlArgs.getParams().s;
            if (s_param) {
                sidebarInput.value = s_param;
                sidebarInput.dispatchEvent(new Event("input"));
            }
        });
}
init();


let isCtrlPressed = false;
document.addEventListener("keydown", function(event) {if (event.ctrlKey) {isCtrlPressed = true;}});
document.addEventListener("keyup", function(event) {if (!event.ctrlKey) {isCtrlPressed = false;}});
document.addEventListener("click", function(event) {
    if (event.target.tagName === "CODE") {
        if (event.target.classList.contains("code_no_copy")) {
            return;
        }
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
    element?.classList.add("tree_item_active");
}

function processingBlockQuote(blockquote) {
    if (blockquote.firstChild.textContent.toLowerCase().startsWith("[!note]\n")) {
        blockquote.classList.add("blockquote_note");
        // class="unselectable"
        // textContent
        blockquote.firstChild.innerHTML = `<p class="blockquote_alerts_p" style="color: var(--md-blockquote-note);"><svg><use href="#icon_md_blockquote_note"/></svg>Note</p>` + removePrefixIgnoreCase(blockquote.firstChild.innerHTML, "[!note]\n");

        blockquote.style.paddingBottom = "6px";
        blockquote.style.marginTop = "12px";
    } else if (blockquote.firstChild.textContent.toLowerCase().startsWith("[!tip]\n")) {
        blockquote.classList.add("blockquote_tip");
        blockquote.firstChild.innerHTML = `<p class="blockquote_alerts_p" style="color: var(--md-blockquote-tip);"><svg><use href="#icon_md_blockquote_tip"/></svg>Tip</p>` + removePrefixIgnoreCase(blockquote.firstChild.innerHTML, "[!tip]\n");

        blockquote.style.paddingBottom = "6px";
        blockquote.style.marginTop = "12px";
    } else if (blockquote.firstChild.textContent.toLowerCase().startsWith("[!important]\n")) {
        blockquote.classList.add("blockquote_important");
        blockquote.firstChild.innerHTML = `<p class="blockquote_alerts_p" style="color: var(--md-blockquote-important);"><svg><use href="#icon_md_blockquote_important"/></svg>Important</p>` + removePrefixIgnoreCase(blockquote.firstChild.innerHTML, "[!important]\n");

        blockquote.style.paddingBottom = "6px";
        blockquote.style.marginTop = "12px";
    } else if (blockquote.firstChild.textContent.toLowerCase().startsWith("[!warning]\n")) {
        blockquote.classList.add("blockquote_warning");
        blockquote.firstChild.innerHTML = `<p class="blockquote_alerts_p" style="color: var(--md-blockquote-warning);"><svg><use href="#icon_md_blockquote_warning"/></svg>Warning</p>` + removePrefixIgnoreCase(blockquote.firstChild.innerHTML, "[!warning]\n");

        blockquote.style.paddingBottom = "6px";
        blockquote.style.marginTop = "12px";
    } else if (blockquote.firstChild.textContent.toLowerCase().startsWith("[!caution]\n")) {
        blockquote.classList.add("blockquote_caution");
        blockquote.firstChild.innerHTML = `<p class="blockquote_alerts_p" style="color: var(--md-blockquote-caution);"><svg><use href="#icon_md_blockquote_caution"/></svg>Caution</p>` + removePrefixIgnoreCase(blockquote.firstChild.innerHTML, "[!caution]\n");

        blockquote.style.paddingBottom = "6px";
        blockquote.style.marginTop = "12px";
    }
}

function processingTables(table) {
    const wrapper = document.createElement("div");
    wrapper.classList.add("table_wrapper");
    table.parentNode.insertBefore(wrapper, table);
    wrapper.appendChild(table);
}
function processingTOC(h_elements) {
    h_list.innerHTML = "";
    if (h_elements.length !== 0) {
        h_list.classList.remove("empty");
        const min_header = Math.min(...Array.from(h_elements).map((header) => {return Number(header.tagName[1])}));
        const color_map = {
            1: "var(--color-h1)",
            2: "var(--color-h2)",
            3: "var(--color-h3)",
            4: "var(--color-h4)",
            5: "var(--color-h5)",
            6: "var(--color-h6)",
        }
        const indent_map = {
            1: "",
            2: "&nbsp;".substring((min_header * 6) - 6),
            3: "&nbsp;&nbsp;".substring((min_header * 6) - 6),
            4: "&nbsp;&nbsp;&nbsp;".substring((min_header * 6) - 6),
            5: "&nbsp;&nbsp;&nbsp;&nbsp;".substring((min_header * 6) - 6),
            6: "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;".substring((min_header * 6) - 6),
        }
        h_elements.forEach(header => {
            const h_num = Number(header.tagName[1]);
            const color = color_map[h_num];
            const indent = indent_map[h_num];
            const element = document.createElement("span");
            element.classList.add("toc_item");
            const header_id = header.id;
            element.onclick = () => {
                rightDrawer.close();
                document.getElementById(header_id)?.scrollIntoView({block: "start", behavior: "smooth"});
            };
            element.title = header.textContent;
            element.id = `--toc--${header_id}`;

            const element_indent = document.createElement("pre");
            element_indent.innerHTML = indent;

            const element_pre = document.createElement("pre");
            element_pre.style.color = color;
            element_pre.textContent = header.tagName;

            const element_span = document.createElement("pre");
            element_span.classList.add("label");
            element_span.textContent = header.textContent;

            element_indent.appendChild(element_pre);

            element.appendChild(element_indent);
            element.appendChild(element_span);
            h_list.appendChild(element);
        });
    } else {
        h_list.classList.add("empty");
        h_list.textContent = "Headings will appear here if they are in the cheat sheet";
    }
}
function processingCheatSheet() {
    cheatsheet_field.querySelectorAll("a").forEach(a => {
        if (
            a.target == ""
            && a.getAttribute("href")[0] !== "#"
            && a.getAttribute("href")[0] !== "?"
        ) {
            a.target = "_blank";
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
    const h_elements = cheatsheet_field.querySelectorAll("h1, h2, h3, h4, h5, h6");
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
    cheatsheet_field.querySelectorAll("table").forEach(processingTables);
    processingTOC(h_elements);
};







/* URL Path */
function myEncodeURIComponent(str) {
    return encodeURIComponent(str)
        .replace(/%2F/g, "/")
        .replace(/%20/g, "+");
}
function myDecodeURIComponent(str) {
    return decodeURIComponent(str)
        .replace(/\+/g, " ")
}
class UrlArgs {
    constructor() {
        this.isInPopstate = false;
    }

    parse() {
        const url = new URL(window.location.href);
        const anchor = url.hash ? myDecodeURIComponent(url.hash.substring(1)) : null;

        const query = url.search.substring(1);
        if (!query) return {main: null, params: {}, anchor};

        const parts = query.split("&");
        let main = null;
        const params = {};

        for (const p of parts) {
            if (!p) continue;

            const eq = p.indexOf("=");

            if (eq === -1) {
                if (main === null) main = myDecodeURIComponent(p);
                continue;
            }

            const key = myDecodeURIComponent(p.substring(0, eq));
            const value = myDecodeURIComponent(p.substring(eq + 1));
            params[key] = value;
        }

        return {main, params, anchor};
    }

    buildSearch(main, params) {
        const parts = [];

        if (main) parts.push(myEncodeURIComponent(main));

        for (const [k, v] of Object.entries(params)) {
            parts.push(
                myEncodeURIComponent(k) + "=" + myEncodeURIComponent(v)
            );
        }

        return parts.length ? "?" + parts.join("&") : "";
    }

    commit(url) {
        const oldHref = window.location.href;
        const newHref = url.toString();
        if (oldHref === newHref) return;

        console.log("QQQ", newHref);
        if (this.isInPopstate) {
            history.replaceState({}, "", newHref);
        } else {
            history.pushState({}, "", newHref);
        }

        this.isInPopstate = false;
    }

    // MAIN

    getMain() {
        return this.parse().main;
    }

    setMain(value) {
        const parsed = this.parse();
        const url = new URL(window.location.href);

        parsed.main = value ? String(value) : null;

        url.search = this.buildSearch(parsed.main, parsed.params);
        url.hash = parsed.anchor ? "#" + myEncodeURIComponent(parsed.anchor) : "";

        this.commit(url);
    }

    // PARAMS

    getParams() {
        return this.parse().params;
    }

    setParam(name, value) {
        const parsed = this.parse();
        const url = new URL(window.location.href);

        if (!value) {
            delete parsed.params[name];
        } else {
            parsed.params[name] = String(value);
        }

        url.search = this.buildSearch(parsed.main, parsed.params);
        url.hash = parsed.anchor ? "#" + myEncodeURIComponent(parsed.anchor) : "";

        // Всегда replaceState
        history.replaceState({}, "", url.toString());
    }

    // ANCHOR

    getAnchor() {
        return this.parse().anchor;
    }

    setAnchor(value) {
        const parsed = this.parse();
        const url = new URL(window.location.href);

        url.search = this.buildSearch(parsed.main, parsed.params);
        url.hash = value ? "#" + myEncodeURIComponent(value) : "";

        this.commit(url);
    }
}

const urlArgs = new UrlArgs();


window.onpopstate = async () => {
    let vpath = urlArgs.getMain() || "README";

    console.log("Back to:", `"${vpath}"`);

    urlArgs.isInPopstate = true;
    await setup_cheatsheet(vpath, true, true);
};
window.addEventListener("hashchange", () => {
    renderBreadcrumbs(urlArgs.getMain());
})


/* Title */
function changeTitle(title) {
    let result = "Cheat sheet";
    if (title) {
        result += ": " + title;
    }
    document.getElementsByTagName("title")[0].textContent = result;
}

/* Path */
function getPathWithoutFilename(filePath) {
    const path = getPath(filePath);
    if (path.endsWith("/")) {
        return path
    }
    const lastSlashIndex = path.lastIndexOf("/");
    if (lastSlashIndex !== -1) {
        return path.substring(0, lastSlashIndex);
    }
   return "";
}
function getPath(filePath) {
    return decodeURIComponent(filePath).trim("/");;
}
function getPathFilename(filePath) {
    const path = getPath(filePath);
    const lastSlashIndex = path.lastIndexOf("/");
    if (lastSlashIndex !== -1) {
        return path.substring(lastSlashIndex + 1);
    }
    return path;
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

    html1 = '<svg width="1.2em" height="1.2em" viewBox="0 0 24 24"><use href="#icon_code_done"/></svg><text class="unselectable">Copied!</text>';
    html2 = '<svg width="1.2em" height="1.2em" viewBox="0 0 24 24"><use href="#icon_code_copy"/></svg><text class="unselectable">Copy code</text>';

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

    download_html = `<svg width="1.2em" height="1.2em" viewBox="0 0 24 24"><use href="#icon_code_download"/></svg><text class="unselectable" title="${filename}">Download code</text>`;
    downloaded_html = `<svg width="1.2em" height="1.2em" viewBox="0 0 24 24"><use href="#icon_code_done"/></svg><text class="unselectable" title="${filename}">Download!</text>`;

    button_element.innerHTML = downloaded_html;

    setTimeout(function() {
        button_element.innerHTML = download_html;
    }, 1000);
}



function loadSettings() {
    const settings = localStorage.getItem("settings");
    let s = settings ? JSON.parse(settings) : {
        "theme": "dark",
        "breadcrumbs": true,
        "settings_css_markdown_preview": true,
        "settings_css": "",
    };
    if (s.theme === undefined) {
        s.theme = "dark";
    }
    if (s.breadcrumbs === undefined) {
        s.breadcrumbs = true;
    }
    if (s.settings_css_markdown_preview === undefined) {
        s.settings_css_markdown_preview = true;
    }
    if (s.settings_css === undefined) {
        s.settings_css = "";
    }
    return s;
}
function saveSettings(settings) {
    localStorage.setItem(
        "settings",
        JSON.stringify(settings)
    );
}
function applySettings(settings) {
    const themeColorMeta = document.querySelector('meta[name="theme-color"]');
    if (settings.theme === "dark") {
        document.documentElement.setAttribute("data-theme", "dark");
        themeColorMeta.setAttribute("content", "#1E1E1E");
        isDark = true;
    } else {
        document.documentElement.removeAttribute("data-theme");
        themeColorMeta.setAttribute("content", "#FFFFFF");
        isDark = false;
    }
    settings_css_markdown_preview.checked = settings.settings_css_markdown_preview;
    settings_breadcrumbs_input.checked = settings.breadcrumbs;
    settings_css_textarea.value = settings.settings_css || "";
    settings_css.textContent = settings.settings_css || "";
}
function css_markdown_preview_func(element) {
    if (element.checked) {
        css_markdown_preview.textContent = `

:root {
    --color-h1: #FF0000;
    --color-h2: #FA7300;
    --color-h3: #FFCA00;
    --color-h4: #00FF00;
    --color-h5: #00A0F5;
    --color-h6: #DD00F2;
    --md-color-b: #F3AB06;
    --md-color-i: #8088C1;
    --md-color-bi: #C39990;
}

[data-theme="dark"] {
    --color-h3: #FFFA00;
}

.cheatsheet_field h1 {color: var(--color-h1);}
.cheatsheet_field h2 {color: var(--color-h2);}
.cheatsheet_field h3 {color: var(--color-h3);}
.cheatsheet_field h4 {color: var(--color-h4);}
.cheatsheet_field h5 {color: var(--color-h5);}
.cheatsheet_field h6 {color: var(--color-h6);}

.cheatsheet_field b, strong    {color: var(--md-color-b);}
.cheatsheet_field i, em        {color: var(--md-color-i);}
.cheatsheet_field strong em, i {color: var(--md-color-bi);}
.cheatsheet_field      b em, i {color: var(--md-color-bi);}
.cheatsheet_field em strong, b {color: var(--md-color-bi);}
.cheatsheet_field  i strong, b {color: var(--md-color-bi);}

strong:has(em), em:has(strong) {color: var(--md-color-bi)!important;}


.cheatsheet_field h1:before {content: "# ";      white-space: nowrap;}
.cheatsheet_field h2:before {content: "## ";     white-space: nowrap;}
.cheatsheet_field h3:before {content: "### ";    white-space: nowrap;}
.cheatsheet_field h4:before {content: "#### ";   white-space: nowrap;}
.cheatsheet_field h5:before {content: "##### ";  white-space: nowrap;}
.cheatsheet_field h6:before {content: "###### "; white-space: nowrap;}
.cheatsheet_field code:before, code:after {content: "\`";}
.cheatsheet_field mark:before, mark:after {content: "==";}
.cheatsheet_field i:before, i:after,     em:before,     em:after {content: "_"}
.cheatsheet_field b:before, b:after, strong:before, strong:after {content: "**"}

`;
        settings.settings_css_markdown_preview = true;
        saveSettings(settings);
    } else {
        css_markdown_preview.textContent = "";
        settings.settings_css_markdown_preview = false;
        saveSettings(settings);
    }
}
function settings_breadcrumbs_func(element) {
    if (!element.checked) {
        settings_breadcrumbs_style.textContent = `
#breadcrumbs_row {display: none;}
:root {--header-total-height: 40px;}
.header_row.bottom {display: none;}
`;
        settings.breadcrumbs = false;
        saveSettings(settings);
    } else {
        settings_breadcrumbs_style.textContent = "";
        settings.breadcrumbs = true;
        saveSettings(settings);
    }
}

let settings = loadSettings();
applySettings(settings);
css_markdown_preview_func(settings_css_markdown_preview)
settings_breadcrumbs_func(settings_breadcrumbs_input)





let highlightRanges = [];
let activeIndex = -1;

function parseSearchQuery(query, inputEl) {
    // Let's try to determine the format of /pattern/flags
    if (
        query.startsWith("/")
        && query.lastIndexOf("/") > 0
        && query.slice(1, query.lastIndexOf("/")).length !== 0
    ) {
        const lastSlash = query.lastIndexOf("/");
        const pattern = query.slice(1, lastSlash);
        const flags = query.slice(lastSlash + 1);

        try {
            const regex = new RegExp(pattern, flags);
            inputEl.style.border = ""; // OK
            mainInputResultCount.style.color = null;
            mainInputResultCount.textContent = "0 results";
            return regex;
        } catch (e) {
            // RegExp syntax error
            inputEl.style.border = "1px solid red";
            mainInputResultCount.style.color = "red";
            mainInputResultCount.textContent = "Bad pattern";
            return null;
        }
    }

    // A regular line
    inputEl.style.border = "";
    mainInputResultCount.style.color = null;
    mainInputResultCount.textContent = "0 results";
    return query;
}
function clearHighlight() {CSS.highlights.delete("search_highlight");}
function getTextNodes(root) {
    const nodes = [];
    const walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT);
    let node;
    while ((node = walker.nextNode())) {
        nodes.push(node);
    }
    return nodes;
}
function locatePositionInNodes(nodes, globalIndex) {
    let pos = 0;

    for (const node of nodes) {
        const len = node.textContent.length;

        if (globalIndex < pos + len) {
            return {
                node,
                offset: globalIndex - pos
            };
        }
        pos += len;
    }
    return null;
}
function highlightText(rawQuery, cheatsheetField, inputEl) {
    clearHighlight();

    const parsed = parseSearchQuery(rawQuery, inputEl);
    if (parsed === null || !parsed) {
        highlightRanges = [];
        activeIndex = -1;
        CSS.highlights.delete("active_search_highlight");
        return;
    }

    const nodes = getTextNodes(cheatsheetField);
    const fullText = nodes.map(n => n.textContent).join("");

    let matches = [];

    if (parsed instanceof RegExp) {
        let m;
        const regex = new RegExp(parsed.source, parsed.flags.includes("g") ? parsed.flags : parsed.flags + "g");
        while ((m = regex.exec(fullText)) !== null) {
            matches.push({ start: m.index, end: m.index + m[0].length });
            if (m[0].length === 0) regex.lastIndex++;
        }
    } else {
        const q = parsed.toLowerCase();
        const lower = fullText.toLowerCase();
        let pos = 0;
        while (true) {
            const i = lower.indexOf(q, pos);
            if (i === -1) break;
            matches.push({ start: i, end: i + q.length });
            pos = i + q.length;
        }
    }

    highlightRanges = [];
    activeIndex = -1;
    CSS.highlights.delete("active_search_highlight");

    if (!matches.length) return;

    const allRanges = [];

    for (const m of matches) {
        const startPos = locatePositionInNodes(nodes, m.start);
        const endPos = locatePositionInNodes(nodes, m.end);

        if (startPos && endPos) {
            const r = new Range();
            r.setStart(startPos.node, startPos.offset);
            r.setEnd(endPos.node, endPos.offset);
            allRanges.push(r);
        }
    }


    mainInputResultCount.style.color = null;
    mainInputResultCount.textContent = `1/${allRanges.length}`;
    if (!allRanges.length) return;

    highlightRanges = allRanges;

    const highlight = new Highlight(...allRanges);
    CSS.highlights.set("search_highlight", highlight);
}
function scrollRangeIntoView(range) {
    // const sel = window.getSelection();
    // const prevRange = sel.rangeCount ? sel.getRangeAt(0) : null;

    // sel.removeAllRanges();
    // sel.addRange(range);

    range.startContainer.parentElement?.scrollIntoView({
        block: "center",
        inline: "nearest",
        behavior: "smooth"
    });

    // sel.removeAllRanges();
    // if (prevRange) {
    //     sel.addRange(prevRange);
    // }
}
function setActiveHighlight(index) {
    if (highlightRanges.length === 0) return;

    activeIndex = ((index % highlightRanges.length) + highlightRanges.length) % highlightRanges.length;

    const activeRange = highlightRanges[activeIndex];

    CSS.highlights.set("active_search_highlight", new Highlight(activeRange));

    scrollRangeIntoView(activeRange);
    mainInputResultCount.style.color = null;
    mainInputResultCount.textContent = `${activeIndex+1}/${highlightRanges.length}`;
}
function nextHighlight() {
    if (highlightRanges.length === 0) return;
    setActiveHighlight(activeIndex + 1);
}
function prevHighlight() {
    if (highlightRanges.length === 0) return;
    setActiveHighlight(activeIndex - 1);
}

floating_search_arrow_up.onclick = prevHighlight;
floating_search_arrow_down.onclick = nextHighlight;


let last_search = "";
mainInput.addEventListener("input", () => {
    if (mainInput.value !== "") {
        console.log(`"${mainInput.value}"`);
        last_search = mainInput.value;
    }
    highlightText(mainInput.value, cheatsheet_field, mainInput);
    nextHighlight();
});

function closeMainSearch() {
    mainInput.value = "";
    mainInput.dispatchEvent(new Event("input"));
    floating_search.style.display = "none";
}

function reset_settings() {
    const settings_css = JSON.parse(localStorage.getItem("settings")).settings_css;
    localStorage.clear();
    localStorage.setItem("settings", JSON.stringify({settings_css}));
    location.reload();
}
reset_all_settings.onclick = reset_settings;



class ContextMenu {
    /**
     * @param {Array} items  - массив пунктов:
     *   { action: "key", label: "Text", icon?: "iconId" }
     *   или "separator"
     *
     * @param {string} itemSelector
     * @param {function} onAction(action, element)
     */
    constructor(items, itemSelector, onAction) {
        this.items = items;
        this.itemSelector = itemSelector;
        this.onAction = onAction;

        this.menu = this.createMenuElement();
        this.longPressTimer = null;
        this.targetElement = null;

        document.body.appendChild(this.menu);
        this.init();
    }

    createMenuElement() {
        const menu = document.createElement("div");
        menu.className = "context_menu";
        menu.style.position = "absolute";
        menu.style.display = "none";

        for (const item of this.items) {
            if (item === "separator") {
                menu.appendChild(document.createElement("hr"));
                continue;
            }

            const div = document.createElement("div");
            div.className = "context_menu_item";
            div.dataset.action = item.action;

            if (item.icon) {
                const svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
                if (item.attrs) {
                    for (const attr in item.attrs) {
                        svg.setAttribute(attr, item.attrs[attr]);
                    }
                }
                const use = document.createElementNS("http://www.w3.org/2000/svg", "use");
                use.setAttribute("href", `#${item.icon}`);
                svg.appendChild(use);
                div.appendChild(svg);
            } else {
                const svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
                div.appendChild(svg);
            }

            const text = document.createElement("span");
            text.textContent = item.label;
            div.appendChild(text);
            menu.appendChild(div);
        }
        return menu;
    }

    init() {
        document.addEventListener("contextmenu", (e) => this.onContextMenu(e));

        document.addEventListener("touchstart", (e) => this.onTouchStart(e));
        document.addEventListener("touchend", () => this.clearLongPress());
        document.addEventListener("touchcancel", () => this.clearLongPress());

        document.addEventListener("pointerdown", (e) => this.onPointerDown(e));
        window.addEventListener("scroll", () => this.hide(), true);
        window.addEventListener("resize", () => this.hide());
        window.addEventListener("blur", () => this.hide());

        document.addEventListener("keydown", (e) => {
            if (e.key === "Escape") this.hide();
        });

        this.menu.addEventListener("click", (e) => this.onMenuClick(e));
    }

    isInsideMenu(e) {
        return !!e.target.closest(".context_menu");
    }

    clearLongPress() {
        clearTimeout(this.longPressTimer);
    }

    show(x, y, target) {
        this.targetElement = target;

        this.menu.style.display = "block";
        this.menu.style.left = "0px";
        this.menu.style.top = "0px";

        const rect = this.menu.getBoundingClientRect();
        const screenW = window.innerWidth;
        const screenH = window.innerHeight;

        let left = x - window.scrollX;
        let top = y - window.scrollY;

        if (left + rect.width > screenW) left = screenW - rect.width - 5;
        if (top + rect.height > screenH) top = screenH - rect.height - 5;

        if (left < 5) left = 5;
        if (top < 5) top = 5;

        this.menu.style.left = left + window.scrollX + "px";
        this.menu.style.top = top + window.scrollY + "px";
    }

    hide() {
        if (this.menu.style.display === "none") return;
        this.menu.style.display = "none";
        this.targetElement = null;
    }

    onContextMenu(e) {
        const item = e.target.closest(this.itemSelector);
        if (item) {
            e.preventDefault();
            this.show(e.pageX, e.pageY, item);
        } else {
            this.hide();
        }
    }

    onTouchStart(e) {
        const item = e.target.closest(this.itemSelector);
        if (!item) return;

        let moved = false;

        const onMove = () => moved = true;
        const cleanup = () => {
            document.removeEventListener("touchmove", onMove);
            document.removeEventListener("touchend", onEnd);
            document.removeEventListener("touchcancel", onCancel);
        };

        const onEnd = () => { this.clearLongPress(); cleanup(); };
        const onCancel = () => { this.clearLongPress(); cleanup(); };

        document.addEventListener("touchmove", onMove, { passive: true });
        document.addEventListener("touchend", onEnd);
        document.addEventListener("touchcancel", onCancel);

        this.longPressTimer = setTimeout(() => {
            if (moved) return;
            const touch = e.touches[0] || e.changedTouches[0];
            this.show(touch.pageX, touch.pageY, item);
            cleanup();
        }, 500);
    }

    onPointerDown(e) {
        if (this.isInsideMenu(e)) return;

        if (!e.target.closest(this.itemSelector)) {
            this.hide();
        } else {
            this.hide();
        }
    }

    onMenuClick(e) {
        const item = e.target.closest(".context_menu_item");
        if (!item) return;

        const action = item.dataset.action;
        if (!action) return;

        if (this.onAction && this.targetElement) {
            this.onAction(action, this.targetElement);
        }

        this.hide();
    }
}




const menu_file = new ContextMenu(
    [
        {action: "open_in_new_tab", label: "Открыть в новой вкладке", icon: "icon_open_new_tab"},
        {action: "open_raw", label: "Открыть в сыром виде", icon: "icon_raw"},
        /* {action: "open_in_split_screen_mode", label: "Открыть в режиме разделения экрана"}, */
        {action: "open_in_github", label: "Открыть на GitHub", icon: "github_logo"},
        {action: "copy_file_name", label: "Скопировать название шпаргалки", icon: "icon_clipboard"},
        {action: "copy_path", label: "Скопировать путь", icon: "icon_clipboard"},
        /*
        "separator",
        {action: "to_favorites", label: "Добавить в избранное", icon: "favorites", attrs: {color: "currentColor"}},
        {action: "delete_from_favorites", label: "Удалить из избранного"},
        */
    ],
    ".tree_item.file",
    (action, element) => {
        console.log(`${action} ${element.dataset.vpath}`);
        const vpath = element.dataset.vpath;
        const base_github_url = "https://github.com/EgorKhabarov/EgorKhabarov.github.io/blob/master/cheatsheet/";

        if (action === "copy_path") {
            copy(element.dataset.vpath);
        } else if (action === "copy_file_name") {
            copy(getPathFilename(element.dataset.vpath));
        } else if (action === "open_in_new_tab") {
            window.open("?"+vpath, "_blank");
        } else if (action === "open_raw") {
            window.open(vpath+".md", "_blank");
        } else if (action === "open_in_github") {
            window.open(base_github_url+vpath+".md", "_blank");
        }
    }
);

const menu_folder = new ContextMenu(
    [
        {action: "open_in_github", label: "Открыть на GitHub", icon: "github_logo"},
        {action: "copy_folder_name", label: "Скопировать название папки", icon: "icon_clipboard"},
        {action: "copy_path", label: "Скопировать путь", icon: "icon_clipboard"},
    ],
    ".tree_item.folder",
    (action, element) => {
        console.log(`${action} ${element.dataset.kpath}`);
        const kpath = element.dataset.kpath;
        const base_github_url = "https://github.com/EgorKhabarov/EgorKhabarov.github.io/blob/master/cheatsheet/";

        if (action === "copy_path") {
            copy(kpath);
        } else if (action === "copy_folder_name") {
            copy(getPathFilename(kpath));
        } else if (action === "open_in_github") {
            window.open(base_github_url+kpath, "_blank");
        }
    }
);

