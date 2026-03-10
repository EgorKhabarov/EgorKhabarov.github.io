# str

## Case

### capitalize
str.`capitalize`()
Переводит первую букву в верхний, а остальные в нижний регистр
```pycon
>>> "capitalize".capitalize()
"Capitalize"
```
### casefold
str.`casefold`()
Переводит все символы в нижний регистр
```pycon
>>> "CaSeFoLd".casefold()
"casefold"
```
### lower
str.`lower`()
Переводит символы строки в нижний регистр
```pycon
>>> "lOwEr".lower()
"lower"
```
### upper
str.`upper`()
Возвращает копию строки в верхнем регистре
```pycon
>>> "upper".upper()
"UPPER"
```
### swapcase
str.`swapcase`()
Меняет регистр всех символов на противоположный
```pycon
>>> "sWaPcAsE".swapcase()
"SwApCaSe"
```
### title
str.`title`()
Возвращает строку, где все слова начинаются с заглавной буквы, а продолжаются строчными
```pycon
>>> "title title".title()
"Title Title"
```

## Check case

### istitle
str.`istitle`()
`True`, если строка начинается с заглавной буквы, а остальные - строчные
```pycon
>>> "Aa".istitle()
True
>>> "aA".istitle()
False
>>> "Aa1 ".istitle()
True
```
### isupper
str.`isupper`()
`True`, если строка в верхнем регистре
```pycon
>>> "A".isupper()
True
>>> "a".isupper()
False
```
### islower
str.`islower`()
`True`, если вся строка в нижнем регистре
```pycon
>>> "a".islower()
True
"A".islower()
False
```

## Align

### center
str.`center`(width\[, fillvalue])
Обрамляет значениями `fillvalue` строку, пока длина не станет `width`
```pycon
>>> "0".center(5, "_")
"__0__"
```
### ljust
str.`ljust`(width, fillchar=" ")
Добавляет в конец строки символ `fillchar`, пока длина не станет `width`
```pycon
>>> "1".ljust(5, "_")
"1____"
```
### rjust
str.`rjust`(width, fillchar=" ")
Добавляет в начало строки символ `fillchar`, пока длина не станет `width`
```pycon
>>> "1".rjust(5, "_")
"____1"
```
### zfill
str.`zfill`(width)
Заполняет строку указанным числом нулей в начале
```pycon
>>> "1".zfill(5)
"00001"
```
### expandtabs
str.`expandtabs`(tabsize=8)
Увеличивает размер символов табуляции до `tabsize` пробелов
```pycon
>>> " ".expandtabs(8)
"        "
```

## Prefix suffix

### startswith
str.`startswith`(prefix\[, start\[, end]])
`True` если строка начинается с `prefix`
```pycon
>>> "1234".startswith("34")
False
>>> "1234".startswith("12")
True
>>> "1234".startswith(("12", "89"))
True
```
### endswith
str.`endswith`(suffix\[, start\[, end]])
`True` если строка заканчивается на `suffix`
```pycon
>>> "1234".endswith("12")
False
>>> "1234".endswith("34")
True
>>> "1234".endswith(("34", "56"))
True
```
### removeprefix
str.`removeprefix`(prefix: str)
Возвращает строку без прификса `prefix`
```pycon
>>> "123".removeprefix("1")
"23"
```
### removesuffix
str.`removesuffix`(suffix: str)
Возвращает строку без суффикса `suffix`
```pycon
>>> "123".removesuffix("3")
"12"
```

## Split

### split
str.`split`(sep=" ", maxsplit=-1)
Возвращает список подстрок, разделенных по `sep` до `maxsplit` раз
```pycon
>>> "1 3".split()
["1", "3"]
```
### rsplit
str.`rsplit`(sep=" ", maxsplit=-1)
Возвращает список подстрок, разделенных по sep до `maxsplit` раз (с конца)
```pycon
>>> "1 3".rsplit()
["1", "3"]
```
### splitlines
str.`splitlines`(keepends=False)
Разделяет строку по `\n`
Не удаляет разделители, если `keepends=True`
```pycon
>>> "1 3\n4".splitlines()
["1 3", "4"]
```
### maketrans + translate
str.`maketrans`(*args)
Возвращает таблицу перевода для `s.translate`

str.`translate`(table)
Заменяет все символы строки согласно таблице перевода 
```pycon
>>> table = str.maketrans({
...     "a": "1",
...     "b": "2",
...     "c": None  # Удалить символ
... })
>>> "abc cab".translate(table)
"12 12"
>>> table = str.maketrans("abc", "123")
>>> "abc".translate(table)
123
```
### partition
str.`partition`(sep)
Разделяет строку на три части по первому разделителю `sep`
\[начало, sep, конец]
```pycon
>>> "user:password".partition(":")
("user", ":", "password")
>>> "hello".partition(":")
("hello", "", "")
```
### rpartition
str.`rpartition`()
Разделяет строку на три части по последнему разделителю `sep`:
\[начало, sep, конец]
```pycon
>>> "/home/user/file.txt".rpartition("/")
("/home/user", "/", "file.txt")
```

## Edit

### format
str.`format`(args, *kwargs)
Последовательно заменяет `{}` в строке на свои аргументы
```pycon
>>> "{}".format("1")
"1"
>>> "{a}".format(a="1")
"1"
```
### format_map
str.`format_map`(dict)
Заменяет `{<val>}` в строке на `dict[<val>]`
```pycon
>>> "{x} {y}".format_map(
...     {"x": 4, "y": -5}
... )
"4 -5"
```
### strip
str.`strip`(\[chars])
Возвращает строку без пробельных символов или `chars` в начале и конце
```pycon
>>> "   1 3   ".strip()
"1 3"
```
### lstrip
str.`lstrip`(\[chars])
Возвращает строку без пробельных символов или `chars` в начале
```pycon
>>> "   1 3   ".lstrip()
"1 3    "
```
### rstrip
str.`rstrip`(\[chars])
Возвращает строку без пробельных символов или `chars` в конце
```pycon
>>> "   1 3   ".rstrip()
"   1 3"
```
### replace
str.`replace`(old, new)
Заменяет все подстроки `old` на `new`
```pycon
>>> "1231".replace("1", "_")
"_23_"
```

## Check content

### count
str.`count`(str\[, start]\[, end]
Считает количество подстрок `str` в выбранном промежутке строки
```pycon
>>> "12123412".count("12")
3
```
### index
str.`index`(str\[, start\[, end]])
Возвращает индекс начала первой подстроки `str` в выбранном промежутке или `ValueError`, если она не найдена
```pycon
>>> "1234".index("2")
1
```
### rindex
str.`rindex`(str\[, start\[, end]])
Возвращает индекс начала последней подстроки `str` в выбранном промежутке или `ValueError`, если она не найдена
```pycon
>>> "123427".rindex("2")
4
```
### find
str.`find`(str\[, start\[, end]])
Возвращает индекс начала первой подстроки `str` в выбранном промежутке или `-1`, если она не найдена
```pycon
>>> "1234".find("2")
1
```
### rfind
str.`rfind`(str\[, start\[, end]])
Возвращает индекс начала последней подстроки `str` в выбранном промежутке или `-1`, если она не найдена
```pycon
>>> "123427".rfind("2")
4
```
### isalnum
str.`isalnum`()
`True`, если строка состоит только из букв и цифр
```pycon
>>> "abc123".isalnum()
True
>>> "abc 123".isalnum()
False
>>> "abc!".isalnum()
False
```
### isalpha
str.`isalpha`()
`True`, если строка состоит только из букв
```pycon
>>> "hello".isalpha()
True
>>> "hello1".isalpha()
False
>>> "Привет".isalpha()
True
```
### isdecimal
str.`isdecimal`()
`True`, если строка состоит только из десятичных цифр
```pycon
>>> "123".isdecimal()
True
>>> "Ⅳ".isdecimal()
False
>>> "²".isdecimal()
False
```
### isnumeric
str.`isnumeric`()
`True`, если строка состоит только из цифр
```pycon
>>> "123".isnumeric()
True
>>> "Ⅳ".isnumeric()
True
>>> "²".isnumeric()
True
```
### isprintable
str.`isprintable`()
`True`, если все символы строки отображаются
Например `\n`, `\t`
```pycon
>>> "hello".isprintable()
True
>>> "hello\n".isprintable()
False
```
### isspace
str.`isspace`()
`True`, если строка состоит из пробелов
```pycon
>>> " \t".isspace()
True
>>> " a ".isspace()
False
```
### isascii
str.`isascii`()
Проверяет, состоит ли строка только из ASCII символов
```pycon
>>> # Состоит только из ASCII
>>> "Hello, World!".isascii()
True
>>> # Состоит не из ASCII
>>> "Привет, мир!".isascii()
False
>>> # Не содержит не-ASCII
>>> "".isascii()
True
```
### isdigit
str.`isdigit`()
Проверяет, состоит ли строка только из цифр (0-9)
```pycon
>>> "12345".isdigit()
True
>>> "abc123".isdigit()
False
>>> "123 456".isdigit()
False
>>> "123.45".isdigit()
False
>>> "+123".isdigit()
False
>>> "-123".isdigit()
False
```
### isidentifier
str.`isidentifier`()
Проверяет, можно ли использовать как имя переменной
```pycon
>>> "variable".isidentifier()
True
>>> "_name123".isidentifier()
True
>>> "123name".isidentifier()
False
>>> "my-var".isidentifier()
False
>>> "class".isidentifier()
True
```

## Other

### encode
str.`encode`(encoding, errors)
Меняет кодировку строки
```pycon
>>> "qwerty123".encode()
b"qwerty123"
```
### join
str.`join`(iter)
Склеивает элементы последовательности `iter` в одну строку с разделителем `str`
```pycon
>>> " ".join(("1", "2"))
"1 2"
```

## Magic

### + и \_\_add\_\_
`+` и str.`__add__`(other)
Конкатенация строк
```pycon
>>> s = "Hello "
>>> s + "world"
'Hello world'
>>> s.__add__("world")
'Hello world'
```
### * и \_\_mul\_\_ или \_\_rmul\_\_
`*` и str.`__mul__`(n)
str.`__rmul__`(n)
Повторяет строку n раз
```pycon
>>> s = "ab"
>>> s * 3
'ababab'
>>> s.__mul__(3)
'ababab'
>>> 3 * "ab"
'ababab'
>>> "ab".__rmul__(3)
'ababab'
```
### == или != и \_\_eq\_\_ или \_\_ne\_\_
`==` и str.`__eq__`(other)
`!=` и str.`__ne__`(other)
Проверяет равенство строк
```pycon
>>> "a" == "a"
True
>>> "a".__eq__("a")
True
>>> "a" != "b"
True
>>> "a".__ne__("b")
True
```
### < или > и \_\_lt\_\_ или \_\_gt\_\_
`<` и str.`__lt__`(other)
`>` и str.`__gt__`(other)
Лексикографическое сравнение
```pycon
>>> "apple" < "banana"
True
>>> "apple".__lt__("banana")
True
>>> "banana" > "apple"
True
>>> "banana".__gt__("apple")
True
```
### <= или >= и \_\_le\_\_ или \_\_ge\_\_
str.`__le__`(other)
str.`__ge__`(other)
```pycon
>>> "apple" <= "apple"
True
>>> "apple".__le__("apple")
True
>>> "banana" >= "apple"
True
>>> "banana".__ge__("apple")
True
```
### % и \_\_mod\_\_ или \_\_rmod\_\_
`%` и str.`__mod__`(value)
str.`__rmod__`(value)
Форматирование строк через `%`
```pycon
>>> "Hello %s" % "Bob"
'Hello Bob'
>>> "Hello %s".__mod__("Bob")
'Hello Bob'
>>> "%s %s" % ("hello", "world")
'hello world'
>>> "%s %s".__rmod__(("hello", "world"))
'hello world'
```
### \_\_format\_\_
str.`__format__`(spec)
Используется `format()` и f-строками
```pycon
>>> f"{'hi':>5}"
'   hi'
>>> format("hi", ">5")
'   hi'
>>> "hi".__format__(">5")
'   hi'
```

# Символы

| Символ   | Назначение                    | Пример              | Результат |
|:---------|:------------------------------|:--------------------|:----------|
| `\n`     | Перевод строки                | `"ab\ncd"`          | ab<br>cd  |
| `\`      | Экранирование                 | `"ab\ncd"`          | ab\ncd    |
| `\a`     | Звонок                        | `"a\aa"`            | a\[BEL]a  |
| `\b`     | Забой                         | `"ab\ba"`           | ac        |
| `\f`     | Перевод страницы              | `"a\fa"`            | a\[FF]a   |
| `\r`     | Возврат каретки               | `"ab\rcd"`          | cd        |
| `\t`     | Горизонтальная табуляция      | `"a\ta"`            | a a       |
| `\v`     | Вертикальная табуляция        | `"a\va"`            | a\[VT]a   |
| `\N{id}` | Символ Юникода по id          | `"\N{Degree Sign}"` | °         |
| `\uhhhh` | 16-ричный символ Юникода      | `"\u2030"`          | ‰         |
| `\Uhhhh` | 32-ичный символ Юникода       | `"\U00000394"`      | Δ         |
| `\xhh`   | 16-ричное значение символа    | `"\x2A"`            | *         |
| `\ooo`   | Восьмеричное значение символа | `"\275"`            | ½         |
| `\0`     | Символ Null                   | `"\0"`              |           |
| `\u00A0` | Символ неразнывного пробела   |                     |           |
