import re
import json
import gzip
import html

from lunr import lunr
from pathlib import Path

from _dev.utils import get_files


def clean_text(text_: str):
    text_ = text_.lower()
    text_ = re.sub(r"\s+", " ", text_)
    text_ = re.sub(r"<[^>]+>", " ", text_)
    text_ = re.sub(r"\[([^]]+)]\(([^)]+)\)", r"\1 \2", text_)
    text_ = html.unescape(text_)
    text_ = re.sub(r"[^\wа-яА-ЯёЁ0-9._/\[\]()^&$#@!~=?№%*\\\s-]", " ", text_)
    text_ = re.sub(r"\s+", " ", text_)
    return text_.strip()


dir_name = "cheatsheet"
documents = []


for i, file in enumerate(get_files(dir_name, lambda _path: _path.endswith(".md"))):
    # print(file.removesuffix(".md"))
    text = Path("..", dir_name, file).read_text(encoding="UTF-8")
    file = file.removesuffix(".md")
    body = clean_text(text)
    documents.append({
        "i": str(i),
        "f": file,
        "n": file.replace("/", " "),
        "b": body
    })


index = lunr(
    ref="i",
    fields=[
        {"field_name": "n", "boost": 20},
        {"field_name": "b", "boost": 1},
    ],
    documents=documents,
    languages=["ru", "en"],
)
data = {
    "index": index.serialize(),
    "docs": [
        {"i": d["i"], "f": d["f"]}
        for d in documents
    ]
}

path = Path("..", dir_name, "cheatsheet_resources", "search-index.json")
json_str = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
# path.write_text(
#     json_str,
#     encoding="UTF-8",
# )
path_gz = Path(path.parent, "search-index.json.gz")
print(path_gz)
with gzip.open(path_gz, "wb") as file:
    file.write(json_str.encode("UTF-8"))
