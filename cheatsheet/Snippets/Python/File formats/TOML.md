# TOML - Tom's Obvious, Minimal Language

формат конфигурационных файлов, который был разработан для использования в проектах, написанных на языке программирования `Rust`

TOML файлы имеют структуру ключ-значение, где ключи и значения разделены знаком `=`, и используют синтаксис, похожий на язык программирования `INI`

```toml
[package]
name = "example"
version = "1.0.0"
authors = ["John Doe <john@example.com>"]
```

```python
import toml  # pip install toml


config = {"BOT": {"bot_name": "", "token": ""}}

with open("config.toml", "w", encoding="UTF-8") as file:
    file.write(toml.dumps(config))
    # toml.dump(config, file)

with open("config.toml", "r", encoding="UTF-8") as file:
    config = toml.load(file)
    # config = toml.loads(file.read())

print(config)
```
