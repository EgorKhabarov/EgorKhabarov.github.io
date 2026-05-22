class ImageViewer {
    constructor({animateBack=true}) {
        this.animateBack = animateBack;
        this.boundImg = null;

        this.scale = 1;
        this.minScale = 1;
        this.maxScale = 5;
        this.x = 0;
        this.y = 0;
        this.dragging = false;
        this.startX = 0;
        this.startY = 0;

        this.lastTap = 0;
        this.pointers = new Map();
        this.pinchStartDist = 0;
        this.pinchStartScale = 1;

        this.createDOM();
        this.bind();
    }

    createDOM() {
        this.overlay = document.createElement("div");
        this.overlay.className = "ImageViewer-overlay";

        this.closeBtn = document.createElement("div");
        this.closeBtn.className = "ImageViewer-close";
        this.closeBtn.textContent = "✕";

        this.viewer = document.createElement("div");
        this.viewer.className = "ImageViewer-viewer";

        this.img = document.createElement("img");
        this.viewer.appendChild(this.img);

        this.overlay.appendChild(this.closeBtn);
        this.overlay.appendChild(this.viewer);
        document.body.appendChild(this.overlay);
    }

    bind() {
        this.closeBtn.addEventListener("click", e => {
            e.stopPropagation();
            this.close();
        });
        this.overlay.addEventListener("click", e => {
            if (e.target === this.overlay) {
                this.close();
            }
        });
        window.addEventListener("keydown", e => {
            if (e.key === "Escape") {
                this.close();
            }
        });
        window.addEventListener("resize", () => {
            if (this.overlay.classList.contains("ImageViewer-active")) {
                this.fit();
            }
        });

        this.viewer.addEventListener("pointerdown", e => this.onPointerDown(e));
        this.viewer.addEventListener("pointermove", e => this.onPointerMove(e));
        this.viewer.addEventListener("pointerup", e => this.onPointerUp(e));
        this.viewer.addEventListener("pointercancel", e => this.onPointerUp(e));
        this.viewer.addEventListener("wheel", e => this.onWheel(e), {passive: false});
    }

    attachTo(img) {
        if (this.boundImg) {
            this.boundImg.removeEventListener("click", this._openHandler);
        }
        this.boundImg = img;
        this._openHandler = () => this.open(img);
        img.addEventListener("click", this._openHandler);
    }

    open(img) {
        this.boundImg = img;
        this.img.src = img.src;
        this.overlay.classList.add("ImageViewer-active");
        document.body.style.overflow = "hidden";

        if (this.img.complete) {
            this.fit();
        } else {
            this.img.onload = () => this.fit();
        }
    }

    close() {
        if (!this.overlay.classList.contains("ImageViewer-active")) {
            return;
        }
        if (this.animateBack && this.boundImg) {
            const rect = this.boundImg.getBoundingClientRect();
            const cx = rect.left + rect.width / 2 - innerWidth / 2;
            const cy = rect.top + rect.height / 2 - innerHeight / 2;
            this.viewer.style.transition = "transform 0.35s cubic-bezier(0.4,0,0.2,1)";
            this.viewer.style.transform = `translate(${cx}px, ${cy}px) scale(0.1)`;
            setTimeout(() => this.finishClose(), 320);
        } else {
            this.finishClose();
        }
    }

    finishClose() {
        this.overlay.classList.remove("ImageViewer-active");
        document.body.style.overflow = "";
        this.viewer.style.transition = "";
    }

    fit() {
        const vw = innerWidth;
        const vh = innerHeight;
        this.scale = Math.min(vw / this.img.naturalWidth, vh / this.img.naturalHeight);
        this.minScale = this.scale;
        this.x = 0;
        this.y = 0;
        this.apply();
    }

    apply() {
        this.viewer.style.transform = `translate(${this.x}px, ${this.y}px) scale(${this.scale})`;
    }

    limits() {
        const vw = innerWidth;
        const vh = innerHeight;
        const w = this.img.naturalWidth * this.scale;
        const h = this.img.naturalHeight * this.scale;
        return {
            x: Math.max(0, (w - vw) / 2),
            y: Math.max(0, (h - vh) / 2),
        };
    }

    elastic(val, limit) {
        if (Math.abs(val) <= limit) {
            return val;
        }
        const excess = Math.abs(val) - limit;
        return Math.sign(val) * (limit + excess * 0.25);
    }

    shouldClose(val, limit) {
        return Math.abs(val) > limit + 90;
    }

    onPointerDown(e) {
        this.viewer.setPointerCapture(e.pointerId);
        this.pointers.set(e.pointerId, e);

        const now = Date.now();
        if (now - this.lastTap < 300 && this.pointers.size === 1) {
            this.toggleZoom(e.clientX, e.clientY);
        }
        this.lastTap = now;

        if (this.pointers.size === 1) {
            this.dragging = true;
            this.viewer.classList.add("ImageViewer-grabbing");
            this.startX = e.clientX - this.x;
            this.startY = e.clientY - this.y;
        }

        if (this.pointers.size === 2) {
            const pts = [...this.pointers.values()];
            this.pinchStartDist = Math.hypot(
                pts[0].clientX - pts[1].clientX,
                pts[0].clientY - pts[1].clientY,
            );
            this.pinchStartScale = this.scale;
            this.dragging = false;
        }
        e.preventDefault();
    }

    onPointerMove(e) {
        if (!this.pointers.has(e.pointerId)) {
            return;
        }
        this.pointers.set(e.pointerId, e);

        if (this.pointers.size === 1 && this.dragging) {
            const lim = this.limits();
            this.x = this.elastic(e.clientX - this.startX, lim.x);
            this.y = this.elastic(e.clientY - this.startY, lim.y);
            this.apply();
        }

        if (this.pointers.size === 2) {
            const pts = [...this.pointers.values()];
            const dist = Math.hypot(
                pts[0].clientX - pts[1].clientX,
                pts[0].clientY - pts[1].clientY,
            );
            const factor = dist / this.pinchStartDist;
            this.scale = Math.min(this.maxScale, Math.max(this.minScale, this.pinchStartScale * factor));
            this.apply();
        }
    }

    onPointerUp(e) {
        this.pointers.delete(e.pointerId);
        this.viewer.releasePointerCapture(e.pointerId);

        if (this.pointers.size === 0) {
            this.dragging = false;
            this.viewer.classList.remove("ImageViewer-grabbing");
            const lim = this.limits();
            if (this.shouldClose(this.x, lim.x) || this.shouldClose(this.y, lim.y)) {
                this.close();
            } else {
                this.x = Math.max(-lim.x, Math.min(lim.x, this.x));
                this.y = Math.max(-lim.y, Math.min(lim.y, this.y));
                this.apply();
            }
        }
    }

    onWheel(e) {
        e.preventDefault();
        const rect = this.viewer.getBoundingClientRect();
        const cx = e.clientX - rect.left;
        const cy = e.clientY - rect.top;
        const prev = this.scale;
        this.scale = Math.min(this.maxScale, Math.max(this.minScale, this.scale * (1 - e.deltaY * 0.001)));
        this.x -= (cx - rect.width / 2) * (this.scale / prev - 1);
        this.y -= (cy - rect.height / 2) * (this.scale / prev - 1);
        this.apply();
    }

    toggleZoom(px, py) {
        const rect = this.viewer.getBoundingClientRect();
        const cx = px - rect.left;
        const cy = py - rect.top;
        const target = this.scale > this.minScale * 1.5 ? this.minScale : Math.min(this.maxScale, this.minScale * 2.5);
        const prev = this.scale;
        this.scale = target;
        this.x -= (cx - rect.width / 2) * (this.scale / prev - 1);
        this.y -= (cy - rect.height / 2) * (this.scale / prev - 1);
        this.apply();
    }
}
