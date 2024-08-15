<p>Реализации конструкции try catch
Для добавления отслеживания ошибок можно прописать следующий код:</p>
<div class="code-element"><div class="lang-line"><text>cpp</text><button class="copy-button" onclick="copyCode(this)"><svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="k">try</span><span class="w"> </span><span class="p">{</span><span class="w"> </span><span class="c1">// В блоке try мы пытаемся выполнить какой-либо код</span>
<span class="w">    </span><span class="k">if</span><span class="w"> </span><span class="p">(</span><span class="n">variable</span><span class="w"> </span><span class="o">==</span><span class="w"> </span><span class="mi">0</span><span class="p">)</span><span class="w"> </span><span class="c1">// Проверяем делитель на ноль</span>
<span class="w">        </span><span class="k">throw</span><span class="w"> </span><span class="mi">277</span><span class="p">;</span><span class="w"> </span><span class="c1">// Запускаем исключение и передаем в него параметр</span>

<span class="w">    </span><span class="n">cout</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">something</span><span class="w"> </span><span class="o">/</span><span class="w"> </span><span class="n">variable</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">endl</span><span class="p">;</span><span class="w"> </span>
<span class="p">}</span><span class="w"> </span><span class="k">catch</span><span class="p">(</span><span class="kt">int</span><span class="w"> </span><span class="n">i</span><span class="p">)</span><span class="w"> </span><span class="p">{</span><span class="w"> </span><span class="c1">// Здесь отлавливаем переданную ошибку</span>
<span class="w">    </span><span class="n">cout</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;Нам очень повезло!&quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">endl</span><span class="p">;</span>
<span class="w">    </span><span class="n">cout</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot;Нам удалось избежать ошибки с индексом &quot;</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">&lt;&lt;</span><span class="w"> </span><span class="s">&quot; - на 0 делить нельзя!&quot;</span><span class="p">;</span>
<span class="p">}</span>
</pre></div></div></div>

<p>В коде выше представлен очень простой пример использования исключений. 
Не обращайте внимание на его простоту, так как главное это рассмотреть общую конструкцию блока try catch.</p>
<p>При использовании такой конструкции, какая бы ошибка не получилась в ходе программы 
сама программа работать не перестанет и пользователь не получить плохой опыт в её использовании.</p>
<p>Если необходимо отследить несколько классов с ошибками, то можно добавить несколько 
блоков catch. Все они добавляются друг под другом точно также как в условных операторах.</p>