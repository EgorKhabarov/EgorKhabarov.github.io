<h1>Бесконечные итераторы</h1>
<table>
<thead>
<tr>
<th>Функция</th>
<th>Пример</th>
<th>Результат</th>
</tr>
</thead>
<tbody>
<tr>
<td>count(start, [step])</td>
<td>count(3, 2)</td>
<td>3 5 7 9…</td>
</tr>
<tr>
<td>cycle(p)</td>
<td>cycle("ABC")</td>
<td>A B С А В…</td>
</tr>
<tr>
<td>repeat(elem [,n])</td>
<td>repeat("x", 5)</td>
<td>x x x x x</td>
</tr>
</tbody>
</table>
<h1>Итераторы, которые завершаются на самой короткой последовательности</h1>
<table>
<thead>
<tr>
<th>Функция</th>
<th>Пример</th>
<th>Результат</th>
</tr>
</thead>
<tbody>
<tr>
<td>accumulate(p [,func])</td>
<td>accumulate([1,2,3,4,5])</td>
<td>1 3 6 10 15</td>
</tr>
<tr>
<td>chain(p, q)</td>
<td>chain("ABC", "DE")</td>
<td>A B C D E</td>
</tr>
<tr>
<td>chain.from_iterable(p)</td>
<td>chain.from_iterable(["ABC", "DE"])</td>
<td>A B C D E</td>
</tr>
<tr>
<td>compress(data, selectors)</td>
<td>compress("ABCDE", (0, 1, 0, 0, 1))</td>
<td>B E</td>
</tr>
<tr>
<td>dropwhile(pred, seq)</td>
<td>dropwhile(lambda x: x &lt; 0, [1, 0, -1, 1, -1])</td>
<td>1 0 -1 1 -1</td>
</tr>
<tr>
<td>filterfalse(pred, seq)</td>
<td>filterfalse(lambda x: x &lt; 0, [1, 0, -1, 1, -1])</td>
<td>1 0 1</td>
</tr>
<tr>
<td>groupby(iterable[, key])</td>
<td>groupby((3, 4, 0, -1), key=lambda x: x &gt; 0)</td>
<td>True [3, 4] False [0, -1]</td>
</tr>
<tr>
<td>islice(seq, [start,] stop [, step])</td>
<td>islice("ABCDEFGH", 1, 6, 2)</td>
<td>B D F</td>
</tr>
<tr>
<td>pairwise(iterable)</td>
<td>pairwise("ABcd12")</td>
<td>AB Bc cd d1 12</td>
</tr>
<tr>
<td>starmap(func, seq)</td>
<td>starmap(operator.mul, ((1, 2), (3, 4)))</td>
<td>2 12</td>
</tr>
<tr>
<td>takewhile(pred, seq)</td>
<td>takewhile(lambda x: x &lt; 0, [1, 0, -1, 1, -1])</td>
<td></td>
</tr>
<tr>
<td>tee(it, n)</td>
<td>tee([1, 2], 3)</td>
<td>[1, 2], [1, 2], [1, 2]</td>
</tr>
<tr>
<td>zip_longest(p, q, …[, fillvalue=None])</td>
<td>zip_longest((1, 2), ("A",), fillvalue="_")</td>
<td>(1, "A") (2, "_")</td>
</tr>
</tbody>
</table>
<h1>Комбинаторные итераторы</h1>
<table>
<thead>
<tr>
<th>Функция</th>
<th>Пример</th>
<th>Результат</th>
</tr>
</thead>
<tbody>
<tr>
<td>product(p, q, …[, repeat=1])</td>
<td>product(("A", "B"), repeat=2)</td>
<td>(A, A) (A, B) (B A) (B B)</td>
</tr>
<tr>
<td>permutations(p[, r])</td>
<td>permutations(("a", "b", "c"), 2)</td>
<td>("a", "b") ("a", "c") ("b", "a") ("b", "c") ("c", "a") ("c", "b")</td>
</tr>
<tr>
<td>combinations(p, r)</td>
<td>combinations("ABC", 2)</td>
<td>("A", "B") ("A", "C") ("B", "C")</td>
</tr>
<tr>
<td>combinations_with_replacement(p, r)</td>
<td>combinations_with_replacement("ABC", 2)</td>
<td>("A", "A") ("A", "B") ("A", "C") ("B", "B") ("B", "C") ("C", "C")</td>
</tr>
</tbody>
</table>
<h1>Модуль itertools</h1>
<pre><code class="language-pycon">&gt;&gt;&gt; def print_iterator(x):
...     for i in range(5):
...         try:
...             print(next(x), end=&quot; &quot;)
...         except StopIteration:
...             break
...     print()
...
&gt;&gt;&gt; # Генерирует бесконечный ряд чисел, начиная с start, с шагом step
&gt;&gt;&gt; from itertools import count
&gt;&gt;&gt; count(start=0, step=1)
0 1 2 3 4
&gt;&gt;&gt;
&gt;&gt;&gt; # Бесконечно циклит элементы в iterable
&gt;&gt;&gt; from itertools import cycle
&gt;&gt;&gt; cycle([1, 2, 3])
1 2 3 1 2
&gt;&gt;&gt;
&gt;&gt;&gt; # Генерирует все возможные перестановки элементов iterable с длиной r
&gt;&gt;&gt; # по умолчанию длина равна длине iterable
&gt;&gt;&gt; from itertools import permutations
&gt;&gt;&gt; permutations(&quot;12345&quot;, r=None)
(&quot;1&quot;, &quot;2&quot;, &quot;3&quot;, &quot;4&quot;, &quot;5&quot;) (&quot;1&quot;, &quot;2&quot;, &quot;3&quot;, &quot;5&quot;, &quot;4&quot;) (&quot;1&quot;, &quot;2&quot;, &quot;4&quot;, &quot;3&quot;, &quot;5&quot;) (&quot;1&quot;, &quot;2&quot;, &quot;4&quot;, &quot;5&quot;, &quot;3&quot;) (&quot;1&quot;, &quot;2&quot;, &quot;5&quot;, &quot;3&quot;, &quot;4&quot;)
&gt;&gt;&gt; permutations(&quot;12345&quot;, r=2)
(&quot;1&quot;, &quot;2&quot;) (&quot;1&quot;, &quot;3&quot;) (&quot;1&quot;, &quot;4&quot;) (&quot;1&quot;, &quot;5&quot;) (&quot;2&quot;, &quot;1&quot;)
&gt;&gt;&gt;
&gt;&gt;&gt; # Генерирует все возможные комбинации элементов iterable с длиной r
&gt;&gt;&gt; from itertools import combinations
&gt;&gt;&gt; combinations(&quot;12345&quot;, r=2)
(&quot;1&quot;, &quot;2&quot;) (&quot;1&quot;, &quot;3&quot;) (&quot;1&quot;, &quot;4&quot;) (&quot;1&quot;, &quot;5&quot;) (&quot;2&quot;, &quot;3&quot;)
&gt;&gt;&gt;
&gt;&gt;&gt; # Генерирует все возможные комбинации элементов iterable с длиной r, с повторением элементов
&gt;&gt;&gt; from itertools import combinations_with_replacement
&gt;&gt;&gt; combinations_with_replacement(&quot;12345&quot;, r=2)
(&quot;1&quot;, &quot;1&quot;) (&quot;1&quot;, &quot;2&quot;) (&quot;1&quot;, &quot;3&quot;) (&quot;1&quot;, &quot;4&quot;) (&quot;1&quot;, &quot;5&quot;)
&gt;&gt;&gt;
&gt;&gt;&gt; Объединяет несколько итераторов в один
&gt;&gt;&gt; from itertools import chain
&gt;&gt;&gt; chain((1, 2), (4, 5))
1 2 4 5
&gt;&gt;&gt;
&gt;&gt;&gt; # Объединяет элементы из каждого итератора в кортежи
&gt;&gt;&gt; # Если итераторы разных длин, то элементы для дополнения берутся из fillvalue
&gt;&gt;&gt; from itertools import zip_longest
&gt;&gt;&gt; zip_longest((1, 2), (&quot;A&quot;,), fillvalue=&quot;_&quot;)
(1, &quot;A&quot;) (2, &quot;_&quot;)
&gt;&gt;&gt;
&gt;&gt;&gt; # Группирует элементы iterable по значениям функции key
&gt;&gt;&gt; from itertools import groupby
&gt;&gt;&gt; groupby((3, 4, 0, -1), key=lambda x: x &gt; 0)
True [3, 4] False [0, -1]
&gt;&gt;&gt;
&gt;&gt;&gt; # Выдаёт элементы из iterable, начиная с start, и заканчивая stop, с шагом step
&gt;&gt;&gt; from itertools import islice
&gt;&gt;&gt; islice(iterable, start, stop=None, step=1)
...
&gt;&gt;&gt;
&gt;&gt;&gt; # Применяет функцию function к каждому элементу iterable, который представлен в виде кортежа
&gt;&gt;&gt; from itertools import starmap
&gt;&gt;&gt; starmap(function, iterable)
...
&gt;&gt;&gt;
&gt;&gt;&gt; # Выдаёт все возможные пары (или кортежи) элементов из каждого из iterables
&gt;&gt;&gt; # repeat определяет, сколько раз каждый итератор будет повторен
&gt;&gt;&gt; from itertools import product
&gt;&gt;&gt; product((&quot;A&quot;, &quot;B&quot;), repeat=2)
(&quot;A&quot;, &quot;A&quot;) (&quot;A&quot;, &quot;B&quot;) (&quot;B&quot;, &quot;A&quot;) (&quot;B&quot;, &quot;B&quot;)
&gt;&gt;&gt;
&gt;&gt;&gt; # Выдаёт сумму (или другую комбинацию) элементов iterable, используя функцию func
&gt;&gt;&gt; from itertools import accumulate
&gt;&gt;&gt; # accumulate(iterable, func=operator.add)
&gt;&gt;&gt; accumulate([1,2,3,4,5])
1 3 6 10 15
&gt;&gt;&gt;
&gt;&gt;&gt; # Выдаёт элементы data, соответствующие истинным значениям selectors
&gt;&gt;&gt; from itertools import compress
&gt;&gt;&gt; compress(&quot;ABCDE&quot;, (0, 1, 0, 0, 1))
B E
&gt;&gt;&gt;
&gt;&gt;&gt; # Выдаёт элементы iterable после первого элемента, для которого predicate вернёт ложное значение
&gt;&gt;&gt; from itertools import dropwhile
&gt;&gt;&gt; dropwhile(predicate, iterable)
...
&gt;&gt;&gt;
&gt;&gt;&gt; # Выдаёт элементы iterable, для которых predicate вернёт ложное значение
&gt;&gt;&gt; from itertools import filterfalse
&gt;&gt;&gt; filterfalse(lambda x: x &lt; 0, [1, 0, -1, 1, -1])
1 0 1
&gt;&gt;&gt;
&gt;&gt;&gt; # Выдаёт пары соседних элементов из iterable
&gt;&gt;&gt; from itertools import pairwise
&gt;&gt;&gt; pairwise(&quot;ABcd12&quot;)
AB Bc cd d1 12
&gt;&gt;&gt;
&gt;&gt;&gt; # Выдаёт object times раз
&gt;&gt;&gt; # Если times не указан бесконечное количество раз
&gt;&gt;&gt; from itertools import repeat
&gt;&gt;&gt; repeat(&quot;x&quot;, 5)
x x x x x
&gt;&gt;&gt;
&gt;&gt;&gt; # Выдаёт элементы iterable до первого элемента, для которого predicate вернёт ложное значение
&gt;&gt;&gt; from itertools import takewhile
&gt;&gt;&gt; takewhile(predicate, iterable)
...
&gt;&gt;&gt;
&gt;&gt;&gt; # Возвращает n независимых итераторов
&gt;&gt;&gt; # Каждый из которых может быть использован независимо для перебора элементов исходного iterable
&gt;&gt;&gt; from itertools import tee
&gt;&gt;&gt; tee([1, 2], 3)
[1, 2], [1, 2], [1, 2]
&gt;&gt;&gt;
</code></pre>