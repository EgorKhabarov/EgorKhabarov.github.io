# TOML - Tom's Obvious, Minimal Language

формат конфигурационных файлов, который был разработан для использования в проектах, написанных на языке программирования `Rust`

TOML файлы имеют структуру ключ-значение, где ключи и значения разделены знаком `=`, и используют синтаксис, похожий на язык программирования `INI`

```toml
[package]
name = "example"
version = "1.0.0"
authors = ["John Doe <john@example.com>"]
```

## tomllib

Built into Python
Supports read only

```python
import tomllib


with open("config.toml", "rb") as file:
    data = tomllib.load(file)
    # data = tomllib.loads(toml_string)
```

## tomlkit

[https://pypi.org/project/tomlkit/](https://pypi.org/project/tomlkit/)
[https://tomlkit.readthedocs.io/en/latest/](https://tomlkit.readthedocs.io/en/latest/)

`pip install tomlkit`

```python
import tomlkit


data = {
    "config": {
        "name": "John Smith",
        "age": 30,
        "city": "New York",
    },
}

with open("data.toml", "w", encoding="UTF-8") as file:
    tomlkit.dump(data, file)
    # file.write(tomlkit.dumps(data))

with open("data.toml", "r", encoding="UTF-8") as file:
    data = tomlkit.load(file)
    # data = tomlkit.loads(file.read())

print(data)
```
