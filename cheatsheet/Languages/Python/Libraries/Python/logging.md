<p>Библиотека "logging" в Python используется для добавления логирования,
то есть записи информации о работе программы, чтобы отслеживать ее выполнение и находить ошибки или проблемы.</p>
<p>Методы модуля "logging" и его подмодулей:</p>
<p><code>getLogger()</code>: Возвращает объект логгера для указанного имени.
<code>basicConfig()</code>: Конфигурирует логгинг с использованием базовых параметров.
<code>Logger.setLevel()</code>: Устанавливает уровень логгирования для указанного логгера.
<code>Logger.addHandler()</code>: Добавляет обработчик к указанному логгеру.
<code>Formatter.format()</code>: Форматирует записи логгера в определенном формате.
<code>StreamHandler</code>: Обработчик, который выводит сообщения логгера в поток (например, на консоль).
<code>FileHandler</code>: Обработчик, который выводит сообщения логгера в файл.
<code>RotatingFileHandler</code>: Обработчик, который выводит сообщения логгера в файл с возможностью
автоматического поворота лог-файла при достижении определенного размера или количества записей.</p>
<p>Наиболее часто используемые методы:</p>
<p><code>logging.debug()</code>: Регистрирует отладочное сообщение.</p>
<pre><code class="language-python">import logging
logging.debug(&quot;This is a debug message&quot;)
</code></pre>
<p><code>logging.info()</code>: Регистрирует информационное сообщение.</p>
<pre><code class="language-python">import logging
logging.info(&quot;This is an info message&quot;)
</code></pre>
<p><code>logging.warning()</code>: Регистрирует предупреждение.</p>
<pre><code class="language-python">import logging
logging.warning(&quot;This is a warning message&quot;)
</code></pre>
<p><code>logging.error()</code>: Регистрирует сообщение об ошибке.</p>
<pre><code class="language-python">import logging
logging.error(&quot;This is an error message&quot;)
</code></pre>
<p><code>logging.critical()</code>: Регистрирует критическое сообщение.</p>
<pre><code class="language-python">import logging
logging.critical(&quot;This is a critical message&quot;)
</code></pre>
<p>import logging</p>
<p>Запись в файл</p>
<pre><code class="language-python">logging.basicConfig(filename=&quot;example.log&quot;,
                    level=logging.DEBUG)
</code></pre>
<p>Запись в консоль</p>
<pre><code class="language-python">logging.basicConfig(level=logging.DEBUG,
                    format=&quot;%(message)s&quot;)
</code></pre>
<p>Запись в файл и в консоль</p>
<pre><code class="language-python">logging.basicConfig(filename=&quot;example.log&quot;,
                    level=logging.DEBUG,
                    format=&quot;%(asctime)s %(levelname)s %(message)s&quot;,
                    datefmt=&quot;%Y-%m-%d %H:%M:%S&quot;)
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
formatter = logging.Formatter(&quot;%(asctime)s &quot;
                              &quot;%(levelname)s &quot;
                              &quot;%(message)s&quot;,
                              datefmt=&quot;%Y-%m-%d %H:%M:%S&quot;)
console.setFormatter(formatter)
logging.getLogger(&quot;&quot;).addHandler(console)
</code></pre>
<p>Для самих сообщений</p>
<pre><code>%s           строка
%d           для целых чисел
%c           для имени логгера
%f           для чисел с плавающей точкой
%r           для строковых представлений объектов
%m           для сообщения журнала
%x           целое число в шестнадцатеричной системе исчисления
%o           целое число в восьмеричной системе исчисления
%e, %E       число в экспоненциальной форме
</code></pre>
<p>Для настроек логгирования</p>
<pre><code>%(message)s     сообщение журнала

%(asctime)s     время записи сообщения в формате (по умолчанию YYYY-MM-DD HH:MM:SS,sss настраивать в basicConfig(datefmt))
%(created)f     время записи сообщения в секундах, начиная с 1 января 1970 года

%(filename)s    имя файла, в котором был вызван логгер
%(funcName)s    имя функции, в которой был вызван логгер
%(name)s        имя логгера, который записывает сообщение
%(module)s      имя модуля, в котором был вызван логгер
%(threadName)s  имя потока, в котором был вызван логгер
%(processName)s имя процесса, в котором был вызван логгер

%(levelname)s   уровень журнала (например, DEBUG, INFO, WARNING, ERROR, CRITICAL)
%(levelno)s     уровень журнала в числовом формате (10 для DEBUG, 20 для INFO и т. д.)

%(lineno)d      номер строки, в которой был вызван логгер
%(pathname)s    полный путь к файлу, в котором был вызван логгер
%(process)d     идентификатор процесса, в котором был вызван логгер
%(thread)d      идентификатор потока, в котором был вызван логгер
</code></pre>
<p>Код для применения функций к тексту</p>
<pre><code class="language-python">logging.info = lambda msg, *args, f=logging.info: f(Up(msg), *args)
</code></pre>