<p>with
В начале блока кода with вызывает метод <strong>enter</strong> у объекта,
который используется для подготовки контекста.
После того как код внутри блока завершился, вызывается метод <strong>exit</strong>,
который используется для освобождения ресурсов.
Контекстный менеджер with удобен для использования,
так как он автоматически освобождает ресурсы в конце блока кода, что избавляет
от необходимости ручного закрытия файла или освобождения других ресурсов.
Контекстный менеджер with может быть использован не только с файлами,
но и с другими объектами, которые поддерживают методы <strong>enter</strong> и <strong>exit</strong>.
Например, он может быть использован для управления блокировками,
сетевыми соединениями и т.д.</p>
<div class="code-element">
    <div class="lang-line">python<button class="copy-button"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg">
    <path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button>
    </div>
    <div class="code"><div class="highlight"><pre><span></span><span class="k">class</span> <span class="nc">Writer</span><span class="p">(</span><span class="nb">object</span><span class="p">):</span>
    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">path</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">path</span> <span class="o">=</span> <span class="n">path</span>

    <span class="k">def</span> <span class="fm">__enter__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">file</span> <span class="o">=</span> <span class="nb">open</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">path</span><span class="p">,</span> <span class="s1">&#39;w&#39;</span><span class="p">,</span> <span class="n">encoding</span><span class="o">=</span><span class="s1">&#39;UTF-8&#39;</span><span class="p">)</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">file</span>

    <span class="k">def</span> <span class="fm">__exit__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">file</span><span class="o">.</span><span class="n">close</span><span class="p">()</span>

<span class="k">with</span> <span class="n">Writer</span><span class="p">(</span><span class="s1">&#39;my_file.txt&#39;</span><span class="p">)</span> <span class="k">as</span> <span class="n">file</span><span class="p">:</span>
    <span class="n">file</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="s1">&#39;hello world&#39;</span><span class="p">)</span>
</pre></div></div>
</div>