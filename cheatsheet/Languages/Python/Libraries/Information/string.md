|                   |                                                                                       |
|-------------------|---------------------------------------------------------------------------------------|
| `ascii_letters`   | Содержит все буквы алфавита в верхнем и нижнем регистрах                              |
| `ascii_lowercase` | Содержит все буквы алфавита в нижнем регистре                                         |
| `ascii_uppercase` | Содержит все буквы алфавита в верхнем регистре                                        |
| `capwords`        |                                                                                       |
| `digits`          | Содержит все цифры от 0 до 9                                                          |
| `hexdigits`       | Содержит все шестнадцатеричные цифры (от 0 до 9 и от A до F)                          |
| `octdigits`       | Содержит все восьмеричные цифры (от 0 до 7)                                           |
| `printable`       | Содержит все печатные символы (буквы, цифры, символы пунктуации и пробельные символы) |
| `punctuation`     | Содержит символы пунктуации                                                           |
| `whitespace`      | Содержит пробельные символы (пробел, табуляция, новая строка и т.д.)                  |
| `Formatter`       |                                                                                       |
| `Template`        | A string class for supporting $-substitutions                                         |


```pycon
>>> string.ascii_lowercase
"abcdefghijklmnopqrstuvwxyz"
>>> string.ascii_uppercase
"ABCDEFGHIJKLMNOPQRSTUVWXYZ"
>>> string.ascii_letters  # ascii_lowercase + ascii_uppercase
"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
>>> string.capwords("text text text")
"Text Text Text"
>>> string.digits
"0123456789"
>>> string.hexdigits
digits + "abcdef" + "ABCDEF"
>>> string.octdigits
"01234567"
>>> string.printable  # digits + ascii_letters + punctuation + whitespace
"0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c"
>>> string.punctuation
"!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
>>> string.whitespace  # " \t\n\r\v\f"
" \t\n\r\x0b\x0c"
>>> string.Formatter
<class 'string.Formatter'>
>>> string.Template
<class 'string.Template'>
```
