<div class="code-element"><div class="lang-line"><text>pycon</text><button class="copy-code-button" onclick="copyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="n">a</span> <span class="o">=</span> <span class="p">[[]]</span><span class="o">*</span><span class="mi">3</span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="n">a</span><span class="p">:</span>
<span class="unselectable"><span class="o">...</span> </span>    <span class="nb">print</span><span class="p">(</span><span class="nb">id</span><span class="p">(</span><span class="n">x</span><span class="p">))</span>
<span class="unselectable"><span class="gp">...</span></span>
<span class="unselectable"><span class="go">3276075832448</span>
<span class="go">3276075832448</span>
<span class="go">3276075832448</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="n">a</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="n">a</span>
<span class="unselectable"><span class="go">[[1], [1], [1]]</span>
<span class="o">&gt;&gt;&gt; </span></span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="n">b</span> <span class="o">=</span> <span class="p">[[]</span> <span class="k">for</span> <span class="n">_</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">3</span><span class="p">)]</span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="n">b</span><span class="p">:</span>
<span class="unselectable"><span class="o">...</span> </span>    <span class="nb">print</span><span class="p">(</span><span class="nb">id</span><span class="p">(</span><span class="n">x</span><span class="p">))</span>
<span class="unselectable"><span class="gp">...</span></span>
<span class="unselectable"><span class="go">3276075828928</span>
<span class="go">3276075828992</span>
<span class="go">3276075828864</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="n">b</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="n">b</span>
<span class="unselectable"><span class="go">[[], [1], []]</span>
<span class="o">&gt;&gt;&gt; </span></span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="n">c</span> <span class="o">=</span> <span class="p">[[]]</span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="nb">print</span><span class="p">(</span><span class="nb">id</span><span class="p">(</span><span class="n">c</span><span class="p">[</span><span class="mi">0</span><span class="p">]))</span>
<span class="unselectable"><span class="go">3276075894784</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="p">(</span><span class="n">c</span> <span class="o">+</span> <span class="n">c</span><span class="p">):</span>
<span class="unselectable"><span class="o">...</span> </span>    <span class="nb">print</span><span class="p">(</span><span class="nb">id</span><span class="p">(</span><span class="n">x</span><span class="p">))</span>
<span class="unselectable"><span class="gp">...</span></span>
<span class="unselectable"><span class="go">3276075894784</span>
<span class="go">3276075894784</span>
<span class="o">&gt;&gt;&gt; </span></span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="n">d</span> <span class="o">=</span> <span class="p">((),)</span><span class="o">*</span><span class="mi">3</span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="n">d</span><span class="p">:</span>
<span class="unselectable"><span class="o">...</span> </span>    <span class="nb">print</span><span class="p">(</span><span class="nb">id</span><span class="p">(</span><span class="n">d</span><span class="p">))</span>
<span class="unselectable"><span class="gp">...</span></span>
<span class="unselectable"><span class="go">3276075830656</span>
<span class="go">3276075830656</span>
<span class="go">3276075830656</span>
</span></pre></div></div></div>