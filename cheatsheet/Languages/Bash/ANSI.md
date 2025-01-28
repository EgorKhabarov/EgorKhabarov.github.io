```python
# Escape sequence
ESC = "\u001b" or "\x1b" or "\033"
```

# Reset

|       |           |
|-------|-----------|
| Reset | `\x1b[0m` |

# Decorations

|                   |            |                                                                                                                  |
|-------------------|------------|------------------------------------------------------------------------------------------------------------------|
| Bold              | `\x1b[1m`  | <b>Bold</b>                                                                                                      |
| Faint (Dim)       | `\x1b[2m`  |                                                                                                                  |
| Italic            | `\x1b[3m`  | <i>Italic</i>                                                                                                    |
| Underline         | `\x1b[4m`  | <u>Underline</u>                                                                                                 |
| Blinking (slow)   | `\x1b[5m`  | <div style="color:rgb(204, 204, 204)">Blinking</div>↓      ↑<div style="color:rgb(102, 102, 102)">Blinking</div> |
| Blinking (rapid)  | `\x1b[6m`  | <div style="color:rgb(204, 204, 204)">Blinking</div>↓      ↑<div style="color:rgb(102, 102, 102)">Blinking</div> |
| Inverse           | `\x1b[7m`  |                                                                                                                  |
| Hidden            | `\x1b[8m`  |                                                                                                                  |
| Strikethrough     | `\x1b[9m`  | <s>Strikethrough</s>                                                                                             |
| Doubly underlined | `\x1b[21m` | <span style="text-decoration:double underline;">Doubly underlined</span>                                         |

# Colors

| 8 Colors |            |                                                     | 16 Colors      |              |                                                            |
|----------|------------|-----------------------------------------------------|----------------|--------------|------------------------------------------------------------|
| Black    | `\x1b[30m` | <div style="color:rgb(  0,   0,   0)">Black</div>   | Bright Black   | `\x1b[30;1m` | <div style="color:rgb(118, 118, 118)">Bright Black</div>   |
| Red      | `\x1b[31m` | <div style="color:rgb(197,  15,  31)">Red</div>     | Bright Red     | `\x1b[31;1m` | <div style="color:rgb(231,  72,  86)">Bright Red</div>     |
| Green    | `\x1b[32m` | <div style="color:rgb( 19, 161,  14)">Green</div>   | Bright Green   | `\x1b[32;1m` | <div style="color:rgb( 22, 198,  12)">Bright Green</div>   |
| Yellow   | `\x1b[33m` | <div style="color:rgb(193, 156,   0)">Yellow</div>  | Bright Yellow  | `\x1b[33;1m` | <div style="color:rgb(249, 241, 165)">Bright Yellow</div>  |
| Blue     | `\x1b[34m` | <div style="color:rgb(  0,  55, 218)">Blue</div>    | Bright Blue    | `\x1b[34;1m` | <div style="color:rgb( 59, 120, 255)">Bright Blue</div>    |
| Magenta  | `\x1b[35m` | <div style="color:rgb(136,  23, 152)">Magenta</div> | Bright Magenta | `\x1b[35;1m` | <div style="color:rgb(180,   0, 158)">Bright Magenta</div> |
| Cyan     | `\x1b[36m` | <div style="color:rgb( 58, 150, 221)">Cyan</div>    | Bright Cyan    | `\x1b[36;1m` | <div style="color:rgb( 97, 214, 214)">Bright Cyan</div>    |
| White    | `\x1b[37m` | <div style="color:rgb(204, 204, 204)">White</div>   | Bright White   | `\x1b[37;1m` | <div style="color:rgb(242, 242, 242)">Bright White</div>   |

### 256 Colors

`\u001b[38;5;{}m`
[https://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html#256-colors](https://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html#256-colors)
```python
for i in range(0, 16):
    for j in range(0, 16):
        print(f"\u001b[38;5;{i * 16 + j}m {i * 16 + j:<4}", end="", flush=True)
    print("\u001b[0m")
```



# Background Colors

|                    |            |                                                                              |                           |              |                                                                              |
|--------------------|------------|------------------------------------------------------------------------------|---------------------------|--------------|------------------------------------------------------------------------------|
| Background Black   | `\x1b[40m` | <div style="background-color:rgb(  0,   0,   0);width: 30px;height: 15px;"/> | Background Bright Black   | `\x1b[40;1m` | <div style="background-color:rgb(118, 118, 118);width: 30px;height: 15px;"/> |
| Background Red     | `\x1b[41m` | <div style="background-color:rgb(197,  15,  31);width: 30px;height: 15px;"/> | Background Bright Red     | `\x1b[41;1m` | <div style="background-color:rgb(231,  72,  86);width: 30px;height: 15px;"/> |
| Background Green   | `\x1b[42m` | <div style="background-color:rgb( 19, 161,  14);width: 30px;height: 15px;"/> | Background Bright Green   | `\x1b[42;1m` | <div style="background-color:rgb( 22, 198,  12);width: 30px;height: 15px;"/> |
| Background Yellow  | `\x1b[43m` | <div style="background-color:rgb(193, 156,   0);width: 30px;height: 15px;"/> | Background Bright Yellow  | `\x1b[43;1m` | <div style="background-color:rgb(249, 241, 165);width: 30px;height: 15px;"/> |
| Background Blue    | `\x1b[44m` | <div style="background-color:rgb(  0,  55, 218);width: 30px;height: 15px;"/> | Background Bright Blue    | `\x1b[44;1m` | <div style="background-color:rgb( 59, 120, 255);width: 30px;height: 15px;"/> |
| Background Magenta | `\x1b[45m` | <div style="background-color:rgb(136,  23, 152);width: 30px;height: 15px;"/> | Background Bright Magenta | `\x1b[45;1m` | <div style="background-color:rgb(180,   0, 158);width: 30px;height: 15px;"/> |
| Background Cyan    | `\x1b[46m` | <div style="background-color:rgb( 58, 150, 221);width: 30px;height: 15px;"/> | Background Bright Cyan    | `\x1b[46;1m` | <div style="background-color:rgb( 97, 214, 214);width: 30px;height: 15px;"/> |
| Background White   | `\x1b[47m` | <div style="background-color:rgb(204, 204, 204);width: 30px;height: 15px;"/> | Background Bright White   | `\x1b[47;1m` | <div style="background-color:rgb(242, 242, 242);width: 30px;height: 15px;"/> |

### 256 Background Colors
`\u001b[48;5;{}m`

```python
for i in range(0, 16):
    for j in range(0, 16):
        code = str(i * 16 + j)
        print("\u001b[48;5;" + code + "m " + code.ljust(4), end="")
    print("\u001b[0m")
```

# RGB

|                   |                          |                             |                                                                                      |
|-------------------|--------------------------|-----------------------------|--------------------------------------------------------------------------------------|
| Colors            | `\x1b[38;2;{r};{g};{b}m` | `\x1b[38;2;200;156;55mtext` | <span style="color:rgb(200, 156, 55)">text</span>                                    |
| Background Colors | `\x1b[48;2;{r};{g};{b}m` | `\x1b[48;2;200;156;55mtext` | <span style="background-color:rgb(200, 156, 55);color:rgb(200, 156, 55)">text</span> |

# Cursor

|                      |                                    |                                                        |
|----------------------|------------------------------------|--------------------------------------------------------|
| Up                   | `\x1b[{n}A`                        |                                                        |
| Down                 | `\x1b[{n}B`                        |                                                        |
| Right                | `\x1b[{n}C`                        |                                                        |
| Left                 | `\x1b[{n}D`                        |                                                        |
| Next Line            | `\x1b[{n}E`                        | Перемещает курсор к началу линий линии вниз            |
| Prev Line            | `\x1b[{n}F`                        | Перемещает курсор к началу линий линии вниз            |
| Set Position         | `\x1b[{n};{m}H`<br>`\x1b[{n};{m}f` | Перемещает курсор в столбец строки                     |
| Set Column           | `\x1b[{n}G`                        | Перемещает курсор в указанный столбец в текущей строке |
| Save Position        | `\x1b[s`                           | Сохранить текущую позицию курсора                      |
| Restore Position     | `\x1b[u`                           | Восстановить сохраненную позицию курсора               |
| Hide Cursor          | `\x1b[?25l`                        |                                                        |
| Show Cursor          | `\x1b[?25h`                        |                                                        |
| Shift + Up           | `\x1b[{n};2A`                      |                                                        |
| Shift + Down         | `\x1b[{n};2B`                      |                                                        |
| Shift + Right        | `\x1b[{n};2C`                      |                                                        |
| Shift + Left         | `\x1b[{n};2D`                      |                                                        |
| Ctrl + Shift + Up    | `\x1b[{n};6A`                      |                                                        |
| Ctrl + Shift + Down  | `\x1b[{n};6B`                      |                                                        |
| Ctrl + Shift + Right | `\x1b[{n};6C`                      |                                                        |
| Ctrl + Shift + Left  | `\x1b[{n};6D`                      |                                                        |

# Deletion

|              |             |                                                                                                                                |
|--------------|-------------|--------------------------------------------------------------------------------------------------------------------------------|
| Clear Screen | `\x1b[{n}J` | n=`0` clears from cursor until end of screen,<br>n=`1` clears from cursor to beginning of screen<br>n=`2` clears entire screen |
| Clear Line   | `\x1b[{n}K` | n=`0` clears from cursor to end of line<br>n=`1` clears from cursor to start of line<br>n=`2` clears entire line               |

- `\x1b[?1049h` Включить альтернативный экранный буфер.
Это часто используется в текстовых редакторах, чтобы предоставить пользователю чистый экран для работы.
- `\x1b[?1049l` Отключить альтернативный экранный буфер и вернуть содержимое основного экрана.
- `\x1b[?1h` Включить режим "прямой печати". Некоторые терминалы могут обрабатывать это по-разному.
- `\x1b[?1l` Отключить режим "прямой печати".
- `\x1b[1;32;40m` устанавливает жирный зеленый текст на черном фоне.
- `\x1b[3;5;7m` Вы можете комбинировать несколько атрибутов, чтобы,
например, сделать текст жирным, с курсивом и инверсным цветом.
- `\x1b[0;31;47m` Это сброс всех атрибутов и установка красного текста на белом фоне.
- `\x1b[X` Удаление символа в позиции курсора (может работать по-разному в зависимости от терминала).
- `\x1b[P` Удаление символа, на который указывает курсор.
- `\007` Это код звукового сигнала (bell). При его использовании терминал издает звук.
- `\033[39m` Этот код сбрасывает цвет текста к цвету по умолчанию.
Если цвет текста был изменён, он вернётся к стандартному цвету терминала.
- `\x1b]0;Title\007` Устанавливает заголовок окна терминала.
- `\x1b]8;;<URL>\x1b\` Создаёт кликабельную ссылку

```bash
echo -e "\033]8;;http://example.com\033\\Click Here\033]8;;\033\\"
```

```bash
echo -e "\033]0;My Terminal Window\007"
```
