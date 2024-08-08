<p>Модуль bz2 в Python предоставляет интерфейс для сжатия и распаковки данных
с использованием алгоритма BZ2 (Burrows-Wheeler).
Он позволяет работать с файлами и байтовыми объектами, обеспечивая эффективное сжатие данных.</p>
<table>
<thead>
<tr>
<th>Метод</th>
<th>Описание</th>
</tr>
</thead>
<tbody>
<tr>
<td>bz2.compress(data, compresslevel=9)</td>
<td>Сжимает данные BZ2. Можно указать уровень сжатия (1-9).</td>
</tr>
<tr>
<td>bz2.decompress(data)</td>
<td>Распаковывает данные BZ2.</td>
</tr>
<tr>
<td>bz2.BZ2File(file, mode="r", buffering=0, compresslevel=9)</td>
<td>Создает файловый объект BZ2. Режимы: "r" (чтение), "w" (запись), "a" (добавление).</td>
</tr>
</tbody>
</table>
<p><strong>bz2.compress(data, compresslevel=9)</strong> Сжимает данные BZ2.</p>
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
    <div class="code"><div class="highlight"><pre><span></span><span class="n">compressed_data</span> <span class="o">=</span> <span class="n">bz2</span><span class="o">.</span><span class="n">compress</span><span class="p">(</span><span class="sa">b</span><span class="s2">&quot;Hello, World!&quot;</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">compressed_data</span><span class="p">)</span>
</pre></div></div>
</div>

<p><strong>bz2.decompress(data)</strong> Распаковывает данные BZ2.</p>
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
    <div class="code"><div class="highlight"><pre><span></span><span class="n">decompressed_data</span> <span class="o">=</span> <span class="n">bz2</span><span class="o">.</span><span class="n">decompress</span><span class="p">(</span><span class="n">compressed_data</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">decompressed_data</span><span class="p">)</span>
</pre></div></div>
</div>