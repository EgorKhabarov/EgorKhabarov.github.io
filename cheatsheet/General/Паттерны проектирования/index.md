# Паттерны проектирования

### Порождающие паттерны <img alt="C" src="General/Паттерны проектирования/C.png" height="17">

Порождающие паттерны проектирования фокусируются на процессах создания объектов.
Они помогают абстрагировать процесс инстанцирования, что может быть полезным,
когда конкретный процесс создания объекта должен быть отделён от его использования.
Это позволяет создавать объекты более гибко и предотвращает жесткую связь между кодом и конкретными классами объектов.


### Структурные паттерны <img alt="S" src="General/Паттерны проектирования/S.png" height="17">

Структурные паттерны проектирования фокусируются на том, как компоненты системы (например, классы и объекты)
могут быть объединены для создания более крупных и гибких структур.
Эти паттерны помогают определить отношения между компонентами и обеспечивают гибкость и масштабируемость систем.


### Поведенческие паттерны <img alt="B" src="General/Паттерны проектирования/B.png" height="17">

Поведенческие паттерны проектирования фокусируются на взаимодействии и распределении обязанностей между объектами и классами.
Они помогают определить, как объекты должны взаимодействовать друг с другом и как распределять ответственность между ними.


![patterns.png](General/Паттерны проектирования/patterns.png)

- [https://ru.wikipedia.org/wiki/Design_Patterns](https://ru.wikipedia.org/wiki/Design_Patterns)
    - [https://ru.wikipedia.org/wiki/Порождающие_шаблоны_проектирования](https://ru.wikipedia.org/wiki/Порождающие_шаблоны_проектирования)
    - [https://ru.wikipedia.org/wiki/Структурные_шаблоны_проектирования](https://ru.wikipedia.org/wiki/Структурные_шаблоны_проектирования)
    - [https://ru.wikipedia.org/wiki/Поведенческие_шаблоны_проектирования](https://ru.wikipedia.org/wiki/Поведенческие_шаблоны_проектирования)

# Промт

[Промт для паттернов проектирования](?Other/ChatGPT/Промты#chatgpt-promt)

# patterns_image_generator.py

<details><summary>patterns_image_generator.py</summary>

```python@patterns_image_generator.py
# pip install pillow
from PIL import Image, ImageDraw, ImageFont


color = {
    "orange": (254, 203, 158),
    "blue": (153, 205, 252),
    "green": (207, 252, 157),
}
pattern_color = {
    "C": color["blue"],
    "S": color["orange"],
    "B": color["green"],
}
pattern = {
    "C": [
        "Singleton (Одиночка)",
        "Factory (Фабрика)",
        "Abstract Factory (Абстрактная фабрика)",
        "Builder (Строитель)",
        "Prototype (Прототип)",
    ],
    "S": [
        "Adapter (Адаптер)",
        "Bridge (Мост)",
        "Composite (Компоновщик)",
        "Decorator (Декоратор)",
        "Facade (Фасад)",
        "Flyweight (Легковес)",
        "Proxy (Заместитель)",
    ],
    "B": [
        "Chain of Responsibility (Цепочка обязанностей)",
        "Command (Команда)",
        "Interpreter (Интерпретатор)",
        "Iterator (Итератор)",
        "Mediator (Посредник)",
        "Memento (Снимок)",
        "Observer (Наблюдатель)",
        "State (Состояние)",
        "Strategy (Стратегия)",
        "Template Method (Шаблонный метод)",
        "Visitor (Посетитель)",
    ],
}
indent = 16
border = 3
rectangle = (64, 45)
text_x_indent = indent * 0.4
text_y_indent = indent // 2
now_x = indent
now_y = indent
font = ImageFont.truetype("arial", 25)

image_x = indent + sum(
    rectangle[0] + indent*2 + font.getbbox(max(pattern_list, key=len))[2]
    for pattern_list in pattern.values()
)
image_y = indent + max(
    len(pattern_list) for pattern_list in pattern.values()
) * (rectangle[1] + indent)
image = Image.new("RGB", (image_x, image_y), "#FFFFFF")
draw = ImageDraw.Draw(image)


for pattern_type, pattern_list in pattern.items():
    for pattern in pattern_list:
        draw.rectangle(
            (now_x, now_y, now_x + rectangle[0], now_y + rectangle[1]),
            pattern_color[pattern_type],
            outline="#000000",
            width=border,
        )
        draw.text(
            (now_x + indent + text_x_indent, now_y + text_y_indent),
            pattern_type,
            fill="#000000",
            font=font,
        )
        draw.text(
            (now_x + rectangle[0] + indent, now_y + text_y_indent),
            pattern,
            fill="#000000",
            font=font,
        )
        draw.point((now_x, now_y), "#FF0000")
        now_y += rectangle[1] + indent

    now_y = indent
    now_x += rectangle[0] + indent * 2 + font.getbbox(max(pattern_list, key=len))[2]


image.save("patterns.png", format="PNG")
```

</details>
