<p>Библиотека "marshal" в Python используется для сериализации и десериализации объектов.
Она предоставляет функциональность для сохранения объектов в бинарном формате и восстановления их позже.</p>
<p>Методы модуля "marshal" и их краткое описание:
<code>dump(obj, file)</code> - Сериализует объект <code>obj</code> и записывает его в файл <code>file</code>.
<code>load(file)</code> - Читает сериализованные данные из файла <code>file</code> и восстанавливает объект.
<code>dumps(obj)</code> - Возвращает сериализованное представление объекта <code>obj</code> в виде строки.
<code>loads(bytes)</code> - Восстанавливает объект из сериализованного представления, передаваемого в виде строки <code>bytes</code>.
<code>version</code> - Целое число, представляющее версию протокола сериализации.</p>
<p>Наиболее распространенные методы "marshal" и их описание:</p>
<p><code>dump(obj, file)</code> - Сериализует объект <code>obj</code> и записывает его в файл <code>file</code>.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">marshal</span>

<span class="n">data</span> <span class="o">=</span> <span class="p">{</span><span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;John&quot;</span><span class="p">,</span> <span class="s2">&quot;age&quot;</span><span class="p">:</span> <span class="mi">30</span><span class="p">}</span>
<span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="s2">&quot;data.bin&quot;</span><span class="p">,</span> <span class="s2">&quot;wb&quot;</span><span class="p">)</span> <span class="k">as</span> <span class="n">file</span><span class="p">:</span>
    <span class="n">marshal</span><span class="o">.</span><span class="n">dump</span><span class="p">(</span><span class="n">data</span><span class="p">,</span> <span class="n">file</span><span class="p">)</span>
</pre></div></div></div>

<p><code>load(file)</code> - Читает сериализованные данные из файла <code>file</code> и восстанавливает объект.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">marshal</span>

<span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="s2">&quot;data.bin&quot;</span><span class="p">,</span> <span class="s2">&quot;rb&quot;</span><span class="p">)</span> <span class="k">as</span> <span class="n">file</span><span class="p">:</span>
    <span class="n">data</span> <span class="o">=</span> <span class="n">marshal</span><span class="o">.</span><span class="n">load</span><span class="p">(</span><span class="n">file</span><span class="p">)</span>
    <span class="nb">print</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>  <span class="c1"># Вывод: {&quot;name&quot;: &quot;John&quot;, &quot;age&quot;: 30}</span>
</pre></div></div></div>

<p><code>dumps(obj)</code> - Возвращает сериализованное представление объекта <code>obj</code> в виде строки.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">marshal</span>

<span class="n">data</span> <span class="o">=</span> <span class="p">{</span><span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;John&quot;</span><span class="p">,</span> <span class="s2">&quot;age&quot;</span><span class="p">:</span> <span class="mi">30</span><span class="p">}</span>
<span class="n">serialized</span> <span class="o">=</span> <span class="n">marshal</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">serialized</span><span class="p">)</span>
</pre></div></div></div>

<p><code>loads(bytes)</code> - Восстанавливает объект из сериализованного представления, передаваемого в виде строки <code>bytes</code>.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">marshal</span>

<span class="n">serialized</span> <span class="o">=</span> <span class="p">(</span>
    <span class="sa">b</span><span class="s2">&quot;</span><span class="se">\x80\x04\x95\x0f\x00\x00\x00\x00\x00\x00\x8c\x08\x00\x00\x00</span><span class="s2">Hello!&quot;</span>
    <span class="sa">b</span><span class="s2">&quot;</span><span class="se">\x94\x8c\x01\x00\x00\x00</span><span class="s2">x</span><span class="se">\x94\x8c\x01\x00\x00\x00</span><span class="s2">y</span><span class="se">\x94\x2e\x94\x94</span><span class="s2">&quot;</span>
    <span class="sa">b</span><span class="s2">&quot;</span><span class="se">\x8c\x06\x00\x00\x00</span><span class="s2">result</span><span class="se">\x94\x94\x8c\x05\x00\x00\x00</span><span class="s2">float</span><span class="se">\x94\x93\x00\x00\x00\x00\x00\x00\x00</span><span class="s2">.&quot;</span>
<span class="p">)</span>

<span class="n">data</span> <span class="o">=</span> <span class="n">marshal</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span><span class="n">serialized</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>  <span class="c1"># Вывод: {&quot;Hello!&quot;: {&quot;x&quot;: &quot;y&quot;, &quot;result&quot;: None, &quot;float&quot;: 0.0}}</span>
</pre></div></div></div>