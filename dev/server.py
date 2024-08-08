from flask import Flask, send_file, send_from_directory, abort
from werkzeug.exceptions import NotFound


app = Flask(__name__)


@app.route("/")
def home():
    return send_file("../index.html")


@app.route("/<path:path>")
def index_html_path(path: str):
    if path.endswith("/"):
        path += "index.html"
    try:
        return send_from_directory("..", path)
    except (FileNotFoundError, NotFound):
        return abort(404, "FileNotFoundError")


# http://127.0.0.1:5000/cheatsheet
app.run("0.0.0.0", port=5000)
# , ssl_context=("cert.pem", "key.pem"))
