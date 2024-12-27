<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">vedis</span> <span class="kn">import</span> <span class="n">Vedis</span>
<span class="n">db</span> <span class="o">=</span> <span class="n">Vedis</span><span class="p">(</span><span class="s2">&quot;:mem:&quot;</span><span class="p">)</span>  <span class="c1"># Create an in-memory database.</span>
<span class="n">db</span> <span class="o">=</span> <span class="n">Vedis</span><span class="p">(</span><span class="s2">&quot;Dict.vedis&quot;</span><span class="p">)</span>
<span class="k">with</span> <span class="n">db</span><span class="o">.</span><span class="n">transaction</span><span class="p">():</span>
    <span class="n">db</span><span class="p">[</span><span class="s2">&quot;key&quot;</span><span class="p">]</span> <span class="o">=</span> <span class="s2">&quot;value&quot;</span>
    <span class="n">db</span><span class="o">.</span><span class="n">rollback</span><span class="p">()</span>  <span class="c1"># Undo changes.</span>
    <span class="n">db</span><span class="o">.</span><span class="n">commit</span><span class="p">()</span>
<span class="nb">print</span><span class="p">(</span><span class="n">db</span><span class="p">[</span><span class="s2">&quot;key&quot;</span><span class="p">])</span>
</pre></div></div></div>

<p><a href="https://vedis-python.readthedocs.io/en/latest/quickstart.html">https://vedis-python.readthedocs.io/en/latest/quickstart.html</a></p>
<p>Пример использования в боте
<a href="https://mastergroosha.github.io/telegram-tutorial/docs/lesson_11/">https://mastergroosha.github.io/telegram-tutorial/docs/lesson_11/</a></p>