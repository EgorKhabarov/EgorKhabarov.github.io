<p>Библиотека <code>collections</code> предоставляет специализированные контейнерные типы данных,
которые расширяют стандартные структуры, такие как списки, кортежи и словари.
Эти структуры данных помогают сделать код более читабельным и эффективным.</p>
<table>
<thead>
<tr>
<th>Контейнер</th>
<th>Описание</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>Counter</code></td>
<td>Счетчик, который предназначен для подсчета хэшируемых объектов.<br>Возвращает словарь, где ключи — объекты, а значения — их количество</td>
</tr>
<tr>
<td><code>defaultdict</code></td>
<td>Словарь, который автоматически создает значение по умолчанию<br>для несуществующих ключей при первом обращении к ним</td>
</tr>
<tr>
<td><code>OrderedDict</code></td>
<td>Словарь, который сохраняет порядок добавления элементов</td>
</tr>
<tr>
<td><code>namedtuple()</code></td>
<td>Создает подклассы кортежей с именованными полями,<br>что позволяет обращаться к элементам по имени</td>
</tr>
<tr>
<td><code>deque</code></td>
<td>Двусторонняя очередь, которая поддерживает добавление<br>и удаление элементов с обоих концов с высокой производительностью</td>
</tr>
<tr>
<td><code>ChainMap</code></td>
<td>Объединяет несколько словарей или других отображений в одно,<br>обеспечивая единый вид для поиска и изменения данных</td>
</tr>
<tr>
<td><code>UserDict</code> <code>UserList</code> <code>UserString</code></td>
<td>Классы для создания пользовательских словарей,<br>списков и строк с возможностью переопределения их поведения</td>
</tr>
</tbody>
</table>
<h1>Counter</h1>
<p>Подкласс словаря, который предназначен для подсчета хэша объектов (например, слов, символов и т.д.).
Он подсчитывает количество вхождений каждого элемента.</p>
<table>
<thead>
<tr>
<th>Функция/Метод</th>
<th>Описание</th>
<th>Пример</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>Counter()</code></td>
<td>Создает объект <code>Counter</code></td>
<td><code>counter = Counter("abracadabra")</code></td>
</tr>
<tr>
<td><code>Counter().elements()</code></td>
<td>Возвращает итератор по элементам, каждый из которых<br>повторяется столько раз, сколько он встречается</td>
<td><code>list(counter.elements())</code></td>
</tr>
<tr>
<td><code>Counter().most_common([n])</code></td>
<td>Возвращает n самых распространенных элементов и их количество</td>
<td><code>counter.most_common(2)</code></td>
</tr>
<tr>
<td><code>Counter().subtract([iterable-or-mapping])</code></td>
<td>Вычитает элементы, как и <code>update</code>, но уменьшает количество</td>
<td><code>counter.subtract("abcd")</code></td>
</tr>
<tr>
<td><code>Counter().update([iterable-or-mapping])</code></td>
<td>Увеличивает счетчик для элементов из <code>iterable</code> или другого <code>Counter</code></td>
<td><code>counter.update("abc")</code></td>
</tr>
</tbody>
</table>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">collections</span> <span class="kn">import</span> <span class="n">Counter</span>

<span class="n">counter</span> <span class="o">=</span> <span class="n">Counter</span><span class="p">(</span><span class="s2">&quot;abracadabra&quot;</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">counter</span><span class="p">)</span>  <span class="c1"># Counter({&quot;a&quot;: 5, &quot;b&quot;: 2, &quot;r&quot;: 2, &quot;c&quot;: 1, &quot;d&quot;: 1})</span>

<span class="c1"># Выводим наиболее часто встречающиеся символы</span>
<span class="nb">print</span><span class="p">(</span><span class="n">counter</span><span class="o">.</span><span class="n">most_common</span><span class="p">(</span><span class="mi">2</span><span class="p">))</span>  <span class="c1"># [(&quot;a&quot;, 5), (&quot;b&quot;, 2)]</span>
<span class="nb">print</span><span class="p">(</span><span class="nb">list</span><span class="p">(</span><span class="n">counter</span><span class="o">.</span><span class="n">elements</span><span class="p">()))</span>  <span class="c1"># [&quot;a&quot;, &quot;a&quot;, &quot;a&quot;, &quot;a&quot;, &quot;a&quot;, &quot;b&quot;, &quot;b&quot;, &quot;r&quot;, &quot;r&quot;, &quot;c&quot;, &quot;d&quot;]</span>
</pre></div></div></div>

<h1>defaultdict</h1>
<p>Подкласс словаря, который вызывает функцию для отсутствующих ключей и использует её результат в качестве значения по умолчанию.</p>
<table>
<thead>
<tr>
<th>Функция/Метод</th>
<th>Описание</th>
<th>Пример</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>defaultdict(default_factory)</code></td>
<td>Создает словарь с значением по умолчанию</td>
<td><code>d = defaultdict(int)</code></td>
</tr>
</tbody>
</table>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">collections</span> <span class="kn">import</span> <span class="n">defaultdict</span>

<span class="n">d</span> <span class="o">=</span> <span class="n">defaultdict</span><span class="p">(</span><span class="nb">int</span><span class="p">)</span>
<span class="n">d</span><span class="p">[</span><span class="s2">&quot;a&quot;</span><span class="p">]</span> <span class="o">+=</span> <span class="mi">1</span>
<span class="nb">print</span><span class="p">(</span><span class="n">d</span><span class="p">)</span>  <span class="c1"># defaultdict(&lt;class &quot;int&quot;&gt;, {&quot;a&quot;: 1})</span>
</pre></div></div></div>

<h1>OrderedDict</h1>
<p>Подкласс словаря, который запоминает порядок добавления элементов.</p>
<table>
<thead>
<tr>
<th>Функция/Метод</th>
<th>Описание</th>
<th>Пример</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>OrderedDict()</code></td>
<td>Создает упорядоченный словарь</td>
<td><code>od = OrderedDict()</code></td>
</tr>
<tr>
<td><code>move_to_end(key, last=True)</code></td>
<td>Перемещает элемент с заданным ключом в конец или начало</td>
<td><code>od.move_to_end("a")</code></td>
</tr>
<tr>
<td><code>popitem(last=True)</code></td>
<td>Удаляет и возвращает элемент с конца или начала</td>
<td><code>od.popitem()</code></td>
</tr>
</tbody>
</table>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">collections</span> <span class="kn">import</span> <span class="n">OrderedDict</span>

<span class="n">od</span> <span class="o">=</span> <span class="n">OrderedDict</span><span class="p">()</span>
<span class="n">od</span><span class="p">[</span><span class="s2">&quot;a&quot;</span><span class="p">]</span> <span class="o">=</span> <span class="mi">1</span>
<span class="n">od</span><span class="p">[</span><span class="s2">&quot;b&quot;</span><span class="p">]</span> <span class="o">=</span> <span class="mi">2</span>
<span class="n">od</span><span class="p">[</span><span class="s2">&quot;c&quot;</span><span class="p">]</span> <span class="o">=</span> <span class="mi">3</span>
<span class="nb">print</span><span class="p">(</span><span class="n">od</span><span class="p">)</span>  <span class="c1"># OrderedDict([(&quot;a&quot;, 1), (&quot;b&quot;, 2), (&quot;c&quot;, 3)])</span>
</pre></div></div></div>

<h1>namedtuple</h1>
<p><a href="?General/Паттерны%20проектирования/Порождающие%20паттерны/Factory%20(Фабрика)">Фабрика классов</a>, которая создает подклассы кортежа с именованными полями.</p>
<table>
<thead>
<tr>
<th>Функция/Метод</th>
<th>Описание</th>
<th>Пример</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>namedtuple(typename, field_names)</code></td>
<td>Создает новый тип кортежа с именами полей</td>
<td><code>Point = namedtuple("Point", "x y")</code></td>
</tr>
<tr>
<td><code>_replace(**kwargs)</code></td>
<td>Возвращает новый экземпляр, заменив указанные поля</td>
<td><code>p._replace(x=10)</code></td>
</tr>
</tbody>
</table>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">collections</span> <span class="kn">import</span> <span class="n">namedtuple</span>

<span class="n">Point</span> <span class="o">=</span> <span class="n">namedtuple</span><span class="p">(</span><span class="s2">&quot;Point&quot;</span><span class="p">,</span> <span class="p">[</span><span class="s2">&quot;x&quot;</span><span class="p">,</span> <span class="s2">&quot;y&quot;</span><span class="p">])</span>
<span class="n">p</span> <span class="o">=</span> <span class="n">Point</span><span class="p">(</span><span class="mi">10</span><span class="p">,</span> <span class="mi">20</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">p</span><span class="p">)</span>    <span class="c1"># Point(x=10, y=20)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">p</span><span class="o">.</span><span class="n">x</span><span class="p">)</span>  <span class="c1"># 10</span>
<span class="nb">print</span><span class="p">(</span><span class="n">p</span><span class="o">.</span><span class="n">y</span><span class="p">)</span>  <span class="c1"># 20</span>
</pre></div></div></div>

<h1>deque</h1>
<p>Двусторонняя очередь, которая обеспечивает быстрый доступ и добавление элементов с обоих концов.</p>
<table>
<thead>
<tr>
<th>Функция/Метод</th>
<th>Описание</th>
<th>Пример</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>append(x)</code></td>
<td>Добавляет элемент в конец</td>
<td><code>dq.append(1)</code></td>
</tr>
<tr>
<td><code>appendleft(x)</code></td>
<td>Добавляет элемент в начало</td>
<td><code>dq.appendleft(1)</code></td>
</tr>
<tr>
<td><code>pop()</code></td>
<td>Удаляет и возвращает элемент с конца</td>
<td><code>dq.pop()</code></td>
</tr>
<tr>
<td><code>popleft()</code></td>
<td>Удаляет и возвращает элемент с начала</td>
<td><code>dq.popleft()</code></td>
</tr>
<tr>
<td><code>rotate(n)</code></td>
<td>Вращает очередь на <code>n</code> шагов</td>
<td><code>dq.rotate(1)</code></td>
</tr>
</tbody>
</table>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">collections</span> <span class="kn">import</span> <span class="n">deque</span>

<span class="n">dq</span> <span class="o">=</span> <span class="n">deque</span><span class="p">([</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">])</span>
<span class="n">dq</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="mi">4</span><span class="p">)</span>
<span class="n">dq</span><span class="o">.</span><span class="n">appendleft</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">dq</span><span class="p">)</span>  <span class="c1"># deque([0, 1, 2, 3, 4])</span>
<span class="n">dq</span><span class="o">.</span><span class="n">pop</span><span class="p">()</span>
<span class="n">dq</span><span class="o">.</span><span class="n">popleft</span><span class="p">()</span>
<span class="nb">print</span><span class="p">(</span><span class="n">dq</span><span class="p">)</span>  <span class="c1"># deque([1, 2, 3])</span>
</pre></div></div></div>

<h1>ChainMap</h1>
<p>Объединяет несколько словарей или других отображений в одно логическое целое.</p>
<table>
<thead>
<tr>
<th>Функция/Метод</th>
<th>Описание</th>
<th>Пример</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>ChainMap(*maps)</code></td>
<td>Создает новый <code>ChainMap</code> из указанных отображений</td>
<td><code>cm = ChainMap(dict1, dict2)</code></td>
</tr>
<tr>
<td><code>new_child(m=None)</code></td>
<td>Возвращает новый <code>ChainMap</code> с m как новой первичной картой</td>
<td><code>cm.new_child({"c": 3})</code></td>
</tr>
</tbody>
</table>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">collections</span> <span class="kn">import</span> <span class="n">ChainMap</span>

<span class="n">d1</span> <span class="o">=</span> <span class="p">{</span><span class="s2">&quot;a&quot;</span><span class="p">:</span> <span class="mi">1</span><span class="p">,</span> <span class="s2">&quot;b&quot;</span><span class="p">:</span> <span class="mi">2</span><span class="p">}</span>
<span class="n">d2</span> <span class="o">=</span> <span class="p">{</span><span class="s2">&quot;b&quot;</span><span class="p">:</span> <span class="mi">3</span><span class="p">,</span> <span class="s2">&quot;c&quot;</span><span class="p">:</span> <span class="mi">4</span><span class="p">}</span>

<span class="n">d</span> <span class="o">=</span> <span class="n">ChainMap</span><span class="p">(</span><span class="n">d1</span><span class="p">,</span> <span class="n">d2</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">d</span><span class="p">)</span>  <span class="c1"># ChainMap({&quot;a&quot;: 1, &quot;b&quot;: 2}, {&quot;b&quot;: 3, &quot;c&quot;: 4})</span>

<span class="nb">print</span><span class="p">(</span><span class="n">d</span><span class="p">[</span><span class="s2">&quot;a&quot;</span><span class="p">])</span>  <span class="c1"># 1</span>
<span class="nb">print</span><span class="p">(</span><span class="n">d</span><span class="p">[</span><span class="s2">&quot;b&quot;</span><span class="p">])</span>  <span class="c1"># 2 (из d1, так как b в d1 появился раньше, чем в d2)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">d</span><span class="p">[</span><span class="s2">&quot;c&quot;</span><span class="p">])</span>  <span class="c1"># 4 (из d2)</span>

<span class="n">d3</span> <span class="o">=</span> <span class="p">{</span><span class="s2">&quot;c&quot;</span><span class="p">:</span> <span class="mi">5</span><span class="p">,</span> <span class="s2">&quot;d&quot;</span><span class="p">:</span> <span class="mi">6</span><span class="p">}</span>
<span class="n">d</span> <span class="o">=</span> <span class="n">d</span><span class="o">.</span><span class="n">new_child</span><span class="p">(</span><span class="n">d3</span><span class="p">)</span>

<span class="nb">print</span><span class="p">(</span><span class="n">d</span><span class="p">[</span><span class="s2">&quot;c&quot;</span><span class="p">])</span>  <span class="c1"># 5 (из d3, так как он добавлен в цепочку позже, чем d2)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">d</span><span class="p">[</span><span class="s2">&quot;d&quot;</span><span class="p">])</span>  <span class="c1"># 6 (из d3)</span>
</pre></div></div></div>

<h1>UserDict, UserList, UserString</h1>
<p>Эти классы предоставляют возможность создания пользовательских классов,
наследуемых от словаря, списка и строки соответственно, с возможностью переопределения их поведения.</p>
<table>
<thead>
<tr>
<th>Класс</th>
<th>Описание</th>
<th>Пример</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>UserDict</code></td>
<td>Базовый класс для создания пользовательских словарей</td>
<td><code>class MyDict(UserDict): pass</code></td>
</tr>
<tr>
<td><code>UserList</code></td>
<td>Базовый класс для создания пользовательских списков</td>
<td><code>class MyList(UserList): pass</code></td>
</tr>
<tr>
<td><code>UserString</code></td>
<td>Базовый класс для создания пользовательских строк</td>
<td><code>class MyString(UserString): pass</code></td>
</tr>
</tbody>
</table>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">collections</span> <span class="kn">import</span> <span class="n">UserDict</span><span class="p">,</span> <span class="n">UserList</span><span class="p">,</span> <span class="n">UserString</span>

<span class="n">d</span> <span class="o">=</span> <span class="n">UserDict</span><span class="p">({</span><span class="s2">&quot;a&quot;</span><span class="p">:</span> <span class="mi">1</span><span class="p">,</span> <span class="s2">&quot;b&quot;</span><span class="p">:</span> <span class="mi">2</span><span class="p">})</span>
<span class="n">d</span><span class="p">[</span><span class="s2">&quot;c&quot;</span><span class="p">]</span> <span class="o">=</span> <span class="mi">3</span>
<span class="nb">print</span><span class="p">(</span><span class="n">d</span><span class="p">)</span>  <span class="c1"># {&quot;a&quot;: 1, &quot;b&quot;: 2, &quot;c&quot;: 3}</span>

<span class="n">l</span> <span class="o">=</span> <span class="n">UserList</span><span class="p">([</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">])</span>
<span class="n">l</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="mi">4</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">l</span><span class="p">)</span>  <span class="c1"># [1, 2, 3, 4]</span>

<span class="n">s</span> <span class="o">=</span> <span class="n">UserString</span><span class="p">(</span><span class="s2">&quot;hello, world&quot;</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">s</span><span class="o">.</span><span class="n">upper</span><span class="p">())</span>  <span class="c1"># HELLO, WORLD</span>


<span class="k">class</span> <span class="nc">MyDict</span><span class="p">(</span><span class="n">UserDict</span><span class="p">):</span>
    <span class="k">def</span> <span class="fm">__setitem__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">,</span> <span class="n">value</span><span class="p">):</span>
        <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;Setting </span><span class="si">{</span><span class="n">key</span><span class="si">}</span><span class="s2"> to </span><span class="si">{</span><span class="n">value</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">)</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__setitem__</span><span class="p">(</span><span class="n">key</span><span class="p">,</span> <span class="n">value</span><span class="p">)</span>


<span class="n">md</span> <span class="o">=</span> <span class="n">MyDict</span><span class="p">()</span>
<span class="n">md</span><span class="p">[</span><span class="s2">&quot;a&quot;</span><span class="p">]</span> <span class="o">=</span> <span class="mi">1</span>  <span class="c1"># Setting a to 1</span>
</pre></div></div></div>

<h1>Полезные ссылки</h1>
<ul>
<li><a href="https://docs.python.org/3/library/collections.html">Официальная документация</a></li>
<li><a href="https://realpython.com/python-collections-module/">Real Python - Advanced Python Collections</a></li>
</ul>