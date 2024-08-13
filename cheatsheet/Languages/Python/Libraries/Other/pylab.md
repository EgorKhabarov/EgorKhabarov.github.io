<p>Название библиотеки: "pylab"</p>
<p>Краткое описание: Библиотека "pylab" является комбинацией библиотеки "matplotlib" и "NumPy"
для выполнения научных и инженерных вычислений в Python.
Она предоставляет функции для создания графиков, визуализации данных и выполнения математических операций.</p>
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
<td><code>plot</code></td>
<td>Построить график из данных</td>
</tr>
<tr>
<td><code>scatter</code></td>
<td>Создать точечную диаграмму</td>
</tr>
<tr>
<td><code>hist</code></td>
<td>Построить гистограмму из данных</td>
</tr>
<tr>
<td><code>imshow</code></td>
<td>Отобразить изображение</td>
</tr>
<tr>
<td><code>xlabel</code></td>
<td>Задать подпись для оси x</td>
</tr>
<tr>
<td><code>ylabel</code></td>
<td>Задать подпись для оси y</td>
</tr>
<tr>
<td><code>title</code></td>
<td>Задать заголовок графика</td>
</tr>
<tr>
<td><code>legend</code></td>
<td>Вывести легенду графика</td>
</tr>
<tr>
<td><code>grid</code></td>
<td>Отобразить сетку на графике</td>
</tr>
<tr>
<td><code>sin</code></td>
<td>Вычислить синус значения</td>
</tr>
<tr>
<td><code>cos</code></td>
<td>Вычислить косинус значения</td>
</tr>
<tr>
<td><code>exp</code></td>
<td>Вычислить экспоненту значения</td>
</tr>
</tbody>
</table>
<p>Метод <code>plot</code> позволяет строить графики из предоставленных данных.</p>
<pre><code class="language-python">import pylab

x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 50]

pylab.plot(x, y)
pylab.show()
</code></pre>
<p>Метод <code>scatter</code> используется для создания точечной диаграммы.</p>
<pre><code class="language-python">import pylab

x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 50]

pylab.scatter(x, y)
pylab.show()
</code></pre>
<p>Метод <code>hist</code> позволяет создать гистограмму из предоставленных данных.</p>
<pre><code class="language-python">import pylab

data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]

pylab.hist(data)
pylab.show()
</code></pre>
<p>Метод <code>imshow</code> используется для отображения изображений.</p>
<pre><code class="language-python">import pylab
import numpy as np

image = np.random.random((10, 10))

pylab.imshow(image)
pylab.show()
</code></pre>
<p>Метод <code>xlabel</code> задает подпись для оси x на графике.</p>
<pre><code class="language-python">import pylab

x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 50]

pylab.plot(x, y)
pylab.xlabel(&quot;X-axis&quot;)
pylab.show()
</code></pre>
<p>Метод <code>ylabel</code> задает подпись для оси y на графике.</p>
<pre><code class="language-python">import pylab

x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 50]

pylab.plot(x, y)
pylab.ylabel(&quot;Y-axis&quot;)
pylab.show()
</code></pre>
<p>Метод <code>title</code> задает заголовок для графика.</p>
<pre><code class="language-python">import pylab

x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 50]

pylab.plot(x, y)
pylab.title(&quot;My Plot&quot;)
pylab.show()
</code></pre>
<p>Метод <code>legend</code> выводит легенду на графике.</p>
<pre><code class="language-python">import pylab

x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 50]

pylab.plot(x, y, label=&quot;Data&quot;)
pylab.legend()
pylab.show()
</code></pre>
<p>Метод <code>grid</code> отображает сетку на графике.</p>
<pre><code class="language-python">import pylab

x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 50]

pylab.plot(x, y)
pylab.grid(True)
pylab.show()
</code></pre>
<p>Метод <code>sin</code> используется для вычисления синуса значения.</p>
<pre><code class="language-python">import pylab


print(pylab.sin(0.5))
</code></pre>
<p>Метод <code>cos</code> используется для вычисления косинуса значения.</p>
<pre><code class="language-python">import pylab


print(pylab.cos(0.5))
</code></pre>
<p>Метод <code>exp</code> используется для вычисления экспоненты значения.</p>
<pre><code class="language-python">import pylab


print(pylab.exp(2))
</code></pre>