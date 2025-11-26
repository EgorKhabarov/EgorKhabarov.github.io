### Composite (Компоновщик)

Паттерн Компоновщик позволяет работать с группами объектов так же, как с отдельными объектами
Это удобно для представления иерархических структур

```python
class Graphic:
    def render(self):
        pass


class Line(Graphic):
    def render(self):
        print("Rendering a line")


class Rectangle(Graphic):
    def render(self):
        print("Rendering a rectangle")


class GraphicGroup(Graphic):
    def __init__(self):
        self.graphics = []

    def add(self, graphic):
        self.graphics.append(graphic)

    def render(self):
        for graphic in self.graphics:
            graphic.render()


group = GraphicGroup()
group.add(Line())
group.add(Rectangle())
group.add(Line())
group.render()
# Rendering a line
# Rendering a rectangle
# Rendering a line
```
