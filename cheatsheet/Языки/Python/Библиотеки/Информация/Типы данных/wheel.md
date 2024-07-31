<p>Библиотека "wheel" в Python используется для упрощения установки пакетов и их распространения.
Она представляет собой формат пакета, который содержит предварительно
скомпилированные бинарные файлы, что позволяет ускорить процесс установки.</p>
<h3>Методы модуля "wheel":</h3>
<p><code>convert</code>: используется для преобразования исходных файлов пакета в формат wheel.
<code>install</code>: позволяет установить пакет из wheel-файла.
<code>unpack</code>: распаковывает содержимое wheel-файла.
<code>pack</code>: упаковывает исходные файлы пакета в wheel-файл.</p>
<h3>Подмодули:</h3>
<p><code>metadata</code>: содержит методы для работы с метаданными пакета, такими как версия, автор и описание.
<code>tags</code>: предоставляет информацию о поддерживаемых платформах и интерпретаторах.
<code>signatures</code>: позволяет работать с подписями wheel-файлов.
<code>pep425tags</code>: предоставляет методы для работы с тегами PEP 425,
которые описывают совместимость пакетов с определенными версиями Python и операционных систем.</p>
<h3>convert</h3>
<p>Преобразует исходные файлы пакета в формат wheel.</p>
<div class="code-element">
<div class="lang-line">
  <text>python</text>
  <button class="copy-button"
          id="code910088685b1ecc8fd7795585669d96e0b"
          onclick="copyCode(code910088685b1ecc8fd7795585669d96e0, code910088685b1ecc8fd7795585669d96e0b)">
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
<div class="code" id="code910088685b1ecc8fd7795585669d96e0"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">wheel</span> <span class="kn">import</span> <span class="n">convert</span>

<span class="n">convert</span><span class="o">.</span><span class="n">pack</span><span class="p">(</span><span class="s2">&quot;path/to/source/package&quot;</span><span class="p">)</span>
</pre></div></div>
</div>

<h3>install</h3>
<p>Устанавливает пакет из wheel-файла.</p>
<div class="code-element">
<div class="lang-line">
  <text>python</text>
  <button class="copy-button"
          id="codefbeade60d884e7efd1362b749a3cd0f5b"
          onclick="copyCode(codefbeade60d884e7efd1362b749a3cd0f5, codefbeade60d884e7efd1362b749a3cd0f5b)">
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
<div class="code" id="codefbeade60d884e7efd1362b749a3cd0f5"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">wheel</span> <span class="kn">import</span> <span class="n">install</span>

<span class="n">install</span><span class="o">.</span><span class="n">install</span><span class="p">(</span><span class="s2">&quot;path/to/wheel/file.whl&quot;</span><span class="p">)</span>
</pre></div></div>
</div>

<h3>unpack</h3>
<p>Распаковывает содержимое wheel-файла.</p>
<div class="code-element">
<div class="lang-line">
  <text>python</text>
  <button class="copy-button"
          id="code453f40e68155a6b8c95458b08af1f724b"
          onclick="copyCode(code453f40e68155a6b8c95458b08af1f724, code453f40e68155a6b8c95458b08af1f724b)">
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
<div class="code" id="code453f40e68155a6b8c95458b08af1f724"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">wheel</span> <span class="kn">import</span> <span class="n">unpack</span>

<span class="n">unpack</span><span class="o">.</span><span class="n">unpack</span><span class="p">(</span><span class="s2">&quot;path/to/wheel/file.whl&quot;</span><span class="p">,</span> <span class="s2">&quot;path/to/destination&quot;</span><span class="p">)</span>
</pre></div></div>
</div>

<h3>pack</h3></h3>
<p>Упаковывает исходные файлы пакета в wheel-файл.</p>
<div class="code-element">
<div class="lang-line">
  <text>python</text>
  <button class="copy-button"
          id="code4722220477268c97cabac169809365b3b"
          onclick="copyCode(code4722220477268c97cabac169809365b3, code4722220477268c97cabac169809365b3b)">
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
<div class="code" id="code4722220477268c97cabac169809365b3"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">wheel</span> <span class="kn">import</span> <span class="n">pack</span>

<span class="n">pack</span><span class="o">.</span><span class="n">pack</span><span class="p">(</span><span class="s2">&quot;path/to/source/package&quot;</span><span class="p">,</span> <span class="s2">&quot;path/to/destination/file.whl&quot;</span><span class="p">)</span>
</pre></div></div>
</div>