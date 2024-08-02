<p>Библиотека "psutil" в Python используется для доступа и управления информацией о системе и процессах.
Она предоставляет функции для получения информации о процессоре, памяти, дисках, сети и др.
Это полезно для мониторинга системы, оптимизации ресурсов и отладки.</p>
<table>
<thead>
<tr>
<th>Метод</th>
<th>Описание</th>
</tr>
</thead>
<tbody>
<tr>
<td>psutil.cpu_percent()</td>
<td>Возвращает процент использования ЦП</td>
</tr>
<tr>
<td>psutil.virtual_memory()</td>
<td>Возвращает информацию о виртуальной памяти</td>
</tr>
<tr>
<td>psutil.disk_usage()</td>
<td>Возвращает использование дискового пространства</td>
</tr>
<tr>
<td>psutil.net_io_counters()</td>
<td>Возвращает сетевые счетчики ввода-вывода</td>
</tr>
<tr>
<td>psutil.process_count()</td>
<td>Возвращает количество запущенных процессов</td>
</tr>
</tbody>
</table>
<p>psutil.cpu_percent(): Возвращает текущий процент использования CPU в виде числа от 0 до 100.</p>
<div class="code-element">
<div class="lang-line">
  <text>python</text>
  <button class="copy-button"
          id="codeefe1f071b4b1b6314abf7554a8dee2d6b"
          onclick="copyCode(codeefe1f071b4b1b6314abf7554a8dee2d6, codeefe1f071b4b1b6314abf7554a8dee2d6b)">
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
<div class="code" id="codeefe1f071b4b1b6314abf7554a8dee2d6"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">psutil</span>

<span class="n">cpu_percent</span> <span class="o">=</span> <span class="n">psutil</span><span class="o">.</span><span class="n">cpu_percent</span><span class="p">()</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Текущий процент использования CPU:&quot;</span><span class="p">,</span> <span class="n">cpu_percent</span><span class="p">)</span>
</pre></div></div>
</div>

<p>psutil.virtual_memory(): Возвращает информацию о виртуальной памяти в виде объекта.
Можно получить доступ к атрибутам, таким как "total" (всего памяти), "available" (доступно памяти), "used" (используется памяти) и др.</p>
<div class="code-element">
<div class="lang-line">
  <text>python</text>
  <button class="copy-button"
          id="code97b9f9e6d4d93c355b4e0d882ec70a43b"
          onclick="copyCode(code97b9f9e6d4d93c355b4e0d882ec70a43, code97b9f9e6d4d93c355b4e0d882ec70a43b)">
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
<div class="code" id="code97b9f9e6d4d93c355b4e0d882ec70a43"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">psutil</span>

<span class="n">virtual_memory</span> <span class="o">=</span> <span class="n">psutil</span><span class="o">.</span><span class="n">virtual_memory</span><span class="p">()</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Общая доступная память:&quot;</span><span class="p">,</span> <span class="n">virtual_memory</span><span class="o">.</span><span class="n">total</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Доступная память:&quot;</span><span class="p">,</span> <span class="n">virtual_memory</span><span class="o">.</span><span class="n">available</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Используется памяти:&quot;</span><span class="p">,</span> <span class="n">virtual_memory</span><span class="o">.</span><span class="n">used</span><span class="p">)</span>
</pre></div></div>
</div>

<p>psutil.disk_usage(): Возвращает информацию об использовании дискового пространства для указанного пути в виде объекта.
Можно получить доступ к атрибутам, таким как "total" (всего пространства),
"used" (используется пространство), "free" (свободное пространство) и др.</p>
<div class="code-element">
<div class="lang-line">
  <text>python</text>
  <button class="copy-button"
          id="code981a7c36b8d210761d8ccc1ca9df731db"
          onclick="copyCode(code981a7c36b8d210761d8ccc1ca9df731d, code981a7c36b8d210761d8ccc1ca9df731db)">
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
<div class="code" id="code981a7c36b8d210761d8ccc1ca9df731d"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">psutil</span>

<span class="n">disk_usage</span> <span class="o">=</span> <span class="n">psutil</span><span class="o">.</span><span class="n">disk_usage</span><span class="p">(</span><span class="s2">&quot;/&quot;</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Общее пространство диска:&quot;</span><span class="p">,</span> <span class="n">disk_usage</span><span class="o">.</span><span class="n">total</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Используется пространства диска:&quot;</span><span class="p">,</span> <span class="n">disk_usage</span><span class="o">.</span><span class="n">used</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Свободное пространство диска:&quot;</span><span class="p">,</span> <span class="n">disk_usage</span><span class="o">.</span><span class="n">free</span><span class="p">)</span>
</pre></div></div>
</div>

<p>psutil.net_io_counters(): Возвращает сетевые счетчики ввода-вывода в виде объекта.
Можно получить доступ к атрибутам, таким как "bytes_sent" (отправленные байты), "bytes_recv" (полученные байты), "packets_sent" (отправленные пакеты) и др.</p>
<div class="code-element">
<div class="lang-line">
  <text>python</text>
  <button class="copy-button"
          id="code388c27441f797b5a34e69dafe676ecb2b"
          onclick="copyCode(code388c27441f797b5a34e69dafe676ecb2, code388c27441f797b5a34e69dafe676ecb2b)">
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
<div class="code" id="code388c27441f797b5a34e69dafe676ecb2"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">psutil</span>

<span class="n">net_io_counters</span> <span class="o">=</span> <span class="n">psutil</span><span class="o">.</span><span class="n">net_io_counters</span><span class="p">()</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Отправленные байты:&quot;</span><span class="p">,</span> <span class="n">net_io_counters</span><span class="o">.</span><span class="n">bytes_sent</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Полученные байты:&quot;</span><span class="p">,</span> <span class="n">net_io_counters</span><span class="o">.</span><span class="n">bytes_recv</span><span class="p">)</span>
</pre></div></div>
</div>

<p>psutil.process_count(): Возвращает количество текущих запущенных процессов.</p>
<div class="code-element">
<div class="lang-line">
  <text>python</text>
  <button class="copy-button"
          id="codea0fa44acbf93850109063ba8af527e2ab"
          onclick="copyCode(codea0fa44acbf93850109063ba8af527e2a, codea0fa44acbf93850109063ba8af527e2ab)">
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
<div class="code" id="codea0fa44acbf93850109063ba8af527e2a"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">psutil</span>

<span class="n">process_count</span> <span class="o">=</span> <span class="n">psutil</span><span class="o">.</span><span class="n">process_count</span><span class="p">()</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Количество запущенных процессов:&quot;</span><span class="p">,</span> <span class="n">process_count</span><span class="p">)</span>
</pre></div></div>
</div>