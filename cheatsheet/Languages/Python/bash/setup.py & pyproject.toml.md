<h1>[extras_require]</h1>
<p>Дополнительные зависимости</p>
<p>Используется для того, чтобы предложить пользователю установить дополнительные зависимости,
которые могут быть нужны только для определенных возможностей библиотеки.</p>
<div class="code_element"><div class="lang_line"><text>text</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-text"><div class="highlight"><pre><span></span>pip install libname[all]
</pre></div></div></div>
<p>означает, что вместе с пакетом <code>libname</code> будут установлены все зависимости,
указанные для ключа <code>all</code> в файле <code>setup.py</code> или <code>pyproject.toml</code>.
В квадратных скобках указывается набор функциональности, для которой нужны дополнительные пакеты.
Например, может быть указано <code>libname[dev]</code> для установки зависимостей, необходимых для разработки,
или <code>libname[security]</code> для установки дополнительных пакетов, связанных с безопасностью.</p>
<h2>Как это реализовать</h2>
<p>Нужно отредактировать файл <code>setup.py</code> или <code>pyproject.toml</code> и использовать ключ <code>extras_require</code>.</p>
<h3>setup.py</h3>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">setuptools</span> <span class="kn">import</span> <span class="n">setup</span>

<span class="n">setup</span><span class="p">(</span>
    <span class="n">name</span><span class="o">=</span><span class="s2">&quot;my_library&quot;</span><span class="p">,</span>
    <span class="n">version</span><span class="o">=</span><span class="s2">&quot;0.1&quot;</span><span class="p">,</span>
    <span class="n">packages</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;my_library&quot;</span><span class="p">],</span>
    <span class="n">install_requires</span><span class="o">=</span><span class="p">[</span>
        <span class="s2">&quot;requests&quot;</span><span class="p">,</span>  <span class="c1"># Основные зависимости</span>
    <span class="p">],</span>
    <span class="n">extras_require</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;dev&quot;</span><span class="p">:</span> <span class="p">[</span>
            <span class="s2">&quot;pytest&quot;</span><span class="p">,</span>       <span class="c1"># Зависимости для разработки</span>
            <span class="s2">&quot;black&quot;</span><span class="p">,</span>        <span class="c1"># Форматирование кода</span>
        <span class="p">],</span>
        <span class="s2">&quot;security&quot;</span><span class="p">:</span> <span class="p">[</span>
            <span class="s2">&quot;cryptography&quot;</span><span class="p">,</span>  <span class="c1"># Зависимости для функций безопасности</span>
        <span class="p">],</span>
        <span class="s2">&quot;all&quot;</span><span class="p">:</span> <span class="p">[</span>
            <span class="s2">&quot;pytest&quot;</span><span class="p">,</span>
            <span class="s2">&quot;black&quot;</span><span class="p">,</span>
            <span class="s2">&quot;cryptography&quot;</span><span class="p">,</span>
        <span class="p">],</span>
    <span class="p">},</span>
<span class="p">)</span>
</pre></div></div></div>
<ul>
<li>Основные зависимости перечислены в <code>install_requires</code>. Они будут установлены всегда.</li>
<li>Опциональные зависимости добавляются через ключ <code>extras_require</code>.
Здесь мы добавили два набора зависимостей: <code>dev</code> и <code>security</code>, а также их комбинацию <code>all</code>.</li>
</ul>
<h3>pyproject.toml</h3>
<div class="code_element"><div class="lang_line"><text>toml</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-toml"><div class="highlight"><pre><span></span><span class="k">[tool.poetry]</span>
<span class="n">name</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="s2">&quot;my_library&quot;</span>
<span class="n">version</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="s2">&quot;0.1.0&quot;</span>

<span class="k">[tool.poetry.dependencies]</span>
<span class="n">python</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="s2">&quot;^3.7&quot;</span>
<span class="n">requests</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="s2">&quot;^2.25.1&quot;</span>

<span class="k">[tool.poetry.extras]</span>
<span class="n">dev</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="p">[</span><span class="s2">&quot;pytest&quot;</span><span class="p">,</span><span class="w"> </span><span class="s2">&quot;black&quot;</span><span class="p">]</span>
<span class="n">security</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="p">[</span><span class="s2">&quot;cryptography&quot;</span><span class="p">]</span>
<span class="n">all</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="p">[</span><span class="s2">&quot;pytest&quot;</span><span class="p">,</span><span class="w"> </span><span class="s2">&quot;black&quot;</span><span class="p">,</span><span class="w"> </span><span class="s2">&quot;cryptography&quot;</span><span class="p">]</span>
</pre></div></div></div>

<h1>Консольный скрипт</h1>
<h3>setup.py</h3>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">setuptools</span> <span class="kn">import</span> <span class="n">setup</span><span class="p">,</span> <span class="n">find_packages</span>

<span class="n">setup</span><span class="p">(</span>
    <span class="n">name</span><span class="o">=</span><span class="s2">&quot;your_library_name&quot;</span><span class="p">,</span>
    <span class="n">version</span><span class="o">=</span><span class="s2">&quot;0.1&quot;</span><span class="p">,</span>
    <span class="n">packages</span><span class="o">=</span><span class="n">find_packages</span><span class="p">(),</span>
    <span class="n">install_requires</span><span class="o">=</span><span class="p">[],</span>  <span class="c1"># Список зависимостей</span>
    <span class="n">entry_points</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;console_scripts&quot;</span><span class="p">:</span> <span class="p">[</span>
            <span class="s2">&quot;your-command=your_module:main_function&quot;</span><span class="p">,</span>  <span class="c1"># команда для консоли = модуль:функция</span>
        <span class="p">],</span>
    <span class="p">},</span>
<span class="p">)</span>
</pre></div></div></div>

<ul>
<li><strong><code>console_scripts</code></strong> — это ключ, который указывает, что вы создаете консольную команду.</li>
<li><strong><code>your-command</code></strong> — имя команды, через которое будет доступна ваша библиотека в терминале.</li>
<li><strong><code>your_module:main_function</code></strong> — путь до модуля и функции, которая будет вызвана при выполнении команды.</li>
</ul>
<h3>setup.cfg</h3>
<p>Этот способ позволяет вынести конфигурацию из кода в файл <code>setup.cfg</code>. Это делает конфигурацию более декларативной.</p>
<div class="code_element"><div class="lang_line"><text>ini</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-ini"><div class="highlight"><pre><span></span><span class="k">[metadata]</span>
<span class="na">name</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="s">your_library_name</span>
<span class="na">version</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="s">0.1</span>

<span class="k">[options]</span>
<span class="na">packages</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="s">find:</span>
<span class="na">install_requires</span><span class="w"> </span><span class="o">=</span>

<span class="k">[options.entry_points]</span>
<span class="na">console_scripts</span><span class="w"> </span><span class="o">=</span>
<span class="na">your-command</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="s">your_module:main_function</span>
</pre></div></div></div>

<h3>pyproject.toml</h3>
<p>Формат <code>pyproject.toml</code> рекомендован PEP 518 и используется для настройки современных Python проектов.
В этом файле можно настроить проект для использования с <code>setuptools</code> или другими сборщиками (например, <code>Poetry</code>).</p>
<div class="code_element"><div class="lang_line"><text>toml</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-toml"><div class="highlight"><pre><span></span><span class="k">[build-system]</span>
<span class="n">requires</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="p">[</span><span class="s2">&quot;setuptools&quot;</span><span class="p">,</span><span class="w"> </span><span class="s2">&quot;wheel&quot;</span><span class="p">]</span>
<span class="n">build-backend</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="s2">&quot;setuptools.build_meta&quot;</span>

<span class="k">[project]</span>
<span class="n">name</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="s2">&quot;your_library_name&quot;</span>
<span class="n">version</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="s2">&quot;0.1&quot;</span>
<span class="n">dependencies</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="p">[]</span>

<span class="k">[project.scripts]</span>
<span class="n">your-command</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="s2">&quot;your_module:main_function&quot;</span>
</pre></div></div></div>

<h3>Дополнительные шаги</h3>
<p>Создание <a href="?Languages/Python/bash/venv">виртуального окружения</a></p>
<div class="code_element"><div class="lang_line"><text>bash</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-bash"><div class="highlight"><pre><span></span>python<span class="w"> </span>-m<span class="w"> </span>venv<span class="w"> </span>env
<span class="nb">source</span><span class="w"> </span>env/bin/activate<span class="w">  </span><span class="c1"># Linux/MacOS</span>
.<span class="se">\e</span>nv<span class="se">\S</span>cripts<span class="se">\a</span>ctivate<span class="w">  </span><span class="c1"># Windows</span>
</pre></div></div></div>

<p>Установка проекта локально для разработки
<a href="?Languages/Python/bash/Flags%20cmd%20pip">pip Флаги</a></p>
<div class="code_element"><div class="lang_line"><text>bash</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-bash"><div class="highlight"><pre><span></span>pip<span class="w"> </span>install<span class="w"> </span>-e<span class="w"> </span>.
</pre></div></div></div>
<div class="code_element"><div class="lang_line"><text>bash</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-bash"><div class="highlight"><pre><span></span>your-command
</pre></div></div></div>