### Шпаргалка по библиотеке Peewee

**Peewee** — это простая и небольшая **ORM** (**Object-Relational Mapping**) библиотека для Python,
которая позволяет взаимодействовать с базами данных через Python-классы и объекты.

```bash
pip install peewee
```

# Подключение

Peewee поддерживает разные базы данных: `SQLite`, `MySQL`, `PostgreSQL` и т.д.

### SQLite
```python
from peewee import SqliteDatabase

db = SqliteDatabase("my_database.db")
```

### PostgreSQL
```python
from peewee import PostgresqlDatabase

db = PostgresqlDatabase("my_database", user="username", password="password", host="localhost", port=5432)
```

### MySQL
```python
from peewee import MySQLDatabase

db = MySQLDatabase("my_database", user="username", password="password", host="localhost", port=3306)
```

# Определение моделей
```python
from peewee import Model, CharField, IntegerField

class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    username = CharField(unique=True)
    age = IntegerField()
```

# Создание таблиц
```python
db.connect()
db.create_tables([User])
```

# Добавление записей
```python
# Создание записи
user = User.create(username="john", age=30)

# Или создание объекта и сохранение через метод save
user = User(username="doe", age=25)
user.save()
```

# Поиск записей
### Получение всех записей
```python
users = User.select()
for user in users:
    print(user.username, user.age)
```

### Фильтрация записей
```python
john = User.get(User.username == "john")
```

### Фильтрация с использованием условий
```python
adults = User.select().where(User.age >= 18)
```

### Получение первой записи
```python
first_user = User.select().first()
```

# Обновление записей
```python
# Обновление записи через объект
user = User.get(User.username == "john")
user.age = 31
user.save()

# Обновление записи через метод update
User.update(age=32).where(User.username == "john").execute()
```

# Удаление записей

```python
# Удаление записи через объект
user = User.get(User.username == "john")
user.delete_instance()

# Удаление записи через метод delete
User.delete().where(User.username == "john").execute()
```

# Связи между моделями
### Один ко многим (ForeignKeyField)
```python
from peewee import ForeignKeyField

class Blog(BaseModel):
    title = CharField()
    content = CharField()
    author = ForeignKeyField(User, backref="blogs")

# Пример создания блога, связанного с пользователем
user = User.get(User.username == "doe")
blog = Blog.create(title="My First Blog", content="Hello, world!", author=user)
```

### Многие ко многим
Для реализации отношений «многие ко многим» создается промежуточная таблица:
```python
class Tag(BaseModel):
    name = CharField(unique=True)

class BlogTag(BaseModel):
    blog = ForeignKeyField(Blog)
    tag = ForeignKeyField(Tag)
```

# Построение запросов
### Сортировка
```python
# Сортировка по возрасту
users = User.select().order_by(User.age.desc())
```

### Лимит и смещение
```python
# Ограничение количества записей
limited_users = User.select().limit(10)
```

### Группировка
```python
# Группировка и подсчет количества
from peewee import fn

user_counts = User.select(fn.COUNT(User.id)).group_by(User.age)
```

# Транзакции
Транзакции в Peewee позволяют выполнять несколько запросов к базе данных как одну атомарную операцию.
```python
with db.atomic():
    User.create(username="alice", age=23)
    User.create(username="bob", age=35)
```

### Пример построения структуры базы данных
Допустим, мы создаем блог-платформу, где пользователи могут публиковать посты, комментировать и добавлять теги.
```python
import datetime
from peewee import Model, CharField, TextField, ForeignKeyField, DateTimeField, SqliteDatabase

db = SqliteDatabase("blog.db")

class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    username = CharField(unique=True)
    password = CharField()

class Blog(BaseModel):
    title = CharField()
    content = TextField()
    pub_date = DateTimeField(default=datetime.datetime.now)
    author = ForeignKeyField(User, backref="blogs")

class Comment(BaseModel):
    blog = ForeignKeyField(Blog, backref="comments")
    user = ForeignKeyField(User, backref="comments")
    content = TextField()
    pub_date = DateTimeField(default=datetime.datetime.now)

class Tag(BaseModel):
    name = CharField(unique=True)

class BlogTag(BaseModel):
    blog = ForeignKeyField(Blog, backref="tags")
    tag = ForeignKeyField(Tag, backref="blogs")

# Создание таблиц
db.connect()
db.create_tables([User, Blog, Comment, Tag, BlogTag])

# Пример создания записи
user = User.create(username="john_doe", password="password123")
blog = Blog.create(title="My Blog Post", content="This is my first post", author=user)
comment = Comment.create(blog=blog, user=user, content="Nice post!")
tag = Tag.create(name="Python")
BlogTag.create(blog=blog, tag=tag)
```

# Пагинация
```python
def paginate(query, page, page_size=10):
    return query.paginate(page, page_size)

# Получение первой страницы с 10 записями
first_page = paginate(User.select(), 1, 10)
```

# Миграции
Для изменения структуры базы данных рекомендуется использовать миграции.
В Peewee для этого есть библиотека `playhouse.migrate`
```python
from playhouse.migrate import *

migrator = SqliteMigrator(db)

# Добавление нового поля в таблицу User
migrate(migrator.add_column("user", "email", CharField(null=True)))
```
