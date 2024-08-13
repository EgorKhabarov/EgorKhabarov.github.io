<h2>Adapter (Адаптер)</h2>
<p><strong>Описание:</strong> Преобразует интерфейс одного класса в интерфейс другого, который ожидает клиент.
Позволяет классам с несовместимыми интерфейсами работать вместе.</p>
<p><strong>Когда использовать:</strong> Когда необходимо использовать существующий класс, но его интерфейс не соответствует нужному.</p>
<p><strong>Пример реализации:</strong></p>
<pre><code class="language-python">class Adaptee:
    def specific_request(self):
        return &quot;specific request&quot;

class Target:
    def request(self):
        pass

class Adapter(Target):
    def __init__(self, adaptee):
        self._adaptee = adaptee

    def request(self):
        return f&quot;Adapter: {self._adaptee.specific_request()}&quot;

adaptee = Adaptee()
adapter = Adapter(adaptee)
print(adapter.request())  # Вывод: &quot;Adapter: specific request&quot;
</code></pre>