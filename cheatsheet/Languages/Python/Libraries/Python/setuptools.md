<table>
<thead>
<tr>
<th>Метод</th>
<th>Описание</th>
</tr>
</thead>
<tbody>
<tr>
<td>setup()</td>
<td>Определяет настройки проекта и его зависимости</td>
</tr>
<tr>
<td>find_packages()</td>
<td>Автоматически находит и включает все пакеты проекта</td>
</tr>
<tr>
<td>find_namespace_packages()</td>
<td>Аналогично find_packages(), но для пространств имен</td>
</tr>
<tr>
<td>setup_requires</td>
<td>Зависимости, необходимые для установки проекта</td>
</tr>
<tr>
<td>install_requires</td>
<td>Зависимости, необходимые для работы проекта</td>
</tr>
<tr>
<td>entry_points</td>
<td>Позволяет определить точки входа (entry points) для проекта</td>
</tr>
</tbody>
</table>
<p><strong>setup()</strong></p>
<p>Описание: Определяет основные настройки проекта и его зависимости.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">setuptools</span> <span class="kn">import</span> <span class="n">setup</span>

<span class="n">setup</span><span class="p">(</span>
    <span class="n">name</span><span class="o">=</span><span class="s2">&quot;mypackage&quot;</span><span class="p">,</span>
    <span class="n">version</span><span class="o">=</span><span class="s2">&quot;1.0.0&quot;</span><span class="p">,</span>
    <span class="n">packages</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;mypackage&quot;</span><span class="p">],</span>
    <span class="n">install_requires</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;requests&quot;</span><span class="p">],</span>
<span class="p">)</span>
</pre></div></div></div>

<p><strong>find_packages()</strong></p>
<p>Описание: Автоматически находит и включает все пакеты проекта.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">setuptools</span> <span class="kn">import</span> <span class="n">setup</span><span class="p">,</span> <span class="n">find_packages</span>

<span class="n">setup</span><span class="p">(</span>
    <span class="n">name</span><span class="o">=</span><span class="s2">&quot;mypackage&quot;</span><span class="p">,</span>
    <span class="n">version</span><span class="o">=</span><span class="s2">&quot;1.0.0&quot;</span><span class="p">,</span>
    <span class="n">packages</span><span class="o">=</span><span class="n">find_packages</span><span class="p">(),</span>
<span class="p">)</span>
</pre></div></div></div>

<p><strong>entry_points</strong></p>
<p>Описание: Позволяет определить точки входа (entry points) для проекта, например, для создания скриптов командной строки.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">setuptools</span> <span class="kn">import</span> <span class="n">setup</span>

<span class="n">setup</span><span class="p">(</span>
    <span class="n">name</span><span class="o">=</span><span class="s2">&quot;mypackage&quot;</span><span class="p">,</span>
    <span class="n">version</span><span class="o">=</span><span class="s2">&quot;1.0.0&quot;</span><span class="p">,</span>
    <span class="n">entry_points</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;console_scripts&quot;</span><span class="p">:</span> <span class="p">[</span>
            <span class="s2">&quot;myscript = mypackage.script:main&quot;</span><span class="p">,</span>
        <span class="p">],</span>
    <span class="p">},</span>
<span class="p">)</span>
</pre></div></div></div>