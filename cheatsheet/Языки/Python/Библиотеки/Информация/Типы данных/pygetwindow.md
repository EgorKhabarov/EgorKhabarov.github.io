<p>Библиотека "pygetwindow" используется для управления окнами в операционной системе с помощью Python.
Она предоставляет функции для поиска, получения информации о размерах и позиции окон, а также для управления их видимостью и активностью.</p>
<p>Методы и подмодули библиотеки "pygetwindow":</p>
<p><code>getAllTitles()</code>: Возвращает список заголовков всех открытых окон.
<code>getWindowsWithTitle(title)</code>: Возвращает список окон с указанным заголовком.
<code>getWindowGeometry(window)</code>: Возвращает геометрию (размеры и позицию) указанного окна.
<code>getWindowAt(x, y)</code>: Возвращает окно, находящееся по указанным координатам.
<code>getActiveWindow()</code>: Возвращает активное окно.
<code>getWindowBorders(window)</code>: Возвращает границы указанного окна.
<code>getWindowRect(window)</code>: Возвращает прямоугольник, охватывающий указанное окно.
<code>getWindowPID(window)</code>: Возвращает идентификатор процесса, связанного с указанным окном.
<code>getWindowProcessID(window)</code>: Возвращает идентификатор процесса, связанного с указанным окном.
<code>getWindowThreadID(window)</code>: Возвращает идентификатор потока, связанного с указанным окном.
<code>getWindowThreadProcessId(window)</code>: Возвращает идентификатор потока и процесса, связанных с указанным окном.
<code>getWindowThreadProcessId(window)</code>: Возвращает идентификатор потока и процесса, связанных с указанным окном.
<code>getWindowThreadProcessId(window)</code>: Возвращает идентификатор потока и процесса, связанных с указанным окном.
<code>getWindowThreadProcessId(window)</code>: Возвращает идентификатор потока и процесса, связанных с указанным окном.
<code>getWindowThreadProcessId(window)</code>: Возвращает идентификатор потока и процесса, связанных с указанным окном.
<code>getWindowThreadProcessId(window)</code>: Возвращает идентификатор потока и процесса, связанных с указанным окном.</p>
<p>Некоторые из самых часто используемых методов библиотеки "pygetwindow":</p>
<p><code>getAllTitles()</code>: Возвращает список заголовков всех открытых окон.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code292b" onclick="copyCode(code292, code292b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code292"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pygetwindow</span>

<span class="n">window_titles</span> <span class="o">=</span> <span class="n">pygetwindow</span><span class="o">.</span><span class="n">getAllTitles</span><span class="p">()</span>
<span class="nb">print</span><span class="p">(</span><span class="n">window_titles</span><span class="p">)</span>
</pre></div></div></div>

<p><code>getWindowsWithTitle(title)</code>: Возвращает список окон с указанным заголовком.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code293b" onclick="copyCode(code293, code293b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code293"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pygetwindow</span>

<span class="n">windows</span> <span class="o">=</span> <span class="n">pygetwindow</span><span class="o">.</span><span class="n">getWindowsWithTitle</span><span class="p">(</span><span class="s2">&quot;Notepad&quot;</span><span class="p">)</span>
<span class="k">for</span> <span class="n">window</span> <span class="ow">in</span> <span class="n">windows</span><span class="p">:</span>
    <span class="nb">print</span><span class="p">(</span><span class="n">window</span><span class="o">.</span><span class="n">title</span><span class="p">)</span>
</pre></div></div></div>

<p><code>getActiveWindow()</code>: Возвращает активное окно.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code294b" onclick="copyCode(code294, code294b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code294"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pygetwindow</span>

<span class="n">active_window</span> <span class="o">=</span> <span class="n">pygetwindow</span><span class="o">.</span><span class="n">getActiveWindow</span><span class="p">()</span>
<span class="nb">print</span><span class="p">(</span><span class="n">active_window</span><span class="o">.</span><span class="n">title</span><span class="p">)</span>
</pre></div></div></div>

<p><code>getWindowGeometry(window)</code>: Возвращает геометрию (размеры и позицию) указанного окна.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code295b" onclick="copyCode(code295, code295b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code295"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pygetwindow</span>

<span class="n">window</span> <span class="o">=</span> <span class="n">pygetwindow</span><span class="o">.</span><span class="n">getWindowsWithTitle</span><span class="p">(</span><span class="s2">&quot;Notepad&quot;</span><span class="p">)[</span><span class="mi">0</span><span class="p">]</span>
<span class="n">geometry</span> <span class="o">=</span> <span class="n">pygetwindow</span><span class="o">.</span><span class="n">getWindowGeometry</span><span class="p">(</span><span class="n">window</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">geometry</span><span class="p">)</span>
</pre></div></div></div>

<p><code>getWindowRect(window)</code>: Возвращает прямоугольник, охватывающий указанное окно.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code296b" onclick="copyCode(code296, code296b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code296"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pygetwindow</span>

<span class="n">window</span> <span class="o">=</span> <span class="n">pygetwindow</span><span class="o">.</span><span class="n">getWindowsWithTitle</span><span class="p">(</span><span class="s2">&quot;Notepad&quot;</span><span class="p">)[</span><span class="mi">0</span><span class="p">]</span>
<span class="n">rect</span> <span class="o">=</span> <span class="n">pygetwindow</span><span class="o">.</span><span class="n">getWindowRect</span><span class="p">(</span><span class="n">window</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">rect</span><span class="p">)</span>
</pre></div></div></div>