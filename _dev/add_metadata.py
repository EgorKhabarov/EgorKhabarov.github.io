import json
import yaml

from bs4 import BeautifulSoup

from _dev.utils import PathDict


def add_metadata(path_: str, metadata: dict) -> None:
    with open("../cheatsheet/index.json", "r", encoding="UTF-8") as index_json_file:
        index_json: dict[str, str | dict[str, str | dict]] = json.load(index_json_file)
    path_dict = PathDict(index_json)
    result_metadata = yaml.safe_load(path_dict[path_]) or {}
    string_result_metadata = json.dumps(result_metadata, indent=4, ensure_ascii=False)
    print(f"\x1b[33mNow metadata\x1b[0m {string_result_metadata}")

    color = metadata.get("color") or None
    tags = (
        [
            str(tag)
            for tag_ in metadata.get("tags")
            if str(tag_)
            for tag in tag_.strip().split(" ")
        ]
        if any(metadata.get("tags", ()))
        else None
    )
    if not (color or tags):
        print("\x1b[31mNo new metadata\x1b[0m")
        return None

    if color:
        result_metadata["color"] = color

    if tags:
        result_tags = set(tags)
        if (
            "tags" in result_metadata
            and result_metadata["tags"]
            and isinstance(result_metadata["tags"], str)
        ):
            result_tags |= set(result_metadata["tags"].split(" "))
        string_tags = " ".join(result_tags)
        result_metadata["tags"] = string_tags

    string_result_metadata = json.dumps(result_metadata, indent=4, ensure_ascii=False)
    print(f"\x1b[32mNew metadata\x1b[0m {string_result_metadata}")
    if input('\x1b[31mTo approve, write "y" or "yes": \x1b[0m') in ("y", "yes"):
        path_dict[path_] = yaml.safe_dump(
            result_metadata, sort_keys=False, allow_unicode=True, indent=4
        )
        with open("../cheatsheet/index.json", "w", encoding="UTF-8") as index_json_file:
            json.dump(path_dict.data, index_json_file, indent=4, ensure_ascii=False)
        print("\x1b[32mMetadata updated successfully\x1b[0m")


def get_h_tags(path_: str) -> list[str]:
    with open(f"../cheatsheet/{path_}.html", "r", encoding="UTF-8") as file:
        soup = BeautifulSoup(file.read(), "html.parser")
    return [
        heading.text for heading in soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"])
    ]


path = """

""".strip()
add_metadata(
    path,
    {
        "color": "",
        "tags": [
            "",
            # *get_h_tags(path),
        ],
    },
)
