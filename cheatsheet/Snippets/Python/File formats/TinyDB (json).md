```bash
pip install tinydb
```

```python
from tinydb import TinyDB, Query


db = TinyDB("db.json")
users_table = db.table("users")
user_id = users_table.insert({"name": "John", "age": 25})
all_users = users_table.all()

# Получение записи по условию (например, по имени)
user_query = Query()
john_data = users_table.search(user_query.name == "John")

# Изменение данных в записи по условию (например, по имени)
users_table.update({"age": 26}, user_query.name == "John")

# Удаление записи по условию (например, по имени)
users_table.remove(user_query.name == "John")
```

[[Snippets/Python/File formats/JSON]]
