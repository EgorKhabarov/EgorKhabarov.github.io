<h1>__all__</h1>
<table>
<thead>
<tr>
<th>Название</th>
<th>Описание</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>@dataclass</code></td>
<td>Декоратор для автоматического создания методов класса, таких как <code>__init__</code>, <code>__repr__</code>, <code>__eq__</code>, и других.</td>
</tr>
<tr>
<td><code>field</code></td>
<td>Функция для настройки полей внутри датакласса. Позволяет задать значения по умолчанию, фабрики значений, а также управлять поведением полей.</td>
</tr>
<tr>
<td><code>Field</code></td>
<td>Класс, представляющий метаинформацию о полях датакласса. Создаётся автоматически при использовании <code>field()</code>.</td>
</tr>
<tr>
<td><code>FrozenInstanceError</code></td>
<td>Исключение, которое возникает при попытке изменить поле объекта неизменяемого (<code>frozen=True</code>) датакласса.</td>
</tr>
<tr>
<td><code>InitVar</code></td>
<td>Специальный тип для переменных, которые используются только в <code>__init__</code> и не сохраняются как атрибуты класса.</td>
</tr>
<tr>
<td><code>KW_ONLY</code></td>
<td>Специальная константа, используемая для обозначения полей, которые должны передаваться только через ключевые аргументы в <code>__init__</code>.</td>
</tr>
<tr>
<td><code>MISSING</code></td>
<td>Значение, указывающее на отсутствие значения по умолчанию для поля, используется библиотекой автоматически.</td>
</tr>
<tr>
<td><code>fields</code></td>
<td>Функция, возвращающая информацию о полях класса (список объектов <code>Field</code>).</td>
</tr>
<tr>
<td><code>asdict</code></td>
<td>Функция, которая преобразует объект датакласса в словарь, где ключами являются имена полей, а значениями — данные этих полей.</td>
</tr>
<tr>
<td><code>astuple</code></td>
<td>Преобразует объект датакласса в кортеж с последовательными значениями полей.</td>
</tr>
<tr>
<td><code>make_dataclass</code></td>
<td>Функция для динамического создания нового датакласса с указанными полями и их типами.</td>
</tr>
<tr>
<td><code>replace</code></td>
<td>Возвращает копию объекта датакласса с изменёнными значениями указанных полей.</td>
</tr>
<tr>
<td><code>is_dataclass</code></td>
<td>Функция, проверяющая, является ли объект экземпляром датакласса.</td>
</tr>
</tbody>
</table>
<h1>Описание</h1>
<h2>@dataclass</h2>
<p>Основной декоратор для объявления классов данных. Автоматически генерирует методы <code>__init__</code>, <code>__repr__</code>, <code>__eq__</code>, и другие.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">dataclasses</span> <span class="kn">import</span> <span class="n">dataclass</span>

<span class="nd">@dataclass</span>
<span class="k">class</span> <span class="nc">Person</span><span class="p">:</span>
    <span class="n">name</span><span class="p">:</span> <span class="nb">str</span>
    <span class="n">age</span><span class="p">:</span> <span class="nb">int</span>
</pre></div></div></div>
<h3>Параметры dataclass</h3>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="nd">@dataclass</span><span class="p">(</span>
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
<td><code>init</code></td>
<td>Нужно ли автоматически генерировать метод <code>__init__</code> для инициализации атрибутов класса</td>
</tr>
<tr>
<td><code>repr</code></td>
<td>Нужно ли автоматически генерировать метод <code>__repr__</code> для вывода строкового представления объектов класса</td>
</tr>
<tr>
<td><code>eq</code></td>
<td>Нужно ли автоматически генерировать метод <code>__eq__</code> для сравнения объектов класса</td>
</tr>
<tr>
<td><code>order</code></td>
<td>Нужно ли автоматически генерировать методы <code>__lt__</code>, <code>__le__</code>, <code>__gt__</code>, <code>__ge__</code> для сравнения объектов класса</td>
</tr>
<tr>
<td><code>unsafe_hash</code></td>
<td>Нужно ли автоматически генерировать метод <code>__hash__</code> для объектов класса.<br>Обычно этот аргумент следует использовать только для классов, объекты которых неизменяемы <code>frozen</code>,<br>так как изменяемые объекты могут привести к неожиданным результатам</td>
</tr>
<tr>
<td><code>frozen</code></td>
<td>Нужно ли сделать объекты класса неизменяемыми <code>immutable</code></td>
</tr>
</tbody>
</table>
<h4>Значения по умолчанию</h4>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="nd">@dataclass</span><span class="p">(</span>
    <span class="o">*</span><span class="p">,</span>
    <span class="n">init</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
    <span class="nb">repr</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
    <span class="n">eq</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
    <span class="n">order</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
    <span class="n">unsafe_hash</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">True</span><span class="p">,</span>
    <span class="n">frozen</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="kc">False</span><span class="p">,</span>
<span class="p">)</span>
</pre></div></div></div>

<h2>field</h2>
<p>Используется для более точной настройки полей.
Например, можно задать фабрику значений по умолчанию или исключить поле из конструктора.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">dataclasses</span> <span class="kn">import</span> <span class="n">dataclass</span><span class="p">,</span> <span class="n">field</span>

<span class="nd">@dataclass</span>
<span class="k">class</span> <span class="nc">Person</span><span class="p">:</span>
    <span class="n">name</span><span class="p">:</span> <span class="nb">str</span>
    <span class="n">age</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="n">field</span><span class="p">(</span><span class="n">default</span><span class="o">=</span><span class="mi">18</span><span class="p">)</span>  <span class="c1"># Значение по умолчанию</span>
    <span class="n">friends</span><span class="p">:</span> <span class="nb">list</span> <span class="o">=</span> <span class="n">field</span><span class="p">(</span><span class="n">default_factory</span><span class="o">=</span><span class="nb">list</span><span class="p">)</span>  <span class="c1"># Фабрика для списка</span>
</pre></div></div></div>

<h2>Field</h2>
<p>Объект, создаваемый при использовании функции <code>field()</code>.
Содержит информацию о поле, его значении по умолчанию, фабрике значений и других метаданных.</p>
<h2>FrozenInstanceError</h2>
<p>Исключение, которое генерируется, если пытаются изменить поле объекта неизменяемого датакласса.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">dataclasses</span> <span class="kn">import</span> <span class="n">dataclass</span><span class="p">,</span> <span class="n">FrozenInstanceError</span>

<span class="nd">@dataclass</span><span class="p">(</span><span class="n">frozen</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<span class="k">class</span> <span class="nc">Point</span><span class="p">:</span>
    <span class="n">x</span><span class="p">:</span> <span class="nb">int</span>
    <span class="n">y</span><span class="p">:</span> <span class="nb">int</span>

<span class="n">p</span> <span class="o">=</span> <span class="n">Point</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">)</span>
<span class="c1"># p.x = 10  # Вызовет FrozenInstanceError</span>
</pre></div></div></div>

<h2>InitVar</h2>
<p>Используется для создания переменных, которые существуют только на этапе инициализации и не сохраняются в объекте.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">dataclasses</span> <span class="kn">import</span> <span class="n">dataclass</span><span class="p">,</span> <span class="n">InitVar</span>

<span class="nd">@dataclass</span>
<span class="k">class</span> <span class="nc">Person</span><span class="p">:</span>
    <span class="n">name</span><span class="p">:</span> <span class="nb">str</span>
    <span class="n">age</span><span class="p">:</span> <span class="n">InitVar</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span>  <span class="c1"># Не сохраняется в объекте</span>
</pre></div></div></div>

<h2>KW_ONLY</h2>
<p>Позволяет указать, что некоторые поля должны передаваться только как именованные аргументы при создании объекта.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">dataclasses</span> <span class="kn">import</span> <span class="n">dataclass</span><span class="p">,</span> <span class="n">KW_ONLY</span>

<span class="nd">@dataclass</span>
<span class="k">class</span> <span class="nc">Person</span><span class="p">:</span>
    <span class="n">name</span><span class="p">:</span> <span class="nb">str</span>
    <span class="n">KW_ONLY</span>
    <span class="n">age</span><span class="p">:</span> <span class="nb">int</span>
</pre></div></div></div>

<h2>MISSING</h2>
<p>Специальное значение, используемое библиотекой <code>dataclasses</code> для обозначения отсутствия значения по умолчанию для поля.</p>
<h2>fields</h2>
<p>Возвращает список полей класса в виде объектов <code>Field</code>.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">dataclasses</span> <span class="kn">import</span> <span class="n">dataclass</span><span class="p">,</span> <span class="n">fields</span>

<span class="nd">@dataclass</span>
<span class="k">class</span> <span class="nc">Person</span><span class="p">:</span>
    <span class="n">name</span><span class="p">:</span> <span class="nb">str</span>
    <span class="n">age</span><span class="p">:</span> <span class="nb">int</span>

<span class="nb">print</span><span class="p">(</span><span class="n">fields</span><span class="p">(</span><span class="n">Person</span><span class="p">))</span>  <span class="c1"># Выводит информацию о полях класса</span>
</pre></div></div></div>

<h2>asdict</h2>
<p>Преобразует объект датакласса в словарь.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">dataclasses</span> <span class="kn">import</span> <span class="n">dataclass</span><span class="p">,</span> <span class="n">asdict</span>

<span class="nd">@dataclass</span>
<span class="k">class</span> <span class="nc">Person</span><span class="p">:</span>
    <span class="n">name</span><span class="p">:</span> <span class="nb">str</span>
    <span class="n">age</span><span class="p">:</span> <span class="nb">int</span>

<span class="n">p</span> <span class="o">=</span> <span class="n">Person</span><span class="p">(</span><span class="s2">&quot;Alice&quot;</span><span class="p">,</span> <span class="mi">30</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">asdict</span><span class="p">(</span><span class="n">p</span><span class="p">))</span>  <span class="c1"># {&quot;name&quot;: &quot;Alice&quot;, &quot;age&quot;: 30}</span>
</pre></div></div></div>

<h2>astuple</h2>
<p>Преобразует объект датакласса в кортеж.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">dataclasses</span> <span class="kn">import</span> <span class="n">astuple</span>

<span class="nb">print</span><span class="p">(</span><span class="n">astuple</span><span class="p">(</span><span class="n">p</span><span class="p">))</span>  <span class="c1"># (&quot;Alice&quot;, 30)</span>
</pre></div></div></div>

<h2>make_dataclass</h2>
<p>Создаёт новый датакласс на лету с указанными полями.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">dataclasses</span> <span class="kn">import</span> <span class="n">make_dataclass</span>

<span class="n">Point</span> <span class="o">=</span> <span class="n">make_dataclass</span><span class="p">(</span><span class="s2">&quot;Point&quot;</span><span class="p">,</span> <span class="p">[(</span><span class="s2">&quot;x&quot;</span><span class="p">,</span> <span class="nb">int</span><span class="p">),</span> <span class="p">(</span><span class="s2">&quot;y&quot;</span><span class="p">,</span> <span class="nb">int</span><span class="p">)])</span>
<span class="n">p</span> <span class="o">=</span> <span class="n">Point</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">p</span><span class="p">)</span>  <span class="c1"># Point(x=1, y=2)</span>
</pre></div></div></div>

<h2>replace</h2>
<p>Возвращает новую копию объекта с изменёнными полями.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">dataclasses</span> <span class="kn">import</span> <span class="n">replace</span>

<span class="n">p2</span> <span class="o">=</span> <span class="n">replace</span><span class="p">(</span><span class="n">p</span><span class="p">,</span> <span class="n">age</span><span class="o">=</span><span class="mi">35</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">p2</span><span class="p">)</span>  <span class="c1"># Person(name=&quot;Alice&quot;, age=35)</span>
</pre></div></div></div>

<h2>is_dataclass</h2>
<p>Проверяет, является ли объект экземпляром датакласса.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">dataclasses</span> <span class="kn">import</span> <span class="n">is_dataclass</span>

<span class="nb">print</span><span class="p">(</span><span class="n">is_dataclass</span><span class="p">(</span><span class="n">p</span><span class="p">))</span>  <span class="c1"># True</span>
</pre></div></div></div>

<h2>__post_init__</h2>
<p>Специальный метод, используемый <strong>только в датаклассах</strong> (аннотированных с помощью декоратора <code>@dataclass</code>).
Его основное предназначение — выполнить дополнительные действия или инициализацию после того, как автоматически сгенерированный метод <code>__init__</code> завершит свою работу.
В обычных классах этот метод не используется автоматически и его наличие не имеет смысла без использования библиотеки <code>dataclasses</code>.</p>
<p>Когда создается объект датакласса, Python сначала автоматически вызывает метод <code>__init__</code>, который создается на основе полей, объявленных в классе.
После этого, если в классе определен метод <code>__post_init__</code>, он будет вызван <strong>сразу после</strong> инициализации полей.</p>
<h3>Пример</h3>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">dataclasses</span> <span class="kn">import</span> <span class="n">dataclass</span>

<span class="nd">@dataclass</span>
<span class="k">class</span> <span class="nc">Employee</span><span class="p">:</span>
    <span class="n">name</span><span class="p">:</span> <span class="nb">str</span>
    <span class="n">base_salary</span><span class="p">:</span> <span class="nb">float</span>
    <span class="n">bonus_percentage</span><span class="p">:</span> <span class="nb">float</span> <span class="o">=</span> <span class="mf">0.0</span>
    <span class="n">total_salary</span><span class="p">:</span> <span class="nb">float</span> <span class="o">=</span> <span class="mf">0.0</span>

    <span class="k">def</span> <span class="nf">__post_init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>  <span class="c1"># Выполняется сразу после создания объекта</span>
        <span class="c1"># Рассчитываем итоговую зарплату на основе бонуса</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">total_salary</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">base_salary</span> <span class="o">+</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">base_salary</span> <span class="o">*</span> <span class="bp">self</span><span class="o">.</span><span class="n">bonus_percentage</span> <span class="o">/</span> <span class="mi">100</span><span class="p">)</span>

<span class="n">emp</span> <span class="o">=</span> <span class="n">Employee</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;Alice&quot;</span><span class="p">,</span> <span class="n">base_salary</span><span class="o">=</span><span class="mi">1000</span><span class="p">,</span> <span class="n">bonus_percentage</span><span class="o">=</span><span class="mi">10</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">emp</span><span class="p">)</span>  <span class="c1"># Employee(name=&quot;Alice&quot;, base_salary=1000, bonus_percentage=10, total_salary=1100.0)</span>
</pre></div></div></div>

<h3>Особенности</h3>
<ol>
<li><strong>Модификация значений полей</strong>: <code>__post_init__</code> часто используется для выполнения дополнительных вычислений или проверок,
требующих значений уже инициализированных полей</li>
<li><strong>Работа с <code>InitVar</code></strong>: Если в датаклассе используются поля <code>InitVar</code>, они передаются в <code>__post_init__</code>,
так как они не сохраняются как обычные атрибуты. Это полезно для временных параметров и инициализаций</li>
</ol>
<h3>Пример с InitVar</h3>
<p>Значение <code>celsius</code> передается в метод <code>__post_init__</code> и используется для вычисления значения поля <code>fahrenheit</code></p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">dataclasses</span> <span class="kn">import</span> <span class="n">dataclass</span><span class="p">,</span> <span class="n">InitVar</span>

<span class="nd">@dataclass</span>
<span class="k">class</span> <span class="nc">TemperatureConverter</span><span class="p">:</span>
    <span class="n">celsius</span><span class="p">:</span> <span class="n">InitVar</span><span class="p">[</span><span class="nb">float</span><span class="p">]</span>
    <span class="n">fahrenheit</span><span class="p">:</span> <span class="nb">float</span> <span class="o">=</span> <span class="mf">0.0</span>

    <span class="k">def</span> <span class="nf">__post_init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">celsius</span><span class="p">):</span>
        <span class="c1"># Преобразование градусов Цельсия в Фаренгейты</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">fahrenheit</span> <span class="o">=</span> <span class="n">celsius</span> <span class="o">*</span> <span class="mi">9</span><span class="o">/</span><span class="mi">5</span> <span class="o">+</span> <span class="mi">32</span>

<span class="n">temp</span> <span class="o">=</span> <span class="n">TemperatureConverter</span><span class="p">(</span><span class="n">celsius</span><span class="o">=</span><span class="mi">25</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">temp</span><span class="p">)</span>  <span class="c1"># TemperatureConverter(fahrenheit=77.0)</span>
</pre></div></div></div>