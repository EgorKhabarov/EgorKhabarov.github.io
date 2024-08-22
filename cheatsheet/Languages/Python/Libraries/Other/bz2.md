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
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="n">compressed_data</span> <span class="o">=</span> <span class="n">bz2</span><span class="o">.</span><span class="n">compress</span><span class="p">(</span><span class="sa">b</span><span class="s2">&quot;Hello, World!&quot;</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">compressed_data</span><span class="p">)</span>
</pre></div></div></div>

<p><strong>bz2.decompress(data)</strong> Распаковывает данные BZ2.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="n">decompressed_data</span> <span class="o">=</span> <span class="n">bz2</span><span class="o">.</span><span class="n">decompress</span><span class="p">(</span><span class="n">compressed_data</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">decompressed_data</span><span class="p">)</span>
</pre></div></div></div>