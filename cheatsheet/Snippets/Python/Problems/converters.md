```python
def sqrt(x, p: int = 2):
    return pow(x, (1 / p))
```
```python
def rgb_to_hex(r: int, g: int, b: int) -> str:
    return "#{:02x}{:02x}{:02x}".format(r, g, b).upper()

def hex_to_rgb(h: str) -> tuple[int, int, int]:
    return tuple(int(h.lstrip("#")[i:i + 2], 16) for i in (0, 2, 4))
```
```pycon
>>> rgb_to_hex(164, 73, 211)
"#A449D3"
>>> hex_to_rgb("#A449D3")
(164, 73, 211)
```
```python
def html_escape(text):
    return "".join(f"&#{ord(char)};" for char in text)
```
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
```python
def unicode(text):
    return "".join(fr"\U{ord(char):0>8x}" for char in text)
```
