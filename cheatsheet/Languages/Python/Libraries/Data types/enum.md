<p>Библиотека "enum" в Python используется для создания и использования перечислений,
которые представляют собой набор именованных значений.
Она облегчает работу с ограниченным набором значений, обеспечивая их типизацию и удобный доступ.</p>
<p>Методы модуля "enum" и его подмодулей:</p>
<p>Модуль "enum":
Enum: Базовый класс для создания перечислений.
auto: Декоратор, который автоматически присваивает значения перечисления.</p>
<p>Подмодуль "Enum":
name: Возвращает имя элемента перечисления.
value: Возвращает значение элемента перечисления.</p>
<p>Подмодуль "IntEnum":
IntEnum: Базовый класс для создания перечислений с целочисленными значениями.</p>
<p>Подмодуль "Flag":
Flag: Базовый класс для создания перечислений с битовыми флагами.
auto: Декоратор, который автоматически присваивает значения флагов.</p>
<p>Некоторые из самых часто используемых методов "enum" и их описание:</p>
<p>Enum.name: Возвращает имя элемента перечисления.</p>
<pre><code class="language-python">from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

print(Color.RED.name)  # Выводит &quot;RED&quot;
</code></pre>
<p>Enum.value: Возвращает значение элемента перечисления.</p>
<pre><code class="language-python">from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

print(Color.RED.value)  # Выводит 1
</code></pre>
<p>Flag: Базовый класс для создания перечислений с битовыми флагами.</p>
<pre><code class="language-python">from enum import Flag, auto

class Permissions(Flag):
    READ = auto()
    WRITE = auto()
    EXECUTE = auto()

user_permissions = Permissions.READ | Permissions.WRITE
print(user_permissions)  # Выводит &lt;Permissions.READ|WRITE: 3&gt;
</code></pre>