<p>Модуль collections в Python содержит различные удобные классы для работы с коллекциями (наборами объектов).
Некоторые из классов в модуле collections:</p>
<p>namedtuple - это класс-фабрика для создания именованных кортежей, которые представляют собой 
             неизменяемые объекты, похожие на обычные кортежи, но каждый элемент имеет уникальное имя.</p>
<p>deque - это двусторонняя очередь, которая позволяет эффективно добавлять и удалять элементы как с начала, так и с конца.</p>
<p>Counter - это класс, который позволяет подсчитывать количество каждого элемента в последовательности.
          Возвращает словарь, где каждый ключ представляет элемент последовательности, а значение - количество его вхождений в последовательность.</p>
<p>OrderedDict - это словарь, который запоминает порядок вставки элементов.
              Позволяет итерироваться по элементам в порядке, в котором они были добавлены в словарь.</p>
<p>defaultdict - это словарь, который возвращает значение по умолчанию, если ключ отсутствует.
              При создании defaultdict необходимо указать функцию, которая будет вызываться для возврата значения по умолчанию. 
              Этот класс часто используется для создания словарей с дефолтным значением или для группировки элементов по какому-то признаку.</p>
<p>ChainMap - это класс, который позволяет объединить несколько словарей в один.
           Он предоставляет удобный способ комбинирования нескольких словарей в один, без необходимости копирования элементов.</p>
<p>UserDict - это класс, который предоставляет интерфейс словаря, но позволяет наследоваться для создания собственных классов словарей.
           Он может быть использован для создания словарей с дополнительной логикой или специальным поведением.</p>
<p>Эти классы облегчают работу с коллекциями в Python и уменьшают необходимость писать большой и сложный код для выполнения стандартных задач.</p>
<p>namedtuple:</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code399b" onclick="copyCode(code399, code399b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code399"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">collections</span> <span class="kn">import</span> <span class="n">namedtuple</span>

<span class="c1"># создаем именованный кортеж Point</span>
<span class="n">Point</span> <span class="o">=</span> <span class="n">namedtuple</span><span class="p">(</span><span class="s1">&#39;Point&#39;</span><span class="p">,</span> <span class="p">[</span><span class="s1">&#39;x&#39;</span><span class="p">,</span> <span class="s1">&#39;y&#39;</span><span class="p">])</span>

<span class="c1"># создаем экземпляр кортежа</span>
<span class="n">p</span> <span class="o">=</span> <span class="n">Point</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">)</span>

<span class="c1"># обращаемся к полям кортежа по имени</span>
<span class="nb">print</span><span class="p">(</span><span class="n">p</span><span class="o">.</span><span class="n">x</span><span class="p">)</span>  <span class="c1"># выведет 1</span>
<span class="nb">print</span><span class="p">(</span><span class="n">p</span><span class="o">.</span><span class="n">y</span><span class="p">)</span>  <span class="c1"># выведет 2</span>
</pre></div></div></div>

<p>deque:</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code400b" onclick="copyCode(code400, code400b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code400"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">collections</span> <span class="kn">import</span> <span class="n">deque</span>

<span class="c1"># создаем пустую двустороннюю очередь</span>
<span class="n">d</span> <span class="o">=</span> <span class="n">deque</span><span class="p">()</span>

<span class="c1"># добавляем элементы в очередь</span>
<span class="n">d</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span>
<span class="n">d</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="mi">2</span><span class="p">)</span>
<span class="n">d</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="mi">3</span><span class="p">)</span>

<span class="c1"># удаляем элементы из очереди</span>
<span class="nb">print</span><span class="p">(</span><span class="n">d</span><span class="o">.</span><span class="n">pop</span><span class="p">())</span>  <span class="c1"># выведет 3</span>
<span class="nb">print</span><span class="p">(</span><span class="n">d</span><span class="o">.</span><span class="n">popleft</span><span class="p">())</span>  <span class="c1"># выведет 1</span>

<span class="c1"># выводим оставшиеся элементы в очереди</span>
<span class="nb">print</span><span class="p">(</span><span class="n">d</span><span class="p">)</span>  <span class="c1"># выведет deque([2])</span>
</pre></div></div></div>

<p>Counter:</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code401b" onclick="copyCode(code401, code401b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code401"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">collections</span> <span class="kn">import</span> <span class="n">Counter</span>

<span class="c1"># создаем счетчик</span>
<span class="n">c</span> <span class="o">=</span> <span class="n">Counter</span><span class="p">(</span><span class="s1">&#39;hello, world&#39;</span><span class="p">)</span>

<span class="c1"># выводим количество вхождений каждого символа</span>
<span class="nb">print</span><span class="p">(</span><span class="n">c</span><span class="p">)</span>  <span class="c1"># выведет Counter({&#39;l&#39;: 3, &#39;o&#39;: 2, &#39;e&#39;: 1, &#39;h&#39;: 1, &#39;,&#39;: 1, &#39; &#39;: 1, &#39;w&#39;: 1, &#39;r&#39;: 1, &#39;d&#39;: 1})</span>

<span class="c1"># выводим наиболее часто встречающиеся символы</span>
<span class="nb">print</span><span class="p">(</span><span class="n">c</span><span class="o">.</span><span class="n">most_common</span><span class="p">(</span><span class="mi">2</span><span class="p">))</span>  <span class="c1"># выведет [(&#39;l&#39;, 3), (&#39;o&#39;, 2)]</span>
</pre></div></div></div>

<p>OrderedDict:</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code402b" onclick="copyCode(code402, code402b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code402"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">collections</span> <span class="kn">import</span> <span class="n">OrderedDict</span>

<span class="c1"># создаем упорядоченный словарь</span>
<span class="n">d</span> <span class="o">=</span> <span class="n">OrderedDict</span><span class="p">()</span>

<span class="c1"># добавляем элементы в словарь</span>
<span class="n">d</span><span class="p">[</span><span class="s1">&#39;a&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="mi">1</span>
<span class="n">d</span><span class="p">[</span><span class="s1">&#39;b&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="mi">2</span>
<span class="n">d</span><span class="p">[</span><span class="s1">&#39;c&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="mi">3</span>

<span class="c1"># выводим элементы в порядке их добавления</span>
<span class="k">for</span> <span class="n">k</span><span class="p">,</span> <span class="n">v</span> <span class="ow">in</span> <span class="n">d</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
    <span class="nb">print</span><span class="p">(</span><span class="n">k</span><span class="p">,</span> <span class="n">v</span><span class="p">)</span>
<span class="c1"># выведет:</span>
<span class="c1"># a 1</span>
<span class="c1"># b 2</span>
<span class="c1"># c 3</span>
</pre></div></div></div>

<p>defaultdict:</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code403b" onclick="copyCode(code403, code403b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code403"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">collections</span> <span class="kn">import</span> <span class="n">defaultdict</span>

<span class="c1"># создаем словарь с дефолтным значением 0</span>
<span class="n">d</span> <span class="o">=</span> <span class="n">defaultdict</span><span class="p">(</span><span class="nb">int</span><span class="p">)</span>

<span class="c1"># добавляем элементы в словарь</span>
<span class="n">d</span><span class="p">[</span><span class="s1">&#39;a&#39;</span><span class="p">]</span> <span class="o">+=</span> <span class="mi">1</span>
<span class="n">d</span><span class="p">[</span><span class="s1">&#39;b&#39;</span><span class="p">]</span> <span class="o">+=</span> <span class="mi">2</span>
<span class="n">d</span><span class="p">[</span><span class="s1">&#39;c&#39;</span><span class="p">]</span> <span class="o">+=</span> <span class="mi">3</span>

<span class="c1"># выводим словарь</span>
<span class="nb">print</span><span class="p">(</span><span class="n">d</span><span class="p">)</span>  <span class="c1"># выведет defaultdict(&lt;class &#39;int&#39;&gt;, {&#39;a&#39;: 1, &#39;b&#39;: 2, &#39;c&#39;: 3})</span>
</pre></div></div></div>

<p>ChainMap:</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code404b" onclick="copyCode(code404, code404b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code404"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">collections</span> <span class="kn">import</span> <span class="n">ChainMap</span>

<span class="c1"># создаем два словаря</span>
<span class="n">d1</span> <span class="o">=</span> <span class="p">{</span><span class="s1">&#39;a&#39;</span><span class="p">:</span> <span class="mi">1</span><span class="p">,</span> <span class="s1">&#39;b&#39;</span><span class="p">:</span> <span class="mi">2</span><span class="p">}</span>
<span class="n">d2</span> <span class="o">=</span> <span class="p">{</span><span class="s1">&#39;b&#39;</span><span class="p">:</span> <span class="mi">3</span><span class="p">,</span> <span class="s1">&#39;c&#39;</span><span class="p">:</span> <span class="mi">4</span><span class="p">}</span>

<span class="c1"># объединяем словари в цепочку</span>
<span class="n">d</span> <span class="o">=</span> <span class="n">ChainMap</span><span class="p">(</span><span class="n">d1</span><span class="p">,</span> <span class="n">d2</span><span class="p">)</span>

<span class="c1"># выводим элементы словаря</span>
<span class="nb">print</span><span class="p">(</span><span class="n">d</span><span class="p">[</span><span class="s1">&#39;a&#39;</span><span class="p">])</span>  <span class="c1"># выведет 1</span>
<span class="nb">print</span><span class="p">(</span><span class="n">d</span><span class="p">[</span><span class="s1">&#39;b&#39;</span><span class="p">])</span>  <span class="c1"># выведет 2 (из d1, так как b в d1 появился раньше, чем в d2)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">d</span><span class="p">[</span><span class="s1">&#39;c&#39;</span><span class="p">])</span>  <span class="c1"># выведет 4 (из d2)</span>

<span class="c1"># создаем новый словарь и добавляем его в цепочку</span>
<span class="n">d3</span> <span class="o">=</span> <span class="p">{</span><span class="s1">&#39;c&#39;</span><span class="p">:</span> <span class="mi">5</span><span class="p">,</span> <span class="s1">&#39;d&#39;</span><span class="p">:</span> <span class="mi">6</span><span class="p">}</span>
<span class="n">d</span> <span class="o">=</span> <span class="n">d</span><span class="o">.</span><span class="n">new_child</span><span class="p">(</span><span class="n">d3</span><span class="p">)</span>

<span class="c1"># выводим элементы словаря</span>
<span class="nb">print</span><span class="p">(</span><span class="n">d</span><span class="p">[</span><span class="s1">&#39;c&#39;</span><span class="p">])</span>  <span class="c1"># выведет 5 (из d3, так как он добавлен в цепочку позже, чем d2)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">d</span><span class="p">[</span><span class="s1">&#39;d&#39;</span><span class="p">])</span>  <span class="c1"># выведет 6 (из d3)</span>
</pre></div></div></div>

<p>UserDict:</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code405b" onclick="copyCode(code405, code405b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code405"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">collections</span> <span class="kn">import</span> <span class="n">UserDict</span>

<span class="c1"># создаем пользовательский словарь</span>
<span class="n">d</span> <span class="o">=</span> <span class="n">UserDict</span><span class="p">({</span><span class="s1">&#39;a&#39;</span><span class="p">:</span> <span class="mi">1</span><span class="p">,</span> <span class="s1">&#39;b&#39;</span><span class="p">:</span> <span class="mi">2</span><span class="p">})</span>

<span class="c1"># добавляем элементы в словарь</span>
<span class="n">d</span><span class="p">[</span><span class="s1">&#39;c&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="mi">3</span>

<span class="c1"># выводим элементы словаря</span>
<span class="nb">print</span><span class="p">(</span><span class="n">d</span><span class="p">)</span>  <span class="c1"># выведет {&#39;a&#39;: 1, &#39;b&#39;: 2, &#39;c&#39;: 3}</span>
</pre></div></div></div>

<p>UserList:</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code406b" onclick="copyCode(code406, code406b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code406"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">collections</span> <span class="kn">import</span> <span class="n">UserList</span>

<span class="c1"># создаем пользовательский список</span>
<span class="n">l</span> <span class="o">=</span> <span class="n">UserList</span><span class="p">([</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">])</span>

<span class="c1"># добавляем элементы в список</span>
<span class="n">l</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="mi">4</span><span class="p">)</span>

<span class="c1"># выводим элементы списка</span>
<span class="nb">print</span><span class="p">(</span><span class="n">l</span><span class="p">)</span>  <span class="c1"># выведет [1, 2, 3, 4]</span>
</pre></div></div></div>

<p>UserString:</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code407b" onclick="copyCode(code407, code407b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code407"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">collections</span> <span class="kn">import</span> <span class="n">UserString</span>

<span class="c1"># создаем пользовательскую строку</span>
<span class="n">s</span> <span class="o">=</span> <span class="n">UserString</span><span class="p">(</span><span class="s1">&#39;hello, world&#39;</span><span class="p">)</span>

<span class="c1"># изменяем строку</span>
<span class="n">s</span><span class="o">.</span><span class="n">data</span> <span class="o">=</span> <span class="n">s</span><span class="o">.</span><span class="n">data</span><span class="o">.</span><span class="n">upper</span><span class="p">()</span>

<span class="c1"># выводим строку</span>
<span class="nb">print</span><span class="p">(</span><span class="n">s</span><span class="p">)</span>  <span class="c1"># выведет HELLO, WORLD</span>
</pre></div></div></div>