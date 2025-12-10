# Полезные ссылки

- [Wikipedia: Форма Бэкуса — Наура](https://ru.wikipedia.org/wiki/Форма_Бэкуса_—_Наура)
- [Wikipedia: BNF](https://en.wikipedia.org/wiki/Backus%E2%80%93Naur_form)
- [Wikipedia: EBNF](https://en.wikipedia.org/wiki/Extended_Backus%E2%80%93Naur_form)



# BNF
Backus-Naur Form
Форма Бэкуса — Наура

**BNF** - формальная нотация для описания синтаксиса языков программирования и других структур данных

<table>
<tbody>
<tr>
<td>Терминалы</td>
<td colspan="2">Конкретные символы (литералы), которые появляются в языке</td>
</tr>
<tr>
<td>Нетерминалы</td>
<td colspan="2">Абстрактные символы (метки), описывающие группы структур</td>
</tr>
<tr>
<td>Продукции</td>
<td colspan="2">Правила, задающие преобразование нетерминалов</td>
</tr>
<tr>
<td rowspan="3">Метасимволы</td>
<td><code>&lt;</code> и <code>&gt;</code></td>
<td>Для обозначения нетерминалов</td>
</tr>
<tr>
<td><code>::=</code></td>
<td>Оператор определения ("разворачивается в")</td>
</tr>
<tr>
<td><code>|</code></td>
<td>Альтернатива ("или")</td>
</tr>
</tbody>
</table>


# EBNF
Extended Backus-Naur Form

**EBNF** расширяет возможности [BNF](#BNF)

|                 |                                  |
|-----------------|----------------------------------|
| `{...}` или `*` | Любое количество раз (включая 0) |
| `[...]`         | 0 или 1 раз (опциональность)     | <!-- или `?`-->
| `+`             | 1 или более раз                  |
| `(...)`         | Для объединения элементов        |
| `"a" ... "z"`   | Диапазоны                        |

# Таблица символов
Стандарт [ISO/IEC 14977](https://www.cl.cam.ac.uk/~mgk25/iso-14977.pdf)

| Употребление                   | Нотация         | Альтернатива | Значение                |
|--------------------------------|-----------------|--------------|-------------------------|
| Определение                    | `=`             |              |                         |
| Конкатенация                   | `,`             |              |                         |
| Окончание                      | `;`             | `.`          |                         |
| Чередование                    | <code>\|</code> |              |                         |
| Необязательный                 | `[ ... ]`       | `(/ ... /)`  | Ни одного раза или один |
| Повторение                     | `{ ... }`       | `(: ... :)`  | Ни одного или более раз |
| Группировка                    | `( ... )`       |              |                         |
| Клеммная строка                | `" ... "`       | `' ... '`    |                         |
| Комментарий                    | `(* ... *)`     |              |                         |
| Специальная последовательность | `? ... ?`       |              |                         |
| Исключение                     | `-`             |              |                         |

|                 |                             |
|-----------------|-----------------------------|
| `*`             | repetition-symbol           |
| `-`             | except-symbol               |
| `,`             | concatenate-symbol          |
| <code>\|</code> | definition-separator-symbol |
| `=`             | defining-symbol             |
| `;`             | terminator-symbol           |
| `.`             | terminator-symbol           |

# BNF of BNF
```ebnf
<syntax>         ::= <rule> | <rule> <syntax>
<rule>           ::= <opt-whitespace> "<" <rule-name> ">" <opt-whitespace> "::=" <opt-whitespace> <expression> <line-end>
<opt-whitespace> ::= " " <opt-whitespace> | ""
<expression>     ::= <list> | <list> <opt-whitespace> "|" <opt-whitespace> <expression>
<line-end>       ::= <opt-whitespace> <EOL> | <line-end> <line-end>
<list>           ::= <term> | <term> <opt-whitespace> <list>
<term>           ::= <literal> | "<" <rule-name> ">"
<literal>        ::= '"' <text1> '"' | "'" <text2> "'"
<text1>          ::= "" | <character1> <text1>
<text2>          ::= "" | <character2> <text2>
<character>      ::= <letter> | <digit> | <symbol>
<letter>         ::= "A" | "B" | "C" | "D" | "E" | "F" | "G" | "H" | "I" | "J" | "K" | "L" | "M"
                   | "N" | "O" | "P" | "Q" | "R" | "S" | "T" | "U" | "V" | "W" | "X" | "Y" | "Z"
                   | "a" | "b" | "c" | "d" | "e" | "f" | "g" | "h" | "i" | "j" | "k" | "l" | "m"
                   | "n" | "o" | "p" | "q" | "r" | "s" | "t" | "u" | "v" | "w" | "x" | "y" | "z"
<digit>          ::= "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"
<symbol>         ::= "|" | " " | "!" | "#" | "$" | "%" | "&" | "(" | ")" | "*" | "+"
                   | "," | "-" | "." | "/" | ":" | ";" | ">" | "=" | "<" | "?" | "@"
                   | "[" | "\" | "]" | "^" | "_" | "`" | "{" | "}" | "~"
<character1>     ::= <character> | "'"
<character2>     ::= <character> | '"'
<rule-name>      ::= <letter> | <rule-name> <rule-char>
<rule-char>      ::= <letter> | <digit> | "-"
```

# EBNF of EBNF

```ebnf
letter = "A" | "B" | "C" | "D" | "E" | "F" | "G"
       | "H" | "I" | "J" | "K" | "L" | "M" | "N"
       | "O" | "P" | "Q" | "R" | "S" | "T" | "U"
       | "V" | "W" | "X" | "Y" | "Z" | "a" | "b"
       | "c" | "d" | "e" | "f" | "g" | "h" | "i"
       | "j" | "k" | "l" | "m" | "n" | "o" | "p"
       | "q" | "r" | "s" | "t" | "u" | "v" | "w"
       | "x" | "y" | "z";

digit = "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9";

symbol = "[" | "]" | "{" | "}" | "(" | ")" | "<" | ">"
       | "'" | '"' | "=" | "|" | "." | "," | ";" | "-"
       | "+" | "*" | "?" | "\n" | "\t" | "\r" | "\f" | "\b";

character = letter | digit | symbol | "_" | " ";
identifier = letter, {letter | digit | "_"};

S = {" " | "\n" | "\t" | "\r" | "\f" | "\b"};

terminal = "'", character - "'", {character - "'"}, "'"
         | '"', character - '"', {character - '"'}, '"';

terminator = ";" | ".";

term = "(", S, rhs, S, ")"
     | "[", S, rhs, S, "]"
     | "{", S, rhs, S, "}"
     | terminal
     | identifier;

factor = term, S, "?"
       | term, S, "*"
       | term, S, "+"
       | term, S, "-", S, term
       | term, S;

concatenation = (S, factor, S, ","?)+;
alternation = (S, concatenation, S, "|"?)+;

rhs = alternation;
lhs = identifier;

rule = lhs, S, "=", S, rhs, S, terminator;

grammar = (S, rule, S)*;
```

# Примеры

```ebnf
<expression> ::= <term> | <expression> "+" <term>
<term>       ::= <factor> | <term> "*" <factor>
<factor>     ::= <number> | "(" <expression> ")"
<number>     ::= <digit> | <number> <digit>
<digit>      ::= "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"
```

```ebnf
<expression> ::= <term> | <expression> "+" <term>
<term>       ::= <factor> { "*" <factor> }
<factor>     ::= <number> | "(" <expression> ")"
<number>     ::= <digit> { <digit> }
<digit>      ::= "0" ... "9"
```


Обычный приоритет переопределяется следующими парами квадратных скобок:

|      |                         |                         |      |
|:-----|:------------------------|------------------------:|-----:|
| `(*` | start-comment-symbol    |      end-comment-symbol | `*)` |
| `'`  | first-quote-symbol      |      first-quote-symbol |  `'` |
| `(`  | start-group-symbol      |        end-group-symbol |  `)` |
| `[`  | start-option-symbol     |       end-option-symbol |  `]` |
| `{`  | start-repeat-symbol     |       end-repeat-symbol |  `}` |
| `?`  | special-sequence-symbol | special-sequence-symbol |  `?` |
| `"`  | second-quote-symbol     |     second-quote-symbol |  `"` |
| `-`  | -symbol                 |                         |      |

```ebnf
aa = "A";                   (* A                             *)
bb = 3 * aa, "B";           (* AAAB                          *)
cc = 3 * [aa], "C";         (* C AC AAC AAAC                 *)
dd = {aa}, "D";             (* D AD AAD AAAD AAAAD etc…      *)
ee = aa, {aa}, "E";         (* AE AAE AAAE AAAAE AAAAAE etc… *)
ff = 3 * aa, 3 * [aa], "F"; (* AAAF AAAAF AAAAAF AAAAAAF     *)
gg = {3 * aa}, "G";         (* G AAAG AAAAAAG etc…           *)
hh = (aa | bb | cc), "H";   (* AH AAABH CH ACH AACH AAACH    *)
```


| Metalanguage symbol                        | Normal representation |
|--------------------------------------------|-----------------------|
| concatenate-symbol                         | `,`                   |
| defining-symbol                            | `=`                   |
| definition-separator-symbol                | <code>\|</code>       |
| except-symbol                              | `-`                   |
| first-quote-symbol                         | `´`                   |
| repetition-symbol                          | `*`                   |
| second-quote-symbol                        | `"`                   |
| special-sequence-symbol                    | `?`                   |
| start-comment-symbol<br>end-comment-symbol | `(*`<br>`*)`          |
| start-group-symbol<br>end-group-symbol     | `(`<br>`)`            |
| start-option-symbol<br>end-option-symbol   | `[`<br>`]`            |
| start-repeat-symbol<br>end-repeat-symbol   | `{`<br>`}`            |
| terminator-symbol                          | `;`                   |

# Полезные шаблоны

### Арифметические выражения
```ebnf
<expr>   ::= <term> | <expr> "+" <term> | <expr> "-" <term>
<term>   ::= <factor> | <term> "*" <factor> | <term> "/" <factor>
<factor> ::= <number> | "(" <expr> ")"
<number> ::= <digit> | <number> <digit>
<digit>  ::= "0" | "1" | ... | "9"
```

### JSON
```ebnf
<object>   ::= "{" <members> "}"
<members>  ::= <pair> | <pair> "," <members>
<pair>     ::= <string> ":" <value>
<array>    ::= "[" <elements> "]"
<elements> ::= <value> | <value> "," <elements>
<value>    ::= <string> | <number> | <object> | <array> | "true" | "false" | "null"
<string>   ::= "\"" { <char> } "\""
<number>   ::= <digit> { <digit> }
```

<!--
Первый символ в кавычках представляет собой апостроф в соответствии с определением ISO/IEC 646:1991,
то есть Юникодом U+0027 (); шрифт, используемый в ISO/IEC 14977:1996(E), делает его очень похожим на острый, Unicode U+00B4 (), поэтому иногда возникает путаница
Тем не менее, стандарт ISO Extended BNF ссылается на ISO/IEC 646:1991, «7-битный кодированный набор символов ISO для обмена информацией»
в качестве нормативного справочника и не упоминает какие-либо другие наборы символов, поэтому формально нет путаницы с символами Юникода за пределами 7-битного диапазона ASCII'´
-->
