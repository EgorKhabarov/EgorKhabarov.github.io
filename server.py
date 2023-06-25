from flask import Flask, send_file, abort
import os


app = Flask(__name__)

@app.route('/cheatsheet')
def cheatsheet():
    return send_file("cheatsheet/index.html")

@app.route('/<path:path>')
def index_html_path(path: str):
    try:
        path = "/" + path.lstrip(r".\/").replace("..", "")
        print(os.path.join(r"cheatsheet", *path.split('/')))

        return send_file(os.path.join(r"cheatsheet", *path.split('/')))
    except FileNotFoundError:
        return abort(404, "FileNotFoundError")

app.run()
