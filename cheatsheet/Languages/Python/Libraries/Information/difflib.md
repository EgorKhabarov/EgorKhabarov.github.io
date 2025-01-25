#### SequenceMatcher
Сравнение двух последовательностей и определение степени их сходства.

```python
import difflib

s1 = "Hello, world!"
s2 = "Hello, everyone!"

matcher = difflib.SequenceMatcher(None, s1, s2)
ratio = matcher.ratio()

print(f"Similarity ratio: {ratio}")

"""Similarity ratio: 0.6206896551724138"""
```


#### get_close_matches
Нахождение наиболее похожей строки в наборе строк на основе заданной строки.

```python
import difflib

colors = ["red", "green", "blue", "yellow"]
color = "grea"

matches = difflib.get_close_matches(color, colors)

print(f"Closest matches: {matches}")

"""Closest matches: ["green"]"""
```


#### unified_diff
Генерация отчета о различиях между двумя последовательностями.

```python
import difflib

text1 = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."""

text2 = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magnus aliqua."""

d = difflib.unified_diff(text1.splitlines(), text2.splitlines())

print("\n".join(d))

"""
---

+++

@@ -1,3 +1,3 @@

 Lorem ipsum dolor sit amet,
 consectetur adipiscing elit,
-sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
+sed do eiusmod tempor incididunt ut labore et dolore magnus aliqua.
"""
```

#### HtmlDiff
Генерация отчета о различиях между двумя последовательностями в формате HTML.

```python
import difflib

text1 = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."""

text2 = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magnus aliqua."""

d = difflib.HtmlDiff().make_file(text1.splitlines(), text2.splitlines())

with open("diff.html", "w") as f:
    f.writelines(d)
```














#### context_diff
Генерация отчета о различиях между двумя последовательностями в формате context diff.

```python
import difflib

text1 = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."""

text2 = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magnus aliqua."""

d = difflib.context_diff(text1.splitlines(), text2.splitlines())

print("\n".join(d))

"""
***

---

***************

*** 1,3 ****

  Lorem ipsum dolor sit amet,
  consectetur adipiscing elit,
! sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
--- 1,3 ----

  Lorem ipsum dolor sit amet,
  consectetur adipiscing elit,
! sed do eiusmod tempor incididunt ut labore et dolore magnus aliqua.
"""
```

#### ndiff
Генерация отчета о различиях между двумя последовательностями в формате ndiff.

```python
import difflib

text1 = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."""

text2 = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magnus aliqua."""

d = difflib.ndiff(text1.splitlines(), text2.splitlines())

print("\n".join(d))

"""
  Lorem ipsum dolor sit amet,
  consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
?                                                          ^

+ sed do eiusmod tempor incididunt ut labore et dolore magnus aliqua.
?                                                          ^^
"""
```

#### isjunk и ignore
Использование пользовательских функций для игнорирования символов при сравнении последовательностей.

```python
import difflib

def isjunk(s):
    return s in [" ", "\n"]

text1 = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."""

text2 = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magnus aliqua."""

matcher = difflib.SequenceMatcher(isjunk, text1, text2)
ratio = matcher.ratio()

print(f"Similarity ratio: {ratio}")

"""Similarity ratio: 0.9878542510121457"""
```

#### reduce_func
Использование пользовательской функции для преобразования различий в отчете о сравнении.

```python
import difflib

text1 = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."""

text2 = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magnus aliqua."""

d = difflib.Differ()
diff = d.compare(text1.splitlines(), text2.splitlines())

def reduce_func(s):
    if s.startswith("- "):
        return f"<span style="color:red">{s}</span>"
    elif s.startswith("+ "):
        return f"<span style="color:green">{s}</span>"
    else:
        return s

diff = map(reduce_func, diff)
diff = "\n".join(diff)

print(diff)

"""
  Lorem ipsum dolor sit amet,
  consectetur adipiscing elit,
<span style="color:red">- sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</span>
?                                                          ^

<span style="color:green">+ sed do eiusmod tempor incididunt ut labore et dolore magnus aliqua.</span>
?                                                          ^^
"""
```
