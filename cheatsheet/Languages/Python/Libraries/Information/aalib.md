<p>aalib - это библиотека для создания ASCII-графики из изображений. Она преобразует изображения в искусственные изображения, составленные из символов ASCII.</p>
<table>
<thead>
<tr>
<th>Метод</th>
<th>Описание</th>
</tr>
</thead>
<tbody>
<tr>
<td>aalib.AsciiArt</td>
<td>Создает объект AsciiArt для конвертации изображений в ASCII-графику.</td>
</tr>
<tr>
<td>AsciiArt.render(image)</td>
<td>Преобразует изображение в ASCII-графику.</td>
</tr>
<tr>
<td>AsciiArt.render_to_memory(image)</td>
<td>Возвращает ASCII-графику в виде строки.</td>
</tr>
<tr>
<td>AsciiArt.save(filename, image)</td>
<td>Сохраняет ASCII-графику в файл.</td>
</tr>
</tbody>
</table>
<p><strong>render(image)</strong> - Преобразует изображение в ASCII-графику.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" onclick="copyCode(this)"><svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">aalib</span>
<span class="kn">import</span> <span class="nn">Image</span>  <span class="c1"># Предполагается, что у вас уже есть изображение под названием &quot;image.jpg&quot;</span>

<span class="n">img</span> <span class="o">=</span> <span class="n">Image</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="s2">&quot;image.jpg&quot;</span><span class="p">)</span><span class="o">.</span><span class="n">convert</span><span class="p">(</span><span class="s2">&quot;L&quot;</span><span class="p">)</span>
<span class="n">width</span><span class="p">,</span> <span class="n">height</span> <span class="o">=</span> <span class="n">img</span><span class="o">.</span><span class="n">size</span>
<span class="n">ascii_img</span> <span class="o">=</span> <span class="n">aalib</span><span class="o">.</span><span class="n">AsciiArt</span><span class="p">(</span><span class="n">width</span><span class="o">=</span><span class="n">width</span><span class="p">,</span> <span class="n">height</span><span class="o">=</span><span class="n">height</span><span class="p">)</span>
<span class="n">ascii_img</span><span class="o">.</span><span class="n">render</span><span class="p">(</span><span class="n">img</span><span class="p">)</span>
<span class="n">ascii_img</span><span class="o">.</span><span class="n">save</span><span class="p">(</span><span class="s2">&quot;output.txt&quot;</span><span class="p">)</span>
</pre></div></div></div>

<p><strong>render_to_memory(image)</strong> - Возвращает ASCII-графику в виде строки.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" onclick="copyCode(this)"><svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">aalib</span>
<span class="kn">import</span> <span class="nn">Image</span>

<span class="n">img</span> <span class="o">=</span> <span class="n">Image</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="s2">&quot;image.jpg&quot;</span><span class="p">)</span><span class="o">.</span><span class="n">convert</span><span class="p">(</span><span class="s2">&quot;L&quot;</span><span class="p">)</span>
<span class="n">ascii_img</span> <span class="o">=</span> <span class="n">aalib</span><span class="o">.</span><span class="n">AsciiArt</span><span class="p">(</span><span class="n">width</span><span class="o">=</span><span class="mi">80</span><span class="p">,</span> <span class="n">height</span><span class="o">=</span><span class="mi">40</span><span class="p">)</span>
<span class="n">ascii_str</span> <span class="o">=</span> <span class="n">ascii_img</span><span class="o">.</span><span class="n">render_to_memory</span><span class="p">(</span><span class="n">img</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">ascii_str</span><span class="p">)</span>
</pre></div></div></div>

<p><strong>save(filename, image)</strong> - Сохраняет ASCII-графику в файл.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" onclick="copyCode(this)"><svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">aalib</span>
<span class="kn">import</span> <span class="nn">Image</span>

<span class="n">img</span> <span class="o">=</span> <span class="n">Image</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="s2">&quot;image.jpg&quot;</span><span class="p">)</span><span class="o">.</span><span class="n">convert</span><span class="p">(</span><span class="s2">&quot;L&quot;</span><span class="p">)</span>
<span class="n">ascii_img</span> <span class="o">=</span> <span class="n">aalib</span><span class="o">.</span><span class="n">AsciiArt</span><span class="p">(</span><span class="n">width</span><span class="o">=</span><span class="mi">80</span><span class="p">,</span> <span class="n">height</span><span class="o">=</span><span class="mi">40</span><span class="p">)</span>
<span class="n">ascii_img</span><span class="o">.</span><span class="n">render</span><span class="p">(</span><span class="n">img</span><span class="p">)</span>
<span class="n">ascii_img</span><span class="o">.</span><span class="n">save</span><span class="p">(</span><span class="s2">&quot;output.txt&quot;</span><span class="p">,</span> <span class="n">img</span><span class="p">)</span>
</pre></div></div></div>