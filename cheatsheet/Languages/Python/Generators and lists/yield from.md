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
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" onclick="copyCode(this)"><svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="k">def</span> <span class="nf">generator1</span><span class="p">():</span>
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