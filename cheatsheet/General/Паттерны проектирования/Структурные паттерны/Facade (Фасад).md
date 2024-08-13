<h3>Facade (Фасад)</h3>
<p>Паттерн Фасад предоставляет унифицированный интерфейс к набору интерфейсов в подсистеме, упрощая использование сложных систем.</p>
<pre><code class="language-python">class CPU:
    def freeze(self):
        print(&quot;Freezing CPU&quot;)

    def jump(self, position):
        print(f&quot;Jumping to {position}&quot;)

    def execute(self):
        print(&quot;Executing instructions&quot;)

class Memory:
    def load(self, position, data):
        print(f&quot;Loading data from {position} to {data}&quot;)

class HardDrive:
    def read(self, lba, size):
        print(f&quot;Reading {size} bytes from LBA {lba}&quot;)
        return &quot;data&quot;

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

# Использование
computer = ComputerFacade()
computer.start()
</code></pre>