```python
# Variation selector ranges
VARIATION_SELECTOR_START = 0xFE00
VARIATION_SELECTOR_END = 0xFE0F
VARIATION_SELECTOR_SUPPLEMENT_START = 0xE0100
VARIATION_SELECTOR_SUPPLEMENT_END = 0xE01EF

def to_variation_selector(byte: int) -> str | None:
    """
    Turns a byte into a variation selector

    :param byte:
    :return:
    """
    if 0 <= byte < 16:
        return chr(VARIATION_SELECTOR_START + byte)
    elif 16 <= byte < 256:
        return chr(VARIATION_SELECTOR_SUPPLEMENT_START + byte - 16)
    return None

def from_variation_selector(code_point: int) -> int | None:
    """
    Receives a byte back from the selector

    :param code_point:
    :return:
    """
    if VARIATION_SELECTOR_START <= code_point <= VARIATION_SELECTOR_END:
        return code_point - VARIATION_SELECTOR_START
    elif VARIATION_SELECTOR_SUPPLEMENT_START <= code_point <= VARIATION_SELECTOR_SUPPLEMENT_END:
        return code_point - VARIATION_SELECTOR_SUPPLEMENT_START + 16
    return None

def encode(emoji: str, text: str) -> str:
    """
    Hides text in emoji by encoding it in selectors

    :param emoji:
    :param text:
    :return:
    """
    bytes_text = text.encode("utf-8")
    encoded = emoji + "".join(filter(None, (to_variation_selector(b) for b in bytes_text)))
    return encoded

def decode(text: str) -> str:
    """
    Extracts hidden text

    :param text:
    :return:
    """
    decoded_bytes = []
    for char in text:
        byte = from_variation_selector(ord(char))
        if byte is None and decoded_bytes:
            break
        elif byte is not None:
            decoded_bytes.append(byte)
    return bytes(decoded_bytes).decode("utf-8")
```
