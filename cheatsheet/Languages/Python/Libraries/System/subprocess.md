<p>Библиотека <code>subprocess</code> в Python используется для запуска новых процессов, выполнения команд в системе,
а также для управления стандартными потоками ввода, вывода и ошибок.
Эта библиотека предоставляет мощный интерфейс для взаимодействия с внешними процессами.</p>
<h1>Основные функции</h1>
<table>
<thead>
<tr>
<th>Функция</th>
<th>Описание</th>
<th>Пример использования</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>subprocess.run()</code></td>
<td>Выполняет команду, ожидает завершения процесса<br>и возвращает результат в виде объекта <code>CompletedProcess</code></td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="n">result</span> <span class="o">=</span> <span class="n">subprocess</span><span class="o">.</span><span class="n">run</span><span class="p">([</span><span class="s2">&quot;ls&quot;</span><span class="p">,</span> <span class="s2">&quot;-l&quot;</span><span class="p">])</span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td><code>subprocess.Popen()</code></td>
<td>Запускает новый процесс и возвращает объект <code>Popen</code>,<br>который можно использовать для взаимодействия с процессом</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="n">process</span> <span class="o">=</span> <span class="n">subprocess</span><span class="o">.</span><span class="n">Popen</span><span class="p">([</span><span class="s2">&quot;ls&quot;</span><span class="p">,</span> <span class="s2">&quot;-l&quot;</span><span class="p">])</span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td><code>subprocess.call()</code></td>
<td>Выполняет команду и возвращает код завершения процесса</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="n">return_code</span> <span class="o">=</span> <span class="n">subprocess</span><span class="o">.</span><span class="n">call</span><span class="p">([</span><span class="s2">&quot;ls&quot;</span><span class="p">,</span> <span class="s2">&quot;-l&quot;</span><span class="p">])</span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td><code>subprocess.check_call()</code></td>
<td>Выполняет команду и вызывает исключение,<br>если процесс завершился с ошибкой</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="n">subprocess</span><span class="o">.</span><span class="n">check_call</span><span class="p">([</span><span class="s2">&quot;ls&quot;</span><span class="p">,</span> <span class="s2">&quot;-l&quot;</span><span class="p">])</span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td><code>subprocess.check_output()</code></td>
<td>Выполняет команду и возвращает её вывод.<br>Если процесс завершился с ошибкой, вызывается исключение</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="n">output</span> <span class="o">=</span> <span class="n">subprocess</span><span class="o">.</span><span class="n">check_output</span><span class="p">([</span><span class="s2">&quot;ls&quot;</span><span class="p">,</span> <span class="s2">&quot;-l&quot;</span><span class="p">])</span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td><code>subprocess.getoutput()</code></td>
<td>Выполняет команду и возвращает её вывод в виде строки.<br>Удобно для команд, не требующих сложного взаимодействия</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="n">output</span> <span class="o">=</span> <span class="n">subprocess</span><span class="o">.</span><span class="n">getoutput</span><span class="p">(</span><span class="s2">&quot;ls -l&quot;</span><span class="p">)</span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td><code>subprocess.getstatusoutput()</code></td>
<td>Выполняет команду и возвращает кортеж (код завершения, вывод)</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="n">status</span><span class="p">,</span> <span class="n">output</span> <span class="o">=</span> <span class="n">subprocess</span><span class="o">.</span><span class="n">getstatusoutput</span><span class="p">(</span><span class="s2">&quot;ls -l&quot;</span><span class="p">)</span><br></pre></div></pre></div></div></td>
</tr>
</tbody>
</table>
<h2>Класс Popen</h2>
<table>
<thead>
<tr>
<th>Метод</th>
<th>Описание</th>
<th>Пример использования</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>Popen.poll()</code></td>
<td>Проверяет завершился ли процесс.<br>Возвращает код завершения или <code>None</code>, если процесс ещё выполняется</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="n">status</span> <span class="o">=</span> <span class="n">process</span><span class="o">.</span><span class="n">poll</span><span class="p">()</span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td><code>Popen.wait()</code></td>
<td>Ожидает завершения процесса и возвращает код завершения</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="n">return_code</span> <span class="o">=</span> <span class="n">process</span><span class="o">.</span><span class="n">wait</span><span class="p">()</span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td><code>Popen.communicate()</code></td>
<td>Отправляет данные на стандартный ввод процесса<br>и получает данные из стандартного вывода и вывода ошибок</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="n">stdout</span><span class="p">,</span> <span class="n">stderr</span> <span class="o">=</span> <span class="n">process</span><span class="o">.</span><span class="n">communicate</span><span class="p">(</span><span class="n">input_data</span><span class="p">)</span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td><code>Popen.terminate()</code></td>
<td>Посылает процессу сигнал <code>SIGTERM</code>, запрашивая его завершение</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="n">process</span><span class="o">.</span><span class="n">terminate</span><span class="p">()</span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td><code>Popen.kill()</code></td>
<td>Принудительно завершает процесс, посылая сигнал <code>SIGKILL</code></td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="n">process</span><span class="o">.</span><span class="n">kill</span><span class="p">()</span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td><code>Popen.stdin</code></td>
<td>Стандартный поток ввода процесса (если установлен <code>stdin=subprocess.PIPE</code>)</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="n">process</span><span class="o">.</span><span class="n">stdin</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="sa">b</span><span class="s2">&quot;data&quot;</span><span class="p">)</span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td><code>Popen.stdout</code></td>
<td>Стандартный поток вывода процесса (если установлен <code>stdout=subprocess.PIPE</code>)</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="n">output</span> <span class="o">=</span> <span class="n">process</span><span class="o">.</span><span class="n">stdout</span><span class="o">.</span><span class="n">read</span><span class="p">()</span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td><code>Popen.stderr</code></td>
<td>Стандартный поток ошибок процесса (если установлен <code>stderr=subprocess.PIPE</code>)</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="n">error_output</span> <span class="o">=</span> <span class="n">process</span><span class="o">.</span><span class="n">stderr</span><span class="o">.</span><span class="n">read</span><span class="p">()</span><br></pre></div></pre></div></div></td>
</tr>
</tbody>
</table>
<h2>Управление потоками ввода-вывода</h2>
<p>Пример взаимодействия с процессом через потоки ввода-вывода:</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">subprocess</span>

<span class="n">process</span> <span class="o">=</span> <span class="n">subprocess</span><span class="o">.</span><span class="n">Popen</span><span class="p">(</span>
    <span class="p">[</span><span class="s2">&quot;grep&quot;</span><span class="p">,</span> <span class="s2">&quot;pattern&quot;</span><span class="p">],</span>
    <span class="n">stdin</span><span class="o">=</span><span class="n">subprocess</span><span class="o">.</span><span class="n">PIPE</span><span class="p">,</span>
    <span class="n">stdout</span><span class="o">=</span><span class="n">subprocess</span><span class="o">.</span><span class="n">PIPE</span><span class="p">,</span>
    <span class="n">stderr</span><span class="o">=</span><span class="n">subprocess</span><span class="o">.</span><span class="n">PIPE</span>
<span class="p">)</span>

<span class="n">stdout</span><span class="p">,</span> <span class="n">stderr</span> <span class="o">=</span> <span class="n">process</span><span class="o">.</span><span class="n">communicate</span><span class="p">(</span><span class="nb">input</span><span class="o">=</span><span class="sa">b</span><span class="s2">&quot;text</span><span class="se">\n</span><span class="s2">pattern</span><span class="se">\n</span><span class="s2">another line</span><span class="se">\n</span><span class="s2">&quot;</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">stdout</span><span class="o">.</span><span class="n">decode</span><span class="p">())</span>  <span class="c1"># &quot;pattern\n&quot;</span>
</pre></div></div></div>

<h1>Примеры использования</h1>
<h3>Простой запуск команды</h3>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">subprocess</span>

<span class="n">subprocess</span><span class="o">.</span><span class="n">run</span><span class="p">([</span><span class="s2">&quot;ls&quot;</span><span class="p">,</span> <span class="s2">&quot;-l&quot;</span><span class="p">])</span>
</pre></div></div></div>

<h3>Получение вывода команды</h3>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">subprocess</span>

<span class="nb">print</span><span class="p">(</span><span class="n">subprocess</span><span class="o">.</span><span class="n">check_output</span><span class="p">([</span><span class="s2">&quot;echo&quot;</span><span class="p">,</span> <span class="s2">&quot;Hello, World!&quot;</span><span class="p">])</span><span class="o">.</span><span class="n">decode</span><span class="p">())</span>  <span class="c1"># &quot;Hello, World!\n&quot;</span>
</pre></div></div></div>

<h3>Проверка кода завершения</h3>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">subprocess</span>

<span class="k">try</span><span class="p">:</span>
  <span class="n">subprocess</span><span class="o">.</span><span class="n">check_call</span><span class="p">([</span><span class="s2">&quot;false&quot;</span><span class="p">])</span>
<span class="k">except</span> <span class="n">subprocess</span><span class="o">.</span><span class="n">CalledProcessError</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
  <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;Процесс завершился с ошибкой: </span><span class="si">{</span><span class="n">e</span><span class="o">.</span><span class="n">returncode</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">)</span>
</pre></div></div></div>

<h3>Запуск процесса с передачей данных на ввод</h3>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">subprocess</span>

<span class="n">process</span> <span class="o">=</span> <span class="n">subprocess</span><span class="o">.</span><span class="n">Popen</span><span class="p">([</span><span class="s2">&quot;cat&quot;</span><span class="p">],</span> <span class="n">stdin</span><span class="o">=</span><span class="n">subprocess</span><span class="o">.</span><span class="n">PIPE</span><span class="p">,</span> <span class="n">stdout</span><span class="o">=</span><span class="n">subprocess</span><span class="o">.</span><span class="n">PIPE</span><span class="p">)</span>
<span class="n">stdout</span><span class="p">,</span> <span class="n">_</span> <span class="o">=</span> <span class="n">process</span><span class="o">.</span><span class="n">communicate</span><span class="p">(</span><span class="nb">input</span><span class="o">=</span><span class="sa">b</span><span class="s2">&quot;Hello, World!</span><span class="se">\n</span><span class="s2">&quot;</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">stdout</span><span class="o">.</span><span class="n">decode</span><span class="p">())</span>  <span class="c1"># &quot;Hello, World!\n&quot;</span>
</pre></div></div></div>

<h1>Исключения</h1>
<table>
<thead>
<tr>
<th>Исключение</th>
<th>Описание</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>subprocess.CalledProcessError</code></td>
<td>Вызывается, если процесс завершился с ненулевым кодом возврата</td>
</tr>
<tr>
<td><code>subprocess.TimeoutExpired</code></td>
<td>Вызывается, если процесс не завершился в течение указанного времени (используется с <code>timeout</code>)</td>
</tr>
<tr>
<td><code>subprocess.SubprocessError</code></td>
<td>Базовое исключение для всех исключений, связанных с <code>subprocess</code></td>
</tr>
</tbody>
</table>
<h1>Полезные параметры</h1>
<table>
<thead>
<tr>
<th>Параметр</th>
<th>Описание</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>stdin</code></td>
<td>Определяет источник стандартного ввода процесса (например, <code>subprocess.PIPE</code>, <code>None</code>, или файловый объект)</td>
</tr>
<tr>
<td><code>stdout</code></td>
<td>Определяет место, куда будет направлен стандартный вывод процесса (например, <code>subprocess.PIPE</code>, <code>None</code>, или файловый объект)</td>
</tr>
<tr>
<td><code>stderr</code></td>
<td>Определяет место, куда будет направлен стандартный поток ошибок процесса (например, <code>subprocess.PIPE</code>, <code>None</code>, или файловый объект)</td>
</tr>
<tr>
<td><code>shell</code></td>
<td>Если <code>True</code>, команда будет выполнена через оболочку (shell). Будьте осторожны, так как это может быть небезопасно</td>
</tr>
<tr>
<td><code>cwd</code></td>
<td>Устанавливает текущий рабочий каталог для процесса</td>
</tr>
<tr>
<td><code>env</code></td>
<td>Определяет переменные окружения для процесса</td>
</tr>
<tr>
<td><code>universal_newlines</code></td>
<td>Если <code>True</code>, ввод-вывод будет интерпретироваться как текст (строки), а не байты</td>
</tr>
<tr>
<td><code>timeout</code></td>
<td>Определяет максимальное время ожидания завершения процесса, после чего будет вызвано исключение <code>TimeoutExpired</code></td>
</tr>
</tbody>
</table>
<h1>Советы по безопасности</h1>
<ol>
<li><strong>Избегайте использования <code>shell=True</code></strong>, особенно с данными, полученными от пользователя, так как это может привести к уязвимостям типа <code>shell injection</code>.</li>
<li><strong>Используйте абсолютные пути</strong> к командам для повышения безопасности и предсказуемости поведения скрипта.</li>
<li><strong>Управляйте таймаутами</strong> для долгих процессов с помощью параметра <code>timeout</code>.</li>
</ol>
<h1>Полезные ссылки</h1>
<ul>
<li><a href="https://docs.python.org/3/library/subprocess.html">Официальная документация</a></li>
<li><a href="https://realpython.com/python-subprocess/">Real Python - Guide to Subprocess</a></li>
</ul>