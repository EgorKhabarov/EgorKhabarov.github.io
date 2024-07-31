<p>Декоратор <code>@classmethod</code> используется для определения методов класса,
которые принимают первый аргумент в виде самого класса (обычно называемый cls),
а не экземпляра класса (как в случае с методами экземпляра, где первый аргумент называется self).</p>
<p><code>@classmethod</code> позволяет вызывать метод как на экземпляре класса, так и на самом классе.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button"id="code76ce15c3e0b3c88c91d9118847259d60b"onclick="copyCode(code76ce15c3e0b3c88c91d9118847259d60, code76ce15c3e0b3c88c91d9118847259d60b)"><svg stroke="currentColor"fill="none"stroke-width="2"viewBox="0 0 24 24"stroke-linecap="round"stroke-linejoin="round"class="h-4 w-4"height="1em"width="1em"xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code76ce15c3e0b3c88c91d9118847259d60"><div class="highlight"><pre><span></span><span class="k">class</span> <span class="nc">MyClass</span><span class="p">:</span>
    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">foo</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">arg</span><span class="p">):</span>
        <span class="nb">print</span><span class="p">(</span><span class="n">arg</span><span class="p">)</span>

<span class="n">MyClass</span><span class="o">.</span><span class="n">foo</span><span class="p">(</span><span class="mi">5</span><span class="p">)</span>
<span class="n">MyClass</span><span class="p">()</span><span class="o">.</span><span class="n">foo</span><span class="p">(</span><span class="mi">6</span><span class="p">)</span>
</pre></div></div></div>
<p>5
6</p>