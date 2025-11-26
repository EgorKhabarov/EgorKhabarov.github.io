### Builder (Строитель)
Паттерн Строитель используется для пошагового создания сложных объектов
Он отделяет конструирование объекта от его представления, так что один и тот же процесс создания может создавать разные представления

```python
class House:
    def __init__(self):
        self.walls = None
        self.roof = None
        self.doors = None

    def __str__(self):
        return f"Walls: {self.walls}, Roof: {self.roof}, Doors: {self.doors}"


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


builder = HouseBuilder()
house = builder.build_walls("Brick walls").build_roof("Tile roof").build_doors("Wooden doors").get_house()
print(house)
```
