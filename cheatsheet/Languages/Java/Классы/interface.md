<div class="code-element"><div class="lang-line"><text>java</text><button class="copy-button" onclick="copyCode(this)"><svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="kd">public</span><span class="w"> </span><span class="kd">interface</span> <span class="nc">ILights</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="kt">boolean</span><span class="w"> </span><span class="n">isOn</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="kc">false</span><span class="p">;</span>
<span class="w">    </span><span class="kt">void</span><span class="w"> </span><span class="nf">setLight</span><span class="w"> </span><span class="p">(</span><span class="kt">boolean</span><span class="w"> </span><span class="n">set</span><span class="p">);</span>
<span class="p">}</span>
</pre></div></div></div>

<p>Все поля реализованные в интерфейсе идут с <strong><code>final</code></strong>.</p>
<p><strong><code>implements</code></strong></p>