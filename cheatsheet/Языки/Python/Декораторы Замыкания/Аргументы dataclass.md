<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code896317683bb531e8e4f04777af4b8d78b" onclick="copyCode(code896317683bb531e8e4f04777af4b8d78, code896317683bb531e8e4f04777af4b8d78b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code896317683bb531e8e4f04777af4b8d78"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">dataclasses</span> <span class="kn">import</span> <span class="n">dataclass</span>
</pre></div></div></div>

<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code600a339137a42676b4d8afa00638f5d1b" onclick="copyCode(code600a339137a42676b4d8afa00638f5d1, code600a339137a42676b4d8afa00638f5d1b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code600a339137a42676b4d8afa00638f5d1"><div class="highlight"><pre><span></span><span class="n">dataclass</span><span class="p">(</span><span class="o">*</span><span class="p">,</span>
          <span class="n">init</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="o">...</span><span class="p">,</span>
          <span class="nb">repr</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="o">...</span><span class="p">,</span>
          <span class="n">eq</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="o">...</span><span class="p">,</span>
          <span class="n">order</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="o">...</span><span class="p">,</span>
          <span class="n">unsafe_hash</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="o">...</span><span class="p">,</span>
          <span class="n">frozen</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="o">...</span><span class="p">)</span>
</pre></div></div></div>

<p>init         Нужно ли автоматически генерировать метод &#95;&#95;init&#95;&#95; для инициализации атрибутов класса.
repr         Нужно ли автоматически генерировать метод &#95;&#95;repr&#95;&#95; для вывода строкового представления объектов класса.
eq           Нужно ли автоматически генерировать метод &#95;&#95;eq&#95;&#95; для сравнения объектов класса.
order        Нужно ли автоматически генерировать методы &#95;&#95;lt&#95;&#95;, &#95;&#95;le&#95;&#95;, &#95;&#95;gt&#95;&#95;, &#95;&#95;ge&#95;&#95; для сравнения объектов класса.
unsafe_hash  Нужно ли автоматически генерировать метод &#95;&#95;hash&#95;&#95; для объектов класса.
             Обычно этот аргумент следует использовать только для классов, объекты которых неизменяемы (frozen),
             так как изменяемые объекты могут привести к неожиданным результатам.
frozen       Нужно ли сделать объекты класса неизменяемыми (immutable).</p>
<p>Все эти аргументы являются необязательными, и если их не указывать,
то будут использованы значения по умолчанию (True для init, repr, eq, order, unsafe_hash и False для frozen).</p>