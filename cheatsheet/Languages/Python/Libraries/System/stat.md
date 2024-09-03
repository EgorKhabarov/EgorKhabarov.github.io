<p>Библиотека "stat" в Python используется для работы с информацией о файловой системе,
такой как атрибуты файла, права доступа и временные метки.</p>
<table>
<thead>
<tr>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>stat.S_ISDIR(mode)</td>
<td>Проверяет, является ли файл директорией</td>
</tr>
<tr>
<td>stat.S_ISREG(mode)</td>
<td>Проверяет, является ли файл обычным файлом</td>
</tr>
<tr>
<td>stat.S_ISLNK(mode)</td>
<td>Проверяет, является ли файл символической ссылкой</td>
</tr>
<tr>
<td>stat.S_ISSOCK(mode)</td>
<td>Проверяет, является ли файл сокетом</td>
</tr>
<tr>
<td>stat.S_ISFIFO(mode)</td>
<td>Проверяет, является ли файл каналом FIFO</td>
</tr>
<tr>
<td>stat.S_ISBLK(mode)</td>
<td>Проверяет, является ли файл блочным устройством</td>
</tr>
<tr>
<td>stat.S_ISCHR(mode)</td>
<td>Проверяет, является ли файл символьным устройством</td>
</tr>
<tr>
<td>stat.S_IMODE(mode)</td>
<td>Возвращает режим доступа к файлу</td>
</tr>
<tr>
<td>stat.S_IFMT(mode)</td>
<td>Возвращает тип файла и режим доступа</td>
</tr>
</tbody>
</table>
<h3>Примеры</h3>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">os</span>
<span class="kn">import</span> <span class="nn">stat</span>

<span class="n">file_path</span> <span class="o">=</span> <span class="s2">&quot;path/to/file.txt&quot;</span>
<span class="n">file_stat</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">stat</span><span class="p">(</span><span class="n">file_path</span><span class="p">)</span>

<span class="k">if</span> <span class="n">stat</span><span class="o">.</span><span class="n">S_ISDIR</span><span class="p">(</span><span class="n">file_stat</span><span class="o">.</span><span class="n">st_mode</span><span class="p">):</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;File is a directory&quot;</span><span class="p">)</span>
<span class="k">else</span><span class="p">:</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;File is not a directory&quot;</span><span class="p">)</span>

<span class="k">if</span> <span class="n">stat</span><span class="o">.</span><span class="n">S_ISREG</span><span class="p">(</span><span class="n">file_stat</span><span class="o">.</span><span class="n">st_mode</span><span class="p">):</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;File is a regular file&quot;</span><span class="p">)</span>
<span class="k">else</span><span class="p">:</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;File is not a regular file&quot;</span><span class="p">)</span>

<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;File mode:&quot;</span><span class="p">,</span> <span class="n">stat</span><span class="o">.</span><span class="n">S_IMODE</span><span class="p">(</span><span class="n">file_stat</span><span class="o">.</span><span class="n">st_mode</span><span class="p">))</span>
</pre></div></div></div>