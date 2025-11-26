```python
from typing import Any  # Любой тип
```

```python
from typing import Literal  # Один из вариантов
direction: Literal["ASC", "DESC"] = "DESC"
```

```python
from typing import Union
val: Union[int, float] = 20.8  # or 20
```

```python
from typing import Final

val: Final = 2
val += 1  # Ошибки не произойдёт, но IDE подсветит как ошибку
```

# Использование статической проверки типов в Python
Интерпретатор Python по умолчанию не осуществляет проверку типов
Однако была создана версия интерпретатора Python – `mypy`, которая обеспечивает проверку типов на уровне интерпретатора

```python
from typing import NoReturn
# NoReturn сообщает что функция не завершается нормально
# Например она возбуждает исключение

def forever() -> NoReturn:
    while True:
        pass
```

Если это генераторная функция, то есть её тело содержит оператор `yield`, для возвращаемого можно воспользоваться аннотацией `Iterable[T]`, либо `Generator[YT, ST, RT]`:

```python
def generate_two() -> Iterable[int]:
    yield 1
    yield "2"  # Incompatible types in "yield" (actual type "str", expected type "int")
```

```python
from typing import Optional

amount: int
amount = None  # Incompatible types in assignment (expression has type "None", variable has type "int")

price: Optional[int]
price = None

# Аннотация Optional[T] эквивалентна Union[T, None], хотя такая запись и не рекомендуется
```

# Предварительное объявление

Обычно вы не можете использовать тип до того, как он создан. Например, следующий код даже не запустится:

```python
class LinkedList:
    data: Any
    next: LinkedList  # NameError: name 'LinkedList' is not defined
```

Чтобы это исправить, допустимо использовать строковый литарал. В этом случае аннотации будут вычислены отложенно

```python
class LinkedList:
    data: Any
    next: "LinkedList"
```

Так же вы можете обращаться к классам из других модулей (конечно, если модуль импортирован):

```python
some_variable: "somemodule.SomeClass"
```

или

```python
from __future__ import annotations

class LinkedList:
    data: int
    next: LinkedList
```

# Generic-типы

Иногда необходимо сохранить информацию о типе, при этом не фиксируя его жестко
Например, если вы пишете контейнер, который хранит однотипные данные
Или функцию, которая возвращает данные того же типа, что и один из аргументов

Такие типы как `List` или `Callable`, которые, мы видели раньше как раз используют механизм дженериков
Но кроме стандартных типов, вы можете создать свои дженерик-типы
Для этого надо, во-первых, завести `TypeVar` переменную, которая будет атрибутом дженерика, и, во-вторых,непосредственно объявить generic-тип:

```python
T = TypeVar("T")

class LinkedList(Generic[T]):
    data: T
    next: "LinkedList[T]"

    def __init__(self, data: T):
        self.data = data

head_int: LinkedList[int] = LinkedList(1)
head_int.next = LinkedList(2)
head_int.next = 2  # error: Incompatible types in assignment (expression has type "int", variable has type "LinkedList[int]")
head_int.data += 1
head_int.data.replace("0", "1")  # error: "int" has no attribute "replace"

head_str: LinkedList[str] = LinkedList("1")
head_str.data.replace("0", "1")

head_str = LinkedList[str](1)  # error: Argument 1 to "LinkedList" has incompatible type "int"; expected "str"
```

Как вы можете заметить, для generic-типов работает автоматический вывод типа параметра
Если требуется, дженерик может иметь любое количеством параметров: `Generic[T1, T2, T3]`
Также, при определении `TypeVar` вы можете ограничить допустимые типы:

```python
T2 = TypeVar("T2", int, float)

class SomethingNumeric(Generic[T2]):
    pass

x = SomethingNumeric[str]()  # error: Value of type variable "T2" of "SomethingNumeric" cannot be "str"
```

# Cast

Иногда анализатор статический анализатор не может корректно определить тип переменной, в этом случае можно использовать функцию `cast`
Её единственная задача - показать анализатору, что выражение имеет определённый тип

```python
from typing import List, cast

def find_first_str(a: List[object]) -> str:
    index = next(i for i, x in enumerate(a) if isinstance(x, str))
    return cast(str, a[index])
```

Также это может быть полезно для декораторов:

```python
MyCallable = TypeVar("MyCallable", bound=Callable)

def logged(func: MyCallable) -> MyCallable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(func.__name__, args, kwargs)
        return func(*args, **kwargs)

    return cast(MyCallable, wrapper)

@logged
def mysum(a: int, b: int) -> int:
    return a + b

mysum(a=1)  # error: Missing positional argument "b" in call to "mysum"
```
