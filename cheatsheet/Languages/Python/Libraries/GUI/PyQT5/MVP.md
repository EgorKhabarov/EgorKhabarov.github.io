minimum viable product

[https://itproger.com/course/python-pyqt5/2](https://itproger.com/course/python-pyqt5/2)

```python
import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow


def application():
    app = QApplication(sys.argv)
    window = QMainWindow()

    window.setWindowTitle("WindowTitle")
    window.setGeometry(300, 250, 500, 300)

    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()

```
