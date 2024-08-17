<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-code-button" onclick="copyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">dataclasses</span> <span class="kn">import</span> <span class="n">dataclass</span>
</pre></div></div></div>

<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-code-button" onclick="copyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="nd">@dataclass</span><span class="p">(</span>
    <span class="o">*</span><span class="p">,</span>
    <span class="n">init</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="o">...</span><span class="p">,</span>
    <span class="nb">repr</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="o">...</span><span class="p">,</span>
    <span class="n">eq</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="o">...</span><span class="p">,</span>
    <span class="n">order</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="o">...</span><span class="p">,</span>
    <span class="n">unsafe_hash</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="o">...</span><span class="p">,</span>
    <span class="n">frozen</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="o">...</span><span class="p">,</span>
<span class="p">)</span>
</pre></div></div></div>

<table>
<thead>
<tr>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>init</td>
<td>Нужно ли автоматически генерировать метод <code>__init__</code> для инициализации атрибутов класса.</td>
</tr>
<tr>
<td>repr</td>
<td>Нужно ли автоматически генерировать метод <code>__repr__</code> для вывода строкового представления объектов класса.</td>
</tr>
<tr>
<td>eq</td>
<td>Нужно ли автоматически генерировать метод <code>__eq__</code> для сравнения объектов класса.</td>
</tr>
<tr>
<td>order</td>
<td>Нужно ли автоматически генерировать методы <code>__lt__</code>, <code>__le__</code>, <code>__gt__</code>, <code>__ge__</code> для сравнения объектов класса.</td>
</tr>
<tr>
<td>unsafe_hash</td>
<td>Нужно ли автоматически генерировать метод <code>__hash__</code> для объектов класса.<br>Обычно этот аргумент следует использовать только для классов, объекты которых неизменяемы <code>frozen</code>,<br>так как изменяемые объекты могут привести к неожиданным результатам.</td>
</tr>
<tr>
<td>frozen</td>
<td>Нужно ли сделать объекты класса неизменяемыми <code>immutable</code>.</td>
</tr>
</tbody>
</table>
<p>Значения по умолчанию</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-code-button" onclick="copyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="nd">@dataclass</span><span class="p">(</span>
    <span class="o">*</span><span class="p">,</span>
    <span class="n">init</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
    <span class="nb">repr</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
    <span class="n">eq</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
    <span class="n">order</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
    <span class="n">unsafe_hash</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
    <span class="n">frozen</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
<span class="p">)</span>
</pre></div></div></div>