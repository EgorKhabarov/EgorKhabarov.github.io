<p>В Python, <strong>enum</strong> — это класс, используемый для создания перечислений (enumerations),
который представляет собой набор символических имен, связанных с уникальными значениями.
Модуль <code>enum</code> был добавлен в Python 3.4 и предоставляет несколько полезных типов для создания перечислений.</p>
<h1>Основные элементы</h1>
<ul>
<li><strong>Enum</strong>: Базовый класс для создания перечислений.</li>
<li><strong>IntEnum</strong>: Перечисления, значения которых — целые числа.</li>
<li><strong>Flag</strong>: Используется для создания битовых флагов, где элементы могут быть комбинированы с помощью побитовых операций.</li>
<li><strong>IntFlag</strong>: То же, что и <code>Flag</code>, но значения также являются целыми числами.</li>
</ul>
<h3>Пример использования Enum</h3>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">enum</span> <span class="kn">import</span> <span class="n">Enum</span>

<span class="k">class</span> <span class="nc">Color</span><span class="p">(</span><span class="n">Enum</span><span class="p">):</span>
    <span class="n">RED</span> <span class="o">=</span> <span class="mi">1</span>
    <span class="n">GREEN</span> <span class="o">=</span> <span class="mi">2</span>
    <span class="n">BLUE</span> <span class="o">=</span> <span class="mi">3</span>

<span class="c1"># Доступ к элементам перечисления</span>
<span class="nb">print</span><span class="p">(</span><span class="n">Color</span><span class="o">.</span><span class="n">RED</span><span class="p">)</span>          <span class="c1"># Color.RED</span>
<span class="nb">print</span><span class="p">(</span><span class="n">Color</span><span class="o">.</span><span class="n">RED</span><span class="o">.</span><span class="n">name</span><span class="p">)</span>     <span class="c1"># &quot;RED&quot;</span>
<span class="nb">print</span><span class="p">(</span><span class="n">Color</span><span class="o">.</span><span class="n">RED</span><span class="o">.</span><span class="n">value</span><span class="p">)</span>    <span class="c1"># 1</span>
</pre></div></div></div>

<h3>Пример использования IntEnum</h3>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">enum</span> <span class="kn">import</span> <span class="n">IntEnum</span>

<span class="k">class</span> <span class="nc">Status</span><span class="p">(</span><span class="n">IntEnum</span><span class="p">):</span>
    <span class="n">OK</span> <span class="o">=</span> <span class="mi">200</span>
    <span class="n">NOT_FOUND</span> <span class="o">=</span> <span class="mi">404</span>
    <span class="n">SERVER_ERROR</span> <span class="o">=</span> <span class="mi">500</span>

<span class="c1"># IntEnum позволяет использовать его как целое число</span>
<span class="nb">print</span><span class="p">(</span><span class="n">Status</span><span class="o">.</span><span class="n">OK</span> <span class="o">+</span> <span class="mi">1</span><span class="p">)</span>  <span class="c1"># 201</span>
</pre></div></div></div>

<h3>Пример использования Flag и IntFlag</h3>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">enum</span> <span class="kn">import</span> <span class="n">Flag</span><span class="p">,</span> <span class="n">IntFlag</span>

<span class="k">class</span> <span class="nc">Permission</span><span class="p">(</span><span class="n">Flag</span><span class="p">):</span>
    <span class="n">READ</span> <span class="o">=</span> <span class="mi">1</span>
    <span class="n">WRITE</span> <span class="o">=</span> <span class="mi">2</span>
    <span class="n">EXECUTE</span> <span class="o">=</span> <span class="mi">4</span>

<span class="c1"># Комбинирование флагов с помощью побитовых операций</span>
<span class="n">perm</span> <span class="o">=</span> <span class="n">Permission</span><span class="o">.</span><span class="n">READ</span> <span class="o">|</span> <span class="n">Permission</span><span class="o">.</span><span class="n">WRITE</span>
<span class="nb">print</span><span class="p">(</span><span class="n">perm</span><span class="p">)</span>  <span class="c1"># Permission.READ|WRITE</span>

<span class="c1"># IntFlag пример</span>
<span class="k">class</span> <span class="nc">Options</span><span class="p">(</span><span class="n">IntFlag</span><span class="p">):</span>
    <span class="n">OPTION1</span> <span class="o">=</span> <span class="mi">1</span>
    <span class="n">OPTION2</span> <span class="o">=</span> <span class="mi">2</span>
    <span class="n">OPTION3</span> <span class="o">=</span> <span class="mi">4</span>

<span class="n">opt</span> <span class="o">=</span> <span class="n">Options</span><span class="o">.</span><span class="n">OPTION1</span> <span class="o">|</span> <span class="n">Options</span><span class="o">.</span><span class="n">OPTION3</span>
<span class="nb">print</span><span class="p">(</span><span class="n">opt</span><span class="p">)</span>  <span class="c1"># Options.OPTION1|OPTION3</span>
</pre></div></div></div>

<h3>Методы и свойства перечислений</h3>
<table>
<thead>
<tr>
<th>Метод/Свойство</th>
<th>Описание</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>.name</code></td>
<td>Возвращает имя элемента перечисления</td>
</tr>
<tr>
<td><code>.value</code></td>
<td>Возвращает значение элемента перечисления</td>
</tr>
<tr>
<td><code>Enum(value)</code></td>
<td>Позволяет получить элемент перечисления по его значению</td>
</tr>
<tr>
<td><code>list(Enum)</code></td>
<td>Возвращает список всех элементов перечисления</td>
</tr>
<tr>
<td><code>Enum.__members__</code></td>
<td>Возвращает словарь всех членов перечисления, где ключи — имена, а значения — сами элементы</td>
</tr>
<tr>
<td><code>.auto()</code></td>
<td>Используется для автоматического назначения значений элементов. (Введен в Python 3.6)</td>
</tr>
</tbody>
</table>
<h3>Пример с использованием <code>auto()</code></h3>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">enum</span> <span class="kn">import</span> <span class="n">Enum</span><span class="p">,</span> <span class="n">auto</span>

<span class="k">class</span> <span class="nc">Animal</span><span class="p">(</span><span class="n">Enum</span><span class="p">):</span>
    <span class="n">DOG</span> <span class="o">=</span> <span class="n">auto</span><span class="p">()</span>
    <span class="n">CAT</span> <span class="o">=</span> <span class="n">auto</span><span class="p">()</span>
    <span class="n">LION</span> <span class="o">=</span> <span class="n">auto</span><span class="p">()</span>

<span class="nb">print</span><span class="p">(</span><span class="nb">list</span><span class="p">(</span><span class="n">Animal</span><span class="p">))</span>  <span class="c1"># [&lt;Animal.DOG: 1&gt;, &lt;Animal.CAT: 2&gt;, &lt;Animal.LION: 3&gt;]</span>
</pre></div></div></div>

<h3>Пользовательские методы и свойства</h3>
<p>Перечисления могут содержать методы и дополнительные свойства.
Вот пример перечисления с пользовательскими методами:</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">enum</span> <span class="kn">import</span> <span class="n">Enum</span>

<span class="k">class</span> <span class="nc">Day</span><span class="p">(</span><span class="n">Enum</span><span class="p">):</span>
    <span class="n">MONDAY</span> <span class="o">=</span> <span class="mi">1</span>
    <span class="n">TUESDAY</span> <span class="o">=</span> <span class="mi">2</span>
    <span class="n">WEDNESDAY</span> <span class="o">=</span> <span class="mi">3</span>
    <span class="n">THURSDAY</span> <span class="o">=</span> <span class="mi">4</span>
    <span class="n">FRIDAY</span> <span class="o">=</span> <span class="mi">5</span>
    <span class="n">SATURDAY</span> <span class="o">=</span> <span class="mi">6</span>
    <span class="n">SUNDAY</span> <span class="o">=</span> <span class="mi">7</span>

    <span class="k">def</span> <span class="nf">is_weekend</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="k">return</span> <span class="bp">self</span> <span class="ow">in</span> <span class="p">(</span><span class="n">Day</span><span class="o">.</span><span class="n">SATURDAY</span><span class="p">,</span> <span class="n">Day</span><span class="o">.</span><span class="n">SUNDAY</span><span class="p">)</span>

<span class="nb">print</span><span class="p">(</span><span class="n">Day</span><span class="o">.</span><span class="n">SATURDAY</span><span class="o">.</span><span class="n">is_weekend</span><span class="p">())</span>  <span class="c1"># True</span>
</pre></div></div></div>

<h3>Перегрузка операторов</h3>
<p>Можно перегружать операторы в перечислениях:</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">enum</span> <span class="kn">import</span> <span class="n">IntEnum</span>

<span class="k">class</span> <span class="nc">Level</span><span class="p">(</span><span class="n">IntEnum</span><span class="p">):</span>
    <span class="n">LOW</span> <span class="o">=</span> <span class="mi">1</span>
    <span class="n">MEDIUM</span> <span class="o">=</span> <span class="mi">2</span>
    <span class="n">HIGH</span> <span class="o">=</span> <span class="mi">3</span>

    <span class="k">def</span> <span class="fm">__ge__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">other</span><span class="p">):</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">value</span> <span class="o">&gt;=</span> <span class="n">other</span><span class="o">.</span><span class="n">value</span>

<span class="nb">print</span><span class="p">(</span><span class="n">Level</span><span class="o">.</span><span class="n">HIGH</span> <span class="o">&gt;=</span> <span class="n">Level</span><span class="o">.</span><span class="n">MEDIUM</span><span class="p">)</span>  <span class="c1"># True</span>
</pre></div></div></div>

<h3>Поддержка итерации</h3>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="k">for</span> <span class="n">color</span> <span class="ow">in</span> <span class="n">Color</span><span class="p">:</span>
    <span class="nb">print</span><span class="p">(</span><span class="n">color</span><span class="p">)</span>
<span class="c1"># Color.RED</span>
<span class="c1"># Color.GREEN</span>
<span class="c1"># Color.BLUE</span>
</pre></div></div></div>

<h3>Ошибки при работе с Enum</h3>
<ul>
<li><strong>ValueError</strong>: Возникает, если обратиться к несуществующему значению.</li>
</ul>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="n">Color</span><span class="p">(</span><span class="mi">10</span><span class="p">))</span>  <span class="c1"># ValueError: 10 is not a valid Color</span>
</pre></div></div></div>

<ul>
<li><strong>AttributeError</strong>: Возникает при обращении к несуществующему члену перечисления.</li>
</ul>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="n">Color</span><span class="o">.</span><span class="n">YELLOW</span><span class="p">)</span>  <span class="c1"># AttributeError: YELLOW</span>
</pre></div></div></div>

<h3>Особенности использования</h3>
<ul>
<li><strong>Перечисления неизменяемы</strong>: Невозможно присваивать новые значения или изменять существующие.</li>
<li><strong>Перечисления можно использовать как ключи словарей</strong>, так как они неизменяемы и хешируемы.</li>
</ul>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="n">status_codes</span> <span class="o">=</span> <span class="p">{</span>
    <span class="n">Status</span><span class="o">.</span><span class="n">OK</span><span class="p">:</span> <span class="s2">&quot;Success&quot;</span><span class="p">,</span>
    <span class="n">Status</span><span class="o">.</span><span class="n">NOT_FOUND</span><span class="p">:</span> <span class="s2">&quot;Not Found&quot;</span><span class="p">,</span>
    <span class="n">Status</span><span class="o">.</span><span class="n">SERVER_ERROR</span><span class="p">:</span> <span class="s2">&quot;Internal Server Error&quot;</span>
<span class="p">}</span>

<span class="nb">print</span><span class="p">(</span><span class="n">status_codes</span><span class="p">[</span><span class="n">Status</span><span class="o">.</span><span class="n">OK</span><span class="p">])</span>  <span class="c1"># &quot;Success&quot;</span>
</pre></div></div></div>

<h3>Итоги</h3>
<ul>
<li><strong>Enum</strong> — базовый класс для создания перечислений.</li>
<li><strong>IntEnum</strong> — перечисления, которые также могут использоваться как целые числа.</li>
<li><strong>Flag и IntFlag</strong> — позволяют создавать флаги, которые можно комбинировать с помощью побитовых операций.</li>
<li>Перечисления могут содержать пользовательские методы и перегружать операторы.</li>
</ul>