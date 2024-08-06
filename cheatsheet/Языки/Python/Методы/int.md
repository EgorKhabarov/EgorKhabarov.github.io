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
<td style="text-align: left;"><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="p">(</span><span class="mi">10</span><span class="p">)</span><span class="o">.</span><span class="n">as_integer_ratio</span><span class="p">()</span><br><span class="unselectable"><span class="p">(</span><span class="mi">10</span><span class="p">,</span> <span class="mi">1</span><span class="p">)</span></span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td style="text-align: left;">int.bit_count()</td>
<td style="text-align: left;">Возвращает количество установленных битов (битов со значением 1)<br>в двоичном представлении числа.</td>
<td style="text-align: left;"><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="p">(</span><span class="mi">123</span><span class="p">)</span><span class="o">.</span><span class="n">bit_count</span><span class="p">()</span><br><span class="unselectable"><span class="mi">6</span></span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td style="text-align: left;">int.bit_length()</td>
<td style="text-align: left;">Возвращает количество битов, необходимых для представления числа в двоичном виде.</td>
<td style="text-align: left;"><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="p">(</span><span class="mi">256</span><span class="p">)</span><span class="o">.</span><span class="n">bit_length</span><span class="p">()</span><br><span class="unselectable"><span class="mi">9</span></span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td style="text-align: left;">int.conjugate()</td>
<td style="text-align: left;">Возвращает сопряженное комплексное число.</td>
<td style="text-align: left;"><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="p">(</span><span class="mi">3</span> <span class="o">+</span> <span class="mi">4</span><span class="n">j</span><span class="p">)</span><span class="o">.</span><span class="n">conjugate</span><span class="p">()</span><br><span class="unselectable"><span class="p">(</span><span class="mi">3</span><span class="o">-</span><span class="mi">4</span><span class="n">j</span><span class="p">)</span></span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td style="text-align: left;">int.denominator</td>
<td style="text-align: left;">Возвращает знаменатель числа в виде рациональной дроби.</td>
<td style="text-align: left;"><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="p">(</span><span class="mi">3</span><span class="p">)</span><span class="o">.</span><span class="n">denominator</span><br><span class="unselectable"><span class="mi">1</span></span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td style="text-align: left;">int.from_bytes()</td>
<td style="text-align: left;">Преобразует байтовую последовательность в целое число,<br>используя указанный порядок байтов и знак.</td>
<td style="text-align: left;"><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="nb">int</span><span class="o">.</span><span class="n">from_bytes</span><span class="p">(</span><br><span class="unselectable"><span class="o">...</span> </span>    <span class="sa">b</span><span class="s2">&quot;</span><span class="se">\x00\x10</span><span class="s2">&quot;</span><span class="p">,</span><br><span class="unselectable"><span class="o">...</span> </span>    <span class="n">byteorder</span><span class="o">=</span><span class="s2">&quot;big&quot;</span><span class="p">,</span><br><span class="unselectable"><span class="o">...</span> </span>    <span class="n">signed</span><span class="o">=</span><span class="kc">False</span><br><span class="unselectable"><span class="o">...</span> </span><span class="p">)</span><br><span class="unselectable"><span class="mi">16</span></span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td style="text-align: left;">int.imag</td>
<td style="text-align: left;">Возвращает мнимую часть комплексного числа.</td>
<td style="text-align: left;"><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="p">(</span><span class="mi">3</span> <span class="o">+</span> <span class="mi">4</span><span class="n">j</span><span class="p">)</span><span class="o">.</span><span class="n">imag</span><br><span class="unselectable"><span class="mf">4.0</span></span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td style="text-align: left;">int.numerator</td>
<td style="text-align: left;">Возвращает числитель числа в виде рациональной дроби.</td>
<td style="text-align: left;"><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="p">(</span><span class="mi">3</span><span class="p">)</span><span class="o">.</span><span class="n">numerator</span><br><span class="unselectable"><span class="mi">3</span></span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td style="text-align: left;">int.real</td>
<td style="text-align: left;">Возвращает действительную часть комплексного числа.</td>
<td style="text-align: left;"><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="p">(</span><span class="mi">3</span> <span class="o">+</span> <span class="mi">4</span><span class="n">j</span><span class="p">)</span><span class="o">.</span><span class="n">real</span><br><span class="unselectable"><span class="mf">3.0</span></span><br></pre></div></pre></div></div></td>
</tr>
<tr>
<td style="text-align: left;">int.to_bytes()</td>
<td style="text-align: left;">Преобразует целое число в байтовую последовательность,<br>используя указанный порядок байтов и знак.</td>
<td style="text-align: left;"><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre><div class="highlight"><pre><span></span><span class="unselectable"><span class="o">&gt;&gt;&gt;</span> </span><span class="p">(</span><span class="mi">1024</span><span class="p">)</span><span class="o">.</span><span class="n">to_bytes</span><span class="p">(</span><br><span class="unselectable"><span class="o">...</span> </span>    <span class="n">length</span><span class="o">=</span><span class="mi">2</span><span class="p">,</span><br><span class="unselectable"><span class="o">...</span> </span>    <span class="n">byteorder</span><span class="o">=</span><span class="s2">&quot;big&quot;</span><span class="p">,</span><br><span class="unselectable"><span class="o">...</span> </span>    <span class="n">signed</span><span class="o">=</span><span class="kc">False</span><br><span class="unselectable"><span class="o">...</span> </span><span class="p">)</span><br><span class="unselectable"><span class="sa">b</span><span class="s2">&quot;</span><span class="se">\x04\x00</span><span class="s2">&quot;</span></span><br></pre></div></pre></div></div></td>
</tr>
</tbody>
</table>