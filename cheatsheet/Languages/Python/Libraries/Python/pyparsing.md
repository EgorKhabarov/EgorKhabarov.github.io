Библиотека "pyparsing" используется для анализа и разбора текстовых данных в языке программирования Python
Она предоставляет возможность создавать грамматики и правила для разбора сложных структур данных

Методы модуля "pyparsing" и его подмодулей:

parseString(string) - Разбирает строку в соответствии с определенной грамматикой и возвращает структурированные данные
Word(alphas) - Определяет грамматическое правило для разбора последовательности символов, состоящей только из букв
nums - Подмодуль, содержащий грамматические правила для разбора числовых значений
CaselessLiteral(string) - Определяет грамматическое правило для разбора нечувствительных к регистру строк
QuotedString(quoteChar) - Определяет грамматическое правило для разбора строки, заключенной в кавычки

Самые часто используемые методы "pyparsing" с их кратким описанием и примером кода:

parseString(string): Разбирает строку в соответствии с грамматикой и возвращает структурированные данные

```python
from pyparsing import Word, alphas, nums

data = "Hello World"
print(Word(alphas).parseString(data))  # ["Hello"]
```

Word(alphas): Определяет грамматическое правило для разбора последовательности символов, состоящей только из букв

```python
from pyparsing import Word, alphas

data = "Hello123"
print(Word(alphas).parseString(data))  # ["Hello"]
```

QuotedString(quoteChar): Определяет грамматическое правило для разбора строки, заключенной в кавычки

```python
from pyparsing import QuotedString

data = '"Hello World"'
print(QuotedString('"').parseString(data))  # ["Hello World"]
```
