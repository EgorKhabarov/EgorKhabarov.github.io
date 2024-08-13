<ul>
<li>slice</li>
<li>frozenset</li>
<li>memoryview</li>
<li>hasattr</li>
<li>reversed</li>
<li>&#95;&#95;import&#95;&#95;</li>
<li>staticmethod</li>
<li>setattr</li>
<li>property</li>
<li>object, </li>
<li>locals</li>
<li>globals</li>
<li>getattr</li>
<li>complex</li>
<li>compile</li>
<li>bytearray</li>
<li>abs</li>
<li>bin</li>
<li>bytes</li>
<li>callable</li>
<li>chr</li>
<li>classmethod</li>
<li>delattr</li>
<li>dir</li>
<li>divmod</li>
<li>filter</li>
<li>oct</li>
<li>nonlocal</li>
</ul>
<h2>slice</h2>
<pre><code class="language-python">print([1, 2, 3, 4, 5][1:4])  # [2, 3, 4]
print([1, 2, 3, 4, 5][slice(1, 4)])  # [2, 3, 4]
</code></pre>
<h2>frozenset</h2>
<p>Неизменяемый тип данных, представляющий собой неупорядоченное множество уникальных элементов.</p>
<pre><code class="language-python">print(frozenset([1, 2, 2, 3, 4]))  # frozenset({1, 2, 3, 4})
</code></pre>
<h2>memoryview</h2>
<p>Доступ к буферу памяти объекта без копирования его данных.</p>
<pre><code class="language-python">my_bytes = bytes([1, 2, 3, 4, 5])
print(memoryview(my_bytes)[1])  # 2
</code></pre>
<h2>hasattr</h2>
<p>Для проверки наличия атрибута (метода или свойства) у объекта.</p>
<pre><code class="language-python">class MyClass:
    def __init__(self):
        self.my_attr = 42

my_obj = MyClass()
print(hasattr(my_obj, &quot;my_attr&quot;))  # True
print(hasattr(my_obj, &quot;non_existent_attr&quot;))  # False
</code></pre>
<h2>reversed</h2>
<p>Для переворачивания последовательности (sequence).</p>
<pre><code class="language-python">my_list = [1, 2, 3, 4, 5]
reversed_list = reversed(my_list)
print(list(reversed_list))  # [5, 4, 3, 2, 1]
</code></pre>
<h2><strong>import</strong></h2>
<p>Для импорта модуля во время выполнения программы.</p>
<pre><code class="language-python">math = __import__(&quot;math&quot;)
print(math.pi)  # 3.141592653589793
</code></pre>
<h2>staticmethod</h2>
<p>Для создания метода класса, который не принимает первый аргумент self (или cls для методов класса).</p>
<pre><code class="language-python">class MyClass:
    @staticmethod
    def my_static_method():
        print(&quot;This is a static method&quot;)

MyClass.my_static_method()  # This is a static method
</code></pre>
<h2>setattr</h2>
<p>Для установки значения атрибута объекта.</p>
<pre><code class="language-python">class MyClass:
    def __init__(self):
        self.my_attr = 42

my_obj = MyClass()
setattr(my_obj, &quot;my_attr&quot;, 43)
print(my_obj.my_attr)  # 43
</code></pre>
<h2>property</h2>
<p>Для создания свойства объекта, которое можно читать и записывать, как обычный атрибут.</p>
<pre><code class="language-python">class MyClass:
    def __init__(self):
        self._my_attr = 42

    @property
    def my_attr(self):
        return self._my_attr

    @my_attr.setter
    def my_attr(self, value):
        self._my_attr
</code></pre>
<h2>object</h2>
<p>Базовый класс, от которого наследуются все остальные классы в Python.</p>
<pre><code class="language-python">class MyClass(object):
    pass
</code></pre>
<h2>locals</h2>
<p>Для получения словаря с локальными переменными в текущем контексте выполнения.</p>
<pre><code class="language-python">def my_func():
    a = 1
    b = 2
    print(locals())

my_func()  # {&quot;a&quot;: 1, &quot;b&quot;: 2}
</code></pre>
<h2>globals</h2>
<p>Для получения словаря с глобальными переменными в текущем модуле.</p>
<pre><code class="language-python">my_var = 42
print(globals())  # {&quot;__name__&quot;: &quot;__main__&quot;, &quot;__doc__&quot;: None, &quot;__package__&quot;: None, &quot;my_var&quot;: 42, ...}
</code></pre>
<h2>getattr</h2>
<p>Для получения значения атрибута объекта по его имени.</p>
<pre><code class="language-python">class MyClass:
    def __init__(self):
        self.my_attr = 42

print(getattr(MyClass(), &quot;my_attr&quot;))  # 42
</code></pre>
<h2>complex</h2>
<p>Для создания комплексного числа.</p>
<pre><code class="language-python">print(complex(1, 2))  # (1+2j)
</code></pre>
<h2>compile</h2>
<p>Для компиляции строки с кодом Python в объект-код.</p>
<pre><code class="language-python">exec(compile('print(&quot;Hello, world!&quot;)', &quot;&lt;string&gt;&quot;, &quot;exec&quot;))  # Hello, world!
</code></pre>
<h2>bytearray</h2>
<p>Изменяемый тип данных, представляющий собой массив байтов.</p>
<pre><code class="language-python">print(bytearray([1, 2, 3, 4, 5]))  # bytearray(b&quot;\x01\x02\x03\x04\x05&quot;)
</code></pre>
<h2>abs</h2>
<p>Получения абсолютного значения числа.</p>
<pre><code class="language-python">print(abs(-42))  # 42
</code></pre>
<h2>bin</h2>
<p>Получения двоичного представления числа.</p>
<pre><code class="language-python">print(bin(42))  # 0b101010
</code></pre>
<h2>bytes</h2>
<p>Неизменяемый тип данных, представляющий собой массив байтов.</p>
<pre><code class="language-python">print(bytes([1, 2, 3, 4, 5]))  # b&quot;\x01\x02\x03\x04\x05&quot;
</code></pre>
<h2>callable</h2>
<p>Является ли объект вызываемым (т.е. функцией или методом).</p>
<pre><code class="language-python">def my_func():
    pass

class MyClass:
    def my_method(self):
        pass

print(callable(my_func))  # True
print(callable(MyClass().my_method))  # True
print(callable(42))  # False
</code></pre>
<h2>chr</h2>
<p>Получение символа Unicode по его коду.</p>
<pre><code class="language-python">print(chr(97))  # &quot;a&quot;
</code></pre>
<h2>classmethod</h2>
<p>Создание метода класса. Этот метод может быть вызван без создания экземпляра класса.</p>
<pre><code class="language-python">class MyClass:
    my_class_attr = 42

    @classmethod
    def my_class_method(cls):
        print(cls.my_class_attr)

MyClass.my_class_method()  # 42
</code></pre>
<h2>delattr</h2>
<p>Удаление атрибута объекта.</p>
<pre><code class="language-python">class MyClass:
    my_attr = 42

my_obj = MyClass()
delattr(my_obj, &quot;my_attr&quot;)
print(hasattr(my_obj, &quot;my_attr&quot;))  # False
</code></pre>
<h2>dir</h2>
<p>Получение списка всех атрибутов объекта.</p>
<pre><code class="language-python">print(dir([1, 2, 3]))  # [&quot;__add__&quot;, &quot;__class__&quot;, &quot;__contains__&quot;, ...]
</code></pre>
<h2>divmod</h2>
<p>Получения частного и остатка от деления двух чисел.</p>
<pre><code class="language-python">print(divmod(42, 5))  # (8, 2)
</code></pre>
<h2>filter</h2>
<p>Фильтрация элементов последовательности с помощью функции.</p>
<pre><code class="language-python">print(list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5])))  # [2, 4]
</code></pre>
<h2>oct</h2>
<p>Получение восьмеричного представления числа.</p>
<pre><code class="language-python">print(oct(42))  # 0o52
</code></pre>
<h2>nonlocal</h2>
<p>Объявление переменной из внешней области видимости внутри функции.</p>
<pre><code class="language-python">def my_func():
    my_var = 42
    def inner_func():
        nonlocal my_var
        my_var = 43
    inner_func()
    print(my_var)

my_func()  # 43
</code></pre>