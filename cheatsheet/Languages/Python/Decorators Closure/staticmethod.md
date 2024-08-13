<p><code>@staticmethod</code> - это декоратор в Python, который используется для определения статического метода внутри класса. 
Статический метод - это метод, который может быть вызван на классе, а не на экземпляре класса. 
Он не имеет доступа к экземпляру класса и не может изменять его состояние.</p>
<pre><code class="language-python">class MyClass:
    @staticmethod
    def my_static_method(arg1, arg2):
        return arg1 + arg2

print(MyClass.my_static_method(1, 2))  # 3
</code></pre>
<p>В этом примере мы определили класс <code>MyClass</code> и внутри него определили статический метод <code>my_static_method</code>. 
Этот метод принимает два аргумента <code>arg1</code> и <code>arg2</code> и возвращает их сумму. 
Затем мы вызвали этот метод на классе <code>MyClass</code>, а не на экземпляре класса.</p>