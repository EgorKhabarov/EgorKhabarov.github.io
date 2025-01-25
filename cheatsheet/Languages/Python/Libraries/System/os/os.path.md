| Функция/Метод                | Описание                                                            | Пример                                   |
|------------------------------|---------------------------------------------------------------------|------------------------------------------|
| `os.path.basename(path)`     | Возвращает имя файла из пути                                        | `os.path.basename("/path/to/file.txt")`  |
| `os.path.dirname(path)`      | Возвращает путь к директории без имени файла                        | `os.path.dirname("/path/to/file.txt")`   |
| `os.path.split(path)`        | Разделяет путь на кортеж `(dirname, basename)`                      | `os.path.split("/path/to/file.txt")`     |
| `os.path.splitext(path)`     | Разделяет путь на кортеж `(root, ext)` с корнем и расширением файла | `os.path.splitext("/path/to/file.txt")`  |
| `os.path.join(path, *paths)` | Соединяет компоненты пути в единый путь                             | `os.path.join("path", "to", "file.txt")` |
| `os.path.abspath(path)`      | Преобразует путь в абсолютный путь                                  | `os.path.abspath("file.txt")`            |
| `os.path.realpath(path)`     | Возвращает канонический путь, учитывая символические ссылки         | `os.path.realpath("symlink")`            |
| `os.path.exists(path)`       | Проверяет, существует ли путь                                       | `os.path.exists("file.txt")`             |
| `os.path.isfile(path)`       | Проверяет, является ли путь файлом                                  | `os.path.isfile("file.txt")`             |
| `os.path.isdir(path)`        | Проверяет, является ли путь директорией                             | `os.path.isdir("directory")`             |
| `os.path.getsize(path)`      | Возвращает размер файла в байтах                                    | `os.path.getsize("file.txt")`            |
| `os.path.abspath(path)`      | Возвращает абсолютный путь                                          | `os.path.abspath("file.txt")`            |
