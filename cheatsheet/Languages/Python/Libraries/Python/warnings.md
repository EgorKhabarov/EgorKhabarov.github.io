<p>Библиотека "warnings" в Python используется для управления предупреждениями, которые могут возникать во время выполнения программы.
Она позволяет контролировать вывод предупреждений и принимать соответствующие действия.</p>
<p>Методы и подмодули библиотеки "warnings":</p>
<p><code>warn(message, warning_type, stacklevel)</code> - генерирует предупреждение с указанным сообщением, типом предупреждения и уровнем стека.
<code>filterwarnings(action, message, category, module, lineno, append)</code> - устанавливает фильтр для предупреждений, определяя действие, текст сообщения, категорию предупреждения, модуль, номер строки и флаг добавления фильтра.
<code>simplefilter(action, category=Warning, lineno=0, append=False)</code> - устанавливает простой фильтр для предупреждений с указанным действием, категорией, номером строки и флагом добавления фильтра.
<code>resetwarnings()</code> - сбрасывает все установленные фильтры предупреждений.
<code>showwarning(message, category, filename, lineno, file=None, line=None)</code> - выводит предупреждение с указанным сообщением, категорией, исходным файлом, номером строки, файлом вывода и строкой кода.
<code>catch_warnings(*, record=False, module=None)</code> - возвращает контекстный менеджер для временного перехвата предупреждений с опциональной записью в список или указанный модуль.</p>
<p><code>warn(message, warning_type, stacklevel)</code> - генерирует предупреждение с заданным сообщением, типом предупреждения и уровнем стека.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-code-button" onclick="copyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">warnings</span>

<span class="n">warnings</span><span class="o">.</span><span class="n">warn</span><span class="p">(</span><span class="s2">&quot;This is a warning message&quot;</span><span class="p">,</span> <span class="ne">UserWarning</span><span class="p">,</span> <span class="n">stacklevel</span><span class="o">=</span><span class="mi">2</span><span class="p">)</span>
</pre></div></div></div>

<p><code>filterwarnings(action, message, category, module, lineno, append)</code> - устанавливает фильтр для предупреждений с указанными параметрами.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-code-button" onclick="copyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">warnings</span>

<span class="n">warnings</span><span class="o">.</span><span class="n">filterwarnings</span><span class="p">(</span><span class="s2">&quot;ignore&quot;</span><span class="p">,</span> <span class="n">category</span><span class="o">=</span><span class="ne">DeprecationWarning</span><span class="p">,</span> <span class="n">module</span><span class="o">=</span><span class="s2">&quot;my_module&quot;</span><span class="p">)</span>
</pre></div></div></div>

<p><code>simplefilter(action, category=Warning, lineno=0, append=False)</code> - устанавливает простой фильтр для предупреждений с указанным действием и категорией.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-code-button" onclick="copyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">warnings</span>

<span class="n">warnings</span><span class="o">.</span><span class="n">simplefilter</span><span class="p">(</span><span class="s2">&quot;ignore&quot;</span><span class="p">,</span> <span class="ne">DeprecationWarning</span><span class="p">)</span>
</pre></div></div></div>

<p><code>resetwarnings()</code> - сбрасывает все установленные фильтры предупреждений.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-code-button" onclick="copyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">warnings</span>

<span class="n">warnings</span><span class="o">.</span><span class="n">resetwarnings</span><span class="p">()</span>
</pre></div></div></div>

<p><code>showwarning(message, category, filename, lineno, file=None, line=None)</code> - выводит предупреждение с указанными параметрами.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-code-button" onclick="copyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">warnings</span>

<span class="n">warnings</span><span class="o">.</span><span class="n">showwarning</span><span class="p">(</span><span class="s2">&quot;This is a warning message&quot;</span><span class="p">,</span> <span class="ne">UserWarning</span><span class="p">,</span> <span class="s2">&quot;example.py&quot;</span><span class="p">,</span> <span class="mi">10</span><span class="p">)</span>
</pre></div></div></div>

<p><code>catch_warnings(*, record=False, module=None)</code> - контекстный менеджер для временного перехвата предупреждений.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-code-button" onclick="copyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">warnings</span>

<span class="k">with</span> <span class="n">warnings</span><span class="o">.</span><span class="n">catch_warnings</span><span class="p">(</span><span class="n">record</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span> <span class="k">as</span> <span class="n">w</span><span class="p">:</span>
    <span class="n">warnings</span><span class="o">.</span><span class="n">warn</span><span class="p">(</span><span class="s2">&quot;This is a warning message&quot;</span><span class="p">)</span>
    <span class="nb">print</span><span class="p">(</span><span class="n">w</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">message</span><span class="p">)</span>
</pre></div></div></div>