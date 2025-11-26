`match-case` мощная конструкция в Python, введённая в версии 3.10,
для реализации сопоставления с образцом (pattern matching).
Она позволяет писать более читаемый и лаконичный код для работы с разными типами данных, структур и условий.

## Синтаксис
```python
match value:
    case template1:
        pass  # Код для template1
    case template2 if condition:
        pass  # Код для template2 при выполнении условия
    case _:
        pass  # Код по умолчанию (аналог else)
```

# Особенности и ключевые фишки
### Сопоставление по значению
Простое сопоставление с конкретным значением
```python
match x:
   case 1:
       print("x равно 1")
   case 2:
       print("x равно 2")
   case _:
       print("Другое значение")
```

### Сопоставление с переменной
Переменные в шаблонах записываются как есть, а `_` используется как "любое значение"
```python
match x:
   case y if y > 0:
       print(f"Положительное число: {y}")
   case _:
       print("Не положительное число")
```

### Сопоставление с коллекциями
Списки, кортежи и их элементы:
```python
match lst:
   case [1, 2, 3]:
       print("Список точно равен [1, 2, 3]")
   case [1, *rest]:  # Распаковка
       print(f"Начинается с 1, остальные элементы: {rest}")
   case _:
       print("Неизвестный список")
```

### Сопоставление с объектами
Использование `attr` для проверки полей объекта:
```python
class Point:
   def __init__(self, x, y):
       self.x = x
       self.y = y

point = Point(3, 4)

match point:
   case Point(x=0, y=0):
       print("Точка в начале координат")
   case Point(x, y) if x == y:
       print(f"Точка на линии y = x: ({x}, {y})")
   case Point(x, y):
       print(f"Координаты точки: ({x}, {y})")
```

### Вложенные структуры
Сопоставление сложных вложенных структур:
```python
match data:
   case {"user": {"id": int(id_), "name": str(name)}}:
       print(f"ID: {id_}, Name: {name}")
   case _:
       print("Неподходящая структура")
```

### Комбинация условий (OR)
Использование `|` для нескольких шаблонов:
```python
match x:
   case 1 | 2 | 3:
       print("x равно 1, 2 или 3")
   case _:
       print("Другое значение")
```

### Сопоставление с литералами и типами
Проверка типов:
```python
match obj:
   case int():
       print("Это целое число")
   case str() as s if s.isdigit():
       print(f"Это строка с числом: {s}")
   case _:
       print("Другой тип")
```

# Примеры с пояснениями

### Обработка HTTP-статусов
```python
match status_code:
   case 200:
       print("OK")
   case 404:
       print("Not Found")
   case 500 | 501:
       print("Server Error")
   case _:
       print("Unknown status")
```

### Работа с JSON-данными
```python
data = {"type": "error", "code": 500}

match data:
   case {"type": "error", "code": code} if code >= 500:
       print(f"Критическая ошибка: {code}")
   case {"type": "success", "data": content}:
       print(f"Успешный ответ: {content}")
   case _:
       print("Неизвестный формат")
```

### Анализ выражений
```python
expr = ("+", 3, 5)

match expr:
   case ("+", a, b):
       print(f"Сумма: {a + b}")
   case ("*", a, b):
       print(f"Произведение: {a * b}")
   case _:
       print("Неизвестное выражение")
```

### Пример с сопоставлением точек
```python
match (x, y):
   case (0, 0):
       print("Начало координат")
   case (x, 0):
       print(f"На оси X, x = {x}")
   case (0, y):
       print(f"На оси Y, y = {y}")
   case (x, y):
       print(f"В точке ({x}, {y})")
```
