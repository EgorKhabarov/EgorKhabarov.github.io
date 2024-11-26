<h1>Работа с файлами и директориями</h1>
<table>
<thead>
<tr>
<th>Функция/Атрибут</th>
<th>Описание</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>os.listdir(".")</code></td>
<td>Возвращает список файлов и директорий в указанном каталоге</td>
</tr>
<tr>
<td><code>os.scandir(path=".")</code></td>
<td>Возвращает итератор <code>DirEntry</code>, который предоставляет информацию<br>о файлах и директориях в директории <code>path</code>.<br>Более выгодный аналог <code>os.listdir</code></td>
</tr>
<tr>
<td><code>os.walk(".")</code></td>
<td>Рекурсивно обходит файлы в дереве директорий</td>
</tr>
<tr>
<td><code>os.getcwd()</code></td>
<td>Возвращает текущий рабочий каталог</td>
</tr>
<tr>
<td><code>os.chdir(path)</code></td>
<td>Изменяет текущий рабочий каталог на указанный</td>
</tr>
<tr>
<td><code>os.mkdir(path, mode=0o777)</code></td>
<td>Создает новую директорию с указанным путем и правами доступа</td>
</tr>
<tr>
<td><code>os.makedirs(path, exist_ok=True)</code></td>
<td>Рекурсивно создает директории, включая промежуточные</td>
</tr>
<tr>
<td><code>os.removedirs(path)</code></td>
<td>Удаляет директории рекурсивно</td>
</tr>
<tr>
<td><code>os.remove(path)</code></td>
<td>Удаляет файл по указанному пути</td>
</tr>
<tr>
<td><code>os.rmdir(path)</code></td>
<td>Удаляет пустую директорию</td>
</tr>
<tr>
<td><code>os.rename(src, dst)</code></td>
<td>Переименовывает файл или директорию</td>
</tr>
<tr>
<td><code>os.replace(src, dst)</code></td>
<td>Перемещает файл или директорию на новое место. Если целевой путь существует, он будет заменен</td>
</tr>
<tr>
<td><code>os.urandom(n)</code></td>
<td>Возвращает <code>n</code> байт случайных данных, пригодных для использования в криптографии</td>
</tr>
<tr>
<td><code>os.unlink(path)</code></td>
<td>Удаляет файл по указанному пути (аналог <code>os.remove</code>)</td>
</tr>
<tr>
<td><code>os.symlink(src, dst)</code></td>
<td>Создает символическую ссылку на файл или директорию (только Unix)</td>
</tr>
<tr>
<td><code>os.stat(path)</code></td>
<td><a target="_self" href="?Languages/Python/Libraries/System/os/os.stat" class="wikilink">os.stat</a> Возвращает информацию о пути (например, размер, время последней модификации)</td>
</tr>
<tr>
<td><code>os.lstat(path)</code></td>
<td>То же, что и <code>os.stat</code>, но не разыменовывает символические ссылки</td>
</tr>
<tr>
<td><code>os.path</code></td>
<td><a target="_self" href="?Languages/Python/Libraries/System/os/os.path" class="wikilink">os.path</a> Содержит функции для работы с путями, такие как <code>join</code>, <code>split</code>, <code>isfile</code>, <code>isdir</code></td>
</tr>
</tbody>
</table>
<h1>Управление процессами</h1>
<table>
<thead>
<tr>
<th>Функция/Атрибут</th>
<th>Описание</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>os.system(command)</code></td>
<td>Выполняет команду в оболочке и возвращает код завершения</td>
</tr>
<tr>
<td><code>os.popen(command)</code></td>
<td>Выполняет команду в оболочке и возвращает объект файла, связанный с потоком вывода</td>
</tr>
<tr>
<td><code>os.kill(pid, sig)</code></td>
<td>Отправляет сигнал процессу с указанным идентификатором (PID) и <a target="_self" href="?Languages/Python/Libraries/System/signal" class="wikilink">signal</a><br><code>os.kill(12345, signal.SIGTERM)</code></td>
</tr>
<tr>
<td><code>os._exit(n)</code></td>
<td>Немедленно завершает выполнение текущего процесса с указанным кодом возврата</td>
</tr>
<tr>
<td><code>os.waitpid(pid, options)</code></td>
<td>Ожидает завершения процесса с указанным идентификатором (PID) и возвращает его код завершения и статус</td>
</tr>
<tr>
<td><code>os.fork()</code></td>
<td>Создает новый процесс путем форкинга текущего (только для Unix)</td>
</tr>
<tr>
<td><code>os.execv(path, args)</code></td>
<td>Заменяет текущий процесс новым процессом, указанным в path</td>
</tr>
<tr>
<td><code>os.abort()</code></td>
<td>Немедленно завершает процесс сгенерировав сигнатуру <code>SIGABRT</code></td>
</tr>
<tr>
<td><code>os.getpid()</code></td>
<td>Возвращает идентификатор текущего процесса</td>
</tr>
<tr>
<td><code>os.getppid()</code></td>
<td>Возвращает идентификатор родительского процесса</td>
</tr>
</tbody>
</table>
<h1>Работа с файловыми дескрипторами</h1>
<table>
<thead>
<tr>
<th>Функция/Атрибут</th>
<th>Описание</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>os.open(path, flags, mode=0o777)</code></td>
<td>Открывает файл и возвращает файловый дескриптор. <code>flags</code> определяет режим открытия (например, <code>os.O_RDONLY</code>, <code>os.O_WRONLY</code>)</td>
</tr>
<tr>
<td><code>os.close(fd)</code></td>
<td>Закрывает файловый дескриптор <code>fd</code></td>
</tr>
<tr>
<td><code>os.read(fd, n)</code></td>
<td>Читает до <code>n</code> байт из файла, связанного с файловым дескриптором <code>fd</code></td>
</tr>
<tr>
<td><code>os.write(fd, str)</code></td>
<td>Записывает строку в файл, связанный с файловым дескриптором <code>fd</code></td>
</tr>
<tr>
<td><code>os.lseek(fd, pos, how)</code></td>
<td>Перемещает указатель чтения/записи в файл, связанный с файловым дескриптором <code>fd</code>. <code>how</code> определяет начало перемещения</td>
</tr>
<tr>
<td><code>os.fsync(fd)</code></td>
<td>Принудительно записывает все изменения, сделанные в файле, связанный с файловым дескриптором <code>fd</code></td>
</tr>
<tr>
<td><code>os.dup(fd)</code></td>
<td>Дублирует файловый дескриптор <code>fd</code></td>
</tr>
<tr>
<td><code>os.dup2(fd, fd2)</code></td>
<td>Дублирует файловый дескриптор <code>fd</code> в <code>fd2</code></td>
</tr>
</tbody>
</table>
<h1>Функции для работы с файловыми системами</h1>
<table>
<thead>
<tr>
<th>Функция</th>
<th>Описание</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>os.fsencode("filename")</code></td>
<td>Кодирует имя файла в системную кодировку</td>
</tr>
<tr>
<td><code>os.fsdecode(b"filename")</code></td>
<td>Декодирует имя файла из системной кодировки</td>
</tr>
<tr>
<td><code>os.get_exec_path()</code></td>
<td>Возвращает список путей для поиска исполняемых файлов</td>
</tr>
<tr>
<td><code>os.fdopen(fd, mode)</code></td>
<td>Открывает файловый объект, связанный с файловым дескриптором</td>
</tr>
</tbody>
</table>
<h1>Атрибуты, связанные с путями и разделителями</h1>
<table>
<thead>
<tr>
<th>Атрибут</th>
<th>Описание</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>os.altsep</code></td>
<td>Альтернативный разделитель пути. Используется, если он поддерживается ОС. В Windows это <code>/</code> вместо <code>\</code></td>
</tr>
<tr>
<td><code>os.curdir</code></td>
<td>Строка, представляющая текущую директорию. Обычно это <code>.</code></td>
</tr>
<tr>
<td><code>os.pardir</code></td>
<td>Строка, представляющая родительскую директорию. Обычно это <code>..</code></td>
</tr>
<tr>
<td><code>os.sep</code></td>
<td>Строка, представляющая разделитель пути, используемый в операционной системе. В Windows это <code>\</code>, в Unix — <code>/</code></td>
</tr>
<tr>
<td><code>os.pathsep</code></td>
<td>Строка, разделяющая компоненты в переменных среды, таких как <code>PATH</code>. В Windows это <code>;</code>, в Unix — <code>:</code></td>
</tr>
<tr>
<td><code>os.linesep</code></td>
<td>Строка, представляющая разделитель строк, используемый в операционной системе. В Windows это <code>\r\n</code>, в Unix — <code>\n</code></td>
</tr>
<tr>
<td><code>os.defpath</code></td>
<td>Стандартный <code>PATH</code>, используемый если переменная окружения <code>PATH</code> не установлена</td>
</tr>
<tr>
<td><code>os.extsep</code></td>
<td>Разделитель расширения файлов. В большинстве ОС это <code>.</code></td>
</tr>
<tr>
<td><code>os.devnull</code></td>
<td>Путь к специальному файлу, который отбрасывает все записанные в него данные (<code>/dev/null</code> на UNIX и <code>NUL</code> на Windows)</td>
</tr>
</tbody>
</table>
<h1>Информация о системе и среде выполнения</h1>
<table>
<thead>
<tr>
<th>Атрибут/Функция</th>
<th>Описание</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>os.name</code></td>
<td>Имя операционной системы. Например, <code>posix</code> для Unix-подобных систем, <code>nt</code> для Windows</td>
</tr>
<tr>
<td><code>os.getenv(key, default=None)</code></td>
<td>Возвращает значение переменной окружения или значение по умолчанию</td>
</tr>
<tr>
<td><code>os.environ</code></td>
<td>Словарь, содержащий переменные окружения</td>
</tr>
<tr>
<td><code>os.getlogin()</code></td>
<td>Возвращает имя пользователя, вошедшего в систему</td>
</tr>
<tr>
<td><code>os.getpid()</code></td>
<td>Возвращает идентификатор текущего процесса</td>
</tr>
<tr>
<td><code>os.getppid()</code></td>
<td>Возвращает идентификатор родительского процесса</td>
</tr>
<tr>
<td><code>os.cpu_count()</code></td>
<td>Возвращает количество процессоров в системе</td>
</tr>
<tr>
<td><code>os.uname()</code></td>
<td>Возвращает информацию о системе, такую как имя системы, имя узла и версию ОС (только Unix)</td>
</tr>
<tr>
<td><code>os.putenv(key, value)</code></td>
<td>Устанавливает значение переменной окружения <strong>(не рекомендуется)</strong></td>
</tr>
<tr>
<td><code>os.unsetenv(key)</code></td>
<td>Удаляет переменную окружения <strong>(не рекомендуется)</strong></td>
</tr>
</tbody>
</table>
<h1>Константы для работы с правами доступа и процессами</h1>
<table>
<thead>
<tr>
<th>Константа</th>
<th>Описание</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>os.F_OK</code></td>
<td>Проверка на существование файла (используется в <code>os.access</code>)</td>
</tr>
<tr>
<td><code>os.R_OK</code></td>
<td>Проверка на возможность чтения файла (используется в <code>os.access</code>)</td>
</tr>
<tr>
<td><code>os.W_OK</code></td>
<td>Проверка на возможность записи в файл (используется в <code>os.access</code>)</td>
</tr>
<tr>
<td><code>os.X_OK</code></td>
<td>Проверка на возможность выполнения файла (используется в <code>os.access</code>)</td>
</tr>
<tr>
<td><code>os.EX_OK</code></td>
<td>Статус выхода для успешного выполнения команды (обычно 0)</td>
</tr>
<tr>
<td><code>os.O_RDONLY</code></td>
<td>Открытие файла только для чтения</td>
</tr>
<tr>
<td><code>os.O_WRONLY</code></td>
<td>Открытие файла только для записи</td>
</tr>
<tr>
<td><code>os.O_RDWR</code></td>
<td>Открытие файла для чтения и записи</td>
</tr>
<tr>
<td><code>os.O_CREAT</code></td>
<td>Создание файла, если он не существует</td>
</tr>
<tr>
<td><code>os.O_EXCL</code></td>
<td>Используется с <code>O_CREAT</code>, чтобы убедиться, что операция создания не завершится, если файл уже существует</td>
</tr>
<tr>
<td><code>os.O_TRUNC</code></td>
<td>Очищает файл при его открытии, если он существует</td>
</tr>
<tr>
<td><code>os.O_APPEND</code></td>
<td>Добавление данных в конец файла</td>
</tr>
<tr>
<td><code>os.O_BINARY</code></td>
<td>Открытие файла в бинарном режиме (Windows)</td>
</tr>
<tr>
<td><code>os.O_TEXT</code></td>
<td>Открытие файла в текстовом режиме (Windows)</td>
</tr>
<tr>
<td><code>os.O_TEMPORARY</code></td>
<td>Открытие временного файла (Windows)</td>
</tr>
<tr>
<td><code>os.O_SHORT_LIVED</code></td>
<td>Указание, что файл будет существовать недолго (Windows)</td>
</tr>
<tr>
<td><code>os.O_SEQUENTIAL</code></td>
<td>Указание, что файл будет читаться последовательно (Windows)</td>
</tr>
<tr>
<td><code>os.O_RANDOM</code></td>
<td>Указание, что файл будет читаться в произвольном порядке (Windows)</td>
</tr>
<tr>
<td><code>os.P_NOWAIT</code></td>
<td>Дочерний процесс запускается, но родительский процесс продолжает выполнение (используется в <code>os.spawnv</code>)</td>
</tr>
<tr>
<td><code>os.P_WAIT</code></td>
<td>Родительский процесс ожидает завершения дочернего процесса (используется в <code>os.spawnv</code>)</td>
</tr>
<tr>
<td><code>os.P_DETACH</code></td>
<td>Дочерний процесс отделяется от родителя и не может получить доступ к его оконному интерфейсу (Windows)</td>
</tr>
</tbody>
</table>
<h1>Управление файловыми дескрипторами</h1>
<table>
<thead>
<tr>
<th>Переменная</th>
<th>Описание</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>os.SEEK_SET</code></td>
<td>Смещение для начала файла (значение <code>0</code>)</td>
</tr>
<tr>
<td><code>os.SEEK_CUR</code></td>
<td>Смещение для текущей позиции в файле (значение <code>1</code>)</td>
</tr>
<tr>
<td><code>os.SEEK_END</code></td>
<td>Смещение для конца файла (значение <code>2</code>)</td>
</tr>
</tbody>
</table>
<h2>Примеры использования</h2>
<h3>Получение списка всех поддиректорий в директории:</h3>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">os</span>

<span class="nb">print</span><span class="p">([</span><span class="n">f</span><span class="o">.</span><span class="n">path</span> <span class="k">for</span> <span class="n">f</span> <span class="ow">in</span> <span class="n">os</span><span class="o">.</span><span class="n">scandir</span><span class="p">(</span><span class="s2">&quot;my_dir&quot;</span><span class="p">)</span> <span class="k">if</span> <span class="n">f</span><span class="o">.</span><span class="n">is_dir</span><span class="p">()])</span>
</pre></div></div></div>

<h3>Работа с файловыми путями</h3>
<div class="code_element"><div class="lang_line"><text>pycon</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-pycon"><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="kn">import</span> <span class="nn">os</span>
<span class="unselectable"><span class="gp">&gt;&gt;&gt;</span></span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="n">path</span> <span class="o">=</span> <span class="s2">&quot;/path/to/file.txt&quot;</span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Базовое имя файла:&quot;</span><span class="p">,</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">basename</span><span class="p">(</span><span class="n">path</span><span class="p">))</span>
<span class="unselectable"><span class="go">Базовое имя файла: file.txt</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Директория:&quot;</span><span class="p">,</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">dirname</span><span class="p">(</span><span class="n">path</span><span class="p">))</span>
<span class="unselectable"><span class="go">Директория: /path/to</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Существует ли файл:&quot;</span><span class="p">,</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="n">path</span><span class="p">))</span>
<span class="unselectable"><span class="go">Существует ли файл: False</span>
</span></pre></div></div></div>

<h3>Работа с файлами</h3>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">os</span>

<span class="n">fd</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="s2">&quot;example.txt&quot;</span><span class="p">,</span> <span class="n">os</span><span class="o">.</span><span class="n">O_CREAT</span> <span class="o">|</span> <span class="n">os</span><span class="o">.</span><span class="n">O_WRONLY</span><span class="p">)</span>
<span class="n">os</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">fd</span><span class="p">,</span> <span class="sa">b</span><span class="s2">&quot;Hello, World!&quot;</span><span class="p">)</span>
<span class="n">os</span><span class="o">.</span><span class="n">close</span><span class="p">(</span><span class="n">fd</span><span class="p">)</span>
</pre></div></div></div>

<h3>Чтение и запись через файловый дескриптор</h3>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">os</span>

<span class="n">fd</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="s2">&quot;file.txt&quot;</span><span class="p">,</span> <span class="n">os</span><span class="o">.</span><span class="n">O_RDWR</span> <span class="o">|</span> <span class="n">os</span><span class="o">.</span><span class="n">O_CREAT</span><span class="p">)</span>
<span class="n">os</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">fd</span><span class="p">,</span> <span class="sa">b</span><span class="s2">&quot;Hello, World!&quot;</span><span class="p">)</span>
<span class="n">os</span><span class="o">.</span><span class="n">lseek</span><span class="p">(</span><span class="n">fd</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="n">os</span><span class="o">.</span><span class="n">SEEK_SET</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">read</span><span class="p">(</span><span class="n">fd</span><span class="p">,</span> <span class="mi">12</span><span class="p">))</span>
<span class="n">os</span><span class="o">.</span><span class="n">close</span><span class="p">(</span><span class="n">fd</span><span class="p">)</span>
</pre></div></div></div>

<h3>Выполнение системной команды и получение результата</h3>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">os</span>

<span class="n">stream</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">popen</span><span class="p">(</span><span class="s2">&quot;ls&quot;</span><span class="p">)</span>
<span class="n">output</span> <span class="o">=</span> <span class="n">stream</span><span class="o">.</span><span class="n">read</span><span class="p">()</span>
<span class="nb">print</span><span class="p">(</span><span class="n">output</span><span class="p">)</span>
</pre></div></div></div>

<h3>Получение случайных данных</h3>
<div class="code_element"><div class="lang_line"><text>pycon</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-pycon"><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="kn">import</span> <span class="nn">os</span>
<span class="unselectable"><span class="gp">&gt;&gt;&gt;</span></span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="n">random_bytes</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">urandom</span><span class="p">(</span><span class="mi">16</span><span class="p">)</span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Случайные байты:&quot;</span><span class="p">,</span> <span class="n">random_bytes</span><span class="p">)</span>
<span class="unselectable"><span class="go">Случайные байты: b&quot;U\x1c\x9a\xec\x80E!\xc2\xdaR\x03\xab\xb8\x19\xe0\xa4&quot;</span>
</span></pre></div></div></div>

<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">os</span>

<span class="k">with</span> <span class="n">os</span><span class="o">.</span><span class="n">scandir</span><span class="p">(</span><span class="s2">&quot;directory&quot;</span><span class="p">)</span> <span class="k">as</span> <span class="n">it</span><span class="p">:</span>
    <span class="k">for</span> <span class="n">entry</span> <span class="ow">in</span> <span class="n">it</span><span class="p">:</span>
        <span class="nb">print</span><span class="p">(</span><span class="n">entry</span><span class="o">.</span><span class="n">name</span><span class="p">,</span> <span class="n">entry</span><span class="o">.</span><span class="n">is_file</span><span class="p">(),</span> <span class="n">entry</span><span class="o">.</span><span class="n">is_dir</span><span class="p">())</span>
</pre></div></div></div>

<h3>Выполнение команды в оболочке</h3>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">os</span>

<span class="n">os</span><span class="o">.</span><span class="n">system</span><span class="p">(</span><span class="s2">&quot;echo Hello, World!&quot;</span><span class="p">)</span>
</pre></div></div></div>

<h3>Работа с путями</h3>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">os</span>

<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Разделитель путей:&quot;</span><span class="p">,</span> <span class="n">os</span><span class="o">.</span><span class="n">sep</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Разделитель расширений:&quot;</span><span class="p">,</span> <span class="n">os</span><span class="o">.</span><span class="n">extsep</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Путь к devnull:&quot;</span><span class="p">,</span> <span class="n">os</span><span class="o">.</span><span class="n">devnull</span><span class="p">)</span>
</pre></div></div></div>

<h3>Создание и удаление директорий</h3>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">os</span>

<span class="n">os</span><span class="o">.</span><span class="n">makedirs</span><span class="p">(</span><span class="s2">&quot;example_dir/subdir&quot;</span><span class="p">)</span>
<span class="n">os</span><span class="o">.</span><span class="n">removedirs</span><span class="p">(</span><span class="s2">&quot;example_dir/subdir&quot;</span><span class="p">)</span>
</pre></div></div></div>

<h1>Полезные ссылки</h1>
<ul>
<li><a href="https://docs.python.org/3/library/os.html">Официальная документация</a></li>
<li><a href="https://realpython.com/python-os-module/">Real Python - How to Use Python’s os and subprocess Modules</a></li>
<li><a href="https://realpython.com/working-with-files-in-python/">Real Python - Working with Files in Python</a></li>
</ul>