<p>Взято из <a href='https://tproger.ru/articles/gajd-po-magicheskim-metodam-v-python' target='_blank'>https://tproger.ru/articles/gajd-po-magicheskim-metodam-v-python</a></p>
<p>Магические методы в Python — подробный гайд</p>
<p>Создание и удаление объектовЛюбое описание объекта в объектно-ориентированном
программировании начинается с создания объекта и его удаления.
Давайте подробнее остановимся на каждом из них:
&#95;&#95;new&#95;&#95;(cls[, ...]) — метод создания типа класса.
Он принимает первым аргументом тип класса, в котором он вызывается, и, как правило, возвращает этот же тип.
В основном используется, чтобы настраивать создание экземпляра класса тех объектов,
которые наследуются от неизменяемых типов (например, int, str, или tuple).
&#95;&#95;init&#95;&#95;(self[, ...]) — конструктор класса. Используется при определении объектов.
&#95;&#95;init_subclass&#95;&#95;(cls) — позволяет переопределить создание подклассов объекта.
Например, добавлять дополнительные атрибуты:</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="codef0cf31472e0d0f1b152096669917edc0b" onclick="copyCode(codef0cf31472e0d0f1b152096669917edc0, codef0cf31472e0d0f1b152096669917edc0b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="codef0cf31472e0d0f1b152096669917edc0"><div class="highlight"><pre><span></span><span class="o">&gt;&gt;&gt;</span> <span class="k">class</span> <span class="nc">Test</span><span class="p">:</span>
<span class="o">&gt;&gt;&gt;</span>     <span class="k">def</span> <span class="nf">__init_subclass__</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="o">/</span><span class="p">,</span> <span class="n">test_param</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
<span class="o">&gt;&gt;&gt;</span>         <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="n">__init_subclass__</span><span class="p">(</span><span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
<span class="o">&gt;&gt;&gt;</span>         <span class="bp">cls</span><span class="o">.</span><span class="n">test_param</span> <span class="o">=</span> <span class="n">test_param</span>
<span class="o">&gt;&gt;&gt;</span>
<span class="o">&gt;&gt;&gt;</span> <span class="k">class</span> <span class="nc">AnotherTest</span><span class="p">(</span><span class="n">Test</span><span class="p">,</span> <span class="n">test_param</span><span class="o">=</span><span class="s2">&quot;Hello World&quot;</span><span class="p">):</span>
<span class="o">&gt;&gt;&gt;</span>     <span class="k">pass</span>
</pre></div></div></div>

<p>&#95;&#95;del&#95;&#95;(self) — деструктор класса. Вызывается автоматически сборщиком мусора, практически никогда не используется, за исключением, когда пользователя необходимо предупредить о незакрытых дескрипторах.</p>
<p>Общие свойства объектов Любой объект может содержать дополнительную информацию, полезную при отладке или приведении типов. Например:
&#95;&#95;repr&#95;&#95;(self) — информационная строка об объекте. Выводится при вызове функции repr(...) или в момент отладки. Для последнего этот метод и предназначен.</p>
<p>Например:</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code2ac57223780e5a2b30248cd77eeda3c5b" onclick="copyCode(code2ac57223780e5a2b30248cd77eeda3c5, code2ac57223780e5a2b30248cd77eeda3c5b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code2ac57223780e5a2b30248cd77eeda3c5"><div class="highlight"><pre><span></span><span class="o">&gt;&gt;&gt;</span> <span class="k">class</span> <span class="nc">Test</span><span class="p">:</span>
<span class="o">&gt;&gt;&gt;</span>     <span class="k">def</span> <span class="fm">__repr__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
<span class="o">&gt;&gt;&gt;</span>         <span class="k">return</span> <span class="s2">&quot;&quot;</span>
<span class="o">&gt;&gt;&gt;</span>
<span class="o">&gt;&gt;&gt;</span> <span class="n">Test</span><span class="p">()</span>
<span class="o">...</span> <span class="s1">&#39;&#39;</span>
</pre></div></div></div>

<p>&#95;&#95;str&#95;&#95;(self) — вызывается при вызове функции str(...), возвращает строковый объект.</p>
<p>Например:</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code3d32b0ac0551834412fe87edf513bb5db" onclick="copyCode(code3d32b0ac0551834412fe87edf513bb5d, code3d32b0ac0551834412fe87edf513bb5db)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code3d32b0ac0551834412fe87edf513bb5d"><div class="highlight"><pre><span></span><span class="o">&gt;&gt;&gt;</span> <span class="k">class</span> <span class="nc">Test</span><span class="p">:</span>
<span class="o">&gt;&gt;&gt;</span>     <span class="k">def</span> <span class="fm">__str__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
<span class="o">&gt;&gt;&gt;</span>         <span class="k">return</span> <span class="s2">&quot;Hello World&quot;</span>
<span class="o">&gt;&gt;&gt;</span>
<span class="o">&gt;&gt;&gt;</span> <span class="n">test</span> <span class="o">=</span> <span class="n">Test</span><span class="p">()</span>
<span class="o">&gt;&gt;&gt;</span> <span class="nb">str</span><span class="p">(</span><span class="n">test</span><span class="p">)</span>
<span class="o">...</span> <span class="s1">&#39;Hello World&#39;</span>
</pre></div></div></div>

<p>&#95;&#95;bytes&#95;&#95;(self) — аналогично &#95;&#95;str&#95;&#95;(self), только возвращается набор байт.
&#95;&#95;format&#95;&#95;(self, format_spec) — вызывается при вызове функции format(...) и используется для форматировании строки с использованием строковых литералов.</p>
<p>Методы сравнения объектов между собой
&#95;&#95;lt&#95;&#95;(self, other) — определяет поведение оператора сравнения «меньше», &lt;.
&#95;&#95;le&#95;&#95;(self, other) — определяет поведение оператора сравнения «меньше или равно», &lt;=.
&#95;&#95;eq&#95;&#95;(self, other) — определяет поведение оператора «равенства», ==.
&#95;&#95;ne&#95;&#95;(self, other) — определяет поведение оператора «неравенства», !=.
&#95;&#95;gt&#95;&#95;(self, other) — определяет поведение оператора сравнения «больше», &gt;.
&#95;&#95;ge&#95;&#95;(self, other) — определяет поведение оператора сравнения «больше или равно», &gt;=.
&#95;&#95;hash&#95;&#95;(self) — вызывается функцией hash(...) и используется для определения контрольной суммы объекта, чтобы доказать его уникальность. Например, чтобы добавить объект в set, frozenset, или использовать в качестве ключа в словаре dict.
&#95;&#95;bool&#95;&#95;(self) — вызывается функцией bool(...) и возвращает True или False в соответствии с реализацией. Если данный метод не реализован в объекте, и объект является какой-либо последовательностью (списком, кортежем и т.д.), вместо него вызывается метод &#95;&#95;len&#95;&#95;. Используется, в основном, в условиях if, например:</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="codec46b388da1f363e2ef306fa391c451d4b" onclick="copyCode(codec46b388da1f363e2ef306fa391c451d4, codec46b388da1f363e2ef306fa391c451d4b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="codec46b388da1f363e2ef306fa391c451d4"><div class="highlight"><pre><span></span><span class="o">&gt;&gt;&gt;</span> <span class="k">class</span> <span class="nc">Test</span><span class="p">:</span>
<span class="o">&gt;&gt;&gt;</span>     <span class="k">def</span> <span class="fm">__bool__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
<span class="o">&gt;&gt;&gt;</span>         <span class="k">return</span> <span class="kc">True</span>
<span class="o">&gt;&gt;&gt;</span>
<span class="o">&gt;&gt;&gt;</span> <span class="n">test</span> <span class="o">=</span> <span class="n">Test</span><span class="p">()</span>
<span class="o">&gt;&gt;&gt;</span>
<span class="o">&gt;&gt;&gt;</span> <span class="k">if</span> <span class="n">test</span><span class="p">:</span>
<span class="o">&gt;&gt;&gt;</span>    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Hello World&quot;</span><span class="p">)</span>
<span class="o">&gt;&gt;&gt;</span>
<span class="o">...</span> <span class="s1">&#39;Hello World&#39;</span>
</pre></div></div></div>

<p>Доступ к атрибутам объекта
Доступ ко всем свойствам объекта также контролируются отдельными методами:
&#95;&#95;getattr&#95;&#95;(self, name) — вызывается методом getattr(...) или при обращении к атрибуту объекта через x.y, где x — объект, а y — атрибут.
&#95;&#95;setattr&#95;&#95;(self, name, value) — вызывается методом setattr(...) или при обращении к атрибуту объекта с последующим определением значения переданного атрибута. Например: x.y = 1, где x — объект, y — атрибут, а 1 — значение атрибута.
&#95;&#95;delattr&#95;&#95;(self, name) — вызывается методом delattr(...)или при ручном удалении атрибута у объекта с помощью del x.y, где  x — объект, а y — атрибут.
&#95;&#95;dir&#95;&#95;(self) — вызывается методом dir(...) и выводит список доступных атрибутов объекта.</p>
<p>Создание последовательностей
Любой объект может реализовать методы встроенных последовательностей (словари, кортежи, списки, строки и так далее). Доступ к значениям последовательности переопределяется следующими методами:
&#95;&#95;len&#95;&#95;(self) — вызывается методом len(...) и возвращает количество элементов в последовательности.
&#95;&#95;getitem&#95;&#95;(self, key) — вызывается при обращении к элементу в последовательности по его ключу (индексу). Метод должен выбрасывать исключение TypeError, если используется некорректный тип ключа, KeyError, если данному ключу не соответствует ни один элемент в последовательности.</p>
<p>Например:</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code308e1e7ce7a266eccd6dc05e37baed3eb" onclick="copyCode(code308e1e7ce7a266eccd6dc05e37baed3e, code308e1e7ce7a266eccd6dc05e37baed3eb)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code308e1e7ce7a266eccd6dc05e37baed3e"><div class="highlight"><pre><span></span><span class="o">&gt;&gt;&gt;</span> <span class="n">list_object</span> <span class="o">=</span> <span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">,</span> <span class="mi">4</span><span class="p">,</span> <span class="mi">5</span><span class="p">]</span>
<span class="o">&gt;&gt;&gt;</span> <span class="nb">print</span><span class="p">(</span><span class="n">list_object</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span>
<span class="o">...</span> <span class="mi">1</span>
<span class="o">&gt;&gt;&gt;</span>
<span class="o">&gt;&gt;&gt;</span> <span class="n">string_object</span> <span class="o">=</span> <span class="s2">&quot;hello world&quot;</span>
<span class="o">&gt;&gt;&gt;</span> <span class="nb">print</span><span class="p">(</span><span class="n">string_object</span><span class="p">[</span><span class="mi">0</span><span class="p">:</span><span class="mi">5</span><span class="p">])</span>
<span class="o">...</span> <span class="s1">&#39;hello&#39;</span>
<span class="o">&gt;&gt;&gt;</span>
<span class="o">&gt;&gt;&gt;</span> <span class="n">dict_object</span> <span class="o">=</span> <span class="p">{</span><span class="s2">&quot;key0&quot;</span><span class="p">:</span> <span class="kc">True</span><span class="p">,</span> <span class="s2">&quot;key1&quot;</span><span class="p">:</span> <span class="kc">False</span><span class="p">}</span>
<span class="o">&gt;&gt;&gt;</span> <span class="nb">print</span><span class="p">(</span><span class="n">dict_object</span><span class="p">[</span><span class="s2">&quot;key0&quot;</span><span class="p">])</span>
<span class="o">...</span> <span class="kc">True</span>
</pre></div></div></div>

<p>&#95;&#95;setitem&#95;&#95;(self, key, value) — вызывается при присваивании какого-либо значения элементу в последовательности. Также может выбрасывать исключения TypeError и KeyError.</p>
<p>Например:</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="codeba08a115c8492f586afd8b034dda5548b" onclick="copyCode(codeba08a115c8492f586afd8b034dda5548, codeba08a115c8492f586afd8b034dda5548b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="codeba08a115c8492f586afd8b034dda5548"><div class="highlight"><pre><span></span><span class="o">&gt;&gt;&gt;</span> <span class="n">list_object</span> <span class="o">=</span> <span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">,</span> <span class="mi">4</span><span class="p">,</span> <span class="mi">5</span><span class="p">]</span>
<span class="o">&gt;&gt;&gt;</span> <span class="n">list_object</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="o">=</span> <span class="mi">78</span>
<span class="o">&gt;&gt;&gt;</span> <span class="nb">print</span><span class="p">(</span><span class="n">list_object</span><span class="p">)</span>
<span class="o">...</span> <span class="p">[</span><span class="mi">78</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">,</span> <span class="mi">4</span><span class="p">,</span> <span class="mi">5</span><span class="p">]</span>
<span class="o">&gt;&gt;&gt;</span>
<span class="o">&gt;&gt;&gt;</span> <span class="n">dict_object</span> <span class="o">=</span> <span class="p">{</span><span class="s2">&quot;key0&quot;</span><span class="p">:</span> <span class="kc">True</span><span class="p">,</span> <span class="s2">&quot;key1&quot;</span><span class="p">:</span> <span class="kc">False</span><span class="p">}</span>
<span class="o">&gt;&gt;&gt;</span> <span class="n">dict_object</span><span class="p">[</span><span class="s2">&quot;key0&quot;</span><span class="p">]</span> <span class="o">=</span> <span class="kc">False</span>
<span class="o">&gt;&gt;&gt;</span> <span class="nb">print</span><span class="p">(</span><span class="n">dict_object</span><span class="p">)</span>
<span class="o">...</span> <span class="p">{</span><span class="s2">&quot;key0&quot;</span><span class="p">:</span> <span class="kc">False</span><span class="p">,</span> <span class="s2">&quot;key1&quot;</span><span class="p">:</span> <span class="kc">False</span><span class="p">}</span>
</pre></div></div></div>

<p>&#95;&#95;delitem&#95;&#95;(self, key) — вызывается при удалении значения в последовательности по его индексу (ключу) с помощью синтаксиса ключевого слова del.
&#95;&#95;missing&#95;&#95;(self, key) — вызывается в случаях, когда значения в последовательности не существует.
&#95;&#95;iter&#95;&#95;(self) — вызывается методом iter(...) и возвращает итератор последовательности, например, для использования объекта в цикле:</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code25307cb7d19b386a0e28b264003696d4b" onclick="copyCode(code25307cb7d19b386a0e28b264003696d4, code25307cb7d19b386a0e28b264003696d4b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code25307cb7d19b386a0e28b264003696d4"><div class="highlight"><pre><span></span><span class="o">&gt;&gt;&gt;</span> <span class="k">class</span> <span class="nc">Test</span><span class="p">:</span>
<span class="o">&gt;&gt;&gt;</span>     <span class="k">def</span> <span class="fm">__iter__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
<span class="o">&gt;&gt;&gt;</span>         <span class="k">return</span> <span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">)</span>
<span class="o">&gt;&gt;&gt;</span>
<span class="o">&gt;&gt;&gt;</span> <span class="k">for</span> <span class="n">value</span> <span class="ow">in</span> <span class="n">Test</span><span class="p">():</span>
<span class="o">&gt;&gt;&gt;</span>     <span class="nb">print</span><span class="p">(</span><span class="n">value</span><span class="p">)</span>
<span class="o">...</span> <span class="mi">1</span>
<span class="o">...</span> <span class="mi">2</span>
<span class="o">...</span> <span class="mi">3</span>
</pre></div></div></div>

<p>&#95;&#95;reversed&#95;&#95;(self) — вызывается методом reversed(...) и аналогично методу &#95;&#95;iter&#95;&#95; возвращает тот же итератор, только в обратном порядке.
&#95;&#95;contains&#95;&#95;(self, item) — вызывается при проверке принадлежности элемента к последовательности с помощью in или not in.</p>
<p>Числовые магические методы
Данные методы делятся на несколько групп: унарные операторы, обычные арифметические, отражённые арифметические операторы, составные присваивания и преобразования типов.</p>
<p>Унарные операторы
&#95;&#95;neg&#95;&#95;(self) — определяет поведение для отрицания (-a)
&#95;&#95;pos&#95;&#95;(self) — определяет поведение для унарного плюса (+a)
&#95;&#95;abs&#95;&#95;(self) — определяет поведение для встроенной функции abs(...)
&#95;&#95;invert&#95;&#95;(self) — определяет поведение для инвертирования оператором ~</p>
<p>Обычные арифметические операторы
&#95;&#95;add&#95;&#95;(self, other) — сложение, оператор +
&#95;&#95;sub&#95;&#95;(self, other) — вычитание, оператор -
&#95;&#95;mul&#95;&#95;(self, other) — умножение, оператор *
&#95;&#95;matmul&#95;&#95;(self, other) — умножение матриц, оператор @
&#95;&#95;truediv&#95;&#95;(self, other) — деление, оператор /
&#95;&#95;floordiv&#95;&#95;(self, other) — целочисленное деление, оператор //
&#95;&#95;mod&#95;&#95;(self, other) — остаток от деления, оператор %
&#95;&#95;divmod&#95;&#95;(self, other) — деление с остатком, определяет поведение для встроенной функции divmod(...)
&#95;&#95;pow&#95;&#95;(self, other[, modulo]) — возведение в степень, оператор **
&#95;&#95;lshift&#95;&#95;(self, other) — двоичный сдвиг влево, оператор &lt;&lt;
&#95;&#95;rshift&#95;&#95;(self, other) — двоичный сдвиг вправо, оператор &gt;&gt;
&#95;&#95;and&#95;&#95;(self, other) — двоичное И, оператор &amp;
&#95;&#95;xor&#95;&#95;(self, other) — исключающее ИЛИ, оператор ^
&#95;&#95;or&#95;&#95;(self, other) — двоичное ИЛИ, оператор |</p>
<p>Отражённые арифметические операторы
Если в обычной арифметике между объектами a и b, объектом, который мы изменяем, является a, и объектом, с которым мы работаем, является b, то в отражённой арифметике наоборот — b является изменяемым, a — объектом, с которым мы работаем, и который передается в качестве аргумента.</p>
<p>Например:</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code17ce67146e18a5326b2244b87d2a1a85b" onclick="copyCode(code17ce67146e18a5326b2244b87d2a1a85, code17ce67146e18a5326b2244b87d2a1a85b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code17ce67146e18a5326b2244b87d2a1a85"><div class="highlight"><pre><span></span><span class="c1"># Сложение, используется обычная арифметика и метод __add__ в объекте left:</span>
<span class="o">&gt;&gt;&gt;</span> <span class="n">left</span> <span class="o">+</span> <span class="n">right</span>
<span class="c1"># Сложение, используется отражённая арифметика и метод __radd__ в объекте left:</span>
<span class="o">&gt;&gt;&gt;</span> <span class="n">right</span> <span class="o">+</span> <span class="n">left</span>
</pre></div></div></div>

<p>Список методов похож на тот, что используется в обычной арифметике, за исключением того, что добавляется префикс «r» ко всем методам:
&#95;&#95;radd&#95;&#95;(self, other) — сложение, оператор +
&#95;&#95;rsub&#95;&#95;(self, other) — вычитание, оператор -
&#95;&#95;rmul&#95;&#95;(self, other) — умножение, оператор *
&#95;&#95;rmatmul&#95;&#95;(self, other) — умножение матриц, оператор @
&#95;&#95;rtruediv&#95;&#95;(self, other) — деление, оператор /
&#95;&#95;rfloordiv&#95;&#95;(self, other) — целочисленное деление, оператор //
&#95;&#95;rmod&#95;&#95;(self, other) — остаток от деления, оператор %
&#95;&#95;rdivmod&#95;&#95;(self, other) — деление с остатком
&#95;&#95;rpow&#95;&#95;(self, other[, modulo]) — возведение в степень, оператор **
&#95;&#95;rlshift&#95;&#95;(self, other) — двоичный сдвиг влево, оператор &lt;&lt;
&#95;&#95;rrshift&#95;&#95;(self, other) — двоичный сдвиг вправо, оператор &gt;&gt;
&#95;&#95;rand&#95;&#95;(self, other) — двоичное И, оператор &amp;
&#95;&#95;rxor&#95;&#95;(self, other) — исключающее ИЛИ, оператор ^
&#95;&#95;ror&#95;&#95;(self, other) — двоичное ИЛИ, оператор |</p>
<p>Составное присваивание
Эти методы — комбинация «обычного» оператора и присваивания. Возвращают тот же тип объекта, который будет присвоен переменной слева. Например:
x = 3
x += 2 # другими словами x = x + 2</p>
<p>&#95;&#95;iadd&#95;&#95;(self, other) — сложение с присваиванием, оператор +=
&#95;&#95;isub&#95;&#95;(self, other) — вычитание с присваиванием, оператор -=
&#95;&#95;imul&#95;&#95;(self, other) — умножение с присваиванием, оператор <em>=
&#95;&#95;imatmul&#95;&#95;(self, other) — умножение матриц с присваиванием, оператор @=
&#95;&#95;itruediv&#95;&#95;(self, other) — деление с присваиванием, оператор /=
&#95;&#95;ifloordiv&#95;&#95;(self, other) — целочисленное деление с присваиванием, оператор //=
&#95;&#95;imod&#95;&#95;(self, other) — остаток от деления с присваиванием, оператор %=
&#95;&#95;ipow&#95;&#95;(self, other[, modulo]) — возведение в степень с присваиванием, оператор </em>*=
&#95;&#95;ilshift&#95;&#95;(self, other) — двоичный сдвиг влево с присваиванием, оператор &lt;&lt;=
&#95;&#95;irshift&#95;&#95;(self, other) — двоичный сдвиг вправо с присваиванием, оператор &gt;&gt;=
&#95;&#95;iand&#95;&#95;(self, other) — двоичное И с присваиванием, оператор &amp;=
&#95;&#95;ixor&#95;&#95;(self, other) — исключающее ИЛИ с присваиванием, оператор ^=
&#95;&#95;ior&#95;&#95;(self, other) — двоичное ИЛИ с присваиванием, оператор |=</p>
<p>Преобразования типов
Помимо всего прочего, в Python множество методов, которые позволяют переопределять поведение встроенных функций преобразования типов, таких как int(...), float(...) и т.д. Например:
&#95;&#95;complex&#95;&#95;(self) — преобразование типа в комплексное число
&#95;&#95;int&#95;&#95;(self) — преобразование типа к int
&#95;&#95;float&#95;&#95;(self) — преобразование типа к float
&#95;&#95;index&#95;&#95;(self) — преобразование типа к int, когда объект используется в срезах (выражения вида [start:stop:step])
&#95;&#95;round&#95;&#95;(self[, ndigits]) — округление числа с помощью функции round(...)
&#95;&#95;trunc&#95;&#95;(self) — вызывается методом math.trunc(...)
&#95;&#95;floor&#95;&#95;(self) — вызывается методом math.floor(...)
&#95;&#95;ceil&#95;&#95;(self) — вызывается методом math.ceil(...)</p>
<p>Вызываемые объекты
&#95;&#95;call&#95;&#95;(self[, args...]) — позволяет любому экземпляру класса вести себя как обычная функция.</p>
<p>Например:</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code87ee9ee61ddc4522256eba444cdd5088b" onclick="copyCode(code87ee9ee61ddc4522256eba444cdd5088, code87ee9ee61ddc4522256eba444cdd5088b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code87ee9ee61ddc4522256eba444cdd5088"><div class="highlight"><pre><span></span><span class="o">&gt;&gt;&gt;</span> <span class="k">class</span> <span class="nc">Test</span><span class="p">:</span>
<span class="o">&gt;&gt;&gt;</span>     <span class="k">def</span> <span class="fm">__call__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">message</span><span class="p">):</span>
<span class="o">&gt;&gt;&gt;</span>         <span class="nb">print</span><span class="p">(</span><span class="n">message</span><span class="p">)</span>
<span class="o">&gt;&gt;&gt;</span>         <span class="k">return</span> <span class="kc">True</span>
<span class="o">&gt;&gt;&gt;</span>
<span class="o">&gt;&gt;&gt;</span> <span class="n">test</span> <span class="o">=</span> <span class="n">Test</span><span class="p">()</span>
<span class="o">&gt;&gt;&gt;</span> <span class="n">test</span><span class="p">(</span><span class="s2">&quot;Hello World&quot;</span><span class="p">)</span>
<span class="o">...</span> <span class="s1">&#39;Hello World&#39;</span>
<span class="o">...</span> <span class="kc">True</span>
</pre></div></div></div>

<p>&#95;&#95;await&#95;&#95;(self) — возвращает итератор, превращая класс в корутину, результат выполнения которой можно получить с помощью await. Подробнее об этом можно узнать в PEP 492.</p>
<p>Контекстные менеджеры
Любой объект может быть представлен как контекстный менеджер, который вызывается с помощью with или async with. Данная конструкция позволяет выполнить какие-либо действия по настройке объекта и при выходе из контекстного менеджера, произвести какие-либо действия по очистке, не смотря на то, было ли вызвано исключение в блоке контекстного менеджера.
&#95;&#95;enter&#95;&#95;(self) — определяет начало блока контекстного менеджера, вызванного с помощью with
&#95;&#95;exit&#95;&#95;(self, exc_type, exc_value, traceback) — определяет конец блока контекстного менеджера. Может использоваться для контролирования исключений, очистки, или любых действий, которые должны быть выполнены после блока внутри with. Если блок выполнился успешно, то все три аргумента (exc_type, exc_value и traceback) будут установлены в значение None.</p>
<p>Например:</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code2b7f81a468f32b68665d10c1b821e2afb" onclick="copyCode(code2b7f81a468f32b68665d10c1b821e2af, code2b7f81a468f32b68665d10c1b821e2afb)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code2b7f81a468f32b68665d10c1b821e2af"><div class="highlight"><pre><span></span><span class="o">&gt;&gt;&gt;</span> <span class="k">class</span> <span class="nc">ContextManager</span><span class="p">:</span>
<span class="o">&gt;&gt;&gt;</span>     <span class="k">def</span> <span class="fm">__enter__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
<span class="o">&gt;&gt;&gt;</span>         <span class="n">log</span><span class="p">(</span><span class="s2">&quot;entering context&quot;</span><span class="p">)</span>
<span class="o">&gt;&gt;&gt;</span>
<span class="o">&gt;&gt;&gt;</span>     <span class="k">def</span> <span class="fm">__exit__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">exc_type</span><span class="p">,</span> <span class="n">exc_value</span><span class="p">,</span> <span class="n">traceback</span><span class="p">):</span>
<span class="o">&gt;&gt;&gt;</span>         <span class="n">log</span><span class="p">(</span><span class="s2">&quot;exiting context&quot;</span><span class="p">)</span>
<span class="o">&gt;&gt;&gt;</span>
<span class="o">&gt;&gt;&gt;</span> <span class="k">with</span> <span class="n">ContextManager</span><span class="p">():</span>
<span class="o">...</span>     <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;in context manager&quot;</span><span class="p">)</span>
<span class="o">...</span>
<span class="o">...</span> <span class="s1">&#39;entering context&#39;</span>
<span class="o">...</span> <span class="s1">&#39;in context manager&#39;</span>
<span class="o">...</span> <span class="s1">&#39;exiting context&#39;</span>
</pre></div></div></div>

<p>&#95;&#95;aenter&#95;&#95;(self) — аналогично &#95;&#95;enter&#95;&#95;, только функция возвращает корутину (результат которой можно получить с помощью await)
&#95;&#95;aexit&#95;&#95;(self, exc_type, exc_value, traceback) — аналогично &#95;&#95;exit&#95;&#95;, только функция возвращает корутину (результат которой можно получить с помощью await)</p>
<p>Например:</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code17142f471271e19c3780893be3fd352ab" onclick="copyCode(code17142f471271e19c3780893be3fd352a, code17142f471271e19c3780893be3fd352ab)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code17142f471271e19c3780893be3fd352a"><div class="highlight"><pre><span></span><span class="o">&gt;&gt;&gt;</span> <span class="k">class</span> <span class="nc">AsyncContextManager</span><span class="p">:</span>
<span class="o">&gt;&gt;&gt;</span>     <span class="k">async</span> <span class="k">def</span> <span class="fm">__aenter__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
<span class="o">&gt;&gt;&gt;</span>         <span class="k">await</span> <span class="n">log</span><span class="p">(</span><span class="s2">&quot;entering context&quot;</span><span class="p">)</span>
<span class="o">&gt;&gt;&gt;</span>
<span class="o">&gt;&gt;&gt;</span>     <span class="k">async</span> <span class="k">def</span> <span class="fm">__aexit__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">exc_type</span><span class="p">,</span> <span class="n">exc_value</span><span class="p">,</span> <span class="n">traceback</span><span class="p">):</span>
<span class="o">&gt;&gt;&gt;</span>         <span class="k">await</span> <span class="n">log</span><span class="p">(</span><span class="s2">&quot;exiting context&quot;</span><span class="p">)</span>
<span class="o">&gt;&gt;&gt;</span>
<span class="o">&gt;&gt;&gt;</span> <span class="k">async</span> <span class="k">with</span> <span class="n">AsyncContextManager</span><span class="p">():</span>
<span class="o">...</span>     <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;in context manager&quot;</span><span class="p">)</span>
<span class="o">...</span>
<span class="o">...</span> <span class="s1">&#39;entering context&#39;</span>
<span class="o">...</span> <span class="s1">&#39;in context manager&#39;</span>
<span class="o">...</span> <span class="s1">&#39;exiting context&#39;</span>
</pre></div></div></div>

<p>Неиспользуемые методы
Некоторые методы, после полного перехода с Python 2 на Python 3 стали устаревшими и больше не используются.
&#95;&#95;unicode&#95;&#95; — полностью исчез в версии Python 3, вместо него используются отдельные методы &#95;&#95;str_&#95;&#95; &#95;&#95;bytes&#95;&#95;
&#95;&#95;div&#95;&#95; — так как в Python 3 теперь по умолчанию «правильное деление», данного метода не существует
&#95;&#95;cmp&#95;&#95; — более не существует, вместо него используются &#95;&#95;lt&#95;&#95;, &#95;&#95;le&#95;&#95;, &#95;&#95;eq&#95;&#95;, &#95;&#95;ne&#95;&#95;, &#95;&#95;gt_&#95;&#95; &#95;&#95;ge&#95;&#95;
&#95;&#95;nonzero&#95;&#95; — переименован в &#95;&#95;bool&#95;&#95;</p>
<p>Упрощение работы с магическими методами
Большая часть из вышеописанных методов реализуется библиотеками, они позволяют использовать так называемые «обрёртки» над классами, в которых будут реализованы необходимые магические методы.</p>
<p>Пример таких библиотек:
dataclasses
attrs</p>
<p>Принципы и идеология этих (и других библиотек) схожи в одном – они позволяют реализовать всю необходимую логику работы с объектом, не дублируя код для каждого отдельного объекта.</p>
<p>Например:</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code59fd7ead40318a8b84c9a493db5da67fb" onclick="copyCode(code59fd7ead40318a8b84c9a493db5da67f, code59fd7ead40318a8b84c9a493db5da67fb)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code59fd7ead40318a8b84c9a493db5da67f"><div class="highlight"><pre><span></span><span class="o">&gt;&gt;&gt;</span> <span class="kn">from</span> <span class="nn">dataclasses</span> <span class="kn">import</span> <span class="n">dataclass</span>
<span class="o">&gt;&gt;&gt;</span>
<span class="o">&gt;&gt;&gt;</span> <span class="nd">@dataclass</span><span class="p">(</span><span class="n">init</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="nb">repr</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">eq</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">order</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">unsafe_hash</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<span class="o">&gt;&gt;&gt;</span> <span class="k">class</span> <span class="nc">Person</span><span class="p">:</span>
<span class="o">&gt;&gt;&gt;</span>     <span class="n">first_name</span><span class="p">:</span> <span class="nb">str</span>
<span class="o">&gt;&gt;&gt;</span>     <span class="n">last_name</span><span class="p">:</span> <span class="nb">str</span>
<span class="o">&gt;&gt;&gt;</span>     <span class="n">age</span><span class="p">:</span> <span class="nb">int</span>
</pre></div></div></div>

<p>Данный объект будет иметь в себе:
Три атрибута first_name, last_name и age, которые также будут передаваться в конструктор класса;
Будет реализован метод &#95;&#95;repr&#95;&#95; для вывода информации для отладки;
Будут реализованы все магические методы сравнения (такие как &#95;&#95;lt&#95;&#95;, &#95;&#95;eq&#95;&#95; и так далее), а также метод &#95;&#95;hash&#95;&#95;.</p>
<p>Чаще всего вы будете пользоваться уже готовыми решениями, как пример выше, но для того чтобы понять, как работает язык Python изнутри, необходимо знать, как работают магические методы, за что они отвечают, что будет, если вызвать ту или иную функцию на объект, и что с этим объектом произойдёт.</p>