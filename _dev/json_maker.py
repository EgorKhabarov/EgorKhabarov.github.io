import os
import json


def make_full_json():
    try:
        with open("metadata.json", "r", encoding="UTF-8") as file:
            try:
                old_metadata = json.load(file)
            except json.decoder.JSONDecodeError:
                old_metadata = {}
    except FileNotFoundError:
        old_metadata = {}

    metadata = {}
    default_value = {}

    for directory, dirnames, filenames in os.walk("../cheatsheet"):
        directory = directory.replace("\\", "/").removeprefix("../cheatsheet").lstrip("/")

        for dirname in dirnames:
            path = f"{directory}/{dirname}/".lstrip("/")
            metadata[path] = old_metadata.get(path, default_value)

        for filename in filenames:
            if filename != "index.md" and filename.endswith(".md"):
                path = f"{directory}/{filename}"
                metadata[path] = old_metadata.get(path, default_value)

    with open("metadata.json", "w", encoding="UTF-8") as file:
        json.dump(metadata, file, indent=2, ensure_ascii=False)

    return metadata


def make_clear_json():
    try:
        with open("metadata.json", "r", encoding="UTF-8") as file:
            try:
                old_metadata = json.load(file)
            except json.decoder.JSONDecodeError:
                old_metadata = {}
    except FileNotFoundError:
        old_metadata = {}

    metadata = {}
    for k, v in old_metadata.items():
        if v:
            metadata[k] = v

    with open("metadata.json", "w", encoding="UTF-8") as file:
        json.dump(metadata, file, indent=2, ensure_ascii=False)

    return metadata


if __name__ == "__main__":
    make_full_json()
