<p>Библиотека "resource" в Python используется для доступа и управления системными ресурсами, такими как время CPU, память и дескрипторы файлов.</p>
<p>Методы и подмодули модуля "resource":</p>
<p><code>getrusage(who)</code> - возвращает информацию о системных ресурсах для указанного процесса или группы процессов.
<code>getrlimit(resource)</code> - получает текущие ограничения на указанный ресурс.
<code>setrlimit(resource, limits)</code> - устанавливает ограничения на указанный ресурс.
<code>getpagesize()</code> - возвращает размер страницы памяти операционной системы.
<code>getrusage()</code> - возвращает информацию о системных ресурсах для текущего процесса.
<code>RUSAGE_SELF</code> - константа, указывающая на текущий процесс.
<code>RUSAGE_CHILDREN</code> - константа, указывающая на дочерние процессы текущего процесса.</p>
<p>Наиболее часто используемые методы:</p>
<p><code>getrusage(who)</code> - получает информацию о системных ресурсах для указанного процесса или группы процессов.</p>
<div class="code-element">
<div class="lang-line">
  <text>python</text>
  <button class="copy-button"
          id="codeff662a707d265a24bf9e75097c69d673b"
          onclick="copyCode(codeff662a707d265a24bf9e75097c69d673, codeff662a707d265a24bf9e75097c69d673b)">
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
<div class="code" id="codeff662a707d265a24bf9e75097c69d673"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">resource</span>

<span class="n">usage</span> <span class="o">=</span> <span class="n">resource</span><span class="o">.</span><span class="n">getrusage</span><span class="p">(</span><span class="n">resource</span><span class="o">.</span><span class="n">RUSAGE_SELF</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">usage</span><span class="p">)</span>
</pre></div></div>
</div>

<p><code>getrlimit(resource)</code> - получает текущие ограничения на указанный ресурс.</p>
<div class="code-element">
<div class="lang-line">
  <text>python</text>
  <button class="copy-button"
          id="code2a5d2eb654bce2f5071664514e2ca416b"
          onclick="copyCode(code2a5d2eb654bce2f5071664514e2ca416, code2a5d2eb654bce2f5071664514e2ca416b)">
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
<div class="code" id="code2a5d2eb654bce2f5071664514e2ca416"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">resource</span>

<span class="n">limit</span> <span class="o">=</span> <span class="n">resource</span><span class="o">.</span><span class="n">getrlimit</span><span class="p">(</span><span class="n">resource</span><span class="o">.</span><span class="n">RLIMIT_CPU</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">limit</span><span class="p">)</span>
</pre></div></div>
</div>

<p><code>setrlimit(resource, limits)</code> - устанавливает ограничения на указанный ресурс.</p>
<div class="code-element">
<div class="lang-line">
  <text>python</text>
  <button class="copy-button"
          id="code5b563a470eba06856d527f2cefc7d1b7b"
          onclick="copyCode(code5b563a470eba06856d527f2cefc7d1b7, code5b563a470eba06856d527f2cefc7d1b7b)">
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
<div class="code" id="code5b563a470eba06856d527f2cefc7d1b7"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">resource</span>

<span class="c1"># Ограничение на время CPU - 2 секунды</span>
<span class="n">limits</span> <span class="o">=</span> <span class="p">(</span><span class="mi">2</span><span class="p">,</span> <span class="n">resource</span><span class="o">.</span><span class="n">RLIM_INFINITY</span><span class="p">)</span>
<span class="n">resource</span><span class="o">.</span><span class="n">setrlimit</span><span class="p">(</span><span class="n">resource</span><span class="o">.</span><span class="n">RLIMIT_CPU</span><span class="p">,</span> <span class="n">limits</span><span class="p">)</span>
</pre></div></div>
</div>