<h1>:: method reference</h1>
<p>Указание на метод без его вызова.</p>
<div class="code_element"><div class="lang_line"><text>java</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-java"><div class="highlight"><pre><span></span><span class="kd">public</span><span class="w"> </span><span class="kd">class</span> <span class="nc">MyClass</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="kd">public</span><span class="w"> </span><span class="kd">static</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="nf">main</span><span class="p">(</span><span class="n">String</span><span class="o">[]</span><span class="w"> </span><span class="n">args</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">        </span><span class="n">MyButton</span><span class="w"> </span><span class="n">button</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="k">new</span><span class="w"> </span><span class="n">MyButton</span><span class="p">();</span>
<span class="w">        </span><span class="n">A</span><span class="w"> </span><span class="n">a</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="k">new</span><span class="w"> </span><span class="n">A</span><span class="p">();</span>
<span class="w">        </span><span class="n">button</span><span class="p">.</span><span class="na">reg</span><span class="p">(</span><span class="n">a</span><span class="p">::</span><span class="n">printOnClick</span><span class="p">);</span><span class="w"> </span><span class="c1">// Передаем ссылку на метод</span>
<span class="w">        </span><span class="k">for</span><span class="w"> </span><span class="p">(</span><span class="kt">int</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span><span class="w"> </span><span class="n">i</span><span class="w"> </span><span class="o">&lt;</span><span class="w"> </span><span class="mi">5</span><span class="p">;</span><span class="w"> </span><span class="n">i</span><span class="o">++</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">            </span><span class="n">button</span><span class="p">.</span><span class="na">click</span><span class="p">();</span><span class="w"> </span><span class="c1">// Генерируем нажатие</span>
<span class="w">            </span><span class="k">try</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="n">Thread</span><span class="p">.</span><span class="na">sleep</span><span class="p">(</span><span class="mi">1000</span><span class="p">);</span><span class="w"> </span><span class="c1">// Имитация ожидания</span>
<span class="w">            </span><span class="p">}</span>
<span class="w">            </span><span class="k">catch</span><span class="w"> </span><span class="p">(</span><span class="n">InterruptedException</span><span class="w"> </span><span class="n">e</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="n">e</span><span class="p">.</span><span class="na">printStackTrace</span><span class="p">();</span>
<span class="w">                </span><span class="n">System</span><span class="p">.</span><span class="na">exit</span><span class="p">(</span><span class="mi">1</span><span class="p">);</span>
<span class="w">            </span><span class="p">}</span>
<span class="w">        </span><span class="p">}</span>
<span class="w">    </span><span class="p">}</span>
<span class="p">}</span>

<span class="kd">interface</span> <span class="nc">IClick</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="kt">void</span><span class="w"> </span><span class="nf">onClick</span><span class="p">();</span>
<span class="p">}</span>

<span class="kd">class</span> <span class="nc">A</span><span class="w"> </span><span class="p">{</span>
<span class="w">     </span><span class="kd">private</span><span class="w"> </span><span class="kt">int</span><span class="w"> </span><span class="n">x</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">10</span><span class="p">;</span>
<span class="w">     </span><span class="kd">public</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="nf">printOnClick</span><span class="p">()</span><span class="w"> </span><span class="p">{</span>
<span class="w">        </span><span class="n">System</span><span class="p">.</span><span class="na">out</span><span class="p">.</span><span class="na">println</span><span class="p">(</span><span class="s">&quot;Нажата кнопка. x = &quot;</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="k">this</span><span class="p">.</span><span class="na">x</span><span class="p">);</span>
<span class="w">        </span><span class="k">this</span><span class="p">.</span><span class="na">x</span><span class="o">++</span><span class="p">;</span>
<span class="w">     </span><span class="p">}</span>
<span class="p">}</span>

<span class="kd">class</span> <span class="nc">MyButton</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="kd">private</span><span class="w"> </span><span class="n">IClick</span><span class="w"> </span><span class="n">ic</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="kc">null</span><span class="p">;</span>
<span class="w">        </span><span class="kd">public</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="nf">reg</span><span class="p">(</span><span class="n">IClick</span><span class="w"> </span><span class="n">ic</span><span class="p">)</span><span class="w"> </span><span class="p">{</span><span class="w"> </span><span class="c1">// Регистрация обработчика</span>
<span class="w">        </span><span class="k">this</span><span class="p">.</span><span class="na">ic</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">ic</span><span class="p">;</span>
<span class="w">    </span><span class="p">}</span>
<span class="w">    </span><span class="kd">public</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="nf">click</span><span class="p">()</span><span class="w"> </span><span class="p">{</span><span class="w"> </span><span class="c1">// Нажатие кнопки</span>
<span class="w">        </span><span class="k">if</span><span class="w"> </span><span class="p">(</span><span class="k">this</span><span class="p">.</span><span class="na">ic</span><span class="w"> </span><span class="o">!=</span><span class="w"> </span><span class="kc">null</span><span class="p">)</span>
<span class="w">        </span><span class="k">this</span><span class="p">.</span><span class="na">ic</span><span class="p">.</span><span class="na">onClick</span><span class="p">();</span>
<span class="w">    </span><span class="p">}</span>
<span class="p">}</span>
</pre></div></div></div>