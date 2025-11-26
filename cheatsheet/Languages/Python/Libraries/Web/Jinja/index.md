<!--{% raw %}-->
**Шаблонный движок**: `Jinja3` шаблонный движок для `Python`,
который помогает отделить логику приложения от представления.
Это достигается за счет использования шаблонов для генерации HTML (или других текстовых форматов),
что позволяет легко изменять внешний вид и структуру выходных данных без изменения логики кода

**Переменные**: В `Jinja3` переменные используются для динамической вставки данных в шаблон.
Они обозначаются двойными фигурными скобками `{{ variable }}`
и могут содержать любые данные, переданные из контекста рендеринга

# Basic usage
```jinja
- variable x has content: {{ x }}
- expression: {{ x + 1 }}
- escaped for HTML: {{ x | e }}
```

# Control structures
```jinja
{% for x in range(5) %}
    {% if x % 2 == 0 %}
        {{ x }} is even!
    {% else %}
        {{ x }} is odd!
    {% endif %}
{% endfor %}
```

# Whitespace trimming
```jinja
these are
{{ "three" }}
lines.

this is conc
{{- "at" -}}
enated.
```

# Special blocks
```jinja
{% filter e %}
{% _raw %}
    This is a raw block where {{nothing is evaluated}}
    {% not even this %}
    and <html is escaped> too with "e" filter
{% _endraw %}
{% endfilter %}

{% macro myfunc(x) %}
    this is a reusable macro, with arguments: {{x}}
{% endmacro %}

{{ myfunc(42) }}

{#
this is a comment
#}
```

# Inheritance
```jinja@shared.html
<html>
  <head>
    <title>{%block title %}{% endblock %}</title>
  </head>
  <body>
    <header><h1>{% block title %}{% endblock %}</h1></header>
    <main>{% block content %}{% endblock %}</main>
  </body>
</html>
```

```jinja@home.html
{% extends "shared.html" %}
{% block title %}Welcome to my site{% endblock %}
{% block content %}
This is the body
{% endblock %}
```

# Basic usage
```python
from jinja2 import Template
template = Template("Hello {{ name }}!")
template.render(name="John Doe") == u"Hello John Doe!"
```
<!--{% endraw %}-->
