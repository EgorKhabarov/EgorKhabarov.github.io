# YAML - Ain't Markup Language

Формат файлов, который используется для хранения и обмена неструктурированными и структурированными данными
Например он популярен в файлах настройки приложений, описание конфигураций и т.д
`YAML` использует отступы и специальные символы для обозначения структуры данных
Он также поддерживает множество типов данных, включая строки, числа, логические значения и массивы

```yaml
name: John Smith
age: 30
city: New York
```

```python
import yaml


data = {
    "name": "John Smith",
    "age": 30,
    "city": "New York",
}

with open("data.yaml", "w", encoding="utf-8") as file:
    file.write(yaml.safe_dump(data, sort_keys=False, allow_unicode=True, indent=4))

with open("data.yaml", "r", encoding="utf-8") as file:
    data = yaml.safe_load(file.read())

print(data)
```

- `pip install yaml`
- `pip install PyYAML`
