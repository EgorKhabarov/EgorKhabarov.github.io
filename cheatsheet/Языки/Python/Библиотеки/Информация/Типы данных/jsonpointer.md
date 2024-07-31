<p>Библиотека "jsonpointer" используется для работы с указателями JSON (JSON pointers).
Она предоставляет функциональность для создания, обновления и извлечения данных из JSON-структур с использованием указателей.</p>
<p>Методы модуля "jsonpointer" и их краткое описание:</p>
<p><code>resolve_pointer(json_obj, pointer)</code>: Разрешает указатель JSON и возвращает соответствующее значение из JSON-объекта.
<code>set_pointer(json_obj, pointer, value)</code>: Устанавливает значение по указателю JSON в JSON-объекте.
<code>remove_pointer(json_obj, pointer)</code>: Удаляет значение по указателю JSON из JSON-объекта.
<code>list_pointers(json_obj)</code>: Возвращает список всех указателей JSON в JSON-объекте.
<code>escape_pointer(pointer)</code>: Экранирует специальные символы в указателе JSON.</p>
<p>Некоторые из самых часто используемых методов "jsonpointer" и их краткое описание:</p>
<p><code>resolve_pointer(json_obj, pointer)</code>: Разрешает указатель JSON и возвращает соответствующее значение из JSON-объекта.</p>
<div class="code-element">
<div class="lang-line">
  <text>python</text>
  <button class="copy-button"
          id="codecde4a0e29834236f22b7f65e352236b1b"
          onclick="copyCode(codecde4a0e29834236f22b7f65e352236b1, codecde4a0e29834236f22b7f65e352236b1b)">
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
<div class="code" id="codecde4a0e29834236f22b7f65e352236b1"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">jsonpointer</span>

<span class="n">json_obj</span> <span class="o">=</span> <span class="p">{</span><span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;John&quot;</span><span class="p">,</span> <span class="s2">&quot;age&quot;</span><span class="p">:</span> <span class="mi">30</span><span class="p">}</span>
<span class="n">pointer</span> <span class="o">=</span> <span class="s2">&quot;/name&quot;</span>
<span class="n">value</span> <span class="o">=</span> <span class="n">jsonpointer</span><span class="o">.</span><span class="n">resolve_pointer</span><span class="p">(</span><span class="n">json_obj</span><span class="p">,</span> <span class="n">pointer</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">value</span><span class="p">)</span>  <span class="c1"># John</span>
</pre></div></div>
</div>

<p><code>set_pointer(json_obj, pointer, value)</code>: Устанавливает значение по указателю JSON в JSON-объекте.</p>
<div class="code-element">
<div class="lang-line">
  <text>python</text>
  <button class="copy-button"
          id="code2d28c32f910111888c4c3e4614365a42b"
          onclick="copyCode(code2d28c32f910111888c4c3e4614365a42, code2d28c32f910111888c4c3e4614365a42b)">
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
<div class="code" id="code2d28c32f910111888c4c3e4614365a42"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">jsonpointer</span>

<span class="n">json_obj</span> <span class="o">=</span> <span class="p">{</span><span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;John&quot;</span><span class="p">,</span> <span class="s2">&quot;age&quot;</span><span class="p">:</span> <span class="mi">30</span><span class="p">}</span>
<span class="n">pointer</span> <span class="o">=</span> <span class="s2">&quot;/name&quot;</span>
<span class="n">value</span> <span class="o">=</span> <span class="s2">&quot;Jane&quot;</span>
<span class="n">jsonpointer</span><span class="o">.</span><span class="n">set_pointer</span><span class="p">(</span><span class="n">json_obj</span><span class="p">,</span> <span class="n">pointer</span><span class="p">,</span> <span class="n">value</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">json_obj</span><span class="p">)</span>  <span class="c1"># {&quot;name&quot;: &quot;Jane&quot;, &quot;age&quot;: 30}</span>
</pre></div></div>
</div>

<p><code>remove_pointer(json_obj, pointer)</code>: Удаляет значение по указателю JSON из JSON-объекта.</p>
<div class="code-element">
<div class="lang-line">
  <text>python</text>
  <button class="copy-button"
          id="codec59829d0440e25bdef442ab0f11db314b"
          onclick="copyCode(codec59829d0440e25bdef442ab0f11db314, codec59829d0440e25bdef442ab0f11db314b)">
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
<div class="code" id="codec59829d0440e25bdef442ab0f11db314"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">jsonpointer</span>

<span class="n">json_obj</span> <span class="o">=</span> <span class="p">{</span><span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;John&quot;</span><span class="p">,</span> <span class="s2">&quot;age&quot;</span><span class="p">:</span> <span class="mi">30</span><span class="p">}</span>
<span class="n">pointer</span> <span class="o">=</span> <span class="s2">&quot;/name&quot;</span>
<span class="n">jsonpointer</span><span class="o">.</span><span class="n">remove_pointer</span><span class="p">(</span><span class="n">json_obj</span><span class="p">,</span> <span class="n">pointer</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">json_obj</span><span class="p">)</span>  <span class="c1"># {&quot;age&quot;: 30}</span>
</pre></div></div>
</div>