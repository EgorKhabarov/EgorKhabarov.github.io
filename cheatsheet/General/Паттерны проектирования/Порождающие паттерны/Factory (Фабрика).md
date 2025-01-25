## Factory (Фабрика)

**Описание:** Предоставляет интерфейс для создания объектов в суперклассе,
но позволяет подклассам изменять тип создаваемых объектов.

**Когда использовать:** Когда нужно делегировать создание объектов подклассам
или когда тип создаваемых объектов заранее неизвестен.

```python
class Car:
    def drive(self):
        raise NotImplementedError


class ElectricCar(Car):
    def drive(self):
        return "Driving an electric car"


class PetrolCar(Car):
    def drive(self):
        return "Driving a petrol car"


class CarFactory:
    @staticmethod
    def create_car(car_type):
        if car_type == "electric":
            return ElectricCar()
        elif car_type == "petrol":
            return PetrolCar()
        else:
            raise ValueError("Unknown car type")
```
