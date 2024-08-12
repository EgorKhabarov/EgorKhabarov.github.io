<p>Библиотека "jsonschema" используется для валидации данных в формате JSON по схеме.
Она позволяет проверить, соответствуют ли данные определенным правилам и структуре, заданным в JSON-схеме.</p>
<p>Таблица методов модуля "jsonschema" и их краткое описание:</p>
<table>
<thead>
<tr>
<th>Метод</th>
<th>Описание</th>
</tr>
</thead>
<tbody>
<tr>
<td>validate</td>
<td>Проверяет, соответствуют ли данные схеме.</td>
</tr>
<tr>
<td>Draft4Validator</td>
<td>Класс, осуществляющий валидацию на основе JSON-схемы в соответствии с разделом 4 стандарта.</td>
</tr>
<tr>
<td>Draft6Validator</td>
<td>Класс, осуществляющий валидацию на основе JSON-схемы в соответствии с разделом 6 стандарта.</td>
</tr>
<tr>
<td>Draft7Validator</td>
<td>Класс, осуществляющий валидацию на основе JSON-схемы в соответствии с разделом 7 стандарта.</td>
</tr>
<tr>
<td>ValidationError</td>
<td>Класс исключения, возникающего при невалидных данных.</td>
</tr>
<tr>
<td>exceptions</td>
<td>Подмодуль, содержащий различные классы исключений.</td>
</tr>
</tbody>
</table>
<p>Список самых часто используемых методов "jsonschema" и их краткое описание:</p>
<p><code>validate(schema, instance)</code> - Проверяет, соответствуют ли данные <code>instance</code> схеме <code>schema</code>.
Возвращает <code>None</code>, если данные валидны. В противном случае, возникает исключение <code>ValidationError</code>.</p>
<div class="code-element">
    <div class="lang-line">
        <text>python</text>
        <button class="copy-button"
        onclick="copyCode(this)">
    <svg stroke="currentColor"
         fill="none"
         stroke-width="2"
         viewBox="0 0 24 24"
         stroke-linecap="round"
         stroke-linejoin="round"
         class="h-4 w-4"
         height="1em"
         width="1em"
         xmlns="http://www.w3.org/2000/svg">
        <path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path>
        <rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect>
    </svg>
    <text>Copy code</text>
</button>

    </div>
    <div class="code"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">jsonschema</span> <span class="kn">import</span> <span class="n">validate</span>

<span class="n">schema</span> <span class="o">=</span> <span class="p">{</span>
    <span class="s2">&quot;type&quot;</span><span class="p">:</span> <span class="s2">&quot;object&quot;</span><span class="p">,</span>
    <span class="s2">&quot;properties&quot;</span><span class="p">:</span> <span class="p">{</span>
        <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="p">{</span><span class="s2">&quot;type&quot;</span><span class="p">:</span> <span class="s2">&quot;string&quot;</span><span class="p">},</span>
        <span class="s2">&quot;age&quot;</span><span class="p">:</span> <span class="p">{</span><span class="s2">&quot;type&quot;</span><span class="p">:</span> <span class="s2">&quot;integer&quot;</span><span class="p">}</span>
    <span class="p">}</span>
<span class="p">}</span>

<span class="n">data</span> <span class="o">=</span> <span class="p">{</span>
    <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;John&quot;</span><span class="p">,</span>
    <span class="s2">&quot;age&quot;</span><span class="p">:</span> <span class="mi">25</span>
<span class="p">}</span>

<span class="k">try</span><span class="p">:</span>
    <span class="n">validate</span><span class="p">(</span><span class="n">schema</span><span class="p">,</span> <span class="n">data</span><span class="p">)</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Data is valid.&quot;</span><span class="p">)</span>
<span class="k">except</span> <span class="n">ValidationError</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Data is invalid:&quot;</span><span class="p">,</span> <span class="n">e</span><span class="p">)</span>
</pre></div></div>
</div>

<p><code>Draft4Validator(schema)</code> - Создает экземпляр валидатора на основе JSON-схемы с использованием стандарта Draft 4.
Используется для последующей валидации данных.</p>
<div class="code-element">
    <div class="lang-line">
        <text>python</text>
        <button class="copy-button"
        onclick="copyCode(this)">
    <svg stroke="currentColor"
         fill="none"
         stroke-width="2"
         viewBox="0 0 24 24"
         stroke-linecap="round"
         stroke-linejoin="round"
         class="h-4 w-4"
         height="1em"
         width="1em"
         xmlns="http://www.w3.org/2000/svg">
        <path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path>
        <rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect>
    </svg>
    <text>Copy code</text>
</button>

    </div>
    <div class="code"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">jsonschema</span> <span class="kn">import</span> <span class="n">Draft4Validator</span>

<span class="n">schema</span> <span class="o">=</span> <span class="p">{</span>
    <span class="s2">&quot;type&quot;</span><span class="p">:</span> <span class="s2">&quot;object&quot;</span><span class="p">,</span>
    <span class="s2">&quot;properties&quot;</span><span class="p">:</span> <span class="p">{</span>
        <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="p">{</span><span class="s2">&quot;type&quot;</span><span class="p">:</span> <span class="s2">&quot;string&quot;</span><span class="p">},</span>
        <span class="s2">&quot;age&quot;</span><span class="p">:</span> <span class="p">{</span><span class="s2">&quot;type&quot;</span><span class="p">:</span> <span class="s2">&quot;integer&quot;</span><span class="p">}</span>
    <span class="p">}</span>
<span class="p">}</span>

<span class="n">validator</span> <span class="o">=</span> <span class="n">Draft4Validator</span><span class="p">(</span><span class="n">schema</span><span class="p">)</span>

<span class="n">data</span> <span class="o">=</span> <span class="p">{</span>
    <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;John&quot;</span><span class="p">,</span>
    <span class="s2">&quot;age&quot;</span><span class="p">:</span> <span class="mi">25</span>
<span class="p">}</span>

<span class="k">for</span> <span class="n">error</span> <span class="ow">in</span> <span class="n">validator</span><span class="o">.</span><span class="n">iter_errors</span><span class="p">(</span><span class="n">data</span><span class="p">):</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Validation error:&quot;</span><span class="p">,</span> <span class="n">error</span><span class="o">.</span><span class="n">message</span><span class="p">)</span>
</pre></div></div>
</div>