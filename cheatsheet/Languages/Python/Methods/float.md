<table>
<thead>
<tr>
<th>Метод</th>
<th>Описание</th>
<th>Пример вызова</th>
</tr>
</thead>
<tbody>
<tr>
<td>float.as_integer_ratio</td>
<td>Возвращает кортеж, представляющий рациональное число,<br>близкое к данному целому числу.</td>
<td><pre><code class="language-python">&gt;&gt;&gt; 10.5.as_integer_ratio()<br>(21, 2)</code></pre></td>
</tr>
<tr>
<td>float.conjugate</td>
<td>Возвращает сопряженное комплексное число.</td>
<td><pre><code class="language-python">&gt;&gt;&gt; 10.5.conjugate()<br>10.5</code></pre></td>
</tr>
<tr>
<td>float.fromhex</td>
<td></td>
<td><pre><code class="language-python">&gt;&gt;&gt; float.fromhex("ff")<br>255.0</code></pre></td>
</tr>
<tr>
<td>float.hex</td>
<td></td>
<td><pre><code class="language-python">&gt;&gt;&gt; (-0.1).hex()<br>"-0x1.999999999999ap-4"<br>&gt;&gt;&gt; 3.14159.hex()<br>"0x1.921f9f01b866ep+1"</code></pre></td>
</tr>
<tr>
<td>float.imag</td>
<td>Возвращает мнимую часть комплексного числа.</td>
<td><pre><code class="language-python">&gt;&gt;&gt; 10.5.imag<br>0.0</code></pre></td>
</tr>
<tr>
<td>float.is_integer</td>
<td></td>
<td><pre><code class="language-python">&gt;&gt;&gt; 10.5.is_integer()<br>False<br>&gt;&gt;&gt; 10.0.is_integer()<br>True</code></pre></td>
</tr>
<tr>
<td>float.real</td>
<td>Возвращает действительную часть комплексного числа.</td>
<td><pre><code class="language-python">&gt;&gt;&gt; 10.0.real<br>10.0</code></pre></td>
</tr>
</tbody>
</table>