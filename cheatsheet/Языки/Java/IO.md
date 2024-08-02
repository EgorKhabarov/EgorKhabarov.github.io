<h2>File</h2>
<div class="code-element">
<div class="lang-line">
  <text>java</text>
  <button class="copy-button"
          id="code82410564fa44b764fcfce67f97da5d36b"
          onclick="copyCode(code82410564fa44b764fcfce67f97da5d36, code82410564fa44b764fcfce67f97da5d36b)">
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
<div class="code" id="code82410564fa44b764fcfce67f97da5d36"><div class="highlight"><pre><span></span><span class="kn">import</span><span class="w"> </span><span class="nn">java.io.File</span><span class="p">;</span>
<span class="kn">import</span><span class="w"> </span><span class="nn">java.io.IOException</span><span class="p">;</span>

<span class="kd">public</span><span class="w"> </span><span class="kd">class</span> <span class="nc">FileExample</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="kd">public</span><span class="w"> </span><span class="kd">static</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="nf">main</span><span class="p">(</span><span class="n">String</span><span class="o">[]</span><span class="w"> </span><span class="n">args</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">        </span><span class="k">try</span><span class="w"> </span><span class="p">{</span>
<span class="w">            </span><span class="n">File</span><span class="w"> </span><span class="n">file</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="k">new</span><span class="w"> </span><span class="n">File</span><span class="p">(</span><span class="s">&quot;example.txt&quot;</span><span class="p">);</span>
<span class="w">            </span><span class="k">if</span><span class="w"> </span><span class="p">(</span><span class="n">file</span><span class="p">.</span><span class="na">createNewFile</span><span class="p">())</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="n">System</span><span class="p">.</span><span class="na">out</span><span class="p">.</span><span class="na">println</span><span class="p">(</span><span class="s">&quot;Файл создан: &quot;</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">file</span><span class="p">.</span><span class="na">getName</span><span class="p">());</span>
<span class="w">            </span><span class="p">}</span><span class="w"> </span><span class="k">else</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="n">System</span><span class="p">.</span><span class="na">out</span><span class="p">.</span><span class="na">println</span><span class="p">(</span><span class="s">&quot;Файл уже существует.&quot;</span><span class="p">);</span>
<span class="w">            </span><span class="p">}</span>
<span class="w">        </span><span class="p">}</span><span class="w"> </span><span class="k">catch</span><span class="w"> </span><span class="p">(</span><span class="n">IOException</span><span class="w"> </span><span class="n">e</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">            </span><span class="n">System</span><span class="p">.</span><span class="na">out</span><span class="p">.</span><span class="na">println</span><span class="p">(</span><span class="s">&quot;Произошла ошибка: &quot;</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">e</span><span class="p">.</span><span class="na">getMessage</span><span class="p">());</span>
<span class="w">        </span><span class="p">}</span>
<span class="w">    </span><span class="p">}</span>
<span class="p">}</span>
</pre></div></div>
</div>

<h2>BufferedReader</h2>
<div class="code-element">
<div class="lang-line">
  <text>java</text>
  <button class="copy-button"
          id="code5fb5cd407c06d6ab9517b48f32605f6bb"
          onclick="copyCode(code5fb5cd407c06d6ab9517b48f32605f6b, code5fb5cd407c06d6ab9517b48f32605f6bb)">
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
<div class="code" id="code5fb5cd407c06d6ab9517b48f32605f6b"><div class="highlight"><pre><span></span><span class="kn">import</span><span class="w"> </span><span class="nn">java.io.BufferedReader</span><span class="p">;</span>
<span class="kn">import</span><span class="w"> </span><span class="nn">java.io.FileReader</span><span class="p">;</span>
<span class="kn">import</span><span class="w"> </span><span class="nn">java.io.IOException</span><span class="p">;</span>

<span class="kd">public</span><span class="w"> </span><span class="kd">class</span> <span class="nc">BufferedReaderExample</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="kd">public</span><span class="w"> </span><span class="kd">static</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="nf">main</span><span class="p">(</span><span class="n">String</span><span class="o">[]</span><span class="w"> </span><span class="n">args</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">        </span><span class="k">try</span><span class="w"> </span><span class="p">(</span><span class="n">BufferedReader</span><span class="w"> </span><span class="n">br</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="k">new</span><span class="w"> </span><span class="n">BufferedReader</span><span class="p">(</span><span class="k">new</span><span class="w"> </span><span class="n">FileReader</span><span class="p">(</span><span class="s">&quot;example.txt&quot;</span><span class="p">)))</span><span class="w"> </span><span class="p">{</span>
<span class="w">            </span><span class="n">String</span><span class="w"> </span><span class="n">line</span><span class="p">;</span>
<span class="w">            </span><span class="k">while</span><span class="w"> </span><span class="p">((</span><span class="n">line</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">br</span><span class="p">.</span><span class="na">readLine</span><span class="p">())</span><span class="w"> </span><span class="o">!=</span><span class="w"> </span><span class="kc">null</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="n">System</span><span class="p">.</span><span class="na">out</span><span class="p">.</span><span class="na">println</span><span class="p">(</span><span class="n">line</span><span class="p">);</span>
<span class="w">            </span><span class="p">}</span>
<span class="w">        </span><span class="p">}</span><span class="w"> </span><span class="k">catch</span><span class="w"> </span><span class="p">(</span><span class="n">IOException</span><span class="w"> </span><span class="n">e</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">            </span><span class="n">System</span><span class="p">.</span><span class="na">out</span><span class="p">.</span><span class="na">println</span><span class="p">(</span><span class="s">&quot;Произошла ошибка: &quot;</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">e</span><span class="p">.</span><span class="na">getMessage</span><span class="p">());</span>
<span class="w">        </span><span class="p">}</span>
<span class="w">    </span><span class="p">}</span>
<span class="p">}</span>
</pre></div></div>
</div>

<h2>FileWriter</h2>
<div class="code-element">
<div class="lang-line">
  <text>java</text>
  <button class="copy-button"
          id="code6c5c046f67d9b871626f2a89c4e76a60b"
          onclick="copyCode(code6c5c046f67d9b871626f2a89c4e76a60, code6c5c046f67d9b871626f2a89c4e76a60b)">
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
<div class="code" id="code6c5c046f67d9b871626f2a89c4e76a60"><div class="highlight"><pre><span></span><span class="kn">import</span><span class="w"> </span><span class="nn">java.io.FileWriter</span><span class="p">;</span>
<span class="kn">import</span><span class="w"> </span><span class="nn">java.io.IOException</span><span class="p">;</span>

<span class="kd">public</span><span class="w"> </span><span class="kd">class</span> <span class="nc">FileWriterExample</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="kd">public</span><span class="w"> </span><span class="kd">static</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="nf">main</span><span class="p">(</span><span class="n">String</span><span class="o">[]</span><span class="w"> </span><span class="n">args</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">        </span><span class="k">try</span><span class="w"> </span><span class="p">(</span><span class="n">FileWriter</span><span class="w"> </span><span class="n">fw</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="k">new</span><span class="w"> </span><span class="n">FileWriter</span><span class="p">(</span><span class="s">&quot;example.txt&quot;</span><span class="p">))</span><span class="w"> </span><span class="p">{</span>
<span class="w">            </span><span class="n">fw</span><span class="p">.</span><span class="na">write</span><span class="p">(</span><span class="s">&quot;Hello, world!&quot;</span><span class="p">);</span>
<span class="w">        </span><span class="p">}</span><span class="w"> </span><span class="k">catch</span><span class="w"> </span><span class="p">(</span><span class="n">IOException</span><span class="w"> </span><span class="n">e</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">            </span><span class="n">System</span><span class="p">.</span><span class="na">out</span><span class="p">.</span><span class="na">println</span><span class="p">(</span><span class="s">&quot;Произошла ошибка: &quot;</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">e</span><span class="p">.</span><span class="na">getMessage</span><span class="p">());</span>
<span class="w">        </span><span class="p">}</span>
<span class="w">    </span><span class="p">}</span>
<span class="p">}</span>
</pre></div></div>
</div>