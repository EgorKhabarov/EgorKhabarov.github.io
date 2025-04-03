```python
def tg_color(chat_id: int):
    """
    0x6FB9F0 Синий
    0xFFD67E Оранжевый
    0xCB86DB Фиолетовый
    0x8EEE98 Зелёный
    0xFF93B2 Розовый
    0xFB6F5F Красный
    """
    return {0: "К", 1: "О", 2: "Ф", 3: "З", 4: "Г", 5: "С", 6: "Р"}[abs(chat_id) % 7]
```
