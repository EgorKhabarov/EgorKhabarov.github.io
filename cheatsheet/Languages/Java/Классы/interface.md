<div class="code_element"><div class="lang_line"><text>java</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-java"><div class="highlight"><pre><span></span><span class="kd">public</span><span class="w"> </span><span class="kd">interface</span> <span class="nc">InterfaceName</span><span class="w"> </span><span class="p">{</span>

<span class="p">}</span>
</pre></div></div></div>
<div class="code_element"><div class="lang_line"><text>java</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-java"><div class="highlight"><pre><span></span><span class="kd">public</span><span class="w"> </span><span class="kd">interface</span> <span class="nc">InterfaceName</span><span class="w"> </span><span class="kd">extends</span><span class="w"> </span><span class="n">Interface2Name</span><span class="p">,</span><span class="w"> </span><span class="n">Interface3Name</span><span class="w"> </span><span class="p">{</span>

<span class="p">}</span>
</pre></div></div></div>
<div class="code_element"><div class="lang_line"><text>java</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-java"><div class="highlight"><pre><span></span><span class="kd">public</span><span class="w"> </span><span class="kd">class</span> <span class="nc">ClassName</span><span class="w"> </span><span class="kd">implements</span><span class="w"> </span><span class="n">InterfaceName</span><span class="p">,</span><span class="w"> </span><span class="n">Interface2Name</span><span class="w"> </span><span class="p">{</span>

<span class="p">}</span>
</pre></div></div></div>

<ul>
<li>Методы <code>public abstract</code></li>
<li>Поля <code>public final static</code></li>
</ul>
<h1>Статические константы</h1>
<p>Помимо сигнатур методов, в блоке интерфейса можно создавать общедоступные статические константы.
Так как создать допускается только статические константы, ключевые слова <code>static</code> и <code>final</code> обычно не указываются
Константы просто наследуются классом и доступны через название класса или через название интерфейса</p>
<h1>Статические методы</h1>
<p>Внутри блока интерфейса можно определить статические методы с реализацией.
Такие методы доступны внутри блока интерфейса, а также через название интерфейса.
Переопределить такие методы внутри класса <strong>нельзя</strong>, и через экземпляр класса или название класса они <strong>недоступны</strong></p>
<div class="code_element"><div class="lang_line"><text>java</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-java"><div class="highlight"><pre><span></span><span class="kd">interface</span> <span class="nc">IStatic</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="kd">static</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="nf">test</span><span class="p">()</span><span class="w"> </span><span class="p">{</span>
<span class="w">        </span><span class="n">print</span><span class="p">();</span>
<span class="w">    </span><span class="p">}</span>

<span class="w">    </span><span class="kd">static</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="nf">print</span><span class="p">()</span><span class="w"> </span><span class="p">{</span>
<span class="w">        </span><span class="n">System</span><span class="p">.</span><span class="na">out</span><span class="p">.</span><span class="na">println</span><span class="p">(</span><span class="s">&quot;Привет&quot;</span><span class="p">);</span>
<span class="w">    </span><span class="p">}</span>
<span class="p">}</span>

<span class="kd">class</span> <span class="nc">K</span><span class="w"> </span><span class="kd">implements</span><span class="w"> </span><span class="n">IStatic</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="kd">public</span><span class="w"> </span><span class="nf">K</span><span class="p">()</span><span class="w"> </span><span class="p">{</span>
<span class="w">        </span><span class="n">IStatic</span><span class="p">.</span><span class="na">test</span><span class="p">();</span>
<span class="w">    </span><span class="p">}</span>
<span class="p">}</span>

<span class="kd">public</span><span class="w"> </span><span class="kd">class</span> <span class="nc">MyClass</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="kd">public</span><span class="w"> </span><span class="kd">static</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="nf">main</span><span class="p">(</span><span class="n">String</span><span class="o">[]</span><span class="w"> </span><span class="n">args</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">        </span><span class="n">K</span><span class="w"> </span><span class="n">k</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="k">new</span><span class="w"> </span><span class="n">K</span><span class="p">();</span><span class="w"> </span><span class="c1">// Привет</span>
<span class="w">        </span><span class="n">IStatic</span><span class="p">.</span><span class="na">print</span><span class="p">();</span><span class="w"> </span><span class="c1">// Привет</span>
<span class="w">    </span><span class="p">}</span>
<span class="p">}</span>
</pre></div></div></div>

<h1>Методы по умолчанию</h1>
<p>Позволяет добавить новый метод и сразу реализовать блок с кодом
Классы могут переопределить метод по умолчанию
Метод по умолчанию объявляется с помощью ключевого слова <code>default</code></p>
<div class="code_element"><div class="lang_line"><text>java</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-java"><div class="highlight"><pre><span></span><span class="kd">interface</span> <span class="nc">IDefault</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="k">default</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="nf">print</span><span class="p">()</span><span class="w"> </span><span class="p">{</span>
<span class="w">        </span><span class="n">System</span><span class="p">.</span><span class="na">out</span><span class="p">.</span><span class="na">println</span><span class="p">(</span><span class="s">&quot;Привет&quot;</span><span class="p">);</span>
<span class="w">    </span><span class="p">}</span>
<span class="p">}</span>

<span class="kd">class</span> <span class="nc">L</span><span class="w"> </span><span class="kd">implements</span><span class="w"> </span><span class="n">IDefault</span><span class="w"> </span><span class="p">{</span>

<span class="p">}</span>

<span class="kd">class</span> <span class="nc">M</span><span class="w"> </span><span class="kd">implements</span><span class="w"> </span><span class="n">IDefault</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="nd">@Override</span>
<span class="w">    </span><span class="kd">public</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="nf">print</span><span class="p">()</span><span class="w"> </span><span class="p">{</span>
<span class="w">        </span><span class="n">System</span><span class="p">.</span><span class="na">out</span><span class="p">.</span><span class="na">println</span><span class="p">(</span><span class="s">&quot;Прощай&quot;</span><span class="p">);</span>
<span class="w">    </span><span class="p">}</span>
<span class="p">}</span>

<span class="kd">public</span><span class="w"> </span><span class="kd">class</span> <span class="nc">MyClass</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="kd">public</span><span class="w"> </span><span class="kd">static</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="nf">main</span><span class="p">(</span><span class="n">String</span><span class="o">[]</span><span class="w"> </span><span class="n">args</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">        </span><span class="n">L</span><span class="w"> </span><span class="n">obj</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="k">new</span><span class="w"> </span><span class="n">L</span><span class="p">();</span>
<span class="w">        </span><span class="n">obj</span><span class="p">.</span><span class="na">print</span><span class="p">();</span><span class="w"> </span><span class="c1">// Привет</span>
<span class="w">        </span><span class="n">M</span><span class="w"> </span><span class="n">obj2</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="k">new</span><span class="w"> </span><span class="n">M</span><span class="p">();</span>
<span class="w">        </span><span class="n">obj2</span><span class="p">.</span><span class="na">print</span><span class="p">();</span><span class="w"> </span><span class="c1">// Прощай</span>
<span class="w">    </span><span class="p">}</span>
<span class="p">}</span>
</pre></div></div></div>

<h2>Коллизия имён</h2>
<div class="code_element"><div class="lang_line"><text>java</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-java"><div class="highlight"><pre><span></span><span class="kd">interface</span> <span class="nc">IDefault2</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="k">default</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="nf">print</span><span class="p">()</span><span class="w"> </span><span class="p">{</span>
<span class="w">        </span><span class="n">System</span><span class="p">.</span><span class="na">out</span><span class="p">.</span><span class="na">println</span><span class="p">(</span><span class="s">&quot;Привет, Вася&quot;</span><span class="p">);</span>
<span class="w">    </span><span class="p">}</span>
<span class="p">}</span>

<span class="kd">class</span> <span class="nc">N</span><span class="w"> </span><span class="kd">implements</span><span class="w"> </span><span class="n">IDefault</span><span class="p">,</span><span class="w"> </span><span class="n">IDefault2</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="nd">@Override</span>
<span class="w">    </span><span class="kd">public</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="nf">print</span><span class="p">()</span><span class="w"> </span><span class="p">{</span>
<span class="w">        </span><span class="n">IDefault</span><span class="p">.</span><span class="na">super</span><span class="p">.</span><span class="na">print</span><span class="p">();</span>
<span class="w">        </span><span class="n">IDefault2</span><span class="p">.</span><span class="na">super</span><span class="p">.</span><span class="na">print</span><span class="p">();</span>
<span class="w">    </span><span class="p">}</span>
<span class="p">}</span>

<span class="kd">public</span><span class="w"> </span><span class="kd">class</span> <span class="nc">MyClass</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="kd">public</span><span class="w"> </span><span class="kd">static</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="nf">main</span><span class="p">(</span><span class="n">String</span><span class="o">[]</span><span class="w"> </span><span class="n">args</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">        </span><span class="n">N</span><span class="w"> </span><span class="n">obj</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="k">new</span><span class="w"> </span><span class="n">N</span><span class="p">();</span>
<span class="w">        </span><span class="n">obj</span><span class="p">.</span><span class="na">print</span><span class="p">();</span><span class="w"> </span><span class="c1">// Привет</span>
<span class="w">                     </span><span class="c1">// Привет, Вася</span>
<span class="w">    </span><span class="p">}</span>
<span class="p">}</span>
</pre></div></div></div>

<h3>Example</h3>
<div class="code_element"><div class="lang_line"><text>java</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-java"><div class="highlight"><pre><span></span><span class="kd">public</span><span class="w"> </span><span class="kd">interface</span> <span class="nc">ILights</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="kt">boolean</span><span class="w"> </span><span class="n">isOn</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="kc">false</span><span class="p">;</span>
<span class="w">    </span><span class="kt">void</span><span class="w"> </span><span class="nf">setLight</span><span class="w"> </span><span class="p">(</span><span class="kt">boolean</span><span class="w"> </span><span class="n">set</span><span class="p">);</span>
<span class="p">}</span>
</pre></div></div></div>

<div class="code_element"><div class="lang_line"><text>java</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-java"><div class="highlight"><pre><span></span><span class="kd">interface</span> <span class="nc">MyInterface</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="kt">int</span><span class="w"> </span><span class="n">MY_CONSTANT</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">10</span><span class="p">;</span>

<span class="w">    </span><span class="k">default</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="nf">defaultMethod</span><span class="p">(</span><span class="n">String</span><span class="w"> </span><span class="n">argument</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">        </span><span class="n">System</span><span class="p">.</span><span class="na">out</span><span class="p">.</span><span class="na">println</span><span class="p">(</span><span class="s">&quot;Value of argument: &quot;</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">argument</span><span class="p">);</span>
<span class="w">        </span><span class="n">System</span><span class="p">.</span><span class="na">out</span><span class="p">.</span><span class="na">println</span><span class="p">(</span><span class="s">&quot;Value of MY_CONSTANT: &quot;</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">MY_CONSTANT</span><span class="p">);</span>
<span class="w">    </span><span class="p">}</span>
<span class="p">}</span>

<span class="kd">class</span> <span class="nc">MyClass</span><span class="w"> </span><span class="kd">implements</span><span class="w"> </span><span class="n">MyInterface</span><span class="w"> </span><span class="p">{}</span>

<span class="kd">public</span><span class="w"> </span><span class="kd">class</span> <span class="nc">Main</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="kd">public</span><span class="w"> </span><span class="kd">static</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="nf">main</span><span class="p">(</span><span class="n">String</span><span class="o">[]</span><span class="w"> </span><span class="n">args</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">        </span><span class="n">MyClass</span><span class="w"> </span><span class="n">myObject</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="k">new</span><span class="w"> </span><span class="n">MyClass</span><span class="p">();</span>
<span class="w">        </span><span class="n">myObject</span><span class="p">.</span><span class="na">defaultMethod</span><span class="p">(</span><span class="s">&quot;Text&quot;</span><span class="p">);</span>
<span class="w">        </span><span class="c1">// Value of argument: Text</span>
<span class="w">        </span><span class="c1">// Value of MY_CONSTANT: 10</span>
<span class="w">    </span><span class="p">}</span>
<span class="p">}</span>
</pre></div></div></div>