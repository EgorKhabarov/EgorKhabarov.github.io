## Singleton (Одиночка)

**Описание:** Гарантирует, что у класса есть только **один экземпляр**,
и предоставляет глобальную точку доступа к этому экземпляру.

**Когда использовать:** Когда нужно ограничить создание объекта одним экземпляром,
например, для логгера, подключения к базе данных, конфигурационного объекта.

```python
class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance


singleton1 = Singleton()
singleton2 = Singleton()
print(singleton1 is singleton2)  # True
```
