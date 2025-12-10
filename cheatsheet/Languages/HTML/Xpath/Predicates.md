# Predicates

```bash
//div[true()]
//div[@class="head"]
//div[@class="head"][@id="top"]
```

Restricts a nodeset only if some condition is true
They can be chained

# Operators

```bash
# Comparison
//a[@id = "xyz"]
//a[@id != "xyz"]
//a[@price > 25]
```

```bash
# Logic (and/or)
//div[@id="head" and position()=2]
//div[(x and y) or not(z)]
```

Use comparison and logic operators to make conditionals

# Using nodes

```bash
# Use them inside functions
//ul[count(li) > 2]
//ul[count(li[@class='hide']) > 0]
```

```bash
# This returns `<ul>` that has a `<li>` child
//ul[li]
```

You can use nodes inside predicates

# Indexing

```bash
//a[1]                  # first <a>
//a[last()]             # last <a>
//ol/li[2]              # second <li>
//ol/li[position()=2]   # same as above
//ol/li[position()>1]   # :not(:first-of-type)
```

Use [] with a number, or last() or position()

# Chaining order

```bash
a[1][@href='/']
a[@href='/'][1]
```

Order is significant, these two are different

# Nesting predicates

```bash
//section[.//h1[@id='hi']]
```
This returns &lt;section> if it has an &lt;h1> descendant with id='hi'
