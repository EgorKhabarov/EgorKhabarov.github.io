# Создание триггеров в SQLite

**Триггер** - это объект базы данных, который автоматически выполняется
при наступлении определённого события (`INSERT`, `UPDATE`, `DELETE`) на заданной таблице
В SQLite триггеры поддерживают различные сценарии, включая до/после событий и проверку условий

# Общий синтаксис
```sql
CREATE TRIGGER trigger_name
[BEFORE | AFTER | INSTEAD OF] [INSERT | DELETE | UPDATE [OF column_name]]
ON table_name
[FOR EACH ROW]
[WHEN condition]
BEGIN
    -- SQL-запросы, которые выполняются в триггере
END;
```

# Типы триггеров
1. `BEFORE` Выполняется перед событием (можно отменить операцию, вызвав ошибку)
2. `AFTER` Выполняется после события (например, для логирования)
3. `INSTEAD OF` Заменяет выполнение события (обычно для представлений)

# Ключевые аспекты

- `FOR EACH ROW`
Указывает, что триггер должен выполняться для каждой строки, затронутой операцией
- `WHEN condition`
Добавляет условие для выполнения триггера. Если условие `FALSE`, триггер не выполняется
- Псевдотаблицы
    - `NEW`: содержит новые значения (доступно для `INSERT` и `UPDATE`)
    - `OLD`: содержит старые значения (доступно для `DELETE` и `UPDATE`)

# Примеры использования

### Логирование вставок
Логируем время и значение, вставленное в `main_table`
```sql
CREATE TABLE log_table (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    operation_time TEXT,
    new_value TEXT
);

CREATE TRIGGER log_insert_trigger
AFTER INSERT ON main_table
FOR EACH ROW
BEGIN
    INSERT INTO log_table (operation_time, new_value)
    VALUES (datetime('now'), NEW.column_name);
END;
```

### Проверка данных перед вставкой
Если возраст меньше 18, вставка данных будет отменена
```sql
CREATE TRIGGER validate_insert
BEFORE INSERT ON users
FOR EACH ROW
WHEN NEW.age < 18
BEGIN
    SELECT RAISE(FAIL, 'Age must be 18 or above');
END;
```

### Ограничение изменения определённого столбца
Запрещаем изменение столбца `salary`
```sql
CREATE TRIGGER prevent_salary_update
BEFORE UPDATE OF salary ON employees
FOR EACH ROW
BEGIN
    SELECT RAISE(FAIL, 'Salary cannot be updated');
END;
```

### Каскадное удаление
При удалении строки из `parent_table` автоматически удаляются связанные строки в `child_table`
```sql
CREATE TRIGGER cascade_delete
AFTER DELETE ON parent_table
FOR EACH ROW
BEGIN
    DELETE FROM child_table WHERE parent_id = OLD.id;
END;
```

### Логирование обновлений
Логируется изменение значения столбца `column_name` в таблице `main_table`
```sql
CREATE TABLE update_log (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    old_value TEXT,
    new_value TEXT,
    updated_at TEXT
);

CREATE TRIGGER log_update
AFTER UPDATE OF column_name ON main_table
FOR EACH ROW
BEGIN
    INSERT INTO update_log (old_value, new_value, updated_at)
    VALUES (OLD.column_name, NEW.column_name, datetime('now'));
END;
```

### Триггер для представления
Добавляем возможность вставлять данные в представление, что напрямую не поддерживается SQLite
```sql
CREATE VIEW view_name AS
SELECT id, name FROM main_table;

CREATE TRIGGER view_insert
INSTEAD OF INSERT ON view_name
FOR EACH ROW
BEGIN
    INSERT INTO main_table (id, name)
    VALUES (NEW.id, NEW.name);
END;
```

# Удаление триггеров
```sql
DROP TRIGGER IF EXISTS trigger_name;
```

# Особенности SQLite
- Многострочные операции:
Триггеры в SQLite работают для каждой строки (`FOR EACH ROW`),
но не поддерживают уровень операций (`FOR EACH STATEMENT`)
- Отсутствие вложенных триггеров:
Если внутри триггера выполняется операция, которая вызывает другой триггер,
SQLite запретит выполнение вложенных триггеров по умолчанию
- Оптимизация условий:
Использование `WHEN` позволяет избежать выполнения ненужных операций

# Советы и best practices
1. Минимизируйте логику триггеров:
Избегайте сложных операций, чтобы не замедлять вставки/обновления
2. Тестируйте:
Убедитесь, что триггеры работают как ожидается, особенно при граничных условиях
3. Документируйте:
Пишите комментарии для сложных триггеров, чтобы другие разработчики могли быстро понять логику
4. Логируйте изменения:
Логи полезны для отладки и анализа истории изменений данных

### Проверка существующих триггеров
Для просмотра списка триггеров в базе данных
```sql
SELECT name FROM sqlite_master WHERE type = 'trigger';
```

Для получения SQL-кода триггера
```sql
SELECT sql FROM sqlite_master WHERE type = 'trigger' AND name = 'trigger_name';
```


---
---
---
---
---
---





# Расширенные сценарии работы с триггерами

## Использование нескольких условий в триггерах
Иногда требуется более сложная логика проверки
Это можно реализовать в блоке `WHEN` или с помощью нескольких запросов в теле триггера

### Логирование только при определённом диапазоне значений
Логируется только повышение зарплаты выше 100,000
```sql
CREATE TRIGGER log_high_salary
AFTER UPDATE OF salary ON employees
FOR EACH ROW
WHEN NEW.salary > 100000 AND OLD.salary <= 100000
BEGIN
    INSERT INTO salary_log (employee_id, old_salary, new_salary, updated_at)
    VALUES (NEW.id, OLD.salary, NEW.salary, datetime('now'));
END;
```

## Триггеры на основе вычисляемых значений
В триггере можно использовать функции и вычисления для обработки данных

### Обновление среднего значения в агрегатной таблице
При добавлении нового результата обновляется средний балл студента
```sql
CREATE TABLE scores (
    id INTEGER PRIMARY KEY,
    student_id INTEGER,
    score INTEGER
);

CREATE TABLE average_scores (
    student_id INTEGER PRIMARY KEY,
    average_score REAL
);

CREATE TRIGGER update_average
AFTER INSERT ON scores
FOR EACH ROW
BEGIN
    INSERT INTO average_scores (student_id, average_score)
    VALUES (
        NEW.student_id,
        (SELECT AVG(score) FROM scores WHERE student_id = NEW.student_id)
    )
    ON CONFLICT(student_id)
    DO UPDATE SET average_score =
        (SELECT AVG(score) FROM scores WHERE student_id = NEW.student_id);
END;
```

## Логика для ограничений на уровне таблицы
Иногда триггеры могут использоваться как заменитель ограничений (`CHECK`), которые требуют сложных условий

### Ограничение на количество строк в таблице
Таблица `user_logs` ограничивается 1000 строками. Если попытаться вставить новую строку, она вызовет ошибку
```sql
CREATE TRIGGER limit_rows
BEFORE INSERT ON user_logs
WHEN (SELECT COUNT(*) FROM user_logs) >= 1000
BEGIN
    SELECT RAISE(FAIL, 'Log table cannot exceed 1000 rows');
END;
```

## Каскадное обновление связанных таблиц
Можно автоматически обновлять данные в связанных таблицах при изменении основной таблицы

### Обновление связанного имени
При изменении имени сотрудника в таблице `employees` автоматически обновляется его имя в таблице `projects`
```sql
CREATE TRIGGER cascade_name_update
AFTER UPDATE OF name ON employees
FOR EACH ROW
BEGIN
    UPDATE projects SET manager_name = NEW.name WHERE manager_id = OLD.id;
END;
```

## Автоматическая генерация уникальных значений
Триггеры могут использоваться для генерации уникальных идентификаторов или значений

### Генерация кода для новой записи
При вставке новой записи автоматически генерируется уникальный код на основе максимального ID
```sql
CREATE TABLE orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_code TEXT UNIQUE,
    created_at TEXT
);

CREATE TRIGGER generate_order_code
BEFORE INSERT ON orders
FOR EACH ROW
BEGIN
    SET NEW.order_code = 'ORD-' || (SELECT MAX(id) + 1 FROM orders);
END;
```

## Работа с INSTEAD OF триггерами

> [!NOTE]
> `INSTEAD OF` используется для представлений или случаев, когда стандартное поведение требуется переопределить

### Вставка в представление
Добавляем возможность вставки в представление `employee_projects`
```sql
CREATE VIEW employee_projects AS
SELECT e.id AS employee_id, e.name AS employee_name, p.name AS project_name
FROM employees e
JOIN projects p ON e.id = p.manager_id;

CREATE TRIGGER insert_into_view
INSTEAD OF INSERT ON employee_projects
FOR EACH ROW
BEGIN
    INSERT INTO employees (id, name) VALUES (NEW.employee_id, NEW.employee_name);
    INSERT INTO projects (manager_id, name) VALUES (NEW.employee_id, NEW.project_name);
END;
```

## Отладка триггеров

### Просмотр SQL-кода триггера
```sql
SELECT name, sql FROM sqlite_master WHERE type = 'trigger' AND name = 'trigger_name';
```

### Временное отключение триггеров
SQLite не поддерживает явное отключение триггеров, но можно временно удалить их
```sql
DROP TRIGGER IF EXISTS trigger_name;
```

### Тестирование триггеров
Используйте транзакции для проверки
```sql
BEGIN TRANSACTION;
-- Выполняем тестовые операции
ROLLBACK;
```

### Логирование
Добавьте дополнительную таблицу для логирования операций триггера
```sql
CREATE TABLE trigger_logs (
  trigger_name TEXT,
  action_time TEXT,
  details TEXT
);

CREATE TRIGGER log_test_trigger
AFTER INSERT ON some_table
FOR EACH ROW
BEGIN
  INSERT INTO trigger_logs (trigger_name, action_time, details)
  VALUES ('log_test_trigger', datetime('now'), 'Inserted row into some_table');
END;
```

## Советы и рекомендации

1. Ограничивайте сложность триггеров:
Если бизнес-логика слишком сложна, лучше переместить её на уровень приложения
2. Избегайте циклических триггеров:
Убедитесь, что триггеры не вызывают друг друга, иначе это приведёт к ошибке
3. Используйте `WHEN` для оптимизации:
Проверяйте условие выполнения триггера, чтобы избежать ненужных операций
4. Минимизируйте побочные эффекты:
Триггеры не должны изменять состояние, о котором не известно вызывающему процессу
5. Регулярно тестируйте:
Проверяйте работу триггеров после изменения структуры базы данных
