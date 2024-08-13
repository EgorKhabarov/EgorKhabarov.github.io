<p><a href="https://github.com/EgorKhabarov/table2string">https://github.com/EgorKhabarov/table2string</a></p>
<h1>table2string</h1>
<p><a href="https://github.com/EgorKhabarov/table2string/actions/workflows/tests.yml"><img alt="GitHub Actions Workflow Status" src="https://img.shields.io/github/actions/workflow/status/EgorKhabarov/table2string/tests.yml?style=flat&amp;logo=GitHub&amp;label=Tests" /></a> <a href="https://github.com/EgorKhabarov/table2string/actions/workflows/publish.yml"><img alt="Publish Python Package to PyPI" src="https://img.shields.io/github/actions/workflow/status/EgorKhabarov/table2string/publish.yml?style=flat&amp;logo=GitHub&amp;label=Publish%20to%20PyPI" /></a></p>
<p><a href="https://pypi.python.org/pypi/table2string"><img alt="PyPi Package Version" src="https://img.shields.io/pypi/v/table2string.svg?style=flat&amp;logo=pypi" /></a> <a href="https://pypi.python.org/pypi/table2string"><img alt="Supported Python versions" src="https://img.shields.io/pypi/pyversions/table2string.svg?style=flat&amp;logo=pypi" /></a> <a href="https://pypi.python.org/pypi/table2string"><img alt="PyPi status" src="https://img.shields.io/pypi/status/table2string.svg?style=flat&amp;logo=pypi" /></a> <a href="https://pypi.org/project/table2string/"><img alt="PyPi downloads" src="https://img.shields.io/pypi/dm/table2string.svg?style=flat&amp;logo=pypi" /></a></p>
<h2>Convert table to string</h2>
<p>While there are several libraries available for converting tables to strings in Python, none seemed to meet my specific requirements. </p>
<ul>
<li><strong>Line Break Support:</strong> Easily include line breaks within cells for enhanced readability.</li>
<li><strong>Emoji Integration:</strong> Effortlessly incorporate emoji characters into your tables to add visual appeal and context.</li>
</ul>
<hr />
<h1>Install</h1>
<h2>PyPI</h2>
<div class="code-element">
    <div class="lang-line">
        <text>shell</text>
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
    <div class="code"><div class="highlight"><pre><span></span>pip<span class="w"> </span>install<span class="w"> </span>-U<span class="w"> </span>table2string
</pre></div></div>
</div>

<h2>GitHub</h2>
<div class="code-element">
    <div class="lang-line">
        <text>shell</text>
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
    <div class="code"><div class="highlight"><pre><span></span>pip<span class="w"> </span>install<span class="w"> </span>-U<span class="w"> </span>git+https://github.com/EgorKhabarov/table2string.git@master
</pre></div></div>
</div>

<hr />
<h1>Usage example</h1>
<div class="code-element">
    <div class="lang-line">
        <text>pycon</text>
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
    <div class="code"><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="kn">from</span> <span class="nn">table2string</span> <span class="kn">import</span> <span class="n">Table</span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="n">Table</span><span class="p">([(</span><span class="s2">&quot;1&quot;</span><span class="p">,</span> <span class="s2">&quot;2&quot;</span><span class="p">,</span> <span class="s2">&quot;3&quot;</span><span class="p">),</span> <span class="p">(</span><span class="s2">&quot;qwe&quot;</span><span class="p">,</span> <span class="s2">&quot;rty</span><span class="se">\n</span><span class="s2">uio&quot;</span><span class="p">,</span> <span class="s2">&quot;&quot;</span><span class="p">)],</span> <span class="n">name</span><span class="o">=</span><span class="s2">&quot;Table Name&quot;</span><span class="p">)</span><span class="o">.</span><span class="n">print</span><span class="p">()</span>
<span class="unselectable"><span class="go">+---------------+</span>
<span class="go">|  Table Name   |</span>
<span class="go">+-----+-----+---+</span>
<span class="go">|   1 |   2 | 3 |</span>
<span class="go">+-----+-----+---+</span>
<span class="go">| qwe | rty |   |</span>
<span class="go">|     | uio |   |</span>
<span class="go">+-----+-----+---+</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="kn">from</span> <span class="nn">io</span> <span class="kn">import</span> <span class="n">StringIO</span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="n">Table</span><span class="o">.</span><span class="n">from_csv</span><span class="p">(</span><span class="n">StringIO</span><span class="p">(</span><span class="s1">&#39;c1,c2,c3</span><span class="se">\n</span><span class="s1">1,2,3</span><span class="se">\n</span><span class="s1">qwe,&quot;rty</span><span class="se">\n</span><span class="s1">uio&quot;,&#39;</span><span class="p">),</span> <span class="n">name</span><span class="o">=</span><span class="s2">&quot;Table Name&quot;</span><span class="p">)</span><span class="o">.</span><span class="n">print</span><span class="p">()</span>
<span class="unselectable"><span class="go">+----------------+</span>
<span class="go">|   Table Name   |</span>
<span class="go">+-----+-----+----+</span>
<span class="go">| c1  | c2  | c3 |</span>
<span class="go">+-----+-----+----+</span>
<span class="go">|   1 |   2 |  3 |</span>
<span class="go">+-----+-----+----+</span>
<span class="go">| qwe | rty |    |</span>
<span class="go">|     | uio |    |</span>
<span class="go">+-----+-----+----+</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="n">Table</span><span class="o">.</span><span class="n">from_csv</span><span class="p">(</span><span class="n">StringIO</span><span class="p">(</span><span class="s1">&#39;c1,c2,c3</span><span class="se">\n</span><span class="s1">1,2,3</span><span class="se">\n</span><span class="s1">qwe,&quot;rty</span><span class="se">\n</span><span class="s1">uio&quot;,&#39;</span><span class="p">),</span> <span class="n">name</span><span class="o">=</span><span class="s2">&quot;Table Name&quot;</span><span class="p">,</span> <span class="n">column_names</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span><span class="o">.</span><span class="n">print</span><span class="p">()</span>
<span class="unselectable"><span class="go">+---------------+</span>
<span class="go">|  Table Name   |</span>
<span class="go">+-----+-----+---+</span>
<span class="go">|   1 |   2 | 3 |</span>
<span class="go">+-----+-----+---+</span>
<span class="go">| qwe | rty |   |</span>
<span class="go">|     | uio |   |</span>
<span class="go">+-----+-----+---+</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="kn">import</span> <span class="nn">sqlite3</span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="n">cursor</span> <span class="o">=</span> <span class="n">sqlite3</span><span class="o">.</span><span class="n">connect</span><span class="p">(</span><span class="s2">&quot;:memory:&quot;</span><span class="p">)</span><span class="o">.</span><span class="n">cursor</span><span class="p">()</span><span class="o">.</span><span class="n">execute</span><span class="p">(</span>
<span class="unselectable"><span class="o">...</span> </span>    <span class="s2">&quot;CREATE TABLE data (c1 TEXT, c2 TEXT, c3 TEXT);&quot;</span>
<span class="unselectable"><span class="o">...</span> </span><span class="p">)</span><span class="o">.</span><span class="n">executemany</span><span class="p">(</span>
<span class="unselectable"><span class="o">...</span> </span>    <span class="s2">&quot;INSERT INTO data (c1, c2, c3) VALUES (?, ?, ?);&quot;</span><span class="p">,</span>
<span class="unselectable"><span class="o">...</span> </span>    <span class="p">[(</span><span class="s2">&quot;1&quot;</span><span class="p">,</span> <span class="s2">&quot;2&quot;</span><span class="p">,</span> <span class="s2">&quot;3&quot;</span><span class="p">),</span> <span class="p">(</span><span class="s2">&quot;qwe&quot;</span><span class="p">,</span> <span class="s2">&quot;rty</span><span class="se">\n</span><span class="s2">uio&quot;</span><span class="p">,</span> <span class="s2">&quot;&quot;</span><span class="p">)],</span>
<span class="unselectable"><span class="o">...</span> </span><span class="p">)</span><span class="o">.</span><span class="n">execute</span><span class="p">(</span>
<span class="unselectable"><span class="o">...</span> </span>    <span class="s2">&quot;SELECT c1, c2, c3 FROM data;&quot;</span>
<span class="unselectable"><span class="o">...</span> </span><span class="p">)</span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="n">Table</span><span class="o">.</span><span class="n">from_db_cursor</span><span class="p">(</span><span class="n">cursor</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="s2">&quot;Table Name&quot;</span><span class="p">)</span><span class="o">.</span><span class="n">print</span><span class="p">()</span>
<span class="unselectable"><span class="go">+---------------+</span>
<span class="go">|  Table Name   |</span>
<span class="go">+-----+-----+---+</span>
<span class="go">|   1 |   2 | 3 |</span>
<span class="go">+-----+-----+---+</span>
<span class="go">| qwe | rty |   |</span>
<span class="go">|     | uio |   |</span>
<span class="go">+-----+-----+---+</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="n">Table</span><span class="o">.</span><span class="n">from_db_cursor</span><span class="p">(</span>
<span class="unselectable"><span class="o">...</span> </span>    <span class="n">cursor</span><span class="o">.</span><span class="n">execute</span><span class="p">(</span><span class="s2">&quot;SELECT c1, c2, c3 FROM data;&quot;</span><span class="p">),</span>
<span class="unselectable"><span class="o">...</span> </span>    <span class="n">name</span><span class="o">=</span><span class="s2">&quot;Table Name&quot;</span><span class="p">,</span>
<span class="unselectable"><span class="o">...</span> </span>    <span class="n">column_names</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
<span class="unselectable"><span class="o">...</span> </span><span class="p">)</span><span class="o">.</span><span class="n">print</span><span class="p">()</span>
<span class="unselectable"><span class="go">+----------------+</span>
<span class="go">|   Table Name   |</span>
<span class="go">+-----+-----+----+</span>
<span class="go">| c1  | c2  | c3 |</span>
<span class="go">+-----+-----+----+</span>
<span class="go">|   1 |   2 |  3 |</span>
<span class="go">+-----+-----+----+</span>
<span class="go">| qwe | rty |    |</span>
<span class="go">|     | uio |    |</span>
<span class="go">+-----+-----+----+</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="kn">from</span> <span class="nn">table2string</span> <span class="kn">import</span> <span class="n">print_table</span><span class="p">,</span> <span class="n">stringify_table</span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="n">print_table</span><span class="p">([(</span><span class="s2">&quot;1&quot;</span><span class="p">,</span> <span class="s2">&quot;2&quot;</span><span class="p">,</span> <span class="s2">&quot;3&quot;</span><span class="p">),</span> <span class="p">(</span><span class="s2">&quot;qwe&quot;</span><span class="p">,</span> <span class="s2">&quot;rty</span><span class="se">\n</span><span class="s2">uio&quot;</span><span class="p">,</span> <span class="s2">&quot;&quot;</span><span class="p">)],</span> <span class="n">name</span><span class="o">=</span><span class="s2">&quot;Table Name&quot;</span><span class="p">)</span>
<span class="unselectable"><span class="go">+---------------+</span>
<span class="go">|  Table Name   |</span>
<span class="go">+-----+-----+---+</span>
<span class="go">|   1 |   2 | 3 |</span>
<span class="go">+-----+-----+---+</span>
<span class="go">| qwe | rty |   |</span>
<span class="go">|     | uio |   |</span>
<span class="go">+-----+-----+---+</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="nb">print</span><span class="p">(</span><span class="n">stringify_table</span><span class="p">([(</span><span class="s2">&quot;1&quot;</span><span class="p">,</span> <span class="s2">&quot;2&quot;</span><span class="p">,</span> <span class="s2">&quot;3&quot;</span><span class="p">),</span> <span class="p">(</span><span class="s2">&quot;qwe&quot;</span><span class="p">,</span> <span class="s2">&quot;rty</span><span class="se">\n</span><span class="s2">uio&quot;</span><span class="p">,</span> <span class="s2">&quot;&quot;</span><span class="p">)],</span> <span class="n">name</span><span class="o">=</span><span class="s2">&quot;Table Name&quot;</span><span class="p">))</span>
<span class="unselectable"><span class="go">+---------------+</span>
<span class="go">|  Table Name   |</span>
<span class="go">+-----+-----+---+</span>
<span class="go">|   1 |   2 | 3 |</span>
<span class="go">+-----+-----+---+</span>
<span class="go">| qwe | rty |   |</span>
<span class="go">|     | uio |   |</span>
<span class="go">+-----+-----+---+</span>
</span></pre></div></div>
</div>

<h2>Custom width and height settings</h2>
<table>
<thead>
<tr>
<th>Width</th>
<th>Example</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>&lt;width&gt;</code></td>
<td><code>10</code></td>
<td>Setting <code>width</code> (<code>10</code>) for the whole table</td>
</tr>
<tr>
<td><code>(&lt;width&gt;,)</code></td>
<td><code>(10,)</code></td>
<td>Setting <code>width_1</code> (<code>10</code>) for all column</td>
</tr>
<tr>
<td><code>(&lt;width_1&gt;, &lt;width_2&gt;)</code></td>
<td><code>(10, 20)</code></td>
<td>Setting <code>width_1</code> (<code>10</code>) for the first column and <code>width_2</code> (<code>20</code>)<br>for all other columns</td>
</tr>
<tr>
<td><code>(&lt;width_1&gt;, &lt;width_2&gt;, &lt;width_3&gt;)</code></td>
<td><code>(10, 20, 30)</code></td>
<td>Setting <code>width_1</code> (<code>10</code>) for the first column and <code>width_2</code> (<code>20</code>)<br>for the second and <code>width_3</code> (<code>30</code>) for the third column</td>
</tr>
</tbody>
</table>
<details>
<summary>Example</summary>

<div class="code-element">
    <div class="lang-line">
        <text>pycon</text>
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
    <div class="code"><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="c1"># Width of the entire table with borders</span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="n">print_table</span><span class="p">([(</span><span class="mi">1</span><span class="p">,),</span> <span class="p">(</span><span class="mf">2.345</span><span class="p">,),</span> <span class="p">(</span><span class="s2">&quot;example&quot;</span><span class="p">,)],</span> <span class="n">max_width</span><span class="o">=</span><span class="mi">10</span><span class="p">)</span>
<span class="unselectable"><span class="go">+--------+</span>
<span class="go">|      1 |</span>
<span class="go">+--------+</span>
<span class="go">|  2.345 |</span>
<span class="go">+--------+</span>
<span class="go">| exampl↩|</span>
<span class="go">| e      |</span>
<span class="go">+--------+</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="c1"># Width of each column individually</span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="n">print_table</span><span class="p">([(</span><span class="mi">1</span><span class="p">,),</span> <span class="p">(</span><span class="mf">2.345</span><span class="p">,),</span> <span class="p">(</span><span class="s2">&quot;example&quot;</span><span class="p">,)],</span> <span class="n">max_width</span><span class="o">=</span><span class="p">(</span><span class="mi">10</span><span class="p">,))</span>
<span class="unselectable"><span class="go">+------------+</span>
<span class="go">|          1 |</span>
<span class="go">+------------+</span>
<span class="go">|      2.345 |</span>
<span class="go">+------------+</span>
<span class="go">| example    |</span>
<span class="go">+------------+</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="n">print_table</span><span class="p">([(</span><span class="s2">&quot;123456</span><span class="se">\n\n</span><span class="s2">789000&quot;</span><span class="p">,</span> <span class="s2">&quot;example&quot;</span><span class="p">)],</span> <span class="n">max_width</span><span class="o">=</span><span class="p">(</span><span class="mi">3</span><span class="p">,</span> <span class="mi">4</span><span class="p">),</span> <span class="n">max_height</span><span class="o">=</span><span class="mi">4</span><span class="p">)</span>
<span class="unselectable"><span class="go">+-----+------+</span>
<span class="go">| 123↩| exam↩|</span>
<span class="go">| 456 | ple  |</span>
<span class="go">|     |      |</span>
<span class="go">| 789…|      |</span>
<span class="go">+-----+------+</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="n">print_table</span><span class="p">([(</span><span class="s2">&quot;123456789&quot;</span><span class="p">,)],</span> <span class="n">max_width</span><span class="o">=</span><span class="p">(</span><span class="mi">1</span><span class="p">,),</span> <span class="n">max_height</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>
<span class="unselectable"><span class="go">+---+</span>
<span class="go">| 1…|</span>
<span class="go">+---+</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="n">print_table</span><span class="p">(</span>
<span class="unselectable"><span class="o">...</span> </span>    <span class="n">table</span><span class="o">=</span><span class="p">[(</span><span class="s2">&quot;123</span><span class="se">\n</span><span class="s2">456</span><span class="se">\n</span><span class="s2">789&quot;</span><span class="p">,)],</span>
<span class="unselectable"><span class="o">...</span> </span>    <span class="n">max_width</span><span class="o">=</span><span class="p">(</span><span class="mi">3</span><span class="p">,),</span>
<span class="unselectable"><span class="o">...</span> </span>    <span class="n">max_height</span><span class="o">=</span><span class="mi">4</span><span class="p">,</span>
<span class="unselectable"><span class="o">...</span> </span>    <span class="n">maximize_height</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
<span class="unselectable"><span class="o">...</span> </span><span class="p">)</span>
<span class="unselectable"><span class="go">+-----+</span>
<span class="go">| 123 |</span>
<span class="go">| 456 |</span>
<span class="go">| 789 |</span>
<span class="go">|     |</span>
<span class="go">+-----+</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="n">print_table</span><span class="p">(</span>
<span class="unselectable"><span class="o">...</span> </span>    <span class="n">table</span><span class="o">=</span><span class="p">[(</span><span class="s2">&quot;123456789&quot;</span><span class="p">,)],</span>
<span class="unselectable"><span class="o">...</span> </span>    <span class="n">max_width</span><span class="o">=</span><span class="p">(</span><span class="mi">3</span><span class="p">,),</span>
<span class="unselectable"><span class="o">...</span> </span>    <span class="n">max_height</span><span class="o">=</span><span class="mi">4</span><span class="p">,</span>
<span class="unselectable"><span class="o">...</span> </span>    <span class="n">maximize_height</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
<span class="unselectable"><span class="o">...</span> </span><span class="p">)</span>
<span class="unselectable"><span class="go">+-----+</span>
<span class="go">| 123↩|</span>
<span class="go">| 456↩|</span>
<span class="go">| 789 |</span>
<span class="go">|     |</span>
<span class="go">+-----+</span>
</span></pre></div></div>
</div>
</details>

<h2>Text alignment</h2>
<table>
<thead>
<tr>
<th>Align</th>
<th>Example</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>"&lt;align&gt;"</code> or <code>("&lt;align&gt;",)</code></td>
<td><code>"^"</code> or <code>("^",)</code></td>
<td>Setting <code>align</code> (<code>"^"</code>) for all columns</td>
</tr>
<tr>
<td><code>("&lt;align_1&gt;", "&lt;align_2&gt;")</code></td>
<td><code>("^", "&lt;")</code></td>
<td>Setting <code>align_1</code> (<code>"^"</code>) for the first column and <code>align_2</code> (<code>"&lt;"</code>)<br>for all other columns</td>
</tr>
<tr>
<td><code>("&lt;align_1&gt;", "&lt;align_2&gt;", "&lt;align_3&gt;")</code></td>
<td><code>("^", "&lt;", "&gt;")</code></td>
<td>Setting <code>align_1</code> (<code>"^"</code>) for the first column and <code>align_2</code> (<code>"&lt;"</code>)<br>for the second and <code>align_3</code> (<code>"&gt;"</code>) for the third column</td>
</tr>
</tbody>
</table>
<h3>ALLOWED_ALIGNS</h3>
<table>
<thead>
<tr>
<th style="text-align: center;">Align</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><code>*</code> or <code>**</code></td>
<td>Alignment depends on the type. If this is a number and there are no line breaks in this cell,<br>then align to the right; otherwise, align to the left.</td>
</tr>
<tr>
<td style="text-align: center;"><code>&lt;</code> or <code>&lt;&lt;</code></td>
<td>All lines are left aligned</td>
</tr>
<tr>
<td style="text-align: center;"><code>^</code> or <code>^^</code></td>
<td>All lines are center aligned</td>
</tr>
<tr>
<td style="text-align: center;"><code>&gt;</code> or <code>&gt;&gt;</code></td>
<td>All lines are right aligned</td>
</tr>
<tr>
<td style="text-align: center;"><code>&lt;^</code></td>
<td>The first line is left aligned and the remaining lines are centered</td>
</tr>
<tr>
<td style="text-align: center;"><code>&lt;&gt;</code></td>
<td>The first line is left aligned and the remaining lines are right aligned</td>
</tr>
<tr>
<td style="text-align: center;"><code>^&lt;</code></td>
<td>The first line is aligned to the center, and the remaining lines are aligned to the left of the first line.</td>
</tr>
<tr>
<td style="text-align: center;"><code>^&gt;</code></td>
<td>The first line is aligned to the center, and the remaining lines are aligned to the right of the first line.</td>
</tr>
<tr>
<td style="text-align: center;"><code>&gt;&lt;</code></td>
<td>The first line is right aligned and the remaining lines are left aligned</td>
</tr>
<tr>
<td style="text-align: center;"><code>&gt;^</code></td>
<td>The first line is right aligned and the remaining lines are centered</td>
</tr>
</tbody>
</table>
<details>
<summary>Example</summary>

<div class="code-element">
    <div class="lang-line">
        <text>pycon</text>
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
    <div class="code"><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="n">kwargs_1</span> <span class="o">=</span> <span class="p">{</span>
<span class="unselectable"><span class="o">...</span> </span>    <span class="s2">&quot;table&quot;</span><span class="p">:</span> <span class="p">[(</span><span class="s2">&quot;1&quot;</span><span class="p">,</span> <span class="s2">&quot;123456789</span><span class="se">\n</span><span class="s2">qwerty</span><span class="se">\n</span><span class="s2">asdfghjklzxcvb&quot;</span><span class="p">)],</span>
<span class="unselectable"><span class="o">...</span> </span>    <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;Table Name</span><span class="se">\n</span><span class="s2">Name</span><span class="se">\n</span><span class="s2">Naaaaame&quot;</span><span class="p">,</span>
<span class="unselectable"><span class="o">...</span> </span>    <span class="s2">&quot;column_names&quot;</span><span class="p">:</span> <span class="p">(</span><span class="s2">&quot;1&quot;</span><span class="p">,</span> <span class="s2">&quot;col 2</span><span class="se">\n</span><span class="s2">c2&quot;</span><span class="p">),</span>
<span class="unselectable"><span class="o">...</span> </span>    <span class="s2">&quot;max_width&quot;</span><span class="p">:</span> <span class="p">(</span><span class="mi">5</span><span class="p">,</span> <span class="mi">15</span><span class="p">),</span>
<span class="unselectable"><span class="o">...</span> </span><span class="p">}</span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="n">print_table</span><span class="p">(</span><span class="o">**</span><span class="n">kwargs_1</span><span class="p">)</span>
<span class="unselectable"><span class="go">+-------------------------+</span>
<span class="go">|       Table Name        |</span>
<span class="go">|          Name           |</span>
<span class="go">|        Naaaaame         |</span>
<span class="go">+-------+-----------------+</span>
<span class="go">|   1   |      col 2      |</span>
<span class="go">|       |       c2        |</span>
<span class="go">+-------+-----------------+</span>
<span class="go">|     1 | 123456789       |</span>
<span class="go">|       | qwerty          |</span>
<span class="go">|       | asdfghjklzxcvb  |</span>
<span class="go">+-------+-----------------+</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="n">print_table</span><span class="p">(</span><span class="o">**</span><span class="n">kwargs_1</span><span class="p">,</span> <span class="n">align</span><span class="o">=</span><span class="s2">&quot;*&quot;</span><span class="p">,</span> <span class="n">name_align</span><span class="o">=</span><span class="s2">&quot;*&quot;</span><span class="p">,</span> <span class="n">column_names_align</span><span class="o">=</span><span class="s2">&quot;*&quot;</span><span class="p">)</span>  <span class="c1"># align=&quot;**&quot;, name_align=&quot;**&quot;, column_names_align=&quot;**&quot;</span>
<span class="unselectable"><span class="go">+-------------------------+</span>
<span class="go">| Table Name              |</span>
<span class="go">| Name                    |</span>
<span class="go">| Naaaaame                |</span>
<span class="go">+-------+-----------------+</span>
<span class="go">|     1 | col 2           |</span>
<span class="go">|       | c2              |</span>
<span class="go">+-------+-----------------+</span>
<span class="go">|     1 | 123456789       |</span>
<span class="go">|       | qwerty          |</span>
<span class="go">|       | asdfghjklzxcvb  |</span>
<span class="go">+-------+-----------------+</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="n">print_table</span><span class="p">(</span><span class="o">**</span><span class="n">kwargs_1</span><span class="p">,</span> <span class="n">align</span><span class="o">=</span><span class="s2">&quot;&lt;&quot;</span><span class="p">,</span> <span class="n">name_align</span><span class="o">=</span><span class="s2">&quot;&lt;&quot;</span><span class="p">,</span> <span class="n">column_names_align</span><span class="o">=</span><span class="s2">&quot;&lt;&quot;</span><span class="p">)</span>  <span class="c1"># align=&quot;&lt;&lt;&quot;, name_align=&quot;&lt;&lt;&quot;, column_names_align=&quot;&lt;&lt;&quot;</span>
<span class="unselectable"><span class="go">+-------------------------+</span>
<span class="go">| Table Name              |</span>
<span class="go">| Name                    |</span>
<span class="go">| Naaaaame                |</span>
<span class="go">+-------+-----------------+</span>
<span class="go">| 1     | col 2           |</span>
<span class="go">|       | c2              |</span>
<span class="go">+-------+-----------------+</span>
<span class="go">| 1     | 123456789       |</span>
<span class="go">|       | qwerty          |</span>
<span class="go">|       | asdfghjklzxcvb  |</span>
<span class="go">+-------+-----------------+</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="n">print_table</span><span class="p">(</span><span class="o">**</span><span class="n">kwargs_1</span><span class="p">,</span> <span class="n">align</span><span class="o">=</span><span class="s2">&quot;&gt;&quot;</span><span class="p">,</span> <span class="n">name_align</span><span class="o">=</span><span class="s2">&quot;&gt;&quot;</span><span class="p">,</span> <span class="n">column_names_align</span><span class="o">=</span><span class="s2">&quot;&gt;&quot;</span><span class="p">)</span>  <span class="c1"># align=&quot;&gt;&gt;&quot;, name_align=&quot;&gt;&gt;&quot;, column_names_align=&quot;&gt;&gt;&quot;</span>
<span class="unselectable"><span class="go">+-------------------------+</span>
<span class="go">|              Table Name |</span>
<span class="go">|                    Name |</span>
<span class="go">|                Naaaaame |</span>
<span class="go">+-------+-----------------+</span>
<span class="go">|     1 |           col 2 |</span>
<span class="go">|       |              c2 |</span>
<span class="go">+-------+-----------------+</span>
<span class="go">|     1 |       123456789 |</span>
<span class="go">|       |          qwerty |</span>
<span class="go">|       |  asdfghjklzxcvb |</span>
<span class="go">+-------+-----------------+</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="n">print_table</span><span class="p">(</span><span class="o">**</span><span class="n">kwargs_1</span><span class="p">,</span> <span class="n">align</span><span class="o">=</span><span class="s2">&quot;^&quot;</span><span class="p">,</span> <span class="n">name_align</span><span class="o">=</span><span class="s2">&quot;^&quot;</span><span class="p">,</span> <span class="n">column_names_align</span><span class="o">=</span><span class="s2">&quot;^&quot;</span><span class="p">)</span>  <span class="c1"># align=&quot;^^&quot;, name_align=&quot;^^&quot;, column_names_align=&quot;^^&quot;</span>
<span class="unselectable"><span class="go">+-------------------------+</span>
<span class="go">|       Table Name        |</span>
<span class="go">|          Name           |</span>
<span class="go">|        Naaaaame         |</span>
<span class="go">+-------+-----------------+</span>
<span class="go">|   1   |      col 2      |</span>
<span class="go">|       |       c2        |</span>
<span class="go">+-------+-----------------+</span>
<span class="go">|   1   |    123456789    |</span>
<span class="go">|       |     qwerty      |</span>
<span class="go">|       | asdfghjklzxcvb  |</span>
<span class="go">+-------+-----------------+</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="n">print_table</span><span class="p">(</span><span class="o">**</span><span class="n">kwargs_1</span><span class="p">,</span> <span class="n">align</span><span class="o">=</span><span class="s2">&quot;^&lt;&quot;</span><span class="p">,</span> <span class="n">name_align</span><span class="o">=</span><span class="s2">&quot;^&lt;&quot;</span><span class="p">,</span> <span class="n">column_names_align</span><span class="o">=</span><span class="s2">&quot;^&lt;&quot;</span><span class="p">)</span>
<span class="unselectable"><span class="go">+-------------------------+</span>
<span class="go">|       Table Name        |</span>
<span class="go">|       Name              |</span>
<span class="go">|       Naaaaame          |</span>
<span class="go">+-------+-----------------+</span>
<span class="go">|   1   |      col 2      |</span>
<span class="go">|       |      c2         |</span>
<span class="go">+-------+-----------------+</span>
<span class="go">|   1   | 123456789       |</span>
<span class="go">|       | qwerty          |</span>
<span class="go">|       | asdfghjklzxcvb  |</span>
<span class="go">+-------+-----------------+</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="n">print_table</span><span class="p">(</span><span class="o">**</span><span class="n">kwargs_1</span><span class="p">,</span> <span class="n">align</span><span class="o">=</span><span class="s2">&quot;^&gt;&quot;</span><span class="p">,</span> <span class="n">name_align</span><span class="o">=</span><span class="s2">&quot;^&gt;&quot;</span><span class="p">,</span> <span class="n">column_names_align</span><span class="o">=</span><span class="s2">&quot;^&gt;&quot;</span><span class="p">)</span>
<span class="unselectable"><span class="go">+-------------------------+</span>
<span class="go">|       Table Name        |</span>
<span class="go">|             Name        |</span>
<span class="go">|         Naaaaame        |</span>
<span class="go">+-------+-----------------+</span>
<span class="go">|   1   |      col 2      |</span>
<span class="go">|       |         c2      |</span>
<span class="go">+-------+-----------------+</span>
<span class="go">|   1   |      123456789  |</span>
<span class="go">|       |         qwerty  |</span>
<span class="go">|       | asdfghjklzxcvb  |</span>
<span class="go">+-------+-----------------+</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="n">print_table</span><span class="p">([(</span><span class="s2">&quot;qwerty</span><span class="se">\n</span><span class="s2">123456789</span><span class="se">\n</span><span class="s2">asdfghjklzxcvb&quot;</span><span class="p">,)],</span> <span class="n">max_width</span><span class="o">=</span><span class="p">(</span><span class="mi">18</span><span class="p">,),</span> <span class="n">align</span><span class="o">=</span><span class="s2">&quot;^&lt;&quot;</span><span class="p">)</span>
<span class="unselectable"><span class="go">+--------------------+</span>
<span class="go">|   qwerty           |</span>
<span class="go">|   123456789        |</span>
<span class="go">|   asdfghjklzxcvb   |</span>
<span class="go">+--------------------+</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="n">print_table</span><span class="p">([(</span><span class="s2">&quot;qwerty</span><span class="se">\n</span><span class="s2">123456789</span><span class="se">\n</span><span class="s2">asdfghjklzxcvb&quot;</span><span class="p">,)],</span> <span class="n">max_width</span><span class="o">=</span><span class="p">(</span><span class="mi">18</span><span class="p">,),</span> <span class="n">align</span><span class="o">=</span><span class="s2">&quot;^&gt;&quot;</span><span class="p">)</span>
<span class="unselectable"><span class="go">+--------------------+</span>
<span class="go">|           qwerty   |</span>
<span class="go">|        123456789   |</span>
<span class="go">|   asdfghjklzxcvb   |</span>
<span class="go">+--------------------+</span>
</span></pre></div></div>
</div>
</details>

<h2>Separator settings</h2>
<table>
<thead>
<tr>
<th>Separator</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>sep=True</code></td>
<td>All horizontal dividers included</td>
</tr>
<tr>
<td><code>sep=False</code></td>
<td>All horizontal dividers are disabled</td>
</tr>
<tr>
<td><code>sep=(1,)</code></td>
<td>Only first delimiter</td>
</tr>
<tr>
<td><code>sep=(1, 3, 5)</code></td>
<td>Only first third and fifth separator</td>
</tr>
<tr>
<td><code>sep=range(1, 100, 5)</code></td>
<td>Delimiter every five lines first 100 lines</td>
</tr>
</tbody>
</table>
<details>
<summary>Example</summary>

<div class="code-element">
    <div class="lang-line">
        <text>pycon</text>
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
    <div class="code"><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="n">table_1</span> <span class="o">=</span> <span class="p">[(</span><span class="s2">&quot;qwe&quot;</span><span class="p">,</span> <span class="s2">&quot;rty</span><span class="se">\n</span><span class="s2">uio&quot;</span><span class="p">),</span> <span class="p">(</span><span class="s2">&quot;123456</span><span class="se">\n\n</span><span class="s2">789000&quot;</span><span class="p">,</span> <span class="s2">&quot;example&quot;</span><span class="p">)]</span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="n">kwargs</span> <span class="o">=</span> <span class="p">{</span>
<span class="unselectable"><span class="o">...</span> </span>    <span class="s2">&quot;max_width&quot;</span><span class="p">:</span> <span class="p">(</span><span class="mi">3</span><span class="p">,</span> <span class="mi">4</span><span class="p">),</span>
<span class="unselectable"><span class="o">...</span> </span>    <span class="s2">&quot;max_height&quot;</span><span class="p">:</span> <span class="mi">4</span><span class="p">,</span>
<span class="unselectable"><span class="o">...</span> </span><span class="p">}</span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="n">print_table</span><span class="p">(</span><span class="n">table_1</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span> <span class="n">sep</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<span class="unselectable"><span class="go">+-----+------+</span>
<span class="go">| qwe | rty  |</span>
<span class="go">|     | uio  |</span>
<span class="go">+-----+------+</span>
<span class="go">| 123↩| exam↩|</span>
<span class="go">| 456 | ple  |</span>
<span class="go">|     |      |</span>
<span class="go">| 789…|      |</span>
<span class="go">+-----+------+</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="n">print_table</span><span class="p">(</span><span class="n">table_1</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span> <span class="n">sep</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
<span class="unselectable"><span class="go">+-----+------+</span>
<span class="go">| qwe | rty  |</span>
<span class="go">|     | uio  |</span>
<span class="go">| 123↩| exam↩|</span>
<span class="go">| 456 | ple  |</span>
<span class="go">|     |      |</span>
<span class="go">| 789…|      |</span>
<span class="go">+-----+------+</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="n">table_2</span> <span class="o">=</span> <span class="p">[(</span><span class="s2">&quot;1&quot;</span><span class="p">,</span> <span class="s2">&quot;2&quot;</span><span class="p">),</span> <span class="p">(</span><span class="s2">&quot;3&quot;</span><span class="p">,</span> <span class="s2">&quot;4&quot;</span><span class="p">)]</span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="n">print_table</span><span class="p">(</span><span class="n">table_2</span><span class="p">,</span> <span class="n">sep</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="s2">&quot;Name&quot;</span><span class="p">)</span>
<span class="unselectable"><span class="go">+-------+</span>
<span class="go">| Name  |</span>
<span class="go">+---+---+</span>
<span class="go">| 1 | 2 |</span>
<span class="go">+---+---+</span>
<span class="go">| 3 | 4 |</span>
<span class="go">+---+---+</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="n">print_table</span><span class="p">(</span><span class="n">table_2</span><span class="p">,</span> <span class="n">sep</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="s2">&quot;Name&quot;</span><span class="p">)</span>
<span class="unselectable"><span class="go">+-------+</span>
<span class="go">| Name  |</span>
<span class="go">+---+---+</span>
<span class="go">| 1 | 2 |</span>
<span class="go">| 3 | 4 |</span>
<span class="go">+---+---+</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="n">table_3</span> <span class="o">=</span> <span class="p">[(</span><span class="s2">&quot;1&quot;</span><span class="p">,</span> <span class="s2">&quot;2&quot;</span><span class="p">),</span> <span class="p">(</span><span class="s2">&quot;3&quot;</span><span class="p">,</span> <span class="s2">&quot;4&quot;</span><span class="p">),</span> <span class="p">(</span><span class="s2">&quot;5&quot;</span><span class="p">,</span> <span class="s2">&quot;6&quot;</span><span class="p">),</span> <span class="p">(</span><span class="s2">&quot;7&quot;</span><span class="p">,</span> <span class="s2">&quot;8&quot;</span><span class="p">)]</span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="n">print_table</span><span class="p">(</span><span class="n">table_3</span><span class="p">,</span> <span class="n">sep</span><span class="o">=</span><span class="p">(</span><span class="mi">1</span><span class="p">,))</span>
<span class="unselectable"><span class="go">+---+---+</span>
<span class="go">| 1 | 2 |</span>
<span class="go">+---+---+</span>
<span class="go">| 3 | 4 |</span>
<span class="go">| 5 | 6 |</span>
<span class="go">| 7 | 8 |</span>
<span class="go">+---+---+</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="n">print_table</span><span class="p">(</span><span class="n">table_3</span><span class="p">,</span> <span class="n">sep</span><span class="o">=</span><span class="p">(</span><span class="mi">2</span><span class="p">,))</span>
<span class="unselectable"><span class="go">+---+---+</span>
<span class="go">| 1 | 2 |</span>
<span class="go">| 3 | 4 |</span>
<span class="go">+---+---+</span>
<span class="go">| 5 | 6 |</span>
<span class="go">| 7 | 8 |</span>
<span class="go">+---+---+</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="n">print_table</span><span class="p">(</span><span class="n">table_3</span><span class="p">,</span> <span class="n">sep</span><span class="o">=</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="mi">3</span><span class="p">))</span>
<span class="unselectable"><span class="go">+---+---+</span>
<span class="go">| 1 | 2 |</span>
<span class="go">+---+---+</span>
<span class="go">| 3 | 4 |</span>
<span class="go">| 5 | 6 |</span>
<span class="go">+---+---+</span>
<span class="go">| 7 | 8 |</span>
<span class="go">+---+---+</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="n">print_table</span><span class="p">(</span><span class="n">table_3</span><span class="p">,</span> <span class="n">sep</span><span class="o">=</span><span class="p">(</span><span class="mi">1</span><span class="p">,),</span> <span class="n">name</span><span class="o">=</span><span class="s2">&quot;Name&quot;</span><span class="p">)</span>
<span class="unselectable"><span class="go">+-------+</span>
<span class="go">| Name  |</span>
<span class="go">+---+---+</span>
<span class="go">| 1 | 2 |</span>
<span class="go">+---+---+</span>
<span class="go">| 3 | 4 |</span>
<span class="go">| 5 | 6 |</span>
<span class="go">| 7 | 8 |</span>
<span class="go">+---+---+</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="n">print_table</span><span class="p">(</span><span class="n">table_3</span><span class="p">,</span> <span class="n">sep</span><span class="o">=</span><span class="p">(</span><span class="mi">2</span><span class="p">,),</span> <span class="n">name</span><span class="o">=</span><span class="s2">&quot;Name&quot;</span><span class="p">)</span>
<span class="unselectable"><span class="go">+-------+</span>
<span class="go">| Name  |</span>
<span class="go">+---+---+</span>
<span class="go">| 1 | 2 |</span>
<span class="go">| 3 | 4 |</span>
<span class="go">+---+---+</span>
<span class="go">| 5 | 6 |</span>
<span class="go">| 7 | 8 |</span>
<span class="go">+---+---+</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="n">print_table</span><span class="p">(</span><span class="n">table_3</span><span class="p">,</span> <span class="n">sep</span><span class="o">=</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="mi">3</span><span class="p">),</span> <span class="n">name</span><span class="o">=</span><span class="s2">&quot;Name&quot;</span><span class="p">)</span>
<span class="unselectable"><span class="go">+-------+</span>
<span class="go">| Name  |</span>
<span class="go">+---+---+</span>
<span class="go">| 1 | 2 |</span>
<span class="go">+---+---+</span>
<span class="go">| 3 | 4 |</span>
<span class="go">| 5 | 6 |</span>
<span class="go">+---+---+</span>
<span class="go">| 7 | 8 |</span>
<span class="go">+---+---+</span>
</span></pre></div></div>
</div>
</details>

<h2>Borders</h2>
<details>
<summary>Border types</summary>

<div class="code-element">
    <div class="lang-line">
        <text>text</text>
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
    <div class="code"><div class="highlight"><pre><span></span>┌──────────────┬───────────────────┐
│  ascii_thin  │ ascii_thin_double │
│  +---+---+   │     +---+---+     │
│  |   |   |   │     |   |   |     │
│  +---+---+   │     +===+===+     │
│  |   |   |   │     |   |   |     │
│  +---+---+   │     +---+---+     │
│  |   |   |   │     |   |   |     │
│  +---+---+   │     +---+---+     │
├──────────────┼───────────────────┤
│ ascii_double │ ascii_double_thin │
│  +===+===+   │     +===+===+     │
│  ‖   ‖   ‖   │     ‖   ‖   ‖     │
│  +===+===+   │     +---+---+     │
│  ‖   ‖   ‖   │     ‖   ‖   ‖     │
│  +===+===+   │     +===+===+     │
│  ‖   ‖   ‖   │     ‖   ‖   ‖     │
│  +===+===+   │     +===+===+     │
├──────────────┼───────────────────┤
│     thin     │    thin_thick     │
│  ┌───┬───┐   │     ┌───┬───┐     │
│  │   │   │   │     │   │   │     │
│  ├───┼───┤   │     ┝━━━┿━━━┥     │
│  │   │   │   │     │   │   │     │
│  ├───┼───┤   │     ├───┼───┤     │
│  │   │   │   │     │   │   │     │
│  └───┴───┘   │     └───┴───┘     │
├──────────────┼───────────────────┤
│ thin_double  │  rounded_double   │
│  ┌───┬───┐   │     ╭───┬───╮     │
│  │   │   │   │     │   │   │     │
│  ╞═══╪═══╡   │     ╞═══╪═══╡     │
│  │   │   │   │     │   │   │     │
│  ├───┼───┤   │     ├───┼───┤     │
│  │   │   │   │     │   │   │     │
│  └───┴───┘   │     ╰───┴───╯     │
├──────────────┼───────────────────┤
│   rounded    │   rounded_thick   │
│  ╭───┬───╮   │     ╭───┬───╮     │
│  │   │   │   │     │   │   │     │
│  ├───┼───┤   │     ┝━━━┿━━━┥     │
│  │   │   │   │     │   │   │     │
│  ├───┼───┤   │     ├───┼───┤     │
│  │   │   │   │     │   │   │     │
│  ╰───┴───╯   │     ╰───┴───╯     │
├──────────────┼───────────────────┤
│    thick     │    thick_thin     │
│  ┏━━━┳━━━┓   │     ┌───┬───┐     │
│  ┃   ┃   ┃   │     │   │   │     │
│  ┣━━━╋━━━┫   │     ┠━━━╂━━━┨     │
│  ┃   ┃   ┃   │     │   │   │     │
│  ┣━━━╋━━━┫   │     ├───┼───┤     │
│  ┃   ┃   ┃   │     │   │   │     │
│  ┗━━━┻━━━┛   │     └───┴───┘     │
├──────────────┼───────────────────┤
│    double    │    double_thin    │
│  ╔═══╦═══╗   │     ╔═══╦═══╗     │
│  ║   ║   ║   │     ║   ║   ║     │
│  ╠═══╬═══╣   │     ╟───╫───╢     │
│  ║   ║   ║   │     ║   ║   ║     │
│  ╠═══╬═══╣   │     ╠═══╬═══╣     │
│  ║   ║   ║   │     ║   ║   ║     │
│  ╚═══╩═══╝   │     ╚═══╩═══╝     │
├──────────────┼───────────────────┤
│   booktabs   │  ascii_booktabs   │
│   ───────    │      -------      │
│              │                   │
│   ━━━━━━━    │      =======      │
│              │                   │
│   ───────    │      -------      │
│              │                   │
│   ───────    │      -------      │
├──────────────┼───────────────────┤
│   markdown   │                   │
│  |   |   |   │                   │
│  |---|---|   │                   │
│  |   |   |   │                   │
│  |   |   |   │                   │
└──────────────┴───────────────────┘
</pre></div></div>
</div>
</details>

<details>
<summary>Example</summary>

<div class="code-element">
    <div class="lang-line">
        <text>pycon</text>
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
    <div class="code"><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="kn">from</span> <span class="nn">table2string</span> <span class="kn">import</span> <span class="n">Table</span><span class="p">,</span> <span class="n">Themes</span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="n">name</span> <span class="o">=</span> <span class="s2">&quot;Table Name&quot;</span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="n">column_names</span> <span class="o">=</span> <span class="p">(</span><span class="s2">&quot;c1&quot;</span><span class="p">,</span> <span class="s2">&quot;c2&quot;</span><span class="p">,</span> <span class="s2">&quot;3&quot;</span><span class="p">)</span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="n">table</span> <span class="o">=</span> <span class="p">[(</span><span class="s2">&quot;1&quot;</span><span class="p">,</span> <span class="s2">&quot;2&quot;</span><span class="p">,</span> <span class="s2">&quot;3&quot;</span><span class="p">),</span> <span class="p">(</span><span class="s2">&quot;qwe&quot;</span><span class="p">,</span> <span class="s2">&quot;rty</span><span class="se">\n</span><span class="s2">uio&quot;</span><span class="p">,</span> <span class="s2">&quot;&quot;</span><span class="p">)]</span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="n">t</span> <span class="o">=</span> <span class="n">Table</span><span class="p">(</span><span class="n">table</span><span class="p">)</span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="n">t_name</span> <span class="o">=</span> <span class="n">Table</span><span class="p">(</span><span class="n">table</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="n">name</span><span class="p">)</span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="n">t_column_names</span> <span class="o">=</span> <span class="n">Table</span><span class="p">(</span><span class="n">table</span><span class="p">,</span> <span class="n">column_names</span><span class="o">=</span><span class="n">column_names</span><span class="p">)</span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="n">t_name_column_names</span> <span class="o">=</span> <span class="n">Table</span><span class="p">(</span><span class="n">table</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="n">name</span><span class="p">,</span> <span class="n">column_names</span><span class="o">=</span><span class="n">column_names</span><span class="p">)</span>
</pre></div></div>
</div>

<details>
<summary>Themes.ascii_thin</summary>

<div class="code-element">
    <div class="lang-line">
        <text>pycon</text>
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
    <div class="code"><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="n">t</span><span class="o">.</span><span class="n">print</span><span class="p">(</span><span class="n">theme</span><span class="o">=</span><span class="n">Themes</span><span class="o">.</span><span class="n">ascii_thin</span><span class="p">)</span>
<span class="unselectable"><span class="go">+-----+-----+---+</span>
<span class="go">|   1 |   2 | 3 |</span>
<span class="go">+-----+-----+---+</span>
<span class="go">| qwe | rty |   |</span>
<span class="go">|     | uio |   |</span>
<span class="go">+-----+-----+---+</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="n">t_column_names</span><span class="o">.</span><span class="n">print</span><span class="p">(</span><span class="n">theme</span><span class="o">=</span><span class="n">Themes</span><span class="o">.</span><span class="n">ascii_thin</span><span class="p">)</span>
<span class="unselectable"><span class="go">+-----+-----+---+</span>
<span class="go">| c1  | c2  | 3 |</span>
<span class="go">+-----+-----+---+</span>
<span class="go">|   1 |   2 | 3 |</span>
<span class="go">+-----+-----+---+</span>
<span class="go">| qwe | rty |   |</span>
<span class="go">|     | uio |   |</span>
<span class="go">+-----+-----+---+</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="n">t_name</span><span class="o">.</span><span class="n">print</span><span class="p">(</span><span class="n">theme</span><span class="o">=</span><span class="n">Themes</span><span class="o">.</span><span class="n">ascii_thin</span><span class="p">)</span>
<span class="unselectable"><span class="go">+---------------+</span>
<span class="go">|  Table Name   |</span>
<span class="go">+-----+-----+---+</span>
<span class="go">|   1 |   2 | 3 |</span>
<span class="go">+-----+-----+---+</span>
<span class="go">| qwe | rty |   |</span>
<span class="go">|     | uio |   |</span>
<span class="go">+-----+-----+---+</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="n">t_name_column_names</span><span class="o">.</span><span class="n">print</span><span class="p">(</span><span class="n">theme</span><span class="o">=</span><span class="n">Themes</span><span class="o">.</span><span class="n">ascii_thin</span><span class="p">)</span>
<span class="unselectable"><span class="go">+---------------+</span>
<span class="go">|  Table Name   |</span>
<span class="go">+-----+-----+---+</span>
<span class="go">| c1  | c2  | 3 |</span>
<span class="go">+-----+-----+---+</span>
<span class="go">|   1 |   2 | 3 |</span>
<span class="go">+-----+-----+---+</span>
<span class="go">| qwe | rty |   |</span>
<span class="go">|     | uio |   |</span>
<span class="go">+-----+-----+---+</span>
</span></pre></div></div>
</div>
</details>


<details>
<summary>Themes.ascii_thin_double</summary>

<div class="code-element">
    <div class="lang-line">
        <text>pycon</text>
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
    <div class="code"><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="n">t</span><span class="o">.</span><span class="n">print</span><span class="p">(</span><span class="n">theme</span><span class="o">=</span><span class="n">Themes</span><span class="o">.</span><span class="n">ascii_thin_double</span><span class="p">)</span>
<span class="unselectable"><span class="go">+-----+-----+---+</span>
<span class="go">|   1 |   2 | 3 |</span>
<span class="go">+=====+=====+===+</span>
<span class="go">| qwe | rty |   |</span>
<span class="go">|     | uio |   |</span>
<span class="go">+-----+-----+---+</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="n">t_column_names</span><span class="o">.</span><span class="n">print</span><span class="p">(</span><span class="n">theme</span><span class="o">=</span><span class="n">Themes</span><span class="o">.</span><span class="n">ascii_thin_double</span><span class="p">)</span>
<span class="unselectable"><span class="go">+-----+-----+---+</span>
<span class="go">| c1  | c2  | 3 |</span>
<span class="go">+=====+=====+===+</span>
<span class="go">|   1 |   2 | 3 |</span>
<span class="go">+-----+-----+---+</span>
<span class="go">| qwe | rty |   |</span>
<span class="go">|     | uio |   |</span>
<span class="go">+-----+-----+---+</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="n">t_name</span><span class="o">.</span><span class="n">print</span><span class="p">(</span><span class="n">theme</span><span class="o">=</span><span class="n">Themes</span><span class="o">.</span><span class="n">ascii_thin_double</span><span class="p">)</span>
<span class="unselectable"><span class="go">+---------------+</span>
<span class="go">|  Table Name   |</span>
<span class="go">+-----+-----+---+</span>
<span class="go">|   1 |   2 | 3 |</span>
<span class="go">+=====+=====+===+</span>
<span class="go">| qwe | rty |   |</span>
<span class="go">|     | uio |   |</span>
<span class="go">+-----+-----+---+</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="n">t_name_column_names</span><span class="o">.</span><span class="n">print</span><span class="p">(</span><span class="n">theme</span><span class="o">=</span><span class="n">Themes</span><span class="o">.</span><span class="n">ascii_thin_double</span><span class="p">)</span>
<span class="unselectable"><span class="go">+---------------+</span>
<span class="go">|  Table Name   |</span>
<span class="go">+-----+-----+---+</span>
<span class="go">| c1  | c2  | 3 |</span>
<span class="go">+=====+=====+===+</span>
<span class="go">|   1 |   2 | 3 |</span>
<span class="go">+-----+-----+---+</span>
<span class="go">| qwe | rty |   |</span>
<span class="go">|     | uio |   |</span>
<span class="go">+-----+-----+---+</span>
</span></pre></div></div>
</div>
</details>


<details>
<summary>Themes.ascii_double</summary>

<div class="code-element">
    <div class="lang-line">
        <text>pycon</text>
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
    <div class="code"><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="n">t</span><span class="o">.</span><span class="n">print</span><span class="p">(</span><span class="n">theme</span><span class="o">=</span><span class="n">Themes</span><span class="o">.</span><span class="n">ascii_double</span><span class="p">)</span>
<span class="unselectable"><span class="go">+=====+=====+===+</span>
<span class="go">‖   1 ‖   2 ‖ 3 ‖</span>
<span class="go">+=====+=====+===+</span>
<span class="go">‖ qwe ‖ rty ‖   ‖</span>
<span class="go">‖     ‖ uio ‖   ‖</span>
<span class="go">+=====+=====+===+</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="n">t_column_names</span><span class="o">.</span><span class="n">print</span><span class="p">(</span><span class="n">theme</span><span class="o">=</span><span class="n">Themes</span><span class="o">.</span><span class="n">ascii_double</span><span class="p">)</span>
<span class="unselectable"><span class="go">+=====+=====+===+</span>
<span class="go">‖ c1  ‖ c2  ‖ 3 ‖</span>
<span class="go">+=====+=====+===+</span>
<span class="go">‖   1 ‖   2 ‖ 3 ‖</span>
<span class="go">+=====+=====+===+</span>
<span class="go">‖ qwe ‖ rty ‖   ‖</span>
<span class="go">‖     ‖ uio ‖   ‖</span>
<span class="go">+=====+=====+===+</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="n">t_name</span><span class="o">.</span><span class="n">print</span><span class="p">(</span><span class="n">theme</span><span class="o">=</span><span class="n">Themes</span><span class="o">.</span><span class="n">ascii_double</span><span class="p">)</span>
<span class="unselectable"><span class="go">+===============+</span>
<span class="go">‖  Table Name   ‖</span>
<span class="go">+=====+=====+===+</span>
<span class="go">‖   1 ‖   2 ‖ 3 ‖</span>
<span class="go">+=====+=====+===+</span>
<span class="go">‖ qwe ‖ rty ‖   ‖</span>
<span class="go">‖     ‖ uio ‖   ‖</span>
<span class="go">+=====+=====+===+</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="n">t_name_column_names</span><span class="o">.</span><span class="n">print</span><span class="p">(</span><span class="n">theme</span><span class="o">=</span><span class="n">Themes</span><span class="o">.</span><span class="n">ascii_double</span><span class="p">)</span>
<span class="unselectable"><span class="go">+===============+</span>
<span class="go">‖  Table Name   ‖</span>
<span class="go">+=====+=====+===+</span>
<span class="go">‖ c1  ‖ c2  ‖ 3 ‖</span>
<span class="go">+=====+=====+===+</span>
<span class="go">‖   1 ‖   2 ‖ 3 ‖</span>
<span class="go">+=====+=====+===+</span>
<span class="go">‖ qwe ‖ rty ‖   ‖</span>
<span class="go">‖     ‖ uio ‖   ‖</span>
<span class="go">+=====+=====+===+</span>
</span></pre></div></div>
</div>
</details>


<details>
<summary>Themes.ascii_double_thin</summary>

<div class="code-element">
    <div class="lang-line">
        <text>pycon</text>
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
    <div class="code"><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="n">t</span><span class="o">.</span><span class="n">print</span><span class="p">(</span><span class="n">theme</span><span class="o">=</span><span class="n">Themes</span><span class="o">.</span><span class="n">ascii_double_thin</span><span class="p">)</span>
<span class="unselectable"><span class="go">+=====+=====+===+</span>
<span class="go">‖   1 ‖   2 ‖ 3 ‖</span>
<span class="go">+-----+-----+---+</span>
<span class="go">‖ qwe ‖ rty ‖   ‖</span>
<span class="go">‖     ‖ uio ‖   ‖</span>
<span class="go">+=====+=====+===+</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="n">t_column_names</span><span class="o">.</span><span class="n">print</span><span class="p">(</span><span class="n">theme</span><span class="o">=</span><span class="n">Themes</span><span class="o">.</span><span class="n">ascii_double_thin</span><span class="p">)</span>
<span class="unselectable"><span class="go">+=====+=====+===+</span>
<span class="go">‖ c1  ‖ c2  ‖ 3 ‖</span>
<span class="go">+-----+-----+---+</span>
<span class="go">‖   1 ‖   2 ‖ 3 ‖</span>
<span class="go">+=====+=====+===+</span>
<span class="go">‖ qwe ‖ rty ‖   ‖</span>
<span class="go">‖     ‖ uio ‖   ‖</span>
<span class="go">+=====+=====+===+</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="n">t_name</span><span class="o">.</span><span class="n">print</span><span class="p">(</span><span class="n">theme</span><span class="o">=</span><span class="n">Themes</span><span class="o">.</span><span class="n">ascii_double_thin</span><span class="p">)</span>
<span class="unselectable"><span class="go">+===============+</span>
<span class="go">‖  Table Name   ‖</span>
<span class="go">+=====+=====+===+</span>
<span class="go">‖   1 ‖   2 ‖ 3 ‖</span>
<span class="go">+-----+-----+---+</span>
<span class="go">‖ qwe ‖ rty ‖   ‖</span>
<span class="go">‖     ‖ uio ‖   ‖</span>
<span class="go">+=====+=====+===+</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="n">t_name_column_names</span><span class="o">.</span><span class="n">print</span><span class="p">(</span><span class="n">theme</span><span class="o">=</span><span class="n">Themes</span><span class="o">.</span><span class="n">ascii_double_thin</span><span class="p">)</span>
<span class="unselectable"><span class="go">+===============+</span>
<span class="go">‖  Table Name   ‖</span>
<span class="go">+=====+=====+===+</span>
<span class="go">‖ c1  ‖ c2  ‖ 3 ‖</span>
<span class="go">+-----+-----+---+</span>
<span class="go">‖   1 ‖   2 ‖ 3 ‖</span>
<span class="go">+=====+=====+===+</span>
<span class="go">‖ qwe ‖ rty ‖   ‖</span>
<span class="go">‖     ‖ uio ‖   ‖</span>
<span class="go">+=====+=====+===+</span>
</span></pre></div></div>
</div>
</details>


<details>
<summary>Themes.ascii_booktabs</summary>

<div class="code-element">
    <div class="lang-line">
        <text>pycon</text>
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
    <div class="code"><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="n">t</span><span class="o">.</span><span class="n">print</span><span class="p">(</span><span class="n">theme</span><span class="o">=</span><span class="n">Themes</span><span class="o">.</span><span class="n">ascii_booktabs</span><span class="p">)</span>
<span class="unselectable"><span class="go"> --------------- </span>
<span class="go">    1     2   3  </span>
<span class="go"> =============== </span>
<span class="go">  qwe   rty      </span>
<span class="go">        uio      </span>
<span class="go"> --------------- </span>
<span class="o">&gt;&gt;&gt; </span></span><span class="n">t_column_names</span><span class="o">.</span><span class="n">print</span><span class="p">(</span><span class="n">theme</span><span class="o">=</span><span class="n">Themes</span><span class="o">.</span><span class="n">ascii_booktabs</span><span class="p">)</span>
<span class="unselectable"><span class="go"> --------------- </span>
<span class="go">  c1    c2    3  </span>
<span class="go"> =============== </span>
<span class="go">    1     2   3  </span>
<span class="go"> --------------- </span>
<span class="go">  qwe   rty      </span>
<span class="go">        uio      </span>
<span class="go"> --------------- </span>
<span class="o">&gt;&gt;&gt; </span></span><span class="n">t_name</span><span class="o">.</span><span class="n">print</span><span class="p">(</span><span class="n">theme</span><span class="o">=</span><span class="n">Themes</span><span class="o">.</span><span class="n">ascii_booktabs</span><span class="p">)</span>
<span class="unselectable"><span class="go"> --------------- </span>
<span class="go">   Table Name    </span>
<span class="go"> --------------- </span>
<span class="go">    1     2   3  </span>
<span class="go"> =============== </span>
<span class="go">  qwe   rty      </span>
<span class="go">        uio      </span>
<span class="go"> --------------- </span>
<span class="o">&gt;&gt;&gt; </span></span><span class="n">t_name_column_names</span><span class="o">.</span><span class="n">print</span><span class="p">(</span><span class="n">theme</span><span class="o">=</span><span class="n">Themes</span><span class="o">.</span><span class="n">ascii_booktabs</span><span class="p">)</span>
<span class="unselectable"><span class="go"> --------------- </span>
<span class="go">   Table Name    </span>
<span class="go"> --------------- </span>
<span class="go">  c1    c2    3  </span>
<span class="go"> =============== </span>
<span class="go">    1     2   3  </span>
<span class="go"> --------------- </span>
<span class="go">  qwe   rty      </span>
<span class="go">        uio      </span>
<span class="go"> ---------------</span>
</span></pre></div></div>
</div>
</details>


<details>
<summary>Themes.thin</summary>

<div class="code-element">
    <div class="lang-line">
        <text>pycon</text>
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
    <div class="code"><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="n">t</span><span class="o">.</span><span class="n">print</span><span class="p">(</span><span class="n">theme</span><span class="o">=</span><span class="n">Themes</span><span class="o">.</span><span class="n">thin</span><span class="p">)</span>
<span class="unselectable"><span class="go">┌─────┬─────┬───┐</span>
<span class="go">│   1 │   2 │ 3 │</span>
<span class="go">├─────┼─────┼───┤</span>
<span class="go">│ qwe │ rty │   │</span>
<span class="go">│     │ uio │   │</span>
<span class="go">└─────┴─────┴───┘</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="n">t_column_names</span><span class="o">.</span><span class="n">print</span><span class="p">(</span><span class="n">theme</span><span class="o">=</span><span class="n">Themes</span><span class="o">.</span><span class="n">thin</span><span class="p">)</span>
<span class="unselectable"><span class="go">┌─────┬─────┬───┐</span>
<span class="go">│ c1  │ c2  │ 3 │</span>
<span class="go">├─────┼─────┼───┤</span>
<span class="go">│   1 │   2 │ 3 │</span>
<span class="go">├─────┼─────┼───┤</span>
<span class="go">│ qwe │ rty │   │</span>
<span class="go">│     │ uio │   │</span>
<span class="go">└─────┴─────┴───┘</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="n">t_name</span><span class="o">.</span><span class="n">print</span><span class="p">(</span><span class="n">theme</span><span class="o">=</span><span class="n">Themes</span><span class="o">.</span><span class="n">thin</span><span class="p">)</span>
<span class="unselectable"><span class="go">┌───────────────┐</span>
<span class="go">│  Table Name   │</span>
<span class="go">├─────┬─────┬───┤</span>
<span class="go">│   1 │   2 │ 3 │</span>
<span class="go">├─────┼─────┼───┤</span>
<span class="go">│ qwe │ rty │   │</span>
<span class="go">│     │ uio │   │</span>
<span class="go">└─────┴─────┴───┘</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="n">t_name_column_names</span><span class="o">.</span><span class="n">print</span><span class="p">(</span><span class="n">theme</span><span class="o">=</span><span class="n">Themes</span><span class="o">.</span><span class="n">thin</span><span class="p">)</span>
<span class="unselectable"><span class="go">┌───────────────┐</span>
<span class="go">│  Table Name   │</span>
<span class="go">├─────┬─────┬───┤</span>
<span class="go">│ c1  │ c2  │ 3 │</span>
<span class="go">├─────┼─────┼───┤</span>
<span class="go">│   1 │   2 │ 3 │</span>
<span class="go">├─────┼─────┼───┤</span>
<span class="go">│ qwe │ rty │   │</span>
<span class="go">│     │ uio │   │</span>
<span class="go">└─────┴─────┴───┘</span>
</span></pre></div></div>
</div>
</details>


<details>
<summary>Themes.thin_thick</summary>

<div class="code-element">
    <div class="lang-line">
        <text>pycon</text>
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
    <div class="code"><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="n">t</span><span class="o">.</span><span class="n">print</span><span class="p">(</span><span class="n">theme</span><span class="o">=</span><span class="n">Themes</span><span class="o">.</span><span class="n">thin_thick</span><span class="p">)</span>
<span class="unselectable"><span class="go">┌─────┬─────┬───┐</span>
<span class="go">│   1 │   2 │ 3 │</span>
<span class="go">┝━━━━━┿━━━━━┿━━━┥</span>
<span class="go">│ qwe │ rty │   │</span>
<span class="go">│     │ uio │   │</span>
<span class="go">└─────┴─────┴───┘</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="n">t_column_names</span><span class="o">.</span><span class="n">print</span><span class="p">(</span><span class="n">theme</span><span class="o">=</span><span class="n">Themes</span><span class="o">.</span><span class="n">thin_thick</span><span class="p">)</span>
<span class="unselectable"><span class="go">┌─────┬─────┬───┐</span>
<span class="go">│ c1  │ c2  │ 3 │</span>
<span class="go">┝━━━━━┿━━━━━┿━━━┥</span>
<span class="go">│   1 │   2 │ 3 │</span>
<span class="go">├─────┼─────┼───┤</span>
<span class="go">│ qwe │ rty │   │</span>
<span class="go">│     │ uio │   │</span>
<span class="go">└─────┴─────┴───┘</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="n">t_name</span><span class="o">.</span><span class="n">print</span><span class="p">(</span><span class="n">theme</span><span class="o">=</span><span class="n">Themes</span><span class="o">.</span><span class="n">thin_thick</span><span class="p">)</span>
<span class="unselectable"><span class="go">┌───────────────┐</span>
<span class="go">│  Table Name   │</span>
<span class="go">├─────┬─────┬───┤</span>
<span class="go">│   1 │   2 │ 3 │</span>
<span class="go">┝━━━━━┿━━━━━┿━━━┥</span>
<span class="go">│ qwe │ rty │   │</span>
<span class="go">│     │ uio │   │</span>
<span class="go">└─────┴─────┴───┘</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="n">t_name_column_names</span><span class="o">.</span><span class="n">print</span><span class="p">(</span><span class="n">theme</span><span class="o">=</span><span class="n">Themes</span><span class="o">.</span><span class="n">thin_thick</span><span class="p">)</span>
<span class="unselectable"><span class="go">┌───────────────┐</span>
<span class="go">│  Table Name   │</span>
<span class="go">├─────┬─────┬───┤</span>
<span class="go">│ c1  │ c2  │ 3 │</span>
<span class="go">┝━━━━━┿━━━━━┿━━━┥</span>
<span class="go">│   1 │   2 │ 3 │</span>
<span class="go">├─────┼─────┼───┤</span>
<span class="go">│ qwe │ rty │   │</span>
<span class="go">│     │ uio │   │</span>
<span class="go">└─────┴─────┴───┘</span>
</span></pre></div></div>
</div>
</details>


<details>
<summary>Themes.thin_double</summary>

<div class="code-element">
    <div class="lang-line">
        <text>pycon</text>
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
    <div class="code"><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="n">t</span><span class="o">.</span><span class="n">print</span><span class="p">(</span><span class="n">theme</span><span class="o">=</span><span class="n">Themes</span><span class="o">.</span><span class="n">thin_double</span><span class="p">)</span>
<span class="unselectable"><span class="go">┌─────┬─────┬───┐</span>
<span class="go">│   1 │   2 │ 3 │</span>
<span class="go">╞═════╪═════╪═══╡</span>
<span class="go">│ qwe │ rty │   │</span>
<span class="go">│     │ uio │   │</span>
<span class="go">└─────┴─────┴───┘</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="n">t_column_names</span><span class="o">.</span><span class="n">print</span><span class="p">(</span><span class="n">theme</span><span class="o">=</span><span class="n">Themes</span><span class="o">.</span><span class="n">thin_double</span><span class="p">)</span>
<span class="unselectable"><span class="go">┌─────┬─────┬───┐</span>
<span class="go">│ c1  │ c2  │ 3 │</span>
<span class="go">╞═════╪═════╪═══╡</span>
<span class="go">│   1 │   2 │ 3 │</span>
<span class="go">├─────┼─────┼───┤</span>
<span class="go">│ qwe │ rty │   │</span>
<span class="go">│     │ uio │   │</span>
<span class="go">└─────┴─────┴───┘</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="n">t_name</span><span class="o">.</span><span class="n">print</span><span class="p">(</span><span class="n">theme</span><span class="o">=</span><span class="n">Themes</span><span class="o">.</span><span class="n">thin_double</span><span class="p">)</span>
<span class="unselectable"><span class="go">┌───────────────┐</span>
<span class="go">│  Table Name   │</span>
<span class="go">├─────┬─────┬───┤</span>
<span class="go">│   1 │   2 │ 3 │</span>
<span class="go">╞═════╪═════╪═══╡</span>
<span class="go">│ qwe │ rty │   │</span>
<span class="go">│     │ uio │   │</span>
<span class="go">└─────┴─────┴───┘</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="n">t_name_column_names</span><span class="o">.</span><span class="n">print</span><span class="p">(</span><span class="n">theme</span><span class="o">=</span><span class="n">Themes</span><span class="o">.</span><span class="n">thin_double</span><span class="p">)</span>
<span class="unselectable"><span class="go">┌───────────────┐</span>
<span class="go">│  Table Name   │</span>
<span class="go">├─────┬─────┬───┤</span>
<span class="go">│ c1  │ c2  │ 3 │</span>
<span class="go">╞═════╪═════╪═══╡</span>
<span class="go">│   1 │   2 │ 3 │</span>
<span class="go">├─────┼─────┼───┤</span>
<span class="go">│ qwe │ rty │   │</span>
<span class="go">│     │ uio │   │</span>
<span class="go">└─────┴─────┴───┘</span>
</span></pre></div></div>
</div>
</details>


<details>
<summary>Themes.rounded</summary>

<div class="code-element">
    <div class="lang-line">
        <text>pycon</text>
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
    <div class="code"><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="n">t</span><span class="o">.</span><span class="n">print</span><span class="p">(</span><span class="n">theme</span><span class="o">=</span><span class="n">Themes</span><span class="o">.</span><span class="n">rounded</span><span class="p">)</span>
<span class="unselectable"><span class="go">╭─────┬─────┬───╮</span>
<span class="go">│   1 │   2 │ 3 │</span>
<span class="go">├─────┼─────┼───┤</span>
<span class="go">│ qwe │ rty │   │</span>
<span class="go">│     │ uio │   │</span>
<span class="go">╰─────┴─────┴───╯</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="n">t_column_names</span><span class="o">.</span><span class="n">print</span><span class="p">(</span><span class="n">theme</span><span class="o">=</span><span class="n">Themes</span><span class="o">.</span><span class="n">rounded</span><span class="p">)</span>
<span class="unselectable"><span class="go">╭─────┬─────┬───╮</span>
<span class="go">│ c1  │ c2  │ 3 │</span>
<span class="go">├─────┼─────┼───┤</span>
<span class="go">│   1 │   2 │ 3 │</span>
<span class="go">├─────┼─────┼───┤</span>
<span class="go">│ qwe │ rty │   │</span>
<span class="go">│     │ uio │   │</span>
<span class="go">╰─────┴─────┴───╯</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="n">t_name</span><span class="o">.</span><span class="n">print</span><span class="p">(</span><span class="n">theme</span><span class="o">=</span><span class="n">Themes</span><span class="o">.</span><span class="n">rounded</span><span class="p">)</span>
<span class="unselectable"><span class="go">╭───────────────╮</span>
<span class="go">│  Table Name   │</span>
<span class="go">├─────┬─────┬───┤</span>
<span class="go">│   1 │   2 │ 3 │</span>
<span class="go">├─────┼─────┼───┤</span>
<span class="go">│ qwe │ rty │   │</span>
<span class="go">│     │ uio │   │</span>
<span class="go">╰─────┴─────┴───╯</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="n">t_name_column_names</span><span class="o">.</span><span class="n">print</span><span class="p">(</span><span class="n">theme</span><span class="o">=</span><span class="n">Themes</span><span class="o">.</span><span class="n">rounded</span><span class="p">)</span>
<span class="unselectable"><span class="go">╭───────────────╮</span>
<span class="go">│  Table Name   │</span>
<span class="go">├─────┬─────┬───┤</span>
<span class="go">│ c1  │ c2  │ 3 │</span>
<span class="go">├─────┼─────┼───┤</span>
<span class="go">│   1 │   2 │ 3 │</span>
<span class="go">├─────┼─────┼───┤</span>
<span class="go">│ qwe │ rty │   │</span>
<span class="go">│     │ uio │   │</span>
<span class="go">╰─────┴─────┴───╯</span>
</span></pre></div></div>
</div>
</details>


<details>
<summary>Themes.rounded_thick</summary>

<div class="code-element">
    <div class="lang-line">
        <text>pycon</text>
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
    <div class="code"><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="n">t</span><span class="o">.</span><span class="n">print</span><span class="p">(</span><span class="n">theme</span><span class="o">=</span><span class="n">Themes</span><span class="o">.</span><span class="n">rounded_thick</span><span class="p">)</span>
<span class="unselectable"><span class="go">╭─────┬─────┬───╮</span>
<span class="go">│   1 │   2 │ 3 │</span>
<span class="go">┝━━━━━┿━━━━━┿━━━┥</span>
<span class="go">│ qwe │ rty │   │</span>
<span class="go">│     │ uio │   │</span>
<span class="go">╰─────┴─────┴───╯</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="n">t_column_names</span><span class="o">.</span><span class="n">print</span><span class="p">(</span><span class="n">theme</span><span class="o">=</span><span class="n">Themes</span><span class="o">.</span><span class="n">rounded_thick</span><span class="p">)</span>
<span class="unselectable"><span class="go">╭─────┬─────┬───╮</span>
<span class="go">│ c1  │ c2  │ 3 │</span>
<span class="go">┝━━━━━┿━━━━━┿━━━┥</span>
<span class="go">│   1 │   2 │ 3 │</span>
<span class="go">├─────┼─────┼───┤</span>
<span class="go">│ qwe │ rty │   │</span>
<span class="go">│     │ uio │   │</span>
<span class="go">╰─────┴─────┴───╯</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="n">t_name</span><span class="o">.</span><span class="n">print</span><span class="p">(</span><span class="n">theme</span><span class="o">=</span><span class="n">Themes</span><span class="o">.</span><span class="n">rounded_thick</span><span class="p">)</span>
<span class="unselectable"><span class="go">╭───────────────╮</span>
<span class="go">│  Table Name   │</span>
<span class="go">├─────┬─────┬───┤</span>
<span class="go">│   1 │   2 │ 3 │</span>
<span class="go">┝━━━━━┿━━━━━┿━━━┥</span>
<span class="go">│ qwe │ rty │   │</span>
<span class="go">│     │ uio │   │</span>
<span class="go">╰─────┴─────┴───╯</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="n">t_name_column_names</span><span class="o">.</span><span class="n">print</span><span class="p">(</span><span class="n">theme</span><span class="o">=</span><span class="n">Themes</span><span class="o">.</span><span class="n">rounded_thick</span><span class="p">)</span>
<span class="unselectable"><span class="go">╭───────────────╮</span>
<span class="go">│  Table Name   │</span>
<span class="go">├─────┬─────┬───┤</span>
<span class="go">│ c1  │ c2  │ 3 │</span>
<span class="go">┝━━━━━┿━━━━━┿━━━┥</span>
<span class="go">│   1 │   2 │ 3 │</span>
<span class="go">├─────┼─────┼───┤</span>
<span class="go">│ qwe │ rty │   │</span>
<span class="go">│     │ uio │   │</span>
<span class="go">╰─────┴─────┴───╯</span>
</span></pre></div></div>
</div>
</details>


<details>
<summary>Themes.rounded_double</summary>

<div class="code-element">
    <div class="lang-line">
        <text>pycon</text>
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
    <div class="code"><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="n">t</span><span class="o">.</span><span class="n">print</span><span class="p">(</span><span class="n">theme</span><span class="o">=</span><span class="n">Themes</span><span class="o">.</span><span class="n">rounded_double</span><span class="p">)</span>
<span class="unselectable"><span class="go">╭─────┬─────┬───╮</span>
<span class="go">│   1 │   2 │ 3 │</span>
<span class="go">╞═════╪═════╪═══╡</span>
<span class="go">│ qwe │ rty │   │</span>
<span class="go">│     │ uio │   │</span>
<span class="go">╰─────┴─────┴───╯</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="n">t_column_names</span><span class="o">.</span><span class="n">print</span><span class="p">(</span><span class="n">theme</span><span class="o">=</span><span class="n">Themes</span><span class="o">.</span><span class="n">rounded_double</span><span class="p">)</span>
<span class="unselectable"><span class="go">╭─────┬─────┬───╮</span>
<span class="go">│ c1  │ c2  │ 3 │</span>
<span class="go">╞═════╪═════╪═══╡</span>
<span class="go">│   1 │   2 │ 3 │</span>
<span class="go">├─────┼─────┼───┤</span>
<span class="go">│ qwe │ rty │   │</span>
<span class="go">│     │ uio │   │</span>
<span class="go">╰─────┴─────┴───╯</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="n">t_name</span><span class="o">.</span><span class="n">print</span><span class="p">(</span><span class="n">theme</span><span class="o">=</span><span class="n">Themes</span><span class="o">.</span><span class="n">rounded_double</span><span class="p">)</span>
<span class="unselectable"><span class="go">╭───────────────╮</span>
<span class="go">│  Table Name   │</span>
<span class="go">├─────┬─────┬───┤</span>
<span class="go">│   1 │   2 │ 3 │</span>
<span class="go">╞═════╪═════╪═══╡</span>
<span class="go">│ qwe │ rty │   │</span>
<span class="go">│     │ uio │   │</span>
<span class="go">╰─────┴─────┴───╯</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="n">t_name_column_names</span><span class="o">.</span><span class="n">print</span><span class="p">(</span><span class="n">theme</span><span class="o">=</span><span class="n">Themes</span><span class="o">.</span><span class="n">rounded_double</span><span class="p">)</span>
<span class="unselectable"><span class="go">╭───────────────╮</span>
<span class="go">│  Table Name   │</span>
<span class="go">├─────┬─────┬───┤</span>
<span class="go">│ c1  │ c2  │ 3 │</span>
<span class="go">╞═════╪═════╪═══╡</span>
<span class="go">│   1 │   2 │ 3 │</span>
<span class="go">├─────┼─────┼───┤</span>
<span class="go">│ qwe │ rty │   │</span>
<span class="go">│     │ uio │   │</span>
<span class="go">╰─────┴─────┴───╯</span>
</span></pre></div></div>
</div>
</details>


<details>
<summary>Themes.thick</summary>

<div class="code-element">
    <div class="lang-line">
        <text>pycon</text>
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
    <div class="code"><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="n">t</span><span class="o">.</span><span class="n">print</span><span class="p">(</span><span class="n">theme</span><span class="o">=</span><span class="n">Themes</span><span class="o">.</span><span class="n">thick</span><span class="p">)</span>
<span class="unselectable"><span class="go">┏━━━━━┳━━━━━┳━━━┓</span>
<span class="go">┃   1 ┃   2 ┃ 3 ┃</span>
<span class="go">┣━━━━━╋━━━━━╋━━━┫</span>
<span class="go">┃ qwe ┃ rty ┃   ┃</span>
<span class="go">┃     ┃ uio ┃   ┃</span>
<span class="go">┗━━━━━┻━━━━━┻━━━┛</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="n">t_column_names</span><span class="o">.</span><span class="n">print</span><span class="p">(</span><span class="n">theme</span><span class="o">=</span><span class="n">Themes</span><span class="o">.</span><span class="n">thick</span><span class="p">)</span>
<span class="unselectable"><span class="go">┏━━━━━┳━━━━━┳━━━┓</span>
<span class="go">┃ c1  ┃ c2  ┃ 3 ┃</span>
<span class="go">┣━━━━━╋━━━━━╋━━━┫</span>
<span class="go">┃   1 ┃   2 ┃ 3 ┃</span>
<span class="go">┣━━━━━╋━━━━━╋━━━┫</span>
<span class="go">┃ qwe ┃ rty ┃   ┃</span>
<span class="go">┃     ┃ uio ┃   ┃</span>
<span class="go">┗━━━━━┻━━━━━┻━━━┛</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="n">t_name</span><span class="o">.</span><span class="n">print</span><span class="p">(</span><span class="n">theme</span><span class="o">=</span><span class="n">Themes</span><span class="o">.</span><span class="n">thick</span><span class="p">)</span>
<span class="unselectable"><span class="go">┏━━━━━━━━━━━━━━━┓</span>
<span class="go">┃  Table Name   ┃</span>
<span class="go">┣━━━━━┳━━━━━┳━━━┫</span>
<span class="go">┃   1 ┃   2 ┃ 3 ┃</span>
<span class="go">┣━━━━━╋━━━━━╋━━━┫</span>
<span class="go">┃ qwe ┃ rty ┃   ┃</span>
<span class="go">┃     ┃ uio ┃   ┃</span>
<span class="go">┗━━━━━┻━━━━━┻━━━┛</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="n">t_name_column_names</span><span class="o">.</span><span class="n">print</span><span class="p">(</span><span class="n">theme</span><span class="o">=</span><span class="n">Themes</span><span class="o">.</span><span class="n">thick</span><span class="p">)</span>
<span class="unselectable"><span class="go">┏━━━━━━━━━━━━━━━┓</span>
<span class="go">┃  Table Name   ┃</span>
<span class="go">┣━━━━━┳━━━━━┳━━━┫</span>
<span class="go">┃ c1  ┃ c2  ┃ 3 ┃</span>
<span class="go">┣━━━━━╋━━━━━╋━━━┫</span>
<span class="go">┃   1 ┃   2 ┃ 3 ┃</span>
<span class="go">┣━━━━━╋━━━━━╋━━━┫</span>
<span class="go">┃ qwe ┃ rty ┃   ┃</span>
<span class="go">┃     ┃ uio ┃   ┃</span>
<span class="go">┗━━━━━┻━━━━━┻━━━┛</span>
</span></pre></div></div>
</div>
</details>


<details>
<summary>Themes.thick_thin</summary>

<div class="code-element">
    <div class="lang-line">
        <text>pycon</text>
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
    <div class="code"><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="n">t</span><span class="o">.</span><span class="n">print</span><span class="p">(</span><span class="n">theme</span><span class="o">=</span><span class="n">Themes</span><span class="o">.</span><span class="n">thick_thin</span><span class="p">)</span>
<span class="unselectable"><span class="go">┌─────┬─────┬───┐</span>
<span class="go">│   1 │   2 │ 3 │</span>
<span class="go">┠━━━━━╂━━━━━╂━━━┨</span>
<span class="go">│ qwe │ rty │   │</span>
<span class="go">│     │ uio │   │</span>
<span class="go">└─────┴─────┴───┘</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="n">t_column_names</span><span class="o">.</span><span class="n">print</span><span class="p">(</span><span class="n">theme</span><span class="o">=</span><span class="n">Themes</span><span class="o">.</span><span class="n">thick_thin</span><span class="p">)</span>
<span class="unselectable"><span class="go">┌─────┬─────┬───┐</span>
<span class="go">│ c1  │ c2  │ 3 │</span>
<span class="go">┠━━━━━╂━━━━━╂━━━┨</span>
<span class="go">│   1 │   2 │ 3 │</span>
<span class="go">├─────┼─────┼───┤</span>
<span class="go">│ qwe │ rty │   │</span>
<span class="go">│     │ uio │   │</span>
<span class="go">└─────┴─────┴───┘</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="n">t_name</span><span class="o">.</span><span class="n">print</span><span class="p">(</span><span class="n">theme</span><span class="o">=</span><span class="n">Themes</span><span class="o">.</span><span class="n">thick_thin</span><span class="p">)</span>
<span class="unselectable"><span class="go">┌───────────────┐</span>
<span class="go">│  Table Name   │</span>
<span class="go">├─────┬─────┬───┤</span>
<span class="go">│   1 │   2 │ 3 │</span>
<span class="go">┠━━━━━╂━━━━━╂━━━┨</span>
<span class="go">│ qwe │ rty │   │</span>
<span class="go">│     │ uio │   │</span>
<span class="go">└─────┴─────┴───┘</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="n">t_name_column_names</span><span class="o">.</span><span class="n">print</span><span class="p">(</span><span class="n">theme</span><span class="o">=</span><span class="n">Themes</span><span class="o">.</span><span class="n">thick_thin</span><span class="p">)</span>
<span class="unselectable"><span class="go">┌───────────────┐</span>
<span class="go">│  Table Name   │</span>
<span class="go">├─────┬─────┬───┤</span>
<span class="go">│ c1  │ c2  │ 3 │</span>
<span class="go">┠━━━━━╂━━━━━╂━━━┨</span>
<span class="go">│   1 │   2 │ 3 │</span>
<span class="go">├─────┼─────┼───┤</span>
<span class="go">│ qwe │ rty │   │</span>
<span class="go">│     │ uio │   │</span>
<span class="go">└─────┴─────┴───┘</span>
</span></pre></div></div>
</div>
</details>


<details>
<summary>Themes.double</summary>

<div class="code-element">
    <div class="lang-line">
        <text>pycon</text>
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
    <div class="code"><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="n">t</span><span class="o">.</span><span class="n">print</span><span class="p">(</span><span class="n">theme</span><span class="o">=</span><span class="n">Themes</span><span class="o">.</span><span class="n">double</span><span class="p">)</span>
<span class="unselectable"><span class="go">╔═════╦═════╦═══╗</span>
<span class="go">║   1 ║   2 ║ 3 ║</span>
<span class="go">╠═════╬═════╬═══╣</span>
<span class="go">║ qwe ║ rty ║   ║</span>
<span class="go">║     ║ uio ║   ║</span>
<span class="go">╚═════╩═════╩═══╝</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="n">t_column_names</span><span class="o">.</span><span class="n">print</span><span class="p">(</span><span class="n">theme</span><span class="o">=</span><span class="n">Themes</span><span class="o">.</span><span class="n">double</span><span class="p">)</span>
<span class="unselectable"><span class="go">╔═════╦═════╦═══╗</span>
<span class="go">║ c1  ║ c2  ║ 3 ║</span>
<span class="go">╠═════╬═════╬═══╣</span>
<span class="go">║   1 ║   2 ║ 3 ║</span>
<span class="go">╠═════╬═════╬═══╣</span>
<span class="go">║ qwe ║ rty ║   ║</span>
<span class="go">║     ║ uio ║   ║</span>
<span class="go">╚═════╩═════╩═══╝</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="n">t_name</span><span class="o">.</span><span class="n">print</span><span class="p">(</span><span class="n">theme</span><span class="o">=</span><span class="n">Themes</span><span class="o">.</span><span class="n">double</span><span class="p">)</span>
<span class="unselectable"><span class="go">╔═══════════════╗</span>
<span class="go">║  Table Name   ║</span>
<span class="go">╠═════╦═════╦═══╣</span>
<span class="go">║   1 ║   2 ║ 3 ║</span>
<span class="go">╠═════╬═════╬═══╣</span>
<span class="go">║ qwe ║ rty ║   ║</span>
<span class="go">║     ║ uio ║   ║</span>
<span class="go">╚═════╩═════╩═══╝</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="n">t_name_column_names</span><span class="o">.</span><span class="n">print</span><span class="p">(</span><span class="n">theme</span><span class="o">=</span><span class="n">Themes</span><span class="o">.</span><span class="n">double</span><span class="p">)</span>
<span class="unselectable"><span class="go">╔═══════════════╗</span>
<span class="go">║  Table Name   ║</span>
<span class="go">╠═════╦═════╦═══╣</span>
<span class="go">║ c1  ║ c2  ║ 3 ║</span>
<span class="go">╠═════╬═════╬═══╣</span>
<span class="go">║   1 ║   2 ║ 3 ║</span>
<span class="go">╠═════╬═════╬═══╣</span>
<span class="go">║ qwe ║ rty ║   ║</span>
<span class="go">║     ║ uio ║   ║</span>
<span class="go">╚═════╩═════╩═══╝</span>
</span></pre></div></div>
</div>
</details>


<details>
<summary>Themes.double_thin</summary>

<div class="code-element">
    <div class="lang-line">
        <text>pycon</text>
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
    <div class="code"><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="n">t</span><span class="o">.</span><span class="n">print</span><span class="p">(</span><span class="n">theme</span><span class="o">=</span><span class="n">Themes</span><span class="o">.</span><span class="n">double_thin</span><span class="p">)</span>
<span class="unselectable"><span class="go">╔═════╦═════╦═══╗</span>
<span class="go">║   1 ║   2 ║ 3 ║</span>
<span class="go">╟─────╫─────╫───╢</span>
<span class="go">║ qwe ║ rty ║   ║</span>
<span class="go">║     ║ uio ║   ║</span>
<span class="go">╚═════╩═════╩═══╝</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="n">t_column_names</span><span class="o">.</span><span class="n">print</span><span class="p">(</span><span class="n">theme</span><span class="o">=</span><span class="n">Themes</span><span class="o">.</span><span class="n">double_thin</span><span class="p">)</span>
<span class="unselectable"><span class="go">╔═════╦═════╦═══╗</span>
<span class="go">║ c1  ║ c2  ║ 3 ║</span>
<span class="go">╟─────╫─────╫───╢</span>
<span class="go">║   1 ║   2 ║ 3 ║</span>
<span class="go">╠═════╬═════╬═══╣</span>
<span class="go">║ qwe ║ rty ║   ║</span>
<span class="go">║     ║ uio ║   ║</span>
<span class="go">╚═════╩═════╩═══╝</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="n">t_name</span><span class="o">.</span><span class="n">print</span><span class="p">(</span><span class="n">theme</span><span class="o">=</span><span class="n">Themes</span><span class="o">.</span><span class="n">double_thin</span><span class="p">)</span>
<span class="unselectable"><span class="go">╔═══════════════╗</span>
<span class="go">║  Table Name   ║</span>
<span class="go">╠═════╦═════╦═══╣</span>
<span class="go">║   1 ║   2 ║ 3 ║</span>
<span class="go">╟─────╫─────╫───╢</span>
<span class="go">║ qwe ║ rty ║   ║</span>
<span class="go">║     ║ uio ║   ║</span>
<span class="go">╚═════╩═════╩═══╝</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="n">t_name_column_names</span><span class="o">.</span><span class="n">print</span><span class="p">(</span><span class="n">theme</span><span class="o">=</span><span class="n">Themes</span><span class="o">.</span><span class="n">double_thin</span><span class="p">)</span>
<span class="unselectable"><span class="go">╔═══════════════╗</span>
<span class="go">║  Table Name   ║</span>
<span class="go">╠═════╦═════╦═══╣</span>
<span class="go">║ c1  ║ c2  ║ 3 ║</span>
<span class="go">╟─────╫─────╫───╢</span>
<span class="go">║   1 ║   2 ║ 3 ║</span>
<span class="go">╠═════╬═════╬═══╣</span>
<span class="go">║ qwe ║ rty ║   ║</span>
<span class="go">║     ║ uio ║   ║</span>
<span class="go">╚═════╩═════╩═══╝</span>
</span></pre></div></div>
</div>
</details>


<details>
<summary>Themes.booktabs</summary>

<div class="code-element">
    <div class="lang-line">
        <text>pycon</text>
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
    <div class="code"><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="n">t</span><span class="o">.</span><span class="n">print</span><span class="p">(</span><span class="n">theme</span><span class="o">=</span><span class="n">Themes</span><span class="o">.</span><span class="n">booktabs</span><span class="p">)</span>
<span class="unselectable"><span class="go"> ─────────────── </span>
<span class="go">    1     2   3  </span>
<span class="go"> ━━━━━━━━━━━━━━━ </span>
<span class="go">  qwe   rty      </span>
<span class="go">        uio      </span>
<span class="go"> ─────────────── </span>
<span class="o">&gt;&gt;&gt; </span></span><span class="n">t_column_names</span><span class="o">.</span><span class="n">print</span><span class="p">(</span><span class="n">theme</span><span class="o">=</span><span class="n">Themes</span><span class="o">.</span><span class="n">booktabs</span><span class="p">)</span>
<span class="unselectable"><span class="go"> ─────────────── </span>
<span class="go">  c1    c2    3  </span>
<span class="go"> ━━━━━━━━━━━━━━━ </span>
<span class="go">    1     2   3  </span>
<span class="go"> ─────────────── </span>
<span class="go">  qwe   rty      </span>
<span class="go">        uio      </span>
<span class="go"> ─────────────── </span>
<span class="o">&gt;&gt;&gt; </span></span><span class="n">t_name</span><span class="o">.</span><span class="n">print</span><span class="p">(</span><span class="n">theme</span><span class="o">=</span><span class="n">Themes</span><span class="o">.</span><span class="n">booktabs</span><span class="p">)</span>
<span class="unselectable"><span class="go"> ─────────────── </span>
<span class="go">   Table Name    </span>
<span class="go"> ─────────────── </span>
<span class="go">    1     2   3  </span>
<span class="go"> ━━━━━━━━━━━━━━━ </span>
<span class="go">  qwe   rty      </span>
<span class="go">        uio      </span>
<span class="go"> ─────────────── </span>
<span class="o">&gt;&gt;&gt; </span></span><span class="n">t_name_column_names</span><span class="o">.</span><span class="n">print</span><span class="p">(</span><span class="n">theme</span><span class="o">=</span><span class="n">Themes</span><span class="o">.</span><span class="n">booktabs</span><span class="p">)</span>
<span class="unselectable"><span class="go"> ─────────────── </span>
<span class="go">   Table Name    </span>
<span class="go"> ─────────────── </span>
<span class="go">  c1    c2    3  </span>
<span class="go"> ━━━━━━━━━━━━━━━ </span>
<span class="go">    1     2   3  </span>
<span class="go"> ─────────────── </span>
<span class="go">  qwe   rty      </span>
<span class="go">        uio      </span>
<span class="go"> ───────────────</span>
</span></pre></div></div>
</div>
</details>


<details>
<summary>Themes.markdown</summary>

<div class="code-element">
    <div class="lang-line">
        <text>pycon</text>
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
    <div class="code"><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="n">t</span><span class="o">.</span><span class="n">print</span><span class="p">(</span><span class="n">theme</span><span class="o">=</span><span class="n">Themes</span><span class="o">.</span><span class="n">markdown</span><span class="p">)</span>
<span class="unselectable"><span class="go">|   1 |   2 | 3 |</span>
<span class="go">|-----|-----|---|</span>
<span class="go">| qwe | rty |   |</span>
<span class="go">|     | uio |   |</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="n">t_column_names</span><span class="o">.</span><span class="n">print</span><span class="p">(</span><span class="n">theme</span><span class="o">=</span><span class="n">Themes</span><span class="o">.</span><span class="n">markdown</span><span class="p">)</span>
<span class="unselectable"><span class="go">| c1  | c2  | 3 |</span>
<span class="go">|-----|-----|---|</span>
<span class="go">|   1 |   2 | 3 |</span>
<span class="go">| qwe | rty |   |</span>
<span class="go">|     | uio |   |</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="n">t_name</span><span class="o">.</span><span class="n">print</span><span class="p">(</span><span class="n">theme</span><span class="o">=</span><span class="n">Themes</span><span class="o">.</span><span class="n">markdown</span><span class="p">)</span>
<span class="unselectable"><span class="go">|  Table Name   |</span>
<span class="go">|   1 |   2 | 3 |</span>
<span class="go">|-----|-----|---|</span>
<span class="go">| qwe | rty |   |</span>
<span class="go">|     | uio |   |</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="n">t_name_column_names</span><span class="o">.</span><span class="n">print</span><span class="p">(</span><span class="n">theme</span><span class="o">=</span><span class="n">Themes</span><span class="o">.</span><span class="n">markdown</span><span class="p">)</span>
<span class="unselectable"><span class="go">|  Table Name   |</span>
<span class="go">| c1  | c2  | 3 |</span>
<span class="go">|-----|-----|---|</span>
<span class="go">|   1 |   2 | 3 |</span>
<span class="go">| qwe | rty |   |</span>
<span class="go">|     | uio |   |</span>
</span></pre></div></div>
</div>
</details>
</details>

<h2>Emojis</h2>
<details>
<summary>Example</summary>

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
    <div class="code"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">prettytable</span> <span class="kn">import</span> <span class="n">PrettyTable</span>
<span class="kn">from</span> <span class="nn">table2string</span> <span class="kn">import</span> <span class="n">Table</span>

<span class="n">names</span> <span class="o">=</span> <span class="p">(</span><span class="s2">&quot;plain text&quot;</span><span class="p">,</span> <span class="s2">&quot;emoji&quot;</span><span class="p">)</span>
<span class="n">table</span> <span class="o">=</span> <span class="p">[</span>
    <span class="p">(</span>
        <span class="s2">&quot;text</span><span class="se">\n</span><span class="s2">text&quot;</span><span class="p">,</span>
        <span class="s2">&quot;👨‍👩‍👧‍👦👨‍👩‍👦‍👦👨‍👩‍👧‍👧</span><span class="se">\n</span><span class="s2">&quot;</span>
        <span class="s2">&quot;👨‍👨‍👧‍👦👨‍👨‍👧‍👧👨‍👩‍👧👩‍❤️‍👨</span><span class="se">\n</span><span class="s2">&quot;</span>
        <span class="s2">&quot;👨‍❤️‍👨👯👩‍🦼👭👨‍👩‍👧‍👦</span><span class="se">\n</span><span class="s2">&quot;</span>
        <span class="s2">&quot;👨‍👨‍👧‍👦👨‍👨‍👦👩‍👩‍👧</span><span class="se">\n</span><span class="s2">&quot;</span>
        <span class="s2">&quot;👨‍👨‍👧‍👧👨‍👩‍👦‍👦&quot;</span><span class="p">,</span>
    <span class="p">),</span>
<span class="p">]</span>
<span class="n">t</span> <span class="o">=</span> <span class="n">PrettyTable</span><span class="p">(</span><span class="n">title</span><span class="o">=</span><span class="s2">&quot;prettytable&quot;</span><span class="p">,</span> <span class="n">field_names</span><span class="o">=</span><span class="n">names</span><span class="p">,</span> <span class="n">align</span><span class="o">=</span><span class="s2">&quot;c&quot;</span><span class="p">)</span>
<span class="n">t</span><span class="o">.</span><span class="n">add_rows</span><span class="p">(</span><span class="n">table</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">t</span><span class="p">)</span>

<span class="n">t</span> <span class="o">=</span> <span class="n">Table</span><span class="p">(</span><span class="n">table</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="s2">&quot;table2string&quot;</span><span class="p">,</span> <span class="n">column_names</span><span class="o">=</span><span class="n">names</span><span class="p">)</span>
<span class="n">t</span><span class="o">.</span><span class="n">print</span><span class="p">(</span><span class="n">align</span><span class="o">=</span><span class="s2">&quot;^&quot;</span><span class="p">,</span> <span class="n">sep</span><span class="o">=</span><span class="p">(</span><span class="mi">1</span><span class="p">,))</span>
</pre></div></div>
</div>

<details>
    <summary>Windows Terminal</summary>
    <img alt="emoji_example_1.png" src="https://raw.githubusercontent.com/EgorKhabarov/table2string/master/images/emoji_example_Windows_Terminal.png">
</details>

<details>
    <summary>Windows 10</summary>
    <img alt="emoji_example_windows_10_terminal.png" src="https://raw.githubusercontent.com/EgorKhabarov/table2string/master/images/emoji_example_windows_10_terminal.png">
</details>

<details>
    <summary>Windows 11</summary>
    <img alt="emoji_example_windows_11_terminal.png" src="https://raw.githubusercontent.com/EgorKhabarov/table2string/master/images/emoji_example_windows_11_terminal.png">
</details>

<details>
    <summary>VT100 terminal emulator</summary>
    <img alt="emoji_example_VT100_terminal_emulator.png" src="https://raw.githubusercontent.com/EgorKhabarov/table2string/master/images/emoji_example_VT100_terminal_emulator.png">
</details>
</details>