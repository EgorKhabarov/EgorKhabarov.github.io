### Facade (Фасад)

Паттерн Фасад предоставляет унифицированный интерфейс к набору интерфейсов в подсистеме, упрощая использование сложных систем.

```python
class CPU:
    def freeze(self):
        print("Freezing CPU")

    def jump(self, position):
        print(f"Jumping to {position}")

    def execute(self):
        print("Executing instructions")


class Memory:
    def load(self, position, data):
        print(f"Loading data from {position} to {data}")


class HardDrive:
    def read(self, lba, size):
        print(f"Reading {size} bytes from LBA {lba}")
        return "data"


class ComputerFacade:
    def __init__(self):
        self.cpu = CPU()
        self.memory = Memory()
        self.hard_drive = HardDrive()

    def start(self):
        self.cpu.freeze()
        self.memory.load(0, self.hard_drive.read(1024, 4096))
        self.cpu.jump(0)
        self.cpu.execute()


computer = ComputerFacade()
computer.start()
# Freezing CPU
# Reading 4096 bytes from LBA 1024
# Loading data from 0 to data
# Jumping to 0
# Executing instructions
```
