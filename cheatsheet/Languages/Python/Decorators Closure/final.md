<p><code>@final</code> - это аннотация (декоратор) в Python, которая указывает, что метод или свойство класса не должны переопределяться в подклассах.</p>
<p>Когда метод или свойство класса помечаются аннотацией <code>@final</code>, это предупреждает программистов,
что эти элементы класса являются частью публичного интерфейса класса, который не должен изменяться в подклассах.
Это позволяет сделать класс более простым и предсказуемым в использовании, так как гарантируется,
что поведение не будет изменено в производных классах.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">typing</span> <span class="kn">import</span> <span class="n">final</span>


<span class="k">class</span> <span class="nc">BaseClass</span><span class="p">:</span>
    <span class="nd">@final</span>
    <span class="k">def</span> <span class="nf">some_method</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="k">pass</span>

<span class="k">class</span> <span class="nc">DerivedClass</span><span class="p">(</span><span class="n">BaseClass</span><span class="p">):</span>
    <span class="k">def</span> <span class="nf">some_method</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>  <span class="c1"># Ошибка: невозможно переопределить метод</span>
        <span class="k">pass</span>
</pre></div></div></div>

<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">typing</span> <span class="kn">import</span> <span class="n">final</span>

<span class="nd">@final</span>
<span class="k">class</span> <span class="nc">FinalClass</span><span class="p">:</span>
    <span class="k">pass</span>

<span class="k">class</span> <span class="nc">AnotherClass</span><span class="p">(</span><span class="n">FinalClass</span><span class="p">):</span>  <span class="c1"># Ошибка: невозможно наследовать от FinalClass</span>
    <span class="k">pass</span>
</pre></div></div></div>

<blockquote>
<p>Декоратор <code>@final</code> является частью системы типизации Python и,
следовательно, не влияет на выполнение кода в интерпретаторе Python.
Он предназначен для статической проверки и повышения читаемости кода.</p>
</blockquote>