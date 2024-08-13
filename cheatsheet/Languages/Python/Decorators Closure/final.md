<p><code>@final</code> - это аннотация (декоратор) в Python, которая указывает, что метод или свойство класса не должны переопределяться в подклассах.</p>
<p>Когда метод или свойство класса помечаются аннотацией <code>@final</code>, это предупреждает программистов, 
что эти элементы класса являются частью публичного интерфейса класса, который не должен изменяться в подклассах. 
Это позволяет сделать класс более простым и предсказуемым в использовании, так как гарантируется, 
что поведение не будет изменено в производных классах.</p>
<pre><code class="language-python">from typing import final


class BaseClass:
    @final
    def some_method(self):
        pass

class DerivedClass(BaseClass):
    def some_method(self):  # Ошибка: невозможно переопределить метод
        pass
</code></pre>
<pre><code class="language-python">from typing import final

@final
class FinalClass:
    pass

class AnotherClass(FinalClass):  # Ошибка: невозможно наследовать от FinalClass
    pass
</code></pre>
<blockquote>
<p>Декоратор <code>@final</code> является частью системы типизации Python и,
следовательно, не влияет на выполнение кода в интерпретаторе Python.
Он предназначен для статической проверки и повышения читаемости кода.</p>
</blockquote>