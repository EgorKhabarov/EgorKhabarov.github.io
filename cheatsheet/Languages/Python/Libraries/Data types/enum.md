<h2>Классы</h2>
<table>
<thead>
<tr>
<th>Элемент</th>
<th>Описание</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>Enum</code></td>
<td>Базовый класс для создания перечислений</td>
</tr>
<tr>
<td><code>IntEnum</code></td>
<td>Подкласс <code>Enum</code>, значения должны быть целыми числами <code>int</code></td>
</tr>
<tr>
<td><code>StrEnum</code></td>
<td>Подкласс <code>Enum</code>, значения должны быть строками <code>str</code> (Начиная с <em>Python 3.11</em>)</td>
</tr>
<tr>
<td><code>Flag</code></td>
<td>Класс для битовых флагов. Позволяет комбинировать значения с помощью битовых операций</td>
</tr>
<tr>
<td><code>IntFlag</code></td>
<td>Подкласс <code>Flag</code>, значения должны быть целыми числами <code>int</code></td>
</tr>
</tbody>
</table>
<h2>Функции и атрибуты</h2>
<table>
<thead>
<tr>
<th>Элемент</th>
<th>Описание</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>auto()</code></td>
<td>Функция для автоматической генерации значений перечисления</td>
</tr>
<tr>
<td><code>unique()</code></td>
<td>Декоратор, который гарантирует, что все элементы перечисления имеют уникальные значения</td>
</tr>
<tr>
<td><code>EnumMeta</code></td>
<td>Метакласс для создания перечислений</td>
</tr>
<tr>
<td><code>Enum.__members__</code></td>
<td>Возвращает словарь, содержащий все члены перечисления в порядке их определения</td>
</tr>
<tr>
<td><code>Enum.__name__</code></td>
<td>Возвращает имя перечисления</td>
</tr>
<tr>
<td><code>Enum.value</code></td>
<td>Возвращает значение элемента перечисления</td>
</tr>
<tr>
<td><code>Enum.name</code></td>
<td>Возвращает имя элемента перечисления</td>
</tr>
</tbody>
</table>
<h3>Enum</h3>
<p>Создание перечисления с именованными константами</p>
<div class="code_element"><div class="lang_line"><text>pycon</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-pycon"><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="kn">from</span> <span class="nn">enum</span> <span class="kn">import</span> <span class="n">Enum</span>
<span class="unselectable"><span class="gp">&gt;&gt;&gt;</span></span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="k">class</span> <span class="nc">Color</span><span class="p">(</span><span class="n">Enum</span><span class="p">):</span>
<span class="unselectable"><span class="o">...</span> </span>    <span class="n">RED</span> <span class="o">=</span> <span class="mi">1</span>
<span class="unselectable"><span class="o">...</span> </span>    <span class="n">GREEN</span> <span class="o">=</span> <span class="mi">2</span>
<span class="unselectable"><span class="o">...</span> </span>    <span class="n">BLUE</span> <span class="o">=</span> <span class="mi">3</span>
<span class="unselectable"><span class="gp">...</span></span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="nb">print</span><span class="p">(</span><span class="n">Color</span><span class="o">.</span><span class="n">RED</span><span class="p">)</span>
<span class="unselectable"><span class="go">Color.RED</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="nb">print</span><span class="p">(</span><span class="n">Color</span><span class="o">.</span><span class="n">RED</span><span class="o">.</span><span class="n">name</span><span class="p">)</span>
<span class="unselectable"><span class="go">RED</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="nb">print</span><span class="p">(</span><span class="n">Color</span><span class="o">.</span><span class="n">RED</span><span class="o">.</span><span class="n">value</span><span class="p">)</span>
<span class="unselectable"><span class="go">1</span>
</span></pre></div></div></div>

<h3>IntEnum</h3>
<p>Перечисление с целочисленными значениями</p>
<div class="code_element"><div class="lang_line"><text>pycon</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-pycon"><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="kn">from</span> <span class="nn">enum</span> <span class="kn">import</span> <span class="n">IntEnum</span>
<span class="unselectable"><span class="gp">&gt;&gt;&gt;</span></span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="k">class</span> <span class="nc">Status</span><span class="p">(</span><span class="n">IntEnum</span><span class="p">):</span>
<span class="unselectable"><span class="o">...</span> </span>    <span class="n">ACTIVE</span> <span class="o">=</span> <span class="mi">1</span>
<span class="unselectable"><span class="o">...</span> </span>    <span class="n">INACTIVE</span> <span class="o">=</span> <span class="mi">0</span>
<span class="unselectable"><span class="gp">...</span></span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="nb">print</span><span class="p">(</span><span class="n">Status</span><span class="o">.</span><span class="n">ACTIVE</span> <span class="o">==</span> <span class="mi">1</span><span class="p">)</span>
<span class="unselectable"><span class="go">True</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="nb">print</span><span class="p">(</span><span class="n">Status</span><span class="o">.</span><span class="n">INACTIVE</span> <span class="o">+</span> <span class="mi">1</span><span class="p">)</span>
<span class="unselectable"><span class="go">1</span>
</span></pre></div></div></div>

<h3>StrEnum <em>(Python 3.11+)</em></h3>
<p>Перечисление со строковыми значениями</p>
<div class="code_element"><div class="lang_line"><text>pycon</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-pycon"><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="kn">from</span> <span class="nn">enum</span> <span class="kn">import</span> <span class="n">StrEnum</span>
<span class="unselectable"><span class="gp">&gt;&gt;&gt;</span></span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="k">class</span> <span class="nc">Role</span><span class="p">(</span><span class="n">StrEnum</span><span class="p">):</span>
<span class="unselectable"><span class="o">...</span> </span>    <span class="n">ADMIN</span> <span class="o">=</span> <span class="s2">&quot;admin&quot;</span>
<span class="unselectable"><span class="o">...</span> </span>    <span class="n">USER</span> <span class="o">=</span> <span class="s2">&quot;user&quot;</span>
<span class="unselectable"><span class="gp">...</span></span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="nb">print</span><span class="p">(</span><span class="n">Role</span><span class="o">.</span><span class="n">ADMIN</span><span class="o">.</span><span class="n">value</span><span class="p">,</span> <span class="n">Role</span><span class="o">.</span><span class="n">ADMIN</span><span class="o">.</span><span class="n">value</span> <span class="o">==</span> <span class="s2">&quot;admin&quot;</span><span class="p">)</span>
<span class="unselectable"><span class="go">admin True</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="nb">print</span><span class="p">(</span><span class="n">Role</span><span class="o">.</span><span class="n">USER</span><span class="p">,</span> <span class="n">Role</span><span class="o">.</span><span class="n">USER</span> <span class="o">==</span> <span class="s2">&quot;user&quot;</span><span class="p">)</span>
<span class="unselectable"><span class="go">user True</span>
</span></pre></div></div></div>

<h3>Flag</h3>
<p>Битовые флаги</p>
<div class="code_element"><div class="lang_line"><text>pycon</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-pycon"><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="kn">from</span> <span class="nn">enum</span> <span class="kn">import</span> <span class="n">Flag</span><span class="p">,</span> <span class="n">auto</span>
<span class="unselectable"><span class="gp">&gt;&gt;&gt;</span></span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="k">class</span> <span class="nc">Permission</span><span class="p">(</span><span class="n">Flag</span><span class="p">):</span>
<span class="unselectable"><span class="o">...</span> </span>    <span class="n">READ</span> <span class="o">=</span> <span class="n">auto</span><span class="p">()</span>
<span class="unselectable"><span class="o">...</span> </span>    <span class="n">WRITE</span> <span class="o">=</span> <span class="n">auto</span><span class="p">()</span>
<span class="unselectable"><span class="o">...</span> </span>    <span class="n">EXECUTE</span> <span class="o">=</span> <span class="n">auto</span><span class="p">()</span>
<span class="unselectable"><span class="gp">...</span></span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="n">combined</span> <span class="o">=</span> <span class="n">Permission</span><span class="o">.</span><span class="n">READ</span> <span class="o">|</span> <span class="n">Permission</span><span class="o">.</span><span class="n">WRITE</span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="nb">print</span><span class="p">(</span><span class="n">combined</span><span class="p">)</span>
<span class="unselectable"><span class="go">Permission.READ|WRITE</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="nb">print</span><span class="p">(</span><span class="n">combined</span> <span class="o">&amp;</span> <span class="n">Permission</span><span class="o">.</span><span class="n">READ</span><span class="p">)</span>
<span class="unselectable"><span class="go">Permission.READ</span>
</span></pre></div></div></div>

<h3>IntFlag</h3>
<p>Битовые флаги с целыми числами</p>
<div class="code_element"><div class="lang_line"><text>pycon</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-pycon"><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="kn">from</span> <span class="nn">enum</span> <span class="kn">import</span> <span class="n">IntFlag</span>
<span class="unselectable"><span class="gp">&gt;&gt;&gt;</span></span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="k">class</span> <span class="nc">Options</span><span class="p">(</span><span class="n">IntFlag</span><span class="p">):</span>
<span class="unselectable"><span class="o">...</span> </span>    <span class="n">OPTION1</span> <span class="o">=</span> <span class="mi">1</span>
<span class="unselectable"><span class="o">...</span> </span>    <span class="n">OPTION2</span> <span class="o">=</span> <span class="mi">2</span>
<span class="unselectable"><span class="o">...</span> </span>    <span class="n">OPTION3</span> <span class="o">=</span> <span class="mi">4</span>
<span class="unselectable"><span class="gp">...</span></span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="n">combo</span> <span class="o">=</span> <span class="n">Options</span><span class="o">.</span><span class="n">OPTION1</span> <span class="o">|</span> <span class="n">Options</span><span class="o">.</span><span class="n">OPTION3</span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="nb">print</span><span class="p">(</span><span class="n">combo</span><span class="p">,</span> <span class="n">combo</span> <span class="o">==</span> <span class="n">Options</span><span class="o">.</span><span class="n">OPTION1</span> <span class="o">|</span> <span class="n">Options</span><span class="o">.</span><span class="n">OPTION3</span><span class="p">)</span>
<span class="unselectable"><span class="go">5 True</span>
</span></pre></div></div></div>

<h3>auto()</h3>
<p>Автоматическая генерация значений</p>
<div class="code_element"><div class="lang_line"><text>pycon</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-pycon"><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="kn">from</span> <span class="nn">enum</span> <span class="kn">import</span> <span class="n">Enum</span><span class="p">,</span> <span class="n">auto</span>
<span class="unselectable"><span class="gp">&gt;&gt;&gt;</span></span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="k">class</span> <span class="nc">State</span><span class="p">(</span><span class="n">Enum</span><span class="p">):</span>
<span class="unselectable"><span class="o">...</span> </span>    <span class="n">START</span> <span class="o">=</span> <span class="n">auto</span><span class="p">()</span>
<span class="unselectable"><span class="o">...</span> </span>    <span class="n">STOP</span> <span class="o">=</span> <span class="n">auto</span><span class="p">()</span>
<span class="unselectable"><span class="o">...</span> </span>    <span class="n">PAUSE</span> <span class="o">=</span> <span class="n">auto</span><span class="p">()</span>
<span class="unselectable"><span class="gp">...</span></span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="nb">print</span><span class="p">(</span><span class="nb">list</span><span class="p">(</span><span class="n">State</span><span class="p">))</span>
<span class="unselectable"><span class="go">[&lt;State.START: 1&gt;, &lt;State.STOP: 2&gt;, &lt;State.PAUSE: 3&gt;]</span>
</span></pre></div></div></div>

<h3>unique()</h3>
<p><code>@unique</code> гарантирует отсутствие дубликатов значений</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="kn">from</span> <span class="nn">enum</span> <span class="kn">import</span> <span class="n">Enum</span><span class="p">,</span> <span class="n">unique</span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span></span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="nd">@unique</span>
<span class="unselectable"><span class="o">...</span> </span><span class="k">class</span> <span class="nc">Shape</span><span class="p">(</span><span class="n">Enum</span><span class="p">):</span>
<span class="unselectable"><span class="o">...</span> </span>    <span class="n">CIRCLE</span> <span class="o">=</span> <span class="mi">1</span>
<span class="unselectable"><span class="o">...</span> </span>    <span class="n">SQUARE</span> <span class="o">=</span> <span class="mi">2</span>
<span class="unselectable"><span class="o">...</span></span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="nd">@unique</span>
<span class="unselectable"><span class="o">...</span> </span><span class="k">class</span> <span class="nc">Shape</span><span class="p">(</span><span class="n">Enum</span><span class="p">):</span>
<span class="unselectable"><span class="o">...</span> </span>    <span class="n">CIRCLE</span> <span class="o">=</span> <span class="mi">1</span>
<span class="unselectable"><span class="o">...</span> </span>    <span class="n">SQUARE</span> <span class="o">=</span> <span class="mi">1</span>
<span class="unselectable"><span class="o">...</span></span>
<span class="unselectable"><span class="ne">ValueError</span><span class="p">:</span> <span class="n">duplicate</span> <span class="n">values</span> <span class="n">found</span> <span class="ow">in</span> <span class="o">&lt;</span><span class="n">enum</span> <span class="s1">&#39;Shape&#39;</span><span class="o">&gt;</span><span class="p">:</span> <span class="n">SQUARE</span> <span class="o">-&gt;</span> <span class="n">CIRCLE</span></span>
</pre></div></div></div>

<h3>.__members__</h3>
<p>Работа с элементами перечисления</p>
<div class="code_element"><div class="lang_line"><text>pycon</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-pycon"><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="kn">from</span> <span class="nn">enum</span> <span class="kn">import</span> <span class="n">Enum</span>
<span class="unselectable"><span class="gp">&gt;&gt;&gt;</span></span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="k">class</span> <span class="nc">Fruits</span><span class="p">(</span><span class="n">Enum</span><span class="p">):</span>
<span class="unselectable"><span class="o">...</span> </span>    <span class="n">APPLE</span> <span class="o">=</span> <span class="mi">1</span>
<span class="unselectable"><span class="o">...</span> </span>    <span class="n">ORANGE</span> <span class="o">=</span> <span class="mi">2</span>
<span class="unselectable"><span class="gp">...</span></span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="nb">print</span><span class="p">(</span><span class="n">Fruits</span><span class="o">.</span><span class="n">__members__</span><span class="p">)</span>
<span class="unselectable"><span class="go">{&#39;APPLE&#39;: &lt;Fruits.APPLE: 1&gt;, &#39;ORANGE&#39;: &lt;Fruits.ORANGE: 2&gt;}</span>
</span></pre></div></div></div>

<h3>EnumMeta</h3>
<p>Пример работы с метаклассом</p>
<div class="code_element"><div class="lang_line"><text>pycon</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-pycon"><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="kn">from</span> <span class="nn">enum</span> <span class="kn">import</span> <span class="n">Enum</span><span class="p">,</span> <span class="n">EnumMeta</span>
<span class="unselectable"><span class="gp">&gt;&gt;&gt;</span></span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="k">class</span> <span class="nc">MyEnumMeta</span><span class="p">(</span><span class="n">EnumMeta</span><span class="p">):</span>
<span class="unselectable"><span class="o">...</span> </span>    <span class="k">def</span> <span class="fm">__contains__</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">item</span><span class="p">):</span>
<span class="unselectable"><span class="o">...</span> </span>        <span class="k">return</span> <span class="n">item</span> <span class="ow">in</span> <span class="bp">cls</span><span class="o">.</span><span class="n">_value2member_map_</span>
<span class="unselectable"><span class="gp">...</span></span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="k">class</span> <span class="nc">Colors</span><span class="p">(</span><span class="n">Enum</span><span class="p">,</span> <span class="n">metaclass</span><span class="o">=</span><span class="n">MyEnumMeta</span><span class="p">):</span>
<span class="unselectable"><span class="o">...</span> </span>    <span class="n">RED</span> <span class="o">=</span> <span class="mi">1</span>
<span class="unselectable"><span class="o">...</span> </span>    <span class="n">BLUE</span> <span class="o">=</span> <span class="mi">2</span>
<span class="unselectable"><span class="gp">...</span></span>
<span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="nb">print</span><span class="p">(</span><span class="mi">1</span> <span class="ow">in</span> <span class="n">Colors</span><span class="p">)</span>
<span class="unselectable"><span class="go">True</span>
<span class="o">&gt;&gt;&gt; </span></span><span class="nb">print</span><span class="p">(</span><span class="mi">3</span> <span class="ow">in</span> <span class="n">Colors</span><span class="p">)</span>
<span class="unselectable"><span class="go">False</span>
</span></pre></div></div></div>

<h3>Пользовательские методы и свойства</h3>
<p>Перечисления могут содержать методы и дополнительные свойства</p>
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
<p>Можно перегружать операторы в перечислениях</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">enum</span> <span class="kn">import</span> <span class="n">IntEnum</span>

<span class="k">class</span> <span class="nc">Level</span><span class="p">(</span><span class="n">IntEnum</span><span class="p">):</span>
    <span class="n">LOW</span> <span class="o">=</span> <span class="mi">1</span>
    <span class="n">MEDIUM</span> <span class="o">=</span> <span class="mi">2</span>
    <span class="n">HIGH</span> <span class="o">=</span> <span class="mi">3</span>

    <span class="k">def</span> <span class="fm">__ge__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">other</span><span class="p">):</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">value</span> <span class="o">&gt;=</span> <span class="n">other</span><span class="o">.</span><span class="n">value</span>

<span class="nb">print</span><span class="p">(</span><span class="n">Level</span><span class="o">.</span><span class="n">HIGH</span> <span class="o">&gt;=</span> <span class="n">Level</span><span class="o">.</span><span class="n">MEDIUM</span><span class="p">)</span>  <span class="c1"># True</span>
</pre></div></div></div>

<h3>Ошибки при работе с Enum</h3>
<ul>
<li><code>ValueError</code> Возникает, если обратиться к несуществующему значению <div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="n">Color</span><span class="p">(</span><span class="mi">10</span><span class="p">))</span>     <span class="c1"># ValueError: 10 is not a valid Color</span>
</pre></div></div></div></li>
<li><code>AttributeError</code> Возникает при обращении к несуществующему члену перечисления <div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="n">Color</span><span class="o">.</span><span class="n">YELLOW</span><span class="p">)</span>  <span class="c1"># AttributeError: YELLOW</span>
</pre></div></div></div></li>
</ul>
<h3>Особенности использования</h3>
<ul>
<li><strong>Перечисления неизменяемы</strong>: Невозможно присваивать новые значения или изменять существующие</li>
<li><strong>Перечисления можно использовать как ключи словарей</strong>, так как они неизменяемы и хешируемы</li>
</ul>