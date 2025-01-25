```python
import sqlite3
import csv

def SQL(query: str, params: tuple | dict = None, commit: bool = False, column_names: bool = False):
    """Выполняет SQL запрос"""
    with sqlite3.connect(r"database.sqlite") as connection:
        cursor = connection.cursor()
        cursor.execute(query, params)
        if commit: connection.commit()
        result = cursor.fetchall()
        if column_names and getattr(cursor, "description"):
            column_names_data = [column[0] for column in cursor.description] or None
            result = column_names_data + result
    return result

data = SQL("SELECT * FROM table_name;")

with open("data.csv", "w", newline="", encoding="UTF-8") as file:
    writer = csv.writer(file)
    writer.writerows(data)

with open("data.csv", "r", encoding="UTF-8") as file:
    reader = csv.reader(file)
    column_names = next(reader)
    SQL(
        f"""
CREATE TABLE table_name (
    {", ".join([f"{column} TEXT" for column in column_names])}
);
""",
        commit=True,
    )
    for row in reader:
        SQL(
            f"""
INSERT INTO table_name (
    {", ".join(column_names)}
)
VALUES (
    {", ".join([f'"{column}"' for column in row])}
)
""",
            commit=True,
        );
```
