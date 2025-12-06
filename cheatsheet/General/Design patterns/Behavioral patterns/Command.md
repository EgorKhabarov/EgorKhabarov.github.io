# Command

Команда

**Описание**: Инкапсулирует запрос как объект, позволяя параметризовать объекты с различными запросами, ставить запросы в очередь или делать их отменяемыми

**Когда использовать**: Когда нужно отделить вызов операции от объекта, который её выполняет, или когда требуется логировать, отменять и повторять операции

```python
class Command:
    def execute(self):
        pass

class Light:
    def turn_on(self):
        return "Light is on"

class LightOnCommand(Command):
    def __init__(self, light):
        self._light = light

    def execute(self):
        return self._light.turn_on()

class RemoteControl:
    def __init__(self, command):
        self._command = command

    def press_button(self):
        return self._command.execute()


light = Light()
command = LightOnCommand(light)
remote = RemoteControl(command)
print(remote.press_button())  # Light is on
```
