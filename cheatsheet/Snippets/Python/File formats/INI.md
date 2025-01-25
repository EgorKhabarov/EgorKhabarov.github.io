# INI (Initialization)

формат конфигурационных файлов, который используется
для хранения настроек приложений и операционных систем.
Он был разработан в `Windows` и стал широко используемым
форматом для хранения конфигурационных данных в различных программных продуктах.

```ini
[Section1]
key1 = value1
key2 = value2

[Section2]
key3 = value3
key4 = value4
```

```python
# config = configparser.ConfigParser()
# config["BOT"] = {"bot_name": "", "token": ""}

import configparser


config = {"BOT": {"bot_name": "", "token": ""}}
config_ini = configparser.ConfigParser()

for key, value in config.items():
    config_ini[key] = value

with open("config.ini", "w") as file:
    config_ini.write(file)

config_ini = configparser.ConfigParser()
config_ini.read("config.ini")
print(config)
```
