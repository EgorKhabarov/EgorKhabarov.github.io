Библиотека "pygetwindow" используется для управления окнами в операционной системе с помощью Python
Она предоставляет функции для поиска, получения информации о размерах и позиции окон, а также для управления их видимостью и активностью

Методы и подмодули библиотеки "pygetwindow":

`getAllTitles()`: Возвращает список заголовков всех открытых окон
`getWindowsWithTitle(title)`: Возвращает список окон с указанным заголовком
`getWindowGeometry(window)`: Возвращает геометрию (размеры и позицию) указанного окна
`getWindowAt(x, y)`: Возвращает окно, находящееся по указанным координатам
`getActiveWindow()`: Возвращает активное окно
`getWindowBorders(window)`: Возвращает границы указанного окна
`getWindowRect(window)`: Возвращает прямоугольник, охватывающий указанное окно
`getWindowPID(window)`: Возвращает идентификатор процесса, связанного с указанным окном
`getWindowProcessID(window)`: Возвращает идентификатор процесса, связанного с указанным окном
`getWindowThreadID(window)`: Возвращает идентификатор потока, связанного с указанным окном
`getWindowThreadProcessId(window)`: Возвращает идентификатор потока и процесса, связанных с указанным окном

Некоторые из самых часто используемых методов библиотеки "pygetwindow":

`getAllTitles()`: Возвращает список заголовков всех открытых окон

```python
import pygetwindow

window_titles = pygetwindow.getAllTitles()
print(window_titles)
```

`getWindowsWithTitle(title)`: Возвращает список окон с указанным заголовком

```python
import pygetwindow

windows = pygetwindow.getWindowsWithTitle("Notepad")
for window in windows:
    print(window.title)
```

`getActiveWindow()`: Возвращает активное окно

```python
import pygetwindow

active_window = pygetwindow.getActiveWindow()
print(active_window.title)
```

`getWindowGeometry(window)`: Возвращает геометрию (размеры и позицию) указанного окна

```python
import pygetwindow

window = pygetwindow.getWindowsWithTitle("Notepad")[0]
geometry = pygetwindow.getWindowGeometry(window)
print(geometry)
```

`getWindowRect(window)`: Возвращает прямоугольник, охватывающий указанное окно

```python
import pygetwindow

window = pygetwindow.getWindowsWithTitle("Notepad")[0]
rect = pygetwindow.getWindowRect(window)
print(rect)
```
