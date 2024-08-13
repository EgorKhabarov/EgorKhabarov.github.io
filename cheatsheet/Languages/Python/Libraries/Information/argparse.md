<p>Библиотека argparse в Python позволяет легко создавать интерфейсы командной строки для ваших скриптов. 
Эта библиотека предоставляет механизмы для определения аргументов командной строки и автоматического 
генерирования справочной информации и сообщений об ошибках.</p>
<p>Вот несколько примеров использования библиотеки argparse в Python:
Простой скрипт</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" onclick="copyCode(this)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">argparse</span>

<span class="n">parser</span> <span class="o">=</span> <span class="n">argparse</span><span class="o">.</span><span class="n">ArgumentParser</span><span class="p">()</span>
<span class="n">parser</span><span class="o">.</span><span class="n">add_argument</span><span class="p">(</span><span class="s2">&quot;echo&quot;</span><span class="p">,</span> <span class="n">help</span><span class="o">=</span><span class="s2">&quot;echo the string you use here&quot;</span><span class="p">)</span>

<span class="n">args</span> <span class="o">=</span> <span class="n">parser</span><span class="o">.</span><span class="n">parse_args</span><span class="p">()</span>
<span class="nb">print</span><span class="p">(</span><span class="n">args</span><span class="o">.</span><span class="n">echo</span><span class="p">)</span>
</pre></div></div></div>

<p>Для запуска скрипта нужно использовать команду</p>
<div class="code-element"><div class="lang-line"><text>bash</text><button class="copy-button" onclick="copyCode(this)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code"><div class="highlight"><pre><span></span>python<span class="w"> </span>script.py<span class="w"> </span>hello
</pre></div></div></div>

<p>Аргументы с флагами</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" onclick="copyCode(this)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">argparse</span>

<span class="n">parser</span> <span class="o">=</span> <span class="n">argparse</span><span class="o">.</span><span class="n">ArgumentParser</span><span class="p">()</span>
<span class="n">parser</span><span class="o">.</span><span class="n">add_argument</span><span class="p">(</span><span class="s2">&quot;--verbosity&quot;</span><span class="p">,</span> <span class="n">help</span><span class="o">=</span><span class="s2">&quot;increase output verbosity&quot;</span><span class="p">,</span> <span class="n">action</span><span class="o">=</span><span class="s2">&quot;store_true&quot;</span><span class="p">)</span>

<span class="n">args</span> <span class="o">=</span> <span class="n">parser</span><span class="o">.</span><span class="n">parse_args</span><span class="p">()</span>
<span class="k">if</span> <span class="n">args</span><span class="o">.</span><span class="n">verbosity</span><span class="p">:</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;verbosity turned on&quot;</span><span class="p">)</span>
</pre></div></div></div>

<p>Для запуска скрипта нужно использовать команду</p>
<div class="code-element"><div class="lang-line"><text>bash</text><button class="copy-button" onclick="copyCode(this)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code"><div class="highlight"><pre><span></span>python<span class="w"> </span>script.py<span class="w"> </span>--verbosity
</pre></div></div></div>

<p>Опциональный аргумент</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" onclick="copyCode(this)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">argparse</span>

<span class="n">parser</span> <span class="o">=</span> <span class="n">argparse</span><span class="o">.</span><span class="n">ArgumentParser</span><span class="p">()</span>
<span class="n">parser</span><span class="o">.</span><span class="n">add_argument</span><span class="p">(</span><span class="s2">&quot;--number&quot;</span><span class="p">,</span> <span class="n">help</span><span class="o">=</span><span class="s2">&quot;enter a number&quot;</span><span class="p">,</span> <span class="nb">type</span><span class="o">=</span><span class="nb">int</span><span class="p">)</span>

<span class="n">args</span> <span class="o">=</span> <span class="n">parser</span><span class="o">.</span><span class="n">parse_args</span><span class="p">()</span>
<span class="k">if</span> <span class="n">args</span><span class="o">.</span><span class="n">number</span><span class="p">:</span>
    <span class="nb">print</span><span class="p">(</span><span class="n">args</span><span class="o">.</span><span class="n">number</span> <span class="o">*</span> <span class="mi">2</span><span class="p">)</span>
</pre></div></div></div>

<p>Для запуска скрипта нужно использовать команду</p>
<div class="code-element"><div class="lang-line"><text>bash</text><button class="copy-button" onclick="copyCode(this)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code"><div class="highlight"><pre><span></span>python<span class="w"> </span>script.py<span class="w"> </span>--number<span class="w"> </span><span class="m">5</span>
</pre></div></div></div>

<p>Обязательный аргумент</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" onclick="copyCode(this)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">argparse</span>

<span class="n">parser</span> <span class="o">=</span> <span class="n">argparse</span><span class="o">.</span><span class="n">ArgumentParser</span><span class="p">()</span>
<span class="n">parser</span><span class="o">.</span><span class="n">add_argument</span><span class="p">(</span><span class="s2">&quot;filename&quot;</span><span class="p">,</span> <span class="n">help</span><span class="o">=</span><span class="s2">&quot;the name of the file to read&quot;</span><span class="p">)</span>

<span class="n">args</span> <span class="o">=</span> <span class="n">parser</span><span class="o">.</span><span class="n">parse_args</span><span class="p">()</span>
<span class="nb">print</span><span class="p">(</span><span class="n">args</span><span class="o">.</span><span class="n">filename</span><span class="p">)</span>
</pre></div></div></div>

<p>Для запуска скрипта нужно использовать команду</p>
<div class="code-element"><div class="lang-line"><text>bash</text><button class="copy-button" onclick="copyCode(this)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code"><div class="highlight"><pre><span></span>python<span class="w"> </span>script.py<span class="w"> </span>filename.txt
</pre></div></div></div>

<p>Группировка аргументов</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" onclick="copyCode(this)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">argparse</span>

<span class="n">parser</span> <span class="o">=</span> <span class="n">argparse</span><span class="o">.</span><span class="n">ArgumentParser</span><span class="p">()</span>
<span class="n">group</span> <span class="o">=</span> <span class="n">parser</span><span class="o">.</span><span class="n">add_mutually_exclusive_group</span><span class="p">()</span>
<span class="n">group</span><span class="o">.</span><span class="n">add_argument</span><span class="p">(</span><span class="s2">&quot;--verbose&quot;</span><span class="p">,</span> <span class="n">help</span><span class="o">=</span><span class="s2">&quot;increase output verbosity&quot;</span><span class="p">,</span> <span class="n">action</span><span class="o">=</span><span class="s2">&quot;store_true&quot;</span><span class="p">)</span>
<span class="n">group</span><span class="o">.</span><span class="n">add_argument</span><span class="p">(</span><span class="s2">&quot;--quiet&quot;</span><span class="p">,</span> <span class="n">help</span><span class="o">=</span><span class="s2">&quot;decrease output verbosity&quot;</span><span class="p">,</span> <span class="n">action</span><span class="o">=</span><span class="s2">&quot;store_true&quot;</span><span class="p">)</span>

<span class="n">args</span> <span class="o">=</span> <span class="n">parser</span><span class="o">.</span><span class="n">parse_args</span><span class="p">()</span>
<span class="k">if</span> <span class="n">args</span><span class="o">.</span><span class="n">verbose</span><span class="p">:</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;verbosity turned on&quot;</span><span class="p">)</span>
<span class="k">elif</span> <span class="n">args</span><span class="o">.</span><span class="n">quiet</span><span class="p">:</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;verbosity turned off&quot;</span><span class="p">)</span>
</pre></div></div></div>

<p>Для запуска скрипта нужно использовать команду</p>
<div class="code-element"><div class="lang-line"><text>bash</text><button class="copy-button" onclick="copyCode(this)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code"><div class="highlight"><pre><span></span>python<span class="w"> </span>script.py<span class="w"> </span>--verbose<span class="w"> </span>или<span class="w"> </span>python<span class="w"> </span>script.py<span class="w"> </span>--quiet
</pre></div></div></div>

<p>Позиционные аргументы с выбором</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" onclick="copyCode(this)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">argparse</span>

<span class="n">parser</span> <span class="o">=</span> <span class="n">argparse</span><span class="o">.</span><span class="n">ArgumentParser</span><span class="p">()</span>
<span class="n">parser</span><span class="o">.</span><span class="n">add_argument</span><span class="p">(</span><span class="s2">&quot;operation&quot;</span><span class="p">,</span> <span class="n">help</span><span class="o">=</span><span class="s2">&quot;operation to perform&quot;</span><span class="p">,</span> <span class="n">choices</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;add&quot;</span><span class="p">,</span> <span class="s2">&quot;sub&quot;</span><span class="p">,</span> <span class="s2">&quot;mul&quot;</span><span class="p">,</span> <span class="s2">&quot;div&quot;</span><span class="p">])</span>
<span class="n">parser</span><span class="o">.</span><span class="n">add_argument</span><span class="p">(</span><span class="s2">&quot;num1&quot;</span><span class="p">,</span> <span class="n">help</span><span class="o">=</span><span class="s2">&quot;first number&quot;</span><span class="p">,</span> <span class="nb">type</span><span class="o">=</span><span class="nb">int</span><span class="p">)</span>
<span class="n">parser</span><span class="o">.</span><span class="n">add_argument</span><span class="p">(</span><span class="s2">&quot;num2&quot;</span><span class="p">,</span> <span class="n">help</span><span class="o">=</span><span class="s2">&quot;second number&quot;</span><span class="p">,</span> <span class="nb">type</span><span class="o">=</span><span class="nb">int</span><span class="p">)</span>

<span class="n">args</span> <span class="o">=</span> <span class="n">parser</span><span class="o">.</span><span class="n">parse_args</span><span class="p">()</span>
<span class="k">if</span> <span class="n">args</span><span class="o">.</span><span class="n">operation</span> <span class="o">==</span> <span class="s2">&quot;add&quot;</span><span class="p">:</span>
    <span class="nb">print</span><span class="p">(</span><span class="n">args</span><span class="o">.</span><span class="n">num1</span> <span class="o">+</span> <span class="n">args</span><span class="o">.</span><span class="n">num2</span><span class="p">)</span>
<span class="k">elif</span> <span class="n">args</span><span class="o">.</span><span class="n">operation</span> <span class="o">==</span> <span class="s2">&quot;sub&quot;</span><span class="p">:</span>
    <span class="nb">print</span><span class="p">(</span><span class="n">args</span><span class="o">.</span><span class="n">num1</span> <span class="o">-</span> <span class="n">args</span><span class="o">.</span><span class="n">num2</span><span class="p">)</span>
<span class="k">elif</span> <span class="n">args</span><span class="o">.</span><span class="n">operation</span> <span class="o">==</span> <span class="s2">&quot;mul&quot;</span><span class="p">:</span>
    <span class="nb">print</span><span class="p">(</span><span class="n">args</span><span class="o">.</span><span class="n">num1</span> <span class="o">*</span> <span class="n">args</span><span class="o">.</span><span class="n">num2</span><span class="p">)</span>
<span class="k">else</span><span class="p">:</span>
    <span class="nb">print</span><span class="p">(</span><span class="n">args</span><span class="o">.</span><span class="n">num1</span> <span class="o">/</span> <span class="n">args</span><span class="o">.</span><span class="n">num2</span><span class="p">)</span>
</pre></div></div></div>

<p>Для запуска скрипта нужно использовать команду</p>
<div class="code-element"><div class="lang-line"><text>bash</text><button class="copy-button" onclick="copyCode(this)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code"><div class="highlight"><pre><span></span>python<span class="w"> </span>script.py<span class="w"> </span>add<span class="w"> </span><span class="m">5</span><span class="w"> </span><span class="m">3</span>
</pre></div></div></div>

<p>Описание программы и аргументов</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" onclick="copyCode(this)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">argparse</span>

<span class="n">parser</span> <span class="o">=</span> <span class="n">argparse</span><span class="o">.</span><span class="n">ArgumentParser</span><span class="p">(</span><span class="n">description</span><span class="o">=</span><span class="s2">&quot;A simple calculator program&quot;</span><span class="p">)</span>
<span class="n">parser</span><span class="o">.</span><span class="n">add_argument</span><span class="p">(</span><span class="s2">&quot;operation&quot;</span><span class="p">,</span> <span class="n">help</span><span class="o">=</span><span class="s2">&quot;operation to perform&quot;</span><span class="p">,</span> <span class="n">choices</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;add&quot;</span><span class="p">,</span> <span class="s2">&quot;sub&quot;</span><span class="p">,</span> <span class="s2">&quot;mul&quot;</span><span class="p">,</span> <span class="s2">&quot;div&quot;</span><span class="p">])</span>
<span class="n">parser</span><span class="o">.</span><span class="n">add_argument</span><span class="p">(</span><span class="s2">&quot;num1&quot;</span><span class="p">,</span> <span class="n">help</span><span class="o">=</span><span class="s2">&quot;first number&quot;</span><span class="p">,</span> <span class="nb">type</span><span class="o">=</span><span class="nb">int</span><span class="p">)</span>
<span class="n">parser</span><span class="o">.</span><span class="n">add_argument</span><span class="p">(</span><span class="s2">&quot;num2&quot;</span><span class="p">,</span> <span class="n">help</span><span class="o">=</span><span class="s2">&quot;second number&quot;</span><span class="p">,</span> <span class="nb">type</span><span class="o">=</span><span class="nb">int</span><span class="p">)</span>

<span class="n">args</span> <span class="o">=</span> <span class="n">parser</span><span class="o">.</span><span class="n">parse_args</span><span class="p">()</span>
<span class="k">if</span> <span class="n">args</span><span class="o">.</span><span class="n">operation</span> <span class="o">==</span> <span class="s2">&quot;add&quot;</span><span class="p">:</span>
    <span class="nb">print</span><span class="p">(</span><span class="n">args</span><span class="o">.</span><span class="n">num1</span> <span class="o">+</span> <span class="n">args</span><span class="o">.</span><span class="n">num2</span><span class="p">)</span>
<span class="k">elif</span> <span class="n">args</span><span class="o">.</span><span class="n">operation</span> <span class="o">==</span> <span class="s2">&quot;sub&quot;</span><span class="p">:</span>
    <span class="nb">print</span><span class="p">(</span><span class="n">args</span><span class="o">.</span><span class="n">num1</span> <span class="o">-</span> <span class="n">args</span><span class="o">.</span><span class="n">num2</span><span class="p">)</span>
<span class="k">elif</span> <span class="n">args</span><span class="o">.</span><span class="n">operation</span> <span class="o">==</span> <span class="s2">&quot;mul&quot;</span><span class="p">:</span>
    <span class="nb">print</span><span class="p">(</span><span class="n">args</span><span class="o">.</span><span class="n">num1</span> <span class="o">*</span> <span class="n">args</span><span class="o">.</span><span class="n">num2</span><span class="p">)</span>
<span class="k">else</span><span class="p">:</span>
    <span class="nb">print</span><span class="p">(</span><span class="n">args</span><span class="o">.</span><span class="n">num1</span> <span class="o">/</span> <span class="n">args</span><span class="o">.</span><span class="n">num2</span><span class="p">)</span>
</pre></div></div></div>

<p>Для запуска скрипта нужно использовать команду: </p>
<div class="code-element"><div class="lang-line"><text>bash</text><button class="copy-button" onclick="copyCode(this)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code"><div class="highlight"><pre><span></span>python<span class="w"> </span>script.py<span class="w"> </span>--help
</pre></div></div></div>

<p>Парсинг аргументов из файла</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" onclick="copyCode(this)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">argparse</span>

<span class="n">parser</span> <span class="o">=</span> <span class="n">argparse</span><span class="o">.</span><span class="n">ArgumentParser</span><span class="p">(</span><span class="n">fromfile_prefix_chars</span><span class="o">=</span><span class="s2">&quot;@&quot;</span><span class="p">)</span>
<span class="n">parser</span><span class="o">.</span><span class="n">add_argument</span><span class="p">(</span><span class="s2">&quot;operation&quot;</span><span class="p">,</span> <span class="n">help</span><span class="o">=</span><span class="s2">&quot;operation to perform&quot;</span><span class="p">,</span> <span class="n">choices</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;add&quot;</span><span class="p">,</span> <span class="s2">&quot;sub&quot;</span><span class="p">,</span> <span class="s2">&quot;mul&quot;</span><span class="p">,</span> <span class="s2">&quot;div&quot;</span><span class="p">])</span>
<span class="n">parser</span><span class="o">.</span><span class="n">add_argument</span><span class="p">(</span><span class="s2">&quot;num1&quot;</span><span class="p">,</span> <span class="n">help</span><span class="o">=</span><span class="s2">&quot;first number&quot;</span><span class="p">,</span> <span class="nb">type</span><span class="o">=</span><span class="nb">int</span><span class="p">)</span>
<span class="n">parser</span><span class="o">.</span><span class="n">add_argument</span><span class="p">(</span><span class="s2">&quot;num2&quot;</span><span class="p">,</span> <span class="n">help</span><span class="o">=</span><span class="s2">&quot;second number&quot;</span><span class="p">,</span> <span class="nb">type</span><span class="o">=</span><span class="nb">int</span><span class="p">)</span>

<span class="n">args</span> <span class="o">=</span> <span class="n">parser</span><span class="o">.</span><span class="n">parse_args</span><span class="p">([</span><span class="s2">&quot;@args.txt&quot;</span><span class="p">])</span>
<span class="k">if</span> <span class="n">args</span><span class="o">.</span><span class="n">operation</span> <span class="o">==</span> <span class="s2">&quot;add&quot;</span><span class="p">:</span>
    <span class="nb">print</span><span class="p">(</span><span class="n">args</span><span class="o">.</span><span class="n">num1</span> <span class="o">+</span> <span class="n">args</span><span class="o">.</span><span class="n">num2</span><span class="p">)</span>
<span class="k">elif</span> <span class="n">args</span><span class="o">.</span><span class="n">operation</span> <span class="o">==</span> <span class="s2">&quot;sub&quot;</span><span class="p">:</span>
    <span class="nb">print</span><span class="p">(</span><span class="n">args</span><span class="o">.</span><span class="n">num1</span> <span class="o">-</span> <span class="n">args</span><span class="o">.</span><span class="n">num2</span><span class="p">)</span>
<span class="k">elif</span> <span class="n">args</span><span class="o">.</span><span class="n">operation</span> <span class="o">==</span> <span class="s2">&quot;mul&quot;</span><span class="p">:</span>
    <span class="nb">print</span><span class="p">(</span><span class="n">args</span><span class="o">.</span><span class="n">num1</span> <span class="o">*</span> <span class="n">args</span><span class="o">.</span><span class="n">num2</span><span class="p">)</span>
<span class="k">else</span><span class="p">:</span>
    <span class="nb">print</span><span class="p">(</span><span class="n">args</span><span class="o">.</span><span class="n">num1</span> <span class="o">/</span> <span class="n">args</span><span class="o">.</span><span class="n">num2</span><span class="p">)</span>
</pre></div></div></div>

<p>Для использования данного примера нужно создать файл "args.txt" со следующим содержимым</p>
<div class="code-element"><div class="lang-line"><text>text</text><button class="copy-button" onclick="copyCode(this)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code"><div class="highlight"><pre><span></span>add 5 3
</pre></div></div></div>

<p>Затем, чтобы запустить скрипт, нужно использовать команду</p>
<div class="code-element"><div class="lang-line"><text>bash</text><button class="copy-button" onclick="copyCode(this)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code"><div class="highlight"><pre><span></span>python<span class="w"> </span>script.py<span class="w"> </span>@args.txt
</pre></div></div></div>

<p>Аргумент со значением по умолчанию</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" onclick="copyCode(this)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">argparse</span>

<span class="n">parser</span> <span class="o">=</span> <span class="n">argparse</span><span class="o">.</span><span class="n">ArgumentParser</span><span class="p">()</span>
<span class="n">parser</span><span class="o">.</span><span class="n">add_argument</span><span class="p">(</span><span class="s2">&quot;--verbosity&quot;</span><span class="p">,</span> <span class="n">help</span><span class="o">=</span><span class="s2">&quot;increase output verbosity&quot;</span><span class="p">,</span> <span class="n">action</span><span class="o">=</span><span class="s2">&quot;store_true&quot;</span><span class="p">)</span>
<span class="n">parser</span><span class="o">.</span><span class="n">add_argument</span><span class="p">(</span><span class="s2">&quot;--num&quot;</span><span class="p">,</span> <span class="n">help</span><span class="o">=</span><span class="s2">&quot;a number&quot;</span><span class="p">,</span> <span class="nb">type</span><span class="o">=</span><span class="nb">int</span><span class="p">,</span> <span class="n">default</span><span class="o">=</span><span class="mi">5</span><span class="p">)</span>

<span class="n">args</span> <span class="o">=</span> <span class="n">parser</span><span class="o">.</span><span class="n">parse_args</span><span class="p">()</span>
<span class="k">if</span> <span class="n">args</span><span class="o">.</span><span class="n">verbosity</span><span class="p">:</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;verbosity turned on&quot;</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">args</span><span class="o">.</span><span class="n">num</span> <span class="o">*</span> <span class="mi">2</span><span class="p">)</span>
</pre></div></div></div>

<p>Для запуска скрипта нужно использовать команду</p>
<div class="code-element"><div class="lang-line"><text>bash</text><button class="copy-button" onclick="copyCode(this)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code"><div class="highlight"><pre><span></span>python<span class="w"> </span>script.py<span class="w"> </span>--verbosity<span class="w"> </span>--num<span class="w"> </span><span class="m">3</span>
</pre></div></div></div>

<p>Поддержка субкоманд</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" onclick="copyCode(this)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">argparse</span>

<span class="n">parser</span> <span class="o">=</span> <span class="n">argparse</span><span class="o">.</span><span class="n">ArgumentParser</span><span class="p">()</span>
<span class="n">subparsers</span> <span class="o">=</span> <span class="n">parser</span><span class="o">.</span><span class="n">add_subparsers</span><span class="p">(</span><span class="n">title</span><span class="o">=</span><span class="s2">&quot;subcommands&quot;</span><span class="p">,</span> <span class="n">dest</span><span class="o">=</span><span class="s2">&quot;subcommand&quot;</span><span class="p">)</span>

<span class="n">parser_a</span> <span class="o">=</span> <span class="n">subparsers</span><span class="o">.</span><span class="n">add_parser</span><span class="p">(</span><span class="s2">&quot;command_a&quot;</span><span class="p">,</span> <span class="n">help</span><span class="o">=</span><span class="s2">&quot;command a help&quot;</span><span class="p">)</span>
<span class="n">parser_a</span><span class="o">.</span><span class="n">add_argument</span><span class="p">(</span><span class="s2">&quot;foo&quot;</span><span class="p">,</span> <span class="nb">type</span><span class="o">=</span><span class="nb">int</span><span class="p">,</span> <span class="n">help</span><span class="o">=</span><span class="s2">&quot;foo help&quot;</span><span class="p">)</span>

<span class="n">parser_b</span> <span class="o">=</span> <span class="n">subparsers</span><span class="o">.</span><span class="n">add_parser</span><span class="p">(</span><span class="s2">&quot;command_b&quot;</span><span class="p">,</span> <span class="n">help</span><span class="o">=</span><span class="s2">&quot;command b help&quot;</span><span class="p">)</span>
<span class="n">parser_b</span><span class="o">.</span><span class="n">add_argument</span><span class="p">(</span><span class="s2">&quot;--bar&quot;</span><span class="p">,</span> <span class="nb">type</span><span class="o">=</span><span class="nb">str</span><span class="p">,</span> <span class="n">help</span><span class="o">=</span><span class="s2">&quot;bar help&quot;</span><span class="p">)</span>

<span class="n">args</span> <span class="o">=</span> <span class="n">parser</span><span class="o">.</span><span class="n">parse_args</span><span class="p">()</span>
<span class="k">if</span> <span class="n">args</span><span class="o">.</span><span class="n">subcommand</span> <span class="o">==</span> <span class="s2">&quot;command_a&quot;</span><span class="p">:</span>
    <span class="nb">print</span><span class="p">(</span><span class="n">args</span><span class="o">.</span><span class="n">foo</span><span class="p">)</span>
<span class="k">else</span><span class="p">:</span>
    <span class="nb">print</span><span class="p">(</span><span class="n">args</span><span class="o">.</span><span class="n">bar</span><span class="p">)</span>
</pre></div></div></div>

<p>Для запуска скрипта нужно использовать команду: </p>
<div class="code-element"><div class="lang-line"><text>bash</text><button class="copy-button" onclick="copyCode(this)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code"><div class="highlight"><pre><span></span>python<span class="w"> </span>script.py<span class="w"> </span>command_a<span class="w"> </span><span class="m">5</span>
</pre></div></div></div>

<p>или</p>
<div class="code-element"><div class="lang-line"><text>bash</text><button class="copy-button" onclick="copyCode(this)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code"><div class="highlight"><pre><span></span>python<span class="w"> </span>script.py<span class="w"> </span>command_b<span class="w"> </span>--bar<span class="w"> </span><span class="nb">test</span>
</pre></div></div></div>