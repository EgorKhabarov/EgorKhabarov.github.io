<h3>Bridge (Мост)</h3>
<p>Паттерн Мост используется для разделения абстракции и её реализации, позволяя изменять их независимо.
Это достигается использованием интерфейсов или абстрактных классов.</p>
<pre><code class="language-python">class DrawingAPI:
    def draw_circle(self, x, y, radius):
        pass

class DrawingAPI1(DrawingAPI):
    def draw_circle(self, x, y, radius):
        print(f&quot;API1.circle at ({x}, {y}), radius {radius}&quot;)

class DrawingAPI2(DrawingAPI):
    def draw_circle(self, x, y, radius):
        print(f&quot;API2.circle at ({x}, {y}), radius {radius}&quot;)

class Circle:
    def __init__(self, x, y, radius, drawing_api):
        self.x = x
        self.y = y
        self.radius = radius
        self.drawing_api = drawing_api

    def draw(self):
        self.drawing_api.draw_circle(self.x, self.y, self.radius)

    def scale(self, factor):
        self.radius *= factor

# Использование
circle1 = Circle(1, 2, 3, DrawingAPI1())
circle1.draw()

circle2 = Circle(5, 7, 11, DrawingAPI2())
circle2.draw()
</code></pre>