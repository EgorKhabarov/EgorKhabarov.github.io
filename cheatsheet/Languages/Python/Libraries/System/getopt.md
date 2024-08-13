<p>Библиотека "getopt" в Python используется для разбора аргументов командной строки.
Она позволяет программам легко определять и обрабатывать аргументы, передаваемые при запуске программы.</p>
<p>Методы и подмодули библиотеки "getopt":
getopt.getopt(args, shortopts, longopts=None): Парсит аргументы командной строки, возвращает пару (opts, args), где opts - список кортежей со значением и аргументом, args - список непарсированных аргументов.
getopt.gnu_getopt(args, shortopts, longopts=None): Аналогичен методу getopt.getopt(), но поддерживает нестандартный формат аргументов, включая возможность использования дефисов в значении аргумента.
getopt.GetoptError: Исключение, возникающее при ошибке разбора аргументов командной строки. Оно содержит информацию об ошибке и методы для доступа к ней.</p>
<p>getopt.getopt(args, shortopts, longopts=None): Парсит аргументы командной строки и возвращает опции и аргументы.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" onclick="copyCode(this)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">getopt</span>
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
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" onclick="copyCode(this)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">getopt</span>
<span class="kn">import</span> <span class="nn">sys</span>

<span class="n">args</span> <span class="o">=</span> <span class="n">sys</span><span class="o">.</span><span class="n">argv</span><span class="p">[</span><span class="mi">1</span><span class="p">:]</span>
<span class="n">shortopts</span> <span class="o">=</span> <span class="s2">&quot;ho:v&quot;</span>   <span class="c1"># Опции без аргументов: -h, -o, -v</span>
<span class="n">longopts</span> <span class="o">=</span> <span class="p">[</span><span class="s2">&quot;help&quot;</span><span class="p">,</span> <span class="s2">&quot;output=&quot;</span><span class="p">,</span> <span class="s2">&quot;verbose&quot;</span><span class="p">]</span>  <span class="c1"># Опции с аргументами: --help, --output, --verbose</span>

<span class="k">try</span><span class="p">:</span>
    <span class="n">opts</span><span class="p">,</span> <span class="n">args</span> <span class="o">=</span> <span class="n">getopt</span><span class="o">.</span><span class="n">gnu_getopt</span><span class="p">(</span><span class="n">args</span><span class="p">,</span> <span class="n">shortopts</span><span class="p">,</span> <span class="n">longopts</span><span class="p">)</span>
<span class="k">except</span> <span class="n">getopt</span><span class="o">.</span><span class="n">GetoptError</span><span class="p">:</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Ошибка в аргументах командной строки.&quot;</span><span class="p">)</span>
</pre></div></div></div>