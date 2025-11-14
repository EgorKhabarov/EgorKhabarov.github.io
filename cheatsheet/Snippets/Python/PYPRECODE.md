```requirements@requirements.txt
table2string
pyperclip
telebot
arrow
```

```bash
python -m pip install -r requirements.txt
```

```bash
python -m pip install table2string pyperclip telebot arrow
```

<!--
`PYPRECODE`
```python
import sys,os,re,requests,time,arrow,html,urllib.parse,math,builtins,string,inspect,base64 as __base64;from uuid import uuid4;from pathlib import Path;from pyperclip import paste, copy;from datetime import datetime,timedelta;from table2string import Table,Themes,HorizontalAlignment,VerticalAlignment;cmd=os.system;sqrt=lambda x,p=2:pow(x,(1/p));uuid=lambda:str(uuid4()).replace('-','');unicode_escape=lambda text:''.join(fr'\U{ord(x):0>8x}'for x in text);html_escape,html_unescape,html_escape_full,re_amp=html.escape,html.unescape,lambda text:''.join(f'&#x{ord(x):x};'for x in text),re.compile(r'(?i)&(?!(?:\#[0-9]+|\#x[0-9a-f]+|[0-9a-z]+);)');url_escape,url_unescape=urllib.parse.quote,urllib.parse.unquote;rgb_to_hex,hex_to_rgb=lambda r,g,b:'#{:02x}{:02x}{:02x}'.format(r,g,b).upper(),lambda h:tuple(int(h.lstrip('#')[i:i+2],16)for i in(0,2,4));color=lambda*args:rgb_to_hex(*args)if len(args)!=1 else rgb_to_hex(*args*3)if isinstance(args[0],int)else hex_to_rgb(*args);video=lambda length,speed=1:(lambda seconds:f'{round(seconds//3600)}:{round((seconds%3600)//60):02}:{round(seconds%60):02} (seconds={round(seconds)})'.lstrip('0:'))(sum(x*60**i for i,x in enumerate(reversed(list(map(lambda x:int(x)if x.isdecimal()else 0,str(length).split(':'))))))//speed);__=lambda a:not a.startswith('__');dir=lambda obj=globals(),func=None:[a for a in builtins.dir(obj)if func is None or func(a)];lp=lambda:len(paste());uurl=lambda:copy(url_unescape(paste()));base64=lambda bytes_:__base64.b64encode(bytes_).decode('UTF-8');print(f'Python {sys.version} on {sys.platform}\nType "help", "copyright", "credits" or "license" for more information.')
```

```path
python -ic "%PYPRECODE%"
```
-->

<!--
```python@PYPRECODE.py
import sys,os,re,requests,time,arrow,html,urllib.parse,math,builtins,string,inspect,base64 as __base64
from uuid import uuid4
from pathlib import Path
from pyperclip import paste, copy
from datetime import datetime, timedelta
from table2string import Table, Themes, HorizontalAlignment, VerticalAlignment

cmd = os.system
sqrt = lambda x, p=2: pow(x, (1 / p))
uuid = lambda: str(uuid4()).replace('-', '')

unicode_escape = lambda text: ''.join(fr'\U{ord(x):0>8x}' for x in text)

html_escape, html_unescape, html_escape_full, re_amp = html.escape, html.unescape, lambda text: ''.join(f'&#x{ord(x):x};' for x in text), re.compile(r'(?i)&(?!(?:\#[0-9]+|\#x[0-9a-f]+|[0-9a-z]+);)')
url_escape, url_unescape = urllib.parse.quote, urllib.parse.unquote

rgb_to_hex, hex_to_rgb = lambda r, g, b: '#{:02x}{:02x}{:02x}'.format(r, g, b).upper(), lambda h: tuple(int(h.lstrip('#')[i:i + 2], 16) for i in (0, 2, 4))
color = lambda *args: rgb_to_hex(*args) if len(args) != 1 else rgb_to_hex(*args*3) if isinstance(args[0], int) else hex_to_rgb(*args)
video = lambda length, speed=1: (lambda seconds:f'{round(seconds//3600)}:{round((seconds%3600)//60):02}:{round(seconds%60):02} (seconds={round(seconds)})'.lstrip('0:'))(sum(x*60**i for i,x in enumerate(reversed(list(map(lambda x: int(x) if x.isdecimal() else 0, str(length).split(':'))))))//speed)

__ = lambda a: not a.startswith('__')
dir = lambda obj=None, func=None: [a for a in builtins.dir(obj or globals()) if func is None or func(a)]
lp = lambda: len(paste())
uurl = lambda: copy(url_unescape(paste()))
base64encode = lambda bytes_: __base64.b64encode(bytes_).decode('UTF-8')
base64decode = lambda string_: __base64.b64decode(string_)
signature = sign = s = lambda func: f'{func.__name__}{inspect.signature(func)}'

print(f'Python {sys.version} on {sys.platform}\nType "help", "copyright", "credits" or "license" for more information.')
```
-->

```python @PYPRECODE.py
import os
import re
import sys
import html
import inspect
import builtins
import urllib.parse
import base64 as __base64
from uuid import uuid4
from typing import Any, Callable
from typing_extensions import Buffer

# unused
# noinspection PyUnresolvedReferences
import time
# noinspection PyUnresolvedReferences
import math
# noinspection PyUnresolvedReferences
import string
# noinspection PyUnresolvedReferences
import requests
# noinspection PyUnresolvedReferences
from pathlib import Path
# noinspection PyUnresolvedReferences
from datetime import datetime, timedelta

# noinspection PyUnresolvedReferences
import arrow
from pyperclip import paste, copy
# noinspection PyUnresolvedReferences
from table2string import Table, Themes, HorizontalAlignment, VerticalAlignment


HELP = r"""
def sqrt(x: int | float, p: int = 2) -> int:
def uuid() -> str:
def video(length: str, speed: int = 1) -> str:

def rgb_to_hex(r: int, g: int, b: int) -> str:
def hex_to_rgb(h: str) -> tuple[int, ...]:
def color(*args: int | str) -> str | tuple[int, ...]:

def unicode_escape(text: str) -> str:
def base64encode(bytes_: bytes | Buffer) -> str:
def base64decode(string_: str | Buffer) -> bytes:
def html_escape_full(text: str) -> str:


def url_escape(string: str,
               safe: str | Iterable[int] = "/",
               encoding: str | None = None,
               errors: str | None = None) -> str:
def url_unescape(string: str | bytes, encoding: str = "UTF-8", errors: str = "replace") -> str:
def html_escape(s: str, quote: bool = True) -> str:
def html_unescape(s: str) -> str:
def uurl() -> None: copy(url_unescape(paste()))

re_amp = re.compile(r'(?i)&(?!(?:\#[0-9]+|\#x[0-9a-f]+|[0-9a-z]+);)')

cmd = os.system
def dir(obj: Any | None = None, func: Callable = None) -> list[str]:
sign = s = def signature(func: Callable) -> str:

__ = lambda a: not a.startswith("__")
lp = lambda: len(paste())
fint = lambda i: f"{i:_}"
""".strip()

# Math

def sqrt(x: int | float, p: int = 2) -> int:
    return pow(x, (1 / p))

def uuid() -> str:
    return str(uuid4()).replace("-", "")

def video(length: str, speed: int = 1) -> str:
    video_seconds: int = sum(
        x * 60 ** i
        for i, x in enumerate(
            reversed(
                list(
                    map(
                        lambda x: int(x) if x.isdecimal() else 0,
                        str(length).split(":")
                    )
                )
            )
        )
    ) // speed
    hours: int = round(video_seconds // 3600)
    minutes: int = round((video_seconds % 3600) // 60)
    seconds: int = round(video_seconds % 60)
    return f"{hours}:{minutes:02}:{seconds:02} (seconds={round(video_seconds)})".lstrip("0:")

# Converters

## Color

def rgb_to_hex(r: int, g: int, b: int) -> str:
    return "{:02x}{:02x}{:02x}".format(r, g, b).upper()

def hex_to_rgb(h: str) -> tuple[int, ...]:
    return tuple(int(h.lstrip("#")[i:i + 2], 16) for i in (0, 2, 4))

def color(*args: int | str) -> str | tuple[int, ...]:
    if len(args) != 1:
        return rgb_to_hex(*args)
    elif isinstance(args[0], int):
        return rgb_to_hex(*args*3)
    else:
        return hex_to_rgb(*args)

## Escape
def unicode_escape(text: str) -> str:
    return "".join(fr"\U{ord(x):0>8x}" for x in text)

def base64encode(bytes_: bytes | Buffer) -> str:
    return __base64.b64encode(bytes_).decode("UTF-8")

def base64decode(string_: str | Buffer) -> bytes:
    return __base64.b64decode(string_)

def html_escape_full(text: str) -> str:
    return "".join(f"&#x{ord(x):x};" for x in text)

def uurl() -> None:
    copy(url_unescape(paste()))

url_escape = urllib.parse.quote
url_unescape = urllib.parse.unquote
html_escape = html.escape
html_unescape = html.unescape

# RegExp
re_amp = re.compile(r'(?i)&(?!(?:\#[0-9]+|\#x[0-9a-f]+|[0-9a-z]+);)')

# Python
cmd = os.system

def dir(obj: Any | None = None, func: Callable = None) -> list[str]:  # noqa
    return [
        a
        for a in builtins.dir(obj or globals())
        if func is None or func(a)
    ]

def signature(func: Callable) -> str:
    return f"{func.__name__}{inspect.signature(func)}\n{""""""}".strip()

sign = s = signature

# Utils
__ = lambda a: not a.startswith("__")
lp = lambda: len(paste())
fint = lambda i: f"{i:_}"

class PyHelp:
    regex_line_start_span = re.compile(r'(?m)^<span class="n">(.+?)</span>')
    regex_remove_o_span = re.compile(r'<span class="o">(=)</span>')
    regex_def_color_span = re.compile(r' = <span class="n">(.+?)</span> = <span class="k">def</span>')
    regex_color_class_span = re.compile(r'<span class="(.+?)">(.+?)</span>')

    def __init__(self):
        self.class_map: dict[str, str] = {
            **dict.fromkeys(("k", "ow", "kn", "si", "se", "kd", "kc", "nt"), self.__format_color("CC7832")),  # Keywords
            **dict.fromkeys(("s", "s1", "s2", "sa", "sd"), self.__format_color("529755")),  # Text
            **dict.fromkeys(("m", "mi", "mf"), self.__format_color("5897BB")),  # Number
            **dict.fromkeys(("nb", "kt"), self.__format_color("8888C6")),  # Default functions
            "fm": self.__format_color("B200B2"),  # Magical methods
            "bp": self.__format_color("94558D"),  # Self
            "nd": self.__format_color("BBB529"),  # Decorator
            "nf": self.__format_color("FFC66D"),  # Function name
            "na": self.__format_color("AA4926"),  # Argument
            **dict.fromkeys(("c1", "cp", "cpf"), self.__format_color("7F7F7F")),  # Comment hsla(0,0%,100%,.5)  
        }

    @staticmethod
    def __format_color(hex_color: str) -> str:
        r, g, b = hex_to_rgb(hex_color)
        return f"\x1b[38;2;{r};{g};{b}m"

    def __repr__(self):
        try:
            from pygments import highlight
            from pygments.util import ClassNotFound
            from pygments.lexers import get_lexer_by_name
            from pygments.formatters import HtmlFormatter
        except ImportError:
            return (
                "\x1b[31mRun `"
                "pip install pygments"
                "` and restart the console for syntax highlighting\x1b[0m"
                f"\n{HELP}"
            )

        
        formatter = HtmlFormatter(style="default")
        language = "python"

        try:
            lexer = get_lexer_by_name(language, stripall=True)
        except ClassNotFound:
            language = "text"
            lexer = get_lexer_by_name(language, stripall=True)
        
        highlighted_code = (
            highlight(HELP, lexer, formatter)
            .strip()
            .removeprefix('<div class="highlight"><pre><span></span>')
            .removesuffix("</pre></div>")
        )
        result = self.regex_line_start_span.sub(r'<span class="nf">\1</span>', highlighted_code)
        result = self.regex_remove_o_span.sub(r'\1', result)
        result = self.regex_def_color_span.sub(r' = <span class="nf">\1</span> = <span class="k">def</span>', result)
        result = self.regex_color_class_span.sub(
            lambda m: (
                html.unescape(m[2])
                if m[1] not in self.class_map
                else f"{self.class_map[m[1]]}{html.unescape(m[2])}\x1b[0m"),
            result,
        )
        # result = result.replace("\x1b", "\\x1b")
        return result.strip()


pyhelp = PyHelp()  # noqa

if __name__ == "__main__":
    if "get_ipython" not in globals():
        print(f"""
Python {sys.version} on {sys.platform}
Type "help", "copyright", "credits" or "license" for more information.
""".strip())
    print('PYPRECODE v1.0.0 Type "pyhelp" for more information.')
```

```bash
python -i "%USERPROFILE%/PYPRECODE.py"
```

<!--
```python
import re
from pyperclip import paste, copy
if input("Скопируйте код и нажмите Enter (вставлять код в консоль не нужно)") or True:
    copy(PYPRECODE := re.sub(r"\n+", r"\n", "\n".join(paste().strip().splitlines())))
```
-->

<!--
quicksort = lambda array: (array if len(array) < 2 else (lambda p, l, g: quicksort(l) + [p] + quicksort(g))(**(lambda pivot, temp_arr: {'p': pivot, 'l': [i for i in temp_arr if i <= pivot], 'g': [i for i in temp_arr if i > pivot]})(array[0], array[1:])))
-->

<!--
1. ```bash SystemPropertiesAdvanced```
2. Переменные среды
3. Создать/Изменить
4. PYPRECODE
-->
