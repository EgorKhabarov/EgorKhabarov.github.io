<p>Модуль collections в Python содержит различные удобные классы для работы с коллекциями (наборами объектов).
Некоторые из классов в модуле collections:</p>
<p>namedtuple - это класс-фабрика для создания именованных кортежей, которые представляют собой 
             неизменяемые объекты, похожие на обычные кортежи, но каждый элемент имеет уникальное имя.</p>
<p>deque - это двусторонняя очередь, которая позволяет эффективно добавлять и удалять элементы как с начала, так и с конца.</p>
<p>Counter - это класс, который позволяет подсчитывать количество каждого элемента в последовательности.
          Возвращает словарь, где каждый ключ представляет элемент последовательности, а значение - количество его вхождений в последовательность.</p>
<p>OrderedDict - это словарь, который запоминает порядок вставки элементов.
              Позволяет итерироваться по элементам в порядке, в котором они были добавлены в словарь.</p>
<p>defaultdict - это словарь, который возвращает значение по умолчанию, если ключ отсутствует.
              При создании defaultdict необходимо указать функцию, которая будет вызываться для возврата значения по умолчанию. 
              Этот класс часто используется для создания словарей с дефолтным значением или для группировки элементов по какому-то признаку.</p>
<p>ChainMap - это класс, который позволяет объединить несколько словарей в один.
           Он предоставляет удобный способ комбинирования нескольких словарей в один, без необходимости копирования элементов.</p>
<p>UserDict - это класс, который предоставляет интерфейс словаря, но позволяет наследоваться для создания собственных классов словарей.
           Он может быть использован для создания словарей с дополнительной логикой или специальным поведением.</p>
<p>Эти классы облегчают работу с коллекциями в Python и уменьшают необходимость писать большой и сложный код для выполнения стандартных задач.</p>
<p>namedtuple:</p>
<pre><code class="language-python">from collections import namedtuple

# создаем именованный кортеж Point
Point = namedtuple(&quot;Point&quot;, [&quot;x&quot;, &quot;y&quot;])

# создаем экземпляр кортежа
p = Point(1, 2)

# обращаемся к полям кортежа по имени
print(p.x)  # выведет 1
print(p.y)  # выведет 2
</code></pre>
<p>deque:</p>
<pre><code class="language-python">from collections import deque

# создаем пустую двустороннюю очередь
d = deque()

# добавляем элементы в очередь
d.append(1)
d.append(2)
d.append(3)

# удаляем элементы из очереди
print(d.pop())  # выведет 3
print(d.popleft())  # выведет 1

# выводим оставшиеся элементы в очереди
print(d)  # выведет deque([2])
</code></pre>
<p>Counter:</p>
<pre><code class="language-python">from collections import Counter

# создаем счетчик
c = Counter(&quot;hello, world&quot;)

# выводим количество вхождений каждого символа
print(c)  # выведет Counter({&quot;l&quot;: 3, &quot;o&quot;: 2, &quot;e&quot;: 1, &quot;h&quot;: 1, &quot;,&quot;: 1, &quot; &quot;: 1, &quot;w&quot;: 1, &quot;r&quot;: 1, &quot;d&quot;: 1})

# выводим наиболее часто встречающиеся символы
print(c.most_common(2))  # выведет [(&quot;l&quot;, 3), (&quot;o&quot;, 2)]
</code></pre>
<p>OrderedDict:</p>
<pre><code class="language-python">from collections import OrderedDict

# создаем упорядоченный словарь
d = OrderedDict()

# добавляем элементы в словарь
d[&quot;a&quot;] = 1
d[&quot;b&quot;] = 2
d[&quot;c&quot;] = 3

# выводим элементы в порядке их добавления
for k, v in d.items():
    print(k, v)
# выведет:
# a 1
# b 2
# c 3
</code></pre>
<p>defaultdict:</p>
<pre><code class="language-python">from collections import defaultdict

# создаем словарь с дефолтным значением 0
d = defaultdict(int)

# добавляем элементы в словарь
d[&quot;a&quot;] += 1
d[&quot;b&quot;] += 2
d[&quot;c&quot;] += 3

# выводим словарь
print(d)  # выведет defaultdict(&lt;class &quot;int&quot;&gt;, {&quot;a&quot;: 1, &quot;b&quot;: 2, &quot;c&quot;: 3})
</code></pre>
<p>ChainMap:</p>
<pre><code class="language-python">from collections import ChainMap

# создаем два словаря
d1 = {&quot;a&quot;: 1, &quot;b&quot;: 2}
d2 = {&quot;b&quot;: 3, &quot;c&quot;: 4}

# объединяем словари в цепочку
d = ChainMap(d1, d2)

# выводим элементы словаря
print(d[&quot;a&quot;])  # выведет 1
print(d[&quot;b&quot;])  # выведет 2 (из d1, так как b в d1 появился раньше, чем в d2)
print(d[&quot;c&quot;])  # выведет 4 (из d2)

# создаем новый словарь и добавляем его в цепочку
d3 = {&quot;c&quot;: 5, &quot;d&quot;: 6}
d = d.new_child(d3)

# выводим элементы словаря
print(d[&quot;c&quot;])  # выведет 5 (из d3, так как он добавлен в цепочку позже, чем d2)
print(d[&quot;d&quot;])  # выведет 6 (из d3)
</code></pre>
<p>UserDict:</p>
<pre><code class="language-python">from collections import UserDict

# создаем пользовательский словарь
d = UserDict({&quot;a&quot;: 1, &quot;b&quot;: 2})

# добавляем элементы в словарь
d[&quot;c&quot;] = 3

# выводим элементы словаря
print(d)  # выведет {&quot;a&quot;: 1, &quot;b&quot;: 2, &quot;c&quot;: 3}
</code></pre>
<p>UserList:</p>
<pre><code class="language-python">from collections import UserList

# создаем пользовательский список
l = UserList([1, 2, 3])

# добавляем элементы в список
l.append(4)

# выводим элементы списка
print(l)  # выведет [1, 2, 3, 4]
</code></pre>
<p>UserString:</p>
<pre><code class="language-python">from collections import UserString

# создаем пользовательскую строку
s = UserString(&quot;hello, world&quot;)

# изменяем строку
s.data = s.data.upper()

# выводим строку
print(s)  # выведет HELLO, WORLD
</code></pre>