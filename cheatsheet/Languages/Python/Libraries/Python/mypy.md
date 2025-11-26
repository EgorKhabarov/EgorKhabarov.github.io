`mypy` статический анализатор типов для Python
Он помогает разработчикам выявлять ошибки в типах на этапе компиляции, до выполнения программы
Это полезно для больших проектов, где сложно отследить все возможные ошибки типов во время выполнения
В отличие от стандартного динамического поведения Python, с помощью `mypy` можно явно аннотировать типы переменных, аргументов функций и возвращаемых значений, чтобы повысить безопасность кода

# Основные особенности и функции

### Аннотация типов
- `mypy` использует встроенную систему аннотаций типов в Python 3.5+
- Аннотации типов добавляются с помощью синтаксиса Python для аргументов функций, возвращаемых значений и переменных

### Поддержка стандартных типов
- `mypy` поддерживает типы из стандартной библиотеки `typing`: `List`, `Dict`, `Tuple`, `Union` и другие

### Поддержка статической и динамической типизации
- Модели, не аннотированные типами, остаются динамическими
- Можно комбинировать статическую и динамическую типизацию

# Пример использования `mypy`

### Установка
Для установки `mypy` используйте команду:
```bash
pip install mypy
```

### Аннотация типов
Аннотации типов можно добавлять непосредственно в код:

```python
def greeting(name: str) -> str:
    return "Hello " + name
```

Здесь `name` строка (`str`), и функция должна возвращать строку
Если типы будут несоответствующими, `mypy` выдаст предупреждение

### Проверка типов
Чтобы запустить проверку типов с помощью `mypy`, выполните команду:
```bash
mypy your_script.py
```

# Примеры аннотаций и их использования

### Аннотации для переменных
```python
x: int = 10
y: str = "Hello"
z: List[int] = [1, 2, 3]
```

### Аннотации для функций
```python
def add(a: int, b: int) -> int:
    return a + b

def process_data(data: List[str]) -> None:
    for item in data:
        print(item)
```

### Optional
```python
from typing import Optional

def get_user_name(user_id: int) -> Optional[str]:
    if user_id == 1:
        return "Alice"
    return None
```

### Union
```python
from typing import Union

def process(value: Union[int, str]) -> str:
    if isinstance(value, int):
        return f"Processing number {value}"
    return f"Processing string {value}"
```

### TypedDict
`TypedDict` позволяет аннотировать словари с заранее известными ключами
```python
from typing import TypedDict

class Point(TypedDict):
    x: int
    y: int

def process_point(p: Point) -> None:
    print(p["x"], p["y"])

point = {"x": 10, "y": 20}
process_point(point)  # Успешно
```

### Mypy конфигурация

Mypy может быть настроен через файл конфигурации `mypy.ini` или `setup.cfg`

```ini
[mypy]
python_version = 3.9
ignore_missing_imports = True
disallow_untyped_calls = True
strict_optional = True
```

- `python_version` указывает версию Python
- `ignore_missing_imports` игнорирует отсутствующие модули
- `disallow_untyped_calls` запрещает вызов неаннотированных функций
- `strict_optional` включает строгую проверку для `Optional`
