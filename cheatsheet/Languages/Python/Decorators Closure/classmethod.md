<p>Декоратор <code>@classmethod</code> используется для определения методов класса,
которые принимают первый аргумент в виде самого класса (обычно называемый <code>cls</code>),
а не экземпляра класса (как в случае с методами экземпляра, где первый аргумент называется <code>self</code>).</p>
<p><code>@classmethod</code> позволяет вызывать метод как на экземпляре класса, так и на самом классе.</p>
<pre><code class="language-python">class MyClass:
    @classmethod
    def foo(cls, arg):
        print(arg)


MyClass.foo(5)    # 5
MyClass().foo(6)  # 6
</code></pre>