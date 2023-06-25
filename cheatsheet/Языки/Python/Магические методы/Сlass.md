<p>&#95;&#95;_new&#95;&#95;(cls, [...)
    Это первый метод, который будет вызван при инициализации объекта. 
    Он принимает в качестве параметров класс и потом любые другие аргументы, 
    которые будут переданы в &#95;&#95;init&#95;&#95;.&#95;&#95;_new&#95;&#95; используется весьма редко, но иногда бывает полезен, 
    в частности, когда класс наследуется от неизменяемого (immutable) типа, такого как 
    кортеж (tuple) или строка.</p>
<p>&#95;&#95;init&#95;&#95;(self, [...)
    Инициализатор класса. Ему передаётся всё, с чем был вызван первоначальный конструктор 
    (если мы вызываем x = SomeClass(10, 'foo'), &#95;&#95;init&#95;&#95; получит 10 и 'foo' в качестве аргументов. 
    <strong>init</strong> почти повсеместно используется при определении классов.</p>
<p>&#95;&#95;_del&#95;&#95;(self)
    Если&#95;&#95;_new&#95;&#95; и &#95;&#95;init&#95;&#95; образуют конструктор объекта,&#95;&#95;_del&#95;&#95; это его деструктор. 
    Он не определяет поведение для выражения del x (поэтому этот код не эквивалентен x&#95;&#95;_del&#95;&#95;()). 
    Скорее, он определяет поведение объекта в то время, когда объект попадает в сборщик мусора. 
    Это может быть довольно удобно для объектов, которые могут требовать дополнительных чисток 
    во время удаления, таких как сокеты или файловые объекты.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code163b" onclick="copyCode(code163, code163b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code163"><div class="highlight"><pre><span></span><span class="k">class</span> <span class="nc">Class</span><span class="p">:</span>
    <span class="k">def</span> <span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">arg</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">arg</span> <span class="o">=</span> <span class="n">arg</span>

    <span class="k">def</span> <span class="fm">__del__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="k">del</span> <span class="bp">self</span><span class="o">.</span><span class="n">arg</span>
</pre></div></div></div>