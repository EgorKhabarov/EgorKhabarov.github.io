<p>Библиотека "resource" в Python используется для доступа и управления системными ресурсами, такими как время CPU, память и дескрипторы файлов.</p>
<p>Методы и подмодули модуля "resource":</p>
<p><code>getrusage(who)</code> - возвращает информацию о системных ресурсах для указанного процесса или группы процессов.
<code>getrlimit(resource)</code> - получает текущие ограничения на указанный ресурс.
<code>setrlimit(resource, limits)</code> - устанавливает ограничения на указанный ресурс.
<code>getpagesize()</code> - возвращает размер страницы памяти операционной системы.
<code>getrusage()</code> - возвращает информацию о системных ресурсах для текущего процесса.
<code>RUSAGE_SELF</code> - константа, указывающая на текущий процесс.
<code>RUSAGE_CHILDREN</code> - константа, указывающая на дочерние процессы текущего процесса.</p>
<p>Наиболее часто используемые методы:</p>
<p><code>getrusage(who)</code> - получает информацию о системных ресурсах для указанного процесса или группы процессов.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-code-button" onclick="copyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">resource</span>

<span class="n">usage</span> <span class="o">=</span> <span class="n">resource</span><span class="o">.</span><span class="n">getrusage</span><span class="p">(</span><span class="n">resource</span><span class="o">.</span><span class="n">RUSAGE_SELF</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">usage</span><span class="p">)</span>
</pre></div></div></div>

<p><code>getrlimit(resource)</code> - получает текущие ограничения на указанный ресурс.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-code-button" onclick="copyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">resource</span>

<span class="n">limit</span> <span class="o">=</span> <span class="n">resource</span><span class="o">.</span><span class="n">getrlimit</span><span class="p">(</span><span class="n">resource</span><span class="o">.</span><span class="n">RLIMIT_CPU</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">limit</span><span class="p">)</span>
</pre></div></div></div>

<p><code>setrlimit(resource, limits)</code> - устанавливает ограничения на указанный ресурс.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-code-button" onclick="copyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">resource</span>

<span class="c1"># Ограничение на время CPU - 2 секунды</span>
<span class="n">limits</span> <span class="o">=</span> <span class="p">(</span><span class="mi">2</span><span class="p">,</span> <span class="n">resource</span><span class="o">.</span><span class="n">RLIM_INFINITY</span><span class="p">)</span>
<span class="n">resource</span><span class="o">.</span><span class="n">setrlimit</span><span class="p">(</span><span class="n">resource</span><span class="o">.</span><span class="n">RLIMIT_CPU</span><span class="p">,</span> <span class="n">limits</span><span class="p">)</span>
</pre></div></div></div>