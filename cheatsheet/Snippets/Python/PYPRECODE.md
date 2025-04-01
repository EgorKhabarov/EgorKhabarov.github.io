```requirements@requirements.txt
table2string
pyperclip
telebot
arrow
```

```bash
python -m pip install -r requirements.txt
```

`PYPRECODE`
```python
import sys,os,re,requests,time,arrow,html,urllib.parse,math,builtins;from uuid import uuid4;from pathlib import Path;from pyperclip import paste, copy;from datetime import datetime,timedelta;from table2string import Table, Themes, HorizontalAlignment, VerticalAlignment;sqrt = lambda x, p=2: pow(x, (1 / p));uuid=lambda: str(uuid4()).replace('-', '');unicode_escape = lambda text: ''.join(fr'\U{ord(x):0>8x}' for x in text);html_escape, html_unescape, html_escape_full, re_amp = html.escape, html.unescape, lambda text: ''.join(f'&#x{ord(x):x};' for x in text), re.compile(r'(?i)&(?!(?:\#[0-9]+|\#x[0-9a-f]+|[0-9a-z]+);)');url_escape, url_unescape = urllib.parse.quote, urllib.parse.unquote;rgb_to_hex, hex_to_rgb = lambda r, g, b: '#{:02x}{:02x}{:02x}'.format(r, g, b).upper(), lambda h: tuple(int(h.lstrip('#')[i:i + 2], 16) for i in (0, 2, 4));color = lambda *args: hex_to_rgb(*args) if len(args) == 1 else rgb_to_hex(*args);video=lambda length,speed=1:(lambda seconds:f'{round(seconds//3600)}:{round((seconds%3600)//60):02}:{round(seconds%60):02} (seconds={round(seconds)})'.lstrip('0:'))(sum(x*60**i for i,x in enumerate(reversed(list(map(lambda x:int(x)if x.isdecimal()else 0,str(length).split(':'))))))//speed);__ = lambda a: not a.startswith('__');dir = lambda obj=globals(), func=None: [a for a in builtins.dir(obj) if func is None or func(a)];print(f'Python {sys.version} on {sys.platform}\nType "help", "copyright", "credits" or "license" for more information.')
```

```path
python -ic "%PYPRECODE%"
```

```python
import sys,os,re,requests,time,arrow,html,urllib.parse,math,builtins,string
from uuid import uuid4
from pathlib import Path
from pyperclip import paste, copy
from datetime import datetime,timedelta
from table2string import Table, Themes, HorizontalAlignment, VerticalAlignment

sqrt = lambda x, p=2: pow(x, (1 / p))
uuid=lambda: str(uuid4()).replace('-', '')

unicode_escape = lambda text: ''.join(fr'\U{ord(x):0>8x}' for x in text)

html_escape, html_unescape, html_escape_full, re_amp = html.escape, html.unescape, lambda text: ''.join(f'&#x{ord(x):x};' for x in text), re.compile(r'(?i)&(?!(?:\#[0-9]+|\#x[0-9a-f]+|[0-9a-z]+);)')
url_escape, url_unescape = urllib.parse.quote, urllib.parse.unquote

rgb_to_hex, hex_to_rgb = lambda r, g, b: '#{:02x}{:02x}{:02x}'.format(r, g, b).upper(), lambda h: tuple(int(h.lstrip('#')[i:i + 2], 16) for i in (0, 2, 4))
color = lambda *args: hex_to_rgb(*args) if len(args) == 1 else rgb_to_hex(*args)
video=lambda length,speed=1:(lambda seconds:f'{round(seconds//3600)}:{round((seconds%3600)//60):02}:{round(seconds%60):02} (seconds={round(seconds)})'.lstrip('0:'))(sum(x*60**i for i,x in enumerate(reversed(list(map(lambda x:int(x)if x.isdecimal()else 0,str(length).split(':'))))))//speed)

__ = lambda a: not a.startswith('__')
dir = lambda obj=globals(), func=None: [a for a in builtins.dir(obj) if func is None or func(a)]

print(f'Python {sys.version} on {sys.platform}\nType "help", "copyright", "credits" or "license" for more information.')
```

```python
import re
from pyperclip import paste, copy
if input("Скопируйте код и нажмите Enter (вставлять код в консоль не нужно)") or True:
    copy(PYPRECODE := re.sub(r"\n+", r"\n", "\n".join(paste().strip().splitlines())))
```

<!--
quicksort = lambda array: (array if len(array) < 2 else (lambda p, l, g: quicksort(l) + [p] + quicksort(g))(**(lambda pivot, temp_arr: {'p': pivot, 'l': [i for i in temp_arr if i <= pivot], 'g': [i for i in temp_arr if i > pivot]})(array[0], array[1:])))
-->
