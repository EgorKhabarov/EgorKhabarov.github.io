from pathlib import Path

from flask import Flask, abort, redirect, request, send_from_directory

app = Flask(__name__)
DOCS_DIR = Path(__file__).resolve().parent.parent


def resolve_safe_path(path: str) -> Path | None:
    try:
        target = (DOCS_DIR / path).resolve()
        target.relative_to(DOCS_DIR)
        return target
    except (ValueError, OSError, RuntimeError):
        return None


def find_file(path: str) -> str | None:
    clean_path = path.lstrip("/")
    if not clean_path:
        candidates = [DOCS_DIR / "index.html"]
    else:
        target = resolve_safe_path(clean_path)
        if target is None:
            return None
        candidates = [target]
        if target.is_dir():
            candidates.append(target / "index.html")
        elif not target.suffix:
            html_target = resolve_safe_path(f"{clean_path}.html")
            if html_target is not None:
                candidates.append(html_target)
    for candidate in candidates:
        try:
            candidate.relative_to(DOCS_DIR)
        except ValueError:
            continue
        if candidate.is_file():
            return candidate.relative_to(DOCS_DIR).as_posix()
    return None


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def get_path(path: str):
    clean_path = path.lstrip("/")
    target = resolve_safe_path(clean_path) if clean_path else None
    if target and target.is_dir() and not path.endswith("/"):
        query = request.query_string.decode("latin-1")
        url = request.path + "/" + (f"?{query}" if query else "")
        return redirect(url, code=301)
    file_to_serve = find_file(path)
    if file_to_serve:
        return send_from_directory(DOCS_DIR, file_to_serve)
    error_page = resolve_safe_path("404.html")
    if error_page and error_page.is_file():
        return send_from_directory(DOCS_DIR, "404.html"), 404
    raise abort(404)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
