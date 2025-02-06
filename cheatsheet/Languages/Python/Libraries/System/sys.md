# sys

| Атрибут / Метод                                  | Описание                                                                                                                                            |
|--------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| `sys.__breakpointhook__`                         | Внутренняя функция для обработки `breakpoint()`                                                                                                     |
| `sys.__displayhook__`                            | Определяет, как результаты выводятся в интерактивном режиме                                                                                         |
| `sys.__doc__`                                    | Документация модуля `sys`                                                                                                                           |
| `sys.__excepthook__`                             | Обработчик необработанных исключений                                                                                                                |
| `sys.__interactivehook__`                        | Хук, вызываемый при запуске интерактивного режима                                                                                                   |
| `sys.__loader__`                                 | Загрузчик модуля                                                                                                                                    |
| `sys.__name__`                                   | Имя модуля (`'sys'`)                                                                                                                                |
| `sys.__package__`                                | Имя пакета, к которому принадлежит модуль                                                                                                           |
| `sys.__spec__`                                   | Спецификация загрузки модуля                                                                                                                        |
| `sys.__stderr__`                                 | Оригинальный поток ошибок                                                                                                                           |
| `sys.__stdin__`                                  | Оригинальный поток ввода                                                                                                                            |
| `sys.__stdout__`                                 | Оригинальный поток вывода                                                                                                                           |
| `sys.__unraisablehook__`                         | Хук для необрабатываемых исключений                                                                                                                 |
| `sys._base_executable`                           | Путь к исполняемому файлу базового интерпретатора                                                                                                   |
| `sys._baserepl`                                  | Внутренний механизм REPL Python                                                                                                                     |
| `sys._cached_windows_version`                    | Кэшированные данные о версии Windows                                                                                                                |
| `sys._clear_internal_caches`                     | Очистка внутренних кэшей интерпретатора                                                                                                             |
| `sys._clear_type_cache()`                        | Очистка кэша типов                                                                                                                                  |
| `sys._current_exceptions`                        | Получает текущие исключения в потоках                                                                                                               |
| `sys._current_frames`                            | Возвращает текущие фреймы выполнения всех потоков                                                                                                   |
| `sys._debugmallocstats`                          | Выводит статистику выделения памяти в отладочном режиме                                                                                             |
| `sys._enablelegacywindowsfsencoding()`           | Включает старую кодировку файловой системы Windows                                                                                                  |
| `sys._framework`                                 | Название фреймворка Python (если применимо)                                                                                                         |
| `sys._get_cpu_count_config()`                    | Возвращает конфигурацию количества ядер CPU                                                                                                         |
| `sys._getframe()`                                | Возвращает объект текущего стека вызовов                                                                                                            |
| `sys._getframemodulename(frame)`                 | Получает имя модуля для фрейма                                                                                                                      |
| `sys._git`                                       | Информация о версии Git, использованной при сборке Python                                                                                           |
| `sys._home`                                      | Путь к домашнему каталогу интерпретатора                                                                                                            |
| `sys._is_gil_enabled()`                          | Проверяет, включен ли GIL (Global Interpreter Lock)                                                                                                 |
| `sys._is_interned(string)`                       | Проверяет, интернирована ли строка                                                                                                                  |
| `sys._setprofileallthreads(func)`                | Устанавливает функцию профилирования для всех потоков                                                                                               |
| `sys._settraceallthreads(func)`                  | Устанавливает функцию трассировки для всех потоков                                                                                                  |
| `sys._stdlib_dir`                                | Путь к стандартной библиотеке Python                                                                                                                |
| `sys._vpath`                                     | Виртуальный путь для модулей                                                                                                                        |
| `sys._xoptions`                                  | Дополнительные опции интерпретатора Python                                                                                                          |
| `sys.activate_stack_trampoline()`                | Активация trampolining для управления стеком                                                                                                        |
| `sys.deactivate_stack_trampoline()`              | Деактивация trampolining                                                                                                                            |
| `sys.addaudithook(hook)`                         | Добавляет аудиторский хук                                                                                                                           |
| `sys.api_version`                                | Версия API интерпретатора Python                                                                                                                    |
| `sys.argv`                                       | Список аргументов командной строки                                                                                                                  |
| `sys.audit(event, *args)`                        | Генерация события аудита                                                                                                                            |
| `sys.base_exec_prefix`                           | Базовый путь для исполняемых файлов Python                                                                                                          |
| `sys.base_prefix`                                | Базовый путь установки Python                                                                                                                       |
| `sys.breakpointhook(*args)`                      | Функция-хук для `breakpoint()`                                                                                                                      |
| `sys.builtin_module_names`                       | Кортеж встроенных модулей Python                                                                                                                    |
| `sys.byteorder`                                  | Порядок байтов (`little` или `big`)                                                                                                                 |
| `sys.call_tracing(func, args)`                   | Запуск функции с трассировкой                                                                                                                       |
| `sys.copyright`                                  | Информация об авторских правах Python                                                                                                               |
| `sys.displayhook(value)`                         | Вывод значения в интерактивном режиме                                                                                                               |
| `sys.dont_write_bytecode`                        | Отключает создание `.pyc` файлов                                                                                                                    |
| `sys.exc_info()`                                 | Возвращает информацию о текущем исключении                                                                                                          |
| `sys.excepthook(type, value, traceback)`         | Устанавливает обработчик исключений                                                                                                                 |
| `sys.exception()`                                | Возвращает текущее исключение                                                                                                                       |
| `sys.exec_prefix`                                | Префикс каталога исполняемых файлов Python                                                                                                          |
| `sys.executable`                                 | Путь к интерпретатору Python                                                                                                                        |
| `sys.exit([код])`                                | Завершает выполнение программы                                                                                                                      |
| `sys.flags`                                      | Флаги, переданные интерпретатору Python                                                                                                             |
| `sys.float_info`                                 | Информация о представлении чисел с плавающей запятой                                                                                                |
| `sys.float_repr_style`                           | Стиль представления чисел с плавающей точкой                                                                                                        |
| `sys.get_asyncgen_hooks()`                       | Получает хуки для асинхронных генераторов                                                                                                           |
| `sys.get_coroutine_origin_tracking_depth()`      | Глубина отслеживания корутин                                                                                                                        |
| `sys.get_int_max_str_digits()`                   | Максимальное число цифр в строковом представлении int                                                                                               |
| `sys.getallocatedblocks()`                       | Возвращает число выделенных блоков памяти                                                                                                           |
| `sys.getdefaultencoding()`                       | Возвращает кодировку по умолчанию                                                                                                                   |
| `sys.getfilesystemencodeerrors()`                | Ошибки кодирования файловой системы                                                                                                                 |
| `sys.getfilesystemencoding()`                    | Возвращает кодировку файловой системы                                                                                                               |
| `sys.getprofile()`                               | Получает текущий профайлер                                                                                                                          |
| `sys.getrecursionlimit()`                        | Возвращает текущий лимит рекурсии                                                                                                                   |
| `sys.getrefcount(obj)`                           | Количество ссылок на объект                                                                                                                         |
| `sys.getsizeof(obj)`                             | Возвращает размер объекта в байтах                                                                                                                  |
| `sys.getswitchinterval()`                        | Интервал переключения потоков Python                                                                                                                |
| `sys.gettrace()`                                 | Возвращает текущую функцию трассировки                                                                                                              |
| `sys.getunicodeinternedsize(string)`             | Размер интернированной строки в байтах                                                                                                              |
| `sys.getwindowsversion()`                        | Информация о версии Windows                                                                                                                         |
| `sys.hash_info`                                  | Информация о хэшировании Python                                                                                                                     |
| `sys.hexversion`                                 | Версия Python в шестнадцатеричном формате                                                                                                           |
| `sys.implementation`                             | Информация о реализации Python                                                                                                                      |
| `sys.int_info`                                   | Информация о представлении int                                                                                                                      |
| `sys.intern(string)`                             | Интернирование строки                                                                                                                               |
| `sys.is_finalizing()`                            | Проверяет, завершается ли интерпретатор                                                                                                             |
| `sys.is_stack_trampoline_active()`               | Проверяет, активен ли stack trampoline                                                                                                              |
| `sys.maxsize`                                    | Максимальный размер целого числа                                                                                                                    |
| `sys.maxunicode`                                 | Максимальный Unicode код                                                                                                                            |
| `sys.meta_path`                                  | Список хуков импорта модулей                                                                                                                        |
| `sys.modules`                                    | Словарь загруженных модулей                                                                                                                         |
| `sys.monitoring`                                 | API для мониторинга выполнения Python                                                                                                               |
| `sys.orig_argv`                                  | Исходный список аргументов командной строки                                                                                                         |
| `sys.path`                                       | Пути поиска модулей                                                                                                                                 |
| `sys.path_hooks`                                 | Хуки обработки путей импорта                                                                                                                        |
| `sys.path_importer_cache`                        | Кэш импортёров для путей                                                                                                                            |
| `sys.platform`                                   | Название платформы (например, `win32`, `linux`)                                                                                                     |
| `sys.platlibdir`                                 | Директория платформо-зависимых библиотек                                                                                                            |
| `sys.prefix`                                     | Префикс установки Python                                                                                                                            |
| `sys.ps1`, `sys.ps2`                             | Промпты в интерактивном режиме                                                                                                                      |
| `sys.pycache_prefix`                             | Префикс каталога для кэша модулей                                                                                                                   |
| `sys.set_asyncgen_hooks(firstiter, finalizer)`   | Устанавливает хуки асинхронных генераторов                                                                                                          |
| `sys.set_coroutine_origin_tracking_depth(depth)` | Устанавливает глубину отслеживания корутин                                                                                                          |
| `sys.set_int_max_str_digits(n)`                  | Устанавливает максимальное число цифр в `int`                                                                                                       |
| `sys.setprofile(func)`                           | Устанавливает профайлер                                                                                                                             |
| `sys.setrecursionlimit(n)`                       | Устанавливает лимит рекурсии                                                                                                                        |
| `sys.setswitchinterval(interval)`                | Устанавливает интервал переключения потоков                                                                                                         |
| `sys.settrace(func)`                             | Устанавливает трассировщик                                                                                                                          |
| `sys.stdin`, `sys.stdout`, `sys.stderr`          | Потоки ввода, вывода и ошибок                                                                                                                       |
| `sys.stdlib_module_names`                        | Список модулей стандартной библиотеки                                                                                                               |
| `sys.thread_info`                                | Информация о потоках Python                                                                                                                         |
| `sys.unraisablehook(unraisable)`                 | Обработчик необрабатываемых исключений                                                                                                              |
| `sys.version`                                    | Строка с версией Python                                                                                                                             |
| `sys.version_info`                               | Кортеж с деталями версии Python                                                                                                                     |
| `sys.warnoptions`                                | Опции предупреждений                                                                                                                                |
| `sys.winver`                                     | **[только для Windows]** Версия Windows API                                                                                                         |
| `sys.dllhandle`                                  | **[только для Windows]** Дескриптор DLL интерпретатора Python                                                                                       |
| `sys.last_type`                                  | Тип последнего неперехваченного исключения                                                                                                          |
| `sys.last_value`                                 | Значение последнего неперехваченного исключения                                                                                                     |
| `sys.last_traceback`                             | Трассировка последнего неперехваченного исключения<br>Эти три доступны только в интерактивном сеансе после того, как<br>трассировка была напечатана |


### getsizeof: Измерение размера объекта
```python
import sys
x = [1, 2, 3]
print("Размер списка в байтах:", sys.getsizeof(x))
```

### path: Добавление пути для поиска модулей
```python
import sys
sys.path.append("/my/custom/path")
```

### setrecursionlimit: Изменение предела рекурсии
```python
import sys
sys.setrecursionlimit(2000)
print("Новый предел рекурсии:", sys.getrecursionlimit())
```

### argv: Список аргументов командной строки
```python
import sys

# Передаем два аргумента при запуске скрипта
# python myscript.py arg1 arg2
print(sys.argv[0])  # myscript.py
print(sys.argv[1])  # arg1
print(sys.argv[2])  # arg2
```

### stdin, stdout, stderr: Потоки ввода, вывода и ошибок
```python
import sys
data = sys.stdin.readline()
sys.stdout.write("Hello, world!\n")
sys.stderr.write("Error occurred\n")
```

### platform: Название платформы
```python
import sys

if sys.platform == "win32":
    print("Windows")
elif sys.platform == "linux":
    print("Linux")
elif sys.platform == "darwin":
    print("MacOS")
```