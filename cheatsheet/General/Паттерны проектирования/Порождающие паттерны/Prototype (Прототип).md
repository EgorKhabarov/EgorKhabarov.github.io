<h3>Prototype (Прототип)</h3>
<p>Паттерн Прототип позволяет копировать объекты, не зависимо от их конкретных классов.
Это особенно полезно, когда создание нового объекта требует сложной или дорогостоящей инициализации.</p>
<pre><code class="language-python">import copy

class Prototype:
    def clone(self):
        return copy.deepcopy(self)

class ConcretePrototype(Prototype):
    def __init__(self, attribute):
        self.attribute = attribute

    def __str__(self):
        return f&quot;ConcretePrototype with attribute: {self.attribute}&quot;

# Использование
prototype = ConcretePrototype(&quot;Initial value&quot;)
clone = prototype.clone()
clone.attribute = &quot;Changed value&quot;
print(prototype)
print(clone)
</code></pre>