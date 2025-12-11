# MARKUP_EXAMPLES

**Below is the debug section for viewing the correctness of the markup**

# Headers

# `#` 1
## `##` 2
### `###` 3
#### `####` 4
##### `#####` 5
###### `######` 6

---

# Highlighting

\*Italic\* - *Italic*
\_Italic\_ - _Italic_

\*\*Bold\*\* - **Bold**
\_\_Bold\_\_ - __Bold__

\*\*\*Bold & Italic\*\*\* - ***Bold & Italic***
\_\_\_Bold & Italic\_\_\_ - ___Bold & Italic___
\*\*\_Bold & Italic\_\*\* - **_Bold & Italic_**
\_\*\*Bold & Italic\*\*\_ - _**Bold & Italic**_

\`text\` - `text`

\|\|text\|\| - ||text||

&#x7e;&#x7e;text&#x7e;&#x7e; - ~~text~~

&#x3d;&#x3d;mark&#x3d;&#x3d; - ==mark==

&#x3d;&#x3d;{color:red;background-color:inherit;}mark&#x3d;&#x3d; - =={color:red;background-color:inherit;}mark==

`---` or `<hr>`

---

---

# Table

<div class="container-row">

```pre
code
```
&nbsp;
````pre
```pre
code
```
````
&nbsp;
`````pre
````pre
```pre
code
```
````
`````
&nbsp;
```pre @file.txt
downloadable code
```

</div>

```table
| c1 | c2 |
|----|----|
| v1 | v2 |
| v3 | v4 |
```

| c1 | c2 |
|----|----|
| v1 | v2 |
| v3 | v4 |

```table
|    |    |
|----|----|
| v1 | v2 |
| v3 | v4 |
```

|    |    |
|----|----|
| v1 | v2 |
| v3 | v4 |

# Blockquote

blockquote 1

> blockquote 1

blockquote 2

>> blockquote 2

blockquote 3

> blockquote 1
>> blockquote 2
>>> blockquote 3

blockquote list

> text
>- 1
>- 2
>- 3
>text
>> text
>>> text
>> text
> text

## Alerts

```markdown
> [!NOTE]
> Useful information that users should know, even when skimming content

> [!TIP]
> Helpful advice for doing things better or more easily

> [!IMPORTANT]
> Key information users need to know to achieve their goal

> [!WARNING]
> Urgent info that needs immediate user attention to avoid problems

> [!CAUTION]
> Advises about risks or negative outcomes of certain actions
```

Read more [here](?Other/GitHub/Markdown) and [here](https://docs.github.com/ru/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)

blockquote NOTE

> [!NOTE]
> Useful information that users should know, even when skimming content

blockquote TIP

> [!TIP]
> Helpful advice for doing things better or more easily

blockquote IMPORTANT

> [!IMPORTANT]
> Key information users need to know to achieve their goal

blockquote WARNING

> [!WARNING]
> Urgent info that needs immediate user attention to avoid problems

blockquote CAUTION

> [!CAUTION]
> Advises about risks or negative outcomes of certain actions

blockquote WARNING

> [!WARNING]
> Urgent info that needs immediate user attention to avoid problems
>> 123
>>> qweret
> r
> 1234tv

blockquote list

> [!TIP]
> text
> - 1
> - 2
> - 3
> text
>> text
>>> text
>> text
> text

# Lists

```markdown
- list elem1
- list elem2
- list elem3
```

- list elem1
- list elem2
- list elem3

### Checkboxes

```markdown
- [ ] disables
- [X] enabled
```

- [ ] disables
- [X] enabled

# Code highlightings

```python
# comment

text = lambda x=1, y=2, z=3: x

@decorator(2, x=1)
def foo(x, y=2, z=3, a=lambda i=1, j=2, k=3: k):
    pass

class Baz(Foo):
    def __init__(self, qwert):
        """
        text
        """
        self.qq = qwert
        print("text")
        print(f"{123} \\n {"qwe":_} {33!r} {4:4<_} {2.34134:.2f}")
        print(b"123q\\n\\rwe")
        print(r"123\\n\\nqwe")
        print(f"""
text
{"text"}
text
""")

    @staticmethod
    def zoo(): pass

    @classmethod
    def zoo2(cls): pass

    @classmethod
    def zoo3(woefh): pass

foo(
    x=1234,
    y=(lambda x=2, t=lambda d=2, h=1: d, y=2: 5)(x=4, y=lambda c=2: c)
)
```

---

# SVG

<table><thead><tr><th style="text-align: center;">Icon</th><th style="text-align: left;">Description</th></tr></thead><tbody>

<tr><td style="text-align: center;" class="unselectable">
<svg viewBox="0 0 24 24" width="20" height="20" style="color: var(--color-file-yellow);"><use href="#icon_folder"></use></svg>
<svg viewBox="0 0 24 24" width="20" height="20" style="color: var(--color-file-yellow);"><use href="#icon_file"></use></svg>
</td><td style="text-align: left;">Обычная папка</td></tr>

<tr><td style="text-align: center;" class="unselectable">
<svg viewBox="0 0 24 24" width="20" height="20" style="color: var(--color-file-white);"><use href="#icon_folder"></use></svg>
<svg viewBox="0 0 24 24" width="20" height="20" style="color: var(--color-file-white);"><use href="#icon_file"></use></svg>
</td><td style="text-align: left;">Обычная шпаргалка</td></tr>

<tr><td style="text-align: center;" class="unselectable">
<svg viewBox="0 0 24 24" width="20" height="20" style="color: var(--color-file-green);"><use href="#icon_folder"></use></svg>
<svg viewBox="0 0 24 24" width="20" height="20" style="color: var(--color-file-green);"><use href="#icon_file"></use></svg>
</td><td style="text-align: left;">Библиотека</td></tr>

<tr><td style="text-align: center;" class="unselectable">
<svg viewBox="0 0 24 24" width="20" height="20" style="color: var(--color-file-red);"><use href="#icon_folder"></use></svg>
<svg viewBox="0 0 24 24" width="20" height="20" style="color: var(--color-file-red);"><use href="#icon_file"></use></svg>
</td><td style="text-align: left;">Важное</td></tr>

<tr><td style="text-align: center;" class="unselectable">
<svg viewBox="0 0 24 24" width="20" height="20" style="color: var(--color-file-pink);"><use href="#icon_folder"></use></svg>
<svg viewBox="0 0 24 24" width="20" height="20" style="color: var(--color-file-pink);"><use href="#icon_file"></use></svg>
</td><td style="text-align: left;"></td></tr>

<tr><td style="text-align: center;" class="unselectable">
<svg viewBox="0 0 24 24" width="20" height="20" style="color: var(--color-file-violet);"><use href="#icon_folder"></use></svg>
<svg viewBox="0 0 24 24" width="20" height="20" style="color: var(--color-file-violet);"><use href="#icon_file"></use></svg>
</td><td style="text-align: left;">Язык</td></tr>

<tr><td style="text-align: center;" class="unselectable">
<svg viewBox="0 0 24 24" width="20" height="20" style="color: var(--color-file-dblue);"><use href="#icon_folder"></use></svg>
<svg viewBox="0 0 24 24" width="20" height="20" style="color: var(--color-file-dblue);"><use href="#icon_file"></use></svg>
</td><td style="text-align: left;"></td></tr>

<tr><td style="text-align: center;" class="unselectable">
<svg viewBox="0 0 24 24" width="20" height="20" style="color: var(--color-file-lblue);"><use href="#icon_folder"></use></svg>
<svg viewBox="0 0 24 24" width="20" height="20" style="color: var(--color-file-lblue);"><use href="#icon_file"></use></svg>
</td><td style="text-align: left;">Картинки</td></tr>

<tr><td style="text-align: center;" class="unselectable">
<svg viewBox="0 0 24 24" width="20" height="20" style="color: var(--color-file-brown);"><use href="#icon_folder"></use></svg>
<svg viewBox="0 0 24 24" width="20" height="20" style="color: var(--color-file-brown);"><use href="#icon_file"></use></svg>
</td><td style="text-align: left;">Примеры кода</td></tr>

</tbody></table>
