# JSON - JavaScript Object Notation

Tекстовый формат обмена данными, который основан на синтаксисе JavaScript.
Он используется для хранения и обмена структурированными данными и часто используется
в веб-приложениях для обмена данными между клиентом и сервером.

```json
{
    "name": "John Smith",
    "age": 30,
    "city": "New York"
}
```

```python
import json


config = {"BOT": {"bot_name": "", "token": ""}}

with open("config.json", "w", encoding="UTF-8") as file:
    file.write(json.dumps(config, indent=4, ensure_ascii=False))
    # json.dump(config, file, indent=4, ensure_ascii=False)

with open("config.json", "r", encoding="UTF-8") as file:
    config = json.load(file)
    # config = json.loads(file.read())

print(config)
```

# JSONL

```python
{"name": "Alice Jones", "age": 25, "city": "Los Angeles"}
{"name": "John Smith", "age": 30, "city": "New York"}
{"name": "Bob Johnson", "age": 40, "city": "Chicago"}
```

```python
import json


config = [
    {"name": "Alice Jones", "age": 25, "city": "Los Angeles"},
    {"name": "John Smith", "age": 30, "city": "New York"},
    {"name": "Bob Johnson", "age": 40, "city": "Chicago"},
]

with open("test.jsonl", "a", encoding="UTF-8") as file:
    file.writelines([str(line) + "\n" for line in config])

with open("config.jsonl", "r", encoding="UTF-8") as file:
    for line in file:
        print(json.loads(line))
```

[[Snippets/Python/File formats/TinyDB (json)]]
