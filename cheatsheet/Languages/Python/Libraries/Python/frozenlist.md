<p>Описание: библиотека "frozenlist" служит для создания неизменяемых списков в Python,
аналогично тому, как <code>tuple</code> предоставляет неизменяемую версию <code>list</code>.</p>
<p>Таблица методов:</p>
<table>
<thead>
<tr>
<th>Метод</th>
<th>Описание</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>init</strong>()</td>
<td>Инициализирует новый объект frozenlist.</td>
</tr>
<tr>
<td><strong>contains</strong>()</td>
<td>Проверяет наличие элемента в списке.</td>
</tr>
<tr>
<td><strong>getitem</strong>()</td>
<td>Получает элемент списка по индексу.</td>
</tr>
<tr>
<td><strong>len</strong>()</td>
<td>Возвращает количество элементов в списке.</td>
</tr>
<tr>
<td>copy()</td>
<td>Возвращает копию frozenlist.</td>
</tr>
</tbody>
</table>
<p>Список самых частых методов, краткое описание и работающие примеры:</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="c1"># Метод __init__()</span>
<span class="n">flist</span> <span class="o">=</span> <span class="n">frozenlist</span><span class="p">([</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">,</span> <span class="mi">4</span><span class="p">,</span> <span class="mi">5</span><span class="p">])</span>
<span class="c1"># Метод __contains__()</span>
<span class="nb">print</span><span class="p">(</span><span class="mi">3</span> <span class="ow">in</span> <span class="n">flist</span><span class="p">)</span>  <span class="c1"># True, так как 3 есть в списке</span>
<span class="c1"># Метод __getitem__()</span>
<span class="nb">print</span><span class="p">(</span><span class="n">flist</span><span class="p">[</span><span class="mi">1</span><span class="p">])</span>    <span class="c1"># 2, так как это элемент на позиции 1</span>
<span class="c1"># Метод __len__()</span>
<span class="nb">print</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">flist</span><span class="p">))</span>  <span class="c1"># 5, так количество элементов в списке равно 5</span>
<span class="c1"># Метод copy()</span>
<span class="n">flist_copy</span> <span class="o">=</span> <span class="n">flist</span><span class="o">.</span><span class="n">copy</span><span class="p">()</span>  <span class="c1"># Создаст копию списка</span>
</pre></div></div></div>

<p>Пожалуйста, убедитесь, что установлена библиотека <code>frozenlist</code>.
Если нет, используйте данную команду для установки - <code>pip install frozenlist</code>.</p>