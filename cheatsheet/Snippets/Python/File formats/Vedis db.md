```python
from vedis import Vedis

db = Vedis(":mem:")  # Create an in-memory database
db = Vedis("database.vedis")

with db.transaction():
    db["key"] = "value"
    db.rollback()  # Undo changes
    db.commit()

print(db["key"])
```

[https://vedis-python.readthedocs.io/en/latest/quickstart.html](https://vedis-python.readthedocs.io/en/latest/quickstart.html)

Пример использования в боте
[https://mastergroosha.github.io/telegram-tutorial/docs/lesson_11/](https://mastergroosha.github.io/telegram-tutorial/docs/lesson_11/)
