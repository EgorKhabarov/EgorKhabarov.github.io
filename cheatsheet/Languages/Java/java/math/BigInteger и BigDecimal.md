<p>Предназначены для работы с большими числами, которые выходят за пределы типа <code>int</code> или <code>double</code>
а также для работы с высокой точностью</p>
<h1>BigInteger</h1>
<p>Класс для работы с целыми числами произвольной длины</p>
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
<td><code>BigInteger(String val)</code></td>
<td>Создает объект из строки</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="n">BigInteger</span><span class="w"> </span><span class="n">num</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="k">new</span><span class="w"> </span><span class="n">BigInteger</span><span class="p">(</span><span class="s">&quot;12345678901234567890&quot;</span><span class="p">);</span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td><code>BigInteger.valueOf(long val)</code></td>
<td>Создает объект из <code>long</code></td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="n">BigInteger</span><span class="w"> </span><span class="n">num</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">BigInteger</span><span class="p">.</span><span class="na">valueOf</span><span class="p">(</span><span class="mi">42</span><span class="p">);</span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td><code>add(BigInteger val)</code></td>
<td>Складывает два числа</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="n">BigInteger</span><span class="w"> </span><span class="n">sum</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">a</span><span class="p">.</span><span class="na">add</span><span class="p">(</span><span class="n">b</span><span class="p">);</span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td><code>subtract(BigInteger val)</code></td>
<td>Вычитает одно число из другого</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="n">BigInteger</span><span class="w"> </span><span class="n">diff</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">a</span><span class="p">.</span><span class="na">subtract</span><span class="p">(</span><span class="n">b</span><span class="p">);</span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td><code>multiply(BigInteger val)</code></td>
<td>Умножает два числа</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="n">BigInteger</span><span class="w"> </span><span class="n">product</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">a</span><span class="p">.</span><span class="na">multiply</span><span class="p">(</span><span class="n">b</span><span class="p">);</span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td><code>divide(BigInteger val)</code></td>
<td>Делит одно число на другое (целочисленное деление)</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="n">BigInteger</span><span class="w"> </span><span class="n">quotient</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">a</span><span class="p">.</span><span class="na">divide</span><span class="p">(</span><span class="n">b</span><span class="p">);</span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td><code>remainder(BigInteger val)</code></td>
<td>Остаток от деления</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="n">BigInteger</span><span class="w"> </span><span class="n">rem</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">a</span><span class="p">.</span><span class="na">remainder</span><span class="p">(</span><span class="n">b</span><span class="p">);</span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td><code>divideAndRemainder(BigInteger val)</code></td>
<td>Возвращает массив с результатом<br>целочисленного деления и остатком</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="n">BigInteger</span><span class="o">[]</span><span class="w"> </span><span class="n">result</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">a</span><span class="p">.</span><span class="na">divideAndRemainder</span><span class="p">(</span><span class="n">b</span><span class="p">);</span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td><code>pow(int exponent)</code></td>
<td>Возводит число в степень</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="n">BigInteger</span><span class="w"> </span><span class="n">power</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">a</span><span class="p">.</span><span class="na">pow</span><span class="p">(</span><span class="mi">3</span><span class="p">);</span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td><code>mod(BigInteger val)</code></td>
<td>Остаток от деления для положительных чисел (модуль)</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="n">BigInteger</span><span class="w"> </span><span class="n">mod</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">a</span><span class="p">.</span><span class="na">mod</span><span class="p">(</span><span class="n">b</span><span class="p">);</span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td><code>gcd(BigInteger val)</code></td>
<td>НОД двух чисел</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="n">BigInteger</span><span class="w"> </span><span class="n">gcd</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">a</span><span class="p">.</span><span class="na">gcd</span><span class="p">(</span><span class="n">b</span><span class="p">);</span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td><code>abs()</code></td>
<td>Возвращает абсолютное значение числа</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="n">BigInteger</span><span class="w"> </span><span class="n">absVal</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">a</span><span class="p">.</span><span class="na">abs</span><span class="p">();</span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td><code>negate()</code></td>
<td>Возвращает отрицательное значение числа</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="n">BigInteger</span><span class="w"> </span><span class="n">neg</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">a</span><span class="p">.</span><span class="na">negate</span><span class="p">();</span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td><code>compareTo(BigInteger val)</code></td>
<td>Сравнивает числа: <code>-1</code> (меньше),<br><code>0</code> (равны), <code>1</code> (больше)</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="kt">int</span><span class="w"> </span><span class="n">cmp</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">a</span><span class="p">.</span><span class="na">compareTo</span><span class="p">(</span><span class="n">b</span><span class="p">);</span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td><code>toString()</code></td>
<td>Преобразует число в строку</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="n">String</span><span class="w"> </span><span class="n">str</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">a</span><span class="p">.</span><span class="na">toString</span><span class="p">();</span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td><code>isProbablePrime(int certainty)</code></td>
<td>Проверяет, является ли число<br>простым с заданной вероятностью</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="kt">boolean</span><span class="w"> </span><span class="n">isPrime</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">a</span><span class="p">.</span><span class="na">isProbablePrime</span><span class="p">(</span><span class="mi">10</span><span class="p">);</span><br></pre></div></pre></div></div></td>
</tr>
</tbody>
</table>
<h3>Пример использования <code>BigInteger</code></h3>
<div class="code_element"><div class="lang_line"><text>java</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-java"><div class="highlight"><pre><span></span><span class="kn">import</span><span class="w"> </span><span class="nn">java.math.BigInteger</span><span class="p">;</span>

<span class="kd">public</span><span class="w"> </span><span class="kd">class</span> <span class="nc">BigIntegerExample</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="kd">public</span><span class="w"> </span><span class="kd">static</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="nf">main</span><span class="p">(</span><span class="n">String</span><span class="o">[]</span><span class="w"> </span><span class="n">args</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">        </span><span class="n">BigInteger</span><span class="w"> </span><span class="n">a</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="k">new</span><span class="w"> </span><span class="n">BigInteger</span><span class="p">(</span><span class="s">&quot;123456789012345678901234567890&quot;</span><span class="p">);</span>
<span class="w">        </span><span class="n">BigInteger</span><span class="w"> </span><span class="n">b</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="k">new</span><span class="w"> </span><span class="n">BigInteger</span><span class="p">(</span><span class="s">&quot;987654321098765432109876543210&quot;</span><span class="p">);</span>

<span class="w">        </span><span class="n">BigInteger</span><span class="w"> </span><span class="n">sum</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">a</span><span class="p">.</span><span class="na">add</span><span class="p">(</span><span class="n">b</span><span class="p">);</span>
<span class="w">        </span><span class="n">BigInteger</span><span class="w"> </span><span class="n">product</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">a</span><span class="p">.</span><span class="na">multiply</span><span class="p">(</span><span class="n">b</span><span class="p">);</span>
<span class="w">        </span><span class="n">BigInteger</span><span class="w"> </span><span class="n">power</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">a</span><span class="p">.</span><span class="na">pow</span><span class="p">(</span><span class="mi">2</span><span class="p">);</span>

<span class="w">        </span><span class="n">System</span><span class="p">.</span><span class="na">out</span><span class="p">.</span><span class="na">println</span><span class="p">(</span><span class="s">&quot;Сумма: &quot;</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">sum</span><span class="p">);</span>
<span class="w">        </span><span class="n">System</span><span class="p">.</span><span class="na">out</span><span class="p">.</span><span class="na">println</span><span class="p">(</span><span class="s">&quot;Произведение: &quot;</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">product</span><span class="p">);</span>
<span class="w">        </span><span class="n">System</span><span class="p">.</span><span class="na">out</span><span class="p">.</span><span class="na">println</span><span class="p">(</span><span class="s">&quot;Квадрат: &quot;</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">power</span><span class="p">);</span>
<span class="w">    </span><span class="p">}</span>
<span class="p">}</span>
<span class="c1">// Сумма: 1111111110111111111011111111100</span>
<span class="c1">// Произведение: 121932631137021795226185032733622923332237463801111263526900</span>
<span class="c1">// Квадрат: 15241578753238836750495351562536198787501905199875019052100</span>
</pre></div></div></div>

<h1>BigDecimal</h1>
<p>Класс для работы с числами с плавающей точкой произвольной точности</p>
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
<td><code>BigDecimal(String val)</code></td>
<td>Создает объект из строки</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="n">BigDecimal</span><span class="w"> </span><span class="n">num</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="k">new</span><span class="w"> </span><span class="n">BigDecimal</span><span class="p">(</span><span class="s">&quot;12345.6789&quot;</span><span class="p">);</span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td><code>BigDecimal.valueOf(double val)</code></td>
<td>Создает объект из <code>double</code></td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="n">BigDecimal</span><span class="w"> </span><span class="n">num</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">BigDecimal</span><span class="p">.</span><span class="na">valueOf</span><span class="p">(</span><span class="mf">12345.6789</span><span class="p">);</span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td><code>add(BigDecimal val)</code></td>
<td>Складывает два числа</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="n">BigDecimal</span><span class="w"> </span><span class="n">sum</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">a</span><span class="p">.</span><span class="na">add</span><span class="p">(</span><span class="n">b</span><span class="p">);</span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td><code>subtract(BigDecimal val)</code></td>
<td>Вычитает одно число из другого</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="n">BigDecimal</span><span class="w"> </span><span class="n">diff</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">a</span><span class="p">.</span><span class="na">subtract</span><span class="p">(</span><span class="n">b</span><span class="p">);</span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td><code>multiply(BigDecimal val)</code></td>
<td>Умножает два числа</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="n">BigDecimal</span><span class="w"> </span><span class="n">product</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">a</span><span class="p">.</span><span class="na">multiply</span><span class="p">(</span><span class="n">b</span><span class="p">);</span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td><code>divide(BigDecimal val, int scale,</code><br><code>RoundingMode roundingMode)</code></td>
<td>Делит числа с указанием<br>точности и метода округления</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="n">BigDecimal</span><span class="w"> </span><span class="n">quotient</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">a</span><span class="p">.</span><span class="na">divide</span><span class="p">(</span><span class="n">b</span><span class="p">,</span><span class="w"> </span><span class="mi">2</span><span class="p">,</span><span class="w"> </span><span class="n">RoundingMode</span><span class="p">.</span><span class="na">HALF_UP</span><span class="p">);</span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td><code>remainder(BigDecimal val)</code></td>
<td>Остаток от деления</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="n">BigDecimal</span><span class="w"> </span><span class="n">rem</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">a</span><span class="p">.</span><span class="na">remainder</span><span class="p">(</span><span class="n">b</span><span class="p">);</span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td><code>setScale(int newScale,</code><br><code>RoundingMode roundingMode)</code></td>
<td>Изменяет точность числа с указанием метода округления</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="n">BigDecimal</span><span class="w"> </span><span class="n">scaled</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">a</span><span class="p">.</span><span class="na">setScale</span><span class="p">(</span><span class="mi">2</span><span class="p">,</span><span class="w"> </span><span class="n">RoundingMode</span><span class="p">.</span><span class="na">HALF_UP</span><span class="p">);</span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td><code>compareTo(BigDecimal val)</code></td>
<td>Сравнивает числа: <code>-1</code> (меньше),<br><code>0</code> (равны), <code>1</code> (больше)</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="kt">int</span><span class="w"> </span><span class="n">cmp</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">a</span><span class="p">.</span><span class="na">compareTo</span><span class="p">(</span><span class="n">b</span><span class="p">);</span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td><code>toString()</code></td>
<td>Преобразует число в строку</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="n">String</span><span class="w"> </span><span class="n">str</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">a</span><span class="p">.</span><span class="na">toString</span><span class="p">();</span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td><code>scale()</code></td>
<td>Возвращает текущую точность числа</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="kt">int</span><span class="w"> </span><span class="n">scale</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">a</span><span class="p">.</span><span class="na">scale</span><span class="p">();</span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td><code>precision()</code></td>
<td>Возвращает общее количество значащих цифр</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="kt">int</span><span class="w"> </span><span class="n">precision</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">a</span><span class="p">.</span><span class="na">precision</span><span class="p">();</span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td><code>stripTrailingZeros()</code></td>
<td>Убирает незначащие нули после запятой</td>
<td><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="n">BigDecimal</span><span class="w"> </span><span class="n">stripped</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">a</span><span class="p">.</span><span class="na">stripTrailingZeros</span><span class="p">();</span><br></pre></div></pre></div></div></td>
</tr>
</tbody>
</table>
<h3>Пример использования <code>BigDecimal</code></h3>
<div class="code_element"><div class="lang_line"><text>java</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-java"><div class="highlight"><pre><span></span><span class="kn">import</span><span class="w"> </span><span class="nn">java.math.BigDecimal</span><span class="p">;</span>
<span class="kn">import</span><span class="w"> </span><span class="nn">java.math.RoundingMode</span><span class="p">;</span>

<span class="kd">public</span><span class="w"> </span><span class="kd">class</span> <span class="nc">BigDecimalExample</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="kd">public</span><span class="w"> </span><span class="kd">static</span><span class="w"> </span><span class="kt">void</span><span class="w"> </span><span class="nf">main</span><span class="p">(</span><span class="n">String</span><span class="o">[]</span><span class="w"> </span><span class="n">args</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">        </span><span class="n">BigDecimal</span><span class="w"> </span><span class="n">a</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="k">new</span><span class="w"> </span><span class="n">BigDecimal</span><span class="p">(</span><span class="s">&quot;12345.6789&quot;</span><span class="p">);</span>
<span class="w">        </span><span class="n">BigDecimal</span><span class="w"> </span><span class="n">b</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="k">new</span><span class="w"> </span><span class="n">BigDecimal</span><span class="p">(</span><span class="s">&quot;0.001&quot;</span><span class="p">);</span>

<span class="w">        </span><span class="n">BigDecimal</span><span class="w"> </span><span class="n">sum</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">a</span><span class="p">.</span><span class="na">add</span><span class="p">(</span><span class="n">b</span><span class="p">);</span>
<span class="w">        </span><span class="n">BigDecimal</span><span class="w"> </span><span class="n">diff</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">a</span><span class="p">.</span><span class="na">subtract</span><span class="p">(</span><span class="n">b</span><span class="p">);</span>
<span class="w">        </span><span class="n">BigDecimal</span><span class="w"> </span><span class="n">scaled</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">a</span><span class="p">.</span><span class="na">setScale</span><span class="p">(</span><span class="mi">2</span><span class="p">,</span><span class="w"> </span><span class="n">RoundingMode</span><span class="p">.</span><span class="na">HALF_UP</span><span class="p">);</span>

<span class="w">        </span><span class="n">System</span><span class="p">.</span><span class="na">out</span><span class="p">.</span><span class="na">println</span><span class="p">(</span><span class="s">&quot;Сумма: &quot;</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">sum</span><span class="p">);</span>
<span class="w">        </span><span class="n">System</span><span class="p">.</span><span class="na">out</span><span class="p">.</span><span class="na">println</span><span class="p">(</span><span class="s">&quot;Разность: &quot;</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">diff</span><span class="p">);</span>
<span class="w">        </span><span class="n">System</span><span class="p">.</span><span class="na">out</span><span class="p">.</span><span class="na">println</span><span class="p">(</span><span class="s">&quot;С округлением: &quot;</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">scaled</span><span class="p">);</span>
<span class="w">    </span><span class="p">}</span>
<span class="p">}</span>
</pre></div></div></div>

<h3>Заметки</h3>
<ol>
<li>Не использовать <code>double</code> или <code>float</code> в конструкторе <code>BigDecimal</code> <div class="code_element"><div class="lang_line"><text>java</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-java"><div class="highlight"><pre><span></span><span class="n">BigDecimal</span><span class="w"> </span><span class="n">a</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="k">new</span><span class="w"> </span><span class="n">BigDecimal</span><span class="p">(</span><span class="mf">0.1</span><span class="p">);</span><span class="w"> </span><span class="c1">// Неточно!</span>
<span class="n">BigDecimal</span><span class="w"> </span><span class="n">b</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="k">new</span><span class="w"> </span><span class="n">BigDecimal</span><span class="p">(</span><span class="s">&quot;0.1&quot;</span><span class="p">);</span><span class="w"> </span><span class="c1">// Точно</span>
</pre></div></div></div></li>
<li>Методы округления (<code>RoundingMode</code>)<ul>
<li><code>RoundingMode.HALF_UP</code> — округление "по математическим правилам"</li>
<li><code>RoundingMode.FLOOR</code> — округление вниз</li>
<li><code>RoundingMode.CEILING</code> — округление вверх</li>
</ul>
</li>
</ol>