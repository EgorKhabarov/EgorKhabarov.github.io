<p>Me:</p>
<blockquote>
<p>Можешь переписать этот код на C++?</p>
<p><div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button"id="code9a1dd2e6721fd8afb93bdac248f4033ab"onclick="copyCode(code9a1dd2e6721fd8afb93bdac248f4033a, code9a1dd2e6721fd8afb93bdac248f4033ab)"><svg stroke="currentColor"fill="none"stroke-width="2"viewBox="0 0 24 24"stroke-linecap="round"stroke-linejoin="round"class="h-4 w-4"height="1em"width="1em"xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code9a1dd2e6721fd8afb93bdac248f4033a"><div class="highlight"><pre><span></span><span class="n">a</span> <span class="o">=</span> <span class="p">[</span><span class="mi">0</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="s2">&quot;привет&quot;</span><span class="p">,</span> <span class="s2">&quot;мир&quot;</span><span class="p">]</span>
<span class="nb">print</span><span class="p">(</span><span class="n">a</span><span class="p">[</span><span class="mi">2</span><span class="p">],</span> <span class="n">a</span><span class="p">[</span><span class="mi">3</span><span class="p">])</span>
</pre></div></div></div></p>
</blockquote>
<hr />
<p>ChatGPT:</p>
<blockquote>
<p>Да, я могу переписать этот код на C++:</p>
<p><div class="code-element"><div class="lang-line"><text>cpp</text><button class="copy-button"id="coded703e0f7d6e94a0f87e0b817e3d952ebb"onclick="copyCode(coded703e0f7d6e94a0f87e0b817e3d952eb, coded703e0f7d6e94a0f87e0b817e3d952ebb)"><svg stroke="currentColor"fill="none"stroke-width="2"viewBox="0 0 24 24"stroke-linecap="round"stroke-linejoin="round"class="h-4 w-4"height="1em"width="1em"xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="coded703e0f7d6e94a0f87e0b817e3d952eb"><div class="highlight"><pre><span></span><span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;iostream&gt;</span>
<span class="cp">#include</span><span class="w"> </span><span class="cpf">&lt;vector&gt;</span>
<span class="w"> </span>
<span class="kt">int</span><span class="w"> </span><span class="nf">main</span><span class="p">()</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="n">vector</span><span class="o">&lt;</span><span class="n">std</span><span class="o">::</span><span class="n">string</span><span class="o">&gt;</span><span class="w"> </span><span class="n">a</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="p">{</span><span class="w"> </span><span class="s">&quot;0&quot;</span><span class="p">,</span><span class="w"> </span><span class="s">&quot;1&quot;</span><span class="p">,</span><span class="w"> </span><span class="s">&quot;привет&quot;</span><span class="p">,</span><span class="w"> </span><span class="s">&quot;мир&quot;</span><span class="w"> </span><span class="p">};</span>
<span class="w">    </span><span class="n">std</span><span class="o">::</span><span class="n">cout</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">a</span><span class="p">[</span><span class="mi">2</span><span class="p">]</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot; &quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">a</span><span class="p">[</span><span class="mi">3</span><span class="p">]</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">std</span><span class="o">::</span><span class="n">endl</span><span class="p">;</span>
<span class="w">    </span><span class="k">return</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span>
<span class="p">}</span>
</pre></div></div></div></p>
<p>Здесь я использовал std::vector, чтобы создать массив строк, 
поскольку C++ не поддерживает нетипизированные массивы.</p>
</blockquote>