<div class="code-element"><div class="lang-line"><text>java</text><button class="copy-button" id="code742b" onclick="copyCode(code742, code742b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code742"><div class="highlight"><pre><span></span><span class="kt">int</span><span class="o">[]</span><span class="w"> </span><span class="n">arr</span><span class="p">;</span><span class="w"> </span><span class="c1">// Обратите внимание, размер не указан, так что мы еще не создали массив.</span>

<span class="n">arr</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="k">new</span><span class="w"> </span><span class="kt">int</span><span class="o">[</span><span class="mi">10</span><span class="o">]</span><span class="p">;</span><span class="w"> </span><span class="c1">// Новый массив размером 10.</span>

<span class="c1">// Или с указанием значений в одну строку:</span>

<span class="kt">int</span><span class="o">[]</span><span class="w"> </span><span class="n">arr</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="p">{</span><span class="mi">1</span><span class="p">,</span><span class="w"> </span><span class="mi">2</span><span class="p">,</span><span class="w"> </span><span class="mi">3</span><span class="p">,</span><span class="w"> </span><span class="mi">4</span><span class="p">,</span><span class="w"> </span><span class="mi">5</span><span class="p">};</span>


<span class="c1">// Мы можем проверить размер массива, выведя на экран его длину:</span>

<span class="n">System</span><span class="p">.</span><span class="na">out</span><span class="p">.</span><span class="na">println</span><span class="p">(</span><span class="n">arr</span><span class="p">.</span><span class="na">length</span><span class="p">);</span>

<span class="c1">// Так же мы можем получить доступ к массиву и установить значения:</span>

<span class="n">arr</span><span class="o">[</span><span class="mi">0</span><span class="o">]</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">4</span><span class="p">;</span>
<span class="n">arr</span><span class="o">[</span><span class="mi">1</span><span class="o">]</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">arr</span><span class="o">[</span><span class="mi">0</span><span class="o">]</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="mi">5</span><span class="p">;</span>
</pre></div></div></div>

<h1>Вывод значений</h1>
<p>Для вывода всех значений массива используйте метод <code>Arrays.toString()</code>, преобразующий массив в строку.</p>
<div class="code-element"><div class="lang-line"><text>java</text><button class="copy-button" id="code743b" onclick="copyCode(code743, code743b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code743"><div class="highlight"><pre><span></span><span class="n">System</span><span class="p">.</span><span class="na">out</span><span class="p">.</span><span class="na">println</span><span class="p">(</span><span class="n">Arrays</span><span class="p">.</span><span class="na">toString</span><span class="p">(</span><span class="n">arr</span><span class="p">));</span>
</pre></div></div></div>

<p>Или напишите цикл, выводящий последовательно элементы массива.</p>
<div class="code-element"><div class="lang-line"><text>java</text><button class="copy-button" id="code744b" onclick="copyCode(code744, code744b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code744"><div class="highlight"><pre><span></span><span class="k">for</span><span class="p">(</span><span class="kt">int</span><span class="w"> </span><span class="n">i</span><span class="o">=</span><span class="mi">0</span><span class="p">;</span><span class="w"> </span><span class="n">i</span><span class="o">&lt;</span><span class="n">arr</span><span class="p">.</span><span class="na">length</span><span class="p">;</span><span class="w"> </span><span class="n">i</span><span class="o">++</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="n">System</span><span class="p">.</span><span class="na">out</span><span class="p">.</span><span class="na">println</span><span class="p">(</span><span class="n">arr</span><span class="o">[</span><span class="n">i</span><span class="o">]</span><span class="p">);</span>
<span class="p">}</span>
</pre></div></div></div>