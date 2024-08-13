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
<pre><code class="language-python">compressed_data = bz2.compress(b&quot;Hello, World!&quot;)
print(compressed_data)
</code></pre>
<p><strong>bz2.decompress(data)</strong> Распаковывает данные BZ2.</p>
<pre><code class="language-python">decompressed_data = bz2.decompress(compressed_data)
print(decompressed_data)
</code></pre>