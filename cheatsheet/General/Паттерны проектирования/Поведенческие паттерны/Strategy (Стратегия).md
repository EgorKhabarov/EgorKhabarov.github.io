<h2>Strategy (Стратегия)</h2>
<p><strong>Описание:</strong> Определяет семейство алгоритмов, инкапсулирует каждый из них и делает их взаимозаменяемыми.
Позволяет изменять алгоритм независимо от клиентов, которые им пользуются.</p>
<p><strong>Когда использовать:</strong> Когда у вас есть несколько схожих алгоритмов,
и необходимо переключаться между ними в зависимости от условий.</p>
<p><strong>Пример реализации:</strong></p>
<pre><code class="language-python">class Strategy:
    def execute(self, data):
        raise NotImplementedError

class ConcreteStrategyA(Strategy):
    def execute(self, data):
        return sorted(data)

class ConcreteStrategyB(Strategy):
    def execute(self, data):
        return sorted(data, reverse=True)

class Context:
    def __init__(self, strategy: Strategy):
        self._strategy = strategy

    def do_some_business_logic(self, data):
        return self._strategy.execute(data)

context = Context(ConcreteStrategyA())
print(context.do_some_business_logic([3, 1, 2]))  # Вывод: [1, 2, 3]

context = Context(ConcreteStrategyB())
print(context.do_some_business_logic([3, 1, 2]))  # Вывод: [3, 2, 1]
</code></pre>