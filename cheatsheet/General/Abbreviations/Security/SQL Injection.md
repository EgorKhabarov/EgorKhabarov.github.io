# SQL Injection
SQL-инъекции
### Суть атаки
Злоумышленник внедряет SQL-код в запрос, изменяя его выполнение
### Пример уязвимости
```python
cursor.execute(f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'")
```
Если `username = ' OR 1=1 --`, то запрос всегда выполнится
### Защита от SQL-инъекций
- **Использование подготовленных запросов (prepared statements)**
- **Ограничение прав доступа к БД**
- **Использование ORM (например, SQLAlchemy)**
