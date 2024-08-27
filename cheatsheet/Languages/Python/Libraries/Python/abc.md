<p><code>abc</code> предоставляет инструменты для работы с абстрактными базовыми классами (ABC).
Эти классы используются для определения интерфейсов, которые должны реализовывать дочерние классы.</p>
<h3>Основные компоненты</h3>
<ul>
<li><strong><code>ABC</code></strong> — абстрактный базовый класс.</li>
<li><strong><code>abstractmethod</code></strong> — декоратор для определения абстрактных методов,
которые должны быть реализованы в дочерних классах.</li>
</ul>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">abc</span> <span class="kn">import</span> <span class="n">ABC</span><span class="p">,</span> <span class="n">abstractmethod</span>


<span class="k">class</span> <span class="nc">MyAbstractClass</span><span class="p">(</span><span class="n">ABC</span><span class="p">):</span>
    <span class="nd">@abstractmethod</span>
    <span class="k">def</span> <span class="nf">my_method</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="k">pass</span>

    <span class="c1"># Пример абстрактного свойства</span>
    <span class="nd">@property</span>
    <span class="nd">@abstractmethod</span>
    <span class="k">def</span> <span class="nf">my_property</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="k">pass</span>


<span class="k">class</span> <span class="nc">ConcreteClass</span><span class="p">(</span><span class="n">MyAbstractClass</span><span class="p">):</span>
    <span class="k">def</span> <span class="nf">my_method</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="k">return</span> <span class="s2">&quot;Method implemented&quot;</span>

    <span class="nd">@property</span>
    <span class="k">def</span> <span class="nf">my_property</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="k">return</span> <span class="s2">&quot;Property value&quot;</span>


<span class="c1"># Попытка создать экземпляр абстрактного класса напрямую вызовет ошибку</span>
<span class="c1"># my_abstract_instance = MyAbstractClass()  # Это вызовет TypeError</span>

<span class="c1"># Создание экземпляра класса, который реализует все абстрактные методы</span>
<span class="n">concrete_instance</span> <span class="o">=</span> <span class="n">ConcreteClass</span><span class="p">()</span>
<span class="nb">print</span><span class="p">(</span><span class="n">concrete_instance</span><span class="o">.</span><span class="n">my_method</span><span class="p">())</span>  <span class="c1"># Method implemented</span>
<span class="nb">print</span><span class="p">(</span><span class="n">concrete_instance</span><span class="o">.</span><span class="n">my_property</span><span class="p">)</span>  <span class="c1"># Property value</span>
</pre></div></div></div>

<p>Абстрактный метод в <code>ABC</code> не имеет реализации и должен быть переопределён в дочернем классе.</p>