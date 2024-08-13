<p><code>@overload</code> - это декоратор в Python, который используется для определения перегрузки метода внутри класса. 
Перегрузка метода - это механизм, позволяющий определить несколько версий метода с разными параметрами. 
При вызове метода, интерпретатор Python выберет версию метода, которая соответствует переданным аргументам.</p>
<pre><code class="language-python">from typing import overload

class MyClass:
    @overload
    def my_method(self, arg1: int) -&gt; int:
        pass

    @overload
    def my_method(self, arg1: str) -&gt; str:
        pass

    def my_method(self, arg1):
        if isinstance(arg1, int):
            return arg1 * 2
        elif isinstance(arg1, str):
            return arg1.upper()


obj = MyClass()
print(obj.my_method(2))        # 4
print(obj.my_method(&quot;hello&quot;))  # HELLO
</code></pre>