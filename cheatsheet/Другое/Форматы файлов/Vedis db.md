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
    <div class="code"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">vedis</span> <span class="kn">import</span> <span class="n">Vedis</span>
<span class="n">db</span> <span class="o">=</span> <span class="n">Vedis</span><span class="p">(</span><span class="s2">&quot;:mem:&quot;</span><span class="p">)</span>  <span class="c1"># Create an in-memory database.</span>
<span class="n">db</span> <span class="o">=</span> <span class="n">Vedis</span><span class="p">(</span><span class="s2">&quot;Dict.vedis&quot;</span><span class="p">)</span>
<span class="k">with</span> <span class="n">db</span><span class="o">.</span><span class="n">transaction</span><span class="p">():</span>
    <span class="n">db</span><span class="p">[</span><span class="s2">&quot;key&quot;</span><span class="p">]</span> <span class="o">=</span> <span class="s2">&quot;value&quot;</span>
    <span class="n">db</span><span class="o">.</span><span class="n">rollback</span><span class="p">()</span>  <span class="c1"># Undo changes.</span>
    <span class="n">db</span><span class="o">.</span><span class="n">commit</span><span class="p">()</span>
<span class="nb">print</span><span class="p">(</span><span class="n">db</span><span class="p">[</span><span class="s2">&quot;key&quot;</span><span class="p">])</span>
</pre></div></div>
</div>

<p><a target="_blank" href="https://vedis-python.readthedocs.io/en/latest/quickstart.html">https://vedis-python.readthedocs.io/en/latest/quickstart.html</a></p>
<p>Пример использования в боте
<a target="_blank" href="https://mastergroosha.github.io/telegram-tutorial/docs/lesson_11/">https://mastergroosha.github.io/telegram-tutorial/docs/lesson_11/</a></p>