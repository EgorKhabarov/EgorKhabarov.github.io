<p>Декоратор <code>@classmethod</code> используется для определения методов класса,
которые принимают первый аргумент в виде самого класса (обычно называемый <code>cls</code>),
а не экземпляра класса (как в случае с методами экземпляра, где первый аргумент называется <code>self</code>).</p>
<p><code>@classmethod</code> позволяет вызывать метод как на экземпляре класса, так и на самом классе.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code"><div class="highlight"><pre><span></span><span class="k">class</span> <span class="nc">MyClass</span><span class="p">:</span>
    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">foo</span><span class="p">(</span><span class="bp">cls</span><span class="p">,</span> <span class="n">arg</span><span class="p">):</span>
        <span class="nb">print</span><span class="p">(</span><span class="n">arg</span><span class="p">)</span>


<span class="n">MyClass</span><span class="o">.</span><span class="n">foo</span><span class="p">(</span><span class="mi">5</span><span class="p">)</span>    <span class="c1"># 5</span>
<span class="n">MyClass</span><span class="p">()</span><span class="o">.</span><span class="n">foo</span><span class="p">(</span><span class="mi">6</span><span class="p">)</span>  <span class="c1"># 6</span>
</pre></div></div></div>