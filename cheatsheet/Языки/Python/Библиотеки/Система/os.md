<p>Получение информации о текущей директории:</p>
<div class="code-element">
<div class="lang-line">
  <text>python</text>
  <button class="copy-button"
          id="codee9fa14b02dacd9a6060b9f17d353e15eb"
          onclick="copyCode(codee9fa14b02dacd9a6060b9f17d353e15e, codee9fa14b02dacd9a6060b9f17d353e15eb)">
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
<div class="code" id="codee9fa14b02dacd9a6060b9f17d353e15e"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">os</span>

<span class="nb">print</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">getcwd</span><span class="p">())</span>
</pre></div></div>
</div>

<p>Создание директории:</p>
<div class="code-element">
<div class="lang-line">
  <text>python</text>
  <button class="copy-button"
          id="code52f42fc83685bc489baaaced072f6e91b"
          onclick="copyCode(code52f42fc83685bc489baaaced072f6e91, code52f42fc83685bc489baaaced072f6e91b)">
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
<div class="code" id="code52f42fc83685bc489baaaced072f6e91"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">os</span>

<span class="n">os</span><span class="o">.</span><span class="n">mkdir</span><span class="p">(</span><span class="s2">&quot;new_dir&quot;</span><span class="p">)</span>
</pre></div></div>
</div>

<p>Удаление директории:</p>
<div class="code-element">
<div class="lang-line">
  <text>python</text>
  <button class="copy-button"
          id="codeb3127cd6883e2e900896b092e0109a0db"
          onclick="copyCode(codeb3127cd6883e2e900896b092e0109a0d, codeb3127cd6883e2e900896b092e0109a0db)">
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
<div class="code" id="codeb3127cd6883e2e900896b092e0109a0d"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">os</span>

<span class="n">os</span><span class="o">.</span><span class="n">rmdir</span><span class="p">(</span><span class="s2">&quot;dir_to_remove&quot;</span><span class="p">)</span>
</pre></div></div>
</div>

<p>Проверка наличия файла или директории:</p>
<div class="code-element">
<div class="lang-line">
  <text>python</text>
  <button class="copy-button"
          id="code2fba18a5a316af8a0cd1cd6243189c3ab"
          onclick="copyCode(code2fba18a5a316af8a0cd1cd6243189c3a, code2fba18a5a316af8a0cd1cd6243189c3ab)">
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
<div class="code" id="code2fba18a5a316af8a0cd1cd6243189c3a"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">os</span>

<span class="k">if</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="s2">&quot;file.txt&quot;</span><span class="p">):</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;File exists!&quot;</span><span class="p">)</span>

<span class="k">if</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="s2">&quot;dir&quot;</span><span class="p">):</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Directory exists!&quot;</span><span class="p">)</span>
</pre></div></div>
</div>

<p>Получение списка файлов в директории:</p>
<div class="code-element">
<div class="lang-line">
  <text>python</text>
  <button class="copy-button"
          id="code2e214c7b982a2f0cd48cf252c84520deb"
          onclick="copyCode(code2e214c7b982a2f0cd48cf252c84520de, code2e214c7b982a2f0cd48cf252c84520deb)">
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
<div class="code" id="code2e214c7b982a2f0cd48cf252c84520de"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">os</span>

<span class="n">files</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">listdir</span><span class="p">(</span><span class="s2">&quot;my_dir&quot;</span><span class="p">)</span>
<span class="k">for</span> <span class="n">file</span> <span class="ow">in</span> <span class="n">files</span><span class="p">:</span>
    <span class="nb">print</span><span class="p">(</span><span class="n">file</span><span class="p">)</span>
</pre></div></div>
</div>

<p>Переименование файла или директории:</p>
<div class="code-element">
<div class="lang-line">
  <text>python</text>
  <button class="copy-button"
          id="codead00908fe5db81537a9d2ee932853e0cb"
          onclick="copyCode(codead00908fe5db81537a9d2ee932853e0c, codead00908fe5db81537a9d2ee932853e0cb)">
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
<div class="code" id="codead00908fe5db81537a9d2ee932853e0c"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">os</span>

<span class="n">os</span><span class="o">.</span><span class="n">rename</span><span class="p">(</span><span class="s2">&quot;old_file.txt&quot;</span><span class="p">,</span> <span class="s2">&quot;new_file.txt&quot;</span><span class="p">)</span>
</pre></div></div>
</div>

<p>Удаление файла:</p>
<div class="code-element">
<div class="lang-line">
  <text>python</text>
  <button class="copy-button"
          id="codec1fff048192957cfe05678cb180b8186b"
          onclick="copyCode(codec1fff048192957cfe05678cb180b8186, codec1fff048192957cfe05678cb180b8186b)">
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
<div class="code" id="codec1fff048192957cfe05678cb180b8186"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">os</span>

<span class="n">os</span><span class="o">.</span><span class="n">remove</span><span class="p">(</span><span class="s2">&quot;file_to_remove.txt&quot;</span><span class="p">)</span>
</pre></div></div>
</div>

<p>Получение информации о файле:</p>
<div class="code-element">
<div class="lang-line">
  <text>python</text>
  <button class="copy-button"
          id="codec4b936ab3ea637b7c5b2a18de493c87ab"
          onclick="copyCode(codec4b936ab3ea637b7c5b2a18de493c87a, codec4b936ab3ea637b7c5b2a18de493c87ab)">
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
<div class="code" id="codec4b936ab3ea637b7c5b2a18de493c87a"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">os</span>

<span class="n">file_stat</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">stat</span><span class="p">(</span><span class="s2">&quot;file.txt&quot;</span><span class="p">)</span>

<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Size of file:&quot;</span><span class="p">,</span> <span class="n">file_stat</span><span class="o">.</span><span class="n">st_size</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Last accessed time:&quot;</span><span class="p">,</span> <span class="n">file_stat</span><span class="o">.</span><span class="n">st_atime</span><span class="p">)</span>
</pre></div></div>
</div>

<p>Проверка, является ли путь директорией или файлом:</p>
<div class="code-element">
<div class="lang-line">
  <text>python</text>
  <button class="copy-button"
          id="code01751ab67f025478596051ce62705ebeb"
          onclick="copyCode(code01751ab67f025478596051ce62705ebe, code01751ab67f025478596051ce62705ebeb)">
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
<div class="code" id="code01751ab67f025478596051ce62705ebe"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">os</span>

<span class="k">if</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">isfile</span><span class="p">(</span><span class="s2">&quot;my_file.txt&quot;</span><span class="p">):</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;This is a file!&quot;</span><span class="p">)</span>

<span class="k">if</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">isdir</span><span class="p">(</span><span class="s2">&quot;my_file.txt&quot;</span><span class="p">):</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;This is a directory!&quot;</span><span class="p">)</span>
</pre></div></div>
</div>

<p>Получение имени файла из пути:</p>
<div class="code-element">
<div class="lang-line">
  <text>python</text>
  <button class="copy-button"
          id="code0544eb522a2c4c67b02b30dc1f6cc32bb"
          onclick="copyCode(code0544eb522a2c4c67b02b30dc1f6cc32b, code0544eb522a2c4c67b02b30dc1f6cc32bb)">
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
<div class="code" id="code0544eb522a2c4c67b02b30dc1f6cc32b"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">os</span>

<span class="nb">print</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">basename</span><span class="p">(</span><span class="s2">&quot;/my_dir/my_file.txt&quot;</span><span class="p">))</span>
</pre></div></div>
</div>

<p>Получение пути к директории из пути к файлу:</p>
<div class="code-element">
<div class="lang-line">
  <text>python</text>
  <button class="copy-button"
          id="code8dbdc85e6433ee8e88e1a38d8c886b26b"
          onclick="copyCode(code8dbdc85e6433ee8e88e1a38d8c886b26, code8dbdc85e6433ee8e88e1a38d8c886b26b)">
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
<div class="code" id="code8dbdc85e6433ee8e88e1a38d8c886b26"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">os</span>

<span class="nb">print</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">dirname</span><span class="p">(</span><span class="s2">&quot;/my_dir/my_file.txt&quot;</span><span class="p">))</span>
</pre></div></div>
</div>

<p>Получение абсолютного пути:</p>
<div class="code-element">
<div class="lang-line">
  <text>python</text>
  <button class="copy-button"
          id="codef1adebc1c5e5804b17eec56cbbab6bccb"
          onclick="copyCode(codef1adebc1c5e5804b17eec56cbbab6bcc, codef1adebc1c5e5804b17eec56cbbab6bccb)">
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
<div class="code" id="codef1adebc1c5e5804b17eec56cbbab6bcc"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">os</span>

<span class="nb">print</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">abspath</span><span class="p">(</span><span class="s2">&quot;my_dir/my_file.txt&quot;</span><span class="p">))</span>
</pre></div></div>
</div>

<p>Объединение путей:</p>
<div class="code-element">
<div class="lang-line">
  <text>python</text>
  <button class="copy-button"
          id="codeb6ce238de4b6d663c4b16841909aa5c9b"
          onclick="copyCode(codeb6ce238de4b6d663c4b16841909aa5c9, codeb6ce238de4b6d663c4b16841909aa5c9b)">
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
<div class="code" id="codeb6ce238de4b6d663c4b16841909aa5c9"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">os</span>

<span class="nb">print</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="s2">&quot;/my_dir&quot;</span><span class="p">,</span> <span class="s2">&quot;my_file.txt&quot;</span><span class="p">))</span>
</pre></div></div>
</div>

<p>Получение расширения файла:</p>
<div class="code-element">
<div class="lang-line">
  <text>python</text>
  <button class="copy-button"
          id="code20d8b5b9d862f3956c233d189ea86038b"
          onclick="copyCode(code20d8b5b9d862f3956c233d189ea86038, code20d8b5b9d862f3956c233d189ea86038b)">
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
<div class="code" id="code20d8b5b9d862f3956c233d189ea86038"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">os</span>

<span class="nb">print</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">splitext</span><span class="p">(</span><span class="s2">&quot;my_file.txt&quot;</span><span class="p">)[</span><span class="mi">1</span><span class="p">])</span>
</pre></div></div>
</div>

<p>Получение списка всех поддиректорий в директории:</p>
<div class="code-element">
<div class="lang-line">
  <text>python</text>
  <button class="copy-button"
          id="code57f64a27d9180dc5cfef09cbaaa6dcf7b"
          onclick="copyCode(code57f64a27d9180dc5cfef09cbaaa6dcf7, code57f64a27d9180dc5cfef09cbaaa6dcf7b)">
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
<div class="code" id="code57f64a27d9180dc5cfef09cbaaa6dcf7"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">os</span>

<span class="nb">print</span><span class="p">([</span><span class="n">f</span><span class="o">.</span><span class="n">path</span> <span class="k">for</span> <span class="n">f</span> <span class="ow">in</span> <span class="n">os</span><span class="o">.</span><span class="n">scandir</span><span class="p">(</span><span class="s2">&quot;my_dir&quot;</span><span class="p">)</span> <span class="k">if</span> <span class="n">f</span><span class="o">.</span><span class="n">is_dir</span><span class="p">()])</span>
</pre></div></div>
</div>