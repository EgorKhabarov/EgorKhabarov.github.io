<p>Библиотека "rlcompleter" используется для автоматического завершения кода в интерактивной оболочке Python (REPL) с помощью клавиши Tab.
Она обеспечивает поддержку автозаполнения имён модулей, функций, переменных и атрибутов.</p>
<p>Методы и подмодули библиотеки "rlcompleter":
Submodule: <code>rlcompleter</code>
Метод <code>Completer(...)</code> - инициализирует объект автозавершения для использования в REPL.
Метод <code>Completer.complete(text, state)</code> - выполняет автозавершение указанного текста в заданном состоянии.
Метод <code>Completer.global_matches(text)</code> - возвращает список всех глобальных имен, соответствующих указанному тексту.</p>
<p>Метод <code>Completer.complete(text, state)</code> - данный метод выполняет автозавершение текста <code>text</code> в конкретном состоянии <code>state</code>.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" onclick="copyCode(this)"><svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">rlcompleter</span>

<span class="n">completer</span> <span class="o">=</span> <span class="n">rlcompleter</span><span class="o">.</span><span class="n">Completer</span><span class="p">()</span>
<span class="n">text</span> <span class="o">=</span> <span class="s2">&quot;pr&quot;</span>
<span class="n">state</span> <span class="o">=</span> <span class="mi">0</span>

<span class="n">completions</span> <span class="o">=</span> <span class="n">completer</span><span class="o">.</span><span class="n">complete</span><span class="p">(</span><span class="n">text</span><span class="p">,</span> <span class="n">state</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">completions</span><span class="p">)</span>
</pre></div></div></div>

<p>Метод <code>Completer.global_matches(text)</code> - данный метод возвращает список глобальных имен, которые соответствуют указанному тексту <code>text</code>.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" onclick="copyCode(this)"><svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">rlcompleter</span>

<span class="n">completer</span> <span class="o">=</span> <span class="n">rlcompleter</span><span class="o">.</span><span class="n">Completer</span><span class="p">()</span>
<span class="n">text</span> <span class="o">=</span> <span class="s2">&quot;pr&quot;</span>

<span class="n">matches</span> <span class="o">=</span> <span class="n">completer</span><span class="o">.</span><span class="n">global_matches</span><span class="p">(</span><span class="n">text</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">matches</span><span class="p">)</span>
</pre></div></div></div>