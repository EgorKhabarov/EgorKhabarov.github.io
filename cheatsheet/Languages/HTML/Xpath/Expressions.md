# Steps and axes

|         |      |      |               |
|---------|------|------|---------------|
| //      | ul   | /    | a[@id='link'] |
| Axis    | Step | Axis | Step          |


# Prefixes

| Prefix | Example             | What     |
|--------|---------------------|----------|
| //     | //hr[@class='edge'] | Anywhere |
| ./     | ./a                 | Relative |
| /      | /html/body/div      | Root     |

Begin your expression with any of these.



# Axes

| Axis | Example           | What       |
|------|-------------------|------------|
| /    | //ul/li/a         | Child      |
| //   | //[@id="list"]//a | Descendant |

Separate your steps with /. Use two (//) if you don’t want to select direct children.


# Steps

```bash
//div
//div[@name='box']
//[@id='link']
```

A step may have an element name (div) and predicates ([...]). Both are optional. They can also be these other things:

```bash
//a/text()     #=> "Go home"
//a/@href      #=> "index.html"
//a/*          #=> All a's child elements
```
