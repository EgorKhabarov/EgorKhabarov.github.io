# Domain-Driven Design (DDD)

Domain-Driven Design (DDD) — это подход к разработке программного обеспечения, ориентированный на модель предметной области
Он помогает структурировать код так, чтобы он был гибким, поддерживаемым и понятным для бизнеса

# Основные концепции DDD

## Предметная область (Domain)
Это сфера реального мира, для которой разрабатывается ПО
Например, если мы разрабатываем банковскую систему, то предметная область — это банковские операции, клиенты, счета

## Ограниченный контекст (Bounded Context)
Определяет границы ответственности внутри системы
Например, в банковском ПО может быть контекст "Кредитование" и контекст "Счета"

## Язык предметной области (Ubiquitous Language)
Общий язык, используемый как разработчиками, так и бизнесом, для единообразного понимания системы

# Основные строительные блоки DDD

### Сущность (Entity)
Объект, имеющий уникальный идентификатор

```python
class User:
    def __init__(self, user_id: int, name: str):
        self.user_id = user_id
        self.name = name

    def change_name(self, new_name: str):
        self.name = new_name
```

### Значимый объект (Value Object)
Объект, не имеющий идентификатора, определяется только своими значениями

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Money:
    amount: float
    currency: str
```

### Агрегат (Aggregate)
Группа связанных сущностей с корневой сущностью (Aggregate Root), через которую происходит управление

```python
class Order:
    def __init__(self, order_id: int, user: User):
        self.order_id = order_id
        self.user = user
        self.items = []

    def add_item(self, item):
        self.items.append(item)
```

### Репозиторий (Repository)
Объект, который управляет хранилищем данных для сущностей

```python
class UserRepository:
    def __init__(self):
        self.users = {}

    def save(self, user: User):
        self.users[user.user_id] = user

    def get(self, user_id: int):
        return self.users.get(user_id)
```

### Сервис домена (Domain Service)
Используется, если логика не принадлежит конкретной сущности

```python
class PaymentService:
    @staticmethod
    def process_payment(order: Order, money: Money):
        print(f"Processing {money.amount} {money.currency} for order {order.order_id}")
```

### События домена (Domain Events)
Фиксируют важные изменения в системе

```python
class OrderCreated:
    def __init__(self, order_id: int):
        self.order_id = order_id
```

# Принципы проектирования в DDD

1. **Чёткие границы контекста** – Каждое подмножество системы должно иметь своё чёткое назначение
2. **Использование Ubiquitous Language** – Единый язык для общения между разработчиками и бизнесом
3. **Сущности должны управлять своими данными** – Избегаем анемичных моделей (только с геттерами и сеттерами)
4. **Отделение доменной логики от инфраструктуры** – Например, репозитории отделены от сущностей

# Когда применять DDD?

- Если система сложная и меняется со временем
- Если важно, чтобы код был понятен бизнес-экспертам
- Если требуется гибкая архитектура с долгосрочной поддерживаемостью

DDD помогает строить масштабируемые, поддерживаемые системы с чистой архитектурой, особенно для сложных предметных областей
