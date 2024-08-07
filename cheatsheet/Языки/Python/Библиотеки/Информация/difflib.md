<h4>SequenceMatcher</h4>
<p>Сравнение двух последовательностей и определение степени их сходства.</p>
<div class="code-element">
    <div class="lang-line">
        <text>python</text>
        <button class="copy-button"
        onclick="copyCode(this)">
    <svg stroke="currentColor"
         fill="none"
         stroke-width="2"
         viewBox="0 0 24 24"
         stroke-linecap="round"
         stroke-linejoin="round"
         class="h-4 w-4"
         height="1em"
         width="1em"
         xmlns="http://www.w3.org/2000/svg">
        <path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path>
        <rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect>
    </svg>
    <text>Copy code</text>
</button>

    </div>
    <div class="code"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">difflib</span>

<span class="n">s1</span> <span class="o">=</span> <span class="s2">&quot;Hello, world!&quot;</span>
<span class="n">s2</span> <span class="o">=</span> <span class="s2">&quot;Hello, everyone!&quot;</span>

<span class="n">matcher</span> <span class="o">=</span> <span class="n">difflib</span><span class="o">.</span><span class="n">SequenceMatcher</span><span class="p">(</span><span class="kc">None</span><span class="p">,</span> <span class="n">s1</span><span class="p">,</span> <span class="n">s2</span><span class="p">)</span>
<span class="n">ratio</span> <span class="o">=</span> <span class="n">matcher</span><span class="o">.</span><span class="n">ratio</span><span class="p">()</span>

<span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;Similarity ratio: </span><span class="si">{</span><span class="n">ratio</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">)</span>

<span class="sd">&quot;&quot;&quot;Similarity ratio: 0.6206896551724138&quot;&quot;&quot;</span>
</pre></div></div>
</div>

<h4>get_close_matches</h4>
<p>Нахождение наиболее похожей строки в наборе строк на основе заданной строки.</p>
<div class="code-element">
    <div class="lang-line">
        <text>python</text>
        <button class="copy-button"
        onclick="copyCode(this)">
    <svg stroke="currentColor"
         fill="none"
         stroke-width="2"
         viewBox="0 0 24 24"
         stroke-linecap="round"
         stroke-linejoin="round"
         class="h-4 w-4"
         height="1em"
         width="1em"
         xmlns="http://www.w3.org/2000/svg">
        <path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path>
        <rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect>
    </svg>
    <text>Copy code</text>
</button>

    </div>
    <div class="code"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">difflib</span>

<span class="n">colors</span> <span class="o">=</span> <span class="p">[</span><span class="s2">&quot;red&quot;</span><span class="p">,</span> <span class="s2">&quot;green&quot;</span><span class="p">,</span> <span class="s2">&quot;blue&quot;</span><span class="p">,</span> <span class="s2">&quot;yellow&quot;</span><span class="p">]</span>
<span class="n">color</span> <span class="o">=</span> <span class="s2">&quot;grea&quot;</span>

<span class="n">matches</span> <span class="o">=</span> <span class="n">difflib</span><span class="o">.</span><span class="n">get_close_matches</span><span class="p">(</span><span class="n">color</span><span class="p">,</span> <span class="n">colors</span><span class="p">)</span>

<span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;Closest matches: </span><span class="si">{</span><span class="n">matches</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">)</span>

<span class="sd">&quot;&quot;&quot;Closest matches: [&quot;green&quot;]&quot;&quot;&quot;</span>
</pre></div></div>
</div>

<h4>unified_diff</h4>
<p>Генерация отчета о различиях между двумя последовательностями.</p>
<div class="code-element">
    <div class="lang-line">
        <text>python</text>
        <button class="copy-button"
        onclick="copyCode(this)">
    <svg stroke="currentColor"
         fill="none"
         stroke-width="2"
         viewBox="0 0 24 24"
         stroke-linecap="round"
         stroke-linejoin="round"
         class="h-4 w-4"
         height="1em"
         width="1em"
         xmlns="http://www.w3.org/2000/svg">
        <path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path>
        <rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect>
    </svg>
    <text>Copy code</text>
</button>

    </div>
    <div class="code"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">difflib</span>

<span class="n">text1</span> <span class="o">=</span> <span class="s2">&quot;&quot;&quot;Lorem ipsum dolor sit amet,</span>
<span class="s2">consectetur adipiscing elit,</span>
<span class="s2">sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.&quot;&quot;&quot;</span>

<span class="n">text2</span> <span class="o">=</span> <span class="s2">&quot;&quot;&quot;Lorem ipsum dolor sit amet,</span>
<span class="s2">consectetur adipiscing elit,</span>
<span class="s2">sed do eiusmod tempor incididunt ut labore et dolore magnus aliqua.&quot;&quot;&quot;</span>

<span class="n">d</span> <span class="o">=</span> <span class="n">difflib</span><span class="o">.</span><span class="n">unified_diff</span><span class="p">(</span><span class="n">text1</span><span class="o">.</span><span class="n">splitlines</span><span class="p">(),</span> <span class="n">text2</span><span class="o">.</span><span class="n">splitlines</span><span class="p">())</span>

<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;</span><span class="se">\n</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">d</span><span class="p">))</span>

<span class="sd">&quot;&quot;&quot;</span>
<span class="sd">---</span>

<span class="sd">+++</span>

<span class="sd">@@ -1,3 +1,3 @@</span>

<span class="sd"> Lorem ipsum dolor sit amet,</span>
<span class="sd"> consectetur adipiscing elit,</span>
<span class="sd">-sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</span>
<span class="sd">+sed do eiusmod tempor incididunt ut labore et dolore magnus aliqua.</span>
<span class="sd">&quot;&quot;&quot;</span>
</pre></div></div>
</div>

<h4>HtmlDiff</h4>
<p>Генерация отчета о различиях между двумя последовательностями в формате HTML.</p>
<div class="code-element">
    <div class="lang-line">
        <text>python</text>
        <button class="copy-button"
        onclick="copyCode(this)">
    <svg stroke="currentColor"
         fill="none"
         stroke-width="2"
         viewBox="0 0 24 24"
         stroke-linecap="round"
         stroke-linejoin="round"
         class="h-4 w-4"
         height="1em"
         width="1em"
         xmlns="http://www.w3.org/2000/svg">
        <path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path>
        <rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect>
    </svg>
    <text>Copy code</text>
</button>

    </div>
    <div class="code"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">difflib</span>

<span class="n">text1</span> <span class="o">=</span> <span class="s2">&quot;&quot;&quot;Lorem ipsum dolor sit amet,</span>
<span class="s2">consectetur adipiscing elit,</span>
<span class="s2">sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.&quot;&quot;&quot;</span>

<span class="n">text2</span> <span class="o">=</span> <span class="s2">&quot;&quot;&quot;Lorem ipsum dolor sit amet,</span>
<span class="s2">consectetur adipiscing elit,</span>
<span class="s2">sed do eiusmod tempor incididunt ut labore et dolore magnus aliqua.&quot;&quot;&quot;</span>

<span class="n">d</span> <span class="o">=</span> <span class="n">difflib</span><span class="o">.</span><span class="n">HtmlDiff</span><span class="p">()</span><span class="o">.</span><span class="n">make_file</span><span class="p">(</span><span class="n">text1</span><span class="o">.</span><span class="n">splitlines</span><span class="p">(),</span> <span class="n">text2</span><span class="o">.</span><span class="n">splitlines</span><span class="p">())</span>

<span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="s2">&quot;diff.html&quot;</span><span class="p">,</span> <span class="s2">&quot;w&quot;</span><span class="p">)</span> <span class="k">as</span> <span class="n">f</span><span class="p">:</span>
    <span class="n">f</span><span class="o">.</span><span class="n">writelines</span><span class="p">(</span><span class="n">d</span><span class="p">)</span>
</pre></div></div>
</div>

<h4>context_diff</h4>
<p>Генерация отчета о различиях между двумя последовательностями в формате context diff.</p>
<div class="code-element">
    <div class="lang-line">
        <text>python</text>
        <button class="copy-button"
        onclick="copyCode(this)">
    <svg stroke="currentColor"
         fill="none"
         stroke-width="2"
         viewBox="0 0 24 24"
         stroke-linecap="round"
         stroke-linejoin="round"
         class="h-4 w-4"
         height="1em"
         width="1em"
         xmlns="http://www.w3.org/2000/svg">
        <path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path>
        <rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect>
    </svg>
    <text>Copy code</text>
</button>

    </div>
    <div class="code"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">difflib</span>

<span class="n">text1</span> <span class="o">=</span> <span class="s2">&quot;&quot;&quot;Lorem ipsum dolor sit amet,</span>
<span class="s2">consectetur adipiscing elit,</span>
<span class="s2">sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.&quot;&quot;&quot;</span>

<span class="n">text2</span> <span class="o">=</span> <span class="s2">&quot;&quot;&quot;Lorem ipsum dolor sit amet,</span>
<span class="s2">consectetur adipiscing elit,</span>
<span class="s2">sed do eiusmod tempor incididunt ut labore et dolore magnus aliqua.&quot;&quot;&quot;</span>

<span class="n">d</span> <span class="o">=</span> <span class="n">difflib</span><span class="o">.</span><span class="n">context_diff</span><span class="p">(</span><span class="n">text1</span><span class="o">.</span><span class="n">splitlines</span><span class="p">(),</span> <span class="n">text2</span><span class="o">.</span><span class="n">splitlines</span><span class="p">())</span>

<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;</span><span class="se">\n</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">d</span><span class="p">))</span>

<span class="sd">&quot;&quot;&quot;</span>
<span class="sd">***</span>

<span class="sd">---</span>

<span class="sd">***************</span>

<span class="sd">*** 1,3 ****</span>

<span class="sd">  Lorem ipsum dolor sit amet,</span>
<span class="sd">  consectetur adipiscing elit,</span>
<span class="sd">! sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</span>
<span class="sd">--- 1,3 ----</span>

<span class="sd">  Lorem ipsum dolor sit amet,</span>
<span class="sd">  consectetur adipiscing elit,</span>
<span class="sd">! sed do eiusmod tempor incididunt ut labore et dolore magnus aliqua.</span>
<span class="sd">&quot;&quot;&quot;</span>
</pre></div></div>
</div>

<h4>ndiff</h4>
<p>Генерация отчета о различиях между двумя последовательностями в формате ndiff.</p>
<div class="code-element">
    <div class="lang-line">
        <text>python</text>
        <button class="copy-button"
        onclick="copyCode(this)">
    <svg stroke="currentColor"
         fill="none"
         stroke-width="2"
         viewBox="0 0 24 24"
         stroke-linecap="round"
         stroke-linejoin="round"
         class="h-4 w-4"
         height="1em"
         width="1em"
         xmlns="http://www.w3.org/2000/svg">
        <path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path>
        <rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect>
    </svg>
    <text>Copy code</text>
</button>

    </div>
    <div class="code"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">difflib</span>

<span class="n">text1</span> <span class="o">=</span> <span class="s2">&quot;&quot;&quot;Lorem ipsum dolor sit amet,</span>
<span class="s2">consectetur adipiscing elit,</span>
<span class="s2">sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.&quot;&quot;&quot;</span>

<span class="n">text2</span> <span class="o">=</span> <span class="s2">&quot;&quot;&quot;Lorem ipsum dolor sit amet,</span>
<span class="s2">consectetur adipiscing elit,</span>
<span class="s2">sed do eiusmod tempor incididunt ut labore et dolore magnus aliqua.&quot;&quot;&quot;</span>

<span class="n">d</span> <span class="o">=</span> <span class="n">difflib</span><span class="o">.</span><span class="n">ndiff</span><span class="p">(</span><span class="n">text1</span><span class="o">.</span><span class="n">splitlines</span><span class="p">(),</span> <span class="n">text2</span><span class="o">.</span><span class="n">splitlines</span><span class="p">())</span>

<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;</span><span class="se">\n</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">d</span><span class="p">))</span>

<span class="sd">&quot;&quot;&quot;</span>
<span class="sd">  Lorem ipsum dolor sit amet,</span>
<span class="sd">  consectetur adipiscing elit,</span>
<span class="sd">sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</span>
<span class="sd">?                                                          ^</span>

<span class="sd">+ sed do eiusmod tempor incididunt ut labore et dolore magnus aliqua.</span>
<span class="sd">?                                                          ^^       </span>
<span class="sd">&quot;&quot;&quot;</span>
</pre></div></div>
</div>

<h4>isjunk и ignore</h4>
<p>Использование пользовательских функций для игнорирования символов при сравнении последовательностей.</p>
<div class="code-element">
    <div class="lang-line">
        <text>python</text>
        <button class="copy-button"
        onclick="copyCode(this)">
    <svg stroke="currentColor"
         fill="none"
         stroke-width="2"
         viewBox="0 0 24 24"
         stroke-linecap="round"
         stroke-linejoin="round"
         class="h-4 w-4"
         height="1em"
         width="1em"
         xmlns="http://www.w3.org/2000/svg">
        <path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path>
        <rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect>
    </svg>
    <text>Copy code</text>
</button>

    </div>
    <div class="code"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">difflib</span>

<span class="k">def</span> <span class="nf">isjunk</span><span class="p">(</span><span class="n">s</span><span class="p">):</span>
    <span class="k">return</span> <span class="n">s</span> <span class="ow">in</span> <span class="p">[</span><span class="s2">&quot; &quot;</span><span class="p">,</span> <span class="s2">&quot;</span><span class="se">\n</span><span class="s2">&quot;</span><span class="p">]</span>

<span class="n">text1</span> <span class="o">=</span> <span class="s2">&quot;&quot;&quot;Lorem ipsum dolor sit amet,</span>
<span class="s2">consectetur adipiscing elit,</span>
<span class="s2">sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.&quot;&quot;&quot;</span>

<span class="n">text2</span> <span class="o">=</span> <span class="s2">&quot;&quot;&quot;Lorem ipsum dolor sit amet,</span>
<span class="s2">consectetur adipiscing elit,</span>
<span class="s2">sed do eiusmod tempor incididunt ut labore et dolore magnus aliqua.&quot;&quot;&quot;</span>

<span class="n">matcher</span> <span class="o">=</span> <span class="n">difflib</span><span class="o">.</span><span class="n">SequenceMatcher</span><span class="p">(</span><span class="n">isjunk</span><span class="p">,</span> <span class="n">text1</span><span class="p">,</span> <span class="n">text2</span><span class="p">)</span>
<span class="n">ratio</span> <span class="o">=</span> <span class="n">matcher</span><span class="o">.</span><span class="n">ratio</span><span class="p">()</span>

<span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;Similarity ratio: </span><span class="si">{</span><span class="n">ratio</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">)</span>

<span class="sd">&quot;&quot;&quot;Similarity ratio: 0.9878542510121457&quot;&quot;&quot;</span>
</pre></div></div>
</div>

<h4>reduce_func</h4>
<p>Использование пользовательской функции для преобразования различий в отчете о сравнении.</p>
<div class="code-element">
    <div class="lang-line">
        <text>python</text>
        <button class="copy-button"
        onclick="copyCode(this)">
    <svg stroke="currentColor"
         fill="none"
         stroke-width="2"
         viewBox="0 0 24 24"
         stroke-linecap="round"
         stroke-linejoin="round"
         class="h-4 w-4"
         height="1em"
         width="1em"
         xmlns="http://www.w3.org/2000/svg">
        <path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path>
        <rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect>
    </svg>
    <text>Copy code</text>
</button>

    </div>
    <div class="code"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">difflib</span>

<span class="n">text1</span> <span class="o">=</span> <span class="s2">&quot;&quot;&quot;Lorem ipsum dolor sit amet,</span>
<span class="s2">consectetur adipiscing elit,</span>
<span class="s2">sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.&quot;&quot;&quot;</span>

<span class="n">text2</span> <span class="o">=</span> <span class="s2">&quot;&quot;&quot;Lorem ipsum dolor sit amet,</span>
<span class="s2">consectetur adipiscing elit,</span>
<span class="s2">sed do eiusmod tempor incididunt ut labore et dolore magnus aliqua.&quot;&quot;&quot;</span>

<span class="n">d</span> <span class="o">=</span> <span class="n">difflib</span><span class="o">.</span><span class="n">Differ</span><span class="p">()</span>
<span class="n">diff</span> <span class="o">=</span> <span class="n">d</span><span class="o">.</span><span class="n">compare</span><span class="p">(</span><span class="n">text1</span><span class="o">.</span><span class="n">splitlines</span><span class="p">(),</span> <span class="n">text2</span><span class="o">.</span><span class="n">splitlines</span><span class="p">())</span>

<span class="k">def</span> <span class="nf">reduce_func</span><span class="p">(</span><span class="n">s</span><span class="p">):</span>
    <span class="k">if</span> <span class="n">s</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="s2">&quot;- &quot;</span><span class="p">):</span>
        <span class="k">return</span> <span class="sa">f</span><span class="s2">&quot;&lt;span style=&quot;</span><span class="n">color</span><span class="p">:</span><span class="n">red</span><span class="s2">&quot;&gt;</span><span class="si">{s}</span><span class="s2">&lt;/span&gt;&quot;</span>
    <span class="k">elif</span> <span class="n">s</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="s2">&quot;+ &quot;</span><span class="p">):</span>
        <span class="k">return</span> <span class="sa">f</span><span class="s2">&quot;&lt;span style=&quot;</span><span class="n">color</span><span class="p">:</span><span class="n">green</span><span class="s2">&quot;&gt;</span><span class="si">{s}</span><span class="s2">&lt;/span&gt;&quot;</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="k">return</span> <span class="n">s</span>

<span class="n">diff</span> <span class="o">=</span> <span class="nb">map</span><span class="p">(</span><span class="n">reduce_func</span><span class="p">,</span> <span class="n">diff</span><span class="p">)</span>
<span class="n">diff</span> <span class="o">=</span> <span class="s2">&quot;</span><span class="se">\n</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">diff</span><span class="p">)</span>

<span class="nb">print</span><span class="p">(</span><span class="n">diff</span><span class="p">)</span>

<span class="sd">&quot;&quot;&quot;</span>
<span class="sd">  Lorem ipsum dolor sit amet,</span>
<span class="sd">  consectetur adipiscing elit,</span>
<span class="sd">&lt;span style=&quot;color:red&quot;&gt;- sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.&lt;/span&gt;</span>
<span class="sd">?                                                          ^</span>

<span class="sd">&lt;span style=&quot;color:green&quot;&gt;+ sed do eiusmod tempor incididunt ut labore et dolore magnus aliqua.&lt;/span&gt;</span>
<span class="sd">?                                                          ^^                                         </span>
<span class="sd">&quot;&quot;&quot;</span>
</pre></div></div>
</div>