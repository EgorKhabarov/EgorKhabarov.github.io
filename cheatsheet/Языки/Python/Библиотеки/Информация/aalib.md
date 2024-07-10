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
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code80b6cc61de6b60d9d3c049be13fb34deb" onclick="copyCode(code80b6cc61de6b60d9d3c049be13fb34de, code80b6cc61de6b60d9d3c049be13fb34deb)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code80b6cc61de6b60d9d3c049be13fb34de"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">aalib</span>
<span class="kn">import</span> <span class="nn">Image</span>  <span class="c1"># Предполагается, что у вас уже есть изображение под названием &quot;image.jpg&quot;</span>

<span class="n">img</span> <span class="o">=</span> <span class="n">Image</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="s2">&quot;image.jpg&quot;</span><span class="p">)</span><span class="o">.</span><span class="n">convert</span><span class="p">(</span><span class="s1">&#39;L&#39;</span><span class="p">)</span>
<span class="n">width</span><span class="p">,</span> <span class="n">height</span> <span class="o">=</span> <span class="n">img</span><span class="o">.</span><span class="n">size</span>
<span class="n">ascii_img</span> <span class="o">=</span> <span class="n">aalib</span><span class="o">.</span><span class="n">AsciiArt</span><span class="p">(</span><span class="n">width</span><span class="o">=</span><span class="n">width</span><span class="p">,</span> <span class="n">height</span><span class="o">=</span><span class="n">height</span><span class="p">)</span>
<span class="n">ascii_img</span><span class="o">.</span><span class="n">render</span><span class="p">(</span><span class="n">img</span><span class="p">)</span>
<span class="n">ascii_img</span><span class="o">.</span><span class="n">save</span><span class="p">(</span><span class="s2">&quot;output.txt&quot;</span><span class="p">)</span>
</pre></div></div></div>

<p><strong>render_to_memory(image)</strong> - Возвращает ASCII-графику в виде строки.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="codeea4cce69fcc3d4efcbe1d41497b21bacb" onclick="copyCode(codeea4cce69fcc3d4efcbe1d41497b21bac, codeea4cce69fcc3d4efcbe1d41497b21bacb)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="codeea4cce69fcc3d4efcbe1d41497b21bac"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">aalib</span>
<span class="kn">import</span> <span class="nn">Image</span>

<span class="n">img</span> <span class="o">=</span> <span class="n">Image</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="s2">&quot;image.jpg&quot;</span><span class="p">)</span><span class="o">.</span><span class="n">convert</span><span class="p">(</span><span class="s1">&#39;L&#39;</span><span class="p">)</span>
<span class="n">ascii_img</span> <span class="o">=</span> <span class="n">aalib</span><span class="o">.</span><span class="n">AsciiArt</span><span class="p">(</span><span class="n">width</span><span class="o">=</span><span class="mi">80</span><span class="p">,</span> <span class="n">height</span><span class="o">=</span><span class="mi">40</span><span class="p">)</span>
<span class="n">ascii_str</span> <span class="o">=</span> <span class="n">ascii_img</span><span class="o">.</span><span class="n">render_to_memory</span><span class="p">(</span><span class="n">img</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">ascii_str</span><span class="p">)</span>
</pre></div></div></div>

<p><strong>save(filename, image)</strong> - Сохраняет ASCII-графику в файл.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code81d54dc429855f007e1208d4e543feaab" onclick="copyCode(code81d54dc429855f007e1208d4e543feaa, code81d54dc429855f007e1208d4e543feaab)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code81d54dc429855f007e1208d4e543feaa"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">aalib</span>
<span class="kn">import</span> <span class="nn">Image</span>

<span class="n">img</span> <span class="o">=</span> <span class="n">Image</span><span class="o">.</span><span class="n">open</span><span class="p">(</span><span class="s2">&quot;image.jpg&quot;</span><span class="p">)</span><span class="o">.</span><span class="n">convert</span><span class="p">(</span><span class="s1">&#39;L&#39;</span><span class="p">)</span>
<span class="n">ascii_img</span> <span class="o">=</span> <span class="n">aalib</span><span class="o">.</span><span class="n">AsciiArt</span><span class="p">(</span><span class="n">width</span><span class="o">=</span><span class="mi">80</span><span class="p">,</span> <span class="n">height</span><span class="o">=</span><span class="mi">40</span><span class="p">)</span>
<span class="n">ascii_img</span><span class="o">.</span><span class="n">render</span><span class="p">(</span><span class="n">img</span><span class="p">)</span>
<span class="n">ascii_img</span><span class="o">.</span><span class="n">save</span><span class="p">(</span><span class="s2">&quot;output.txt&quot;</span><span class="p">,</span> <span class="n">img</span><span class="p">)</span>
</pre></div></div></div>