import os
from werkzeug.exceptions import NotFound
from flask import Flask, send_file, send_from_directory, abort, redirect


app = Flask(__name__)


@app.route("/")
def home():
    return send_file("../index.html")


@app.route("/<path:path>")
def index_html_path(path: str):
    if os.path.isdir(os.path.join("..", path)) and not path.endswith("/"):
        return redirect(f"/{path}/", code=302)

    if path.endswith("/"):
        path += "index.html"

    try:
        return send_from_directory("..", path)
    except (FileNotFoundError, NotFound):
        try:
            return send_from_directory("..", path + ".html")
        except (FileNotFoundError, NotFound):
            try:
                return send_from_directory("..", f"{path.rstrip("/")}/index.html")
            except (FileNotFoundError, NotFound):
                return abort(404, "FileNotFoundError")


# http://127.0.0.1:5000/cheatsheet
app.run("0.0.0.0", port=5000)
# , ssl_context=("cert.pem", "key.pem"))
