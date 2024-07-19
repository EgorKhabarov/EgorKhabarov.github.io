<p>sys.argv содержит список аргументов командной строки, переданных скрипту. 
Первый элемент списка (sys.argv[0]) является именем скрипта:</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code4dbf3a541c7cf16729e17965a4114988b" onclick="copyCode(code4dbf3a541c7cf16729e17965a4114988, code4dbf3a541c7cf16729e17965a4114988b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code4dbf3a541c7cf16729e17965a4114988"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">sys</span>

<span class="c1"># Передаем два аргумента при запуске скрипта:</span>
<span class="c1"># python myscript.py arg1 arg2</span>
<span class="nb">print</span><span class="p">(</span><span class="n">sys</span><span class="o">.</span><span class="n">argv</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span>  <span class="c1"># myscript.py</span>
<span class="nb">print</span><span class="p">(</span><span class="n">sys</span><span class="o">.</span><span class="n">argv</span><span class="p">[</span><span class="mi">1</span><span class="p">])</span>  <span class="c1"># arg1</span>
<span class="nb">print</span><span class="p">(</span><span class="n">sys</span><span class="o">.</span><span class="n">argv</span><span class="p">[</span><span class="mi">2</span><span class="p">])</span>  <span class="c1"># arg2</span>
</pre></div></div></div>

<p>sys.exit() завершает выполнение программы. 
Можно передать код возврата, который будет использован в качестве кода завершения:</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code6055b32ca1754a8d5a53474ca7b90601b" onclick="copyCode(code6055b32ca1754a8d5a53474ca7b90601, code6055b32ca1754a8d5a53474ca7b90601b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code6055b32ca1754a8d5a53474ca7b90601"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">sys</span>

<span class="c1"># Завершаем программу с кодом 0</span>
<span class="n">sys</span><span class="o">.</span><span class="n">exit</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span>

<span class="c1"># Завершаем программу с кодом ошибки 1</span>
<span class="n">sys</span><span class="o">.</span><span class="n">exit</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span>
</pre></div></div></div>

<p>sys.stdin - стандартный поток ввода
sys.stdout - стандартный поток вывода
sys.stderr - стандартный поток ошибок. 
Эти потоки могут быть перенаправлены в файлы или другие потоки ввода/вывода:</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code0675c4d99531a91bf4c7e1343272f493b" onclick="copyCode(code0675c4d99531a91bf4c7e1343272f493, code0675c4d99531a91bf4c7e1343272f493b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code0675c4d99531a91bf4c7e1343272f493"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">sys</span>

<span class="c1"># Читаем данные из стандартного потока ввода</span>
<span class="n">data</span> <span class="o">=</span> <span class="n">sys</span><span class="o">.</span><span class="n">stdin</span><span class="o">.</span><span class="n">readline</span><span class="p">()</span>

<span class="c1"># Пишем данные в стандартный поток вывода</span>
<span class="n">sys</span><span class="o">.</span><span class="n">stdout</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="s2">&quot;Hello, world!</span><span class="se">\n</span><span class="s2">&quot;</span><span class="p">)</span>

<span class="c1"># Пишем ошибки в стандартный поток ошибок</span>
<span class="n">sys</span><span class="o">.</span><span class="n">stderr</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="s2">&quot;Error occurred</span><span class="se">\n</span><span class="s2">&quot;</span><span class="p">)</span>
</pre></div></div></div>

<p>sys.platform содержит строку, которая идентифицирует операционную систему, на которой запущена программа:</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code452d0a0bfdc221540107b490d86ed88bb" onclick="copyCode(code452d0a0bfdc221540107b490d86ed88b, code452d0a0bfdc221540107b490d86ed88bb)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code452d0a0bfdc221540107b490d86ed88b"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">sys</span>

<span class="k">if</span> <span class="n">sys</span><span class="o">.</span><span class="n">platform</span> <span class="o">==</span> <span class="s2">&quot;win32&quot;</span><span class="p">:</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Windows&quot;</span><span class="p">)</span>
<span class="k">elif</span> <span class="n">sys</span><span class="o">.</span><span class="n">platform</span> <span class="o">==</span> <span class="s2">&quot;linux&quot;</span><span class="p">:</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Linux&quot;</span><span class="p">)</span>
<span class="k">elif</span> <span class="n">sys</span><span class="o">.</span><span class="n">platform</span> <span class="o">==</span> <span class="s2">&quot;darwin&quot;</span><span class="p">:</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;MacOS&quot;</span><span class="p">)</span>
</pre></div></div></div>

<p>sys.getsizeof() возвращает размер объекта в байтах:</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code76c150ddbcc643f1497e2459efa16144b" onclick="copyCode(code76c150ddbcc643f1497e2459efa16144, code76c150ddbcc643f1497e2459efa16144b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code76c150ddbcc643f1497e2459efa16144"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">sys</span>

<span class="n">a</span> <span class="o">=</span> <span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">]</span>
<span class="nb">print</span><span class="p">(</span><span class="n">sys</span><span class="o">.</span><span class="n">getsizeof</span><span class="p">(</span><span class="n">a</span><span class="p">))</span>  <span class="c1"># 88</span>
</pre></div></div></div>

<p>sys.path содержит список путей, в которых Python ищет модули:</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="codee1b999acd1d306ddb1a4fe56c30895a3b" onclick="copyCode(codee1b999acd1d306ddb1a4fe56c30895a3, codee1b999acd1d306ddb1a4fe56c30895a3b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="codee1b999acd1d306ddb1a4fe56c30895a3"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">sys</span>

<span class="nb">print</span><span class="p">(</span><span class="n">sys</span><span class="o">.</span><span class="n">path</span><span class="p">)</span>

<span class="sd">&quot;&quot;&quot;</span>
<span class="sd">[</span>
<span class="sd">    &quot;&quot;, </span>
<span class="sd">    &quot;C:\\Users\\User\\AppData\\Local\\Programs\\Python\\Python311\\python311.zip&quot;, </span>
<span class="sd">    &quot;C:\\Users\\User\\AppData\\Local\\Programs\\Python\\Python311\\DLLs&quot;, </span>
<span class="sd">    &quot;C:\\Users\\User\\AppData\\Local\\Programs\\Python\\Python311\\Lib&quot;, </span>
<span class="sd">    &quot;C:\\Users\\User\\AppData\\Local\\Programs\\Python\\Python311&quot;, </span>
<span class="sd">    &quot;C:\\Users\\User\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\site-packages&quot;</span>
<span class="sd">]</span>
<span class="sd">&quot;&quot;&quot;</span>
</pre></div></div></div>

<p>sys.getdefaultencoding() возвращает кодировку по умолчанию, используемую для строк в Python:</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="codee15d034d6b4ce05e06702b2de097c8c0b" onclick="copyCode(codee15d034d6b4ce05e06702b2de097c8c0, codee15d034d6b4ce05e06702b2de097c8c0b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="codee15d034d6b4ce05e06702b2de097c8c0"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">sys</span>

<span class="nb">print</span><span class="p">(</span><span class="n">sys</span><span class="o">.</span><span class="n">getdefaultencoding</span><span class="p">())</span>  <span class="c1"># utf-8</span>
</pre></div></div></div>

<p>sys.getfilesystemencoding() возвращает кодировку, используемую файловой системой:</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code2396612430ded239407fa2fba4742ccbb" onclick="copyCode(code2396612430ded239407fa2fba4742ccb, code2396612430ded239407fa2fba4742ccbb)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code2396612430ded239407fa2fba4742ccb"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">sys</span>

<span class="nb">print</span><span class="p">(</span><span class="n">sys</span><span class="o">.</span><span class="n">getfilesystemencoding</span><span class="p">())</span>  <span class="c1"># utf-8</span>
</pre></div></div></div>

<p>sys.getwindowsversion() возвращает информацию о версии Windows, если программа запущена в Windows:</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="codefe6c560cb61fdfe5f45c72f2b17e52c5b" onclick="copyCode(codefe6c560cb61fdfe5f45c72f2b17e52c5, codefe6c560cb61fdfe5f45c72f2b17e52c5b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="codefe6c560cb61fdfe5f45c72f2b17e52c5"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">sys</span>

<span class="k">if</span> <span class="n">sys</span><span class="o">.</span><span class="n">platform</span> <span class="o">==</span> <span class="s2">&quot;win32&quot;</span><span class="p">:</span>
    <span class="nb">print</span><span class="p">(</span><span class="n">sys</span><span class="o">.</span><span class="n">getwindowsversion</span><span class="p">())</span>

<span class="sd">&quot;&quot;&quot;sys.getwindowsversion(major=10, minor=0, build=19044, platform=2, service_pack=&quot;&quot;)&quot;&quot;&quot;</span>
</pre></div></div></div>

<p>sys.version содержит строку, которая содержит информацию о версии Python:</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code2e2ed719be583d740d319e51ab6790a9b" onclick="copyCode(code2e2ed719be583d740d319e51ab6790a9, code2e2ed719be583d740d319e51ab6790a9b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code2e2ed719be583d740d319e51ab6790a9"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">sys</span>

<span class="nb">print</span><span class="p">(</span><span class="n">sys</span><span class="o">.</span><span class="n">version</span><span class="p">)</span>

<span class="sd">&quot;&quot;&quot;3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)]&quot;&quot;&quot;</span>
</pre></div></div></div>

<p>sys.modules содержит словарь, содержащий все импортированные модули:</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code15004ef7a1b5342a302c51a83271b344b" onclick="copyCode(code15004ef7a1b5342a302c51a83271b344, code15004ef7a1b5342a302c51a83271b344b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code15004ef7a1b5342a302c51a83271b344"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">sys</span>
<span class="kn">import</span> <span class="nn">math</span>

<span class="nb">print</span><span class="p">(</span><span class="n">sys</span><span class="o">.</span><span class="n">modules</span><span class="p">[</span><span class="s2">&quot;math&quot;</span><span class="p">])</span>  <span class="c1"># &lt;module &#39;math&#39; (built-in)&gt;</span>
</pre></div></div></div>

<p>sys.maxsize содержит максимальное значение целого числа, которое может быть использовано в Python:</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code971471fa9a751618cf8359d4b5f9b352b" onclick="copyCode(code971471fa9a751618cf8359d4b5f9b352, code971471fa9a751618cf8359d4b5f9b352b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code971471fa9a751618cf8359d4b5f9b352"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">sys</span>

<span class="nb">print</span><span class="p">(</span><span class="n">sys</span><span class="o">.</span><span class="n">maxsize</span><span class="p">)</span>  <span class="c1"># 9223372036854775807</span>
</pre></div></div></div>

<p>sys.float_info содержит информацию о типе float в Python:</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code90d622d6157eac38edbbc06f9846c0d5b" onclick="copyCode(code90d622d6157eac38edbbc06f9846c0d5, code90d622d6157eac38edbbc06f9846c0d5b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code90d622d6157eac38edbbc06f9846c0d5"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">sys</span>

<span class="nb">print</span><span class="p">(</span><span class="n">sys</span><span class="o">.</span><span class="n">float_info</span><span class="p">)</span>

<span class="sd">&quot;&quot;&quot;sys.float_info(max=1.7976931348623157e+308, max_exp=1024, max_10_exp=308, min=2.2250738585072014e-308, min_exp=-1021, min_10_exp=-307, dig=15, mant_dig=53, epsilon=2.220446049250313e-16, radix=2, rounds=1)&quot;&quot;&quot;</span>
</pre></div></div></div>

<p>sys.stdin.isatty(), sys.stdout.isatty(), sys.stderr.isatty()
sys.stdin.isatty(), sys.stdout.isatty(), и sys.stderr.isatty() возвращают True, 
если соответствующий поток является терминальным устройством (tty):</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code1a65b341738cc4df16e7d70275f13814b" onclick="copyCode(code1a65b341738cc4df16e7d70275f13814, code1a65b341738cc4df16e7d70275f13814b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code1a65b341738cc4df16e7d70275f13814"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">sys</span>

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
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="codebbd81be7ab502e564c790787937e68f8b" onclick="copyCode(codebbd81be7ab502e564c790787937e68f8, codebbd81be7ab502e564c790787937e68f8b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="codebbd81be7ab502e564c790787937e68f8"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">sys</span>

<span class="nb">print</span><span class="p">(</span><span class="n">sys</span><span class="o">.</span><span class="n">getrecursionlimit</span><span class="p">())</span>  <span class="c1"># 1000</span>

<span class="n">sys</span><span class="o">.</span><span class="n">setrecursionlimit</span><span class="p">(</span><span class="mi">3000</span><span class="p">)</span>
</pre></div></div></div>

<p>sys.settrace() устанавливает функцию обратного вызова для отслеживания исполнения кода Python:</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="codec9bff22e22ca0390ef212d811a82a6f7b" onclick="copyCode(codec9bff22e22ca0390ef212d811a82a6f7, codec9bff22e22ca0390ef212d811a82a6f7b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="codec9bff22e22ca0390ef212d811a82a6f7"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">sys</span>

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
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="coded1e1c551d36ef875dd65328a6abc65dbb" onclick="copyCode(coded1e1c551d36ef875dd65328a6abc65db, coded1e1c551d36ef875dd65328a6abc65dbb)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="coded1e1c551d36ef875dd65328a6abc65db"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">sys</span>

<span class="k">def</span> <span class="nf">divide</span><span class="p">(</span><span class="n">x</span><span class="p">,</span> <span class="n">y</span><span class="p">):</span>
    <span class="k">try</span><span class="p">:</span>
        <span class="n">result</span> <span class="o">=</span> <span class="n">x</span> <span class="o">/</span> <span class="n">y</span>
    <span class="k">except</span><span class="p">:</span>
        <span class="nb">print</span><span class="p">(</span><span class="n">sys</span><span class="o">.</span><span class="n">exc_info</span><span class="p">())</span>

<span class="n">divide</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="mi">0</span><span class="p">)</span>
</pre></div></div></div>