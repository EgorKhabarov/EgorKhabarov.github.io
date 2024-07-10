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
<td>Определяет настройки проекта и его зависимости.</td>
</tr>
<tr>
<td>find_packages()</td>
<td>Автоматически находит и включает все пакеты проекта.</td>
</tr>
<tr>
<td>find_namespace_packages()</td>
<td>Аналогично find_packages(), но для пространств имен.</td>
</tr>
<tr>
<td>setup_requires</td>
<td>Зависимости, необходимые для установки проекта.</td>
</tr>
<tr>
<td>install_requires</td>
<td>Зависимости, необходимые для работы проекта.</td>
</tr>
<tr>
<td>entry_points</td>
<td>Позволяет определить точки входа (entry points) для проекта.</td>
</tr>
</tbody>
</table>
<p><strong>setup()</strong></p>
<p>Описание: Определяет основные настройки проекта и его зависимости.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code2179c838fc98c8ff21efdb51fe07d33eb" onclick="copyCode(code2179c838fc98c8ff21efdb51fe07d33e, code2179c838fc98c8ff21efdb51fe07d33eb)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code2179c838fc98c8ff21efdb51fe07d33e"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">setuptools</span> <span class="kn">import</span> <span class="n">setup</span>

<span class="n">setup</span><span class="p">(</span>
    <span class="n">name</span><span class="o">=</span><span class="s1">&#39;mypackage&#39;</span><span class="p">,</span>
    <span class="n">version</span><span class="o">=</span><span class="s1">&#39;1.0.0&#39;</span><span class="p">,</span>
    <span class="n">packages</span><span class="o">=</span><span class="p">[</span><span class="s1">&#39;mypackage&#39;</span><span class="p">],</span>
    <span class="n">install_requires</span><span class="o">=</span><span class="p">[</span><span class="s1">&#39;requests&#39;</span><span class="p">],</span>
<span class="p">)</span>
</pre></div></div></div>

<p><strong>find_packages()</strong></p>
<p>Описание: Автоматически находит и включает все пакеты проекта.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code1fa4b05c9f23835a5f2688f2146b923db" onclick="copyCode(code1fa4b05c9f23835a5f2688f2146b923d, code1fa4b05c9f23835a5f2688f2146b923db)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code1fa4b05c9f23835a5f2688f2146b923d"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">setuptools</span> <span class="kn">import</span> <span class="n">setup</span><span class="p">,</span> <span class="n">find_packages</span>

<span class="n">setup</span><span class="p">(</span>
    <span class="n">name</span><span class="o">=</span><span class="s1">&#39;mypackage&#39;</span><span class="p">,</span>
    <span class="n">version</span><span class="o">=</span><span class="s1">&#39;1.0.0&#39;</span><span class="p">,</span>
    <span class="n">packages</span><span class="o">=</span><span class="n">find_packages</span><span class="p">(),</span>
<span class="p">)</span>
</pre></div></div></div>

<p><strong>entry_points</strong></p>
<p>Описание: Позволяет определить точки входа (entry points) для проекта, например, для создания скриптов командной строки.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code4022a469c87a8728acd3585976194efeb" onclick="copyCode(code4022a469c87a8728acd3585976194efe, code4022a469c87a8728acd3585976194efeb)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code4022a469c87a8728acd3585976194efe"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">setuptools</span> <span class="kn">import</span> <span class="n">setup</span>

<span class="n">setup</span><span class="p">(</span>
    <span class="n">name</span><span class="o">=</span><span class="s1">&#39;mypackage&#39;</span><span class="p">,</span>
    <span class="n">version</span><span class="o">=</span><span class="s1">&#39;1.0.0&#39;</span><span class="p">,</span>
    <span class="n">entry_points</span><span class="o">=</span><span class="p">{</span>
        <span class="s1">&#39;console_scripts&#39;</span><span class="p">:</span> <span class="p">[</span>
            <span class="s1">&#39;myscript = mypackage.script:main&#39;</span><span class="p">,</span>
        <span class="p">],</span>
    <span class="p">},</span>
<span class="p">)</span>
</pre></div></div></div>