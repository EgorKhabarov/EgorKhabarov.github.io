<h1>Функции и константы</h1>
<table>
<thead>
<tr>
<th>Название</th>
<th>Описание</th>
<th>Пример использования</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>acos(x)</code></td>
<td>Возвращает арккосинус</td>
<td><code>math.acos(1)</code>  # 0.0</td>
</tr>
<tr>
<td><code>acosh(x)</code></td>
<td>Возвращает обратный гиперболический косинус</td>
<td><code>math.acosh(1)</code>  # 0.0</td>
</tr>
<tr>
<td><code>asin(x)</code></td>
<td>Возвращает арксинус в радианах</td>
<td><code>math.asin(1)</code>  # 1.5707963267948966</td>
</tr>
<tr>
<td><code>asinh(x)</code></td>
<td>Возвращает обратный гиперболический синус</td>
<td><code>math.asinh(0)</code>  # 0.0</td>
</tr>
<tr>
<td><code>atan(x)</code></td>
<td>Возвращает арктангенс в радианах</td>
<td><code>math.atan(1)</code>  # 0.7853981633974483</td>
</tr>
<tr>
<td><code>atan2(y, x)</code></td>
<td>Возвращает арктангенс от частного двух аргументов, учитывая квадрант</td>
<td><code>math.atan2(1, 1)</code>  # 0.7853981633974483</td>
</tr>
<tr>
<td><code>atanh(x)</code></td>
<td>Возвращает обратный гиперболический тангенс</td>
<td><code>math.atanh(0)</code>  # 0.0</td>
</tr>
<tr>
<td><code>cbrt(x)</code></td>
<td><strong>(В Python 3.11+)</strong> Возвращает кубический корень</td>
<td><code>math.cbrt(27)</code>  # 3.0</td>
</tr>
<tr>
<td><code>ceil(x)</code></td>
<td>Округляет число <code>x</code> до ближайшего целого вверх</td>
<td><code>math.ceil(4.2)</code>  # 5</td>
</tr>
<tr>
<td><code>comb(n, k)</code></td>
<td><strong>(В Python 3.10+)</strong> Возвращает число сочетаний из <code>n</code> по <code>k</code></td>
<td><code>math.comb(5, 2)</code>  # 10</td>
</tr>
<tr>
<td><code>copysign(x, y)</code></td>
<td>Возвращает число <code>x</code> с знаком числа <code>y</code></td>
<td><code>math.copysign(3, -1)</code>  # -3.0</td>
</tr>
<tr>
<td><code>cos(x)</code></td>
<td>Возвращает косинус угла <code>x</code>, выраженного в радианах</td>
<td><code>math.cos(0)</code>  # 1.0</td>
</tr>
<tr>
<td><code>cosh(x)</code></td>
<td>Возвращает гиперболический косинус</td>
<td><code>math.cosh(0)</code>  # 1.0</td>
</tr>
<tr>
<td><code>degrees(x)</code></td>
<td>Преобразует угол <code>x</code> из радиан в градусы</td>
<td><code>math.degrees(math.pi)</code>  # 180.0</td>
</tr>
<tr>
<td><code>dist(p, q)</code></td>
<td><strong>(В Python 3.8+)</strong> Возвращает евклидово расстояние<br>между точками <code>p</code> и <code>q</code>, представленными как кортежи координат</td>
<td><code>math.dist([1, 2], [4, 6])</code>  # 5.0</td>
</tr>
<tr>
<td><code>e</code></td>
<td>Константа основание натурального логарифма</td>
<td><code>2.718281828459045</code></td>
</tr>
<tr>
<td><code>erf(x)</code></td>
<td>Возвращает значение функции ошибок для числа <code>x</code></td>
<td><code>math.erf(1)</code>  # 0.8427007929497149</td>
</tr>
<tr>
<td><code>erfc(x)</code></td>
<td>Возвращает дополнительную функцию ошибок для числа <code>x</code></td>
<td><code>math.erfc(1)</code>  # 0.15729920705028513</td>
</tr>
<tr>
<td><code>exp(x)</code></td>
<td>Возвращает значение <code>e**x</code></td>
<td><code>math.exp(1)</code>  # 2.718281828459045</td>
</tr>
<tr>
<td><code>exp2(x)</code></td>
<td><strong>(В Python 3.8+)</strong> Возвращает значение <code>2**x</code></td>
<td><code>math.exp2(3)</code>  # 8.0</td>
</tr>
<tr>
<td><code>expm1(x)</code></td>
<td>Возвращает <code>e**x - 1</code></td>
<td><code>math.expm1(0)</code>  # 0.0</td>
</tr>
<tr>
<td><code>fabs(x)</code></td>
<td>Возвращает абсолютное значение в виде числа с плавающей точкой</td>
<td><code>math.fabs(-5)</code>  # 5.0</td>
</tr>
<tr>
<td><code>factorial(x)</code></td>
<td>Возвращает факториал</td>
<td><code>math.factorial(5)</code>  # 120</td>
</tr>
<tr>
<td><code>floor(x)</code></td>
<td>Округляет до ближайшего целого вниз</td>
<td><code>math.floor(4.8)</code>  # 4</td>
</tr>
<tr>
<td><code>fmod(x, y)</code></td>
<td>Возвращает остаток от деления <code>x</code> на <code>y</code>, используя тот же знак, что и <code>x</code></td>
<td><code>math.fmod(5, 2)</code>  # 1.0</td>
</tr>
<tr>
<td><code>frexp(x)</code></td>
<td>Разлагает число <code>x</code> на мантиссу и экспоненту: возвращает кортеж <code>(m, e)</code>,<br>такой что <code>x = m * 2**e</code> и <code>0.5 &lt;= abs(m) &lt; 1.0</code></td>
<td><code>math.frexp(8)</code>  # (0.5, 4)</td>
</tr>
<tr>
<td><code>fsum(iterable)</code></td>
<td>Возвращает точную сумму чисел из итерируемого объекта.</td>
<td><code>math.fsum([0.1] * 10)</code>  # 1.0</td>
</tr>
<tr>
<td><code>gamma(x)</code></td>
<td>Возвращает гамма-функцию</td>
<td><code>math.gamma(5)</code>  # 24.0</td>
</tr>
<tr>
<td><code>gcd(x, y)</code></td>
<td>Возвращает наибольший общий делитель</td>
<td><code>math.gcd(8, 12)</code>  # 4</td>
</tr>
<tr>
<td><code>hypot(x, y)</code></td>
<td>Возвращает гипотенузу треугольника с катетами <code>x</code> и <code>y</code>, то есть <code>sqrt(x**2 + y**2)</code></td>
<td><code>math.hypot(3, 4)</code>  # 5.0</td>
</tr>
<tr>
<td><code>inf</code></td>
<td>Положительная бесконечность <code>float("inf")</code></td>
<td><code>inf</code></td>
</tr>
<tr>
<td><code>isclose(a, b)</code></td>
<td>Проверяет, близки ли два числа <code>a</code> и <code>b</code> с учётом относительной и абсолютной точности</td>
<td><code>math.isclose(0.1 + 0.2, 0.3)</code>  # True</td>
</tr>
<tr>
<td><code>isfinite(x)</code></td>
<td>Возвращает <code>True</code>, если число конечно (не бесконечное и не <code>NaN</code>)</td>
<td><code>math.isfinite(1.0)</code>  # True</td>
</tr>
<tr>
<td><code>isinf(x)</code></td>
<td>Возвращает <code>True</code>, если число бесконечное</td>
<td><code>math.isinf(float('inf'))</code>  # True</td>
</tr>
<tr>
<td><code>isnan(x)</code></td>
<td>Возвращает <code>True</code>, если число не является числом (<code>NaN</code>)</td>
<td><code>math.isnan(float('nan'))</code>  # True</td>
</tr>
<tr>
<td><code>isqrt(n)</code></td>
<td><strong>(В Python 3.8+)</strong> Возвращает целочисленный квадратный корень</td>
<td><code>math.isqrt(16)</code>  # 4</td>
</tr>
<tr>
<td><code>lcm(*args)</code></td>
<td><strong>(В Python 3.9+)</strong> Возвращает наименьшее общее кратное всех переданных аргументов</td>
<td><code>math.lcm(4, 6)</code>  # 12</td>
</tr>
<tr>
<td><code>ldexp(x, i)</code></td>
<td>Возвращает <code>x * (2**i)</code></td>
<td><code>math.ldexp(1.5, 2)</code>  # 6.0</td>
</tr>
<tr>
<td><code>lgamma(x)</code></td>
<td>Возвращает натуральный логарифм гамма-функции</td>
<td><code>math.lgamma(5)</code>  # 3.1780538303479458</td>
</tr>
<tr>
<td><code>log(x, base)</code></td>
<td>Возвращает логарифм по основанию <code>base</code> <br>Если основание не указано, используется натуральный логарифм (<code>e</code>)</td>
<td><code>math.log(8, 2)</code>  # 3.0</td>
</tr>
<tr>
<td><code>log10(x)</code></td>
<td>Возвращает логарифм по основанию 10</td>
<td><code>math.log10(100)</code>  # 2.0</td>
</tr>
<tr>
<td><code>log1p(x)</code></td>
<td>Возвращает <code>log(1 + x)</code> с высокой точностью для малых значений <code>x</code></td>
<td><code>math.log1p(0.0001)</code>  # 0.00009999500033334777</td>
</tr>
<tr>
<td><code>log2(x)</code></td>
<td>Возвращает логарифм по основанию 2</td>
<td><code>math.log2(8)</code>  # 3.0</td>
</tr>
<tr>
<td><code>modf(x)</code></td>
<td>Возвращает кортеж из дробной и целой части</td>
<td><code>math.modf(3.14)</code>  # (0.14000000000000012, 3.0)</td>
</tr>
<tr>
<td><code>nan</code></td>
<td>Представление "Не число" (<code>NaN</code>) <code>float('nan')</code></td>
<td><code>print(math.nan)</code>  # nan</td>
</tr>
<tr>
<td><code>nextafter(x, y)</code></td>
<td>Возвращает ближайшее число к <code>x</code>, направленное в сторону <code>y</code></td>
<td><code>math.nextafter(1.0, 2.0)</code>  # 1.0000000000000002</td>
</tr>
<tr>
<td><code>perm(n, k)</code></td>
<td><strong>(В Python 3.8+)</strong> Возвращает число перестановок из <code>n</code> по <code>k</code></td>
<td><code>math.perm(5, 2)</code>  # 20</td>
</tr>
<tr>
<td><code>pi</code></td>
<td>Константа π (приблизительно 3.141592653589793)</td>
<td><code>print(math.pi)</code>  # 3.141592653589793</td>
</tr>
<tr>
<td><code>pow(x, y)</code></td>
<td>Возвращает результат возведения числа <code>x</code> в степень <code>y</code></td>
<td><code>math.pow(2, 3)</code>  # 8.0</td>
</tr>
<tr>
<td><code>prod(iterable)</code></td>
<td><strong>(В Python 3.8+)</strong> Возвращает произведение всех элементов итерируемого объекта</td>
<td><code>math.prod([1, 2, 3, 4])</code>  # 24</td>
</tr>
<tr>
<td><code>radians(x)</code></td>
<td>Преобразует угол из градусов в радианы</td>
<td><code>math.radians(180)</code>  # 3.141592653589793</td>
</tr>
<tr>
<td><code>remainder(x, y)</code></td>
<td>Возвращает остаток от деления <code>x</code> на <code>y</code>, аналогично оператору <code>%</code>, но с учетом знака делимого</td>
<td><code>math.remainder(5, 3)</code>  # -1.0</td>
</tr>
<tr>
<td><code>sin(x)</code></td>
<td>Возвращает синус угла, выраженного в радианах</td>
<td><code>math.sin(math.pi / 2)</code>  # 1.0</td>
</tr>
<tr>
<td><code>sinh(x)</code></td>
<td>Возвращает гиперболический синус</td>
<td><code>math.sinh(0)</code>  # 0.0</td>
</tr>
<tr>
<td><code>sqrt(x)</code></td>
<td>Возвращает квадратный корень</td>
<td><code>math.sqrt(16)</code>  # 4.0</td>
</tr>
<tr>
<td><code>tan(x)</code></td>
<td>Возвращает тангенс угла, выраженного в радианах</td>
<td><code>math.tan(math.pi / 4)</code>  # 0.9999999999999999</td>
</tr>
<tr>
<td><code>tanh(x)</code></td>
<td>Возвращает гиперболический тангенс</td>
<td><code>math.tanh(0)</code>  # 0.0</td>
</tr>
<tr>
<td><code>tau</code></td>
<td>Константа τ (2π, приблизительно 6.283185307179586)</td>
<td><code>math.tau</code>  # 6.283185307179586</td>
</tr>
<tr>
<td><code>trunc(x)</code></td>
<td>Округляет число <code>x</code> до ближайшего целого, отбрасывая дробную часть</td>
<td><code>math.trunc(4.9)</code>  # 4</td>
</tr>
<tr>
<td><code>ulp(x)</code></td>
<td>Возвращает расстояние до следующего числа с плавающей точкой после <code>x</code></td>
<td><code>math.ulp(1.0)</code>  # 2.220446049250313e-16</td>
</tr>
</tbody>
</table>
<h1>Примеры</h1>
<h3>Работа с тригонометрическими функциями</h3>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">math</span>

<span class="n">angle_deg</span> <span class="o">=</span> <span class="mi">45</span>
<span class="n">angle_rad</span> <span class="o">=</span> <span class="n">math</span><span class="o">.</span><span class="n">radians</span><span class="p">(</span><span class="n">angle_deg</span><span class="p">)</span>

<span class="n">sin_val</span> <span class="o">=</span> <span class="n">math</span><span class="o">.</span><span class="n">sin</span><span class="p">(</span><span class="n">angle_rad</span><span class="p">)</span>
<span class="n">cos_val</span> <span class="o">=</span> <span class="n">math</span><span class="o">.</span><span class="n">cos</span><span class="p">(</span><span class="n">angle_rad</span><span class="p">)</span>
<span class="n">tan_val</span> <span class="o">=</span> <span class="n">math</span><span class="o">.</span><span class="n">tan</span><span class="p">(</span><span class="n">angle_rad</span><span class="p">)</span>

<span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;Sin(</span><span class="si">{</span><span class="n">angle_deg</span><span class="si">}</span><span class="s2">°) = </span><span class="si">{</span><span class="n">sin_val</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">)</span>  <span class="c1"># Sin(45°) = 0.7071067811865475</span>
<span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;Cos(</span><span class="si">{</span><span class="n">angle_deg</span><span class="si">}</span><span class="s2">°) = </span><span class="si">{</span><span class="n">cos_val</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">)</span>  <span class="c1"># Cos(45°) = 0.7071067811865476</span>
<span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;Tan(</span><span class="si">{</span><span class="n">angle_deg</span><span class="si">}</span><span class="s2">°) = </span><span class="si">{</span><span class="n">tan_val</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">)</span>  <span class="c1"># Tan(45°) = 0.9999999999999999</span>
</pre></div></div></div>

<h3>Проверка близости чисел</h3>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">math</span>

<span class="n">a</span> <span class="o">=</span> <span class="mf">0.1</span> <span class="o">+</span> <span class="mf">0.2</span>
<span class="n">b</span> <span class="o">=</span> <span class="mf">0.3</span>

<span class="k">if</span> <span class="n">math</span><span class="o">.</span><span class="n">isclose</span><span class="p">(</span><span class="n">a</span><span class="p">,</span> <span class="n">b</span><span class="p">):</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Числа близки!&quot;</span><span class="p">)</span>  <span class="c1"># Числа близки!</span>
<span class="k">else</span><span class="p">:</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Числа не близки!&quot;</span><span class="p">)</span>
</pre></div></div></div>

<h3>Вычисление факториала и гамма-функции</h3>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">math</span>

<span class="n">n</span> <span class="o">=</span> <span class="mi">5</span>
<span class="n">fact</span> <span class="o">=</span> <span class="n">math</span><span class="o">.</span><span class="n">factorial</span><span class="p">(</span><span class="n">n</span><span class="p">)</span>
<span class="n">gamma_val</span> <span class="o">=</span> <span class="n">math</span><span class="o">.</span><span class="n">gamma</span><span class="p">(</span><span class="n">n</span> <span class="o">+</span> <span class="mi">1</span><span class="p">)</span>  <span class="c1"># gamma(n) = (n-1)!</span>

<span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;Факториал </span><span class="si">{</span><span class="n">n</span><span class="si">}</span><span class="s2">: </span><span class="si">{</span><span class="n">fact</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">)</span>         <span class="c1"># Факториал 5: 120</span>
<span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;Gamma(</span><span class="si">{</span><span class="n">n</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="mi">1</span><span class="si">}</span><span class="s2">): </span><span class="si">{</span><span class="n">gamma_val</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">)</span>   <span class="c1"># Gamma(6): 120.0</span>
</pre></div></div></div>

<h3>Использование функции <code>prod</code> для вычисления произведения элементов</h3>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">math</span>

<span class="n">numbers</span> <span class="o">=</span> <span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">,</span> <span class="mi">4</span><span class="p">]</span>
<span class="n">product</span> <span class="o">=</span> <span class="n">math</span><span class="o">.</span><span class="n">prod</span><span class="p">(</span><span class="n">numbers</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;Произведение элементов: </span><span class="si">{</span><span class="n">product</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">)</span>  <span class="c1"># Произведение элементов: 24</span>
</pre></div></div></div>

<h3>Работа с бесконечностями и <code>NaN</code></h3>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">math</span>

<span class="n">positive_inf</span> <span class="o">=</span> <span class="n">math</span><span class="o">.</span><span class="n">inf</span>
<span class="n">negative_inf</span> <span class="o">=</span> <span class="o">-</span><span class="n">math</span><span class="o">.</span><span class="n">inf</span>
<span class="n">not_a_number</span> <span class="o">=</span> <span class="n">math</span><span class="o">.</span><span class="n">nan</span>

<span class="nb">print</span><span class="p">(</span><span class="n">math</span><span class="o">.</span><span class="n">isinf</span><span class="p">(</span><span class="n">positive_inf</span><span class="p">))</span>  <span class="c1"># True</span>
<span class="nb">print</span><span class="p">(</span><span class="n">math</span><span class="o">.</span><span class="n">isinf</span><span class="p">(</span><span class="n">negative_inf</span><span class="p">))</span>  <span class="c1"># True</span>
<span class="nb">print</span><span class="p">(</span><span class="n">math</span><span class="o">.</span><span class="n">isnan</span><span class="p">(</span><span class="n">not_a_number</span><span class="p">))</span>  <span class="c1"># True</span>
</pre></div></div></div>

<h3>Преобразование между градусами и радианами</h3>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">math</span>

<span class="n">angle_deg</span> <span class="o">=</span> <span class="mi">90</span>
<span class="n">angle_rad</span> <span class="o">=</span> <span class="n">math</span><span class="o">.</span><span class="n">radians</span><span class="p">(</span><span class="n">angle_deg</span><span class="p">)</span>
<span class="n">converted_deg</span> <span class="o">=</span> <span class="n">math</span><span class="o">.</span><span class="n">degrees</span><span class="p">(</span><span class="n">angle_rad</span><span class="p">)</span>

<span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;</span><span class="si">{</span><span class="n">angle_deg</span><span class="si">}</span><span class="s2"> градусов = </span><span class="si">{</span><span class="n">angle_rad</span><span class="si">}</span><span class="s2"> радиан&quot;</span><span class="p">)</span>     <span class="c1"># 90 градусов = 1.5707963267948966 радиан</span>
<span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;</span><span class="si">{</span><span class="n">angle_rad</span><span class="si">}</span><span class="s2"> радиан = </span><span class="si">{</span><span class="n">converted_deg</span><span class="si">}</span><span class="s2"> градусов&quot;</span><span class="p">)</span>  <span class="c1"># 1.5707963267948966 радиан = 90.0 градусов</span>
</pre></div></div></div>

<h1>Пояснения к функциям и константам</h1>
<h3><code>acos(x)</code>, <code>asin(x)</code>, <code>atan(x)</code></h3>
<ul>
<li>Арккосинус, арксинус и арктангенс возвращают угол в радианах, соответствующий данному тригонометрическому значению.</li>
<li>Область определения:<ul>
<li><code>acos(x)</code>, <code>asin(x)</code> — <code>x</code> должен быть в диапазоне [-1, 1].</li>
<li><code>atan(x)</code> — любое вещественное число.</li>
</ul>
</li>
</ul>
<h3><code>acosh(x)</code>, <code>asinh(x)</code>, <code>atanh(x)</code></h3>
<ul>
<li>Обратные гиперболические функции.</li>
<li>Область определения:<ul>
<li><code>acosh(x)</code> — <code>x</code> &gt;= 1.</li>
<li><code>atanh(x)</code> — <code>-1 &lt; x &lt; 1</code>.</li>
</ul>
</li>
</ul>
<h3><code>cbrt(x)</code></h3>
<ul>
<li>Вычисляет кубический корень числа <code>x</code>.</li>
<li>Доступен начиная с Python 3.11.</li>
</ul>
<h3><code>ceil(x)</code> и <code>floor(x)</code></h3>
<ul>
<li><code>ceil(x)</code> округляет число вверх до ближайшего целого.</li>
<li><code>floor(x)</code> округляет число вниз до ближайшего целого.</li>
</ul>
<h3><code>comb(n, k)</code> и <code>perm(n, k)</code></h3>
<ul>
<li><code>comb(n, k)</code> возвращает количество сочетаний из <code>n</code> по <code>k</code>.</li>
<li><code>perm(n, k)</code> возвращает количество перестановок из <code>n</code> по <code>k</code>.</li>
<li>Доступны начиная с Python 3.8 и 3.10 соответственно.</li>
</ul>
<h3><code>copysign(x, y)</code></h3>
<ul>
<li>Возвращает число <code>x</code> с знаком <code>y</code>.</li>
<li>Полезно для переноса знака при сохранении величины числа.</li>
</ul>
<h3><code>cos(x)</code>, <code>sin(x)</code>, <code>tan(x)</code> и их гиперболические аналоги <code>cosh(x)</code>, <code>sinh(x)</code>, <code>tanh(x)</code></h3>
<ul>
<li>Тригонометрические и гиперболические функции, работающие с углами, выраженными в радианах.</li>
</ul>
<h3><code>degrees(x)</code> и <code>radians(x)</code></h3>
<ul>
<li>Преобразуют углы между градусами и радианами.</li>
</ul>
<h3><code>dist(p, q)</code></h3>
<ul>
<li>Вычисляет евклидово расстояние между двумя точками <code>p</code> и <code>q</code>.</li>
</ul>
<h3><code>erf(x)</code> и <code>erfc(x)</code></h3>
<ul>
<li>Функция ошибок и её дополнение, используемые в статистике и теории вероятностей.</li>
</ul>
<h3><code>exp(x)</code>, <code>exp2(x)</code>, <code>expm1(x)</code></h3>
<ul>
<li>Экспоненциальные функции.</li>
<li><code>expm1(x)</code> вычисляет <code>e**x - 1</code> с высокой точностью для малых <code>x</code>.</li>
</ul>
<h3><code>fabs(x)</code></h3>
<ul>
<li>Возвращает абсолютное значение числа <code>x</code> как число с плавающей точкой.</li>
</ul>
<h3><code>factorial(x)</code></h3>
<ul>
<li>Вычисляет факториал числа <code>x</code>.</li>
</ul>
<h3><code>fmod(x, y)</code> и <code>remainder(x, y)</code></h3>
<ul>
<li><code>fmod(x, y)</code> возвращает остаток от деления <code>x</code> на <code>y</code>, сохраняя знак <code>x</code>.</li>
<li><code>remainder(x, y)</code> возвращает остаток от деления с учётом знака делимого.</li>
</ul>
<h3><code>frexp(x)</code> и <code>ldexp(x, i)</code></h3>
<ul>
<li><code>frexp(x)</code> разлагает число на мантиссу и экспоненту.</li>
<li><code>ldexp(x, i)</code> возвращает <code>x * (2**i)</code>.</li>
</ul>
<h3><code>fsum(iterable)</code></h3>
<ul>
<li>Возвращает точную сумму элементов итерируемого объекта, минимизируя ошибки округления.</li>
</ul>
<h3><code>gamma(x)</code> и <code>lgamma(x)</code></h3>
<ul>
<li>Гамма-функция и её логарифм.</li>
</ul>
<h3><code>gcd(x, y)</code> и <code>lcm(*args)</code></h3>
<ul>
<li><code>gcd(x, y)</code> вычисляет наибольший общий делитель.</li>
<li><code>lcm(*args)</code> вычисляет наименьшее общее кратное для всех аргументов.</li>
</ul>
<h3><code>hypot(x, y)</code></h3>
<ul>
<li>Вычисляет гипотенузу прямоугольного треугольника с катетами <code>x</code> и <code>y</code>.</li>
</ul>
<h3><code>inf</code> и <code>nan</code></h3>
<ul>
<li><code>inf</code> представляет бесконечность.</li>
<li><code>nan</code> представляет "Не число".</li>
</ul>
<h3><code>isclose(a, b)</code></h3>
<ul>
<li>Проверяет, близки ли два числа с учётом заданной точности.</li>
</ul>
<h3><code>isfinite(x)</code>, <code>isinf(x)</code>, <code>isnan(x)</code></h3>
<ul>
<li>Проверяют свойства числа: конечное ли оно, бесконечное или <code>NaN</code>.</li>
</ul>
<h3><code>isqrt(n)</code></h3>
<ul>
<li>Возвращает целочисленный квадратный корень числа <code>n</code>.</li>
</ul>
<h3><code>modf(x)</code></h3>
<ul>
<li>Разделяет число на дробную и целую части.</li>
</ul>
<h3><code>nextafter(x, y)</code></h3>
<ul>
<li>Возвращает ближайшее число к <code>x</code>, направленное в сторону <code>y</code>.</li>
</ul>
<h3><code>perm(n, k)</code></h3>
<ul>
<li>Вычисляет количество перестановок из <code>n</code> по <code>k</code>.</li>
</ul>
<h3><code>pi</code>, <code>e</code>, <code>tau</code></h3>
<ul>
<li><code>pi</code> — число π.</li>
<li><code>e</code> — основание натурального логарифма.</li>
<li><code>tau</code> — число τ (2π).</li>
</ul>
<h3><code>pow(x, y)</code></h3>
<ul>
<li>Возводит <code>x</code> в степень <code>y</code>.</li>
</ul>
<h3><code>prod(iterable)</code></h3>
<ul>
<li>Возвращает произведение всех элементов итерируемого объекта.</li>
</ul>
<h3><code>radians(x)</code> и <code>degrees(x)</code></h3>
<ul>
<li>Преобразуют углы между градусами и радианами.</li>
</ul>
<h3><code>remainder(x, y)</code></h3>
<ul>
<li>Возвращает остаток от деления <code>x</code> на <code>y</code>, аналогично оператору <code>%</code>, но с учетом знака делимого.</li>
</ul>
<h3><code>sin(x)</code>, <code>sinh(x)</code>, <code>cos(x)</code>, <code>cosh(x)</code>, <code>tan(x)</code>, <code>tanh(x)</code></h3>
<ul>
<li>Тригонометрические и гиперболические функции.</li>
</ul>
<h3><code>trunc(x)</code></h3>
<ul>
<li>Округляет число <code>x</code> до ближайшего целого, отбрасывая дробную часть.</li>
</ul>
<h3>ulp(x)</h3>
<ul>
<li>Возвращает расстояние до следующего числа с плавающей точкой после <code>x</code>.</li>
</ul>
<h1>Дополнительные примеры использования функций</h1>
<h3>Проверка, является ли число бесконечным или <code>NaN</code></h3>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="n">math</span><span class="o">.</span><span class="n">isinf</span><span class="p">(</span><span class="nb">float</span><span class="p">(</span><span class="s2">&quot;inf&quot;</span><span class="p">)))</span>  <span class="c1"># True</span>
<span class="nb">print</span><span class="p">(</span><span class="n">math</span><span class="o">.</span><span class="n">isnan</span><span class="p">(</span><span class="nb">float</span><span class="p">(</span><span class="s2">&quot;nan&quot;</span><span class="p">)))</span>  <span class="c1"># True</span>
</pre></div></div></div>

<h3>gamma</h3>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">math</span>

<span class="n">x</span> <span class="o">=</span> <span class="mi">5</span>
<span class="n">gamma_val</span> <span class="o">=</span> <span class="n">math</span><span class="o">.</span><span class="n">gamma</span><span class="p">(</span><span class="n">x</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;Gamma(</span><span class="si">{</span><span class="n">x</span><span class="si">}</span><span class="s2">) равен </span><span class="si">{</span><span class="n">gamma_val</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">)</span>  <span class="c1"># Gamma(5) равен 24.0</span>
</pre></div></div></div>

<h3>Использование функции <code>prod</code> для вычисления произведения элементов</h3>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">math</span>

<span class="n">numbers</span> <span class="o">=</span> <span class="p">[</span><span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">,</span> <span class="mi">4</span><span class="p">]</span>
<span class="n">product</span> <span class="o">=</span> <span class="n">math</span><span class="o">.</span><span class="n">prod</span><span class="p">(</span><span class="n">numbers</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;Произведение элементов </span><span class="si">{</span><span class="n">numbers</span><span class="si">}</span><span class="s2"> равно </span><span class="si">{</span><span class="n">product</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">)</span>  <span class="c1"># 24</span>
</pre></div></div></div>

<h3>Вычисление гипотенузы и угла в треугольнике</h3>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">math</span>

<span class="n">a</span> <span class="o">=</span> <span class="mi">3</span>
<span class="n">b</span> <span class="o">=</span> <span class="mi">4</span>

<span class="c1"># Гипотенуза</span>
<span class="n">c</span> <span class="o">=</span> <span class="n">math</span><span class="o">.</span><span class="n">hypot</span><span class="p">(</span><span class="n">a</span><span class="p">,</span> <span class="n">b</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;Гипотенуза равна </span><span class="si">{</span><span class="n">c</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">)</span>  <span class="c1"># 5.0</span>

<span class="c1"># Угол при катете a</span>
<span class="n">angle_rad</span> <span class="o">=</span> <span class="n">math</span><span class="o">.</span><span class="n">atan2</span><span class="p">(</span><span class="n">b</span><span class="p">,</span> <span class="n">a</span><span class="p">)</span>
<span class="n">angle_deg</span> <span class="o">=</span> <span class="n">math</span><span class="o">.</span><span class="n">degrees</span><span class="p">(</span><span class="n">angle_rad</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;Угол при катете a: </span><span class="si">{</span><span class="n">angle_deg</span><span class="si">}</span><span class="s2">°&quot;</span><span class="p">)</span>  <span class="c1"># 53.13010235415598°</span>
</pre></div></div></div>

<h3>Использование функции <code>isclose</code> для проверки близости чисел</h3>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">math</span>

<span class="n">a</span> <span class="o">=</span> <span class="mf">0.1</span> <span class="o">+</span> <span class="mf">0.2</span>
<span class="n">b</span> <span class="o">=</span> <span class="mf">0.3</span>

<span class="k">if</span> <span class="n">math</span><span class="o">.</span><span class="n">isclose</span><span class="p">(</span><span class="n">a</span><span class="p">,</span> <span class="n">b</span><span class="p">):</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Числа близки&quot;</span><span class="p">)</span>  <span class="c1"># Числа близки</span>
<span class="k">else</span><span class="p">:</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Числа не близки&quot;</span><span class="p">)</span>
</pre></div></div></div>

<h3>Рассчет значения <code>ulp</code> (Unit in the Last Place)</h3>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">math</span>

<span class="n">x</span> <span class="o">=</span> <span class="mf">1.0</span>
<span class="n">ulp_val</span> <span class="o">=</span> <span class="n">math</span><span class="o">.</span><span class="n">ulp</span><span class="p">(</span><span class="n">x</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;ULP для </span><span class="si">{</span><span class="n">x</span><span class="si">}</span><span class="s2"> равен </span><span class="si">{</span><span class="n">ulp_val</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">)</span>  <span class="c1"># 2.220446049250313e-16</span>
</pre></div></div></div>

<h1>Константы</h1>
<table>
<thead>
<tr>
<th>Константа</th>
<th>Описание</th>
<th>Пример использования</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>math.pi</code></td>
<td>Число <code>π</code>, приблизительно <code>3.141592653589793</code></td>
<td><code>3.141592653589793</code></td>
</tr>
<tr>
<td><code>math.e</code></td>
<td>Основание натурального логарифма, приблизительно <code>2.718281828459045</code></td>
<td><code>2.718281828459045</code></td>
</tr>
<tr>
<td><code>math.tau</code></td>
<td>Число <code>τ</code> (<strong>2π</strong>), приблизительно <code>6.283185307179586</code></td>
<td><code>6.283185307179586</code></td>
</tr>
<tr>
<td><code>math.inf</code></td>
<td>Представляет положительную бесконечность</td>
<td><code>inf</code></td>
</tr>
<tr>
<td><code>math.nan</code></td>
<td>Представляет "Не число" (<code>NaN</code>)</td>
<td><code>nan</code></td>
</tr>
</tbody>
</table>
<h1>Ссылки</h1>
<ul>
<li><a href="https://docs.python.org/3/library/math.html">Официальная документация</a></li>
<li><a href="https://realpython.com/python-math-module/">Real Python - Math Module</a></li>
<li><a href="https://docs.python.org/3/library/math.html#module-math">Документация по функциям и константам</a></li>
</ul>
<h1>Полезные советы</h1>
<ul>
<li><strong>Работа с углами</strong>: Всегда помните, что тригонометрические функции
(<code>sin</code>, <code>cos</code>, <code>tan</code> и др.) работают с углами, выраженными в радианах.
Используйте <code>math.radians()</code> и <code>math.degrees()</code> для преобразования между градусами и радианами.</li>
<li><strong>Числа с плавающей точкой</strong>: При работе с числами с плавающей точкой (<code>float</code>)
учитывайте возможные ошибки округления. Функция <code>math.isclose()</code>
поможет проверить близость чисел с учётом заданной точности.</li>
<li><strong>Оптимизация производительности</strong>: Некоторые функции, такие как <code>math.isqrt()</code>,
предоставляют оптимизированные способы выполнения операций, что особенно полезно для больших чисел или частых вызовов функций.</li>
<li><strong>Гамма-функция</strong>: Функции <code>math.gamma()</code> и <code>math.lgamma()</code> полезны в статистике
и математике для работы с непрерывными распределениями и факториалами вещественных чисел.</li>
</ul>