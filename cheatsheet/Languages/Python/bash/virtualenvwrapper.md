Работа с виртуальными окружениями с помощью `virtualenvwrapper`

# Создание нового виртуального окружения

`mkvirtualenv [-a project_path] [-i package] [-r requirements_file] [virtualenv options] ENVNAME`
```bash
mkvirtualenv myenv --python=python3.10
```

Создает новое виртуальное окружение с именем `myenv`, используя указанную версию Python (например, 3.10)
После создания окружение автоматически активируется, и в командной строке появляется префикс `(myenv)`

# Активация существующего окружения

```bash
workon myenv
```

Активирует ранее созданное виртуальное окружение с именем `myenv`
Чтобы узнать список доступных окружений выполните команду без аргументов
```bash
workon
```
Это выведет список всех виртуальных окружений, находящихся в каталоге `~/.virtualenvs/`

# Деактивация (выход) из виртуального окружения

```bash
deactivate
```

Выходит из текущего активного виртуального окружения и возвращает вас к системному (глобальному) интерпретатору Python

# Удаление виртуального окружения

```bash
rmvirtualenv myenv
```

Полностью удаляет виртуальное окружение с именем `myenv`

# Дополнительные полезные моменты

### Путь к виртуальным окружениям
Все созданные окружения находятся в каталоге `~/.virtualenvs/`

### Проверка версии Python в окружении
После активации выполните
```bash
python --version
```
Это позволит убедиться, что используется нужная версия Python

### Установка пакетов в активированном окружении
Используйте `pip` для установки необходимых пакетов
```bash
pip install -r requirements.txt
```
  
`mkvirtualenv` и `workon` являются частью набора инструментов `virtualenvwrapper`,
который значительно упрощает управление множеством виртуальных окружений, особенно когда приходится часто переключаться между ними

[https://virtualenvwrapper.readthedocs.io/en/latest/command_ref.html](https://virtualenvwrapper.readthedocs.io/en/latest/command_ref.html)
