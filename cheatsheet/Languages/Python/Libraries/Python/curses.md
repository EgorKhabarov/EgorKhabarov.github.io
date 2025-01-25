### Шпаргалка по библиотеке **`curses`** в Python

**`curses`** — это модуль в Python для создания текстовых пользовательских интерфейсов (TUI) в терминалах
Он предоставляет функции для работы с окнами, цветами, клавишами, курсором и другой функциональностью терминалов

### **Основные функции библиотеки `curses`**

| Функция                                   | Описание                                                                                           | Пример использования                                        |
|-------------------------------------------|----------------------------------------------------------------------------------------------------|-------------------------------------------------------------|
| `initscr()`                               | Инициализирует экран, создавая объект главного окна                                                | `stdscr = curses.initscr()`                                 |
| `endwin()`                                | Восстанавливает работу терминала после завершения программы                                        | `curses.endwin()`                                           |
| `noecho()`                                | Отключает автоматический вывод вводимых символов на экран                                          | `curses.noecho()`                                           |
| `echo()`                                  | Включает вывод вводимых символов на экран                                                          | `curses.echo()`                                             |
| `cbreak()`                                | Включает режим `cbreak`, при котором ввод<br>передается программе без необходимости нажимать Enter | `curses.cbreak()`                                           |
| `nocbreak()`                              | Выключает режим `cbreak`                                                                           | `curses.nocbreak()`                                         |
| `keypad(window, True/False)`              | Включает или отключает обработку специальных<br>клавиш, таких как стрелки, F-клавиши и др          | `stdscr.keypad(True)`                                       |
| `curs_set(visibility)`                    | Устанавливает видимость курсора<br>(0 — невидим, 1 — видим, 2 — видим и жирный)                    | `curses.curs_set(0)`                                        |
| `start_color()`                           | Инициализирует работу с цветами                                                                    | `curses.start_color()`                                      |
| `init_pair(pair_number, fg, bg)`          | Устанавливает пару цветов для использования<br>(например, текст/фон)                               | `curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)` |
| `getch()`                                 | Читает один символ с клавиатуры                                                                    | `key = stdscr.getch()`                                      |
| `refresh()`                               | Обновляет экран для отображения изменений                                                          | `stdscr.refresh()`                                          |
| `clear()`                                 | Очищает экран                                                                                      | `stdscr.clear()`                                            |
| `newwin(nlines, ncols, begin_y, begin_x)` | Создает новое окно с заданными размерами и позицией                                                | `win = curses.newwin(10, 20, 5, 5)`                         |
| `addstr(y, x, string)`                    | Выводит строку на экране в указанной позиции                                                       | `stdscr.addstr(5, 5, "Hello World")`                        |
| `border()`                                | Рисует границу вокруг окна                                                                         | `win.border()`                                              |


### **Работа с цветами**

Чтобы использовать цвета в `curses`, необходимо сначала
инициализировать цветовой режим с помощью `start_color()` и создать пары цветов

```python
import curses

def main(stdscr):
    curses.start_color()  # Инициализация цветового режима
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)  # Пара цветов

    stdscr.addstr(0, 0, "Hello, World!", curses.color_pair(1))  # Использование цветовой пары
    stdscr.refresh()
    stdscr.getch()

curses.wrapper(main)
```

### **Управление окнами**

Вы можете создавать и управлять несколькими окнами с помощью `newwin()`

```python
import curses

def main(stdscr):
    # Создание нового окна
    win = curses.newwin(10, 40, 5, 5)  # Высота 10, ширина 40, позиция (5,5)
    win.border()  # Добавление границы вокруг окна
    win.addstr(1, 1, "This is a new window!")
    win.refresh()  # Обновление экрана

    stdscr.getch()

curses.wrapper(main)
```

### **Обработка клавиш**

`curses` поддерживает ввод с клавиатуры и специальные клавиши,
такие как стрелки, функциональные клавиши (F1, F2 и т.д.)

```python
import curses

def main(stdscr):
    stdscr.keypad(True)  # Включение обработки специальных клавиш
    stdscr.addstr("Press any key (ESC to exit)...")
    while True:
        key = stdscr.getch()
        if key == 27:  # ESC
            break
        stdscr.addstr(2, 0, f"Key pressed: {key}")
        stdscr.refresh()

curses.wrapper(main)
```

- **Некоторые специальные клавиши**
    - `curses.KEY_UP`: стрелка вверх
    - `curses.KEY_DOWN`: стрелка вниз
    - `curses.KEY_LEFT`: стрелка влево
    - `curses.KEY_RIGHT`: стрелка вправо
    - `curses.KEY_F1`, `curses.KEY_F2` и т.д.: функциональные клавиши F1, F2...

### **Пример программы с цветами и окнами**

Пример программы, которая создает два окна с разными цветами и выводит текст в них

```python
import curses

def main(stdscr):
    # Инициализация цветов
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)

    # Главное окно
    stdscr.addstr(0, 0, "Main window", curses.color_pair(1))

    # Создание нового окна
    win = curses.newwin(10, 40, 5, 5)
    win.border()
    win.addstr(1, 1, "Window with border", curses.color_pair(2))

    stdscr.refresh()
    win.refresh()

    stdscr.getch()

curses.wrapper(main)
```

### **Некоторые полезные функции и особенности**

| Функция                     | Описание                                                                                              |
|-----------------------------|-------------------------------------------------------------------------------------------------------|
| `curses.wrapper(func)`      | Запускает функцию с инициализацией и завершением `curses` окружения автоматически                     |
| `curses.newpad()`           | Создает "пад" (большой буфер экрана) для управления большими текстами, которые не помещаются на экран |
| `getmaxyx()`                | Возвращает максимальные размеры окна (высота и ширина)                                                |
| `curses.is_term_resized()`  | Проверяет, был ли изменен размер терминала                                                            |
| `curses.flash()`            | Визуальный сигнал, мигание экрана                                                                     |
| `curses.beep()`             | Аудиосигнал                                                                                           |
| `curses.textpad.Textbox()`  | Создает текстовое поле для редактирования текста                                                      |

### **Завершение работы с `curses`**

При завершении программы важно корректно выйти из режима `curses`,
чтобы терминал вернулся в нормальный режим
Обычно для этого вызывается `curses.endwin()`,
но использование `curses.wrapper()` автоматически обрабатывает завершение

### **Полезные ссылки**
[Документация `curses`](https://docs.python.org/3/library/curses.html)
