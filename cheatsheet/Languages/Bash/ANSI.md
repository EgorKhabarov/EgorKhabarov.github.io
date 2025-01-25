```python
# Escape sequence
ESC = "\u001b" or "\x1b"
```

|       |             |
|-------|-------------|
| Reset | ESC`[0m` |

# Decorations

|                        |           |
|------------------------|-----------|
| Bold                   | ESC`[1m`  |
| Faint (Dim)            | ESC`[2m`  |
| Italic                 | ESC`[3m`  |
| Underline              | ESC`[4m`  |
| Blinking (slow)        | ESC`[5m`  |
| Blinking (rapid)       | ESC`[6m`  |
| Inverse                | ESC`[7m`  |
| Hidden                 | ESC`[8m`  |
| Strikethrough          | ESC`[9m`  |
| Doubly underlined mode | ESC`[21m` |

# Colors

| 8 Colors |           | 16 Colors      |             |
|----------|-----------|----------------|-------------|
| Black    | ESC`[30m` | Bright Black   | ESC`[30;1m` |
| Red      | ESC`[31m` | Bright Red     | ESC`[31;1m` |
| Green    | ESC`[32m` | Bright Green   | ESC`[32;1m` |
| Yellow   | ESC`[33m` | Bright Yellow  | ESC`[33;1m` |
| Blue     | ESC`[34m` | Bright Blue    | ESC`[34;1m` |
| Magenta  | ESC`[35m` | Bright Magenta | ESC`[35;1m` |
| Cyan     | ESC`[36m` | Bright Cyan    | ESC`[36;1m` |
| White    | ESC`[37m` | Bright White   | ESC`[37;1m` |

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

|                    |           |                           |             |
|--------------------|-----------|---------------------------|-------------|
| Background Black   | ESC`[40m` | Background Bright Black   | ESC`[40;1m` |
| Background Red     | ESC`[41m` | Background Bright Red     | ESC`[41;1m` |
| Background Green   | ESC`[42m` | Background Bright Green   | ESC`[42;1m` |
| Background Yellow  | ESC`[43m` | Background Bright Yellow  | ESC`[43;1m` |
| Background Blue    | ESC`[44m` | Background Bright Blue    | ESC`[44;1m` |
| Background Magenta | ESC`[45m` | Background Bright Magenta | ESC`[45;1m` |
| Background Cyan    | ESC`[46m` | Background Bright Cyan    | ESC`[46;1m` |
| Background White   | ESC`[47m` | Background Bright White   | ESC`[47;1m` |

### 256 Background Colors
`\u001b[48;5;{}m`

```python
import sys
for i in range(0, 16):
    for j in range(0, 16):
        code = str(i * 16 + j)
        print("\u001b[48;5;" + code + "m " + code.ljust(4), end="")
    print("\u001b[0m")
```

# RGB Colors
ESC`[38;2;{r};{g};{b}m`

# RGB Background Colors
ESC`[48;2;{r};{g};{b}m`

# Cursor

|                      |                                  |                                                        |
|----------------------|----------------------------------|--------------------------------------------------------|
| Up                   | ESC`[{n}A`                       |                                                        |
| Down                 | ESC`[{n}B`                       |                                                        |
| Right                | ESC`[{n}C`                       |                                                        |
| Left                 | ESC`[{n}D`                       |                                                        |
| Next Line            | ESC`[{n}E`                       | Перемещает курсор к началу линий линии вниз            |
| Prev Line            | ESC`[{n}F`                       | Перемещает курсор к началу линий линии вниз            |
| Set Position         | ESC`[{n};{m}H`<br>ESC`[{n};{m}f` | Перемещает курсор в столбец строки                     |
| Set Column           | ESC`[{n}G`                       | Перемещает курсор в указанный столбец в текущей строке |
| Save Position        | ESC`[s`                          | Сохранить текущую позицию курсора                      |
| Restore Position     | ESC`[u`                          | Восстановить сохраненную позицию курсора               |
| Hide Cursor          | ESC`[?25l`                       |                                                        |
| Show Cursor          | ESC`[?25h`                       |                                                        |
| Shift + Up           | ESC`[{n};2A`                     |                                                        |
| Shift + Down         | ESC`[{n};2B`                     |                                                        |
| Shift + Right        | ESC`[{n};2C`                     |                                                        |
| Shift + Left         | ESC`[{n};2D`                     |                                                        |
| Ctrl + Shift + Up    | ESC`[{n};6A`                     |                                                        |
| Ctrl + Shift + Down  | ESC`[{n};6B`                     |                                                        |
| Ctrl + Shift + Right | ESC`[{n};6C`                     |                                                        |
| Ctrl + Shift + Left  | ESC`[{n};6D`                     |                                                        |

# Deletion

|              |            |                                                                                                                                |
|--------------|------------|--------------------------------------------------------------------------------------------------------------------------------|
| Clear Screen | ESC`[{n}J` | n=`0` clears from cursor until end of screen,<br>n=`1` clears from cursor to beginning of screen<br>n=`2` clears entire screen |
| Clear Line   | ESC`[{n}K` | n=`0` clears from cursor to end of line<br>n=`1` clears from cursor to start of line<br>n=`2` clears entire line               |

- ESC`[?1049h` Включить альтернативный экранный буфер.
Это часто используется в текстовых редакторах, чтобы предоставить пользователю чистый экран для работы.
- ESC`[?1049l` Отключить альтернативный экранный буфер и вернуть содержимое основного экрана.
- ESC`[?1h` Включить режим "прямой печати". Некоторые терминалы могут обрабатывать это по-разному.
- ESC`[?1l` Отключить режим "прямой печати".
- ESC`[1;32;40m` устанавливает жирный зеленый текст на черном фоне.
- ESC`[3;5;7m` Вы можете комбинировать несколько атрибутов, чтобы,
например, сделать текст жирным, с курсивом и инверсным цветом.
- ESC`[0;31;47m` Это сброс всех атрибутов и установка красного текста на белом фоне.
- ESC`[X` Удаление символа в позиции курсора (может работать по-разному в зависимости от терминала).
- ESC`[P` Удаление символа, на который указывает курсор.
- `\007` Это код звукового сигнала (bell). При его использовании терминал издает звук.
- `\033[39m` Этот код сбрасывает цвет текста к цвету по умолчанию.
Если цвет текста был изменён, он вернётся к стандартному цвету терминала.
- ESC`]0;Title\007` Устанавливает заголовок окна терминала.
- ESC`]8;;<URL>ESC\` Создаёт кликабельную ссылку

```bash
echo -e "\033]8;;http://example.com\033\\Click Here\033]8;;\033\\"
```

```bash
echo -e "\033]0;My Terminal Window\007"
```


`Alt-f` - Переместить одно слово вправо
`Alt-b` - Переместить одно слово влево
`Alt-Backspace` - Удалить одно слово слева


<table>
  <thead>
    <tr>
      <th style="background: inherit; border: none;"></th>
      <th>Emacs keys</th>
      <th>Action</th>
      <th>Scope</th>
      <th>Direction/Place</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="7">Moving around</th>
      <td><code>Ctrl-b</code></td>
      <td>Move the cursor</td>
      <td>one character</td>
      <td>⇦ to the left</td>
    </tr>
    <tr>
      <td><code>Ctrl-f</code></td>
      <td>Move the cursor</td>
      <td>one character</td>
      <td>⇨ to the right</td>
    </tr>
    <tr>
      <td><code>Alt-b</code></td>
      <td>Move the cursor</td>
      <td>one word</td>
      <td>⇦ to the left</td>
    </tr>
    <tr>
      <td><code>Alt-f</code></td>
      <td>Move the cursor</td>
      <td>one word</td>
      <td>⇨ to the right</td>
    </tr>
    <tr>
      <td><code>Ctrl-a</code></td>
      <td>Move the cursor</td>
      <td></td>
      <td>⇤ to the start of the line</td>
    </tr>
    <tr>
      <td><code>Ctrl-e</code></td>
      <td>Move the cursor</td>
      <td></td>
      <td>⇥ to the end of the line</td>
    </tr>
    <tr>
      <td><code>Ctrl-x-x</code></td>
      <td>Move the cursor</td>
      <td></td>
      <td>⇤⇥ to the start, and to the end again<br></td>
    </tr>
  </tbody>
  <tbody>
    <tr>
      <th rowspan="8">Cut, copy<br>and paste</th>
      <td>Backspace</td>
      <td>Delete</td>
      <td>the character</td>
      <td>⇦ to the left of the cursor</td>
    </tr>
    <tr>
      <td>DEL<br><code>Ctrl-d</code></td>
      <td>Delete</td>
      <td>the character</td>
      <td>underneath the cursor</td>
    </tr>
    <tr>
      <td><code>Ctrl-u</code></td>
      <td>Delete</td>
      <td>everything</td>
      <td>⇤ from the cursor back to the line start</td>
    </tr>
    <tr>
      <td><code>Ctrl-k</code></td>
      <td>Delete</td>
      <td>everything</td>
      <td>⇥ from the cursor to the end of the line</td>
    </tr>
    <tr>
      <td><code>Alt-d</code></td>
      <td>Delete</td>
      <td>word</td>
      <td>⇨ untill before the next word boundary</td>
    </tr>
    <tr>
      <td><code>Ctrl-w</code></td>
      <td>Delete</td>
      <td>word</td>
      <td>⇦ untill after the previous word boundary</td>
    </tr>
    <tr>
      <td><code>Ctrl-y</code></td>
      <td>Yank/Paste</td>
      <td>prev. killed text</td>
      <td>at the cursor position</td>
    </tr>
    <tr>
      <td><code>Alt-y</code></td>
      <td>Yank/Paste</td>
      <td>prev. prev. killed text</td>
      <td>at the cursor position</td>
    </tr>
  </tbody>
  <tbody>
    <tr>
      <th rowspan="9">History</th>
      <td><code>Ctrl-p</code></td>
      <td>Move in history</td>
      <td>one line</td>
      <td>⇧ before this line</td>
    </tr>
    <tr>
      <td><code>Ctrl-n</code></td>
      <td>Move in history</td>
      <td>one line</td>
      <td>⇩ after this line</td>
    </tr>
    <tr>
      <td><code>Alt-&gt;</code></td>
      <td>Move in history</td>
      <td>all the lines</td>
      <td>⇩ to the line currently being entered</td>
    </tr>

    <tr>
      <td><code>Ctrl-r</code></td>
      <td colspan="2">Incrementally search the line history</td>
      <td>⇧ backwardly</td>
    </tr>

    <tr>
      <td><code>Ctrl-s</code></td>
      <td colspan="2">Incrementally search the line history</td>
      <td>⇩ forwardly</td>
    </tr>

    <tr>
      <td><code>Ctrl-J</code></td>
      <td colspan="3">End an incremental search</td>
    </tr>

    <tr>
      <td><code>Ctrl-G</code></td>
      <td colspan="3">Abort an incremental search and restore the original line</td>
    </tr>

    <tr>
      <td><code>Alt-Ctrl-y</code></td>
      <td>Yank/Paste</td>
      <td>arg. 1 of prev. cmnd</td>
      <td>at the cursor position</td>
    </tr>

    <tr>
      <td><code>Alt-.</code><br><code>Alt-_</code></td>
      <td>Yank/Paste</td>
      <td>last arg of prev. cmnd</td>
      <td>at the cursor position</td>
    </tr>
  </tbody>
  <tbody>
    <tr>
      <th rowspan="4">Undo</th>
      <td><code>Ctrl-_</code><br><code>Ctrl-x</code><br><code>Ctrl-u</code></td>
      <td colspan="3">Undo the last editing command; you can undo all the way back to an empty line</td>
    </tr>
    <tr>
      <td><code>Alt-r</code></td>
      <td colspan="3">Undo all changes made to this line</td>
    </tr>
    <tr>
      <td><code>Ctrl-l</code></td>
      <td colspan="3">Clear the screen, reprinting the current line at the top</td>
    </tr>
    <tr>
      <td><code>Ctrl-l</code></td>
      <td colspan="3">Clear the screen, reprinting the current line at the top</td>
    </tr>
  </tbody>
  <tbody>
    <tr>
      <th rowspan="4">Completion</th>
      <td>TAB</td>
      <td colspan="3">Auto-complete a name</td>
    </tr>
    <tr>
      <td><code>Alt-/</code></td>
      <td colspan="3">Auto-complete a name (without smart completion)</td>
    </tr>
    <tr>
      <td><code>Alt-?</code></td>
      <td colspan="3">List the possible completions of the preceeding text</td>
    </tr>
    <tr>
      <td><code>Alt-*</code></td>
      <td colspan="3">Insert all possible completions of the preceeding text</td>
    </tr>
  </tbody>
  <tbody>
    <tr>
      <th rowspan="2">Transpose</th>
      <td><code>Ctrl-t</code></td>
      <td>Transpose/drag</td>
      <td>char. before the cursor</td>
      <td>↷ over the character at the cursor</td>
    </tr>
    <tr>
      <td><code>Alt-t</code></td>
      <td>Transpose/drag</td>
      <td>word before the cursor</td>
      <td>↷ over the word at/after the cursor</td>
    </tr>
  </tbody>
</table>
