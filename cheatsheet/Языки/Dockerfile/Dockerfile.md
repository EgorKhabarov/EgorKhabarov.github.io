<p>Dockerfile
FROM:    Определяет базовый образ, на основе которого будет создан ваш образ контейнера. 
         Здесь мы используем образ <code>Python 3.9</code> на основе <code>slim-версии Debian</code>.</p>
<p>WORKDIR: Устанавливает рабочую директорию внутри контейнера, где будут выполняться команды.</p>
<p>COPY:    Копирует файлы из текущей директории на вашем компьютере внутрь контейнера.</p>
<p>RUN:     Выполняет команды внутри контейнера для установки зависимостей, указанных в файле <code>requirements.txt</code>.</p>
<p>CMD:     Определяет команду, которая будет запущена при запуске контейнера. 
         Здесь мы указываем запуск основного скрипта <code>main.py</code>.</p>
<div class="code-element">
<div class="lang-line">
  <text>Dockerfile</text>
  <button class="copy-button"
          id="code5147f585d92264afa63dac63bea645f6b"
          onclick="copyCode(code5147f585d92264afa63dac63bea645f6, code5147f585d92264afa63dac63bea645f6b)">
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
  <button class="copy-button-2"
        id="code5147f585d92264afa63dac63bea645f6_2b"
        onclick="DownloadCode(code5147f585d92264afa63dac63bea645f6, code5147f585d92264afa63dac63bea645f6_2b, 'Dockerfile')">
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
    <text>Download code</text>
  </button>
</div>
<div class="code" id="code5147f585d92264afa63dac63bea645f6"><div class="highlight"><pre><span></span><span class="k">FROM</span><span class="w"> </span><span class="s">python:3.9-slim-buster</span>

<span class="k">WORKDIR</span><span class="w"> </span><span class="s">/app</span>

<span class="k">COPY</span><span class="w"> </span>requirements.txt<span class="w"> </span>.

<span class="k">RUN</span><span class="w"> </span>pip3<span class="w"> </span>install<span class="w"> </span>--no-cache-dir<span class="w"> </span>-r<span class="w"> </span>requirements.txt

<span class="k">COPY</span><span class="w"> </span>.<span class="w"> </span>.

<span class="k">CMD</span><span class="w"> </span><span class="p">[</span><span class="s2">&quot;python3&quot;</span><span class="p">,</span><span class="w"> </span><span class="s2">&quot;main.py&quot;</span><span class="p">]</span>
</pre></div></div>
</div>

<div class="code-element">
<div class="lang-line">
  <text>Dockerfile</text>
  <button class="copy-button"
          id="code1ac822c9c22cd625e6dcb4038e2bde3fb"
          onclick="copyCode(code1ac822c9c22cd625e6dcb4038e2bde3f, code1ac822c9c22cd625e6dcb4038e2bde3fb)">
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
<div class="code" id="code1ac822c9c22cd625e6dcb4038e2bde3f"><div class="highlight"><pre><span></span><span class="k">ENV</span><span class="w"> </span><span class="nv">BOT_TOKEN</span><span class="o">=</span><span class="s2">&quot;&quot;</span>
</pre></div></div>
</div>

<p><img alt="docker.png" src="Языки/Dockerfile/docker.png" /></p>