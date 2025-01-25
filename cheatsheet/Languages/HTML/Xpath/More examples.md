# Examples

```bash
//*                 # all elements
count(//*)          # count all elements
(//h1)[1]/text()    # text of the first h1 heading
//li[span]          # find a <li> with an <span> inside it
                    # ...expands to //li[child::span]
//ul/li/..          # use .. to select a parent
```


# Find a parent

```bash
//section[h1[@id='section-name']]
```

Finds a &lt;section> that directly contains h1#section-name

```bash
//section[//h1[@id='section-name']]
```

Finds a &lt;section> that contains h1#section-name.
(Same as above, but uses descendant-or-self instead of child)

# Closest

```bash
./ancestor-or-self::[@class="box"]
```

Works like jQuery’s $().closest('.box').

# Attributes

```bash
//item[@price > 2*@discount]
```

Finds &lt;item> and check its attributes
