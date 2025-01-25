```python
chr_digit = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


def number_to_string(number):
    if number == 0:
        return "0"
    sign = "-" if number < 0 else ""
    number = abs(number)
    digits = []
    while number > 0:
        digit = number % 10
        digits.append(chr_digit[digit])
        number //= 10
    digits.reverse()
    return sign + "".join(digits)


def string_to_number(string):
    if string == "0":
        return 0
    sign = 1
    if string[0] == "-":
        sign = -1
        string = string[1:]
    number = 0
    for char in string:
        digit = chr_digit.index(char)
        number = number * 10 + digit
    return sign * number
```
```pycon
>>> print(number_to_string(12345))
"12345"
>>> print(string_to_number("12345"))
12345
```
