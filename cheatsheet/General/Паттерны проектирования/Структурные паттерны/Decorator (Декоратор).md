<h2>Decorator (Декоратор)</h2>
<p><strong>Описание:</strong> Позволяет динамически добавлять новое поведение объектам, оборачивая их в класс-оболочку.</p>
<p><strong>Когда использовать:</strong> Когда нужно добавлять дополнительные функциональности объектам без изменения их класса.</p>
<p><strong>Пример реализации:</strong></p>
<pre><code class="language-python">class Component:
    def operation(self):
        pass

class ConcreteComponent(Component):
    def operation(self):
        return &quot;ConcreteComponent&quot;

class Decorator(Component):
    def __init__(self, component):
        self._component = component

    def operation(self):
        return f&quot;Decorator({self._component.operation()})&quot;

component = ConcreteComponent()
decorated = Decorator(component)
print(decorated.operation())  # Вывод: &quot;Decorator(ConcreteComponent)&quot;
</code></pre>