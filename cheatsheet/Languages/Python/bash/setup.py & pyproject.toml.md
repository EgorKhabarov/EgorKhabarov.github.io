# [extras_require]
Дополнительные зависимости

Используется для того, чтобы предложить пользователю установить дополнительные зависимости,
которые могут быть нужны только для определенных возможностей библиотеки.


```
pip install libname[all]
```
означает, что вместе с пакетом `libname` будут установлены все зависимости,
указанные для ключа `all` в файле `setup.py` или `pyproject.toml`.
В квадратных скобках указывается набор функциональности, для которой нужны дополнительные пакеты.
Например, может быть указано `libname[dev]` для установки зависимостей, необходимых для разработки,
или `libname[security]` для установки дополнительных пакетов, связанных с безопасностью.

## Как это реализовать

Нужно отредактировать файл `setup.py` или `pyproject.toml` и использовать ключ `extras_require`.

### setup.py
```python
from setuptools import setup

setup(
    name="my_library",
    version="0.1",
    packages=["my_library"],
    install_requires=[
        "requests",  # Основные зависимости
    ],
    extras_require={
        "dev": [
            "pytest",       # Зависимости для разработки
            "black",        # Форматирование кода
        ],
        "security": [
            "cryptography",  # Зависимости для функций безопасности
        ],
        "all": [
            "pytest",
            "black",
            "cryptography",
        ],
    },
)
```
- Основные зависимости перечислены в `install_requires`. Они будут установлены всегда.
- Опциональные зависимости добавляются через ключ `extras_require`.
Здесь мы добавили два набора зависимостей: `dev` и `security`, а также их комбинацию `all`.


### pyproject.toml

```toml
[tool.poetry]
name = "my_library"
version = "0.1.0"

[tool.poetry.dependencies]
python = "^3.7"
requests = "^2.25.1"

[tool.poetry.extras]
dev = ["pytest", "black"]
security = ["cryptography"]
all = ["pytest", "black", "cryptography"]
```


















# Консольный скрипт

### setup.py

```python
from setuptools import setup, find_packages

setup(
    name="your_library_name",
    version="0.1",
    packages=find_packages(),
    install_requires=[],  # Список зависимостей
    entry_points={
        "console_scripts": [
            "your-command=your_module:main_function",  # команда для консоли = модуль:функция
        ],
    },
)
```

- **`console_scripts`** — это ключ, который указывает, что вы создаете консольную команду.
- **`your-command`** — имя команды, через которое будет доступна ваша библиотека в терминале.
- **`your_module:main_function`** — путь до модуля и функции, которая будет вызвана при выполнении команды.

### setup.cfg

Этот способ позволяет вынести конфигурацию из кода в файл `setup.cfg`. Это делает конфигурацию более декларативной.

```ini
[metadata]
name = your_library_name
version = 0.1

[options]
packages = find:
install_requires =

[options.entry_points]
console_scripts =
your-command = your_module:main_function
```


### pyproject.toml

Формат `pyproject.toml` рекомендован PEP 518 и используется для настройки современных Python проектов.
В этом файле можно настроить проект для использования с `setuptools` или другими сборщиками (например, `Poetry`).

```toml
[build-system]
requires = ["setuptools", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "your_library_name"
version = "0.1"
dependencies = []

[project.scripts]
your-command = "your_module:main_function"
```


### Дополнительные шаги

Создание [виртуального окружения](?Languages/Python/bash/venv)
```bash
python -m venv env
source env/bin/activate  # Linux/MacOS
.\env\Scripts\activate  # Windows
```

Установка проекта локально для разработки
[pip Флаги](?Languages/Python/bash/Flags%20cmd%20pip)
```bash
pip install -e .
```
```bash
your-command
```
