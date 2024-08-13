<h2>Singleton (Одиночка)</h2>
<p><strong>Описание:</strong> Гарантирует, что у класса есть только <strong>один экземпляр</strong>,
и предоставляет глобальную точку доступа к этому экземпляру.</p>
<p><strong>Когда использовать:</strong> Когда нужно ограничить создание объекта одним экземпляром,
например, для логгера, подключения к базе данных, конфигурационного объекта.</p>
<p><strong>Пример реализации:</strong></p>
<pre><code class="language-python">class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance


singleton1 = Singleton()
singleton2 = Singleton()
print(singleton1 is singleton2)  # True
</code></pre>