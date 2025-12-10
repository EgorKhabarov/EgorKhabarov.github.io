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
