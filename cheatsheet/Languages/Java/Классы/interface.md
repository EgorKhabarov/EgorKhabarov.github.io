<div class="code-element">
    <div class="lang-line">
        <text>java</text>
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
    <div class="code"><div class="highlight"><pre><span></span><span class="kd">public</span><span class="w"> </span><span class="kd">interface</span> <span class="nc">ILights</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="kt">boolean</span><span class="w"> </span><span class="n">isOn</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="kc">false</span><span class="p">;</span>
<span class="w">    </span><span class="kt">void</span><span class="w"> </span><span class="nf">setLight</span><span class="w"> </span><span class="p">(</span><span class="kt">boolean</span><span class="w"> </span><span class="n">set</span><span class="p">);</span>
<span class="p">}</span>
</pre></div></div>
</div>

<p>Все поля реализованные в интерфейсе идут с <strong><code>final</code></strong>.</p>
<p><strong><code>implements</code></strong></p>