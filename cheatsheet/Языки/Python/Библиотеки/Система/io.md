<p>Библиотека io в Python предоставляет возможности работы с потоками ввода-вывода.</p>
<p>io.StringIO() - создание в памяти строкового потока.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="coded99b337f64dcd161fc7ab057d4d2d066b" onclick="copyCode(coded99b337f64dcd161fc7ab057d4d2d066, coded99b337f64dcd161fc7ab057d4d2d066b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="coded99b337f64dcd161fc7ab057d4d2d066"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">io</span>

<span class="n">stream</span> <span class="o">=</span> <span class="n">io</span><span class="o">.</span><span class="n">StringIO</span><span class="p">()</span>
<span class="n">stream</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="s2">&quot;Hello, world!&quot;</span><span class="p">)</span>
<span class="n">stream</span><span class="o">.</span><span class="n">seek</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">stream</span><span class="o">.</span><span class="n">read</span><span class="p">())</span>  <span class="c1"># Hello, world!</span>
</pre></div></div></div>

<p>io.BytesIO() - создание в памяти потока байт.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="codef76c5f383f22da0eea9b1ef517e36543b" onclick="copyCode(codef76c5f383f22da0eea9b1ef517e36543, codef76c5f383f22da0eea9b1ef517e36543b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="codef76c5f383f22da0eea9b1ef517e36543"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">io</span>

<span class="n">stream</span> <span class="o">=</span> <span class="n">io</span><span class="o">.</span><span class="n">BytesIO</span><span class="p">()</span>
<span class="n">stream</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="sa">b</span><span class="s2">&quot;Hello, world!&quot;</span><span class="p">)</span>
<span class="n">stream</span><span class="o">.</span><span class="n">seek</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">stream</span><span class="o">.</span><span class="n">read</span><span class="p">())</span>  <span class="c1"># b&#39;Hello, world!&#39;</span>
</pre></div></div></div>

<p>io.open() - открытие файла в нужном режиме.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="codee15bad2d5d5d29d79c2c39ae7a8b7528b" onclick="copyCode(codee15bad2d5d5d29d79c2c39ae7a8b7528, codee15bad2d5d5d29d79c2c39ae7a8b7528b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="codee15bad2d5d5d29d79c2c39ae7a8b7528"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">io</span>

<span class="k">with</span> <span class="n">io</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="s2">&quot;example.txt&quot;</span><span class="p">,</span> <span class="s2">&quot;w&quot;</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
    <span class="n">f</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="s2">&quot;Hello, world!&quot;</span><span class="p">)</span>

<span class="k">with</span> <span class="n">io</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="s2">&quot;example.txt&quot;</span><span class="p">,</span> <span class="s2">&quot;r&quot;</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
    <span class="nb">print</span><span class="p">(</span><span class="n">f</span><span class="o">.</span><span class="n">read</span><span class="p">())</span>  <span class="c1"># Hello, world!</span>
</pre></div></div></div>

<p>io.TextIOWrapper() - обертка для текстовых потоков.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="codea0dc60ed64d9879e4deb7dd9e2ebacc3b" onclick="copyCode(codea0dc60ed64d9879e4deb7dd9e2ebacc3, codea0dc60ed64d9879e4deb7dd9e2ebacc3b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="codea0dc60ed64d9879e4deb7dd9e2ebacc3"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">io</span>

<span class="k">with</span> <span class="n">io</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="s2">&quot;example.txt&quot;</span><span class="p">,</span> <span class="s2">&quot;w&quot;</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
    <span class="n">wrapper</span> <span class="o">=</span> <span class="n">io</span><span class="o">.</span><span class="n">TextIOWrapper</span><span class="p">(</span><span class="n">f</span><span class="p">,</span> <span class="n">encoding</span><span class="o">=</span><span class="s2">&quot;utf-8&quot;</span><span class="p">)</span>
    <span class="n">wrapper</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="s2">&quot;Привет, мир!&quot;</span><span class="p">)</span>

<span class="k">with</span> <span class="n">io</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="s2">&quot;example.txt&quot;</span><span class="p">,</span> <span class="s2">&quot;r&quot;</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
    <span class="n">wrapper</span> <span class="o">=</span> <span class="n">io</span><span class="o">.</span><span class="n">TextIOWrapper</span><span class="p">(</span><span class="n">f</span><span class="p">,</span> <span class="n">encoding</span><span class="o">=</span><span class="s2">&quot;utf-8&quot;</span><span class="p">)</span>
    <span class="nb">print</span><span class="p">(</span><span class="n">wrapper</span><span class="o">.</span><span class="n">read</span><span class="p">())</span>  <span class="c1"># Привет, мир!</span>
</pre></div></div></div>

<p>io.BufferedWriter() - буферизированный записывающий поток.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code3a0c8132b0abd957bf33328637870518b" onclick="copyCode(code3a0c8132b0abd957bf33328637870518, code3a0c8132b0abd957bf33328637870518b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code3a0c8132b0abd957bf33328637870518"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">io</span>

<span class="k">with</span> <span class="n">io</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="s2">&quot;example.txt&quot;</span><span class="p">,</span> <span class="s2">&quot;wb&quot;</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
    <span class="n">writer</span> <span class="o">=</span> <span class="n">io</span><span class="o">.</span><span class="n">BufferedWriter</span><span class="p">(</span><span class="n">f</span><span class="p">)</span>
    <span class="n">writer</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="sa">b</span><span class="s2">&quot;Hello, world!&quot;</span><span class="p">)</span>

<span class="k">with</span> <span class="n">io</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="s2">&quot;example.txt&quot;</span><span class="p">,</span> <span class="s2">&quot;rb&quot;</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
    <span class="n">reader</span> <span class="o">=</span> <span class="n">io</span><span class="o">.</span><span class="n">BufferedReader</span><span class="p">(</span><span class="n">f</span><span class="p">)</span>
    <span class="nb">print</span><span class="p">(</span><span class="n">reader</span><span class="o">.</span><span class="n">read</span><span class="p">())</span>  <span class="c1"># b&#39;Hello, world!&#39;</span>
</pre></div></div></div>

<p>io.BufferedReader() - буферизированный читающий поток.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="codecc92e271280d72cd9f90cb9f6e46a1bcb" onclick="copyCode(codecc92e271280d72cd9f90cb9f6e46a1bc, codecc92e271280d72cd9f90cb9f6e46a1bcb)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="codecc92e271280d72cd9f90cb9f6e46a1bc"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">io</span>

<span class="k">with</span> <span class="n">io</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="s2">&quot;example.txt&quot;</span><span class="p">,</span> <span class="s2">&quot;wb&quot;</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
    <span class="n">f</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="sa">b</span><span class="s2">&quot;Hello, world!&quot;</span><span class="p">)</span>

<span class="k">with</span> <span class="n">io</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="s2">&quot;example.txt&quot;</span><span class="p">,</span> <span class="s2">&quot;rb&quot;</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
    <span class="n">reader</span> <span class="o">=</span> <span class="n">io</span><span class="o">.</span><span class="n">BufferedReader</span><span class="p">(</span><span class="n">f</span><span class="p">)</span>
    <span class="nb">print</span><span class="p">(</span><span class="n">reader</span><span class="o">.</span><span class="n">read</span><span class="p">())</span>  <span class="c1"># b&#39;Hello, world!&#39;</span>
</pre></div></div></div>

<p>io.FileIO() - создание потока для работы с файлом в бинарном режиме.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code1b720f2b1551d2958fd1a0583eb28eaab" onclick="copyCode(code1b720f2b1551d2958fd1a0583eb28eaa, code1b720f2b1551d2958fd1a0583eb28eaab)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code1b720f2b1551d2958fd1a0583eb28eaa"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">io</span>

<span class="k">with</span> <span class="n">io</span><span class="o">.</span><span class="n">FileIO</span><span class="p">(</span><span class="s2">&quot;example.txt&quot;</span><span class="p">,</span> <span class="s2">&quot;w&quot;</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
    <span class="n">f</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="sa">b</span><span class="s2">&quot;Hello, world!&quot;</span><span class="p">)</span>

<span class="k">with</span> <span class="n">io</span><span class="o">.</span><span class="n">FileIO</span><span class="p">(</span><span class="s2">&quot;example.txt&quot;</span><span class="p">,</span> <span class="s2">&quot;r&quot;</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
    <span class="nb">print</span><span class="p">(</span><span class="n">f</span><span class="o">.</span><span class="n">read</span><span class="p">())</span>  <span class="c1"># b&#39;Hello, world!&#39;</span>
</pre></div></div></div>

<p>io.TextIOBase() - базовый класс для всех текстовых потоков.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="coded645665d5980fed43dcdb4567881d01bb" onclick="copyCode(coded645665d5980fed43dcdb4567881d01b, coded645665d5980fed43dcdb4567881d01bb)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="coded645665d5980fed43dcdb4567881d01b"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">io</span>

<span class="k">class</span> <span class="nc">UpperTextIO</span><span class="p">(</span><span class="n">io</span><span class="o">.</span><span class="n">TextIOBase</span><span class="p">):</span>
    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">stream</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_stream</span> <span class="o">=</span> <span class="n">stream</span>

    <span class="k">def</span> <span class="nf">write</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">text</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_stream</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">text</span><span class="o">.</span><span class="n">upper</span><span class="p">())</span>

<span class="k">with</span> <span class="n">io</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="s2">&quot;example.txt&quot;</span><span class="p">,</span> <span class="s2">&quot;w&quot;</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
    <span class="n">wrapper</span> <span class="o">=</span> <span class="n">io</span><span class="o">.</span><span class="n">TextIOWrapper</span><span class="p">(</span><span class="n">f</span><span class="p">,</span> <span class="n">encoding</span><span class="o">=</span><span class="s2">&quot;utf-8&quot;</span><span class="p">)</span>
    <span class="n">upper_wrapper</span> <span class="o">=</span> <span class="n">UpperTextIO</span><span class="p">(</span><span class="n">wrapper</span><span class="p">)</span>
    <span class="n">upper_wrapper</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="s2">&quot;hello, world!&quot;</span><span class="p">)</span>
    <span class="n">wrapper</span><span class="o">.</span><span class="n">flush</span><span class="p">()</span>

<span class="k">with</span> <span class="n">io</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="s2">&quot;example.txt&quot;</span><span class="p">,</span> <span class="s2">&quot;r&quot;</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
    <span class="n">wrapper</span> <span class="o">=</span> <span class="n">io</span><span class="o">.</span><span class="n">TextIOWrapper</span><span class="p">(</span><span class="n">f</span><span class="p">,</span> <span class="n">encoding</span><span class="o">=</span><span class="s2">&quot;utf-8&quot;</span><span class="p">)</span>
    <span class="nb">print</span><span class="p">(</span><span class="n">wrapper</span><span class="o">.</span><span class="n">read</span><span class="p">())</span>  <span class="c1"># HELLO, WORLD!</span>
</pre></div></div></div>

<p>io.StringIO.getvalue() - получение содержимого из строкового потока.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code40aa85165e3ce7912c1693fa042e26f6b" onclick="copyCode(code40aa85165e3ce7912c1693fa042e26f6, code40aa85165e3ce7912c1693fa042e26f6b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code40aa85165e3ce7912c1693fa042e26f6"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">io</span>

<span class="n">stream</span> <span class="o">=</span> <span class="n">io</span><span class="o">.</span><span class="n">StringIO</span><span class="p">()</span>
<span class="n">stream</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="s2">&quot;Hello, world!&quot;</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">stream</span><span class="o">.</span><span class="n">getvalue</span><span class="p">())</span>  <span class="c1"># Hello, world!</span>
</pre></div></div></div>

<p>io.BytesIO.getvalue() - получение содержимого из потока байт.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="codeb97b788eaa6c281c7de7f072e6b823e2b" onclick="copyCode(codeb97b788eaa6c281c7de7f072e6b823e2, codeb97b788eaa6c281c7de7f072e6b823e2b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="codeb97b788eaa6c281c7de7f072e6b823e2"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">io</span>

<span class="n">stream</span> <span class="o">=</span> <span class="n">io</span><span class="o">.</span><span class="n">BytesIO</span><span class="p">()</span>
<span class="n">stream</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="sa">b</span><span class="s2">&quot;Hello, world!&quot;</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">stream</span><span class="o">.</span><span class="n">getvalue</span><span class="p">())</span>  <span class="c1"># b&#39;Hello, world!&#39;</span>
</pre></div></div></div>

<p>io.TextIOWrapper.detach() - отсоединение потока от обертки.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code1c313f92bf3275c555f610e077d90c27b" onclick="copyCode(code1c313f92bf3275c555f610e077d90c27, code1c313f92bf3275c555f610e077d90c27b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code1c313f92bf3275c555f610e077d90c27"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">io</span>

<span class="k">with</span> <span class="n">io</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="s2">&quot;example.txt&quot;</span><span class="p">,</span> <span class="s2">&quot;w&quot;</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
    <span class="n">wrapper</span> <span class="o">=</span> <span class="n">io</span><span class="o">.</span><span class="n">TextIOWrapper</span><span class="p">(</span><span class="n">f</span><span class="p">,</span> <span class="n">encoding</span><span class="o">=</span><span class="s2">&quot;utf-8&quot;</span><span class="p">)</span>
    <span class="n">wrapper</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="s2">&quot;Hello, world!&quot;</span><span class="p">)</span>
    <span class="n">stream</span> <span class="o">=</span> <span class="n">wrapper</span><span class="o">.</span><span class="n">detach</span><span class="p">()</span>
    <span class="n">stream</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="sa">b</span><span class="s2">&quot;!!!&quot;</span><span class="p">)</span>

<span class="k">with</span> <span class="n">io</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="s2">&quot;example.txt&quot;</span><span class="p">,</span> <span class="s2">&quot;r&quot;</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
    <span class="n">wrapper</span> <span class="o">=</span> <span class="n">io</span><span class="o">.</span><span class="n">TextIOWrapper</span><span class="p">(</span><span class="n">f</span><span class="p">,</span> <span class="n">encoding</span><span class="o">=</span><span class="s2">&quot;utf-8&quot;</span><span class="p">)</span>
    <span class="nb">print</span><span class="p">(</span><span class="n">wrapper</span><span class="o">.</span><span class="n">read</span><span class="p">())</span>  <span class="c1"># Hello, world!!!</span>
</pre></div></div></div>

<p>io.BufferedRandom() - буферизированный поток с произвольным доступом.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code107c73df6405b6272db61bd5328d2d0db" onclick="copyCode(code107c73df6405b6272db61bd5328d2d0d, code107c73df6405b6272db61bd5328d2d0db)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code107c73df6405b6272db61bd5328d2d0d"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">io</span>

<span class="k">with</span> <span class="n">io</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="s2">&quot;example.txt&quot;</span><span class="p">,</span> <span class="s2">&quot;wb&quot;</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
    <span class="n">writer</span> <span class="o">=</span> <span class="n">io</span><span class="o">.</span><span class="n">BufferedRandom</span><span class="p">(</span><span class="n">f</span><span class="p">)</span>
    <span class="n">writer</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="sa">b</span><span class="s2">&quot;Hello, world!&quot;</span><span class="p">)</span>
    <span class="n">writer</span><span class="o">.</span><span class="n">flush</span><span class="p">()</span>
    <span class="n">writer</span><span class="o">.</span><span class="n">seek</span><span class="p">(</span><span class="o">-</span><span class="mi">6</span><span class="p">,</span> <span class="n">io</span><span class="o">.</span><span class="n">SEEK_CUR</span><span class="p">)</span>
    <span class="n">writer</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="sa">b</span><span class="s2">&quot;Python!&quot;</span><span class="p">)</span>

<span class="k">with</span> <span class="n">io</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="s2">&quot;example.txt&quot;</span><span class="p">,</span> <span class="s2">&quot;rb&quot;</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
    <span class="n">reader</span> <span class="o">=</span> <span class="n">io</span><span class="o">.</span><span class="n">BufferedReader</span><span class="p">(</span><span class="n">f</span><span class="p">)</span>
    <span class="nb">print</span><span class="p">(</span><span class="n">reader</span><span class="o">.</span><span class="n">read</span><span class="p">())</span>  <span class="c1"># b&#39;Hello, Python!&#39;</span>
</pre></div></div></div>