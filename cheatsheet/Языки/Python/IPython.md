<p><strong>Одиночный символ <code>%</code></strong>: Применяется для магических команд, которые действуют на одну строку в текущей ячейке.
<strong>Двойной символ <code>%%</code></strong>: Применяется для ячеек с кодом, которые содержат блоки скриптов на различных языках (например, Python, Bash, Ruby).</p>
<table>
<thead>
<tr>
<th>Команда</th>
<th>Описание</th>
<th>Пример использования</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>%%!</code></td>
<td>Выполняет команды оболочки в ячейке.</td>
<td><code>%%!</code><br><code>echo "Hello, World!"</code></td>
</tr>
<tr>
<td><code>%cpaste</code></td>
<td>Вставляет и выполняет блок кода, введённый вручную.</td>
<td><code>%cpaste</code><br><code>(вставить код)</code><br><code>--</code></td>
</tr>
<tr>
<td><code>%load</code></td>
<td>Загружает коды из файла в текущую ячейку.</td>
<td><code>%load script.py</code></td>
</tr>
<tr>
<td><code>%pdb</code></td>
<td>Включает или выключает отладчик Python (pdb) при возникновении ошибок.</td>
<td><code>%pdb on</code> или <code>%pdb off</code></td>
</tr>
<tr>
<td><code>%%python2</code></td>
<td>Выполняет ячейку в интерпретаторе Python 2 (если установлен).</td>
<td><code>%%python2</code><br><code>print "Hello from Python 2"</code></td>
</tr>
<tr>
<td><code>%sx</code></td>
<td>Выполняет команды оболочки и возвращает их результаты как список строк.</td>
<td><code>output = %sx ls -l</code><br><code>print(output)</code></td>
</tr>
<tr>
<td><code>%%HTML</code></td>
<td>Отображает HTML-код в ячейке.</td>
<td><code>%%HTML</code><br><code>&lt;h1&gt;Hello, World!&lt;/h1&gt;</code></td>
</tr>
<tr>
<td><code>%ddir</code></td>
<td>Расширенный список атрибутов объекта.</td>
<td><code>%ddir object_name</code></td>
</tr>
<tr>
<td><code>%load_ext</code></td>
<td>Загружает расширение IPython.</td>
<td><code>%load_ext autoreload</code></td>
</tr>
<tr>
<td><code>%pdef</code></td>
<td>Показывает определение функции, включая аргументы.</td>
<td><code>%pdef function_name</code></td>
</tr>
<tr>
<td><code>%%python3</code></td>
<td>Выполняет ячейку в интерпретаторе Python 3 (по умолчанию).</td>
<td><code>%%python3</code><br><code>print("Hello from Python 3")</code></td>
</tr>
<tr>
<td><code>%%sx</code></td>
<td>Выполняет команды оболочки в ячейке и возвращает их результаты как список строк.</td>
<td><code>%%sx</code><br><code>ls -l</code></td>
</tr>
<tr>
<td><code>%%SVG</code></td>
<td>Отображает SVG-код в ячейке.</td>
<td><code>%%SVG</code><br><code>&lt;svg&gt;...&lt;/svg&gt;</code></td>
</tr>
<tr>
<td><code>%debug</code></td>
<td>Начинает сессию отладки в точке вызова.</td>
<td><code>%debug</code></td>
</tr>
<tr>
<td><code>%loadpy</code></td>
<td>Загружает и выполняет файл Python.</td>
<td><code>%loadpy script.py</code></td>
</tr>
<tr>
<td><code>%pdoc</code></td>
<td>Показывает строку документации объекта.</td>
<td><code>%pdoc function_name</code></td>
</tr>
<tr>
<td><code>%quickref</code></td>
<td>Показывает краткое руководство по IPython.</td>
<td><code>%quickref</code></td>
</tr>
<tr>
<td><code>%system</code></td>
<td>Выполняет команду оболочки.</td>
<td><code>%system ls -l</code></td>
</tr>
<tr>
<td><code>%alias</code></td>
<td>Создаёт псевдоним для команды оболочки.</td>
<td><code>%alias ll ls -l</code></td>
</tr>
<tr>
<td><code>%%debug</code></td>
<td>Начинает сессию отладки в ячейке (аналогично <code>%debug</code>, но для всей ячейки).</td>
<td><code>%%debug</code><br><code>buggy_function()</code></td>
</tr>
<tr>
<td><code>%logoff</code></td>
<td>Отключает журналирование.</td>
<td><code>%logoff</code></td>
</tr>
<tr>
<td><code>%%perl</code></td>
<td>Выполняет код Perl в ячейке.</td>
<td><code>%%perl</code><br><code>print "Hello from Perl\n";</code></td>
</tr>
<tr>
<td><code>%recall</code></td>
<td>Повторяет предыдущую команду или извлекает её по индексу из истории.</td>
<td><code>%recall 42</code></td>
</tr>
<tr>
<td><code>%%system</code></td>
<td>Выполняет команды оболочки в ячейке.</td>
<td><code>%%system</code><br><code>ls -l</code></td>
</tr>
<tr>
<td><code>%alias_magic</code></td>
<td>Создаёт псевдоним для существующей магической команды IPython.</td>
<td><code>%alias_magic t timeit</code><br><code># Теперь можно использовать 't' вместо 'timeit'</code><br><code>t my_function()</code></td>
</tr>
<tr>
<td><code>%dhist</code></td>
<td>Показывает историю директорий, в которых вы работали.</td>
<td><code>%dhist</code></td>
</tr>
<tr>
<td><code>%logon</code></td>
<td>Включает журналирование.</td>
<td><code>%logon</code></td>
</tr>
<tr>
<td><code>%pfile</code></td>
<td>Открывает и показывает содержимое файла с кодом.</td>
<td><code>%pfile my_script.py</code></td>
</tr>
<tr>
<td><code>%rehashx</code></td>
<td>Пересчитывает псевдонимы для всех исполняемых файлов в $PATH (для использования с <code>%sx</code>).</td>
<td><code>%rehashx</code></td>
</tr>
<tr>
<td><code>%tb</code></td>
<td>Показывает traceback (стек вызовов) от последнего исключения.</td>
<td><code>%tb</code></td>
</tr>
<tr>
<td><code>%autoawait</code></td>
<td>Устанавливает функцию ожидания по умолчанию для поддержки асинхронного кода.</td>
<td><code>%autoawait asyncio</code></td>
</tr>
<tr>
<td><code>%dirs</code></td>
<td>Показывает список директорий в стеке директорий.</td>
<td><code>%dirs</code></td>
</tr>
<tr>
<td><code>%logstart</code></td>
<td>Начинает журналирование сессии.</td>
<td><code>%logstart</code></td>
</tr>
<tr>
<td><code>%pinfo</code></td>
<td>Показывает информацию об объекте.</td>
<td><code>%pinfo function_name</code></td>
</tr>
<tr>
<td><code>%reload_ext</code></td>
<td>Перезагружает расширение IPython.</td>
<td><code>%reload_ext autoreload</code></td>
</tr>
<tr>
<td><code>%time</code></td>
<td>Измеряет время выполнения однострочного кода.</td>
<td><code>%time my_function()</code></td>
</tr>
<tr>
<td><code>%autocall</code></td>
<td>Управляет автоматическим вызовом функций в IPython.</td>
<td><code>%autocall 1</code></td>
</tr>
<tr>
<td><code>%doctest_mode</code></td>
<td>Включает/выключает режим тестирования документации (doctest).</td>
<td><code>%doctest_mode</code></td>
</tr>
<tr>
<td><code>%logstate</code></td>
<td>Показывает текущее состояние логирования.</td>
<td><code>%logstate</code></td>
</tr>
<tr>
<td><code>%pinfo2</code></td>
<td>Показывает подробную информацию о объекте (дополненная версия <code>%pinfo</code>).</td>
<td><code>%pinfo2 my_function</code></td>
</tr>
<tr>
<td><code>%ren</code></td>
<td>Переименовывает переменную в среде IPython.</td>
<td><code>%ren old_variable new_variable</code></td>
</tr>
<tr>
<td><code>%%time</code></td>
<td>Измеряет время выполнения всей ячейки.</td>
<td><code>%%time</code><br><code>my_function()</code></td>
</tr>
<tr>
<td><code>%autoindent</code></td>
<td>Включает или выключает автоматический отступ.</td>
<td><code>%autoindent</code></td>
</tr>
<tr>
<td><code>%echo</code></td>
<td>Отображает текст или значение переменной.</td>
<td><code>%echo "Hello, World!"</code></td>
</tr>
<tr>
<td><code>%logstop</code></td>
<td>Останавливает журналирование сессии.</td>
<td><code>%logstop</code></td>
</tr>
<tr>
<td><code>%pip</code></td>
<td>Позволяет использовать pip для установки пакетов изнутри IPython.</td>
<td><code>%pip install numpy</code></td>
</tr>
<tr>
<td><code>%rep</code></td>
<td>Повторяет и выполняет последнюю команду.</td>
<td><code>%rep</code></td>
</tr>
<tr>
<td><code>%timeit</code></td>
<td>Измеряет время выполнения многократного запуска однострочного кода.</td>
<td><code>%timeit sum(range(10000))</code></td>
</tr>
<tr>
<td><code>%automagic</code></td>
<td>Включает или выключает автоматическое распознавание магических команд без префикса <code>%</code>.</td>
<td><code>%automagic on</code></td>
</tr>
<tr>
<td><code>%ed</code></td>
<td>Открывает редактор для редактирования строки или блока кода.</td>
<td><code>%ed script.py</code></td>
</tr>
<tr>
<td><code>%ls</code></td>
<td>Список файлов и директорий.</td>
<td><code>%ls</code></td>
</tr>
<tr>
<td><code>%popd</code></td>
<td>Удаляет верхний каталог из стека директорий и переходит в новый верхний каталог.</td>
<td><code>%popd</code></td>
</tr>
<tr>
<td><code>%rerun</code></td>
<td>Повторяет последнюю команду с историей в ячейке.</td>
<td><code>%rerun</code></td>
</tr>
<tr>
<td><code>%%timeit</code></td>
<td>Измеряет время выполнения многократного запуска кода в ячейке.</td>
<td><code>%%timeit</code><br><code>sum(range(10000))</code></td>
</tr>
<tr>
<td><code>%%bash</code></td>
<td>Выполняет код Bash в ячейке.</td>
<td><code>%%bash</code><br><code>echo "Hello from Bash"</code></td>
</tr>
<tr>
<td><code>%edit</code></td>
<td>Открывает редактор для редактирования строки или блока кода.</td>
<td><code>%edit script.py</code></td>
</tr>
<tr>
<td><code>%lsmagic</code></td>
<td>Показывает список всех доступных магических команд.</td>
<td><code>%lsmagic</code></td>
</tr>
<tr>
<td><code>%pprint</code></td>
<td>Включает или выключает красивый вывод (pretty-printing) объектов.</td>
<td><code>%pprint</code></td>
</tr>
<tr>
<td><code>%reset</code></td>
<td>Сбрасывает пространство имен IPython, удаляя все переменные и импортированные модули.</td>
<td><code>%reset</code></td>
</tr>
<tr>
<td><code>%unalias</code></td>
<td>Удаляет заданный псевдоним.</td>
<td><code>%unalias ll</code></td>
</tr>
<tr>
<td><code>%bookmark</code></td>
<td>Управление закладками для директорий.</td>
<td><code>%bookmark mydir /path/to/directory</code></td>
</tr>
<tr>
<td><code>%env</code></td>
<td>Установка переменных среды или просмотр текущих переменных среды.</td>
<td><code>%env PATH=/new/path</code></td>
</tr>
<tr>
<td><code>%macro</code></td>
<td>Определяет макрос для последовательности команд.</td>
<td><code>%macro my_macro 1-5</code><br><code>print("Hello")</code></td>
</tr>
<tr>
<td><code>%precision</code></td>
<td>Устанавливает количество отображаемых знаков после запятой.</td>
<td><code>%precision 4</code></td>
</tr>
<tr>
<td><code>%reset_selective</code></td>
<td>Сбрасывает только указанные переменные в пространстве имен IPython.</td>
<td><code>%reset_selective my_variable</code></td>
</tr>
<tr>
<td><code>%unload_ext</code></td>
<td>Выгружает указанное расширение IPython.</td>
<td><code>%unload_ext autoreload</code></td>
</tr>
<tr>
<td><code>%%capture</code></td>
<td>Перенаправляет вывод и ошибки в переменные.</td>
<td><code>%%capture output</code><br><code>print("Hello, World!")</code></td>
</tr>
<tr>
<td><code>%%file</code></td>
<td>Записывает содержимое ячейки в файл.</td>
<td><code>%%file my_script.py</code><br><code>print("Hello, World!")</code></td>
</tr>
<tr>
<td><code>%magic</code></td>
<td>Показывает справку по магическим командам.</td>
<td><code>%magic</code></td>
</tr>
<tr>
<td><code>%prun</code></td>
<td>Выполняет код с профилированием с использованием cProfile.</td>
<td><code>%prun my_function()</code></td>
</tr>
<tr>
<td><code>%rmdir</code></td>
<td>Удаляет указанные директории.</td>
<td><code>%rmdir directory_name</code></td>
</tr>
<tr>
<td><code>%who</code></td>
<td>Показывает переменные и их типы в глобальном пространстве.</td>
<td><code>%who</code></td>
</tr>
<tr>
<td><code>%cd</code></td>
<td>Изменяет текущую рабочую директорию.</td>
<td><code>%cd /path/to/directory</code></td>
</tr>
<tr>
<td><code>%gui</code></td>
<td>Устанавливает графический интерфейс для бэкенда IPython.</td>
<td><code>%gui qt</code></td>
</tr>
<tr>
<td><code>%mamba</code></td>
<td>Запускает установку пакетов с помощью Mamba (альтернатива pip).</td>
<td><code>%mamba install numpy</code></td>
</tr>
<tr>
<td><code>%%prun</code></td>
<td>Выполняет код с профилированием с использованием cProfile (для всей ячейки).</td>
<td><code>%%prun</code><br><code>my_function()</code></td>
</tr>
<tr>
<td><code>%%ruby</code></td>
<td>Выполняет код Ruby в ячейке.</td>
<td><code>%%ruby</code><br><code>puts "Hello from Ruby"</code></td>
</tr>
<tr>
<td><code>%who_ls</code></td>
<td>Показывает имена всех переменных в глобальном пространстве в виде списка.</td>
<td><code>%who_ls</code></td>
</tr>
<tr>
<td><code>%cls</code></td>
<td>Очищает консольный вывод.</td>
<td><code>%cls</code></td>
</tr>
<tr>
<td><code>%hist</code></td>
<td>Показывает историю ввода.</td>
<td><code>%hist</code></td>
</tr>
<tr>
<td><code>%%markdown</code></td>
<td>Размечает содержимое ячейки как Markdown.</td>
<td><code>%%markdown</code><br><code># Заголовок</code><br><code>**Текст**</code></td>
</tr>
<tr>
<td><code>%psearch</code></td>
<td>Поиск по именам символов с использованием шаблона.</td>
<td><code>%psearch *function*</code></td>
</tr>
<tr>
<td><code>%run</code></td>
<td>Запускает внешний скрипт Python или IPython.</td>
<td><code>%run my_script.py</code></td>
</tr>
<tr>
<td><code>%whos</code></td>
<td>Показывает все переменные в текущем пространстве имен и их типы.</td>
<td><code>%whos</code></td>
</tr>
<tr>
<td><code>%%cmd</code></td>
<td>Запускает команды Windows cmd в ячейке.</td>
<td><code>%%cmd</code><br><code>dir</code></td>
</tr>
<tr>
<td><code>%history</code></td>
<td>Показывает историю ввода и вывода.</td>
<td><code>%history -n 1-10</code></td>
</tr>
<tr>
<td><code>%matplotlib</code></td>
<td>Включает встроенную поддержку matplotlib.</td>
<td><code>%matplotlib inline</code></td>
</tr>
<tr>
<td><code>%psource</code></td>
<td>Показывает исходный код объекта.</td>
<td><code>%psource my_function</code></td>
</tr>
<tr>
<td><code>%save</code></td>
<td>Сохраняет ввод и вывод ячейки в файл Python.</td>
<td><code>%save my_session.py 1-5</code></td>
</tr>
<tr>
<td><code>%%writefile</code></td>
<td>Записывает содержимое ячейки в файл.</td>
<td><code>%%writefile my_file.txt</code><br><code>Hello, World!</code></td>
</tr>
<tr>
<td><code>%code_wrap</code></td>
<td>Устанавливает или отключает авто-перенос строк для вывода кода.</td>
<td><code>%code_wrap on</code></td>
</tr>
<tr>
<td><code>%%html</code></td>
<td>Размечает содержимое ячейки как HTML.</td>
<td><code>%%html</code><br><code>&lt;h1&gt;Hello, World!&lt;/h1&gt;</code></td>
</tr>
<tr>
<td><code>%micromamba</code></td>
<td>Запускает установку пакетов с помощью Micromamba (альтернатива pip).</td>
<td><code>%micromamba install numpy</code></td>
</tr>
<tr>
<td><code>%pushd</code></td>
<td>Добавляет текущую директорию в стек и переходит в новую директорию.</td>
<td><code>%pushd /path/to/directory</code></td>
</tr>
<tr>
<td><code>%sc</code></td>
<td>Выполняет код, используя Subprocess.</td>
<td><code>%sc ls -l</code></td>
</tr>
<tr>
<td><code>%xdel</code></td>
<td>Удаляет переменные и объекты из сессии IPython.</td>
<td><code>%xdel my_variable</code></td>
</tr>
<tr>
<td><code>%%code_wrap</code></td>
<td>Устанавливает или отключает авто-перенос строк для вывода кода в ячейке.</td>
<td><code>%%code_wrap on</code></td>
</tr>
<tr>
<td><code>%%javascript</code></td>
<td>Выполняет JavaScript код в ячейке (для Jupyter Notebook).</td>
<td><code>%%javascript</code><br><code>console.log("Hello, World!")</code></td>
</tr>
<tr>
<td><code>%mkdir</code></td>
<td>Создает новую директорию.</td>
<td><code>%mkdir new_directory</code></td>
</tr>
<tr>
<td><code>%pwd</code></td>
<td>Выводит текущую рабочую директорию.</td>
<td><code>%pwd</code></td>
</tr>
<tr>
<td><code>%%script</code></td>
<td>Запускает ячейку с указанным интерпретатором (bash, python, ruby, etc).</td>
<td><code>%%script bash</code><br><code>ls -l</code></td>
</tr>
<tr>
<td><code>%xmode</code></td>
<td>Устанавливает уровень подробности трассировки для ошибок.</td>
<td><code>%xmode Verbose</code></td>
</tr>
<tr>
<td><code>%colors</code></td>
<td>Устанавливает цветовую схему для вывода в IPython.</td>
<td><code>%colors Linux</code></td>
</tr>
<tr>
<td><code>%%js</code></td>
<td>Выполняет JavaScript код в ячейке (для Jupyter Notebook).</td>
<td><code>%%js</code><br><code>console.log("Hello, World!")</code></td>
</tr>
<tr>
<td><code>%notebook</code></td>
<td>Запускает скрипт Python как блокнот Jupyter.</td>
<td><code>%notebook script.py</code></td>
</tr>
<tr>
<td><code>%pycat</code></td>
<td>Показывает содержимое скрипта Python.</td>
<td><code>%pycat script.py</code></td>
</tr>
<tr>
<td><code>%set_env</code></td>
<td>Устанавливает переменные среды для текущей сессии IPython.</td>
<td><code>%set_env PATH=/new/path</code></td>
</tr>
<tr>
<td><code>%conda</code></td>
<td>Взаимодействует с conda для управления окружением и пакетами.</td>
<td><code>%conda install numpy</code></td>
</tr>
<tr>
<td><code>%killbgscripts</code></td>
<td>Останавливает все фоновые процессы выполнения скриптов.</td>
<td><code>%killbgscripts</code></td>
</tr>
<tr>
<td><code>%page</code></td>
<td>Отображает содержимое объекта с поддержкой постраничного просмотра.</td>
<td><code>%page large_object</code></td>
</tr>
<tr>
<td><code>%pylab</code></td>
<td>Загружает matplotlib и numpy для интерактивной работы в IPython.</td>
<td><code>%pylab</code></td>
</tr>
<tr>
<td><code>%%sh</code></td>
<td>Выполняет команды Shell (sh) в ячейке.</td>
<td><code>%%sh</code><br><code>ls -l</code></td>
</tr>
<tr>
<td><code>%config</code></td>
<td>Конфигурирует IPython и его расширения.</td>
<td><code>%config IPCompleter.greedy=True</code></td>
</tr>
<tr>
<td><code>%%latex</code></td>
<td>Размечает содержимое ячейки как LaTeX.</td>
<td><code>%%latex</code><br><code>\begin{equation}</code><br><code>E = mc^2</code><br><code>\end{equation}</code></td>
</tr>
<tr>
<td><code>%paste</code></td>
<td>Вставляет и выполняет блок кода, считанный из буфера обмена.</td>
<td><code>%paste</code></td>
</tr>
<tr>
<td><code>%%pypy</code></td>
<td>Выполняет код Python с использованием интерпретатора PyPy.</td>
<td><code>%%pypy</code><br><code>print("Hello, PyPy!")</code></td>
</tr>
<tr>
<td><code>%store</code></td>
<td>Сохраняет переменные в файл между сеансами IPython.</td>
<td><code>%store my_variable</code></td>
</tr>
<tr>
<td><code>%copy</code></td>
<td>Копирует файлы между локальной файловой системой и файловой системой Jupyter Notebook.</td>
<td><code>%copy my_file.txt another_directory/</code></td>
</tr>
<tr>
<td><code>%ldir</code></td>
<td>Список файлов и директорий в локальной файловой системе.</td>
<td><code>%ldir</code></td>
</tr>
<tr>
<td><code>%pastebin</code></td>
<td>Отправляет содержимое ячейки на Pastebin и возвращает URL.</td>
<td><code>%pastebin</code></td>
</tr>
<tr>
<td><code>%%python</code></td>
<td>Выполняет код Python в ячейке.</td>
<td><code>%%python</code><br><code>print("Hello, Python!")</code></td>
</tr>
<tr>
<td><code>%%svg</code></td>
<td>Размечает содержимое ячейки как SVG (Scalable Vector Graphics).</td>
<td><code>%%svg</code><br><code>&lt;svg height="100" width="100"&gt; ... &lt;/svg&gt;</code></td>
</tr>
</tbody>
</table>