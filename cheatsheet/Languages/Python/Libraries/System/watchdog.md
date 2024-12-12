<p><code>watchdog</code> — это Python-библиотека для мониторинга изменений в файловой системе.
Она позволяет отслеживать создание, удаление, модификацию файлов и папок, а также их перемещение.</p>
<div class="code_element"><div class="lang_line"><text>bash</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-bash"><div class="highlight"><pre><span></span>pip<span class="w"> </span>install<span class="w"> </span>watchdog
</pre></div></div></div>

<table>
<thead>
<tr>
<th>Класс / Метод</th>
<th>Описание</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>Observer</code></td>
<td>Основной класс для запуска наблюдения за файловой системой</td>
</tr>
<tr>
<td><code>Observer.schedule(handler, path, recursive)</code></td>
<td>Назначает обработчик событий для указанного пути</td>
</tr>
<tr>
<td><code>Observer.start()</code></td>
<td>Запускает наблюдение</td>
</tr>
<tr>
<td><code>Observer.stop()</code></td>
<td>Останавливает наблюдение</td>
</tr>
<tr>
<td><code>Observer.join()</code></td>
<td>Блокирует поток до завершения наблюдения</td>
</tr>
<tr>
<td><code>FileSystemEventHandler</code></td>
<td>Базовый класс для создания обработчиков событий</td>
</tr>
<tr>
<td><code>on_created(event)</code></td>
<td>Вызывается при создании файла или директории</td>
</tr>
<tr>
<td><code>on_deleted(event)</code></td>
<td>Вызывается при удалении файла или директории</td>
</tr>
<tr>
<td><code>on_modified(event)</code></td>
<td>Вызывается при изменении файла или директории</td>
</tr>
<tr>
<td><code>on_moved(event)</code></td>
<td>Вызывается при перемещении/переименовании файла или директории</td>
</tr>
<tr>
<td><code>LoggingEventHandler</code></td>
<td>Встроенный обработчик для логирования всех событий</td>
</tr>
<tr>
<td><code>PatternMatchingEventHandler</code></td>
<td>Обработчик событий с поддержкой фильтрации по шаблонам</td>
</tr>
<tr>
<td><code>ignore_patterns</code></td>
<td>Список шаблонов, которые нужно игнорировать</td>
</tr>
<tr>
<td><code>patterns</code></td>
<td>Список шаблонов для отслеживания (например, <code>["*.txt"]</code>)</td>
</tr>
</tbody>
</table>
<h3>Наблюдение за папкой</h3>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">time</span>

<span class="kn">from</span> <span class="nn">watchdog.observers</span> <span class="kn">import</span> <span class="n">Observer</span>
<span class="kn">from</span> <span class="nn">watchdog.events</span> <span class="kn">import</span> <span class="n">FileSystemEventHandler</span>


<span class="k">class</span> <span class="nc">MyHandler</span><span class="p">(</span><span class="n">FileSystemEventHandler</span><span class="p">):</span>
    <span class="k">def</span> <span class="nf">on_created</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">event</span><span class="p">):</span>
        <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;Создан: </span><span class="si">{</span><span class="n">event</span><span class="o">.</span><span class="n">src_path</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">on_deleted</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">event</span><span class="p">):</span>
        <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;Удален: </span><span class="si">{</span><span class="n">event</span><span class="o">.</span><span class="n">src_path</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">on_modified</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">event</span><span class="p">):</span>
        <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;Изменен: </span><span class="si">{</span><span class="n">event</span><span class="o">.</span><span class="n">src_path</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">on_moved</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">event</span><span class="p">):</span>
        <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;Перемещен: </span><span class="si">{</span><span class="n">event</span><span class="o">.</span><span class="n">src_path</span><span class="si">}</span><span class="s2"> -&gt; </span><span class="si">{</span><span class="n">event</span><span class="o">.</span><span class="n">dest_path</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">)</span>


<span class="n">path</span> <span class="o">=</span> <span class="s2">&quot;./watch_folder&quot;</span>
<span class="n">event_handler</span> <span class="o">=</span> <span class="n">MyHandler</span><span class="p">()</span>
<span class="n">observer</span> <span class="o">=</span> <span class="n">Observer</span><span class="p">()</span>
<span class="n">observer</span><span class="o">.</span><span class="n">schedule</span><span class="p">(</span><span class="n">event_handler</span><span class="p">,</span> <span class="n">path</span><span class="p">,</span> <span class="n">recursive</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<span class="n">observer</span><span class="o">.</span><span class="n">start</span><span class="p">()</span>

<span class="k">try</span><span class="p">:</span>
    <span class="k">while</span> <span class="kc">True</span><span class="p">:</span>
        <span class="n">time</span><span class="o">.</span><span class="n">sleep</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span>
<span class="k">except</span> <span class="ne">KeyboardInterrupt</span><span class="p">:</span>
    <span class="n">observer</span><span class="o">.</span><span class="n">stop</span><span class="p">()</span>
<span class="n">observer</span><span class="o">.</span><span class="n">join</span><span class="p">()</span>
</pre></div></div></div>

<h3>Логирование изменений в папке</h3>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">time</span>

<span class="kn">from</span> <span class="nn">watchdog.observers</span> <span class="kn">import</span> <span class="n">Observer</span>
<span class="kn">from</span> <span class="nn">watchdog.events</span> <span class="kn">import</span> <span class="n">LoggingEventHandler</span>


<span class="n">path</span> <span class="o">=</span> <span class="s2">&quot;./watch_folder&quot;</span>
<span class="n">event_handler</span> <span class="o">=</span> <span class="n">LoggingEventHandler</span><span class="p">()</span>
<span class="n">observer</span> <span class="o">=</span> <span class="n">Observer</span><span class="p">()</span>
<span class="n">observer</span><span class="o">.</span><span class="n">schedule</span><span class="p">(</span><span class="n">event_handler</span><span class="p">,</span> <span class="n">path</span><span class="p">,</span> <span class="n">recursive</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<span class="n">observer</span><span class="o">.</span><span class="n">start</span><span class="p">()</span>

<span class="k">try</span><span class="p">:</span>
    <span class="k">while</span> <span class="kc">True</span><span class="p">:</span>
        <span class="n">time</span><span class="o">.</span><span class="n">sleep</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span>
<span class="k">except</span> <span class="ne">KeyboardInterrupt</span><span class="p">:</span>
    <span class="n">observer</span><span class="o">.</span><span class="n">stop</span><span class="p">()</span>
<span class="n">observer</span><span class="o">.</span><span class="n">join</span><span class="p">()</span>
</pre></div></div></div>

<h3>Использование фильтров с <code>PatternMatchingEventHandler</code></h3>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">time</span>

<span class="kn">from</span> <span class="nn">watchdog.observers</span> <span class="kn">import</span> <span class="n">Observer</span>
<span class="kn">from</span> <span class="nn">watchdog.events</span> <span class="kn">import</span> <span class="n">PatternMatchingEventHandler</span>


<span class="k">class</span> <span class="nc">MyHandler</span><span class="p">(</span><span class="n">PatternMatchingEventHandler</span><span class="p">):</span>
    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">patterns</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;*.txt&quot;</span><span class="p">],</span> <span class="n">ignore_patterns</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;*.log&quot;</span><span class="p">],</span> <span class="n">ignore_directories</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">on_created</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">event</span><span class="p">):</span>
        <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;Текстовый файл создан: </span><span class="si">{</span><span class="n">event</span><span class="o">.</span><span class="n">src_path</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">)</span>


<span class="n">path</span> <span class="o">=</span> <span class="s2">&quot;./watch_folder&quot;</span>
<span class="n">event_handler</span> <span class="o">=</span> <span class="n">MyHandler</span><span class="p">()</span>
<span class="n">observer</span> <span class="o">=</span> <span class="n">Observer</span><span class="p">()</span>
<span class="n">observer</span><span class="o">.</span><span class="n">schedule</span><span class="p">(</span><span class="n">event_handler</span><span class="p">,</span> <span class="n">path</span><span class="p">,</span> <span class="n">recursive</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<span class="n">observer</span><span class="o">.</span><span class="n">start</span><span class="p">()</span>

<span class="k">try</span><span class="p">:</span>
    <span class="k">while</span> <span class="kc">True</span><span class="p">:</span>
        <span class="n">time</span><span class="o">.</span><span class="n">sleep</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span>
<span class="k">except</span> <span class="ne">KeyboardInterrupt</span><span class="p">:</span>
    <span class="n">observer</span><span class="o">.</span><span class="n">stop</span><span class="p">()</span>
<span class="n">observer</span><span class="o">.</span><span class="n">join</span><span class="p">()</span>
</pre></div></div></div>

<h3>Отслеживание изменений в нескольких папках</h3>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">time</span>

<span class="kn">from</span> <span class="nn">watchdog.observers</span> <span class="kn">import</span> <span class="n">Observer</span>
<span class="kn">from</span> <span class="nn">watchdog.events</span> <span class="kn">import</span> <span class="n">FileSystemEventHandler</span>


<span class="k">class</span> <span class="nc">MyHandler</span><span class="p">(</span><span class="n">FileSystemEventHandler</span><span class="p">):</span>
    <span class="k">def</span> <span class="nf">on_modified</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">event</span><span class="p">):</span>
        <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;Изменен: </span><span class="si">{</span><span class="n">event</span><span class="o">.</span><span class="n">src_path</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">)</span>


<span class="n">paths</span> <span class="o">=</span> <span class="p">[</span><span class="s2">&quot;./folder1&quot;</span><span class="p">,</span> <span class="s2">&quot;./folder2&quot;</span><span class="p">]</span>
<span class="n">observer</span> <span class="o">=</span> <span class="n">Observer</span><span class="p">()</span>

<span class="k">for</span> <span class="n">path</span> <span class="ow">in</span> <span class="n">paths</span><span class="p">:</span>
    <span class="n">observer</span><span class="o">.</span><span class="n">schedule</span><span class="p">(</span><span class="n">MyHandler</span><span class="p">(),</span> <span class="n">path</span><span class="p">,</span> <span class="n">recursive</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>

<span class="n">observer</span><span class="o">.</span><span class="n">start</span><span class="p">()</span>

<span class="k">try</span><span class="p">:</span>
    <span class="k">while</span> <span class="kc">True</span><span class="p">:</span>
        <span class="n">time</span><span class="o">.</span><span class="n">sleep</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span>
<span class="k">except</span> <span class="ne">KeyboardInterrupt</span><span class="p">:</span>
    <span class="n">observer</span><span class="o">.</span><span class="n">stop</span><span class="p">()</span>
<span class="n">observer</span><span class="o">.</span><span class="n">join</span><span class="p">()</span>
</pre></div></div></div>

<h3>Обработка больших директорий с буферизацией</h3>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">time</span>

<span class="kn">from</span> <span class="nn">watchdog.observers</span> <span class="kn">import</span> <span class="n">Observer</span>
<span class="kn">from</span> <span class="nn">watchdog.events</span> <span class="kn">import</span> <span class="n">FileSystemEventHandler</span>


<span class="k">class</span> <span class="nc">BufferedHandler</span><span class="p">(</span><span class="n">FileSystemEventHandler</span><span class="p">):</span>
    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">events</span> <span class="o">=</span> <span class="p">[]</span>

    <span class="k">def</span> <span class="nf">on_modified</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">event</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">events</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;Изменен: </span><span class="si">{</span><span class="n">event</span><span class="o">.</span><span class="n">src_path</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">)</span>
        <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">events</span><span class="p">)</span> <span class="o">&gt;=</span> <span class="mi">10</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">flush</span><span class="p">()</span>

    <span class="k">def</span> <span class="nf">flush</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;</span><span class="se">\n</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">events</span><span class="p">))</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">events</span><span class="o">.</span><span class="n">clear</span><span class="p">()</span>


<span class="n">path</span> <span class="o">=</span> <span class="s2">&quot;./watch_folder&quot;</span>
<span class="n">event_handler</span> <span class="o">=</span> <span class="n">BufferedHandler</span><span class="p">()</span>
<span class="n">observer</span> <span class="o">=</span> <span class="n">Observer</span><span class="p">()</span>
<span class="n">observer</span><span class="o">.</span><span class="n">schedule</span><span class="p">(</span><span class="n">event_handler</span><span class="p">,</span> <span class="n">path</span><span class="p">,</span> <span class="n">recursive</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<span class="n">observer</span><span class="o">.</span><span class="n">start</span><span class="p">()</span>

<span class="k">try</span><span class="p">:</span>
    <span class="k">while</span> <span class="kc">True</span><span class="p">:</span>
        <span class="n">time</span><span class="o">.</span><span class="n">sleep</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span>
<span class="k">except</span> <span class="ne">KeyboardInterrupt</span><span class="p">:</span>
    <span class="n">observer</span><span class="o">.</span><span class="n">stop</span><span class="p">()</span>
<span class="n">observer</span><span class="o">.</span><span class="n">join</span><span class="p">()</span>
</pre></div></div></div>

<p><a href="https://habr.com/ru/articles/140649/">https://habr.com/ru/articles/140649/</a></p>