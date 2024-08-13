<h1>yield from</h1>
<p>Это выражение, которое позволяет делегировать выполнение
генератора другому генератору, который называется <strong>подгенератором</strong>. 
Это означает, что когда генератор встречает выражение <code>yield from</code> с указанием <strong>подгенератора</strong>,
он передает управление этому <strong>подгенератору</strong>, 
который затем возвращает значения генерируемых им элементов непосредственно в генератор-делегат.</p>
<p>Кроме того, <code>yield from</code> позволяет пропустить передачу через промежуточный уровень вложенности. 
Это означает, что когда подгенератор завершает свою работу, управление передается автоматически обратно генератору-делегату. 
Это может быть полезно в случаях, когда вы хотите объединить несколько генераторов вместе,
чтобы создать новый генератор, который генерирует элементы из каждого из них.</p>
<p>Вот пример, который демонстрирует использование yield from:</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" onclick="copyCode(this)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code"><div class="highlight"><pre><span></span><span class="k">def</span> <span class="nf">generator1</span><span class="p">():</span>
    <span class="k">yield</span> <span class="s2">&quot;A&quot;</span>
    <span class="k">yield</span> <span class="s2">&quot;B&quot;</span>
    <span class="k">yield</span> <span class="s2">&quot;C&quot;</span>

<span class="k">def</span> <span class="nf">generator2</span><span class="p">():</span>
    <span class="k">yield</span> <span class="s2">&quot;D&quot;</span>
    <span class="k">yield from</span> <span class="n">generator1</span><span class="p">()</span>
    <span class="k">yield</span> <span class="s2">&quot;E&quot;</span>
    <span class="k">yield</span> <span class="s2">&quot;F&quot;</span>

<span class="p">[</span><span class="n">letter</span> <span class="k">for</span> <span class="n">letter</span> <span class="ow">in</span> <span class="n">generator2</span><span class="p">()]</span>
<span class="c1"># [&quot;D&quot;, &quot;A&quot;, &quot;B&quot;, &quot;C&quot;, &quot;E&quot;, &quot;F&quot;]</span>
</pre></div></div></div>

<p>Здесь <code>generator2</code> создает новый генератор, используя <code>yield from</code> 
для вызова генератора <code>generator1</code> и объединения его с другими элементами, которые генерирует <code>generator2</code>. 
Когда <code>generator1</code> завершает свою работу, управление автоматически возвращается обратно в <code>generator2</code>,
который продолжает генерировать свои элементы.</p>