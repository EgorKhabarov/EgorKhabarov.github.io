# Using axes

```bash
//ul/li                       # ul > li
//ul/child::li                # ul > li (same)
//ul/following-sibling::li    # ul ~ li
//ul/descendant-or-self::li   # ul li
//ul/ancestor-or-self::li     # $('ul').closest('li')
```

Steps of an expression are separated by /, usually used to pick child nodes
That’s not always true: you can specify a different “axis” with ::

|      |      |          |      |
|------|------|----------|------|
| //   | ul   | /child:: | li   |
| Axis | Step | Axis     | Step |

# Child axis

```bash
# both the same
//ul/li/a
//child::ul/child::li/child::a
```

child:: is the default axis. This makes //a/b/c work

```bash
# both the same
# this works because `child::li` is truthy, so the predicate succeeds
//ul[li]
//ul[child::li]
```

```bash
# both the same
//ul[count(li) > 2]
//ul[count(child::li) > 2]
```



# Descendant-or-self axis

```bash
# both the same
//div//h4
//div/descendant-or-self::h4
```

// is short for the descendant-or-self:: axis

```bash
# both the same
//ul//[last()]
//ul/descendant-or-self::[last()]
```

# Other axes

| Axis                             | Abbrev   | Notes                                        |
|----------------------------------|----------|----------------------------------------------|
| ancestor                         |          |                                              |
| ancestor-or-self                 |          |                                              |
| attribute                        | @        |  @href is short for attribute::href          |
| child                            |          |  div is short for child::div                 |
| descendant                       |          |                                              |
| descendant-or-self               | //       | // is short for /descendant-or-self::node()/ |
| namespace                        |          |                                              |
| self                             | .        |  . is short for self::node()                 |
| parent                           | ..       | .. is short for parent::node()               |
| following                        |          |                                              |
| following-sibling                |          |                                              |
| preceding                        |          |                                              |
| preceding-sibling                |          |                                              |

There are other axes you can use

# Unions

//a | //span
Use | to join two expressions
