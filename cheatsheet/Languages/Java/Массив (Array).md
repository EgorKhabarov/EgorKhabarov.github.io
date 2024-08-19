<ul>
<li><strong><code>Массив (array)</code></strong> — это структура данных фиксированного размера</li>
<li><strong><code>Список (list)</code></strong> — это интерфейс в Java, который представляет динамическую структуру данных, размер которой может изменяться.</li>
</ul>
<div class="code_element"><div class="lang_line"><text>java</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code"><div class="highlight"><pre><span></span><span class="c1">// Создание пустого массива</span>
<span class="kt">char</span><span class="o">[]</span><span class="w"> </span><span class="n">stroka</span><span class="p">;</span>
<span class="c1">// Или</span>
<span class="kt">int</span><span class="w"> </span><span class="n">numbers</span><span class="o">[]</span><span class="p">;</span>
<span class="n">numbers</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="k">new</span><span class="w"> </span><span class="kt">int</span><span class="o">[</span><span class="mi">10</span><span class="o">]</span><span class="p">;</span>

<span class="kt">int</span><span class="o">[]</span><span class="w"> </span><span class="n">nums</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="k">new</span><span class="w"> </span><span class="kt">int</span><span class="o">[</span><span class="mi">4</span><span class="o">]</span><span class="p">;</span>
<span class="n">nums</span><span class="o">[</span><span class="mi">0</span><span class="o">]</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">1</span><span class="p">;</span>

<span class="kt">int</span><span class="o">[]</span><span class="w"> </span><span class="n">nums2</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="k">new</span><span class="w"> </span><span class="kt">int</span><span class="o">[]</span><span class="w"> </span><span class="p">{</span><span class="w"> </span><span class="mi">1</span><span class="p">,</span><span class="w"> </span><span class="mi">2</span><span class="p">,</span><span class="w"> </span><span class="mi">3</span><span class="p">,</span><span class="w"> </span><span class="mi">5</span><span class="w"> </span><span class="p">};</span>
<span class="kt">int</span><span class="o">[]</span><span class="w"> </span><span class="n">nums3</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="p">{</span><span class="w"> </span><span class="mi">1</span><span class="p">,</span><span class="w"> </span><span class="mi">2</span><span class="p">,</span><span class="w"> </span><span class="mi">3</span><span class="p">,</span><span class="w"> </span><span class="mi">5</span><span class="w"> </span><span class="p">};</span>

<span class="n">System</span><span class="p">.</span><span class="na">out</span><span class="p">.</span><span class="na">println</span><span class="p">(</span><span class="n">Arrays</span><span class="p">.</span><span class="na">toString</span><span class="p">(</span><span class="n">nums3</span><span class="p">));</span>
<span class="n">System</span><span class="p">.</span><span class="na">out</span><span class="p">.</span><span class="na">println</span><span class="p">(</span><span class="n">nums3</span><span class="p">.</span><span class="na">length</span><span class="p">);</span>

<span class="n">System</span><span class="p">.</span><span class="na">out</span><span class="p">.</span><span class="na">println</span><span class="p">(</span><span class="n">Arrays</span><span class="p">.</span><span class="na">toString</span><span class="p">(</span><span class="k">new</span><span class="w"> </span><span class="kt">int</span><span class="o">[]</span><span class="w"> </span><span class="p">{</span><span class="w"> </span><span class="mi">1</span><span class="p">,</span><span class="w"> </span><span class="mi">2</span><span class="p">,</span><span class="w"> </span><span class="mi">3</span><span class="p">,</span><span class="w"> </span><span class="mi">5</span><span class="w"> </span><span class="p">}));</span>
<span class="n">System</span><span class="p">.</span><span class="na">out</span><span class="p">.</span><span class="na">println</span><span class="p">(</span><span class="k">new</span><span class="w"> </span><span class="kt">int</span><span class="o">[]</span><span class="w"> </span><span class="p">{</span><span class="w"> </span><span class="mi">1</span><span class="p">,</span><span class="w"> </span><span class="mi">2</span><span class="p">,</span><span class="w"> </span><span class="mi">3</span><span class="p">,</span><span class="w"> </span><span class="mi">5</span><span class="w"> </span><span class="p">}.</span><span class="na">length</span><span class="p">);</span>
</pre></div></div></div>

<h1>Вывод значений</h1>
<p>Для вывода всех значений массива используйте метод <code>Arrays.toString()</code>, преобразующий массив в строку.</p>
<div class="code_element"><div class="lang_line"><text>java</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code"><div class="highlight"><pre><span></span><span class="kn">import</span><span class="w"> </span><span class="nn">java.util.Arrays</span><span class="p">;</span>
</pre></div></div></div>
<div class="code_element"><div class="lang_line"><text>java</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code"><div class="highlight"><pre><span></span><span class="n">System</span><span class="p">.</span><span class="na">out</span><span class="p">.</span><span class="na">println</span><span class="p">(</span><span class="n">Arrays</span><span class="p">.</span><span class="na">toString</span><span class="p">(</span><span class="n">arr</span><span class="p">));</span>
</pre></div></div></div>

<p>Или напишите цикл, выводящий последовательно элементы массива.</p>
<div class="code_element"><div class="lang_line"><text>java</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code"><div class="highlight"><pre><span></span><span class="k">for</span><span class="p">(</span><span class="kt">int</span><span class="w"> </span><span class="n">i</span><span class="o">=</span><span class="mi">0</span><span class="p">;</span><span class="w"> </span><span class="n">i</span><span class="o">&lt;</span><span class="n">arr</span><span class="p">.</span><span class="na">length</span><span class="p">;</span><span class="w"> </span><span class="n">i</span><span class="o">++</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="n">System</span><span class="p">.</span><span class="na">out</span><span class="p">.</span><span class="na">println</span><span class="p">(</span><span class="n">arr</span><span class="o">[</span><span class="n">i</span><span class="o">]</span><span class="p">);</span>
<span class="p">}</span>
<span class="c1">// Или</span>
<span class="k">for</span><span class="w"> </span><span class="p">(</span><span class="kt">int</span><span class="w"> </span><span class="n">el</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="n">arr</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="n">System</span><span class="p">.</span><span class="na">out</span><span class="p">.</span><span class="na">println</span><span class="p">(</span><span class="n">el</span><span class="p">);</span>
<span class="p">}</span>
</pre></div></div></div>

<h1>Многомерный массив</h1>
<div class="code_element"><div class="lang_line"><text>java</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code"><div class="highlight"><pre><span></span><span class="kt">int</span><span class="o">[][]</span><span class="w"> </span><span class="n">x</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="p">{</span><span class="w"> </span><span class="p">{</span><span class="w"> </span><span class="mi">0</span><span class="p">,</span><span class="w"> </span><span class="mi">1</span><span class="p">,</span><span class="w"> </span><span class="mi">2</span><span class="w"> </span><span class="p">},</span><span class="w"> </span><span class="p">{</span><span class="w"> </span><span class="mi">3</span><span class="p">,</span><span class="w"> </span><span class="mi">4</span><span class="p">,</span><span class="w"> </span><span class="mi">5</span><span class="w"> </span><span class="p">}</span><span class="w"> </span><span class="p">};</span>
</pre></div></div></div>

<p><img alt="collections.jpg" src="Languages/Java/collections.jpg" /></p>
<p>Основные коллекции
Помимо главного интерфейса Collection есть три других главных формата:</p>
<ul>
<li><code>List</code> - коллекция для создания массивов данных, где индексами являются числа (0, 1, 2 и так далее);</li>
<li><code>Set</code> - тоже самое что <code>List</code>, вот только в <code>Set</code> нельзя установить повторяющиеся элементы;</li>
<li><code>Map</code> - коллекция для создания массивов данных, где индексами являются ключи ("one", "2", "three" и так далее).</li>
</ul>
<div class="code_element"><div class="lang_line"><text>java</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code"><div class="highlight"><pre><span></span><span class="kn">import</span><span class="w"> </span><span class="nn">java.util.LinkedList</span><span class="p">;</span>
<span class="kn">import</span><span class="w"> </span><span class="nn">java.util.ArrayList</span><span class="p">;</span>


<span class="kd">public</span><span class="w"> </span><span class="kd">class</span> <span class="nc">Main</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="kd">public</span><span class="w"> </span><span class="kd">static</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="nf">main</span><span class="p">(</span><span class="n">String</span><span class="o">[]</span><span class="w"> </span><span class="n">args</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">        </span><span class="n">ArrayList</span><span class="o">&lt;</span><span class="n">Float</span><span class="o">&gt;</span><span class="w"> </span><span class="n">numbers</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="k">new</span><span class="w"> </span><span class="n">ArrayList</span><span class="o">&lt;&gt;</span><span class="p">(</span><span class="mi">1</span><span class="p">);</span><span class="w">  </span><span class="c1">// 1 (initialCapacity) можно не указывать</span>
<span class="w">        </span><span class="n">LinkedList</span><span class="o">&lt;</span><span class="n">String</span><span class="o">&gt;</span><span class="w"> </span><span class="n">names</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="k">new</span><span class="w"> </span><span class="n">LinkedList</span><span class="o">&lt;&gt;</span><span class="p">();</span>
<span class="w">    </span><span class="p">}</span>
<span class="p">}</span>
</pre></div></div></div>

<ul>
<li><code>add()</code> - добавление элемента в конец массива;</li>
<li><code>remove()</code> - удаление элемента из массива по его индексу;</li>
<li><code>clear()</code> - очистка всего массива;</li>
<li><code>size()</code> - получение размера массива (количество элементов);</li>
<li><code>addFirst()</code> - добавление элемента в начало массива;</li>
<li><code>addLast()</code> - добавление элемента в конец;</li>
<li><code>clone()</code> - выполняет клонирование массива;</li>
<li><code>get()</code> - возвращает элемент по индексу;</li>
<li><code>getFirst()</code> - возвращает первый элемент в массиве;</li>
<li><code>getLast()</code> - возвращает последний элемент в массиве;</li>
<li><code>set(index, element)</code> - меняет значение элемента по индексу.</li>
</ul>
<div class="code_element"><div class="lang_line"><text>java</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code"><div class="highlight"><pre><span></span><span class="n">List</span><span class="o">&lt;</span><span class="n">Object</span><span class="o">&gt;</span><span class="w"> </span><span class="n">items</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="k">new</span><span class="w"> </span><span class="n">ArrayList</span><span class="o">&lt;&gt;</span><span class="p">();</span>
<span class="n">items</span><span class="p">.</span><span class="na">add</span><span class="p">(</span><span class="s">&quot;Hello&quot;</span><span class="p">);</span>
<span class="n">items</span><span class="p">.</span><span class="na">add</span><span class="p">(</span><span class="mi">42</span><span class="p">);</span>
<span class="n">items</span><span class="p">.</span><span class="na">add</span><span class="p">(</span><span class="mf">3.14</span><span class="p">);</span>
<span class="n">items</span><span class="p">.</span><span class="na">add</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span><span class="w"> </span><span class="mf">3.14</span><span class="p">);</span>
<span class="n">items</span><span class="p">.</span><span class="na">add</span><span class="p">(</span><span class="mi">2</span><span class="p">,</span><span class="w"> </span><span class="mf">3.14</span><span class="p">);</span>

<span class="n">System</span><span class="p">.</span><span class="na">out</span><span class="p">.</span><span class="na">println</span><span class="p">(</span><span class="n">items</span><span class="p">.</span><span class="na">get</span><span class="p">(</span><span class="mi">0</span><span class="p">));</span>
<span class="c1">// System.out.println(items.get(-1)); // Index -1 out of bounds for length 5</span>
<span class="n">System</span><span class="p">.</span><span class="na">out</span><span class="p">.</span><span class="na">println</span><span class="p">(</span><span class="n">items</span><span class="p">.</span><span class="na">size</span><span class="p">());</span>
<span class="k">for</span><span class="w"> </span><span class="p">(</span><span class="n">Object</span><span class="w"> </span><span class="n">item</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="n">items</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="n">System</span><span class="p">.</span><span class="na">out</span><span class="p">.</span><span class="na">println</span><span class="p">(</span><span class="n">item</span><span class="p">);</span>
<span class="p">}</span>
</pre></div></div></div>
<div class="code_element"><div class="lang_line"><text>output</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code"><div class="highlight"><pre><span></span><span class="go">5</span>
<span class="go">3.14</span>
<span class="go">Hello</span>
<span class="go">3.14</span>
<span class="go">42</span>
<span class="go">3.14</span>
</pre></div></div></div>