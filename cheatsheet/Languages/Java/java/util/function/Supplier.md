<h1><code>Supplier&lt;T&gt;</code></h1>
<p><code>T get()</code>
Вернем случайное целое число от 0 до 100 включительно</p>
<div class="code_element"><div class="lang_line"><text>java</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-java"><div class="highlight"><pre><span></span><span class="kn">import</span><span class="w"> </span><span class="nn">java.util.Random</span><span class="p">;</span>
<span class="kn">import</span><span class="w"> </span><span class="nn">java.util.function.*</span><span class="p">;</span>

<span class="kd">public</span><span class="w"> </span><span class="kd">class</span> <span class="nc">MyClass</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="kd">public</span><span class="w"> </span><span class="kd">static</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="nf">main</span><span class="p">(</span><span class="n">String</span><span class="o">[]</span><span class="w"> </span><span class="n">args</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">        </span><span class="n">MyClass</span><span class="p">.</span><span class="na">test</span><span class="p">(</span>
<span class="w">            </span><span class="p">()</span><span class="w"> </span><span class="o">-&gt;</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="n">Random</span><span class="w"> </span><span class="n">r</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="k">new</span><span class="w"> </span><span class="n">Random</span><span class="p">();</span>
<span class="w">                </span><span class="k">return</span><span class="w"> </span><span class="n">r</span><span class="p">.</span><span class="na">nextInt</span><span class="p">(</span><span class="mi">101</span><span class="p">);</span>
<span class="w">            </span><span class="p">}</span>
<span class="w">        </span><span class="p">);</span>
<span class="w">    </span><span class="p">}</span>
<span class="w">    </span><span class="kd">public</span><span class="w"> </span><span class="kd">static</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="nf">test</span><span class="p">(</span><span class="n">Supplier</span><span class="o">&lt;</span><span class="n">Integer</span><span class="o">&gt;</span><span class="w"> </span><span class="n">f</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">        </span><span class="n">System</span><span class="p">.</span><span class="na">out</span><span class="p">.</span><span class="na">println</span><span class="p">(</span><span class="n">f</span><span class="p">.</span><span class="na">get</span><span class="p">());</span>
<span class="w">    </span><span class="p">}</span>
<span class="p">}</span>
</pre></div></div></div>