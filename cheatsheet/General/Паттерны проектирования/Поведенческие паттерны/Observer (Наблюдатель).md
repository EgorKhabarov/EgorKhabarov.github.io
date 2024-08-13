<h2>Observer (Наблюдатель)</h2>
<p><strong>Описание:</strong> Определяет зависимость <strong>один-ко-многим</strong> между объектами таким образом,
что при <strong>изменении состояния одного объекта все зависимые объекты уведомляются и обновляются автоматически</strong>.</p>
<p><strong>Когда использовать:</strong> Когда изменение состояния одного объекта должно привести к изменению состояния других объектов,
например, в системах событий или уведомлений.</p>
<p><strong>Пример реализации:</strong></p>
<pre><code class="language-python">class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update()

class ConcreteObserver:
    def update(self):
        print(&quot;Observer updated&quot;)

subject = Subject()
observer = ConcreteObserver()
subject.attach(observer)
subject.notify()  # Вывод: &quot;Observer updated&quot;
</code></pre>