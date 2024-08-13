<table>
<thead>
<tr>
<th style="text-align: left;">Метод</th>
<th style="text-align: left;">Описание</th>
<th style="text-align: left;">Пример вызова</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">int.as_integer_ratio()</td>
<td style="text-align: left;">Возвращает кортеж, представляющий рациональное число,<br>близкое к данному целому числу.</td>
<td style="text-align: left;"><pre><code class="language-python">&gt;&gt;&gt; (10).as_integer_ratio()<br>(10, 1)</code></pre></td>
</tr>
<tr>
<td style="text-align: left;">int.bit_count()</td>
<td style="text-align: left;">Возвращает количество установленных битов (битов со значением 1)<br>в двоичном представлении числа.</td>
<td style="text-align: left;"><pre><code class="language-python">&gt;&gt;&gt; (123).bit_count()<br>6</code></pre></td>
</tr>
<tr>
<td style="text-align: left;">int.bit_length()</td>
<td style="text-align: left;">Возвращает количество битов, необходимых для представления числа в двоичном виде.</td>
<td style="text-align: left;"><pre><code class="language-python">&gt;&gt;&gt; (256).bit_length()<br>9</code></pre></td>
</tr>
<tr>
<td style="text-align: left;">int.conjugate()</td>
<td style="text-align: left;">Возвращает сопряженное комплексное число.</td>
<td style="text-align: left;"><pre><code class="language-python">&gt;&gt;&gt; (3 + 4j).conjugate()<br>(3-4j)</code></pre></td>
</tr>
<tr>
<td style="text-align: left;">int.denominator</td>
<td style="text-align: left;">Возвращает знаменатель числа в виде рациональной дроби.</td>
<td style="text-align: left;"><pre><code class="language-python">&gt;&gt;&gt; (3).denominator<br>1</code></pre></td>
</tr>
<tr>
<td style="text-align: left;">int.from_bytes()</td>
<td style="text-align: left;">Преобразует байтовую последовательность в целое число,<br>используя указанный порядок байтов и знак.</td>
<td style="text-align: left;"><pre><code class="language-python">&gt;&gt;&gt; int.from_bytes(<br>...     b"\x00\x10",<br>...     byteorder="big",<br>...     signed=False<br>... )<br>16</code></pre></td>
</tr>
<tr>
<td style="text-align: left;">int.imag</td>
<td style="text-align: left;">Возвращает мнимую часть комплексного числа.</td>
<td style="text-align: left;"><pre><code class="language-python">&gt;&gt;&gt; (3 + 4j).imag<br>4.0</code></pre></td>
</tr>
<tr>
<td style="text-align: left;">int.numerator</td>
<td style="text-align: left;">Возвращает числитель числа в виде рациональной дроби.</td>
<td style="text-align: left;"><pre><code class="language-python">&gt;&gt;&gt; (3).numerator<br>3</code></pre></td>
</tr>
<tr>
<td style="text-align: left;">int.real</td>
<td style="text-align: left;">Возвращает действительную часть комплексного числа.</td>
<td style="text-align: left;"><pre><code class="language-python">&gt;&gt;&gt; (3 + 4j).real<br>3.0</code></pre></td>
</tr>
<tr>
<td style="text-align: left;">int.to_bytes()</td>
<td style="text-align: left;">Преобразует целое число в байтовую последовательность,<br>используя указанный порядок байтов и знак.</td>
<td style="text-align: left;"><pre><code class="language-python">&gt;&gt;&gt; (1024).to_bytes(<br>...     length=2,<br>...     byteorder="big",<br>...     signed=False<br>... )<br>b"\x04\x00"</code></pre></td>
</tr>
</tbody>
</table>