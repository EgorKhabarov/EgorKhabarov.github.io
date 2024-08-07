<table>
<thead>
<tr>
<th>Флаг</th>
<th>Описание</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>-c</code></td>
<td>Выполнить однострочный Python-код из командной строки.</td>
</tr>
<tr>
<td><code>-m</code></td>
<td>Запустить указанный Python-модуль как скрипт.</td>
</tr>
<tr>
<td><code>-i</code> <code>—interactive</code></td>
<td>Запускает интерпретатор Python в интерактивном режиме после выполнения скрипта.</td>
</tr>
<tr>
<td><code>-O</code> <code>—optimize</code></td>
<td>Включает режим оптимизации, который удаляет отладочную информацию и выполняет оптимизации в байт-коде.<br>Это может уменьшить размер файлов <code>.pyc</code> и улучшить производительность, но осложнить отладку.</td>
</tr>
<tr>
<td><code>-B</code> <code>—dont-write-bytecode</code></td>
<td>Предотвращает запись байт-кода (<code>.pyc</code> файлов) на диск.</td>
</tr>
<tr>
<td><code>-v</code> <code>—verbose</code></td>
<td>Выводит подробные сообщения о том, какие модули импортируются<br>и какие файлы открываются в процессе выполнения программы.</td>
</tr>
<tr>
<td><code>-q</code> <code>—quiet</code></td>
<td>Уменьшает уровень вывода, игнорируя сообщения о запуске и прочие информационные сообщения.</td>
</tr>
<tr>
<td><code>-E</code> <code>—ignore-environment</code></td>
<td>Игнорировать переменные окружения,<br>которые обычно влияют на поведение Python, такие как <code>PYTHONPATH</code>.</td>
</tr>
<tr>
<td><code>-u</code> <code>—unbuffered</code></td>
<td>Переключает режим не буферизованного ввода/вывода.<br>Полезно при работе с каналами и потоками данных,<br>чтобы гарантировать более немедленную обработку данных.</td>
</tr>
<tr>
<td><code>-h</code> <code>—help</code></td>
<td>Выведет список всех доступных флагов и их описания.</td>
</tr>
</tbody>
</table>
<div class="code-element">
    <div class="lang-line">
        <text>text</text>
        <button class="copy-button"
        onclick="copyCode(this)">
    <svg stroke="currentColor"
         fill="none"
         stroke-width="2"
         viewBox="0 0 24 24"
         stroke-linecap="round"
         stroke-linejoin="round"
         class="h-4 w-4"
         height="1em"
         width="1em"
         xmlns="http://www.w3.org/2000/svg">
        <path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path>
        <rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect>
    </svg>
    <text>Copy code</text>
</button>

    </div>
    <div class="code"><div class="highlight"><pre><span></span>&gt;python -h
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
-S     : do not imply &quot;import site&quot; on initialization
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
</pre></div></div>
</div>