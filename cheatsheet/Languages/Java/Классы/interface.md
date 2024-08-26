<div class="code_element"><div class="lang_line"><text>java</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-java"><div class="highlight"><pre><span></span><span class="kd">public</span><span class="w"> </span><span class="kd">interface</span> <span class="nc">InterfaceName</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span>
<span class="p">}</span>
</pre></div></div></div>
<div class="code_element"><div class="lang_line"><text>java</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-java"><div class="highlight"><pre><span></span><span class="kd">public</span><span class="w"> </span><span class="kd">interface</span> <span class="nc">InterfaceName</span><span class="w"> </span><span class="kd">extends</span><span class="w"> </span><span class="n">Interface2Name</span><span class="p">,</span><span class="w"> </span><span class="n">Interface3Name</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span>
<span class="p">}</span>
</pre></div></div></div>
<div class="code_element"><div class="lang_line"><text>java</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-java"><div class="highlight"><pre><span></span><span class="kd">public</span><span class="w"> </span><span class="kd">class</span> <span class="nc">ClassName</span><span class="w"> </span><span class="kd">implements</span><span class="w"> </span><span class="n">InterfaceName</span><span class="p">,</span><span class="w"> </span><span class="n">Interface2Name</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span>
<span class="p">}</span>
</pre></div></div></div>

<ul>
<li>Методы <code>public abstract</code></li>
<li>Поля <code>public final static</code></li>
</ul>
<h3>Example</h3>
<div class="code_element"><div class="lang_line"><text>java</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-java"><div class="highlight"><pre><span></span><span class="kd">public</span><span class="w"> </span><span class="kd">interface</span> <span class="nc">ILights</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="kt">boolean</span><span class="w"> </span><span class="n">isOn</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="kc">false</span><span class="p">;</span>
<span class="w">    </span><span class="kt">void</span><span class="w"> </span><span class="nf">setLight</span><span class="w"> </span><span class="p">(</span><span class="kt">boolean</span><span class="w"> </span><span class="n">set</span><span class="p">);</span>
<span class="p">}</span>
</pre></div></div></div>

<div class="code_element"><div class="lang_line"><text>java</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-java"><div class="highlight"><pre><span></span><span class="kd">interface</span> <span class="nc">MyInterface</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="n">MY_CONSTANT</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">10</span><span class="p">;</span>

<span class="w">    </span><span class="k">default</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="nf">defaultMethod</span><span class="p">(</span><span class="n">String</span><span class="w"> </span><span class="n">argument</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">        </span><span class="n">System</span><span class="p">.</span><span class="na">out</span><span class="p">.</span><span class="na">println</span><span class="p">(</span><span class="s">&quot;Value of argument: &quot;</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">argument</span><span class="p">);</span>
<span class="w">        </span><span class="n">System</span><span class="p">.</span><span class="na">out</span><span class="p">.</span><span class="na">println</span><span class="p">(</span><span class="s">&quot;Value of MY_CONSTANT: &quot;</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">MY_CONSTANT</span><span class="p">);</span>
<span class="w">    </span><span class="p">}</span>
<span class="p">}</span>

<span class="kd">class</span> <span class="nc">MyClass</span><span class="w"> </span><span class="kd">implements</span><span class="w"> </span><span class="n">MyInterface</span><span class="w"> </span><span class="p">{}</span>

<span class="kd">public</span><span class="w"> </span><span class="kd">class</span> <span class="nc">Main</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="kd">public</span><span class="w"> </span><span class="kd">static</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="nf">main</span><span class="p">(</span><span class="n">String</span><span class="o">[]</span><span class="w"> </span><span class="n">args</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">        </span><span class="n">MyClass</span><span class="w"> </span><span class="n">myObject</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="k">new</span><span class="w"> </span><span class="n">MyClass</span><span class="p">();</span>
<span class="w">        </span><span class="n">myObject</span><span class="p">.</span><span class="na">defaultMethod</span><span class="p">(</span><span class="s">&quot;Text&quot;</span><span class="p">);</span>
<span class="w">        </span><span class="c1">// Value of argument: Text</span>
<span class="w">        </span><span class="c1">// Value of MY_CONSTANT: 10</span>
<span class="w">    </span><span class="p">}</span>
<span class="p">}</span>
</pre></div></div></div>