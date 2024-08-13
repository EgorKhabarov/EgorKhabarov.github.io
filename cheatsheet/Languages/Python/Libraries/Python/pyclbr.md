<p>Библиотека "pyclbr" в Python используется для анализа и чтения исходного кода классов и функций в модуле.
Она позволяет получить информацию о структуре программы, такую как классы, методы, атрибуты и их связи.</p>
<p>Таблица методов модуля "pyclbr" и его подмодулей:</p>
<table>
<thead>
<tr>
<th>Метод</th>
<th>Описание</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>readmodule()</code></td>
<td>Читает и анализирует модуль, возвращая словарь классов и функций.</td>
</tr>
<tr>
<td><code>readmodule_ex()</code></td>
<td>Похож на <code>readmodule()</code>, но также возвращает дополнительную информацию о модуле.</td>
</tr>
<tr>
<td><code>Class</code></td>
<td>Класс, представляющий отдельный класс из исходного кода.</td>
</tr>
<tr>
<td><code>Function</code></td>
<td>Класс, представляющий отдельную функцию из исходного кода.</td>
</tr>
<tr>
<td><code>Module</code></td>
<td>Класс, представляющий модуль и его структуру.</td>
</tr>
</tbody>
</table>
<p><code>readmodule()</code> Читает и анализирует модуль, возвращая словарь классов и функций.</p>
<pre><code class="language-python">import pyclbr

module_data = pyclbr.readmodule(&quot;module_name&quot;)

for class_name, class_data in module_data.items():
    print(f&quot;Class: {class_name}&quot;)
    for method_name, method_data in class_data.methods.items():
        print(f&quot;Method: {method_name}&quot;)
</code></pre>
<p><code>Class</code> Класс, представляющий отдельный класс из исходного кода.</p>
<pre><code class="language-python">import pyclbr

class_data = pyclbr.Class(&quot;class_name&quot;)

print(f&quot;Class: {class_data.name}&quot;)
for method_name, method_data in class_data.methods.items():
    print(f&quot;Method: {method_name}&quot;)
</code></pre>
<p><code>Function</code> Класс, представляющий отдельную функцию из исходного кода.</p>
<pre><code class="language-python">import pyclbr

function_data = pyclbr.Function(&quot;function_name&quot;)

print(f&quot;Function: {function_data.name}&quot;)
print(f&quot;Start line: {function_data.lineno}&quot;)
</code></pre>
<p><code>Module</code> Класс, представляющий модуль и его структуру.</p>
<pre><code class="language-python">import pyclbr

module_data = pyclbr.Module(&quot;module_name&quot;)

print(f&quot;Module: {module_data.name}&quot;)
for class_name, class_data in module_data.classes.items():
    print(f&quot;Class: {class_name}&quot;)
</code></pre>