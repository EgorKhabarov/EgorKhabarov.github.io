**Tkinter** стандартная библиотека Python для создания графических пользовательских интерфейсов (GUI)
Она проста в использовании и подходит для создания небольших приложений с интерфейсом

Tkinter является встроенной библиотекой в Python, поэтому обычно не требует установки. Для проверки правильности установки можно запустить:

```bash
python -m tkinter
```

# Основные компоненты

## Основное окно (root)

Пример создания главного окна приложения
```python
import tkinter as tk

root = tk.Tk()
root.title("My App")
root.geometry("400x300")  # Установка размеров окна
root.mainloop()  # Запуск цикла обработки событий
```

## Виджеты (Widgets)

Tkinter предоставляет множество виджетов для создания интерфейса

| Виджет        | Описание                      | Пример использования                              |
|---------------|-------------------------------|---------------------------------------------------|
| `Label`       | Текстовая метка               | `label = tk.Label(root, text="Hello, Tkinter!")`  |
| `Button`      | Кнопка                        | `button = tk.Button(root, text="Click Me")`       |
| `Entry`       | Однострочное текстовое поле   | `entry = tk.Entry(root)`                          |
| `Text`        | Многострочное текстовое поле  | `text = tk.Text(root)`                            |
| `Checkbutton` | Флажок                        | `check = tk.Checkbutton(root, text="Check me")`   |
| `Radiobutton` | Переключатель                 | `radio = tk.Radiobutton(root, text="Option 1")`   |
| `Listbox`     | Список элементов              | `listbox = tk.Listbox(root)`                      |
| `Scale`       | Ползунок                      | `scale = tk.Scale(root, from_=0, to=100)`         |
| `Menu`        | Меню                          | Создается для окна или других виджетов            |
| `Canvas`      | Холст для рисования графики   | `canvas = tk.Canvas(root, width=400, height=300)` |
| `Frame`       | Контейнер для других виджетов | `frame = tk.Frame(root)`                          |
| `Scrollbar`   | Полоса прокрутки              | `scrollbar = tk.Scrollbar(root)`                  |

### Пример использования нескольких виджетов

```python
import tkinter as tk

root = tk.Tk()

label = tk.Label(root, text="Enter your name:")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Submit", command=lambda: print(entry.get()))
button.pack()

root.mainloop()
```

## Обработчики событий

Для того чтобы связывать события, такие как нажатие кнопки, с действиями в коде, используется параметр `command` для кнопок и других элементов

Пример с обработкой нажатия кнопки
```python
def on_button_click():
    print("Button clicked!")

button = tk.Button(root, text="Click Me", command=on_button_click)
button.pack()
```

## Организация виджетов

Tkinter предоставляет три метода для управления расположением виджетов: `pack`, `grid`, и `place`

### Метод `pack()`

Простой метод для последовательного размещения виджетов сверху вниз или слева направо
```python
label.pack(side="top")
button.pack(side="bottom")
```

### Метод `grid()`

Позволяет размещать виджеты в виде таблицы, указывая строки и столбцы
```python
label.grid(row=0, column=0)
entry.grid(row=0, column=1)
button.grid(row=1, column=1)
```

### Метод `place()`

Точный контроль над позицией виджета по координатам (x, y)
```python
button.place(x=50, y=100)
```

## Окна сообщений

Tkinter предоставляет модули для отображения окон сообщений

```python
from tkinter import messagebox

# Сообщение об ошибке
messagebox.showerror("Error", "Something went wrong!")

# Сообщение с подтверждением
messagebox.askquestion("Confirm", "Are you sure?")
```

## Меню

Меню можно добавить к главному окну с помощью виджета `Menu`

```python
menubar = tk.Menu(root)

# Создаем меню "File"
file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="New")
file_menu.add_command(label="Open")
file_menu.add_command(label="Save")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=file_menu)

# Устанавливаем меню в окно
root.config(menu=menubar)
```

## Работа с графикой (Canvas)

`Canvas` позволяет рисовать простые графические элементы: линии, овалы, прямоугольники, текст и изображения

```python
canvas = tk.Canvas(root, width=400, height=300)
canvas.pack()

# Рисование прямоугольника
canvas.create_rectangle(50, 50, 150, 150, fill="blue")

# Рисование круга
canvas.create_oval(200, 50, 300, 150, fill="green")

# Рисование текста
canvas.create_text(200, 200, text="Hello, Canvas", font=("Arial", 20))
```

## Полоса прокрутки (Scrollbar)

Полосы прокрутки могут быть добавлены к элементам `Listbox`, `Text`, или `Canvas`

Пример добавления полосы прокрутки к текстовому полю
```python
scrollbar = tk.Scrollbar(root)
scrollbar.pack(side="right", fill="y")

text = tk.Text(root, yscrollcommand=scrollbar.set)
text.pack(side="left", fill="both")

scrollbar.config(command=text.yview)
```

# Примеры
### Простое приложение

Создадим простое приложение для ввода текста и кнопки, которая выводит этот текст в консоль

```python
import tkinter as tk

def show_text():
    text = entry.get()
    print(f"You entered: {text}")

root = tk.Tk()
root.title("Simple App")

label = tk.Label(root, text="Enter some text:")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Submit", command=show_text)
button.pack()

root.mainloop()
```

### Калькулятор

```python
import tkinter as tk

def on_click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(screen.get())
            screen.set(result)
        except:
            screen.set("Error")
    elif text == "C":
        screen.set("")
    else:
        current = screen.get()
        screen.set(current + text)

root = tk.Tk()
root.geometry("400x600")
root.title("Calculator")

screen = tk.StringVar()
entry = tk.Entry(root, textvar=screen, font="Arial 20", bd=10, relief="sunken")
entry.pack(fill="both", ipadx=8, padx=10, pady=10)

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]

for row in buttons:
    frame = tk.Frame(root)
    frame.pack()
    for btn in row:
        button = tk.Button(frame, text=btn, font="Arial 18", padx=10, pady=10)
        button.pack(side="left", fill="both", expand=True)
        button.bind("<Button-1>", on_click)

root.mainloop()
```
