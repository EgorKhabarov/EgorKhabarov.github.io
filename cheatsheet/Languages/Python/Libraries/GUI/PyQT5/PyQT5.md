**PyQt5** набор привязок Python к инструментам Qt5,
который позволяет создавать кроссплатформенные графические пользовательские интерфейсы (GUI)

```bash
pip install pyqt5
```

# Основные классы
- QApplication - основной класс приложения
- QMainWindow - класс главного окна
- QLabel - метка для отображения текста

# Основные виджеты в PyQt5

| Виджет         | Описание                                      | Пример использования                                 |
|----------------|-----------------------------------------------|------------------------------------------------------|
| `QPushButton`  | Кнопка для взаимодействия с пользователем     | `button = QPushButton("Click Me", self)`             |
| `QLabel`       | Метка для отображения текста или изображений  | `label = QLabel("Hello World", self)`                |
| `QLineEdit`    | Поле для ввода текста                         | `line_edit = QLineEdit(self)`                        |
| `QCheckBox`    | Чекбокс (галочка)                             | `checkbox = QCheckBox("Check me", self)`             |
| `QRadioButton` | Радиокнопка для выбора одного из вариантов    | `radio_button = QRadioButton("Option 1", self)`      |
| `QComboBox`    | Выпадающий список                             | `combo_box = QComboBox(self)`                        |
| `QTextEdit`    | Многострочное поле для ввода текста           | `text_edit = QTextEdit(self)`                        |
| `QSlider`      | Ползунок для выбора числового значения        | `slider = QSlider(Qt.Horizontal, self)`              |
| `QProgressBar` | Прогресс-бар для отображения выполнения задач | `progress = QProgressBar(self)`                      |

# Работа с событиями

В PyQt5 каждый виджет может реагировать на различные события, такие как нажатие кнопок, изменение текста и т.д
Для обработки событий используются сигналы и слоты

```python
import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Создаем кнопку
        button = QPushButton("Нажми меня", self)
        button.clicked.connect(self.on_button_click)  # Привязываем сигнал к слоту

    def on_button_click(self):
        print("Кнопка была нажата")

app = QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec_())
```

Сигналы и слоты:

- `clicked.connect(slot)` - связывает сигнал с функцией-слотом
- Слот - это метод, который выполняется при наступлении события

# Макеты (Layouts)

Макеты в PyQt5 используются для управления размещением виджетов внутри окон

| Макет         | Описание                                           | Пример использования     |
|---------------|----------------------------------------------------|--------------------------|
| `QVBoxLayout` | Вертикальный макет                                 | `layout = QVBoxLayout()` |
| `QHBoxLayout` | Горизонтальный макет                               | `layout = QHBoxLayout()` |
| `QGridLayout` | Сетка для размещения виджетов в строках и столбцах | `layout = QGridLayout()` |
| `QFormLayout` | Макет для пар "метка - элемент ввода"              | `layout = QFormLayout()` |

Пример использования вертикального и горизонтального макетов

```python
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Вертикальный макет
        layout = QVBoxLayout()

        # Добавляем кнопки в макет
        layout.addWidget(QPushButton("Кнопка 1"))
        layout.addWidget(QPushButton("Кнопка 2"))
        layout.addWidget(QPushButton("Кнопка 3"))

        self.setLayout(layout)  # Применяем макет к виджету

app = QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec_())
```

# Работа с окнами сообщений

В PyQt5 можно показывать диалоговые окна сообщений

Пример: показ сообщения об ошибке

```python
from PyQt5.QtWidgets import QMessageBox

def show_error():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)
    msg.setText("Это ошибка!")
    msg.setWindowTitle("Ошибка")
    msg.exec_()

show_error()
```

# Работа с меню

Создание меню в PyQt5 осуществляется с помощью `QMenuBar`, `QMenu` и `QAction`

```python
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Создаем меню
        menu = self.menuBar()
        file_menu = menu.addMenu("Файл")

        # Добавляем действия в меню
        open_action = QAction("Открыть", self)
        file_menu.addAction(open_action)

        save_action = QAction("Сохранить", self)
        file_menu.addAction(save_action)

app = QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec_())
```

# Управление положением и размерами виджетов

Вы можете задавать размеры и положение виджетов вручную, либо с помощью макетов

- `move(x, y)` перемещает виджет
- `resize(width, height)` изменяет размер виджета

```python
button = QPushButton("Кнопка", self)
button.move(100, 100)  # Положение
button.resize(200, 50)  # Размер
```

# Обработка событий клавиатуры и мыши

PyQt5 предоставляет возможность обрабатывать события клавиатуры и мыши с помощью специальных методов

| Событие                | Метод                      |
|------------------------|----------------------------|
| Нажатие клавиши        | `keyPressEvent(event)`     |
| Отпускание клавиши     | `keyReleaseEvent(event)`   |
| Нажатие кнопки мыши    | `mousePressEvent(event)`   |
| Отпускание кнопки мыши | `mouseReleaseEvent(event)` |

Пример обработки нажатий клавиш

```python
class MyWindow(QMainWindow):
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()  # Закрытие окна по нажатию Esc
```

# Пример небольшого приложения

Пример приложения с кнопкой, текстовым полем и прогресс-баром

```python
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QProgressBar

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Пример приложения")

        # Макет
        layout = QVBoxLayout()

        # Текстовое поле
        self.line_edit = QLineEdit(self)
        layout.addWidget(self.line_edit)

        # Кнопка
        button = QPushButton("Нажми меня", self)
        button.clicked.connect(self.on_button_click)
        layout.addWidget(button)

        # Прогресс-бар
        self.progress_bar = QProgressBar(self)
        layout.addWidget(self.progress_bar)

        self.setLayout(layout)

    def on_button_click(self):
        text = self.line_edit.text()
        self.progress_bar.setValue(len(text) * 10)

app = QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec_())
```

# Полезные ссылки
- [Официальная документация PyQt5](https://riverbankcomputing.com/software/pyqt/intro)
- [Qt Designer для создания интерфейсов](https://build-system.fman.io/qt-designer-download)
