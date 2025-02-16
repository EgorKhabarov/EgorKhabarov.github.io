# Descendant selectors

|              |           |    |
|--------------|-----------|----|
| h1           | //h1      | ?  |
| div p        | //div//p  | ?  |
| ul > li      | //ul/li   | ?  |
| ul > li > a  | //ul/li/a |    |
| div > *      | //div/*   |    |
| :root        | /         | ?  |
| :root > body | /body     |    |

# Attribute selectors

|                       |                                     |    |
|-----------------------|-------------------------------------|----|
| #id                   | //*\[@id="id"]                      | ?  |
| .class                | //*\[@class="class"] …kinda         |    |
| input\[type="submit"] | //input\[@type="submit"]            |    |
| a#abc\[for="xyz"]     | //a\[@id="abc"]\[@for="xyz"]        | ?  |
| a\[rel]               | //a\[@rel]                          |    |
| a\[href^='/']         | //a\[starts-with(@href, '/')]       | ?  |
| a\[href$='pdf']       | //a\[ends-with(@href, '.pdf')]      |    |
| a\[href*='://']       | //a\[contains(@href, '://')]        |    |
| a\[rel~='help']       | //a\[contains(@rel, 'help')] …kinda |    |

# Order selectors

|                        |                           |    |
|------------------------|---------------------------|----|
| ul > li:first-of-type  | //ul/li\[1]               | ?  |
| ul > li:nth-of-type(2) | //ul/li\[2]               |    |
| ul > li:last-of-type   | //ul/li\[last()]          |    |
| li#id:first-of-type    | //li\[1]\[@id="id"]       | ?  |
| a:first-child          | //*\[1]\[name()="a"]      |    |
| a:last-child           | //*\[last()]\[name()="a"] |    |

# Siblings

|          |                                    |    |
|----------|------------------------------------|----|
| h1 ~ ul  | //h1/following-sibling::ul         | ?  |
| h1 + ul  | //h1/following-sibling::ul[1]      |    |
| h1 ~ #id | //h1/following-sibling::[@id="id"] |    |


# jQuery

|                            |                                |    |
|----------------------------|--------------------------------|----|
| $('ul > li').parent()      | //ul/li/..                     | ?  |
| $('li').closest('section') | //li/ancestor-or-self::section |    |
| $('a').attr('href')        | //a/@href                      | ?  |
| $('span').text()           | //span/text()                  |    |

# Other things

|                         |                                  |    |
|-------------------------|----------------------------------|----|
| h1:not(\[id])           | //h1\[not(@id)]                  | ?  |
| Text match              | //button\[text()="Submit"]       | ?  |
| Text match (substring)  | //button\[contains(text(),"Go")] |    |
| Arithmetic              | //product\[@price > 2.50]        |    |
| Has children            | //ul\[*]                         |    |
| Has children (specific) | //ul\[li]                        |    |
| Or logic                | //a\[@name or @href]             | ?  |
| Union (joins results)   | //a \| //div                     | ?  |

# Class check

|                                                                     |
|---------------------------------------------------------------------|
| //div[contains(concat(' ',normalize-space(@class),' '),' foobar ')] |

Xpath doesn’t have the “check if part of space-separated list” operator, so this is the workaround (source)
