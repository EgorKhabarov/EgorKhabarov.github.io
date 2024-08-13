<p><code>@final</code> - это аннотация (декоратор) в Python, которая указывает, что метод или свойство класса не должны переопределяться в подклассах.</p>
<p>Когда метод или свойство класса помечаются аннотацией <code>@final</code>, это предупреждает программистов, 
что эти элементы класса являются частью публичного интерфейса класса, который не должен изменяться в подклассах. 
Это позволяет сделать класс более простым и предсказуемым в использовании, так как гарантируется, 
что поведение не будет изменено в производных классах.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" onclick="copyCode(this)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">typing</span> <span class="kn">import</span> <span class="n">final</span>


<span class="k">class</span> <span class="nc">BaseClass</span><span class="p">:</span>
    <span class="nd">@final</span>
    <span class="k">def</span> <span class="nf">some_method</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="k">pass</span>

<span class="k">class</span> <span class="nc">DerivedClass</span><span class="p">(</span><span class="n">BaseClass</span><span class="p">):</span>
    <span class="k">def</span> <span class="nf">some_method</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>  <span class="c1"># Ошибка: невозможно переопределить метод</span>
        <span class="k">pass</span>
</pre></div></div></div>

<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" onclick="copyCode(this)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">typing</span> <span class="kn">import</span> <span class="n">final</span>

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