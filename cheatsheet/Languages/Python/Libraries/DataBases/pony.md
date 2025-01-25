# Pony ORM

**Pony ORM** — это объектно-реляционная модель (ORM) для Python,
которая позволяет работать с базами данных, используя генераторы выражений Python вместо SQL-запросов.
Pony ORM поддерживает такие базы данных, как `SQLite`, `MySQL`, `PostgreSQL`, `Oracle`.

```bash
pip install pony
```

# Создание структуры

Для работы с Pony ORM, необходимо создать объекты классов, которые будут связаны с таблицами базы данных.
Используется класс `Database` для управления подключениями и класс `Entity` для создания моделей.

# Пример создания

```python
from pony.orm import Database, Required, Set

db = Database()

class Author(db.Entity):
    name = Required(str)
    books = Set("Book")

class Book(db.Entity):
    title = Required(str)
    author = Required(Author)

db.bind(provider="sqlite", filename=":memory:")
db.generate_mapping(create_tables=True)
```

# Взаимодействие с базой данных

После создания структуры базы данных, можно добавлять, изменять, удалять и извлекать данные,
используя методы Pony ORM и генераторы выражений.

### Добавление данных

```python
from pony.orm import db_session

with db_session:
    author = Author(name="J.K. Rowling")
    book = Book(title="Harry Potter and the Philosopher's Stone", author=author)
```

### Извлечение данных

```python
with db_session:
    books = Book.select(lambda b: b.author.name == "J.K. Rowling")
    for book in books:
        print(book.title)
```

### Обновление данных

```python
with db_session:
    book = Book.get(title="Harry Potter and the Philosopher's Stone")
    book.title = "Harry Potter and the Sorcerer's Stone"
```

### Удаление данных

```python
with db_session:
    book = Book.get(title="Harry Potter and the Sorcerer's Stone")
    book.delete()
```

### Генераторы выражений (Query Expressions)

Pony ORM позволяет использовать Python выражения для фильтрации, сортировки и выборки данных.
Это делает код более читабельным и легким в написании.

```python
with db_session:
    books = select(b for b in Book if "Harry Potter" in b.title)
    for book in books:
        print(book.title)
```

# Отношения между сущностями

Pony ORM поддерживает различные типы отношений между сущностями

### **Один-ко-многим (One-to-Many)**:
Пример был показан выше, где один автор может написать несколько книг (отношение `Author -> Book`).

### **Многие-ко-многим (Many-to-Many)**:
Пример создания связи между студентами и курсами, которые они могут посещать.

```python
class Student(db.Entity):
    name = Required(str)
    courses = Set("Course")

class Course(db.Entity):
    name = Required(str)
    students = Set(Student)
```

### **Один-к-одному (One-to-One)**
Связь между студентом и его личным профилем.

```python
class Profile(db.Entity):
    student = Required("Student")
    bio = Required(str)

class Student(db.Entity):
    name = Required(str)
    profile = Required(Profile)
```

# Транзакции

Pony ORM автоматически управляет транзакциями через контекстный менеджер `db_session`.
Все операции, выполняемые в рамках `db_session`, происходят в одной транзакции.
Pony ORM автоматически коммитит или откатывает транзакцию в зависимости от результата выполнения.

```python
from pony.orm import db_session

with db_session:
    author = Author(name="George Orwell")
    book = Book(title="1984", author=author)
```

# Кэширование

Pony ORM кэширует объекты в рамках одной сессии `db_session`.
Это значит, что повторные запросы за одним и тем же объектом
в рамках одной сессии не будут обращаться к базе данных.

```python
with db_session:
    author1 = Author.get(name="George Orwell")
    author2 = Author.get(name="George Orwell")
    print(author1 is author2)  # True
```

### Пример полной работы с базой данных

```python
from pony.orm import Database, Required, Set, db_session, select

db = Database()

class Author(db.Entity):
    name = Required(str)
    books = Set("Book")

class Book(db.Entity):
    title = Required(str)
    author = Required(Author)

# Привязка базы данных к SQLite
db.bind(provider="sqlite", filename="library.sqlite", create_db=True)
db.generate_mapping(create_tables=True)

# Добавление данных
with db_session:
    author = Author(name="George Orwell")
    book1 = Book(title="1984", author=author)
    book2 = Book(title="Animal Farm", author=author)

# Извлечение данных
with db_session:
    books = select(b for b in Book if b.author.name == "George Orwell")
    for book in books:
        print(f"{book.title} by {book.author.name}")

# Обновление данных
with db_session:
    book = Book.get(title="1984")
    book.title = "Nineteen Eighty-Four"

# Удаление данных
with db_session:
    book = Book.get(title="Animal Farm")
    book.delete()
```

# Особенности работы с Pony ORM

- **Ленивая загрузка**: Pony ORM автоматически загружает связанные данные только тогда, когда они необходимы.
- **Оптимизация запросов**: Генераторы выражений оптимизируются в SQL-запросы, что обеспечивает производительность.
- **Поддержка сложных запросов**: Можно выполнять сложные SQL-запросы с использованием привычных Python-выражений.
