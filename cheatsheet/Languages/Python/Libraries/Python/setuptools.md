| Метод                     | Описание                                                    |
|---------------------------|-------------------------------------------------------------|
| setup()                   | Определяет настройки проекта и его зависимости              |
| find_packages()           | Автоматически находит и включает все пакеты проекта         |
| find_namespace_packages() | Аналогично find_packages(), но для пространств имен         |
| setup_requires            | Зависимости, необходимые для установки проекта              |
| install_requires          | Зависимости, необходимые для работы проекта                 |
| entry_points              | Позволяет определить точки входа (entry points) для проекта |

**setup()**

Описание: Определяет основные настройки проекта и его зависимости.


```python
from setuptools import setup

setup(
    name="mypackage",
    version="1.0.0",
    packages=["mypackage"],
    install_requires=["requests"],
)
```

**find_packages()**

Описание: Автоматически находит и включает все пакеты проекта.

```python
from setuptools import setup, find_packages

setup(
    name="mypackage",
    version="1.0.0",
    packages=find_packages(),
)
```

**entry_points**

Описание: Позволяет определить точки входа (entry points) для проекта, например, для создания скриптов командной строки.

```python
from setuptools import setup

setup(
    name="mypackage",
    version="1.0.0",
    entry_points={
        "console_scripts": [
            "myscript = mypackage.script:main",
        ],
    },
)
```
