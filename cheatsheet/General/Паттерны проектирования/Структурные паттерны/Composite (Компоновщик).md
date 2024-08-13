<h3>Composite (Компоновщик)</h3>
<p>Паттерн Компоновщик позволяет работать с группами объектов так же, как с отдельными объектами.
Это удобно для представления иерархических структур.</p>
<pre><code class="language-python">class Graphic:
    def render(self):
        pass

class Line(Graphic):
    def render(self):
        print(&quot;Rendering a line&quot;)

class Rectangle(Graphic):
    def render(self):
        print(&quot;Rendering a rectangle&quot;)

class GraphicGroup(Graphic):
    def __init__(self):
        self.graphics = []

    def add(self, graphic):
        self.graphics.append(graphic)

    def render(self):
        for graphic in self.graphics:
            graphic.render()

# Использование
group = GraphicGroup()
group.add(Line())
group.add(Rectangle())
group.add(Line())

group.render()
</code></pre>