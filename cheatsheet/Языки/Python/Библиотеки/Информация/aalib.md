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
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button"id="code1360a445b9a6eb7586cb6e9cbab9f71ab"onclick="copyCode(code1360a445b9a6eb7586cb6e9cbab9f71a, code1360a445b9a6eb7586cb6e9cbab9f71ab)"><svg stroke="currentColor"fill="none"stroke-width="2"viewBox="0 0 24 24"stroke-linecap="round"stroke-linejoin="round"class="h-4 w-4"height="1em"width="1em"xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code1360a445b9a6eb7586cb6e9cbab9f71a"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">aalib</span>
<span class="kn">import</span> <span class="nn">Image</span>  <span class="c1"># Предполагается, что у вас уже есть изображение под названием &quot;image.jpg&quot;</span>

<span class="n">img</span> <span class="o">=</span> <span class="n">Image</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="s2">&quot;image.jpg&quot;</span><span class="p">)</span><span class="o">.</span><span class="n">convert</span><span class="p">(</span><span class="s2">&quot;L&quot;</span><span class="p">)</span>
<span class="n">width</span><span class="p">,</span> <span class="n">height</span> <span class="o">=</span> <span class="n">img</span><span class="o">.</span><span class="n">size</span>
<span class="n">ascii_img</span> <span class="o">=</span> <span class="n">aalib</span><span class="o">.</span><span class="n">AsciiArt</span><span class="p">(</span><span class="n">width</span><span class="o">=</span><span class="n">width</span><span class="p">,</span> <span class="n">height</span><span class="o">=</span><span class="n">height</span><span class="p">)</span>
<span class="n">ascii_img</span><span class="o">.</span><span class="n">render</span><span class="p">(</span><span class="n">img</span><span class="p">)</span>
<span class="n">ascii_img</span><span class="o">.</span><span class="n">save</span><span class="p">(</span><span class="s2">&quot;output.txt&quot;</span><span class="p">)</span>
</pre></div></div></div>

<p><strong>render_to_memory(image)</strong> - Возвращает ASCII-графику в виде строки.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button"id="code98e052e57f0aac3ca635c86e1900b8d7b"onclick="copyCode(code98e052e57f0aac3ca635c86e1900b8d7, code98e052e57f0aac3ca635c86e1900b8d7b)"><svg stroke="currentColor"fill="none"stroke-width="2"viewBox="0 0 24 24"stroke-linecap="round"stroke-linejoin="round"class="h-4 w-4"height="1em"width="1em"xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code98e052e57f0aac3ca635c86e1900b8d7"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">aalib</span>
<span class="kn">import</span> <span class="nn">Image</span>

<span class="n">img</span> <span class="o">=</span> <span class="n">Image</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="s2">&quot;image.jpg&quot;</span><span class="p">)</span><span class="o">.</span><span class="n">convert</span><span class="p">(</span><span class="s2">&quot;L&quot;</span><span class="p">)</span>
<span class="n">ascii_img</span> <span class="o">=</span> <span class="n">aalib</span><span class="o">.</span><span class="n">AsciiArt</span><span class="p">(</span><span class="n">width</span><span class="o">=</span><span class="mi">80</span><span class="p">,</span> <span class="n">height</span><span class="o">=</span><span class="mi">40</span><span class="p">)</span>
<span class="n">ascii_str</span> <span class="o">=</span> <span class="n">ascii_img</span><span class="o">.</span><span class="n">render_to_memory</span><span class="p">(</span><span class="n">img</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">ascii_str</span><span class="p">)</span>
</pre></div></div></div>

<p><strong>save(filename, image)</strong> - Сохраняет ASCII-графику в файл.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button"id="code803015983841dc8e2e0fdfa4700019aab"onclick="copyCode(code803015983841dc8e2e0fdfa4700019aa, code803015983841dc8e2e0fdfa4700019aab)"><svg stroke="currentColor"fill="none"stroke-width="2"viewBox="0 0 24 24"stroke-linecap="round"stroke-linejoin="round"class="h-4 w-4"height="1em"width="1em"xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code803015983841dc8e2e0fdfa4700019aa"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">aalib</span>
<span class="kn">import</span> <span class="nn">Image</span>

<span class="n">img</span> <span class="o">=</span> <span class="n">Image</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="s2">&quot;image.jpg&quot;</span><span class="p">)</span><span class="o">.</span><span class="n">convert</span><span class="p">(</span><span class="s2">&quot;L&quot;</span><span class="p">)</span>
<span class="n">ascii_img</span> <span class="o">=</span> <span class="n">aalib</span><span class="o">.</span><span class="n">AsciiArt</span><span class="p">(</span><span class="n">width</span><span class="o">=</span><span class="mi">80</span><span class="p">,</span> <span class="n">height</span><span class="o">=</span><span class="mi">40</span><span class="p">)</span>
<span class="n">ascii_img</span><span class="o">.</span><span class="n">render</span><span class="p">(</span><span class="n">img</span><span class="p">)</span>
<span class="n">ascii_img</span><span class="o">.</span><span class="n">save</span><span class="p">(</span><span class="s2">&quot;output.txt&quot;</span><span class="p">,</span> <span class="n">img</span><span class="p">)</span>
</pre></div></div></div>