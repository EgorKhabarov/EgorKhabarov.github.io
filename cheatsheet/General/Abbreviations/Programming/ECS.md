# ECS

**ECS (Entity-Component-System)** — это шаблон проектирования, в котором данные и логика строго разделены:

- **Entity (Сущность)** — уникальный идентификатор объекта
- **Component (Компонент)** — структура данных, описывающая аспект поведения или состояния
- **System (Система)** — логика, работающая с группами сущностей по наличию компонентов

Такой подход особенно популярен в игровых движках и симуляциях

## Компоненты

Компоненты — это простые классы или структуры, содержащие только данные (никакой логики)

```python
class Position:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Velocity:
    def __init__(self, dx=0, dy=0):
        self.dx = dx
        self.dy = dy

class Health:
    def __init__(self, hp=100):
        self.hp = hp
```

## Сущности

Сущность — просто уникальный ID (обычно `int` или `uuid.UUID`).

```python
import itertools

class EntityManager:
    def __init__(self):
        self._id_gen = itertools.count()
    
    def create_entity(self):
        return next(self._id_gen)
```

### Хранилище компонентов

Используем словари, чтобы хранить компоненты по типу и привязке к сущностям

```python
class World:
    def __init__(self):
        self.components = {}  # {ComponentType: {entity_id: component}}

    def add_component(self, entity, component):
        ctype = type(component)
        if ctype not in self.components:
            self.components[ctype] = {}
        self.components[ctype][entity] = component

    def get_component(self, component_type):
        return self.components.get(component_type, {})

    def get_entity_components(self, entity):
        return {
            ctype: comps[entity]
            for ctype, comps in self.components.items()
            if entity in comps
        }
```

## Системы

Система перебирает сущности, у которых есть нужные компоненты, и применяет к ним поведение

### Система перемещения

```python
class MovementSystem:
    def update(self, world, dt):
        positions = world.get_component(Position)
        velocities = world.get_component(Velocity)

        for entity in positions:
            if entity in velocities:
                pos = positions[entity]
                vel = velocities[entity]
                pos.x += vel.dx * dt
                pos.y += vel.dy * dt
```

### Система урона

```python
class DamageSystem:
    def update(self, world):
        healths = world.get_component(Health)
        for entity, health in healths.items():
            health.hp -= 1
            if health.hp <= 0:
                print(f"Entity {entity} is dead")
```

# Использование

```python
# Создание мира и сущностей
world = World()
entities = EntityManager()

player = entities.create_entity()
enemy = entities.create_entity()

# Назначение компонентов
world.add_component(player, Position(0, 0))
world.add_component(player, Velocity(1, 1))
world.add_component(player, Health(10))

world.add_component(enemy, Position(5, 5))
world.add_component(enemy, Health(3))

# Создание систем
movement = MovementSystem()
damage = DamageSystem()

# Цикл обновления
for frame in range(5):
    movement.update(world, dt=1.0)
    damage.update(world)
```

# Расширение

Ты можешь добавить:

- **Фильтрацию сущностей**: метод `get_entities_with(*component_types)`
- **Удаление компонентов и сущностей**
- **События** и **сигналы**
- **Системы с приоритетами**
- **Система тегов/группировки**

# Преимущества

- Высокая производительность при правильной реализации
- Гибкость и масштабируемость
- Чёткое разделение данных и логики

# Недостатки

- Непривычная парадигма для тех, кто привык к ООП
- Повышенная сложность без фреймворка
- Могут быть проблемы с отладкой при большой вложенности

### Фильтрация по компонентам

```python
def get_entities_with(world, *component_types):
    if not component_types:
        return set()

    sets = [set(world.get_component(t).keys()) for t in component_types]
    return set.intersection(*sets)
```

```python
for entity in get_entities_with(world, Position, Health):
    pos = world.get_component(Position)[entity]
    hp = world.get_component(Health)[entity]
    print(f"Entity {entity} is at ({pos.x}, {pos.y}) with HP {hp.hp}")
```
