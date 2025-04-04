```python
def make_transliterate(text: str) -> str:
    symbols = (
        "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ",
        "abvgdeejzijklmnoprstufhzcss_y_euaABVGDEEJZIJKLMNOPRSTUFHZCSS_Y_EUA",
    )
    tr = {ord(a): ord(b) for a, b in zip(*symbols)}
    return text.translate(tr)
```

```python
def from_ghbdtn(text: str) -> str:
    en = """qwertyuiop[]asdfghjkl;'zxcvbnm,./`QWERTYUIOP{}ASDFGHJKL:"ZXCVBNM<>?~&$@#^"""
    ru = """йцукенгшщзхъфывапролджэячсмитьбю.ёЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ,Ё?;\"№:"""

    table = str.maketrans(dict(zip(en, ru)))
    return text.translate(table)
```
