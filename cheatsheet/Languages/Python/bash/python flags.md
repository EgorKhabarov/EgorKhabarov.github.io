| Флаг                        | Описание                                                                                                                                                                                              |
|-----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `-c`                        | Выполнить однострочный Python-код из командной строки                                                                                                                                                 |
| `-m`                        | Запустить указанный Python-модуль как скрипт                                                                                                                                                          |
| `-i` `-interactive`         | Запускает интерпретатор Python в интерактивном режиме после выполнения скрипта                                                                                                                        |
| `-O` `-optimize`            | Включает режим оптимизации, который удаляет отладочную информацию и выполняет оптимизации в байт-коде<br>Это может уменьшить размер файлов `.pyc` и улучшить производительность, но осложнить отладку |
| `-B` `-dont-write-bytecode` | Предотвращает запись байт-кода (`.pyc` файлов) на диск                                                                                                                                                |
| `-v` `-verbose`             | Выводит подробные сообщения о том, какие модули импортируются<br>и какие файлы открываются в процессе выполнения программы                                                                            |
| `-q` `-quiet`               | Уменьшает уровень вывода, игнорируя сообщения о запуске и прочие информационные сообщения                                                                                                             |
| `-E` `-ignore-environment`  | Игнорировать переменные окружения,<br>которые обычно влияют на поведение Python, такие как `PYTHONPATH`                                                                                               |
| `-u` `-unbuffered`          | Переключает режим не буферизованного ввода/вывода<br>Полезно при работе с каналами и потоками данных,<br>чтобы гарантировать более немедленную обработку данных                                       |
| `-h` `-help`                | Выведет список всех доступных флагов и их описания                                                                                                                                                    |

```
>python -h
usage: python [option] ... [-c cmd | -m mod | file | -] [arg] ...
Options (and corresponding environment variables):
-b     : issue warnings about str(bytes_instance), str(bytearray_instance)
         and comparing bytes/bytearray with str. (-bb: issue errors)
-B     : do not write .pyc files on import; also PYTHONDONTWRITEBYTECODE=x
-c cmd : program passed in as string (terminates option list)
-d     : turn on parser debugging output (for experts only, only works on
         debug builds); also PYTHONDEBUG=x
-E     : ignore PYTHON* environment variables (such as PYTHONPATH)
-h     : print this help message and exit (also -? or --help)
-i     : inspect interactively after running script; forces a prompt even
         if stdin does not appear to be a terminal; also PYTHONINSPECT=x
-I     : isolate Python from the users environment (implies -E and -s)
-m mod : run library module as a script (terminates option list)
-O     : remove assert and __debug__-dependent statements; add .opt-1 before
         .pyc extension; also PYTHONOPTIMIZE=x
-OO    : do -O changes and also discard docstrings; add .opt-2 before
         .pyc extension
-P     : do not prepend a potentially unsafe path to sys.path; also PYTHONSAFEPATH
-q     : do not print version and copyright messages on interactive startup
-s     : do not add user site directory to sys.path; also PYTHONNOUSERSITE
-S     : do not imply "import site" on initialization
-u     : force the stdout and stderr streams to be unbuffered;
         this option has no effect on stdin; also PYTHONUNBUFFERED=x
-v     : verbose (trace import statements); also PYTHONVERBOSE=x
         can be supplied multiple times to increase verbosity
-V     : print the Python version number and exit (also --version)
         when given twice, print more information about the build
-W arg : warning control; arg is action:message:category:module:lineno
         also PYTHONWARNINGS=arg
-x     : skip first line of source, allowing use of non-Unix forms of #!cmd
-X opt : set implementation-specific option
--check-hash-based-pycs always|default|never:
         control how Python invalidates hash-based .pyc files
--help-env      : print help about Python environment variables and exit
--help-xoptions : print help about implementation-specific -X options and exit
--help-all      : print complete help information and exit
Arguments:
file   : program read from script file
-      : program read from stdin (default; interactive mode if a tty)
arg ...: arguments passed to program in sys.argv[1:]
```
