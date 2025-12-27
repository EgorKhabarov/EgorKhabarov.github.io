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

    getParam(name, default_=undefined) {
        return this.parse().params[name] || default_;
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
