**Unittest** встроенная библиотека Python для написания и выполнения тестов.
Она реализует функциональность для написания модульных тестов (unit tests),
которая позволяет автоматизировать проверку корректности работы кода.

## Основные компоненты и структура тестов в Unittest

### Основные классы и методы

| Класс/Метод            | Описание                                                                           | Пример использования                                     |
|------------------------|------------------------------------------------------------------------------------|----------------------------------------------------------|
| `unittest.TestCase`    | Базовый класс, от которого наследуются все классы с тестами                        | `class MyTests(unittest.TestCase): ...`                  |
| `setUp()`              | Метод, который запускается перед каждым тестом. Инициализирует окружение для теста | `def setUp(self): self.db = Database()`                  |
| `tearDown()`           | Метод, который запускается после каждого теста. Очищает ресурсы, если нужно        | `def tearDown(self): self.db.close()`                    |
| `assertEqual(a, b)`    | Проверяет, что `a` и `b` равны                                                     | `self.assertEqual(result, 10)`                           |
| `assertNotEqual(a, b)` | Проверяет, что `a` и `b` не равны                                                  | `self.assertNotEqual(result, 5)`                         |
| `assertTrue(x)`        | Проверяет, что условие `x` истинно (True)                                          | `self.assertTrue(condition)`                             |
| `assertFalse(x)`       | Проверяет, что условие `x` ложно (False)                                           | `self.assertFalse(is_valid)`                             |
| `assertIsNone(x)`      | Проверяет, что объект `x` равен `None`                                             | `self.assertIsNone(value)`                               |
| `assertIsNotNone(x)`   | Проверяет, что объект `x` не равен `None`                                          | `self.assertIsNotNone(result)`                           |
| `assertIn(a, b)`       | Проверяет, что объект `a` содержится в объекте `b`                                 | `self.assertIn(element, container)`                      |
| `assertNotIn(a, b)`    | Проверяет, что объект `a` не содержится в объекте `b`                              | `self.assertNotIn(item, list)`                           |
| `assertRaises`         | Проверяет, что вызываемая функция бросает указанное исключение                     | `with self.assertRaises(ValueError): func_that_raises()` |

### Пример тестового класса

```python
import unittest


class TestMathFunctions(unittest.TestCase):
    def setUp(self):
        self.a = 10
        self.b = 5

    def test_add(self):
        result = self.a + self.b
        self.assertEqual(result, 15)

    def test_subtract(self):
        result = self.a - self.b
        self.assertEqual(result, 5)

    def tearDown(self):
        # Здесь можно освободить ресурсы
        pass

if __name__ == "__main__":
    unittest.main()
```

### Запуск тестов

Через командную строку
```bash
python -m unittest test_module.py
```
Запуск всех тестов в файле
```bash
python -m unittest discover
```

### Организация тестов

Тесты обычно организуются в классы, наследуемые от `unittest.TestCase`
Каждый метод в классе, начинающийся с `test_`, будет считаться отдельным тестом

```python
import unittest


class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")

    def test_isupper(self):
        self.assertTrue("FOO".isupper())
        self.assertFalse("Foo".isupper())

    def test_split(self):
        s = "hello world"
        self.assertEqual(s.split(), ["hello", "world"])
        # Проверка исключения
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == "__main__":
    unittest.main()
```

### Скип тестов

Можно пропустить тест, если его выполнение в текущий момент не нужно, с помощью декоратора `@unittest.skip`

```python
import unittest

class TestSkipped(unittest.TestCase):
    @unittest.skip("Причина пропуска")
    def test_skipped(self):
        self.fail("Этот тест будет пропущен")

if __name__ == "__main__":
    unittest.main()
```

Также можно использовать другие формы скипа
`@unittest.skipIf(condition, "reason")`: Пропустить тест, если условие истинно
`@unittest.skipUnless(condition, "reason")`: Пропустить тест, если условие ложно

### Параметры командной строки

Запуск тестов можно модифицировать с помощью параметров командной строки
- `-v`: Запуск тестов с более подробным выводом (**verbose**)
- `-q`: Уменьшение подробности вывода (**quiet mode**)
- `-f`: Остановка на первом неудачном тесте

```bash
python -m unittest -v test_module
```

### Дополнительные возможности

- **Параметризация тестов**: С помощью библиотеки `unittest.TestLoader`, можно запускать тесты динамически

```python
suite = unittest.TestLoader().loadTestsFromTestCase(TestMathFunctions)
unittest.TextTestRunner().run(suite)
```

- **Mocking (имитация объектов)**: Python предоставляет отдельную библиотеку для моков - `unittest.mock`,
которая может быть полезна для тестирования внешних зависимостей, API, баз данных и других компонентов.

### Полезные библиотеки для улучшения тестирования
- **`unittest.mock`** - для создания мока (имитации объектов) в тестах.
- **`nose2`** - расширенная библиотека для тестирования с дополнительными возможностями.
- **`pytest`** - популярная библиотека для тестирования,
которая поддерживает `unittest`, но предлагает более гибкие возможности
