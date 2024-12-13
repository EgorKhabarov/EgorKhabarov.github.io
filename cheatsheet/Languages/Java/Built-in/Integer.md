<p><code>Integer</code> — это класс-оболочка для типа <code>int</code> в Java, предоставляющий дополнительные методы для работы с целыми числами.</p>
<p><strong>Примитив vs Объект</strong>: <code>int</code> — примитивный тип, а <code>Integer</code> — класс-оболочка, который может быть <code>null</code> и поддерживает методы.</p>
<p>Преобразование между <code>int</code> и <code>Integer</code> происходит автоматически</p>
<div class="code_element"><div class="lang_line"><text>java</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-java"><div class="highlight"><pre><span></span><span class="n">Integer</span><span class="w"> </span><span class="n">obj</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">42</span><span class="p">;</span><span class="w"> </span><span class="c1">// Автоупаковка</span>
<span class="kt">int</span><span class="w"> </span><span class="n">num</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">obj</span><span class="p">;</span><span class="w">    </span><span class="c1">// Автораспаковка</span>
</pre></div></div></div>

<table>
<thead>
<tr>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td><code>Integer.MIN_VALUE</code></td>
<td><code>-2,147,483,648</code></td>
</tr>
<tr>
<td><code>Integer.MAX_VALUE</code></td>
<td><code>2,147,483,647</code></td>
</tr>
</tbody>
</table>
<table>
<thead>
<tr>
<th>Метод</th>
<th>Описание</th>
<th>Пример использования</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>.valueOf(String s)</code></td>
<td>Преобразует строку в объект <code>Integer</code></td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="n">Integer</span><span class="w"> </span><span class="n">num</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">Integer</span><span class="p">.</span><span class="na">valueOf</span><span class="p">(</span><span class="s">&quot;42&quot;</span><span class="p">);</span><br><span class="c1">// 42</span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td><code>.valueOf(int i)</code></td>
<td>Возвращает объект <code>Integer</code>, представляющий указанное значение <code>int</code></td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="n">Integer</span><span class="w"> </span><span class="n">num</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">Integer</span><span class="p">.</span><span class="na">valueOf</span><span class="p">(</span><span class="mi">42</span><span class="p">);</span><br><span class="c1">// 42</span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td><code>.parseInt(String s)</code></td>
<td>Преобразует строку в примитивное значение <code>int</code></td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="kt">int</span><span class="w"> </span><span class="n">num</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">Integer</span><span class="p">.</span><span class="na">parseInt</span><span class="p">(</span><span class="s">&quot;42&quot;</span><span class="p">);</span><br><span class="c1">// 42</span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td><code>.parseInt</code><br>(String s, int radix)</td>
<td>Преобразует строку в число указанной системы счисления</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="kt">int</span><span class="w"> </span><span class="n">num</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">Integer</span><span class="p">.</span><span class="na">parseInt</span><span class="p">(</span><span class="s">&quot;2A&quot;</span><span class="p">,</span><span class="w"> </span><span class="mi">16</span><span class="p">);</span><br><span class="c1">// 42</span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td><code>.toString(int i)</code></td>
<td>Преобразует число <code>int</code> в строку</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="n">String</span><span class="w"> </span><span class="n">str</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">Integer</span><span class="p">.</span><span class="na">toString</span><span class="p">(</span><span class="mi">42</span><span class="p">);</span><br><span class="c1">// &quot;42&quot;</span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td><code>.toString</code><br>(int i, int radix)</td>
<td>Преобразует число в строку указанной системы счисления</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="n">String</span><span class="w"> </span><span class="n">str</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">Integer</span><span class="p">.</span><span class="na">toString</span><span class="p">(</span><span class="mi">42</span><span class="p">,</span><span class="w"> </span><span class="mi">16</span><span class="p">);</span><br><span class="c1">// &quot;2a&quot;</span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td><code>.compare(int x, int y)</code></td>
<td>Сравнивает два числа.<br>Возвращает <code>0</code>, если равны, &lt; <code>0</code>,<br>если <code>x &lt; y</code>, &gt; <code>0</code>, если <code>x &gt; y</code></td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="kt">int</span><span class="w"> </span><span class="n">result</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">Integer</span><span class="p">.</span><span class="na">compare</span><span class="p">(</span><span class="mi">42</span><span class="p">,</span><span class="w"> </span><span class="mi">24</span><span class="p">);</span><br><span class="c1">// 1</span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td><code>.compareTo</code><br>(Integer another)</td>
<td>Сравнивает текущий объект <code>Integer</code> с другим</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="n">Integer</span><span class="w"> </span><span class="n">num</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">42</span><span class="p">;</span><br><span class="kt">int</span><span class="w"> </span><span class="n">result</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">num</span><span class="p">.</span><span class="na">compareTo</span><span class="p">(</span><span class="mi">24</span><span class="p">);</span><br><span class="c1">// 1</span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td><code>.max(int a, int b)</code></td>
<td>Возвращает большее из двух чисел</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="kt">int</span><span class="w"> </span><span class="n">max</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">Integer</span><span class="p">.</span><span class="na">max</span><span class="p">(</span><span class="mi">42</span><span class="p">,</span><span class="w"> </span><span class="mi">24</span><span class="p">);</span><br><span class="c1">// 42</span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td><code>.min(int a, int b)</code></td>
<td>Возвращает меньшее из двух чисел</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="kt">int</span><span class="w"> </span><span class="n">min</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">Integer</span><span class="p">.</span><span class="na">min</span><span class="p">(</span><span class="mi">42</span><span class="p">,</span><span class="w"> </span><span class="mi">24</span><span class="p">);</span><br><span class="c1">// 24</span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td><code>.sum(int a, int b)</code></td>
<td>Возвращает сумму двух чисел</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="kt">int</span><span class="w"> </span><span class="n">sum</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">Integer</span><span class="p">.</span><span class="na">sum</span><span class="p">(</span><span class="mi">42</span><span class="p">,</span><span class="w"> </span><span class="mi">24</span><span class="p">);</span><br><span class="c1">// 66</span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td><code>.bitCount(int i)</code></td>
<td>Возвращает количество установленных битов<br>в числе (единиц в бинарной записи числа)</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="kt">int</span><span class="w"> </span><span class="n">bits</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">Integer</span><span class="p">.</span><span class="na">bitCount</span><span class="p">(</span><span class="mi">42</span><span class="p">);</span><br><span class="c1">// 3</span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td><code>.highestOneBit(int i)</code></td>
<td>Возвращает число, в котором установлен<br>только самый старший значащий бит исходного числа</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="kt">int</span><span class="w"> </span><span class="n">highBit</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">Integer</span><span class="p">.</span><span class="na">highestOneBit</span><span class="p">(</span><span class="mi">42</span><span class="p">);</span><br><span class="c1">// 32</span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td><code>.lowestOneBit(int i)</code></td>
<td>Возвращает число, в котором установлен<br>только младший значащий бит исходного числа</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="kt">int</span><span class="w"> </span><span class="n">lowBit</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">Integer</span><span class="p">.</span><span class="na">lowestOneBit</span><span class="p">(</span><span class="mi">42</span><span class="p">);</span><br><span class="c1">// 2</span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td><code>.reverse(int i)</code></td>
<td>Возвращает число с битами, расположенными в обратном порядке</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="kt">int</span><span class="w"> </span><span class="n">reversed</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">Integer</span><span class="p">.</span><span class="na">reverse</span><span class="p">(</span><span class="mi">42</span><span class="p">);</span><br><span class="c1">// 1409286144</span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td><code>.reverseBytes(int i)</code></td>
<td>Возвращает число с байтами, расположенными в обратном порядке</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="kt">int</span><span class="w"> </span><span class="n">reversedBytes</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">Integer</span><span class="p">.</span><span class="na">reverseBytes</span><span class="p">(</span><span class="mi">42</span><span class="p">);</span><br><span class="c1">// 704643072</span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td><code>.rotateLeft</code><br>(int i, int distance)</td>
<td>Сдвигает биты числа влево циклически на указанное количество позиций</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="kt">int</span><span class="w"> </span><span class="n">rotated</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">Integer</span><span class="p">.</span><span class="na">rotateLeft</span><span class="p">(</span><span class="mi">42</span><span class="p">,</span><span class="w"> </span><span class="mi">2</span><span class="p">);</span><br><span class="c1">// 168</span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td><code>.rotateRight</code><br>(int i, int distance)</td>
<td>Сдвигает биты числа вправо циклически на указанное количество позиций</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="kt">int</span><span class="w"> </span><span class="n">rotated</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">Integer</span><span class="p">.</span><span class="na">rotateRight</span><span class="p">(</span><span class="mi">42</span><span class="p">,</span><span class="w"> </span><span class="mi">2</span><span class="p">);</span><br><span class="c1">// -2147483638</span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td><code>.signum(int i)</code></td>
<td>Возвращает знак числа: <code>1</code> для положительных,<br><code>-1</code> для отрицательных, <code>0</code> для нуля</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="kt">int</span><span class="w"> </span><span class="n">sign</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">Integer</span><span class="p">.</span><span class="na">signum</span><span class="p">(</span><span class="o">-</span><span class="mi">42</span><span class="p">);</span><br><span class="c1">// -1</span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td><code>.decode(String nm)</code></td>
<td>Преобразует строку с числом в десятичной,<br>шестнадцатеричной или восьмеричной системе в <code>Integer</code></td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="n">Integer</span><span class="w"> </span><span class="n">num</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">Integer</span><span class="p">.</span><span class="na">decode</span><span class="p">(</span><span class="s">&quot;0x2A&quot;</span><span class="p">);</span><br><span class="c1">// 42</span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td><code>.getInteger(String nm)</code></td>
<td>Возвращает значение свойства системы с именем<br><code>nm</code>, интерпретируя его как число</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td><code>.hashCode(int value)</code></td>
<td>Хэш-код для числа</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="kt">int</span><span class="w"> </span><span class="n">hash</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">Integer</span><span class="p">.</span><span class="na">hashCode</span><span class="p">(</span><span class="mi">42</span><span class="p">);</span><br><span class="c1">// 42</span><br></pre></div></pre></div></div></td>
</tr>
</tbody>
</table>