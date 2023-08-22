<table>
<thead>
<tr>
<th style="text-align: left;">Метод</th>
<th style="text-align: left;">Описание</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">int.as_integer_ratio()</td>
<td style="text-align: left;">Возвращает кортеж, представляющий рациональное число, близкое к данному целому числу.</td>
</tr>
<tr>
<td style="text-align: left;">int.bit_count()</td>
<td style="text-align: left;">Возвращает количество установленных битов (битов со значением 1) в двоичном представлении числа.</td>
</tr>
<tr>
<td style="text-align: left;">int.bit_length()</td>
<td style="text-align: left;">Возвращает количество битов, необходимых для представления числа в двоичном виде.</td>
</tr>
<tr>
<td style="text-align: left;">int.conjugate()</td>
<td style="text-align: left;">Возвращает сопряженное комплексное число.</td>
</tr>
<tr>
<td style="text-align: left;">int.denominator</td>
<td style="text-align: left;">Возвращает знаменатель числа в виде рациональной дроби.</td>
</tr>
<tr>
<td style="text-align: left;">int.from_bytes()</td>
<td style="text-align: left;">Преобразует байтовую последовательность в целое число, используя указанный порядок байтов и знак.</td>
</tr>
<tr>
<td style="text-align: left;">int.imag</td>
<td style="text-align: left;">Возвращает мнимую часть комплексного числа.</td>
</tr>
<tr>
<td style="text-align: left;">int.numerator</td>
<td style="text-align: left;">Возвращает числитель числа в виде рациональной дроби.</td>
</tr>
<tr>
<td style="text-align: left;">int.real</td>
<td style="text-align: left;">Возвращает действительную часть комплексного числа.</td>
</tr>
<tr>
<td style="text-align: left;">int.to_bytes()</td>
<td style="text-align: left;">Преобразует целое число в байтовую последовательность, используя указанный порядок байтов и знак.</td>
</tr>
</tbody>
</table>
<table>
<thead>
<tr>
<th style="text-align: left;">Метод</th>
<th style="text-align: left;">Пример вызова</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;">int.as_integer_ratio()</td>
<td style="text-align: left;"><div class="code">x = <span class="m">10</span><br><span class="nb">print</span>(x.as_integer_ratio()) <span class="c1"># (10, 1)</span></div></td>
</tr>
<tr>
<td style="text-align: left;">int.bit_count()</td>
<td style="text-align: left;"><div class="code">x = <span class="m">123</span><br><span class="nb">print</span>(x.bit_count()) <span class="c1"># 6</span></div></td>
</tr>
<tr>
<td style="text-align: left;">int.bit_length()</td>
<td style="text-align: left;"><div class="code">x = <span class="m">256</span><br><span class="nb">print</span>(x.bit_length()) <span class="c1"># 9</span></div></td>
</tr>
<tr>
<td style="text-align: left;">int.conjugate()</td>
<td style="text-align: left;"><div class="code">x = <span class="m">3</span> + <span class="m">4j</span><br><span class="nb">print</span>(x.conjugate()) <span class="c1"># (3-4j)</span></div></td>
</tr>
<tr>
<td style="text-align: left;">int.denominator</td>
<td style="text-align: left;"><div class="code">x = <span class="m">3.5</span><br><span class="nb">print</span>(x.denominator) <span class="c1"># ???</span></div></td>
</tr>
<tr>
<td style="text-align: left;">int.from_bytes()</td>
<td style="text-align: left;"><div class="code">bytes = <span class="s">b'\x00\x10'</span><br><span class="nb">print</span>(int.from_bytes(bytes, <span class="na">byteorder</span>=<span class="s">'big'</span>, <span class="na">signed</span>=<span class="k">False</span>)) <span class="c1"># 16</span></div></td>
</tr>
<tr>
<td style="text-align: left;">int.imag</td>
<td style="text-align: left;"><div class="code">x = <span class="m">3</span> + <span class="m">4j</span><br><span class="nb">print</span>(x.imag) <span class="c1"># 4.0</span></div></td>
</tr>
<tr>
<td style="text-align: left;">int.numerator</td>
<td style="text-align: left;"><div class="code">x = <span class="m">3.5</span><br><span class="nb">print</span>(x.numerator) <span class="c1"># ???</span></div></td>
</tr>
<tr>
<td style="text-align: left;">int.real</td>
<td style="text-align: left;"><div class="code">x = <span class="m">3</span> + <span class="m">4j</span><br><span class="nb">print</span>(x.real) <span class="c1"># 3.0</span></div></td>
</tr>
<tr>
<td style="text-align: left;">int.to_bytes()</td>
<td style="text-align: left;"><div class="code">num = <span class="m">1024</span><br><span class="nb">print</span>(num.to_bytes(<span class="na">length</span>=<span class="m">2</span>, <span class="na">byteorder</span>=<span class="s">'big'</span>, <span class="na">signed</span>=<span class="k">False</span>)) <span class="c1"># b'\x04\x00'</span></div></td>
</tr>
</tbody>
</table>