<pre><code class="language-python">from dataclasses import dataclass
</code></pre>
<pre><code class="language-python">@dataclass(
    *,
    init: bool = ...,
    repr: bool = ...,
    eq: bool = ...,
    order: bool = ...,
    unsafe_hash: bool = ...,
    frozen: bool = ...,
)
</code></pre>
<table>
<thead>
<tr>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>init</td>
<td>Нужно ли автоматически генерировать метод <code>__init__</code> для инициализации атрибутов класса.</td>
</tr>
<tr>
<td>repr</td>
<td>Нужно ли автоматически генерировать метод <code>__repr__</code> для вывода строкового представления объектов класса.</td>
</tr>
<tr>
<td>eq</td>
<td>Нужно ли автоматически генерировать метод <code>__eq__</code> для сравнения объектов класса.</td>
</tr>
<tr>
<td>order</td>
<td>Нужно ли автоматически генерировать методы <code>__lt__</code>, <code>__le__</code>, <code>__gt__</code>, <code>__ge__</code> для сравнения объектов класса.</td>
</tr>
<tr>
<td>unsafe_hash</td>
<td>Нужно ли автоматически генерировать метод <code>__hash__</code> для объектов класса.<br>Обычно этот аргумент следует использовать только для классов, объекты которых неизменяемы <code>frozen</code>,<br>так как изменяемые объекты могут привести к неожиданным результатам.</td>
</tr>
<tr>
<td>frozen</td>
<td>Нужно ли сделать объекты класса неизменяемыми <code>immutable</code>.</td>
</tr>
</tbody>
</table>
<p>Значения по умолчанию</p>
<pre><code class="language-python">@dataclass(
    *,
    init: bool = True,
    repr: bool = True,
    eq: bool = True,
    order: bool = True,
    unsafe_hash: bool = True,
    frozen: bool = False,
)
</code></pre>