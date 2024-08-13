<h2>Factory (Фабрика)</h2>
<p><strong>Описание:</strong> Предоставляет интерфейс для создания объектов в суперклассе,
но позволяет подклассам изменять тип создаваемых объектов.</p>
<p><strong>Когда использовать:</strong> Когда нужно делегировать создание объектов подклассам
или когда тип создаваемых объектов заранее неизвестен.</p>
<p><strong>Пример реализации:</strong></p>
<pre><code class="language-python">class Car:
    def drive(self):
        raise NotImplementedError

class ElectricCar(Car):
    def drive(self):
        return &quot;Driving an electric car&quot;

class PetrolCar(Car):
    def drive(self):
        return &quot;Driving a petrol car&quot;

class CarFactory:
    @staticmethod
    def create_car(car_type):
        if car_type == &quot;electric&quot;:
            return ElectricCar()
        elif car_type == &quot;petrol&quot;:
            return PetrolCar()
        else:
            raise ValueError(&quot;Unknown car type&quot;)
</code></pre>