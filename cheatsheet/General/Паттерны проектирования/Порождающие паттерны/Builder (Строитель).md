<h3>Builder (Строитель)</h3>
<p>Паттерн Строитель используется для пошагового создания сложных объектов.
Он отделяет конструирование объекта от его представления,
так что один и тот же процесс создания может создавать разные представления.</p>
<pre><code class="language-python">class House:
    def __init__(self):
        self.walls = None
        self.roof = None
        self.doors = None

    def __str__(self):
        return f&quot;Walls: {self.walls}, Roof: {self.roof}, Doors: {self.doors}&quot;

class HouseBuilder:
    def __init__(self):
        self.house = House()

    def build_walls(self, walls):
        self.house.walls = walls
        return self

    def build_roof(self, roof):
        self.house.roof = roof
        return self

    def build_doors(self, doors):
        self.house.doors = doors
        return self

    def get_house(self):
        return self.house

# Использование
builder = HouseBuilder()
house = builder.build_walls(&quot;Brick walls&quot;).build_roof(&quot;Tile roof&quot;).build_doors(&quot;Wooden doors&quot;).get_house()
print(house)
</code></pre>