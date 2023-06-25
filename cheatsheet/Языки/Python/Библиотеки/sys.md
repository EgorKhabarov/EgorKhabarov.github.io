<p>sys.argv содержит список аргументов командной строки, переданных скрипту. 
Первый элемент списка (sys.argv[0]) является именем скрипта:</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code34b" onclick="copyCode(code34, code34b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code34"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">sys</span>

<span class="c1"># Передаем два аргумента при запуске скрипта:</span>
<span class="c1"># python myscript.py arg1 arg2</span>
<span class="nb">print</span><span class="p">(</span><span class="n">sys</span><span class="o">.</span><span class="n">argv</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span>  <span class="c1"># myscript.py</span>
<span class="nb">print</span><span class="p">(</span><span class="n">sys</span><span class="o">.</span><span class="n">argv</span><span class="p">[</span><span class="mi">1</span><span class="p">])</span>  <span class="c1"># arg1</span>
<span class="nb">print</span><span class="p">(</span><span class="n">sys</span><span class="o">.</span><span class="n">argv</span><span class="p">[</span><span class="mi">2</span><span class="p">])</span>  <span class="c1"># arg2</span>
</pre></div></div></div>

<p>sys.exit() завершает выполнение программы. 
Можно передать код возврата, который будет использован в качестве кода завершения:</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code35b" onclick="copyCode(code35, code35b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code35"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">sys</span>

<span class="c1"># Завершаем программу с кодом 0</span>
<span class="n">sys</span><span class="o">.</span><span class="n">exit</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span>

<span class="c1"># Завершаем программу с кодом ошибки 1</span>
<span class="n">sys</span><span class="o">.</span><span class="n">exit</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span>
</pre></div></div></div>

<p>sys.stdin - стандартный поток ввода
sys.stdout - стандартный поток вывода
sys.stderr - стандартный поток ошибок. 
Эти потоки могут быть перенаправлены в файлы или другие потоки ввода/вывода:</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code36b" onclick="copyCode(code36, code36b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code36"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">sys</span>

<span class="c1"># Читаем данные из стандартного потока ввода</span>
<span class="n">data</span> <span class="o">=</span> <span class="n">sys</span><span class="o">.</span><span class="n">stdin</span><span class="o">.</span><span class="n">readline</span><span class="p">()</span>

<span class="c1"># Пишем данные в стандартный поток вывода</span>
<span class="n">sys</span><span class="o">.</span><span class="n">stdout</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="s2">&quot;Hello, world!</span><span class="se">\n</span><span class="s2">&quot;</span><span class="p">)</span>

<span class="c1"># Пишем ошибки в стандартный поток ошибок</span>
<span class="n">sys</span><span class="o">.</span><span class="n">stderr</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="s2">&quot;Error occurred</span><span class="se">\n</span><span class="s2">&quot;</span><span class="p">)</span>
</pre></div></div></div>

<p>sys.platform содержит строку, которая идентифицирует операционную систему, на которой запущена программа:</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code37b" onclick="copyCode(code37, code37b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code37"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">sys</span>

<span class="k">if</span> <span class="n">sys</span><span class="o">.</span><span class="n">platform</span> <span class="o">==</span> <span class="s2">&quot;win32&quot;</span><span class="p">:</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Windows&quot;</span><span class="p">)</span>
<span class="k">elif</span> <span class="n">sys</span><span class="o">.</span><span class="n">platform</span> <span class="o">==</span> <span class="s2">&quot;linux&quot;</span><span class="p">:</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Linux&quot;</span><span class="p">)</span>
<span class="k">elif</span> <span class="n">sys</span><span class="o">.</span><span class="n">platform</span> <span class="o">==</span> <span class="s2">&quot;darwin&quot;</span><span class="p">:</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;MacOS&quot;</span><span class="p">)</span>
</pre></div></div></div>

<p>sys.getsizeof() возвращает размер объекта в байтах:</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code38b" onclick="copyCode(code38, code38b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code38"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">sys</span>

<span class="n">a</span> <span class="o">=</span> <span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">]</span>
<span class="nb">print</span><span class="p">(</span><span class="n">sys</span><span class="o">.</span><span class="n">getsizeof</span><span class="p">(</span><span class="n">a</span><span class="p">))</span> <span class="c1"># 88</span>
</pre></div></div></div>

<p>sys.path содержит список путей, в которых Python ищет модули:</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code39b" onclick="copyCode(code39, code39b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code39"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">sys</span>

<span class="nb">print</span><span class="p">(</span><span class="n">sys</span><span class="o">.</span><span class="n">path</span><span class="p">)</span>

<span class="sd">&quot;&quot;&quot;</span>
<span class="sd">[</span>
<span class="sd">    &#39;&#39;, </span>
<span class="sd">    &#39;C:\\Users\\Egor\\AppData\\Local\\Programs\\Python\\Python311\\python311.zip&#39;, </span>
<span class="sd">    &#39;C:\\Users\\Egor\\AppData\\Local\\Programs\\Python\\Python311\\DLLs&#39;, </span>
<span class="sd">    &#39;C:\\Users\\Egor\\AppData\\Local\\Programs\\Python\\Python311\\Lib&#39;, </span>
<span class="sd">    &#39;C:\\Users\\Egor\\AppData\\Local\\Programs\\Python\\Python311&#39;, </span>
<span class="sd">    &#39;C:\\Users\\Egor\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\site-packages&#39;</span>
<span class="sd">]</span>
<span class="sd">&quot;&quot;&quot;</span>
</pre></div></div></div>

<p>sys.getdefaultencoding() возвращает кодировку по умолчанию, используемую для строк в Python:</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code40b" onclick="copyCode(code40, code40b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code40"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">sys</span>

<span class="nb">print</span><span class="p">(</span><span class="n">sys</span><span class="o">.</span><span class="n">getdefaultencoding</span><span class="p">())</span>  <span class="c1"># utf-8</span>
</pre></div></div></div>

<p>sys.getfilesystemencoding() возвращает кодировку, используемую файловой системой:</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code41b" onclick="copyCode(code41, code41b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code41"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">sys</span>

<span class="nb">print</span><span class="p">(</span><span class="n">sys</span><span class="o">.</span><span class="n">getfilesystemencoding</span><span class="p">())</span>  <span class="c1"># utf-8</span>
</pre></div></div></div>

<p>sys.getwindowsversion() возвращает информацию о версии Windows, если программа запущена в Windows:</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code42b" onclick="copyCode(code42, code42b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code42"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">sys</span>

<span class="k">if</span> <span class="n">sys</span><span class="o">.</span><span class="n">platform</span> <span class="o">==</span> <span class="s2">&quot;win32&quot;</span><span class="p">:</span>
    <span class="nb">print</span><span class="p">(</span><span class="n">sys</span><span class="o">.</span><span class="n">getwindowsversion</span><span class="p">())</span>

<span class="sd">&quot;&quot;&quot;sys.getwindowsversion(major=10, minor=0, build=19044, platform=2, service_pack=&#39;&#39;)&quot;&quot;&quot;</span>
</pre></div></div></div>

<p>sys.version содержит строку, которая содержит информацию о версии Python:</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code43b" onclick="copyCode(code43, code43b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code43"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">sys</span>

<span class="nb">print</span><span class="p">(</span><span class="n">sys</span><span class="o">.</span><span class="n">version</span><span class="p">)</span>

<span class="sd">&quot;&quot;&quot;3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)]&quot;&quot;&quot;</span>
</pre></div></div></div>

<p>sys.modules содержит словарь, содержащий все импортированные модули:</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code44b" onclick="copyCode(code44, code44b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code44"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">sys</span>
<span class="kn">import</span> <span class="nn">math</span>

<span class="nb">print</span><span class="p">(</span><span class="n">sys</span><span class="o">.</span><span class="n">modules</span><span class="p">[</span><span class="s2">&quot;math&quot;</span><span class="p">])</span>  <span class="c1"># &lt;module &#39;math&#39; (built-in)&gt;</span>
</pre></div></div></div>

<p>sys.maxsize содержит максимальное значение целого числа, которое может быть использовано в Python:</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code45b" onclick="copyCode(code45, code45b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code45"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">sys</span>

<span class="nb">print</span><span class="p">(</span><span class="n">sys</span><span class="o">.</span><span class="n">maxsize</span><span class="p">)</span>  <span class="c1"># 9223372036854775807</span>
</pre></div></div></div>

<p>sys.float_info содержит информацию о типе float в Python:</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code46b" onclick="copyCode(code46, code46b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code46"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">sys</span>

<span class="nb">print</span><span class="p">(</span><span class="n">sys</span><span class="o">.</span><span class="n">float_info</span><span class="p">)</span>

<span class="sd">&quot;&quot;&quot;sys.float_info(max=1.7976931348623157e+308, max_exp=1024, max_10_exp=308, min=2.2250738585072014e-308, min_exp=-1021, min_10_exp=-307, dig=15, mant_dig=53, epsilon=2.220446049250313e-16, radix=2, rounds=1)&quot;&quot;&quot;</span>
</pre></div></div></div>

<p>sys.stdin.isatty(), sys.stdout.isatty(), sys.stderr.isatty()
sys.stdin.isatty(), sys.stdout.isatty(), и sys.stderr.isatty() возвращают True, 
если соответствующий поток является терминальным устройством (tty):</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code47b" onclick="copyCode(code47, code47b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code47"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">sys</span>

<span class="k">if</span> <span class="n">sys</span><span class="o">.</span><span class="n">stdin</span><span class="o">.</span><span class="n">isatty</span><span class="p">():</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;stdin is a tty&quot;</span><span class="p">)</span>
<span class="k">else</span><span class="p">:</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;stdin is not a tty&quot;</span><span class="p">)</span>

<span class="k">if</span> <span class="n">sys</span><span class="o">.</span><span class="n">stdout</span><span class="o">.</span><span class="n">isatty</span><span class="p">():</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;stdout is a tty&quot;</span><span class="p">)</span>
<span class="k">else</span><span class="p">:</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;stdout is not a tty&quot;</span><span class="p">)</span>

<span class="k">if</span> <span class="n">sys</span><span class="o">.</span><span class="n">stderr</span><span class="o">.</span><span class="n">isatty</span><span class="p">():</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;stderr is a tty&quot;</span><span class="p">)</span>
<span class="k">else</span><span class="p">:</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;stderr is not a tty&quot;</span><span class="p">)</span>
</pre></div></div></div>

<p>sys.getrecursionlimit() возвращает текущий предел рекурсии Python. sys.setrecursionlimit() устанавливает предел рекурсии Python:</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code48b" onclick="copyCode(code48, code48b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code48"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">sys</span>

<span class="nb">print</span><span class="p">(</span><span class="n">sys</span><span class="o">.</span><span class="n">getrecursionlimit</span><span class="p">())</span>  <span class="c1"># 1000</span>

<span class="n">sys</span><span class="o">.</span><span class="n">setrecursionlimit</span><span class="p">(</span><span class="mi">3000</span><span class="p">)</span>
</pre></div></div></div>

<p>sys.settrace() устанавливает функцию обратного вызова для отслеживания исполнения кода Python:</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code49b" onclick="copyCode(code49, code49b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code49"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">sys</span>

<span class="k">def</span> <span class="nf">trace_calls</span><span class="p">(</span><span class="n">frame</span><span class="p">,</span> <span class="n">event</span><span class="p">,</span> <span class="n">arg</span><span class="p">):</span>
    <span class="k">if</span> <span class="n">event</span> <span class="o">==</span> <span class="s2">&quot;call&quot;</span><span class="p">:</span>
        <span class="nb">print</span><span class="p">(</span><span class="n">frame</span><span class="o">.</span><span class="n">f_code</span><span class="o">.</span><span class="n">co_name</span><span class="p">)</span>

    <span class="k">return</span> <span class="n">trace_calls</span>

<span class="n">sys</span><span class="o">.</span><span class="n">settrace</span><span class="p">(</span><span class="n">trace_calls</span><span class="p">)</span>

<span class="k">def</span> <span class="nf">my_function</span><span class="p">():</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Hello, world!&quot;</span><span class="p">)</span>

<span class="n">my_function</span><span class="p">()</span>

<span class="n">sys</span><span class="o">.</span><span class="n">settrace</span><span class="p">(</span><span class="kc">None</span><span class="p">)</span>
</pre></div></div></div>

<p>sys.exc_info() возвращает кортеж из трех значений, представляющих текущее исключение, если оно присутствует:</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code50b" onclick="copyCode(code50, code50b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code50"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">sys</span>

<span class="k">def</span> <span class="nf">divide</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="n">y</span><span class="p">):</span>
    <span class="k">try</span><span class="p">:</span>
        <span class="n">result</span> <span class="o">=</span> <span class="n">x</span> <span class="o">/</span> <span class="n">y</span>
    <span class="k">except</span><span class="p">:</span>
        <span class="nb">print</span><span class="p">(</span><span class="n">sys</span><span class="o">.</span><span class="n">exc_info</span><span class="p">())</span>

<span class="n">divide</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="mi">0</span><span class="p">)</span>
</pre></div></div></div>