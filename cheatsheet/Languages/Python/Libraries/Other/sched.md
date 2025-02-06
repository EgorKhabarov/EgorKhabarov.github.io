Библиотека "sched" в Python используется для планирования и управления задачами в программе.
Она позволяет создавать расписания выполнения задач и контролировать их выполнение в определенные моменты времени.

Методы модуля "sched" и его подмодулей:

|                                                    |                                                                                                           |
|----------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| `sched.timefunc`                                   | Устанавливает функцию, которая будет использоваться для получения времени                                 |
| `sched.delayfunc`                                  | Устанавливает функцию, вызываемую перед каждым циклом планировщика                                        |
| `sched.enter(delay, priority, action, argument)`   | Планирует выполнение задачи с заданным задержкой, приоритетом, действием и аргументом                     |
| `sched.enterabs(time, priority, action, argument)` | Планирует выполнение задачи в определенный момент времени с указанным приоритетом, действием и аргументом |
| `sched.cancel(event)`                              | Отменяет выполнение задачи, связанной с указанным событием                                                |
| `sched.run()`                                      | Запускает планировщик и начинает выполнение задач                                                         |

Самые часто используемые методы библиотеки "sched" и их краткие описания:
`enter(delay, priority, action, argument)`: Планирует выполнение задачи с заданной задержкой и приоритетом.

```python
import sched
import time

def print_message():
    print("Scheduled task executed.")

scheduler = sched.scheduler(time.time, time.sleep)
scheduler.enter(5, 1, print_message, ())
scheduler.run()
```

`enterabs(time, priority, action, argument)`: Планирует выполнение задачи в определенный момент времени с указанным приоритетом.

```python
import sched
import time

def print_message():
    print("Scheduled task executed.")

scheduler = sched.scheduler(time.time, time.sleep)
scheduler.enterabs(time.time() + 10, 1, print_message, ())
scheduler.run()
```

`cancel(event)`: Отменяет выполнение задачи, связанной с указанным событием.

```python
import sched
import time

def print_message():
    print("Scheduled task executed.")

scheduler = sched.scheduler(time.time, time.sleep)
event = scheduler.enter(5, 1, print_message, ())
scheduler.cancel(event)
scheduler.run()
```
