<p>Библиотека "getopt" в Python используется для разбора аргументов командной строки.
Она позволяет программам легко определять и обрабатывать аргументы, передаваемые при запуске программы.</p>
<p>Методы и подмодули библиотеки "getopt":
getopt.getopt(args, shortopts, longopts=None): Парсит аргументы командной строки, возвращает пару (opts, args), где opts - список кортежей со значением и аргументом, args - список непарсированных аргументов.
getopt.gnu_getopt(args, shortopts, longopts=None): Аналогичен методу getopt.getopt(), но поддерживает нестандартный формат аргументов, включая возможность использования дефисов в значении аргумента.
getopt.GetoptError: Исключение, возникающее при ошибке разбора аргументов командной строки. Оно содержит информацию об ошибке и методы для доступа к ней.</p>
<p>getopt.getopt(args, shortopts, longopts=None): Парсит аргументы командной строки и возвращает опции и аргументы.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" onclick="copyCode(this)"><svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">getopt</span>
<span class="kn">import</span> <span class="nn">sys</span>

<span class="n">args</span> <span class="o">=</span> <span class="n">sys</span><span class="o">.</span><span class="n">argv</span><span class="p">[</span><span class="mi">1</span><span class="p">:]</span>
<span class="n">shortopts</span> <span class="o">=</span> <span class="s2">&quot;ho:v&quot;</span>   <span class="c1"># Опции без аргументов: -h, -o, -v</span>
<span class="n">longopts</span> <span class="o">=</span> <span class="p">[</span><span class="s2">&quot;help&quot;</span><span class="p">,</span> <span class="s2">&quot;output=&quot;</span><span class="p">,</span> <span class="s2">&quot;verbose&quot;</span><span class="p">]</span>  <span class="c1"># Опции с аргументами: --help, --output, --verbose</span>

<span class="k">try</span><span class="p">:</span>
    <span class="n">opts</span><span class="p">,</span> <span class="n">args</span> <span class="o">=</span> <span class="n">getopt</span><span class="o">.</span><span class="n">getopt</span><span class="p">(</span><span class="n">args</span><span class="p">,</span> <span class="n">shortopts</span><span class="p">,</span> <span class="n">longopts</span><span class="p">)</span>
<span class="k">except</span> <span class="n">getopt</span><span class="o">.</span><span class="n">GetoptError</span><span class="p">:</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Ошибка в аргументах командной строки.&quot;</span><span class="p">)</span>
</pre></div></div></div>

<p>getopt.gnu_getopt(args, shortopts, longopts=None): Парсит аргументы командной строки с нестандартным форматом и возвращает опции и аргументы.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" onclick="copyCode(this)"><svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">getopt</span>
<span class="kn">import</span> <span class="nn">sys</span>

<span class="n">args</span> <span class="o">=</span> <span class="n">sys</span><span class="o">.</span><span class="n">argv</span><span class="p">[</span><span class="mi">1</span><span class="p">:]</span>
<span class="n">shortopts</span> <span class="o">=</span> <span class="s2">&quot;ho:v&quot;</span>   <span class="c1"># Опции без аргументов: -h, -o, -v</span>
<span class="n">longopts</span> <span class="o">=</span> <span class="p">[</span><span class="s2">&quot;help&quot;</span><span class="p">,</span> <span class="s2">&quot;output=&quot;</span><span class="p">,</span> <span class="s2">&quot;verbose&quot;</span><span class="p">]</span>  <span class="c1"># Опции с аргументами: --help, --output, --verbose</span>

<span class="k">try</span><span class="p">:</span>
    <span class="n">opts</span><span class="p">,</span> <span class="n">args</span> <span class="o">=</span> <span class="n">getopt</span><span class="o">.</span><span class="n">gnu_getopt</span><span class="p">(</span><span class="n">args</span><span class="p">,</span> <span class="n">shortopts</span><span class="p">,</span> <span class="n">longopts</span><span class="p">)</span>
<span class="k">except</span> <span class="n">getopt</span><span class="o">.</span><span class="n">GetoptError</span><span class="p">:</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Ошибка в аргументах командной строки.&quot;</span><span class="p">)</span>
</pre></div></div></div>