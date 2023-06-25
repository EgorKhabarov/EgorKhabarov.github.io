DICT = {
    "Общее": {
        "Парадигмы": {
            "Императивная": """
Разработчик пишет для компьютера инструкции, которым тот следует.

Виды программирования относятся к императивной парадигме:
процедурное структурное аспектно-ориентированное объектно-ориентированное и другие.

Пример
Сложи два числа;
Если а, то сделай б, а иначе сделай в;
Отправь запрос на сервер;
Открой файл;
Выведи строку.

C# - Разработчик говорит как это можно получить (императивный)

```C#
int[] N = new int[] { 5, 1, 3, 9, 12, 583, 998, 7538, 72, 53, 71, 85, 7, 2, 9 };
List<int> nums = new List<int>();
for(int i = 0; i < N.Length; i++) {
if(N[i] > 3 && N[i] < 100){nums.Add(N[i]);}}
int[] N2 = nums.ToArray();
```

Императивное программирование даёт больше свободы, поэтому его чаще используют
в творческих областях, особенно там, где важен порядок выполняемых действий.
""",
            "Декларативная": """
Разработчик описывает проблему и ожидаемый результат, но не пишет никаких инструкций.

В декларативном программировании отсутствуют переменные,
состояние и прочие понятия, которые свойственны императивной парадигме.

К декларативной парадигме относятся функциональное и логическое программирование.

Пример
Дано:    5, 1, 3, 9, 12, 583, 998, 7538, 72, 53, 71, 85, 7, 2, 9
Задача:  Получить из этого массива все числа, которые больше 3, но меньше 100.
Решение: Получить из массива N все числа, которые больше 3 и меньше 100.

SQL - Разработчик говорит, что ему нужно (декларативный)

```sql
SELECT num FROM N WHERE num > 3 AND num < 100;
```
Декларативное программирование — это обёртка для императивного.
Не подходит для задач, для решения которых важно иметь доступ к состоянию программы.
Например, если нужно проверить, нажата ли кнопка или поставлена ли галочка в чекбокс.
"""
        },
        "ООП": """
|              |                                                                                                                          |
|--------------|--------------------------------------------------------------------------------------------------------------------------|
| инкапсуляция | предназначена для изоляции контрактных обязательств абстракции<br>(протокол/интерфейс) от их реализации (public/private) |
| наследование | это когда тип данных может наследовать данные и<br>функциональность некоторого существующего типа                        |
| полиморфизм  | способность функции обрабатывать данные разных типов                                                                     |
| абстракция   | это процесс упрощения или скрытия сложной реальности,<br>чтобы сосредоточиться на наиболее важных аспектах.              |

В программировании, абстракция означает создание общей концепции, которая скрывает детали реализации, 
но предоставляет только необходимый набор функций и методов для взаимодействия с объектом. 
В итоге, абстракция помогает создавать более понятный, гибкий и расширяемый код.


Абстракция
Это процесс создания абстрактных классов и интерфейсов для представления концептуальных объектов и их взаимодействия в программе. 
Абстракция позволяет скрыть реализацию объектов и предоставить только необходимый набор свойств и методов для их использования. 
Это упрощает процесс разработки и поддержки программы, улучшает ее читаемость и расширяемость.

Например, в программе для управления банковским счетом можно создать абстрактный класс "Счет" со свойствами "номер счета" и "баланс", 
а также методами для внесения и снятия денег. 
Конкретные типы счетов, такие как "текущий счет" или "депозитный счет", могут быть созданы на основе этого абстрактного класса 
и расширены своими дополнительными свойствами и методами.
""",
        "Интерпретатор Компилятор": """
|               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Интерпретатор | Программа, которая читает и исполняет команды на другом языке программирования.<br>Он принимает код на этом языке, анализирует его, и выполняет инструкции,<br>указанные в коде.<br>Интерпретаторы часто используются для языков программирования, которые<br>поддерживают интерпретацию, таких как Python, Ruby и JavaScript.<br>Они также могут быть использованы для языков, которые обычно компилируются,<br>таких как C++ или C#, чтобы обеспечить более быструю отладку и тестирование кода                                                                                         |
| Компилятор    | Программа, которая преобразует код на одном языке программирования в машинный<br>язык, который может быть понят целевой машиной.<br>Компилятор анализирует код, выполняет необходимые преобразования, и создает<br>исполняемый файл, который содержит машинный код, готовый к выполнению.<br>Компиляторы часто используются для языков программирования, которые требуют<br>компиляции перед выполнением, таких как C++ или C#. Они также могут быть<br>использованы для языков, которые обычно интерпретируются, таких как<br>Python и Ruby, чтобы создать более быстро выполняемый код. |
""",
        "sync asyn": """
https://habr.com/ru/post/421625

|               |                                                                                                                                                                                                                                                                                    |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Синхронность  | Означает, что программа выполняет одну задачу за раз, поэтому она не может<br>выполнять несколько задач одновременно. Это означает, что если одна задача<br>занимает много времени, то все остальные задачи будут ждать,<br>пока эта задача не будет завершена.                    |
| Асинхронность | Означает, что программа может выполнять несколько задач одновременно.<br>Она может ожидать ответа от сервера и продолжать выполнение других задач<br>в то время, как она ждет. Это позволяет программе эффективно использовать<br>ресурсы и обрабатывать больше задач за один раз. |
""",
        "GIT": """
https://git-scm.com/

|                                                                  |
|------------------------------------------------------------------|
| git config --global user.name "EgorKhabarov"                     |
| git config --global user.email "not.a.fan.of.broccoli@gmail.com" |

|                            |                                        |
|----------------------------|----------------------------------------|
| git init                   | инициализация нового репозитория       |
| git clone [url]            | клонирование существующего репозитория |
| git add [file]             | добавление файла в индекс              |
| git commit -m "message"    | коммит с сообщением                    |
| git diff                   | просмотр изменений в файлах            |
| git status                 | просмотр текущего статуса репозитория<br>Tracked - файлы, о которых знает Git и которые добавляются в репозиторий.<br>Untracked - файлы, находящиеся в вашем рабочем каталоге, но не добавленные в репозиторий |
| git branch                   | просмотр списка веток                       |
| git checkout [branch/commit] | переключение на другую ветку/коммит         |
| git merge [branch]           | слияние ветки с текущей                     |
| git pull                     | получение и обновление удалённой ветки      |
| git push                     | отправка изменений на удалённый репозиторий |
| git log                      | просмотр истории коммитов                   |
| git reset [file]             | сброс индексации файла                      |
| git rm [file]                | удаление файла из репозитория               |
| mkdir [path]                 | сделать новый каталог             |
| cd [path]                    | изменяет текущий рабочий каталог  |
| git init                     | инициализировать Git в этой папке |
| git status                   | проверяем статус                  |
| git add [file_name]          | подготавливаем файл<br>Использование --all вместо отдельных имен файлов приведет к<br>stage изменению всех (новых, измененных и удаленных) файлов.<br>Сокращенная команда git add --all для git add -A |
| git status                   | проверяем статус |
| git commit -m "комментарий"  | подтверждаем     |



Git Commit без этапа
git status --short            увидеть изменения в более компактном виде
git commit -a -m "комментарий"
Обычно не рекомендуется пропускать промежуточную среду.
Пропуск этапа этапа иногда может привести к включению нежелательных изменений.


Новая ветка Git
Мы работаем в нашем локальном репозитории 
и не хотим нарушать или разрушать основной проект.

```bash
git branch name               создаем новый ветки
git checkout name             извлечение файла ветки
git commit -m "комментарий"   подтверждаем
```

Аварийное отделение
Теперь представьте, что мы еще не закончили с образами hello-world, 
но нам нужно исправить ошибку на master. Я не хочу связываться с master напрямую, 
и я не хочу связываться с образами hello-world, так как это еще не сделано.

```bash
git checkout -b emergency-fix создаем новую ветку для решения чрезвычайной ситуации
git status
git add name
git commit -m "комментарий"
```

Объединить ветки
У нас готово аварийное исправление, 
поэтому давайте объединим ветки master и Emergency-fix.
Во-первых, нам нужно перейти на ветку master:

```bash
git checkout master
git merge emergency-fix       объединяем текущую ветку (master) с Emergency-fix
git branch -d emergency-fix   удалить Emergency-Fix
```

Объединить конфликт

```bash
git checkout hello-world-images
git add --all
git commit -m "added new image"
```

<img alt="GIT.png" src="cheatsheet\Общее\GIT.png">
""",
        "HTTP": {
            "HTTР": """HTTP
(Hypertext Transfer Protocol)
Протокол для передачи гипертекстовых документов, таких как веб-страницы.
HTTPS (HTTP Secure) - это расширение HTTP, которое использует шифрование
данных для безопасной передачи информации между сервером и клиентом.
Протокол HTTPS использует те же методы, что и протокол HTTP,
такие как GET, POST, PUT, DELETE и т. д.
Однако в отличие от HTTP, HTTPS использует шифрование данных
для защиты информации во время передачи.
""",
            "Запросы": """
|        |            |
|--------|------------|
| GET    | Получение данных с сервера.<br>Не изменяют состояние сервера и обычно используются<br>для получения данных, не требующих аутентификации. |
| POST   | Отправки данных на сервер.<br>Используются для создания новых ресурсов или<br>изменения существующих ресурсов на сервере.                |
| PUT    | Обновления ресурса на сервере.<br>Заменяют текущий ресурс с указанным<br>идентификатором на новый ресурс.                                |
| DELETE | Удаления ресурса с сервера.<br>Удаляют ресурс с указанным идентификатором с сервера.                                                     |
""",
            "Протоколы связи": """
|                                                                 |                 |
|-----------------------------------------------------------------|-----------------|
| HTTP (Hypertext Transfer Protocol)                              | Протокол передачи гипертекста, который используется<br>для передачи веб-страниц и другого контента между сервером и клиентом в Интернете.<br>HTTP использует методы запроса-ответа между клиентом и сервером, где клиент отправляет запрос на сервер,<br>а сервер отправляет ответ с запрошенной информацией.<br>HTTP также поддерживает кэширование, что позволяет уменьшить количество передаваемых данных и ускорить загрузку страниц.                                                                                                                                                                |
| HTTPS (Hypertext Transfer Protocol Secure)                      | Это безопасная версия HTTP, которая использует шифрование SSL/TLS для защиты передаваемых данных от перехвата и подделки.<br>HTTPS добавляет дополнительный уровень безопасности в сравнении с HTTP и является необходимым<br>для обеспечения безопасной передачи конфиденциальной информации,<br>такой как пароли, номера кредитных карт и другие личные данные.                                                                                                                                                                                                                                        |
| SMTP (Simple Mail Transfer Protocol)                            | Протокол передачи почты, который используется для отправки электронной почты между почтовыми серверами.<br>SMTP работает на уровне приложения в модели OSI и использует порт 25 для обмена данными.<br>SMTP использует методы запроса-ответа, где отправитель отправляет сообщение на сервер,<br>а сервер затем доставляет сообщение получателю.                                                                                                                                                                                                                                                         |
| POP3 (Post Office Protocol version 3)                           | Протокол приема почты, который используется для получения электронной почты с сервера на клиентское устройство.<br>POP3 работает на уровне приложения и использует порт 110 для обмена данными.<br>Когда клиентский компьютер подключается к почтовому серверу,<br>POP3 загружает все письма с сервера на устройство, а затем удаляет их с сервера.                                                                                                                                                                                                                                                      |
| IMAP (Internet Message Access Protocol)                         | Протокол доступа к электронной почте, который также используется для получения электронной почты с сервера<br>на клиентское устройство, но предоставляет более продвинутые функции,<br>такие как хранение писем на сервере и синхронизация между устройствами.<br>IMAP работает на уровне приложения и использует порт 143 для обмена данными.<br>IMAP позволяет клиентам просматривать только заголовки писем или загружать их содержимое полностью,<br>а также удалять письма на сервере, не загружая их на устройство.                                                                                |
| TCP/IP<br>(Transmission Control Protocol/<br>Internet Protocol) | Это семейство протоколов, используемых для обмена данными в сети Интернет.<br>TCP отвечает за надежную передачу данных между приложениями,<br>установление и управление соединениями, а также контроль потока данных.<br>IP же отвечает за маршрутизацию пакетов данных между устройствами в сети,<br>идентификацию устройств, управление адресами и т.д.<br>TCP/IP также включает другие протоколы, такие как DNS (Domain Name System),<br>который переводит доменные имена в IP-адреса, и DHCP (Dynamic Host Configuration Protocol),<br>который автоматически назначает IP-адреса устройствам в сети. |
| FTP (File Transfer Protocol)                                    | Протокол передачи файлов, который используется для передачи файлов между компьютерами в сети.<br>FTP работает на уровне приложения и использует порт 21 для установки соединения и передачи команд,<br>а также порт 20 для передачи данных.<br>FTP позволяет пользователям загружать и скачивать файлы с сервера,<br>создавать и удалять директории и управлять правами доступа к файлам.                                                                                                                                                                                                                |
| SSH (Secure Shell)                                              | Протокол безопасной удаленной работы с командной строкой, который используется<br>для управления удаленными компьютерами и серверами.<br>SSH работает на уровне приложения и использует порт 22 для обмена данными.<br>SSH обеспечивает защиту от перехвата и подделки данных с помощью шифрования,<br>а также обеспечивает возможность удаленной аутентификации и управления устройством.                                                                                                                                                                                                               |
| DNS (Domain Name System)                                        | Протокол, который переводит доменные имена в IP-адреса и обратно.<br>DNS работает на уровне приложения и использует порт 53 для обмена данными.<br>DNS предоставляет возможность использования доменных имен для доступа к ресурсам<br>в сети вместо использования IP-адресов, что упрощает и облегчает работу сети.                                                                                                                                                                                                                                                                                     |
| SNMP (Simple Network Management Protocol)                       | Протокол управления сетью, который используется для мониторинга и управления сетевыми устройствами,<br>такими как маршрутизаторы, коммутаторы, серверы и т.д.<br>SNMP работает на уровне приложения и использует порты 161 и 162 для обмена данными.<br>SNMP позволяет администраторам мониторить статус устройств, настраивать их параметры и диагностировать проблемы в сети.                                                                                                                                                                                                                          |


"""
        },
    },
    "Языки": {
        "Python": {
            "Библиотеки": {
                "io": """
Библиотека io в Python предоставляет возможности работы с потоками ввода-вывода.

io.StringIO() - создание в памяти строкового потока.

```python
import io

stream = io.StringIO()
stream.write("Hello, world!")
stream.seek(0)
print(stream.read())  # Hello, world!
```

io.BytesIO() - создание в памяти потока байт.

```python
import io

stream = io.BytesIO()
stream.write(b"Hello, world!")
stream.seek(0)
print(stream.read())  # b'Hello, world!'
```

io.open() - открытие файла в нужном режиме.

```python
import io

with io.open("example.txt", "w") as f:
    f.write("Hello, world!")
    
with io.open("example.txt", "r") as f:
    print(f.read())  # Hello, world!
```

io.TextIOWrapper() - обертка для текстовых потоков.

```python
import io

with io.open("example.txt", "w") as f:
    wrapper = io.TextIOWrapper(f, encoding="utf-8")
    wrapper.write("Привет, мир!")
    
with io.open("example.txt", "r") as f:
    wrapper = io.TextIOWrapper(f, encoding="utf-8")
    print(wrapper.read())  # Привет, мир!
```

io.BufferedWriter() - буферизированный записывающий поток.

```python
import io

with io.open("example.txt", "wb") as f:
    writer = io.BufferedWriter(f)
    writer.write(b"Hello, world!")
    
with io.open("example.txt", "rb") as f:
    reader = io.BufferedReader(f)
    print(reader.read())  # b'Hello, world!'
```

io.BufferedReader() - буферизированный читающий поток.

```python
import io

with io.open("example.txt", "wb") as f:
    f.write(b"Hello, world!")
    
with io.open("example.txt", "rb") as f:
    reader = io.BufferedReader(f)
    print(reader.read())  # b'Hello, world!'
```

io.FileIO() - создание потока для работы с файлом в бинарном режиме.

```python
import io

with io.FileIO("example.txt", "w") as f:
    f.write(b"Hello, world!")
    
with io.FileIO("example.txt", "r") as f:
    print(f.read())  # b'Hello, world!'
```

io.TextIOBase() - базовый класс для всех текстовых потоков.

```python
import io

class UpperTextIO(io.TextIOBase):
    def __init__(self, stream):
        self._stream = stream
        
    def write(self, text):
        self._stream.write(text.upper())
        
with io.open("example.txt", "w") as f:
    wrapper = io.TextIOWrapper(f, encoding="utf-8")
    upper_wrapper = UpperTextIO(wrapper)
    upper_wrapper.write("hello, world!")
    wrapper.flush()
    
with io.open("example.txt", "r") as f:
    wrapper = io.TextIOWrapper(f, encoding="utf-8")
    print(wrapper.read())  # HELLO, WORLD!
```

io.StringIO.getvalue() - получение содержимого из строкового потока.

```python
import io

stream = io.StringIO()
stream.write("Hello, world!")
print(stream.getvalue())  # Hello, world!
```

io.BytesIO.getvalue() - получение содержимого из потока байт.

```python
import io

stream = io.BytesIO()
stream.write(b"Hello, world!")
print(stream.getvalue())  # b'Hello, world!'
```

io.TextIOWrapper.detach() - отсоединение потока от обертки.

```python
import io

with io.open("example.txt", "w") as f:
    wrapper = io.TextIOWrapper(f, encoding="utf-8")
    wrapper.write("Hello, world!")
    stream = wrapper.detach()
    stream.write(b"!!!")
    
with io.open("example.txt", "r") as f:
    wrapper = io.TextIOWrapper(f, encoding="utf-8")
    print(wrapper.read())  # Hello, world!!!
```

io.BufferedRandom() - буферизированный поток с произвольным доступом.

```python
import io

with io.open("example.txt", "wb") as f:
    writer = io.BufferedRandom(f)
    writer.write(b"Hello, world!")
    writer.flush()
    writer.seek(-6, io.SEEK_CUR)
    writer.write(b"Python!")
    
with io.open("example.txt", "rb") as f:
    reader = io.BufferedReader(f)
    print(reader.read())  # b'Hello, Python!'
```
""",
                "os": """
Получение информации о текущей директории:

```python
import os

print(os.getcwd())
```

Создание директории:

```python
import os

os.mkdir("new_dir")
```

Удаление директории:

```python
import os

os.rmdir("dir_to_remove")
```

Проверка наличия файла или директории:

```python
import os

if os.path.exists("file.txt"):
    print("File exists!")
    
if os.path.exists("dir"):
    print("Directory exists!")
```


Получение списка файлов в директории:
```python
import os

files = os.listdir("my_dir")
for file in files:
    print(file)
```

Переименование файла или директории:

```python
import os

os.rename("old_file.txt", "new_file.txt")
```

Удаление файла:

```python
import os

os.remove("file_to_remove.txt")
```

Получение информации о файле:

```python
import os

file_stat = os.stat("file.txt")

print("Size of file:", file_stat.st_size)
print("Last accessed time:", file_stat.st_atime)
```

Проверка, является ли путь директорией или файлом:

```python
import os

if os.path.isfile("my_file.txt"):
    print("This is a file!")
    
if os.path.isdir("my_file.txt"):
    print("This is a directory!")
```

Получение имени файла из пути:

```python
import os

print(os.path.basename("/my_dir/my_file.txt"))
```

Получение пути к директории из пути к файлу:

```python
import os

print(os.path.dirname("/my_dir/my_file.txt"))
```

Получение абсолютного пути:

```python
import os

print(os.path.abspath("my_dir/my_file.txt"))
```

Объединение путей:

```python
import os

print(os.path.join("/my_dir", "my_file.txt"))
```

Получение расширения файла:

```python
import os

print(os.path.splitext("my_file.txt")[1])
```

Получение списка всех поддиректорий в директории:

```python
import os

print([f.path for f in os.scandir("my_dir") if f.is_dir()])
```
""",
                "sys": r'''
sys.argv содержит список аргументов командной строки, переданных скрипту. 
Первый элемент списка (sys.argv[0]) является именем скрипта:

```python
import sys

# Передаем два аргумента при запуске скрипта:
# python myscript.py arg1 arg2
print(sys.argv[0])  # myscript.py
print(sys.argv[1])  # arg1
print(sys.argv[2])  # arg2
```

sys.exit() завершает выполнение программы. 
Можно передать код возврата, который будет использован в качестве кода завершения:

```python
import sys

# Завершаем программу с кодом 0
sys.exit(0)

# Завершаем программу с кодом ошибки 1
sys.exit(1)
```

sys.stdin - стандартный поток ввода
sys.stdout - стандартный поток вывода
sys.stderr - стандартный поток ошибок. 
Эти потоки могут быть перенаправлены в файлы или другие потоки ввода/вывода:

```python
import sys

# Читаем данные из стандартного потока ввода
data = sys.stdin.readline()

# Пишем данные в стандартный поток вывода
sys.stdout.write("Hello, world!\n")

# Пишем ошибки в стандартный поток ошибок
sys.stderr.write("Error occurred\n")
```

sys.platform содержит строку, которая идентифицирует операционную систему, на которой запущена программа:

```python
import sys

if sys.platform == "win32":
    print("Windows")
elif sys.platform == "linux":
    print("Linux")
elif sys.platform == "darwin":
    print("MacOS")
```

sys.getsizeof() возвращает размер объекта в байтах:

```python
import sys

a = [1, 2, 3]
print(sys.getsizeof(a)) # 88
```




sys.path содержит список путей, в которых Python ищет модули:

```python
import sys

print(sys.path)

"""
[
    '', 
    'C:\\Users\\Egor\\AppData\\Local\\Programs\\Python\\Python311\\python311.zip', 
    'C:\\Users\\Egor\\AppData\\Local\\Programs\\Python\\Python311\\DLLs', 
    'C:\\Users\\Egor\\AppData\\Local\\Programs\\Python\\Python311\\Lib', 
    'C:\\Users\\Egor\\AppData\\Local\\Programs\\Python\\Python311', 
    'C:\\Users\\Egor\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\site-packages'
]
"""
```

sys.getdefaultencoding() возвращает кодировку по умолчанию, используемую для строк в Python:

```python
import sys

print(sys.getdefaultencoding())  # utf-8
```

sys.getfilesystemencoding() возвращает кодировку, используемую файловой системой:

```python
import sys

print(sys.getfilesystemencoding())  # utf-8
```

sys.getwindowsversion() возвращает информацию о версии Windows, если программа запущена в Windows:

```python
import sys

if sys.platform == "win32":
    print(sys.getwindowsversion())

"""sys.getwindowsversion(major=10, minor=0, build=19044, platform=2, service_pack='')"""
```

sys.version содержит строку, которая содержит информацию о версии Python:

```python
import sys

print(sys.version)

"""3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)]"""
```

sys.modules содержит словарь, содержащий все импортированные модули:

```python
import sys
import math

print(sys.modules["math"])  # <module 'math' (built-in)>
```












sys.maxsize содержит максимальное значение целого числа, которое может быть использовано в Python:

```python
import sys

print(sys.maxsize)  # 9223372036854775807
```

sys.float_info содержит информацию о типе float в Python:

```python
import sys

print(sys.float_info)

"""sys.float_info(max=1.7976931348623157e+308, max_exp=1024, max_10_exp=308, min=2.2250738585072014e-308, min_exp=-1021, min_10_exp=-307, dig=15, mant_dig=53, epsilon=2.220446049250313e-16, radix=2, rounds=1)"""
```

sys.stdin.isatty(), sys.stdout.isatty(), sys.stderr.isatty()
sys.stdin.isatty(), sys.stdout.isatty(), и sys.stderr.isatty() возвращают True, 
если соответствующий поток является терминальным устройством (tty):

```python
import sys

if sys.stdin.isatty():
    print("stdin is a tty")
else:
    print("stdin is not a tty")

if sys.stdout.isatty():
    print("stdout is a tty")
else:
    print("stdout is not a tty")

if sys.stderr.isatty():
    print("stderr is a tty")
else:
    print("stderr is not a tty")
```

sys.getrecursionlimit() возвращает текущий предел рекурсии Python. sys.setrecursionlimit() устанавливает предел рекурсии Python:

```python
import sys

print(sys.getrecursionlimit())  # 1000

sys.setrecursionlimit(3000)
```

sys.settrace() устанавливает функцию обратного вызова для отслеживания исполнения кода Python:

```python
import sys

def trace_calls(frame, event, arg):
    if event == "call":
        print(frame.f_code.co_name)

    return trace_calls

sys.settrace(trace_calls)

def my_function():
    print("Hello, world!")

my_function()

sys.settrace(None)
```





sys.exc_info() возвращает кортеж из трех значений, представляющих текущее исключение, если оно присутствует:

```python
import sys

def divide(x, y):
    try:
        result = x / y
    except:
        print(sys.exc_info())

divide(1, 0)
```
''',
                "argparse": """
Библиотека argparse в Python позволяет легко создавать интерфейсы командной строки для ваших скриптов. 
Эта библиотека предоставляет механизмы для определения аргументов командной строки и автоматического 
генерирования справочной информации и сообщений об ошибках.

Вот несколько примеров использования библиотеки argparse в Python:
Простой скрипт

```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("echo", help="echo the string you use here")

args = parser.parse_args()
print(args.echo)
```

Для запуска скрипта нужно использовать команду

```
python script.py hello
```

Аргументы с флагами

```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--verbosity", help="increase output verbosity", action="store_true")

args = parser.parse_args()
if args.verbosity:
    print("verbosity turned on")
```

Для запуска скрипта нужно использовать команду

```
python script.py --verbosity
```

Опциональный аргумент

```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--number", help="enter a number", type=int)

args = parser.parse_args()
if args.number:
    print(args.number * 2)
```

Для запуска скрипта нужно использовать команду

```
python script.py --number 5
```

Обязательный аргумент

```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("filename", help="the name of the file to read")

args = parser.parse_args()
print(args.filename)
```

Для запуска скрипта нужно использовать команду

```
python script.py filename.txt
```

Группировка аргументов

```python
import argparse

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
group.add_argument("--verbose", help="increase output verbosity", action="store_true")
group.add_argument("--quiet", help="decrease output verbosity", action="store_true")

args = parser.parse_args()
if args.verbose:
    print("verbosity turned on")
elif args.quiet:
    print("verbosity turned off")
```

Для запуска скрипта нужно использовать команду

```
python script.py --verbose или python script.py --quiet
```




Позиционные аргументы с выбором

```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("operation", help="operation to perform", choices=["add", "sub", "mul", "div"])
parser.add_argument("num1", help="first number", type=int)
parser.add_argument("num2", help="second number", type=int)

args = parser.parse_args()
if args.operation == "add":
    print(args.num1 + args.num2)
elif args.operation == "sub":
    print(args.num1 - args.num2)
elif args.operation == "mul":
    print(args.num1 * args.num2)
else:
    print(args.num1 / args.num2)
```

Для запуска скрипта нужно использовать команду

```
python script.py add 5 3
```

Описание программы и аргументов

```python
import argparse

parser = argparse.ArgumentParser(description="A simple calculator program")
parser.add_argument("operation", help="operation to perform", choices=["add", "sub", "mul", "div"])
parser.add_argument("num1", help="first number", type=int)
parser.add_argument("num2", help="second number", type=int)

args = parser.parse_args()
if args.operation == "add":
    print(args.num1 + args.num2)
elif args.operation == "sub":
    print(args.num1 - args.num2)
elif args.operation == "mul":
    print(args.num1 * args.num2)
else:
    print(args.num1 / args.num2)
```

Для запуска скрипта нужно использовать команду: 

```
python script.py --help
```




Парсинг аргументов из файла

```python
import argparse

parser = argparse.ArgumentParser(fromfile_prefix_chars='@')
parser.add_argument("operation", help="operation to perform", choices=["add", "sub", "mul", "div"])
parser.add_argument("num1", help="first number", type=int)
parser.add_argument("num2", help="second number", type=int)

args = parser.parse_args(['@args.txt'])
if args.operation == "add":
    print(args.num1 + args.num2)
elif args.operation == "sub":
    print(args.num1 - args.num2)
elif args.operation == "mul":
    print(args.num1 * args.num2)
else:
    print(args.num1 / args.num2)
```

Для использования данного примера нужно создать файл "args.txt" со следующим содержимым

```
add 5 3
```

Затем, чтобы запустить скрипт, нужно использовать команду

```
python script.py @args.txt
```

Аргумент со значением по умолчанию

```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--verbosity", help="increase output verbosity", action="store_true")
parser.add_argument("--num", help="a number", type=int, default=5)

args = parser.parse_args()
if args.verbosity:
    print("verbosity turned on")
print(args.num * 2)
```

Для запуска скрипта нужно использовать команду

```
python script.py --verbosity --num 3
```

Поддержка субкоманд

```python
import argparse

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(title='subcommands', dest='subcommand')

parser_a = subparsers.add_parser('command_a', help='command a help')
parser_a.add_argument('foo', type=int, help='foo help')

parser_b = subparsers.add_parser('command_b', help='command b help')
parser_b.add_argument('--bar', type=str, help='bar help')

args = parser.parse_args()
if args.subcommand == 'command_a':
    print(args.foo)
else:
    print(args.bar)
```

Для запуска скрипта нужно использовать команду: 

```
python script.py command_a 5
```

или

```
python script.py command_b --bar test
```
""",
                "subprocess": r"""
Библиотека subprocess в Python используется для запуска новых процессов, подключения к существующим процессам, 
выполнения команд в командной строке и многого другого. 
Вот несколько примеров использования этой библиотеки:

Запуск команды в командной строке

```python
import subprocess

result = subprocess.run(['ls', '-l'], capture_output=True, text=True)
print(result.stdout)
```

В этом примере мы использовали метод run для выполнения команды ls -l в командной строке. 
Опция capture_output=True заставляет метод сохранять вывод команды, а опция text=True указывает, что мы ожидаем текстовый вывод.

Запуск команды с переменными окружения

```python
import subprocess

env = {'MYVAR': 'myvalue'}
result = subprocess.run(['env'], env=env, capture_output=True, text=True)
print(result.stdout)
В этом примере мы использовали опцию env для установки переменной окружения MYVAR 
со значением myvalue и выполнения команды env, которая отображает все переменные окружения.
```

Запуск процесса в фоновом режиме

```python
import subprocess

subprocess.Popen(['python', 'myscript.py'])
```

Этот пример запускает скрипт myscript.py в фоновом режиме.

Подключение к существующему процессу

```python
import subprocess

process = subprocess.Popen(['ssh', 'user@remotehost'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)

stdin_data = 'ls\n'
process.stdin.write(stdin_data.encode())

stdout_data = process.stdout.readline()
print(stdout_data)
```

Этот пример подключается к удаленному хосту по SSH и выполняет команду ls. 
Мы используем метод write для передачи данных в стандартный ввод процесса, а метод readline для чтения данных из его стандартного вывода.





Запуск команды с аргументами

```python
import subprocess

filename = 'example.txt'
result = subprocess.run(['wc', '-l', filename], capture_output=True, text=True)
print(result.stdout)
```

В этом примере мы использовали метод run для выполнения команды wc -l example.txt в командной строке. 
Мы передали аргументы команды в виде списка. 
Результат сохраняется в переменную result, а затем выводится на экран.

Получение кода возврата команды

```python
import subprocess

result = subprocess.run(['ls', 'nonexistent'], capture_output=True, text=True)
print(result.returncode)
```

В этом примере мы попытались выполнить команду ls nonexistent, которая должна завершиться с ошибкой, 
потому что файла nonexistent не существует. 
Мы использовали атрибут returncode объекта CompletedProcess, 
который содержит код возврата команды. 
В данном случае он равен 1, что означает ошибку.

Запуск команды с использованием shell

```python
import subprocess

result = subprocess.run('echo "Hello, world!"', shell=True, capture_output=True, text=True)
print(result.stdout)
```

В этом примере мы использовали опцию shell=True, чтобы выполнить команду echo "Hello, world!" через оболочку. 
Результат выводится на экран.

Запуск команды с заданием текущей директории

```python
import subprocess

result = subprocess.run(['ls'], cwd='/tmp', capture_output=True, text=True)
print(result.stdout)
```

В этом примере мы использовали опцию cwd для выполнения команды ls в директории /tmp. 
Результат выводится на экран.
""",
                "itertools": """Модуль itertools
Возвращает итератор, который генерирует бесконечный ряд чисел, начиная с start, с шагом step.

```python
from itertools import count

count(start=0, step=1)
```

Возвращает итератор, который бесконечно циклит элементы в iterable.

```python
from itertools import cycle

cycle(iterable)
```

Возвращает итератор, который генерирует все возможные перестановки 
элементов iterable с длиной r (по умолчанию длина равна длине iterable).
Если r задан, то выдаются только перестановки из r элементов.

```python
from itertools import permutations

permutations(iterable, r=None)
```

Возвращает итератор, который генерирует все возможные комбинации элементов iterable с длиной r.

```python
from itertools import combinations

combinations(iterable, r)
```

Возвращает итератор, который генерирует все возможные комбинации элементов iterable с длиной r, с повторением элементов.

```python
from itertools import combinations_with_replacement

combinations_with_replacement(iterable, r)
```

Возвращает итератор, который объединяет несколько итераторов в один.

```python
from itertools import chain

chain(*iterables)
```

Возвращает итератор, который объединяет элементы из каждого итератора в кортежи. 
Если итераторы разных длин, то элементы для дополнения берутся из fillvalue.

```python
from itertools import zip_longest

zip_longest(*iterables, fillvalue=None)
```

Возвращает итератор, который группирует элементы iterable по значениям функции key.

```python
from itertools import groupby

groupby(iterable, key=None)
```

Возвращает итератор, который выдаёт элементы из iterable, начиная с start, и заканчивая stop, с шагом step.

```python
from itertools import islice

islice(iterable, start, stop=None, step=1)
```

Возвращает итератор, который применяет функцию function к каждому элементу iterable, который представлен в виде кортежа.

```python
from itertools import starmap

starmap(function, iterable)
```

Возвращает итератор, который выдаёт все возможные пары (или кортежи) элементов из каждого из iterables. 
repeat определяет, сколько раз каждый итератор будет повторен.

```python
from itertools import product

product(*iterables, repeat=1)
```

Возвращает итератор, который выдаёт сумму (или другую комбинацию) элементов iterable, используя функцию func.

```python
from itertools import accumulate

accumulate(iterable, func=operator.add)
```

Возвращает итератор, который выдаёт элементы data, соответствующие истинным значениям selectors.

```python
from itertools import compress

compress(data, selectors)
```

Возвращает итератор, который выдаёт элементы iterable после первого элемента, для которого predicate вернёт ложное значение.

```python
from itertools import dropwhile

dropwhile(predicate, iterable)
```

Возвращает итератор, который выдаёт элементы iterable, для которых predicate вернёт ложное значение.

```python
from itertools import filterfalse

filterfalse(predicate, iterable)
```

Возвращает итератор, который выдаёт пары соседних элементов из iterable.

```python
from itertools import pairwise

pairwise(iterable)
```

Возвращает итератор, который выдаёт object times раз (бесконечное количество раз, если times не указан).

```python
from itertools import repeat

repeat(object, times=None)
```

Возвращает итератор, который выдаёт элементы iterable до первого элемента, для которого predicate вернёт ложное значение.

```python
from itertools import takewhile

takewhile(predicate, iterable)
```

Возвращает n независимых итераторов, каждый из которых может быть 
использован независимо для перебора элементов исходного iterable.

```python
from itertools import tee

tee(iterable, n=2)
```
""",
                "collections": """
Модуль collections в Python содержит различные удобные классы для работы с коллекциями (наборами объектов).
Некоторые из классов в модуле collections:

namedtuple - это класс-фабрика для создания именованных кортежей, которые представляют собой 
             неизменяемые объекты, похожие на обычные кортежи, но каждый элемент имеет уникальное имя.

deque - это двусторонняя очередь, которая позволяет эффективно добавлять и удалять элементы как с начала, так и с конца.

Counter - это класс, который позволяет подсчитывать количество каждого элемента в последовательности.
          Возвращает словарь, где каждый ключ представляет элемент последовательности, а значение - количество его вхождений в последовательность.

OrderedDict - это словарь, который запоминает порядок вставки элементов.
              Позволяет итерироваться по элементам в порядке, в котором они были добавлены в словарь.

defaultdict - это словарь, который возвращает значение по умолчанию, если ключ отсутствует.
              При создании defaultdict необходимо указать функцию, которая будет вызываться для возврата значения по умолчанию. 
              Этот класс часто используется для создания словарей с дефолтным значением или для группировки элементов по какому-то признаку.

ChainMap - это класс, который позволяет объединить несколько словарей в один.
           Он предоставляет удобный способ комбинирования нескольких словарей в один, без необходимости копирования элементов.

UserDict - это класс, который предоставляет интерфейс словаря, но позволяет наследоваться для создания собственных классов словарей.
           Он может быть использован для создания словарей с дополнительной логикой или специальным поведением.

Эти классы облегчают работу с коллекциями в Python и уменьшают необходимость писать большой и сложный код для выполнения стандартных задач.


namedtuple:

```python
from collections import namedtuple

# создаем именованный кортеж Point
Point = namedtuple('Point', ['x', 'y'])

# создаем экземпляр кортежа
p = Point(1, 2)

# обращаемся к полям кортежа по имени
print(p.x)  # выведет 1
print(p.y)  # выведет 2
```

deque:

```python
from collections import deque

# создаем пустую двустороннюю очередь
d = deque()

# добавляем элементы в очередь
d.append(1)
d.append(2)
d.append(3)

# удаляем элементы из очереди
print(d.pop())  # выведет 3
print(d.popleft())  # выведет 1

# выводим оставшиеся элементы в очереди
print(d)  # выведет deque([2])
```

Counter:

```python
from collections import Counter

# создаем счетчик
c = Counter('hello, world')

# выводим количество вхождений каждого символа
print(c)  # выведет Counter({'l': 3, 'o': 2, 'e': 1, 'h': 1, ',': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})

# выводим наиболее часто встречающиеся символы
print(c.most_common(2))  # выведет [('l', 3), ('o', 2)]
```

OrderedDict:

```python
from collections import OrderedDict

# создаем упорядоченный словарь
d = OrderedDict()

# добавляем элементы в словарь
d['a'] = 1
d['b'] = 2
d['c'] = 3

# выводим элементы в порядке их добавления
for k, v in d.items():
    print(k, v)
# выведет:
# a 1
# b 2
# c 3
```

defaultdict:

```python
from collections import defaultdict

# создаем словарь с дефолтным значением 0
d = defaultdict(int)

# добавляем элементы в словарь
d['a'] += 1
d['b'] += 2
d['c'] += 3

# выводим словарь
print(d)  # выведет defaultdict(<class 'int'>, {'a': 1, 'b': 2, 'c': 3})
```

ChainMap:

```python
from collections import ChainMap

# создаем два словаря
d1 = {'a': 1, 'b': 2}
d2 = {'b': 3, 'c': 4}

# объединяем словари в цепочку
d = ChainMap(d1, d2)

# выводим элементы словаря
print(d['a'])  # выведет 1
print(d['b'])  # выведет 2 (из d1, так как b в d1 появился раньше, чем в d2)
print(d['c'])  # выведет 4 (из d2)

# создаем новый словарь и добавляем его в цепочку
d3 = {'c': 5, 'd': 6}
d = d.new_child(d3)

# выводим элементы словаря
print(d['c'])  # выведет 5 (из d3, так как он добавлен в цепочку позже, чем d2)
print(d['d'])  # выведет 6 (из d3)
```


UserDict:

```python
from collections import UserDict

# создаем пользовательский словарь
d = UserDict({'a': 1, 'b': 2})

# добавляем элементы в словарь
d['c'] = 3

# выводим элементы словаря
print(d)  # выведет {'a': 1, 'b': 2, 'c': 3}
```

UserList:

```python
from collections import UserList

# создаем пользовательский список
l = UserList([1, 2, 3])

# добавляем элементы в список
l.append(4)

# выводим элементы списка
print(l)  # выведет [1, 2, 3, 4]
```

UserString:

```python
from collections import UserString

# создаем пользовательскую строку
s = UserString('hello, world')

# изменяем строку
s.data = s.data.upper()

# выводим строку
print(s)  # выведет HELLO, WORLD
```
""",
                "functools": '''
partial(func, *args, **kwargs)              возвращает новую функцию, которая является копией исходной функции func, 
                                            но с некоторыми аргументами, переданными как *args и **kwargs, заранее заданными.

reduce(func, iterable[, initializer])       применяет функцию func к первым двум элементам последовательности iterable, 
                                            затем применяет func к результату и следующему элементу, и так далее, пока не будет обработан весь список. 
                                            Если указан initializer, он используется как первый элемент в последовательности.

cache(func)                                 декоратор, который кэширует результаты вызовов функции func с одинаковыми аргументами, чтобы избежать повторных вычислений.

wraps(wrapped[, assigned[, updated]])       декоратор, который копирует информацию об исходной функции wrapped в декорированную функцию. 
                                            Это позволяет сохранить метаданные, такие как имя функции, документацию и атрибуты.

total_ordering(cls)                         декоратор, который автоматически генерирует методы сравнения объектов 
                                            для класса cls на основе определения методов __eq__() и __lt__().

cmp_to_key(func)                            преобразует функцию func для использования в функциях сортировки. 
                                            Функция func(a, b) должна возвращать число, которое указывает порядок элементов a и b.

partialmethod(func, *args, **kwargs)        возвращает частичный метод, который может быть вызван как метод экземпляра класса. 
                                            Аргумент func должен быть методом класса.
                                            
lru_cache                                   декоратор реализует механизм кеширования результатов функции с помощью алгоритма "Least Recently Used" (LRU).

partial(func, *args, **kwargs)  
Возвращает новую функцию, которая является копией исходной функции func, 
но с некоторыми аргументами, переданными как *args и **kwargs, заранее заданными.

```python
from functools import partial

def power(base, exponent)
    return base ** exponent

# Создаем функцию возведения в квадрат, используя partial
square = partial(power, exponent=2)

# Вызываем функции
print(square(2))  # Output: 4
print(square(3))  # Output: 9
```

reduce(func, iterable[, initializer]) 
Применяет функцию func к первым двум элементам последовательности iterable, затем применяет func к результату и следующему элементу, 
и так далее, пока не будет обработан весь список. Если указан initializer, он используется как первый элемент в последовательности.

```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Найдем произведение всех чисел в списке
product = reduce(lambda x, y: x*y, numbers)

print(product)  # Output: 120
```

cache(func): 
Декоратор, который кэширует результаты вызовов функции func с одинаковыми аргументами, чтобы избежать повторных вычислений.

```python
from functools import cache

@cache
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))  # Output: 120
```

wraps(wrapped[, assigned[, updated]]) 
Декоратор, который копирует информацию об исходной функции wrapped в декорированную функцию. 
Это позволяет сохранить метаданные, такие как имя функции, документацию и атрибуты.
| сохраняет имя и документацию функции так как обычный декоратор заменяет собой функцию

```python
from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Calling function:", func.__name__)
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def my_function():
    """This is my function."""
    print("Hello, World!")

print(my_function.__name__)  # Output: my_function
print(my_function.__doc__)   # Output: This is my function.
```

```python-console
>>> def dec(f):
...     def w(x, y):
...         return f(x, y)
...     return w
...
>>> @dec
... def foo(x, y):
...     """comment"""
...     return x + y
...
>>> foo
<function dec.<locals>.w at 0x00000182FB1982C0>
>>> foo.__name__
'w'
>>> from functools import wraps
>>> def dec(f):
...     @wraps(f)
...     def w(x, y):
...         return f(x, y)
...     return w
...
>>> @dec
... def foo(x, y):
...     """comment"""
...     return x + y
...
>>> foo
<function foo at 0x00000182FB198400>
>>> foo.__name__
'foo'
>>>
```

total_ordering(cls) 
Декоратор, который автоматически генерирует методы сравнения объектов 
для класса cls на основе определения методов __eq__() и __lt__().

```python
from functools import total_ordering

@total_ordering
class Person:
    def __init__(self, name, age):
        self.name = name
    def __eq__(self, other):
        return self.age == other.age
    
    def __lt__(self, other):
        return self.age < other.age

person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

print(person1 == person2)  # Output: False
print(person1 != person2)  # Output: True
print(person1 < person2)   # Output: True
print(person1 > person2)   # Output: False
```

cmp_to_key(cmp) 
Преобразует функцию сравнения cmp в ключ-функцию, которая может быть использована для сортировки объектов. 
Эта функция полезна, когда необходимо отсортировать список объектов с использованием пользовательской функции сравнения.

```python
from functools import cmp_to_key

def my_cmp(a, b):
    if a < b:
        return -1
    elif a > b:
        return 1
    else:
        return 0

numbers = [4, 2, 7, 1, 3]

sorted_numbers = sorted(numbers, key=cmp_to_key(my_cmp))

print(sorted_numbers)  # Output: [1, 2, 3, 4, 7]
```





lru_cache — это декоратор в модуле functools в Python, который реализует 
механизм кеширования результатов функции с помощью алгоритма "Least Recently Used" (LRU).

LRU-кеширование позволяет сохранять недавно использованные результаты функции в кеше, 
чтобы повторно использовать их при последующих вызовах функции с теми же параметрами. 
Когда кеш заполнен до определенной максимальной величины, самые редко используемые 
элементы будут удалены из кеша, чтобы освободить место для новых элементов.

Для использования lru_cache необходимо импортировать модуль functools и применить декоратор @functools.lru_cache() к функции, 
которую нужно кешировать. Опционально можно передать в декоратор максимальное количество 
элементов в кеше (maxsize). Если параметр не задан, по умолчанию используется maxsize=128.

Например, вот как можно использовать lru_cache для кеширования результата функции fibonacci(n):

```python
from functools import lru_cache

@lru_cache(maxsize=128)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
```

Этот код создает кеш для fibonacci с максимальным размером 128 элементов. 
При вызове fibonacci(n) для любого n, результат будет сохранен в кеше. 
При повторном вызове fibonacci(n) с тем же n, результат будет возвращен из кеша без повторного вычисления.
''',
                "contextlib": """
Модуль contextlib - это стандартная библиотека Python, который содержит утилиты для работы с контекстными менеджерами.
Контекстные менеджеры могут использоваться, например, для управления ресурсами, такими как файлы или сетевые соединения.



#### contextlib.contextmanager
Декоратор превращает генераторную функцию в контекстный менеджер. 
Генератор должен содержать точку входа и выхода из контекста.

```python
import contextlib

@contextlib.contextmanager
def my_context():
    print("Entering context")
    yield
    print("Exiting context")

with my_context():
    print("Inside context")
```

В этом примере my_context() - это контекстный менеджер, который выводит сообщения при входе и выходе из контекста.



#### contextlib.suppress
это контекстный менеджер, который подавляет указанные исключения. 
Он используется, когда вы хотите, чтобы программа продолжала работать даже при возникновении определенных ошибок. 
Пример использования:

```python
import contextlib

with contextlib.suppress(FileNotFoundError):
    with open('non_existent_file.txt', 'r') as f:
        print(f.read())
```

В этом примере suppress используется для подавления исключения FileNotFoundError, 
которое возникает, если файл non_existent_file.txt не найден. 
Вместо того, чтобы возбудить исключение, программа продолжит работу без выполнения блока кода внутри with выражения.


#### contextlib.redirect_stdout и contextlib.redirect_stderr
эти контекстные менеджеры перенаправляют стандартный вывод и стандартный вывод ошибок соответственно в файл или объект. 
Пример использования:

```python
import contextlib
import io

with io.StringIO() as output:
    with contextlib.redirect_stdout(output):
        print("Hello, world!")
    contents = output.getvalue()

print(contents)
```

В этом примере стандартный вывод перенаправляется в объект io.StringIO(), 
а затем содержимое этого объекта выводится на экран.

Модуль contextlib содержит и другие функции, такие как closing, nullcontext и ExitStack. 
Они все предназначены для упрощения работы с контекстными менеджерами в Python.










#### contextlib.closing
Это функция, которая превращает объект с методом close() в контекстный менеджер. 
Это может быть полезно, например, для работы с файлами или соединениями. 
Пример использования:

```python
import contextlib
from urllib.request import urlopen

with contextlib.closing(urlopen('https:&sol;&sol;www.example.com/')) as page:
    for line in page:
        print(line.decode('utf-8'))
```

В этом примере urlopen('https:&sol;&sol;www.example.com/') возвращает объект с методом close(), 
который используется внутри контекстного менеджера closing.



#### contextlib.nullcontext
Это класс, который предоставляет пустой контекстный менеджер, который не делает ничего. 
Он может быть использован, когда нужен контекстный менеджер, 
но никакой реальной работы в контексте выполнять не требуется. 
Пример использования:

```python
import contextlib

with contextlib.nullcontext():
    print("Hello, world!")
```

В этом примере ничего не происходит в контексте, но благодаря использованию nullcontext, 
код работает корректно в рамках контекстного менеджера.


#### contextlib.ExitStack
Это класс, который предоставляет возможность управления несколькими контекстными менеджерами одновременно. 
Он может быть использован, когда требуется обеспечить надежное управление ресурсами в случае, 
когда ресурсы могут быть открыты и закрыты в произвольном порядке. 
Пример использования:

```python
import contextlib

with contextlib.ExitStack() as stack:
    files = [stack.enter_context(open(f)) for f in ['file1.txt', 'file2.txt', 'file3.txt']]
    for file in files:
        print(file.readline())
```

В этом примере ExitStack используется для управления тремя файлами, которые могут быть открыты и закрыты в любом порядке. 
Функция stack.enter_context(open(f)) добавляет каждый файл в стек контекстных менеджеров, 
который гарантирует их правильное закрытие в конце работы с ними.
""",
                "difflib": r'''
#### SequenceMatcher
Сравнение двух последовательностей и определение степени их сходства.

```python
import difflib

s1 = "Hello, world!"
s2 = "Hello, everyone!"

matcher = difflib.SequenceMatcher(None, s1, s2)
ratio = matcher.ratio()

print(f"Similarity ratio: {ratio}")

"""Similarity ratio: 0.6206896551724138"""
```


#### get_close_matches
Нахождение наиболее похожей строки в наборе строк на основе заданной строки.

```python
import difflib

colors = ['red', 'green', 'blue', 'yellow']
color = 'grea'

matches = difflib.get_close_matches(color, colors)

print(f"Closest matches: {matches}")

"""Closest matches: ['green']"""
```


#### unified_diff
Генерация отчета о различиях между двумя последовательностями.

```python
import difflib

text1 = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."""

text2 = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magnus aliqua."""

d = difflib.unified_diff(text1.splitlines(), text2.splitlines())

print('\n'.join(d))

"""
---

+++

@@ -1,3 +1,3 @@

 Lorem ipsum dolor sit amet,
 consectetur adipiscing elit,
-sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
+sed do eiusmod tempor incididunt ut labore et dolore magnus aliqua.
"""
```

#### HtmlDiff
Генерация отчета о различиях между двумя последовательностями в формате HTML.

```python
import difflib

text1 = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."""

text2 = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magnus aliqua."""

d = difflib.HtmlDiff().make_file(text1.splitlines(), text2.splitlines())

with open('diff.html', 'w') as f:
    f.writelines(d)
```














#### context_diff
Генерация отчета о различиях между двумя последовательностями в формате context diff.

```python
import difflib

text1 = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."""

text2 = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magnus aliqua."""

d = difflib.context_diff(text1.splitlines(), text2.splitlines())

print('\n'.join(d))

"""
***

---

***************

*** 1,3 ****

  Lorem ipsum dolor sit amet,
  consectetur adipiscing elit,
! sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
--- 1,3 ----

  Lorem ipsum dolor sit amet,
  consectetur adipiscing elit,
! sed do eiusmod tempor incididunt ut labore et dolore magnus aliqua.
"""
```

#### ndiff
Генерация отчета о различиях между двумя последовательностями в формате ndiff.

```python
import difflib

text1 = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."""

text2 = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magnus aliqua."""

d = difflib.ndiff(text1.splitlines(), text2.splitlines())

print('\n'.join(d))

"""
  Lorem ipsum dolor sit amet,
  consectetur adipiscing elit,
- sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
?                                                          ^

+ sed do eiusmod tempor incididunt ut labore et dolore magnus aliqua.
?                                                          ^^       
"""
```

#### isjunk и ignore
Использование пользовательских функций для игнорирования символов при сравнении последовательностей.

```python
import difflib

def isjunk(s):
    return s in [' ', '\n']

text1 = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."""

text2 = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magnus aliqua."""

matcher = difflib.SequenceMatcher(isjunk, text1, text2)
ratio = matcher.ratio()

print(f"Similarity ratio: {ratio}")

"""Similarity ratio: 0.9878542510121457"""
```

#### reduce_func
Использование пользовательской функции для преобразования различий в отчете о сравнении.

```python
import difflib

text1 = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."""

text2 = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magnus aliqua."""

d = difflib.Differ()
diff = d.compare(text1.splitlines(), text2.splitlines())

def reduce_func(s):
    if s.startswith('- '):
        return f"<span style='color:red'>{s}</span>"
    elif s.startswith('+ '):
        return f"<span style='color:green'>{s}</span>"
    else:
        return s

diff = map(reduce_func, diff)
diff = '\n'.join(diff)

print(diff)

"""
  Lorem ipsum dolor sit amet,
  consectetur adipiscing elit,
<span style='color:red'>- sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</span>
?                                                          ^

<span style='color:green'>+ sed do eiusmod tempor incididunt ut labore et dolore magnus aliqua.</span>
?                                                          ^^                                         
"""
```
''',
                "random": """
Модуль random в Python предоставляет функции для генерации случайных чисел и последовательностей. 
Ниже приведен список некоторых из наиболее часто используемых функций:

random()                       - возвращает случайное число с плавающей запятой в диапазоне [0.0, 1.0).
randint(a, b)                  - возвращает случайное целое число в диапазоне [a, b], включая границы.
uniform(a, b)                  - возвращает случайное число с плавающей запятой в диапазоне [a, b).
randrange(start, stop[, step]) - возвращает случайный элемент из диапазона, созданного с использованием аргументов start, stop и step.
choice(seq)                    - возвращает случайный элемент из последовательности seq.
shuffle(seq)                   - перемешивает элементы последовательности seq в произвольном порядке.
sample(population, k)          - возвращает список длиной k из уникальных элементов случайно выбранных из population.

getstate() и setstate(state)   - используются для сохранения и восстановления внутреннего состояния генератора случайных чисел. 
                                 Состояние генератора включает в себя информацию, необходимую для воспроизведения последовательности случайных чисел.
getrandbits(k)                 - возвращает целое число, состоящее из k случайных битов.
choices(population, weights=None, *, cum_weights=None, k=1) 
                               - выбирает k элементов из population с возможностью задания весов для каждого элемента. 
                                 Функция может использоваться для случайной выборки элементов с заменой из набора данных, 
                                 где некоторые элементы могут быть выбраны чаще, чем другие.
randbytes(n) - возвращает n случайных байтов.

Это только некоторые функции, доступные в модуле random. 
Существует также много других функций, таких как seed(), gauss(), triangular(), betavariate(), expovariate() и многие другие. 
Вы можете получить дополнительную информацию о модуле random и его функциях в официальной документации Python.
""",
                "decimal": """
from decimal import Decimal

Библиотека decimal предоставляет более точный способ работы с десятичными числами, чем встроенные типы данных float и double. 
Она позволяет представлять числа с фиксированной точностью и позволяет управлять точностью вычислений. 
Это может быть полезно в тех случаях, когда требуется точный результат, например, при финансовых расчетах.

Класс Decimal
Класс Decimal используется для создания и работы с десятичными числами с фиксированной точностью. Вот несколько примеров:i

```python
from decimal import Decimal

# Создание десятичного числа
a = Decimal('10.5')

# Арифметические операции
b = Decimal('2')
a + b # 12.5
a - b # 8.5
a * b # 21.0
a / b # 5.25

# Округление
a.quantize(Decimal('1.00')) # 10.50
a.quantize(Decimal('0.1'))  # 10.5

# Преобразование в разные форматы
a.to_eng_string()    # '10.5'
a.as_integer_ratio() # (21, 2)
```

Класс Context
Класс Context представляет контекст округления, который управляет поведением операций с десятичными числами. Вот несколько примеров:

```python
from decimal import Decimal, Context

# Создание контекста округления
ctx = Context(prec=3, rounding=ROUND_HALF_UP)

# Создание десятичного числа с использованием контекста
a = Decimal('10.5', context=ctx)

# Арифметические операции с использованием контекста
b = Decimal('2', context=ctx)
c = a + b
d = a - b
e = a * b
f = a / b

# Округление с использованием контекста
g = a.quantize(Decimal('1.00'), context=ctx)
h = a.quantize(Decimal('0.1'), context=ctx)
```

Функции округления
Модуль decimal также предоставляет несколько функций округления, которые можно использовать с десятичными числами. Вот несколько примеров:

```python
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_DOWN, ROUND_CEILING, ROUND_FLOOR

a = Decimal('10.555')

# Округление до двух знаков с округлением до ближайшего
a.quantize(Decimal('1.00'), rounding=ROUND_HALF_UP) # 10.56    

# Округление до двух знаков с округлением в меньшую сторону
a.quantize(Decimal('1.00'), rounding=ROUND_FLOOR)   # 10.55

# Округление до целого числа, округление до ближайшего
a.quantize(Decimal('1'), rounding=ROUND_HALF_UP)    # 11

# Округление до целого числа, округление в большую сторону
a.quantize(Decimal('1'), rounding=ROUND_CEILING)    # 11
```
""",
                "fractions": """
from fractions import Fraction

Модуль fractions предоставляет класс Fraction, который позволяет работать с дробными числами в виде объектов.
Класс Fraction позволяет представлять дробное число в виде числителя и знаменателя. 
Он автоматически упрощает дробь, позволяет выполнять арифметические операции с дробями 
и конвертировать дроби в различные форматы (например, вещественные числа или строки).

Вот примеры использования класса Fraction:

```python
from fractions import Fraction

# создание дроби с помощью числителя и знаменателя
print(Fraction(3, 4))    # вывод: 3/4

# создание дроби из вещественного числа
print(Fraction(0.5))    # вывод: 1/2

# арифметические операции с дробями
print(Fraction(1, 4) + Fraction(1, 2))    # вывод: 3/4

# конвертирование дроби в вещественное число
print(float(Fraction(3, 4)))    # вывод: 0.75

# конвертирование дроби в строку
print(str(Fraction(3, 4)))    # вывод: '3/4'
```

Класс Fraction может быть полезен в тех случаях, когда требуется более точный 
и удобный способ работы с дробными числами, чем встроенные типы данных. 
Он может использоваться, например, при работе с финансовыми расчетами, 
при расчете вероятностей или в других задачах, связанных с математикой.





Fraction   
Класс для представления рациональных чисел. 
Этот класс позволяет создавать объекты, которые представляют дроби в виде числителя и знаменателя. 
Например, Fraction(3, 4) создаст дробь 3/4.

```python
from fractions import Fraction

print(Fraction(3, 4) + Fraction(1, 2))  # выводит 5/4
```

gcd

Функция для вычисления наибольшего общего делителя двух чисел.

```python
from fractions import gcd

print(gcd(6, 9))  # выводит 3
```

lcm
Функция для вычисления наименьшего общего кратного двух чисел.

```python
from fractions import lcm

print(lcm(6, 9))  # выводит 18
```

limit_denominator
Метод объекта Fraction, который позволяет получить рациональное число, 
ближайшее к данному, с знаменателем не превосходящим указанное значение.

```python
from fractions import Fraction

print(Fraction(7, 12).limit_denominator(5))  # выводит 3/5
```

Fraction.from_float
Метод класса Fraction, который позволяет создать рациональное число, 
представляющее указанное число с плавающей точкой.

```python
from fractions import Fraction

print(Fraction.from_float(0.5))  # выводит 1/2
```

Fraction.from_decimal
Метод класса Fraction, который позволяет создать рациональное число, представляющее указанное десятичное число.

```python
from fractions import Fraction

print(Fraction.from_decimal('0.75'))  # выводит 3/4
```

is_integer
Метод объекта Fraction, который возвращает True, если данная дробь представляет целое число, и False в противном случае.

```python
from fractions import Fraction

print(Fraction(3, 2).is_integer())  # выводит False
print(Fraction(6, 4).is_integer())  # выводит True
```

Fraction.as_integer_ratio
Метод объекта Fraction, который возвращает кортеж из двух целых чисел, 
представляющих данную дробь в виде несократимой простой дроби.

```python
from fractions import Fraction

print(Fraction(5, 15).as_integer_ratio())  # выводит (1, 3)
```

Fraction.from_ratio
Метод класса Fraction, который позволяет создать рациональное число на основе заданного отношения двух целых чисел.

```python
from fractions import Fraction

print(Fraction.from_ratio(5, 15))  # выводит 1/3
```

Fraction.limit_denominator(max_denominator=1000000): 
Метод объекта Fraction, который возвращает рациональное число, ближайшее к данному, 
с знаменателем не превосходящим указанное значение. 
Если аргумент max_denominator не указан, то по умолчанию он равен 1 миллиону.

```python
from fractions import Fraction

print(Fraction(3, 4).limit_denominator(10))  # выводит 1/1
```

Fraction.from_jedec
Метод класса Fraction, который позволяет создать рациональное число на основе заданной строки в формате JEDEC.

```python
from fractions import Fraction

print(Fraction.from_jedec('1/2'))  # выводит 1/2
```

Fraction.from_tuple
Метод класса Fraction, который позволяет создать рациональное число на основе заданного кортежа из двух целых чисел (числителя и знаменателя).

```python
from fractions import Fraction

print(Fraction.from_tuple((3, 4)))  # выводит 3/4
```
""",
                "Django": {
                    "Команды": """
Запустить сервер

```
./manage.py runserver
```

Создать Django проект

```
django-admin startproject PROJECTNAME
```

Перейти в папку с этим проектом

```
cd PROJECTNAME
```

Создать приложение (App)

```
./manage.py startapp APPNAME
```

Сделать миграцию (изменение в базе данных)

```
./manage.py makemigrations
./manage.py migrate
```

Создать админа

```
./manage.py createsuperuser
```
"""
                },
                "logging": """import logging

Запись в файл

```python
logging.basicConfig(filename='example.log',
                    level=logging.DEBUG)
```

Запись в консоль

```python
logging.basicConfig(level=logging.DEBUG,
                    format='%(message)s')
```

Запись в файл и в консоль

```python
logging.basicConfig(filename='example.log',
                    level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s '
                              '%(levelname)s '
                              '%(message)s',
                              datefmt='%Y-%m-%d %H:%M:%S')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)
```

Для самих сообщений

```
%s           строка
%d           для целых чисел
%c           для имени логгера
%f           для чисел с плавающей точкой
%r           для строковых представлений объектов
%m           для сообщения журнала
%x           целое число в шестнадцатеричной системе исчисления
%o           целое число в восьмеричной системе исчисления
%e, %E       число в экспоненциальной форме
```

Для настроек логгирования

```
%(message)s     сообщение журнала

%(asctime)s     время записи сообщения в формате (по умолчанию YYYY-MM-DD HH:MM:SS,sss настраивать в basicConfig(datefmt))
%(created)f     время записи сообщения в секундах, начиная с 1 января 1970 года

%(filename)s    имя файла, в котором был вызван логгер
%(funcName)s    имя функции, в которой был вызван логгер
%(name)s        имя логгера, который записывает сообщение
%(module)s      имя модуля, в котором был вызван логгер
%(threadName)s  имя потока, в котором был вызван логгер
%(processName)s имя процесса, в котором был вызван логгер

%(levelname)s   уровень журнала (например, DEBUG, INFO, WARNING, ERROR, CRITICAL)
%(levelno)s     уровень журнала в числовом формате (10 для DEBUG, 20 для INFO и т. д.)

%(lineno)d      номер строки, в которой был вызван логгер
%(pathname)s    полный путь к файлу, в котором был вызван логгер
%(process)d     идентификатор процесса, в котором был вызван логгер
%(thread)d      идентификатор потока, в котором был вызван логгер
```


Код для применения функций к тексту

```python
logging.info = lambda msg, *args, f=logging.info: f(Up(msg), *args)
```
""",
                "textwrap": """
Функция textwrap.wrap из модуля textwrap в Python используется 
для разбиения текстовой строки на список строк с заданной шириной столбца.

Например, если у вас есть длинная строка и вы хотите разбить ее на строки 
с длиной в 10 символов, вы можете использовать textwrap.wrap следующим образом:

```python
import textwrap

long_string = "This is a very long string that needs to be wrapped."
wrapped_string = textwrap.wrap(long_string, width=10)

print(wrapped_string)
# Output: ['This is a', 'very long', 'string', 'that needs', 'to be', 'wrapped.']
```

Кроме textwrap.wrap, модуль textwrap также содержит другие функции, такие как:

textwrap.fill        эта функция принимает строку и ширину столбца и возвращает отформатированную строку, где каждая строка имеет не более заданного количества символов.
textwrap.indent      эта функция принимает строку и префикс, который нужно добавить к каждой строке, и возвращает новую строку с добавленным префиксом.
textwrap.shorten     эта функция принимает строку и максимальную длину, которую должна иметь итоговая строка. 
                     Если исходная строка длиннее, то она обрезается и добавляется многоточие в конце.
textwrap.dedent      эта функция удаляет общий префикс всех строк в тексте, чтобы сделать его более компактным.
textwrap.TextWrapper это класс, который представляет настройки форматирования текста, такие как ширина столбца, префикс, отступы и другие параметры. 
                     Вы можете использовать этот класс, чтобы создать экземпляр объекта, который может быть использован для форматирования нескольких строк текста.
""",
                "PIL": {
                    "ImageDraw.Draw": """
```python
from PIL import Image
from PIL.ImageDraw import Draw

image = Image.open(r"")
draw = ImageDraw.Draw(image)
draw = Draw(image)
```

```python
[print(x) for x in dir(draw)]
```

arc                 Рисует дугу (часть 'пончика') на изображении. 
                    Принимает четыре аргумента: координаты прямоугольника, в котором находится дуга, начальный и конечный углы (в градусах), а также цвет линии.

bitmap              Рисует изображение в виде битовой карты на текущем изображении. 
                    Принимает два аргумента: координаты верхнего левого угла и изображение в формате Bitmap.

chord               Рисует сегмент круга на изображении, соединяя начальную и конечную точки с центром. 
                    Принимает аргументы, аналогичные arc.

draw                Используется для рисования на изображении с помощью кисти. 
                    Принимает два аргумента: изображение и цвет кисти.

ellipse             Рисует эллипс на изображении. 
                    Принимает два аргумента: координаты прямоугольника, в котором находится эллипс, и цвет линии.

fill                Заполняет область на изображении определенным цветом. 
                    Принимает два аргумента: координаты прямоугольника и цвет.

font                Используется для настройки шрифта, который будет использоваться при отрисовке текста. 
                    Принимает аргумент в формате ImageFont. (не работало...)

fontmode            Задает режим отображения текста. Может принимать значения "1" или "L".

getfont             Возвращает текущий шрифт.

im                  Текущее изображение.

ink                 Цвет, используемый для рисования.

line                Рисует линию на изображении. 
                    Принимает два аргумента: координаты начальной и конечной точек и цвет линии.

mode                Режим изображения. 
                    Может принимать значения "1", "L", "P", "RGB" или "CMYK".

multiline_text      Рисует многострочный текст на изображении. 
                    Принимает три аргумента: координаты верхнего левого угла, текст и дополнительные параметры.

multiline_textbbox  Возвращает ограничивающий прямоугольник для многострочного текста. 
                    Принимает те же аргументы, что и multiline_text.

multiline_textsize  Возвращает размер многострочного текста. 
                    Принимает те же аргументы, что и multiline_text.

palette             Палитра изображения.

pieslice            Рисует сегмент пирога на изображении. 
                    Принимает аргументы, аналогичные arc.

point               Рисует точку на изображении. 
                    Принимает аргументы - координаты точки и цвет.

polygon             Рисует многоугольник на изображении. 
                    Принимает два аргумента: список координат вершин многоугольника и цвет линии.

rectangle           Рисует прямоугольник на изображении. 
                    Принимает два аргумента: координаты прямоугольника и цвет линии.

regular_polygon     Рисует правильный многоугольник на изображении. 
                    Принимает три аргумента: центр многоугольника, количество сторон и радиус.

rounded_rectangle   Рисует прямоугольник с закругленными углами на изображении. 
                    Принимает аргументы, аналогичные rectangle.

shape               Рисует многоугольник, который может быть заполнен или обведен. 
                    Принимает два аргумента: список координат вершин многоугольника и цвет.

text                Рисует текст на изображении. 
                    Принимает три аргумента: координаты верхнего левого угла, текст и цвет.

textbbox            Возвращает ограничивающий прямоугольник для текста. 
                    Принимает те же аргументы, что и text.

textlength          Возвращает длину текста. 
                    Принимает два аргумента: текст и шрифт.

textsize            Возвращает размер текста. 
                    Принимает два аргумента: текст и шрифт.
"""
                },
                "datetime": """
<img alt="datetime.png" src="cheatsheet\Языки\Python\Библиотеки\datetime.png">
"""
            },
            "Методы": {
                "list": """
| Метод             |   INPUT   |  OUTPUT      |
|:------------------|:----------|:-------------|
| list.sort()       | [4, 3, 5] | [3, 4, 5]    |
| list.clear()      | [1, 2, 3] | []           |
| list.append(4)    | [1, 2, 3] | [1, 2, 3, 4] |
| list.count(1)     | [1, 1, 2] |  2           |
| list.extend([4])  | [1, 2, 3] | [1, 2, 3, 4] |
| list.insert(3, 4) | [1, 2, 3] | [1, 2, 3, 4] |
| list.index(2)     | [1, 2, 3] |  1           |
| list.remove(2)    | [1, 2, 3] | [1, 3]       |
| list.pop(2)       | [1, 2, 3] | [1, 2]       |
| list.reverse()    | [1, 2, 3] | [3, 2, 1]    |
| list.сору()       | [1, 2, 3] | [1, 2, 3]    |
| list.len()        | [1, 2, 3] |  3           |
| list.min()        | [1, 2, 3] |  3           |
| list.max()        | [1, 2, 3] |  3           |
""",
                "srt": r"""
| Метод                                  | Описание                                                                                                    |
|:---------------------------------------|:------------------------------------------------------------------------------------------------------------|
| str.capitalize()                       | Переводит первую букву в верхний, а остальные в нижний регистр.                                             |
| str.casefold()                         | Переводит все символы в нижний регистр                                                                      |
| str.center(width[, fillvalue])         | Обрамляет значениями fillvalue строку, пока длина не станет width                                           |
| str.count(str[, start][, end]          | Считает количество подстрок str в выбранном промежутке строки                                               |
| str.encode(encoding, errors)           | Меняет кодировку строки                                                                                     |
| str.endswith(suffix[, start][, end])   | Возвращает True если строка заканчивается на suffix, иначе False                                            |
| str.expandtabs(tabsize=8)              | Увеличивает размер символов табуляции до tabsize пробелов                                                   |
| str.find(str[, start][, end])          | Возвращает индекс начала первой подстроки str в выбранном промежутке или -1, если она не найдена            |
| str.format(args, *kwargs)              | Последовательно заменяет {} в строке на свои аргументы                                                      |
| str.format_map(dict)                   | Заменяет {<val>} в строке на dict[<val>]                                                                    |
| str.index(str[, start][, end])         | Возвращает индекс начала первой подстроки str в выбранном промежутке или ValueError, если она не найдена    |
| str.isalnum()                          | Возвращает True, если строка состоит только из букв и цифр, иначе False                                     |
| str.isalpha()                          | Возвращает True, если строка состоит только из букв, иначе False                                            |
| str.isdecimal()                        | Возвращает True, если строка состоит только из цифр, иначе False [1]                                        |
| str.isdigit()                          | Возвращает True, если строка состоит только из цифр, иначе False [1]                                        |
| str.isidentifier()                     | Возвращает True, если строка является идентификатором (if, class, assert), иначе False                      |
| str.islower()                          | Возвращает True, если вся строка в нижнем регистре, иначе False                                             |
| str.isnumeric()                        | Возвращает True, если строка состоит только из цифр, иначе False [1]                                        |
| str.isprintable()                      | Возвращает True, если все символы строки отображаются, иначе False (например, \n, \t)                       |
| str.isspace()                          | Возвращает True, если строка состоит из пробелов, иначе False                                               |
| str.istitle()                          | Возвращает True, если строка начинается с заглавной буквы, а остальные — строчные, иначе False              |
| str.isupper()                          | Возвращает True, если строка в верхнем регистре, иначе False                                                |
| str.join(iter)                         | Склеивает элементы последовательности iter в одну строку с разделителем s                                   |
| str.ljust(width, fillchar=' ')         | Добавляет в конец строки символ fillchar, пока длина не станет width                                        |
| str.lower()                            | Переводит символы строки в нижний регистр                                                                   |
| str.lstrip([chars])                    | Возвращает строку без пробельных символов или chars в начале                                                |
| str.maketrans(*args)                   | Возвращает таблицу перевода для s.translate                                                                 |
| str.partition(sep)                     | Разделяет строку на три части по первому разделителю sep: [начало, sep, конец]                              |
| str.replace(old, new)                  | Заменяет все подстроки old на new                                                                           |
| str.rfind(str[, start][, end])         | Возвращает индекс начала последней подстроки str в выбранном промежутке или -1, если она не найдена         |
| str.rindex(str[, start][, end])        | Возвращает индекс начала последней подстроки str в выбранном промежутке или ValueError, если она не найдена |
| str.rjust(width, fillchar=' ')         | Добавляет в начало строки символ fillchar, пока длина не станет width                                       |
| str.rpartition()                       | Разделяет строку на три части по последнему разделителю sep: [начало, sep, конец]                           |
| str.rsplit(sep=' ', maxsplit=-1)       | Возвращает список подстрок, разделенных по sep до maxsplit раз (с конца)                                    |
| str.rstrip([chars])                    | Возвращает строку без пробельных символов или chars в конце                                                 |
| str.split((sep=' ', maxsplit=-1))      | Возвращает список подстрок, разделенных по sep до maxsplit раз                                              |
| str.splitlines(keepends=False)         | Разделяет строку по \n. Не удаляет разделители, если keepends=True.                                         |
| str.startswith(prefix[, start][, end]) | Возвращает True если строка начинается с prefix, иначе False                                                |
| str.strip([chars])                     | Возвращает строку без пробельных символов или chars в начале и конце                                        |
| str.swapcase()                         | Меняет регистр всех символов на противоположный                                                             |
| str.title()                            | Возвращает строку, где все слова начинаются с заглавной буквы, а продолжаются строчными                     |
| str.translate(table)                   | Заменяет все символы строки согласно таблице перевода                                                       |
| str.upper()                            | Возвращает копию строки в верхнем регистре                                                                  |
| str.zfill(width)                       | Заполняет строку указанным числом нулей в начале                                                            |

**Символы**

| Символ | Назначение                    | Пример            | Результат |
|:-------|:------------------------------|:------------------|:----------|
| \n     | Перевод строки                | 'ab\ncd'          | ab        |
|        |                               |                   | cd        |
| \      | Экранирование                 | 'ab\\ncd'         | ab\ncd    |
| \a     | Звонок                        | 'a\aa'            | a[BEL]a   |
| \b     | Забой                         | 'ab\ba'           | ac        |
| \f     | Перевод страницы              | 'a\fa'            | a[FF]a    |
| \r     | Возврат каретки               | 'ab\rcd'          | cd        |
| \t     | Горизонтальная табуляция      | 'a\ta'            | a a       |
| \v     | Вертикальная табуляция        | 'a\va'            | a[VT]a    |
| \N{id} | Символ Юникода по id          | '\N{Degree Sign}' | °         |
| \uhhhh | 16-ричный символ Юникода      | '\u2030'          | ‰         |
| \Uhhhh | 32-ичный символ Юникода       | '\U00000394'      | Δ         |
| \xhh   | 16-ричное значение символа    | '\x2A'            | *         |
| \ooo   | восьмеричное значение символа | '/275'            | ½         |
| \0     | символ Null                   | '\0'              |           |
| \u00A0 | символ неразнывного пробела   |                   |           |
""",
                "dict": """
|                   |                                                                                                                                                                                      |
|:------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| dict.clear()      | Удаляет все элементы                                                                                                                                                                 |
| dict.copy()       | Возвращает поверхностную копию словаря                                                                                                                                               |
| dict.fromkeys()   | Создает словарь из заданной последовательности<br>print(dict.fromkeys(('key1', 'key2', 'key3'), 0)) # {'key1': 0, 'key2': 0, 'key3': 0}                                              |
| dict.get()        | Возвращает значение ключа<brprint({"model": "Mustang", "year": 1964}.get("model")) # Mustang                                                                                         |
| dict.items()      | Возвращает вид пары словаря (ключ, значение)                                                                                                                                         |
| dict.keys()       | Возвращает объект просмотра всех ключей                                                                                                                                              |
| dict.pop()        | Удаляет и возвращает элемент с заданным ключом                                                                                                                                       |
| dict.popitem()    | Возвращает и удаляет последний элемент из словаря                                                                                                                                    |
| dict.setdefault() | Returns the value of the specified key. If the key does not exist: insert the key, with the specified value<br>Возвращает значение по ключу. Если ключ отсутствует он вставляет ключ |
| dict.update()     | Updates the dictionary with the specified key-value pairs                                                                                                                            |
| dict.values()     | Возвращает список всех значений в словаре                                                                                                                                            |
""",
                "set": """
| Название метода                       | Что он делает                                                                                                 |
|:--------------------------------------|:--------------------------------------------------------------------------------------------------------------|
| set.add(element)                      | Добавляет элемент element во множество. Если элемент уже присутствует, ничего не происходит.                  |
| set.pop()                             | Удаляет и возвращает произвольный элемент из множества. Если множество пустое, возникает исключение KeyError. |
| set.difference_update(set2)           | Обновляет множество, удаляя элементы из set, которые присутствуют в set2.                                     |
| set.remove(element)                   | Удаляет элемент element из множества. Если элемент не найден, возникает исключение KeyError.                  |
| set.copy()                            | Возвращает копию множества.                                                                                   |
| set.union(set2)                       | Возвращает новое множество, содержащее все элементы из set и set2.                                            |
| set.isdisjoint(set2)                  | Проверяет, есть ли общие элементы между set и set2. Возвращает True, если нет, иначе False.                   |
| set.clear()                           | Удаляет все элементы из множества, делая его пустым.                                                          |
| set.discard(element)                  | Удаляет элемент element из множества. Если элемент не найден, ничего не происходит.                           |
| set.update(set2)                      | Обновляет множество, добавляя элементы из set2.                                                               |
| set.difference(set2)                  | Возвращает новое множество, содержащее элементы из set, которые отсутствуют в set2.                           |
| set.intersection(set2)                | Возвращает новое множество, содержащее только элементы, присутствующие одновременно в set и set2.             |
| set.intersection_update(set2)         | Обновляет множество, оставляя только элементы, присутствующие одновременно в set и set2.                      |
| set.issubset(set2)                    | Проверяет, является ли set подмножеством set2. Возвращает True, если так, иначе False.                        |
| set.issuperset(set2)                  | Проверяет, является ли set надмножеством set2. Возвращает True, если так, иначе False.                        |
| set.symmetric_difference(set2)        | Возвращает новое множество, содержащее элементы, присутствующие только в одном из set и set2.                 |
| set.symmetric_difference_update(set2) | Обновляет множество, оставляя только элементы, присутствующие только в одном из set и set2.                   |



В Python «замороженный» означает, что объект не может быть изменен. Например, рассмотрим setи frozenset:

```python
>>> s = set((1, 2, 3))
>>> s
{1, 2, 3}
>>> s.add(4)
>>> s
{1, 2, 3, 4}
>>> fs = frozenset((1, 2, 3))
>>> fs
frozenset({1, 2, 3})
>>> fs.add(4)
...
AttributeError: 'frozenset' object has no attribute 'add'
```
""",
            },
            "Магические методы": {
                "Кратко о использовании": """                   
| Магический метод                | Когда он вызывается (пример)     | Объяснение                                           |
|---------------------------------|----------------------------------|------------------------------------------------------|
| __new__(cls [,...])             | instance = MyClass(arg1, arg2)   | __new__ вызывается при создании экземпляра           |
| __init__(self [,...])           | instance = MyClass(arg1, arg2)   | __init__ вызывается при создании экземпляра          |
| __pos__(self)                   | +self                            | Унарный знак плюса                                   |
| __neg__(self)                   | -self                            | Унарный знак минуса                                  |
| __invert__(self)                | ~self                            | Побитовая инверсия                                   |
| __index__(self)                 | x[self]                          | Преобразование, когда объект используется как индекс |
| __nonzero__(self)               | bool(self), if self:             | Булевое значение объекта                             |
| __getattr__(self, name)         | self.name # name не определено   | Пытаются получить несуществующий атрибут             |
| __setattr__(self, name, val)    | self.name = val                  | Присвоение любому атрибуту                           |
| __delattr__(self, name)         | del self.name                    | Удаление атрибута                                    |
| __getattribute__(self, name)    | self.name                        | Получить любой атрибут                               |
| __getitem__(self, key)          | self[key]                        | Получение элемента через индекс                      |
| __setitem__(self, key, val)     | self[key] = val                  | Присвоение элементу через индекс                     |
| __delitem__(self, key)          | del self[key]                    | Удаление элемента через индекс                       |
| __iter__(self)                  | for x in self                    | Итерация                                             |
| __contains__(self, value)       | value in self, value not in self | Проверка принадлежности с помощью in                 |
| __call__(self [,...])           | self(args)                       | «Вызов» экземпляра                                   |
| __enter__(self)                 | with self as x:                  | with оператор менеджеров контекста                   |
| __exit__(self, exc, val, trace) | with self as x:                  | with оператор менеджеров контекста                   |
| __getstate__(self)              | pickle.dump(pkl_file, self)      | Сериализация                                         |
| __setstate__(self)              | data = pickle.load(pkl_file)     | Сериализация                                         |
""",
                "Сlass": """
&#95;&#95;_new&#95;&#95;(cls, [...)
    Это первый метод, который будет вызван при инициализации объекта. 
    Он принимает в качестве параметров класс и потом любые другие аргументы, 
    которые будут переданы в &#95;&#95;init&#95;&#95;.&#95;&#95;_new&#95;&#95; используется весьма редко, но иногда бывает полезен, 
    в частности, когда класс наследуется от неизменяемого (immutable) типа, такого как 
    кортеж (tuple) или строка.

&#95;&#95;init&#95;&#95;(self, [...)
    Инициализатор класса. Ему передаётся всё, с чем был вызван первоначальный конструктор 
    (если мы вызываем x = SomeClass(10, 'foo'), &#95;&#95;init&#95;&#95; получит 10 и 'foo' в качестве аргументов. 
    __init__ почти повсеместно используется при определении классов.

&#95;&#95;_del&#95;&#95;(self)
    Если&#95;&#95;_new&#95;&#95; и &#95;&#95;init&#95;&#95; образуют конструктор объекта,&#95;&#95;_del&#95;&#95; это его деструктор. 
    Он не определяет поведение для выражения del x (поэтому этот код не эквивалентен x&#95;&#95;_del&#95;&#95;()). 
    Скорее, он определяет поведение объекта в то время, когда объект попадает в сборщик мусора. 
    Это может быть довольно удобно для объектов, которые могут требовать дополнительных чисток 
    во время удаления, таких как сокеты или файловые объекты.

```python
class Class:
    def __init__(self, arg):
        self.arg = arg

    def __del__(self):
        del self.arg
```
""",
                "Сравнения": """
&#95;&#95;eq&#95;&#95;(self, other) - ==
&#95;&#95;ne&#95;&#95;(self, other) - !=
&#95;&#95;lt&#95;&#95;(self, other) - <
&#95;&#95;gt&#95;&#95;(self, other) - >
&#95;&#95;le&#95;&#95;(self, other) - <=
&#95;&#95;ge&#95;&#95;(self, other) - >=

```python
class Word(str):
    '''Класс для слов, определяющий сравнение по длине слов.'''
    def __new__(cls, word):
        # Мы должны использовать __new__, так как тип str неизменяемый
        # и мы должны инициализировать его раньше (при создании)
        if ' ' in word:
            print "Value contains spaces. Truncating to first space."
            word = word[:word.index(' ')] 
            # Теперь Word это все символы до первого пробела
        return str.__new__(cls, word)

    def __gt__(self, other):
        return len(self) > len(other)
    def __lt__(self, other):
        return len(self) < len(other)
    def __ge__(self, other):
        return len(self) >= len(other)
    def __le__(self, other):
        return len(self) <= len(other)
```

Теперь мы можем создать два Word (при помощи Word('foo') и Word('bar')) и сравнить их по длине. 
Заметьте, что мы не определяли __eq__ и __ne__, так как это приведёт к странному поведению 
(например, Word('foo') == Word('bar') будет расцениваться как истина)

Стандартная библиотека предоставляет нам класс-декторатор в модуле functools, 
который и определит все сравнивающие методы, от вас достаточно 
определить только __eq__ и ещё один (__gt__, __lt__ и т.п.) 
Для того, чтобы задействовать её, поместите @total_ordering над вашим определением класса.
""",
                "Унарные операторы": """
Обычные арифметические операторы

|                                                          |                                                                                     |
|----------------------------------------------------------|-------------------------------------------------------------------------------------|
| &#95;&#95;add&#95;&#95;(self, other)                     | +         Сложение                                                                  |
| &#95;&#95;pos&#95;&#95;(self)                            | +self     Унарный плюс                                                              |
| &#95;&#95;sub&#95;&#95;(self, other)                     | -         Вычитание                                                                 |
| &#95;&#95;neg&#95;&#95;(self)                            | -self     Отрицание                                                                 |
| &#95;&#95;mul&#95;&#95;(self, other)                     | *         Умножение                                                                 |
| &#95;&#95;floordiv&#95;&#95;(self, other)                | //        Целочисленное деление                                                     |
| Нету в python 3 ??? &#95;&#95;div&#95;&#95;(self, other) | /         Деление                                                                   |
| &#95;&#95;truediv&#95;&#95;(self, other)                 |           Правильное деление. Нужно from &#95;&#95;future&#95;&#95; import division |
| &#95;&#95;mod&#95;&#95;(self, other)                     | %         Остаток от деления                                                        |
| &#95;&#95;divmod&#95;&#95;(self, other)                  |           Определяет поведение для встроенной функции divmod()                      |
| &#95;&#95;pow&#95;&#95;                                  | **        Возведение в степень                                                      |
| &#95;&#95;lshift&#95;&#95;(self, other)                  | &lt;&lt;  Двоичный сдвиг влево                                                      |
| &#95;&#95;rshift&#95;&#95;(self, other)                  | &gt;      Двоичный сдвиг вправо                                                     |
| &#95;&#95;and&#95;&#95;(self, other)                     | &         Двоичное И                                                                |
| &#95;&#95;or&#95;&#95;(self, other)                      | &vert;    Двоичное ИЛИ                                                              |
| &#95;&#95;xor&#95;&#95;(self, other)                     | ^         Двоичный xor                                                              |

Каждый из этих методов должен возвращать значение, которое будет присвоено 
переменной слева (например, для a += b, &#95;&#95;iadd&#95;&#95; должен вернуть a + b, что будет присвоено a). 

|                                            |           |                                                                               |
|--------------------------------------------|-----------|-------------------------------------------------------------------------------|
| &#95;&#95;iadd&#95;&#95;(self, other)      | +=        | Сложение с присваиванием                                                      |
| &#95;&#95;isub&#95;&#95;(self, other)      | -=        | Вычитание с присваиванием                                                     |
| &#95;&#95;imul&#95;&#95;(self, other)      | *=        | Умножение с присваиванием                                                     |
| &#95;&#95;imatmul&#95;&#95;(self, other)   | @=        | Умножение матриц с присваиванием                                              |
| &#95;&#95;ifloordiv&#95;&#95;(self, other) | //=       | Целочисленное деление с присваиванием                                         |
| &#95;&#95;idiv&#95;&#95;(self, other)      | /=        | Деление с присваиванием                                                       |
| &#95;&#95;itruediv&#95;&#95;(self, other)  |           | Правильное деление с присваиванием.<br>Нужно from __future__ import division. |
| &#95;&#95;imo&#95;&#95;(self, other)       | %=        | Остаток от деления с присваиванием                                            |
| &#95;&#95;ipow&#95;&#95;                   | **=       | Возведение в степень с присваиванием                                          |
| &#95;&#95;ilshift&#95;&#95;(self, other)   | &lt;&lt;= | Двоичный сдвиг влево с присваиванием                                          |
| &#95;&#95;irshift&#95;&#95;(self, other)   | &gt;&gt;= | Двоичный сдвиг вправо с присваиванием                                         |
| &#95;&#95;iand&#95;&#95;(self, other)      | &=        | Двоичное И с присваиванием                                                    |
| &#95;&#95;ior&#95;&#95;(self, other)       | &vert;=   | Двоичное ИЛИ с присваиванием                                                  |
| &#95;&#95;ixor&#95;&#95;(self, other)      | ^=        | Двоичный xor с присваиванием                                                  |

|                                            |                             |                                                          |
|--------------------------------------------|-----------------------------|----------------------------------------------------------|
| &#95;&#95;abs&#95;&#95;(self)              | встроенная функции abs().   |                                                          |
| &#95;&#95;invert&#95;&#95;(self)           | ~                           | инвертирования оператором.                               |
| &#95;&#95;round&#95;&#95;(self)            | встроенная функции round(). | n это число знаков после запятой, до которого округлить. |
| &#95;&#95;floor&#95;&#95;(self)            | math.floor()                | округления до ближайшего меньшего целого.                |
| &#95;&#95;ceil&#95;&#95;(self)             | math.ceil()                 | округления до ближайшего большего целого.                |
| &#95;&#95;trunc&#95;&#95;(self)            | math.trunc()                | обрезания до целого.                                     |

Отражённая арифметика
some_object + other
Это «обычное» сложение. Единственное, чем отличается эквивалентное отражённое выражение, это порядок слагаемых:
other + some_object
В большинстве случаев, результат отражённой операции такой же, как её обычный эквивалент, 
поэтому при определении __radd__ вы можете ограничиться вызовом &#95;&#95;add&#95;&#95; да и всё. 
Заметьте, что объект слева от оператора (other в примере) 
не должен иметь обычной неотражённой версии этого метода.

|                                            |        |
|--------------------------------------------|--------|--------------------------------------------------------------------------------------------|
| &#95;&#95;radd&#95;&#95;(self, other)      | +      | Отражённое сложение                                                                        |
| &#95;&#95;rsub&#95;&#95;(self, other)      | -      | Отражённое вычитание                                                                       |
| &#95;&#95;rmul&#95;&#95;(self, other)      | *      | Отражённое умножение                                                                       |
| &#95;&#95;rfloordiv&#95;&#95;(self, other) | //     | Отражённое целочисленное деление                                                           |
| &#95;&#95;rdiv&#95;&#95;(self, other)      | /      | Отражённое деление                                                                         |
| &#95;&#95;rtruediv&#95;&#95;(self, other)  |        | Отражённое правильное деление. Нужно from __future__ import division                       |
| &#95;&#95;rmod&#95;&#95;(self, other)      | %      | Отражённый остаток от деления                                                              |
| &#95;&#95;rdivmod&#95;&#95;(self, other)   |        | Определяет поведение для встроенной функции divmod(), когда вызывается divmod(other, self) |
| &#95;&#95;rpow&#95;&#95;                   | **     | Отражённое возведение в степень                                                            |
| &#95;&#95;rlshift&#95;&#95;(self, other)   | <<     | Отражённый двоичный сдвиг влево                                                            |
| &#95;&#95;rrshift&#95;&#95;(self, other)   | >>     | Отражённый двоичный сдвиг вправо                                                           |
| &#95;&#95;rand&#95;&#95;(self, other)      | &      | Отражённое двоичное И                                                                      |
| &#95;&#95;ror&#95;&#95;(self, other)       | &vert; | Отражённое двоичное ИЛИ                                                                    |
| &#95;&#95;rxor&#95;&#95;(self, other)      | ^      | Отражённый двоичный xor                                                                    |
""",
                "Преобразование типов": """
__int__(self)           в int.
__long__(self)          в long.
__float__(self)         в float.
__complex__(self)       в комплексное число.
__oct__(self)           в восьмеричное число.
__hex__(self)           в шестнадцатиричное число.
__index__(self)         Преобразование типа к int, когда объект используется в срезах (выражения вида [start:stop:step]). 
                        Если вы определяете свой числовый тип, который может использоваться как индекс списка, вы должны определить __index__.
__trunc__(self)         Вызывается при math.trunc(self). 
                        Должен вернуть своё значение, обрезанное до целочисленного типа (обычно long).
__str__(self)           Определяет поведение функции str(), вызванной для экземпляра вашего класса.
__repr__(self)          Определяет поведение функции repr(), вызыванной для экземпляра вашего класса. 
                        Главное отличие от str() в целевой аудитории. 
                        repr() больше предназначен для машинно-ориентированного вывода 
                        (более того, это часто должен быть валидный код на Питоне), а str() предназначен для чтения людьми.
__bytes__(self)         ведёт себя так же как __str__
__format__(self, formatstr)
                        Определяет поведение, когда экземпляр вашего класса используется в форматировании строк нового стиля. 
                        Например, "Hello, {0:abc}!".format(a) приведёт к вызову a.__format__("abc"). 
                        Это может быть полезно для определения ваших собственных числовых или строковых типов, 
                        которым вы можете захотеть предоставить какие-нибудь специальные опции форматирования.
__hash__(self)          Определяет поведение функции hash(), вызыванной для экземпляра вашего класса. 
                        Метод должен возвращать целочисленное значение, которое будет использоваться 
                        для быстрого сравнения ключей в словарях. 
                        Заметьте, что в таком случае обычно нужно определять и __eq__ тоже. 
                        Руководствуйтесь следующим правилом: a == b подразумевает hash(a) == hash(b).
__bool__(self)          Определяет поведение функции bool(), вызванной для экземпляра вашего класса. 
                        Должна вернуть True или False, в зависимости от того, 
                        когда вы считаете экземпляр соответствующим True или False.
__dir__(self)           Определяет поведение функции dir(), вызванной на экземпляре вашего класса. 
                        Этот метод должен возвращать пользователю список атрибутов. 
                        Обычно, определение __dir__ не требуется, но может быть жизненно важно для интерактивного 
                        использования вашего класса, если вы переопределили __getattr__ или __getattribute__ 
                        (с которыми вы встретитесь в следующей части), 
                        или каким-либо другим образом динамически создаёте атрибуты.
__sizeof__(self)        Определяет поведение функции sys.getsizeof(), вызыванной на экземпляре вашего класса. 
                        Метод должен вернуть размер вашего объекта в байтах. 
                        Он главным образом полезен для классов, определённых в 
                        расширениях на C, но всё-равно полезно о нём знать.
""",
                "Контроль доступа к атрибутам": """
__getattr__(self, name)              Вы можете определить поведение для случая, когда пользователь пытается обратиться 
                                     к атрибуту, который не существует (совсем или пока ещё). 
                                     Это может быть полезным для перехвата и перенаправления частых опечаток, 
                                     предупреждения об использовании устаревших атрибутов 
                                     (вы можете всё-равно вычислить и вернуть этот атрибут, если хотите), 
                                     или хитро возвращать AttributeError, когда это вам нужно. 
                                     Правда, этот метод вызывается только когда пытаются получить 
                                     доступ к несуществующему атрибуту, поэтому это не очень хорошее решение для инкапсуляции.
__setattr__(self, name, value)       В отличии от __getattr__, __setattr__ решение для инкапсуляции. 
                                     Этот метод позволяет вам определить поведение для присвоения значения атрибуту, 
                                     независимо от того существует атрибут или нет. 
                                     То есть, вы можете определить любые правила для любых изменений значения атрибутов. 
                                     Впрочем, вы должны быть осторожны с тем, как использовать __setattr__, 
                                     смотрите пример нехорошего случая в конце этого списка.
__delattr__                          Это то же, что и __setattr__, но для удаления атрибутов, вместо установки значений. 
                                     Здесь требуются те же меры предосторожности, что и в __setattr__ чтобы избежать 
                                     бесконечной рекурсии (вызов del self.name в определении __delattr__ вызовет бесконечную рекурсию)
__getattribute__(self, name)         Выглядит к месту среди своих коллег __setattr__ и __delattr__, 
                                     но я бы не рекомендовал вам его использовать. __getattribute__ может использоваться 
                                     только с классами нового типа (в новых версиях Питона все классы нового типа, а в старых версиях 
                                     вы можете получить такой класс унаследовавшись от object). 
                                     Этот метод позволяет вам определить поведение для каждого случая доступа к атрибутам 
                                     (а не только к несуществующим, как __getattr__(self, name)). 
                                     Он страдает от таких же проблем с бесконечной рекурсией, как и его коллеги 
                                     (на этот раз вы можете вызывать __getattribute__ у базового класса, чтобы их предотвратить). 
                                     Он, так же, главным образом устраняет необходимость в __getattr__, 
                                     который в случае реализации __getattribute__ может быть вызван только явным образом 
                                     или в случае генерации исключения AttributeError. 
                                     Вы конечно можете использовать этот метод (в конце концов, это ваш выбор), 
                                     но я бы не рекомендовал, потому что случаев, когда он действительно полезен очень мало 
                                     (намного реже нужно переопределять поведение при получении, а не при установке значения) 
                                     и реализовать его без возможных ошибок очень сложно.

Вы можете запросто получить проблему при определении любого метода, управляющего доступом к атрибутам. Рассмотрим пример:

```python
def __setattr__(self, name, value):
    self.name = value
    # это рекурсия, так как всякий раз, когда любому атрибуту присваивается значение,
    # вызывается  __setattr__().
    # тоесть, на самом деле это равнозначно self.__setattr__('name', value). 
    # Так как метод вызывает сам себя, рекурсия продолжится бесконечно, пока всё не упадёт

def __setattr__(self, name, value):
    self.__dict__[name] = value # присваивание в словарь переменных класса
    # дальше определение произвольного поведения
```

Ещё раз, мощь магических методов в Питоне невероятна, а с большой силой 
приходит и большая ответственность. 
Важно знать, как правильно использовать магические методы, ничего не ломая.

Вот пример использования методов контроля доступа 
(заметьте, что мы используем super, так как не все классы имеют атрибут __dict__):

```python
class AccessCounter(object):
    '''Класс, содержащий атрибут value и реализующий счётчик доступа к нему.
    Счётчик увеличивается каждый раз, когда меняется value.'''

    def __init__(self, val):
        super(AccessCounter, self).__setattr__('counter', 0)
        super(AccessCounter, self).__setattr__('value', val)

    def __setattr__(self, name, value):
        if name == 'value':
            super(AccessCounter, self).__setattr__('counter', self.counter + 1)
        # Не будем делать здесь никаких условий.
        # Если вы хотите предотвратить изменение других атрибутов,
        # выбросьте исключение AttributeError(name)
        super(AccessCounter, self).__setattr__(name, value)

    def __delattr__(self, name):
        if name == 'value':
            super(AccessCounter, self).__setattr__('counter', self.counter + 1)
        super(AccessCounter, self).__delattr__(name)]
```
""",
                "Магия контейнеров": """
В Питоне существует множество способов заставить ваши классы вести себя как встроенные последовательности 
(словари, кортежи, списки, строки и так далее). 
Это, безусловно, мои любимые магические методы, из-за до абсурда высокой степени контроля, 
которую они дают и той магии, от которой с экземплярами ваших классов вдруг начинает прекрасно 
работать целое множество глобальных функций. 
Но, до того как мы перейдём ко всяким хорошим вещам, мы должны знать о протоколах.
Протоколы немного похожи на интерфейсы в других языках тем, что они предоставляют 
набор методов, которые вы должны реализовать. 
Однако, в Питоне протоколы абсолютно ни к чему не обязывают и не требуют 
обязательно реализовать какое-либо объявление. 
Наверное, они больше похожи на руководящие указания.

Протокол для определения неизменяемых контейнеров: чтобы создать неизменяемый контейнер, вы должны только определить __len__ и __getitem__

Протокол изменяемого контейнера требует того же, что и неизменяемого контейнера, плюс __setitem__ и __delitem__

Если вы хотите, чтобы ваши объекты можно было перебирать итерацией, вы должны определить __iter__, который возвращает итератор. 
Этот итератор должен соответствовать протоколу итератора, который требует методов __iter__(возвращает самого себя) и __next__.


__len__(self)                  Кколичество элементов в контейнере. Часть протоколов для изменяемого и неизменяемого контейнеров.
__getitem__(self, key)         Поведение при доступе к элементу, используя синтаксис self[key]. 
                               Тоже относится и к протоколу изменяемых и к протоколу неизменяемых контейнеров. 
                               Должен выбрасывать соответствующие исключения: 
                               TypeError если неправильный тип ключа и KeyError если ключу не соответствует никакого значения.
__setitem__(self, key, value)  Определяет поведение при присваивании значения элементу, 
                               используя синтаксис self[nkey] = value. 
                               Часть протокола изменяемого контейнера. 
                               Опять же, вы должны выбрасывать KeyError и TypeError в соответсвующий случаях.
__delitem__(self, key)         Определяет поведение при удалении элемента (то есть del self[key]). 
                               Это часть только протокола для изменяемого контейнера. 
                               Вы должны выбрасывать соответствующее исключение, если ключ некорректен.
__iter__(self)                 Должен вернуть итератор для контейнера. 
                               Итераторы возвращаются в множестве ситуаций, главным образом для встроенной функции iter() 
                               и в случае перебора элементов контейнера выражением for x in container:. 
                               Итераторы сами по себе объекты и они тоже должны определять метод __iter__, который возвращает self.
__reversed__(self)             Вызывается чтобы определить поведения для встроенной функции reversed(). 
                               Должен вернуть обратную версию последовательности. 
                               Реализуйте метод только если класс упорядоченный, как список или кортеж.
__contains__(self, item)       Предназначен для проверки принадлежности элемента с помощью in и not in. 
                               Вы спросите, почему же это не часть протокола последовательности? 
                               Потому что когда __contains__ не определён, Питон просто перебирает всю последовательность 
                               элемент за элементом и возвращает True если находит нужный.
__missing__(self, key)         Используется при наследовании от dict. 
                               Определяет поведение для для каждого случая, когда пытаются получить элемент по 
                               несуществующему ключу (так, например, если у меня есть словарь d и я пишу d["george"] 
                               когда "george" не является ключом в словаре, вызывается d.__missing__("george")).
Пример

```python
class FunctionalList:
    '''Класс-обёртка над списком с добавлением некоторой функциональной магии: head,
    tail, init, last, drop, take.'''

    def __init__(self, values=None):
        if values is None:
            self.values = []
        else:
            self.values = values

    def __len__(self):
        return len(self.values)

    def __getitem__(self, key):
        # если значение или тип ключа некорректны, list выбросит исключение
        return self.values[key]

    def __setitem__(self, key, value):
        self.values[key] = value

    def __delitem__(self, key):
        del self.values[key]

    def __iter__(self):
        return iter(self.values)

    def __reversed__(self):
        return FunctionalList(reversed(self.values))

    def append(self, value):
        self.values.append(value)
    def head(self):
        # получить первый элемент
        return self.values[0]
    def tail(self):
        # получить все элементы после первого
        return self.values[1:]
    def init(self):
        # получить все элементы кроме последнего
        return self.values[:-1]
    def last(self):
        # получить последний элемент
        return self.values[-1]
    def drop(self, n):
        # все элементы кроме первых n
        return self.values[n:]
    def take(self, n):
        # первые n элементов
        return self.values[:n]
```

Теперь у вас есть полезный (относительно) пример реализации своей собственной последовательности. 
Существуют, конечно, и куда более практичные реализации произвольных последовательностей, 
но большое их число уже реализовано в стандартной библиотеке, такие как Counter, OrderedDict, NamedTuple
""",
                "isinstance()": """
__instancecheck__(self, instance) Проверяет, является ли экземлпяр членом вашего класса (isinstance(instance, class)
__subclasscheck__(self, subclass) Проверяет, является наследуется ли класс от вашего класса (issubclass(subclass, class))
""",
                "Вызываемые объекты": """
__call__(self, [args...])            Позволяет любому экземпляру вашего класса быть вызванным как-будто он функция. 
                                     Главным образом это означает, что x() означает то же, что и x.__call__(). 
                                     Заметьте, __call__ принимает произвольное число аргументов; 
                                     то есть, вы можете определить __call__ так же как любую другую функцию, 
                                     принимающую столько аргументов, сколько вам нужно.

__call__, в частности, может быть полезен в классах, чьи экземпляры часто изменяют своё состояние. 
«Вызвать» экземпляр может быть интуитивно понятным и элегантным способом изменить состояние объекта. 
Примером может быть класс, представляющий положение некоторого объекта на плоскости:

```python
class Entity:
    '''Класс, описывающий объект на плоскости. "Вызываемый", чтобы обновить позицию объекта.'''

    def __init__(self, size, x, y):
        self.x, self.y = x, y
        self.size = size

    def __call__(self, x, y):
        '''Изменить положение объекта.'''
        self.x, self.y = x, y

    # чик...
```
""",
                "Менеджеры контекста": """
__enter__(self)                      Определяет, что должен сделать менеджер контекста в начале блока, созданного оператором with. 
                                     Заметьте, что возвращаемое __enter__ значение и есть то значение, с которым производится работа внутри with.
__exit__(self, exception_type, 
         exception_value, traceback) Определяет действия менеджера контекста после того, как блок будет выполнен (или прерван во время работы). 
                                     Может использоваться для контролирования исключений, чистки, любых действий которые должны быть 
                                     выполнены незамедлительно после блока внутри with. 
                                     Если блок выполнен успешно, exception_type, exception_value, и traceback будут установлены в None. 
                                     В другом случае вы сами выбираете, перехватывать ли исключение или предоставить это пользователю; 
                                     если вы решили перехватить исключение, убедитесь, что __exit__ возвращает True после того 
                                     как всё сказано и сделано. 
                                     Если вы не хотите, чтобы исключение было перехвачено менеджером контекста, просто позвольте ему случиться.

__enter__ и __exit__ могут быть полезны для специфичных классов с хорошо описанным и 
распространённым поведением для их настройки и очистки ресурсов. 
Вы можете использовать эти методы и для создания общих менеджеров контекста для разных объектов. 

Вот пример:

```python
class Closer:
    '''Менеджер контекста для автоматического закрытия объекта вызовом метода close 
    в with-выражении.'''

    def __init__(self, obj):
        self.obj = obj

    def __enter__(self):
        return self.obj # привязка к активному объекту with-блока

    def __exit__(self, exception_type, exception_val, trace):
        try:
            self.obj.close()
        except AttributeError: # у объекта нет метода close
            print 'Not closable.'
            return True # исключение перехвачено
```

__aenter__(self) — аналогично __enter__, только функция возвращает корутину (результат которой можно получить с помощью await)

__aexit__(self, exc_type, exc_value, traceback) — аналогично __exit__, только функция возвращает корутину (результат которой можно получить с помощью await)

```python
class AsyncContextManager:
    async def __aenter__(self):
        await log("entering context")

    async def __aexit__(self, exc_type, exc_value, traceback):
        await log("exiting context")

async with AsyncContextManager():
    print("in context manager")

'entering context'
'in context manager'
'exiting context'
```
""",
                "Построение дескрипторов": '''
Дескрипторы это такие классы, с помощью которых можно добавить свою логику к событиям доступа 
(получение, изменение, удаление) к атрибутам других объектов. 
Дескрипторы не подразумевается использовать сами по себе; скорее, предполагается, 
что ими будут владеть какие-нибудь связанные с ними классы. 
Дескрипторы могут быть полезны для построения объектно-ориентированных баз данных или классов, 
чьи атрибуты зависят друг от друга. В частности, дескрипторы полезны при представлении атрибутов 
в нескольких системах исчисления или каких-либо вычисляемых атрибутов 
(как расстояние от начальной точки до представленной атрибутом точки на сетке).

Чтобы класс стал дескриптором, он должен реализовать по крайней мере один метод из 
__get__, __set__ или __delete__. 

__get__(self, instance, instance_class) Определяет поведение при возвращении значения из дескриптора. 
                                        instance это объект, для чьего атрибута-дескриптора вызывается метод. 
                                        owner это тип (класс) объекта.
__set__(self, instance, value)          Определяет поведение при изменении значения из дескриптора. 
                                        instance это объект, для чьего атрибута-дескриптора вызывается метод. 
                                        value это значение для установки в дескриптор.
__delete__(self, instance)              Определяет поведение для удаления значения из дескриптора. 
                                        instance это объект, владеющий дескриптором.

Теперь пример полезного использования дескрипторов: преобразование единиц измерения.

```python
class Meter(object):
    """Дескриптор для метра."""

    def __init__(self, value=0.0):
        self.value = float(value)
    def __get__(self, instance, owner):
        return self.value
    def __set__(self, instance, value):
        self.value = float(value)

class Foot(object):
    """Дескриптор для фута."""

    def __get__(self, instance, owner):
        return instance.meter * 3.2808
    def __set__(self, instance, value):
        instance.meter = float(value) / 3.2808

class Distance(object):
    """Класс, описывающий расстояние, содержит два дескриптора для футов и
    метров."""
    meter = Meter()
    foot = Foot()
```
''',
                "Копирование": """
В Питоне оператор присваивания не копирует объекты, а только добавляет ещё одну ссылку. 
Но для коллекций, содержащих изменяемые элементы, иногда необходимо полноценное копирование, 
чтобы можно было менять элементы одной последовательности, не затрагивая другую. 
Здесь в игру и вступает copy. Мы должны сказать Питону как правильно копировать.

__copy__(self)                       Определяет поведение copy.copy() для экземпляра вашего класса. 
                                     copy.copy() возвращает поверхностную копию вашего объекта — это означает, 
                                     что хоть сам объект и создан заново, все его данные ссылаются на данные оригинального объекта. 
                                     И при изменении данных нового объекта, изменения будут происходить и в оригинальном.
__deepcopy__(self, memodict={})      Определяет поведение copy.deepcopy() для экземпляров вашего класса. 
                                     copy.deepcopy() возвращает глубокую копию вашего объекта — копируются и объект и его данные. 
                                     memodict это кэш предыдущих скопированных объектов, он предназначен для оптимизации 
                                     копирования и предотвращения бесконечной рекурсии, когда копируются рекурсивные структуры данных. 
                                     Когда вы хотите полностью скопировать какой-нибудь конкретный атрибут, 
                                     вызовите на нём copy.deepcopy() с первым параметром memodict
""",
                "Ещё": """
__init_subclass__(cls) — позволяет переопределить создание подклассов объекта. Например, добавлять дополнительные атрибуты:

```python
>>> class Test:
>>>     def __init_subclass__(cls, /, test_param, **kwargs):
>>>         super().__init_subclass__(**kwargs)
>>>         cls.test_param = test_param
>>>
>>> class AnotherTest(Test, test_param="Hello World"):
>>>     pass
```

repr() это встроенная функция Python, которая возвращает строковое представление объекта
Доступ к атрибутам объекта
Доступ ко всем свойствам объекта также контролируются отдельными методами:

__getattr__(self, name) — вызывается методом getattr(...) или при обращении к атрибуту объекта через x.y, где x — объект, а y — атрибут.

__setattr__(self, name, value) — вызывается методом setattr(...)или при обращении к атрибуту объекта с последующим определением значения переданного атрибута. 
Например: x.y = 1, где x — объект, y — атрибут, а 1 — значение атрибута.

__delattr__(self, name) — вызывается методом delattr(...)или при ручном удалении атрибута у объекта с помощью del x.y, где  x — объект, а y — атрибут.

__dir__(self) — вызывается методом dir(...) и выводит список доступных атрибутов объекта.



Создание последовательностей
Любой объект может реализовать методы встроенных последовательностей (словари, кортежи, списки, строки и так далее). 
Доступ к значениям последовательности переопределяется следующими методами:

__len__(self) — вызывается методом len(...) и возвращает количество элементов в последовательности.

__getitem__(self, key) — вызывается при обращении к элементу в последовательности по его ключу (индексу). 
Метод должен выбрасывать исключение TypeError, если используется некорректный тип ключа, KeyError, 
если данному ключу не соответствует ни один элемент в последовательности. Например:

```python
>>> list_object = [1, 2, 3, 4, 5]
>>> print(list_object[0])
... 1
>>>
>>> string_object = "hello world"
>>> print(string_object[0:5])
... 'hello'
>>>
>>> dict_object = {"key0": True, "key1": False}
>>> print(dict_object["key0"])
... True
```

__setitem__(self, key, value) — вызывается при присваивании какого-либо значения элементу в последовательности. 
Также может выбрасывать исключения TypeError и KeyError. Например:

```python
>>> list_object = [1, 2, 3, 4, 5]
>>> list_object[0] = 78
>>> print(list_object)
... [78, 2, 3, 4, 5]
>>>
>>> dict_object = {"key0": True, "key1": False}
>>> dict_object["key0"] = False
>>> print(dict_object)
... {"key0": False, "key1": False}
```

__delitem__(self, key) — вызывается при удалении значения в последовательности по его индексу (ключу) с помощью синтаксиса ключевого слова del.

__missing__(self, key) — вызывается в случаях, когда значения в последовательности не существует.

__iter__(self) — вызывается методом iter(...) и возвращает итератор последовательности, например, для использования объекта в цикле:

```python
>>> class Test:
>>>     def __iter__(self):
>>>         return (1, 2, 3)
>>>
>>> for value in Test():
>>>     print(value)
... 1
... 2
... 3
```

__reversed__(self) — вызывается методом reversed(...) и аналогично методу __iter__ возвращает тот же итератор, только в обратном порядке.

__contains__(self, item) — вызывается при проверке принадлежности элемента к последовательности с помощью in или not in.


__imatmul__(self, other) — умножение матриц с присваиванием, оператор @=
"""
            },
            "Декораторы Замыкания": {
                "Декораторы Замыкания": """Декораторы (decorators) в Python

Специальные функции, которые позволяют модифицировать поведение
других функций. Они часто используются для добавления нового функционала
к существующим функциям без изменения их кода.

```python
def cache_decorator(func):
    cache = {}
    def wrapper(*args, **kwargs):
        key = f"{args}:{kwargs}"
        if key not in cache:
            result = func(*args, **kwargs)
            cache[key] = result
        return cache[key]
    return wrapper

@cache_decorator
def expensive_function(x):
    # дорогая расчетная функция
    return x**2

print(expensive_function(2))  # 4
print(expensive_function(2))  # 4 (значение берется из кеша)
print(expensive_function(3))  # 9
print(expensive_function(3))  # 9 (значение берется из кеша)
```

Python - closure (Замыкания)

Функции, которые ссылаются на переменные, определенные вне этой функции.
Они позволяют сохранять состояние переменных между вызовами функции.
Замыкания часто используются в Python для создания функций-генераторов,
которые возвращают новые функции с измененными параметрами.

Например, следующий код создает функцию-генератор, которая возвращает
функции, увеличивающие число на указанное значение:

```python
def make_incrementor(n):
    def incrementor(x):
        return x + n
    return incrementor

plus_3 = make_incrementor(3)
plus_5 = make_incrementor(5)

print(plus_3(10))  # 13
print(plus_5(10))  # 15
```
""",
                "Аргументы dataclass": """
```python
from dataclasses import dataclass
```

dataclass(*,
          init: bool = ...,
          repr: bool = ...,
          eq: bool = ...,
          order: bool = ...,
          unsafe_hash: bool = ...,
          frozen: bool = ...)

init         Нужно ли автоматически генерировать метод __init__ для инициализации атрибутов класса.
repr         Нужно ли автоматически генерировать метод __repr__ для вывода строкового представления объектов класса.
eq           Нужно ли автоматически генерировать метод __eq__ для сравнения объектов класса.
order        Нужно ли автоматически генерировать методы __lt__, __le__, __gt__, __ge__ для сравнения объектов класса.
unsafe_hash  Нужно ли автоматически генерировать метод __hash__ для объектов класса.
             Обычно этот аргумент следует использовать только для классов, объекты которых неизменяемы (frozen),
             так как изменяемые объекты могут привести к неожиданным результатам.
frozen       Нужно ли сделать объекты класса неизменяемыми (immutable).

Все эти аргументы являются необязательными, и если их не указывать,
то будут использованы значения по умолчанию (True для init, repr, eq, order, unsafe_hash и False для frozen).

""",
                "property": """
```python
class Student:
    def __init__(self):
        self._score = 0

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, s):
        if 0 <= s <= 100:
            self._score = s
        else:
            raise ValueError

user1 = Student()
print(user1.score) # 0
user1.score = 1
print(user1.score) # 1
user1._score = 999
print(user1.score) # 999
user1.score = 999
print(user1.score) # ValueError
```
""",
                "cached_property": """
```python
from functools import cached_property


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @cached_property
    def area(self):
        return 3.14 * self.radius ** 2


circle = Circle(10)
print(circle.area)
# напечатает 314.0
print(circle.area)
# вернет кешированное значение 314.0 без вычислений
```
""",
                "staticmethod": """
@staticmethod - это декоратор в Python, который используется для определения статического метода внутри класса. 
Статический метод - это метод, который может быть вызван на классе, а не на экземпляре класса. 
Он не имеет доступа к экземпляру класса и не может изменять его состояние.

Пример использования @staticmethod:

```python
class MyClass:
    @staticmethod
    def my_static_method(arg1, arg2):
        return arg1 + arg2

result = MyClass.my_static_method(1, 2)
print(result) # 3
```

В этом примере мы определили класс MyClass и внутри него определили статический метод my_static_method. 
Этот метод принимает два аргумента arg1 и arg2 и возвращает их сумму. 
Затем мы вызвали этот метод на классе MyClass, а не на экземпляре класса.
""",
                "overload": """
@overload - это декоратор в Python, который используется для определения перегрузки метода внутри класса. 
Перегрузка метода - это механизм, позволяющий определить несколько версий метода с разными параметрами. 
При вызове метода, интерпретатор Python выберет версию метода, которая соответствует переданным аргументам.

Пример использования @overload:

```python
from typing import overload

class MyClass:
    @overload
    def my_method(self, arg1: int) -> int:
        pass
    
    @overload
    def my_method(self, arg1: str) -> str:
        pass
    
    def my_method(self, arg1):
        if isinstance(arg1, int):
            return arg1 * 2
        elif isinstance(arg1, str):
            return arg1.upper()

obj = MyClass()
result1 = obj.my_method(2)
print(result1) # 4

result2 = obj.my_method("hello")
print(result2) # HELLO
```

В этом примере мы определили класс MyClass и внутри него определили метод my_method с помощью декоратора @overload. 
Мы определили две версии метода: одна принимает целое число и возвращает его удвоенное значение, а другая принимает строку и возвращает ее в верхнем регистре. 
Наконец, мы определили основную версию метода, которая выбирает нужную версию метода в зависимости от типа переданного аргумента.
""",
                "final": """
@final - это аннотация (декоратор) в Python, которая указывает, 
что метод или свойство класса не должны переопределяться в подклассах.

Когда метод или свойство класса помечаются аннотацией @final, это предупреждает программистов, 
что эти элементы класса являются частью публичного интерфейса класса, который не должен изменяться в подклассах. 
Это позволяет сделать класс более простым и предсказуемым в использовании, так как гарантируется, 
что поведение не будет изменено в производных классах.
Пример использования аннотации @final:

```python
class BaseClass:
    @final
    def some_method(self):
        pass

class DerivedClass(BaseClass):
    def some_method(self):  # Ошибка - метод some_method не может быть переопределен
        pass
```

В этом примере, метод some_method в базовом классе BaseClass помечен аннотацией @final, 
что предотвращает его переопределение в производном классе DerivedClass. 
Если в производном классе попытаться переопределить метод some_method, то возникнет ошибка.
"""
            },
            "pip": {
                "pip": """
Утилита pip в Python имеет множество флагов, которые можно использовать при установке пакетов. 
Ниже перечислены некоторые из наиболее часто используемых флагов:

-r, --requirements: Установить пакеты из указанного файла зависимостей (requirements.txt).
-U, --upgrade:      Обновить уже установленные пакеты до последней версии.
-e, --editable:     Установить пакет в режиме редактирования, что позволяет вносить изменения в код и сразу же видеть результаты.
-t, --target:       Указать путь к каталогу, в который будут установлены пакеты.
-f, --find-links:   Указать дополнительные источники для поиска пакетов (например, URL или путь к локальному каталогу).
-i, --index-url:    Указать URL для поиска пакетов в репозитории PyPI.
--no-index:         Не использовать PyPI для поиска пакетов, только локальные источники.
--no-cache-dir:     Не использовать кэш при установке пакетов.
--user:             Установить пакеты в домашний каталог текущего пользователя.

Это только некоторые из флагов, которые могут быть использованы при установке пакетов через pip. 
Вы можете узнать больше о флагах, запустив команду pip install --help.
""",
                "requirements.txt": """
Команда, которая создает список всех пакетов и их версий, 
установленных в настоящее время в среде Python.

```python
pip freeze > requirements.txt
```

Файл requirements.txt используется для указания зависимостей для проекта Python. 
В нем перечислены пакеты и их версии, необходимые для правильной работы проекта. 
Это упрощает настройку той же среды на другом компьютере или при развертывании приложения в производственной среде.
Когда вы запустите pip freeze > requirements.txt, он создаст новый файл с именем requirements.txt
в вашем текущем каталоге и запишет вывод pip freeze команды в этот файл, 
который будет содержать список всех пакетов и их версий, которые в 
настоящее время установлены в вашей среде Python, один пакет за строку.
Позже вы можете использовать 

```python
pip install -r requirements.txt
```

для установки всех пакетов и их версий, перечисленныx в файле, 
это гарантирует, что среда такая же, как та, которая 
использовалась для создания requirements.txt файла.

Рекомендуется включить requirements.txt файл в репозиторий вашего проекта, 
чтобы другие разработчики или пользователи могли легко 
настроить ту же среду и запустить проект с правильными зависимостями.

Для создания файла с библиотеками используемыми только для нужного проекта использовать 

```python
pip freeze --local > requirements.txt
```
""",
            },
            "with as": """with
В начале блока кода with вызывает метод __enter__ у объекта,
который используется для подготовки контекста.
После того как код внутри блока завершился, вызывается метод __exit__,
который используется для освобождения ресурсов.
Контекстный менеджер with удобен для использования,
так как он автоматически освобождает ресурсы в конце блока кода, что избавляет
от необходимости ручного закрытия файла или освобождения других ресурсов.
Контекстный менеджер with может быть использован не только с файлами,
но и с другими объектами, которые поддерживают методы __enter__ и __exit__.
Например, он может быть использован для управления блокировками,
сетевыми соединениями и т.д.

```python
class Writer(object):
    def __init__(self, path):
        self.path = path

    def __enter__(self):
        self.file = open(self.path, 'w', encoding='UTF-8')
        return self.file

    def __exit__(self, *args):
        self.file.close()

with Writer('my_file.txt') as file:
    file.write('hello world')
```
""",
            "fstrings": """
F-строки - это новый способ форматирования строк в Python 3.6 и выше. 
Они позволяют встраивать выражения Python внутри строк посредством указания их в {} внутри строки, заключенной в f.



replacement_field ::=  "{" [field_name] ["!" преобразование] [":" спецификация формата] "}"
field_name        ::=  arg_name ("." attribute_name | "[" element_index "]")*
arg_name          ::=  [identifier | digit+]
attribute_name    ::=  identifier
element_index     ::=  digit+ | index_string
index_string      ::=  <любой исходный символ, кроме "]"> +
conversion        ::=  "r" | "s" | "a"
format_spec       ::=  <описано в следующем разделе>

За field_name может следовать поле преобразования , которому предшествует восклицательный знак '!', 
и format_spec , которому предшествует двоеточие ':'. 
Они определяют нестандартный формат для замещающего значения.

В настоящее время поддерживаются три флага преобразования: '!s'который вызывает str() значение, '!r'который вызывает repr()и '!a'который вызывает ascii().

Некоторые примеры:

```python
"Harold's a clever {0!s}"        # Calls str() on the argument first
"Bring out the holy {name!r}"    # Calls repr() on the argument first
"More {!a}"                      # Calls ascii() on the argument first
```


format_spec     ::= [[ fill] align][ sign][z][#][0][ width][ grouping_option][. precision][ type]
заполнить            ::= <любой символ>
выровнять           ::= "<" | ">" | "=" | "^"
знак            ::= "+" | "-" | " "
ширина           ::=   digit+
grouping_option ::= "_" | ","
точность       ::=   digit+
тип            ::= "b" | "c" | "d" | "e" | "E" | "f" | "F" | "g" | "G" | "n" | "o" | "s" | "x" | "X" | "%"

Вариант Значение
'<'     Принудительно выравнивает поле по левому краю в доступном пространстве 
        (это значение по умолчанию для большинства объектов).
'>'     Принудительно выравнивает поле по правому краю в доступном пространстве (это значение по умолчанию для чисел).
'='     Принудительно размещает заполнение после знака (если есть), но перед цифрами. 
        Это используется для печати полей в форме «+000000120». 
        Этот параметр выравнивания действителен только для числовых типов. 
        Он становится значением по умолчанию для чисел, когда «0» непосредственно предшествует ширине поля.
'^'     Центрирует поле в доступном пространстве.
Параметр знака действителен только для числовых типов и может быть одним из следующих:

Вариант Значение

'+'     указывает, что знак должен использоваться как для положительных, так и для отрицательных чисел.
'-'     указывает, что знак следует использовать только для отрицательных чисел (это поведение по умолчанию).
spase   указывает, что перед положительными числами следует использовать начальный пробел, а перед отрицательными — знак минус.

Параметр 'z'приводит отрицательные нулевые значения с плавающей запятой к положительным нулям после округления до точности формата. 
Этот параметр действителен только для типов представления с плавающей запятой.


Опция '#' приводит к использованию «альтернативной формы» для преобразования. 
          Альтернативная форма определяется по-разному для разных типов. 
          Этот параметр действителен только для целых, плавающих и сложных типов. 
          Для целых чисел, когда используется двоичный, восьмеричный или шестнадцатеричный вывод, 
          эта опция добавляет соответствующий префикс '0b', '0o', '0x'или '0X'к выходному значению. 
          Для чисел с плавающей запятой и сложных альтернативная форма приводит к тому, что результат 
          преобразования всегда содержит символ десятичной точки, даже если за ним не следуют цифры. 
          Обычно символ десятичной точки появляется в результате этих преобразований только в том случае, 
          если за ним следует цифра. Кроме того, для преобразований 'g'и 'G' конечные нули не удаляются из результата.
Опция ','сигнализирует об использовании запятой для разделителя тысяч. 
         Для разделителя, учитывающего локаль, 'n'вместо этого используйте целочисленный тип представления.
Опция '_'сигнализирует об использовании подчеркивания для разделителя тысяч для типов представления с плавающей 
         запятой и для целочисленного типа представления 'd'. 
         Для целочисленных типов представления 'b', 'o', 'x'и 'X'символы подчеркивания будут вставлены 
         через каждые 4 цифры. Для других типов презентаций указание этой опции является ошибкой.
ширина — десятичное целое число, определяющее минимальную общую ширину поля, включая все префиксы, 
        разделители и другие символы форматирования. Если не указано, то ширина поля будет определяться содержимым.
Если явное выравнивание не задано, перед полем ширины'0' ставится нулевой символ ( ), 
        что позволяет использовать заполнение нулями с учетом знака для числовых типов. 
        Это эквивалентно символу заполнения'0' с типом выравнивания'=' .
установка перед полем ширины'0' больше не влияет на выравнивание строк по умолчанию.

Точность представляет собой десятичное целое число , указывающее, сколько цифр должно отображаться после десятичной 
точки для типов представления 'f'и 'F', или до и после десятичной точки для типов представления 'g'или 'G'. 
Для типов строкового представления поле указывает максимальный размер поля, другими словами, сколько символов 
будет использовано из содержимого поля. Точность не допускается для целочисленных типов представления .


Доступные типы представления строк:

Тип    Значение
's'    Формат строки. Это тип по умолчанию для строк, и его можно опустить.
None   То же, что 's'.

Доступные типы целочисленного представления:

Тип   Значение
'b'   Двоичный формат. Выводит число по основанию 2.
'c'   Характер. Преобразует целое число в соответствующий символ Юникода перед печатью.
'd'   Десятичное целое. Выводит число в базе 10.
'o'   Восьмеричный формат. Выводит число по основанию 8.
'x'   Шестнадцатеричный формат. Выводит число по основанию 16, используя строчные буквы для цифр выше 9.
'X'   Шестнадцатеричный формат. Выводит число по основанию 16, используя прописные буквы для цифр выше 9. Если '#'указано, префикс '0x'также будет прописным '0X'.
'n'   Число. Это то же самое 'd', что и , за исключением того, что он использует текущую настройку локали для вставки соответствующих символов-разделителей чисел.
None  То же, что ' 

Доступные типы представления для floatи Decimalзначений:

Тип    Значение
'e'    Научная нотация. Для заданной точности pформатирует число в экспоненте с буквой «e», отделяющей коэффициент от показателя степени. 
       Коэффициент имеет одну цифру до и pцифры после запятой, всего значащих цифр. 
       Без заданной точности использует точность цифр после запятой для и показывает все цифры коэффициента для. 
       Если за десятичной точкой не следуют цифры, десятичная точка также удаляется, если не используется этот параметр.p + 16floatDecimal#
'E'    Научная нотация. То же, что и 'e'за исключением того, что в качестве символа-разделителя используется заглавная буква «E».
'f'    Обозначение с фиксированной точкой. Для заданной точности pформатирует число как десятичное число, 
       в котором pпосле запятой следуют только цифры. 
       Без заданной точности использует точность 6цифр после запятой для floatи использует точность, 
       достаточную для отображения всех цифр коэффициента для Decimal. 
       Если за десятичной точкой не следуют цифры, десятичная точка также удаляется, если не #используется этот параметр.
'F'    Обозначение с фиксированной точкой. То же , что и 'f', но преобразуется nanв NANи infв INF.
'g'    Общий формат. Для заданной точности это округляет число до значащих цифр, а затем форматирует результат 
       либо в формате с фиксированной запятой, либо в экспоненциальном представлении, в зависимости от его величины. 
       Точность рассматривается как эквивалентная точности .p >= 1p01
Точные правила таковы: предположим, что результат, отформатированный с типом представления 'e'и точностью p-1, 
будет иметь показатель степени exp. Затем, если , где -4 для чисел с плавающей запятой и -6 для , число форматируется с типом представления и точностью . 
В противном случае число форматируется с типом представления и точностью . В обоих случаях из мантиссы удаляются незначащие конечные нули, а также 
удаляется десятичная точка, если за ней не следуют оставшиеся цифры, если не используется опция.m <= exp < pmDecimals'f'p-1-exp'e'p-1'#'
Без заданной точности использует точность 6 значащих цифр для float. При Decimalкоэффициент результата формируется из цифр коэффициента значения; 
научное обозначение используется для значений, меньших 1e-6абсолютного значения, и значений, 
в которых разрядное значение младшей значащей цифры больше 1, а в противном случае используется обозначение с фиксированной запятой.
Положительная и отрицательная бесконечность, положительные и отрицательные нули и нанс форматируются как , , и infсоответственно -inf, 0независимо от точности.-0nan
'G'    Общий формат. То же, что и 'g'за исключением переключения, 'E'если число становится слишком большим. Представления бесконечности и NaN также в верхнем регистре.
'n'    Число. Это то же самое 'g', что и , за исключением того, что он использует текущую настройку локали для вставки соответствующих символов-разделителей чисел.
'%'    Процент. Умножает число на 100 и отображает в фиксированном ( 'f') формате, за которым следует знак процента.
Никто  Поскольку floatэто то же самое 'g', что и , за исключением того, что когда для форматирования результата используется запись с 
фиксированной точкой, он всегда включает по крайней мере одну цифру после десятичной точки. Используемая точность настолько велика, насколько это необходимо для точного представления заданного значения.
Для Decimalэто то же самое, что 'g'или 'G'в зависимости от значения context.capitalsдля текущего десятичного контекста. 
Общий эффект заключается в том, чтобы соответствовать выходным данным str() , измененным другими модификаторами формата.



Доступ к аргументам по позиции:

```python
'{0}, {1}, {2}'.format('a', 'b', 'c')
'a, b, c'
'{}, {}, {}'.format('a', 'b', 'c')  # 3.1+ only
'a, b, c'
'{2}, {1}, {0}'.format('a', 'b', 'c')
'c, b, a'
'{2}, {1}, {0}'.format(*'abc')      # unpacking argument sequence
'c, b, a'
'{0}{1}{0}'.format('abra', 'cad')   # arguments' indices can be repeated
'abracadabra'
```

Доступ к аргументам по имени:

```python
'Coordinates: {latitude}, {longitude}'.format(latitude='37.24N', longitude='-115.81W')
'Coordinates: 37.24N, -115.81W'
coord = {'latitude': '37.24N', 'longitude': '-115.81W'}
'Coordinates: {latitude}, {longitude}'.format(**coord)
'Coordinates: 37.24N, -115.81W'
```

Доступ к атрибутам аргументов:

```python
c = 3-5j
('The complex number {0} is formed from the real part {0.real} '
 'and the imaginary part {0.imag}.').format(c)
'The complex number (3-5j) is formed from the real part 3.0 and the imaginary part -5.0.'
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __str__(self):
        return 'Point({self.x}, {self.y})'.format(self=self)

str(Point(4, 2))
'Point(4, 2)'
```

Доступ к элементам аргументов:

```python
coord = (3, 5)
'X: {0[0]};  Y: {0[1]}'.format(coord)
'X: 3;  Y: 5'

Замена %sи %r:
"repr() shows quotes: {!r}; str() doesn't: {!s}".format('test1', 'test2')
"repr() shows quotes: 'test1'; str() doesn't: test2"
```

Выравнивание текста и указание ширины:

```python
'{:<30}'.format('left aligned')
'left aligned                  '
'{:>30}'.format('right aligned')
'                 right aligned'
'{:^30}'.format('centered')
'           centered           '
'{:*^30}'.format('centered')  # use '*' as a fill char
'***********centered***********'
```

Замена %+f, %-f, и и указание знака:% f

```python
'{:+f}; {:+f}'.format(3.14, -3.14)  # show it always
'+3.140000; -3.140000'
'{: f}; {: f}'.format(3.14, -3.14)  # show a space for positive numbers
' 3.140000; -3.140000'
'{:-f}; {:-f}'.format(3.14, -3.14)  # show only the minus -- same as '{:f}; {:f}'
'3.140000; -3.140000'
```

Замена %xи %oпреобразование значения в разные базы:

```python
# format also supports binary numbers
"int: {0:d};  hex: {0:x};  oct: {0:o};  bin: {0:b}".format(42)
'int: 42;  hex: 2a;  oct: 52;  bin: 101010'
# with 0x, 0o, or 0b as prefix:
"int: {0:d};  hex: {0:#x};  oct: {0:#o};  bin: {0:#b}".format(42)
'int: 42;  hex: 0x2a;  oct: 0o52;  bin: 0b101010'
```

Использование запятой в качестве разделителя тысяч:

```python
'{:,}'.format(1234567890)
'1,234,567,890'
```

Выражение процента:

```python
points = 19
total = 22
'Correct answers: {:.2%}'.format(points/total)
'Correct answers: 86.36%'
```

Использование форматирования для конкретного типа:

```python
import datetime
d = datetime.datetime(2010, 7, 4, 12, 15, 58)
'{:%Y-%m-%d %H:%M:%S}'.format(d)
'2010-07-04 12:15:58'
```

Вложенные аргументы и более сложные примеры:

```python
for align, text in zip('<^>', ['left', 'center', 'right']):
    '{0:{fill}{align}16}'.format(text, fill=align, align=align)

'left<<<<<<<<<<<<'
'^^^^^center^^^^^'
'>>>>>>>>>>>right'
octets = [192, 168, 0, 1]
'{:02X}{:02X}{:02X}{:02X}'.format(*octets)
'C0A80001'
int(_, 16)
3232235521
width = 5
for num in range(5,12): 
    for base in 'dXob':
        print('{0:{width}{base}}'.format(num, base=base, width=width), end=' ')
    print()

#    5     5     5   101
#    6     6     6   110
#    7     7     7   111
#    8     8    10  1000
#    9     9    11  1001
#   10     A    12  1010
#   11     B    13  1011
```








Форматирование чисел:
Для вывода количества знаков после запятой можно использовать флаг f:

```python
print(f"pi {22 / 7:.2f}")
```

Форматирование строк:

```python
print(f"{name.upper():<10}") # выравнивается в лево на 10 символов
print(f"{name.upper():>10}") # выравнивается в право на 10 символов
print(f"{name.upper():^10}") # выравнивается по центру шириной 10 символов
print(f"{22/7:>10.2f}")      # выравнивает в право на 10 и оставляет два знака после точки
```

Форматирование строк может быть улучшено с помощью флагов:

```python
print(f"{name.upper():=^10}") # CENTERED WITH 10 CHARACTERS WIDTH AND FILLED WITH "="
```

```python
class Person:
    def __format__(self, format_spec):
        return "Person Object"

p = Person()
print(f"{p}") # Person Object
```
""",
            "print(file=)": """
```python
with open('output.txt', 'w') as f:
    print('Hello, world!', file=f)
```
""",
            "for in list comprehension": """
```python
list_of_tuples = [(1, 2), (3, 4), (5, 6)]

result_list = [item for tpl in list_of_tuples for item in tpl]

print(result_list) # [1, 2, 3, 4, 5, 6]
```

==

```python
list_of_tuples = [(1, 2), (3, 4), (5, 6)]
result_list = []
for tpl in list_of_tuples:
    for item in tpl:
        result_list.append(item)
        
print(result_list) # [1, 2, 3, 4, 5, 6]
```
""",
            "Умножение списков": """
```python-console
>>> a = [[]]*3
>>> [print(id(x)) for x in a]
 2725519109056
 2725519109056
 2725519109056
>>> a[1].append(1)
>>> a
[[1], [1], [1]]
>>>
>>> b = [[] for _ in range(3)]
>>> [print(id(x)) for x in b]
 2725519148736
 2725519105984
 2725519108352
>>>
>>> c = [[]]
>>> print(id(c[0]))
2014139788672
>>> [id(x) for x in (c + c)]
[2014139788672, 2014139788672]
>>>
```
""",
            "yield from": """
yield from - это выражение, которое позволяет делегировать выполнение генератора другому генератору, который называется подгенератором. 
Это означает, что когда генератор встречает выражение yield from с указанием подгенератора, он передает управление этому подгенератору, 
который затем возвращает значения генерируемых им элементов непосредственно в генератор-делегат.

Кроме того, yield from позволяет пропустить передачу через промежуточный уровень вложенности. 
Это означает, что когда подгенератор завершает свою работу, управление передается автоматически обратно генератору-делегату. 
Это может быть полезно в случаях, когда вы хотите объединить несколько генераторов вместе, чтобы создать новый генератор, который генерирует элементы из каждого из них.

Вот пример, который демонстрирует использование yield from:

```python
def generator1():
    yield 'A'
    yield 'B'
    yield 'C'

def generator2():
    yield 'D'
    yield from generator1()
    yield 'E'
    yield 'F'

[letter for letter in generator2()] # ['D', 'A', 'B', 'C', 'E', 'F']
```

Здесь generator2 создает новый генератор, используя yield from 
для вызова генератора generator1 и объединения его с другими элементами, которые генерирует generator2. 
Когда generator1 завершает свою работу, управление автоматически возвращается обратно в generator2, который продолжает генерировать свои элементы.
""",
            "PyCharm": """
В PyCharm вы можете использовать TODO комментарий для отслеживания задач, которые необходимо выполнить в вашем коде. 
Вот как вы можете добавлять TODO элементы и управлять ими в PyCharm:

Введите TODO ключевое слово, а затем описание задачи в комментарии, 
например: # TODO fix this code.

Выберите View> Tool Windows> TODO, чтобы открыть окно инструментов TODO.
В окне инструмента TODO вы увидите список всех TODO элементов вашего кода, сгруппированных по номеру файла и строки.
Вы можете дважды щелкнуть элемент TODO, чтобы перейти к его местоположению в коде.
Чтобы пометить элемент TODO как выполненный, вы можете удалить его или заменить TODO ключевое слово на DONE.

Примечание. 
Окно инструментов TODO также поддерживает настраиваемые фильтры, 
поэтому вы можете настроить, какие элементы TODO будут отображаться и в каком порядке. 
Чтобы настроить фильтры, перейдите в Settings> Appearance & Behavior> TODO.
""",
            "import": """
```python-console
>>> def im(): import math
...
>>> math
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'math' is not defined
>>> im()
>>> math
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'math' is not defined
```

```python
import importlib

importlib.reload(my_module)
```

```python
import subprocess
import importlib

library_name = input("Введите название библиотеки, которую вы хотите установить: ")

# проверяем, установлена ли библиотека
try:
    importlib.import_module(library_name)
    print(f"Библиотека {library_name} уже установлена.")
except ImportError:
    # устанавливаем библиотеку
    subprocess.call(['pip', 'install', library_name])
    print(f"Библиотека {library_name} установлена успешно.")

```
""",
            "Встроенные функции": r"""
slice frozenset memoryview, hasattr, reversed, __import__, staticmethod, setattr, property, object, 
locals, globals, getattr, complex, compile, bytearray, abs, bin, bytes, callable, chr, classmethod, 
delattr, dir, divmod, filter, oct, nonlocal


slice - используется для создания срезов (slice) из последовательности (sequence), таких как строки, списки, кортежи и т.д. Пример:

```python
my_list = [1, 2, 3, 4, 5]
slice_obj = slice(1, 4)
print(my_list[slice_obj])  # Output: [2, 3, 4]
```

frozenset - это неизменяемый тип данных, представляющий собой неупорядоченное множество уникальных элементов. Пример:

```python
my_set = frozenset([1, 2, 2, 3, 4])
print(my_set)  # Output: frozenset({1, 2, 3, 4})
```

memoryview - используется для доступа к буферу памяти объекта без копирования его данных. Пример:

```python
my_bytes = bytes([1, 2, 3, 4, 5])
my_memory_view = memoryview(my_bytes)
print(my_memory_view[1])  # Output: 2
```

hasattr - используется для проверки наличия атрибута (метода или свойства) у объекта. Пример:

```python
class MyClass:
    def __init__(self):
        self.my_attr = 42

my_obj = MyClass()
print(hasattr(my_obj, 'my_attr'))  # Output: True
print(hasattr(my_obj, 'non_existent_attr'))  # Output: False
```

reversed - используется для переворачивания последовательности (sequence). Пример:

```python
my_list = [1, 2, 3, 4, 5]
reversed_list = reversed(my_list)
print(list(reversed_list))  # Output: [5, 4, 3, 2, 1]
```

__import__ - используется для импорта модуля во время выполнения программы. Пример:

```python
my_module = __import__('math')
print(my_module.pi)  # Output: 3.141592653589793
```

staticmethod - используется для создания метода класса, который не принимает первый аргумент self (или cls для методов класса). Пример:

```python
class MyClass:
    @staticmethod
    def my_static_method():
        print('This is a static method')

MyClass.my_static_method()  # Output: This is a static method
```

setattr - используется для установки значения атрибута объекта. Пример:

```python
class MyClass:
    def __init__(self):
        self.my_attr = 42

my_obj = MyClass()
setattr(my_obj, 'my_attr', 43)
print(my_obj.my_attr)  # Output: 43
```

property - используется для создания свойства объекта, которое можно читать и записывать, как обычный атрибут. Пример:

```python
class MyClass:
    def __init__(self):
        self._my_attr = 42

    @property
    def my_attr(self):
        return self._my_attr

    @my_attr.setter
    def my_attr(self, value):
        self._my_attr
```

object - это базовый класс, от которого наследуются все остальные классы в Python. Пример:

```python
class MyClass(object):
    pass
```

locals - используется для получения словаря с локальными переменными в текущем контексте выполнения. Пример:

```python
def my_func():
    a = 1
    b = 2
    print(locals())

my_func()  # Output: {'a': 1, 'b': 2}
```

globals - используется для получения словаря с глобальными переменными в текущем модуле. Пример:

```python
my_var = 42
print(globals())  # Output: {'__name__': '__main__', '__doc__': None, '__package__': None, 'my_var': 42, ...}
```

getattr - используется для получения значения атрибута объекта по его имени. Пример:

```python
class MyClass:
    def __init__(self):
        self.my_attr = 42

my_obj = MyClass()
print(getattr(my_obj, 'my_attr'))  # Output: 42
```

complex - используется для создания комплексного числа. Пример:

```python
my_complex = complex(1, 2)
print(my_complex)  # Output: (1+2j)
```

compile - используется для компиляции строки с кодом Python в объект-код. Пример:

```python
my_code = 'print("Hello, world!")'
my_compiled_code = compile(my_code, '<string>', 'exec')
exec(my_compiled_code)  # Output: Hello, world!
```

bytearray - это изменяемый тип данных, представляющий собой массив байтов. Пример:

```python
my_bytearray = bytearray([1, 2, 3, 4, 5])
print(my_bytearray)  # Output: bytearray(b'\x01\x02\x03\x04\x05')
```

abs - используется для получения абсолютного значения числа. Пример:

```python
my_num = -42
print(abs(my_num))  # Output: 42
```

bin - используется для получения двоичного представления числа. Пример:

```python
my_num = 42
print(bin(my_num))  # Output: 0b101010
```

bytes - это неизменяемый тип данных, представляющий собой массив байтов. Пример:

```python
my_bytes = bytes([1, 2, 3, 4, 5])
print(my_bytes)  # Output: b'\x01\x02\x03\x04\x05'
```

callable - используется для проверки, является ли объект вызываемым (т.е. функцией или методом). Пример:

```python
def my_func():
    pass

class MyClass:
    def my_method(self):
        pass

print(callable(my_func))  # Output: True
print(callable(MyClass().my_method))  # Output: True
print(callable(42))  # Output: False
```

chr - используется для получения символа Unicode по его коду. Пример:

```python
my_char = chr(97)
print(my_char)  # Output: 'a'
```

classmethod - используется для создания метода класса. Этот метод может быть вызван без создания экземпляра класса. Пример:

```python
class MyClass:
    my_class_attr = 42

    @classmethod
    def my_class_method(cls):
        print(cls.my_class_attr)

MyClass.my_class_method()  # Output: 42
```

delattr - используется для удаления атрибута объекта. Пример:

```python
class MyClass:
    my_attr = 42

my_obj = MyClass()
delattr(my_obj, 'my_attr')
print(hasattr(my_obj, 'my_attr'))  # Output: False
```

dir - используется для получения списка всех атрибутов объекта. Пример:

```python
my_list = [1, 2, 3]
print(dir(my_list))  # Output: ['__add__', '__class__', '__contains__', ...]
```

divmod - используется для получения частного и остатка от деления двух чисел. Пример:

```python
my_divmod = divmod(42, 5)
print(my_divmod)  # Output: (8, 2)
```

filter - используется для фильтрации элементов последовательности с помощью функции. Пример:

```python
my_list = [1, 2, 3, 4, 5]
my_filtered_list = list(filter(lambda x: x % 2 == 0, my_list))
print(my_filtered_list)  # Output: [2, 4]
```

oct - используется для получения восьмеричного представления числа. Пример:

```python
my_num = 42
print(oct(my_num))  # Output: 0o52
```

nonlocal - используется для объявления переменной из внешней области видимости внутри функции. Пример:

```python
def my_func():
    my_var = 42
    def inner_func():
        nonlocal my_var
        my_var = 43
    inner_func()
    print(my_var)

my_func()  # Output: 43
```
""",
            "Аннотации типов": """
```python
from typing import Any # Любой тип
```

```python
from typing import Literal # Один из вариантов
direction: Literal["ASC", "DESC"] = "DESC"
```

```python
from typing import Union
val: Union[int, float] = 20.8 # or 20
```

```python
from typing import Final

val: Final = 2
val += 1 # Ошибки не произойдёт, но idle подсветит как ошибку.
```

# Использование статической проверки типов в Python
Интерпретатор Python по умолчанию не осуществляет проверку типов.
Однако была создана версия интерпретатора Python – mypy,
которая обеспечивает проверку типов на уровне интерпретатора.

```python
from typing import NoReturn
# NoReturn сообщает что функция не завершается нормально.
# Например она возбуждает исключение.

def forever() -> NoReturn:
    while True:
        pass
```

Если это генераторная функция, то есть её тело содержит оператор yield, 
для возвращаемого можно воспользоваться аннотацией `Iterable[T]`, либо `Generator[YT, ST, RT]`:

```python
def generate_two() -> Iterable[int]:
    yield 1
    yield "2"  # Incompatible types in "yield" (actual type "str", expected type "int")
```

```python
from typing import Optional

amount: int
amount = None  # Incompatible types in assignment (expression has type "None", variable has type "int")

price: Optional[int]
price = None

# Аннотация Optional[T] эквивалентна Union[T, None], хотя такая запись и не рекомендуется.
```

Предварительное объявление

Обычно вы не можете использовать тип до того, как он создан. Например, следующий код даже не запустится:

```python
class LinkedList:
    data: Any
    next: LinkedList  # NameError: name 'LinkedList' is not defined
```

Чтобы это исправить, допустимо использовать строковый литарал. В этом случае аннотации будут вычислены отложенно.

```python
class LinkedList:
    data: Any
    next: 'LinkedList'
```

Так же вы можете обращаться к классам из других модулей (конечно, если модуль импортирован):

```python
some_variable: 'somemodule.SomeClass'
```

или

```python
from __future__ import annotations

class LinkedList:
    data: int
    next: LinkedList
```

# Generic-типы

Иногда необходимо сохранить информацию о типе, при этом не фиксируя его жестко.
Например, если вы пишете контейнер, который хранит однотипные данные.
Или функцию, которая возвращает данные того же типа, что и один из аргументов.

Такие типы как List или Callable, которые, мы видели раньше как раз используют механизм дженериков.
Но кроме стандартных типов, вы можете создать свои дженерик-типы.
Для этого надо, во-первых, завести TypeVar переменную,
которая будет атрибутом дженерика, и, во-вторых,непосредственно объявить generic-тип:

```python
T = TypeVar("T")

class LinkedList(Generic[T]):
    data: T
    next: "LinkedList[T]"

    def __init__(self, data: T):
        self.data = data

head_int: LinkedList[int] = LinkedList(1)
head_int.next = LinkedList(2)
head_int.next = 2  # error: Incompatible types in assignment (expression has type "int", variable has type "LinkedList[int]")
head_int.data += 1
head_int.data.replace("0", "1")  # error: "int" has no attribute "replace"

head_str: LinkedList[str] = LinkedList("1")
head_str.data.replace("0", "1")

head_str = LinkedList[str](1)  # error: Argument 1 to "LinkedList" has incompatible type "int"; expected "str"
```

Как вы можете заметить, для generic-типов работает автоматический вывод типа параметра.
Если требуется, дженерик может иметь любое количеством параметров: Generic[T1, T2, T3].
Также, при определении TypeVar вы можете ограничить допустимые типы:

```python
T2 = TypeVar("T2", int, float)

class SomethingNumeric(Generic[T2]):
    pass

x = SomethingNumeric[str]()  # error: Value of type variable "T2" of "SomethingNumeric" cannot be "str"
```

# Cast

Иногда анализатор статический анализатор не может корректно определить тип переменной,
в этом случае можно использовать функцию cast.
Её единственная задача — показать анализатору, что выражение имеет определённый тип.
Например:

```python
from typing import List, cast

def find_first_str(a: List[object]) -> str:
    index = next(i for i, x in enumerate(a) if isinstance(x, str))
    return cast(str, a[index])
```

Также это может быть полезно для декораторов:

```python
MyCallable = TypeVar("MyCallable", bound=Callable)

def logged(func: MyCallable) -> MyCallable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(func.__name__, args, kwargs)
        return func(*args, **kwargs)

    return cast(MyCallable, wrapper)

@logged
def mysum(a: int, b: int) -> int:
    return a + b

mysum(a=1)  # error: Missing positional argument "b" in call to "mysum"
```
"""
        },
        "SQL": {
            "Разное": """+------------------------------------------------------------------------------------------+
| Индексирование базы данных                                                               |
|     +----------------------------------------------------------------------------------+ |
|     | Процесс создания специальной структуры данных, которая позволяет быстро          | |
|     | находить нужные записи в базе данных. Индексы могут быть созданы для отдельных   | |
|     | полей или сочетаний полей в таблице базы данных. Как правило, индексы            | |
|     | упорядочивают записи в базе данных по определенному полю или полям,              | |
|     | что позволяет быстро находить нужные записи путем поиска в упорядоченном списке. | |
|     | Индексы также могут улучшить производительность базы данных при выполнении       | |
|     | различных операций, таких как сортировка и группировка данных.                   | |
|     +----------------------------------------------------------------------------------+ |
| AVERAGE (функция среднего)                                                               |
|     +----------------------------------------------------------------------------------+ |
|     | Функция, которая вычисляет среднее значение выборки данных.                      | |
|     | Она работает так: суммирует все значения в выборке и                             | |
|     | делит результат на количество значений.                                          | |
|     | Например, если у нас есть таблица с четырьмя строками и одним столбцом,          | |
|     | содержащим числа 10, 20, 30 и 40, то среднее значение будет равно 25.            | |
|     | Это можно посчитать, суммируя все числа (10 + 20 + 30 + 40)                      | |
|     | и деля полученный результат (100) на количество чисел (4), что даст 25.          | |
|     +----------------------------------------------------------------------------------+ |
| Оконные функции                                                                          |
|     +----------------------------------------------------------------------------------+ |
|     | Функции баз данных, которые выполняют операции над наборами данных,              | |
|     | называемыми "окнами". Окна - это наборы строк в таблице, которые определяются    | |
|     | каким-либо критерием (например, временным интервалом,                            | |
|     | порядковым номером и т. д.).                                                     | |
|     | Оконные функции позволяют совершать различные операции над этими наборами строк, | |
|     | например, вычислять агрегатные функции (среднее, сумма, минимум и т. д.),        | |
|     | применять фильтры и группировки, выполнять ранжирование.                         | |
|     | Оконные функции обычно используются с оператором OVER, который определяет        | |
|     | окно данных, над которыми будут выполняться операции.                            | |
|     | Например, чтобы вычислить среднее значение поля "Зарплата" для каждой строки     | |
|     | в таблице, можно использовать следующий запрос:                                  | |
|     +----------------------------------------------------------------------------------+ |
|     | SELECT AVERAGE(Salary) OVER (PARTITION BY Department) FROM Employees;            | |
|     +----------------------------------------------------------------------------------+ |
|     | В этом примере функция AVERAGE вычисляет среднее                                 | |
|     | значение поля "Зарплата" для каждой группы строк                                 | |
|     +----------------------------------------------------------------------------------+ |
| PARTITION BY                                                                             |
|     +----------------------------------------------------------------------------------+ |
|     | Это часть оконных функций в базах данных, который используется для разбиения     | |
|     | набора строк на группы, называемые "партициями".Каждая партиция - это набор строк| |
|     | с общими свойствами, определяемыми критерием, указанным в PARTITION BY           | |
|     | Может использоваться совместно с другими операторами,                            | |
|     | такими как ORDER BY и ROWS/RANGE, чтобы определить окно данных более точно.      | |
|     | Например, чтобы вычислить среднее значение поля "Зарплата" для каждого отдела,   | |
|     | но учитывая только последние 3 месяца, можно использовать следующий запрос:      | |
|     +----------------------------------------------------------------------------------+ |
|     | SELECT AVERAGE(Salary)                                                           | |
|     | OVER (PARTITION BY Department                                                    | |
|     |       ORDER BY Month ROWS BETWEEN 2 PRECEDING AND CURRENT ROW)                   | |
|     | FROM Employees;                                                                  | |
|     +----------------------------------------------------------------------------------+ |
|     | В этом примере функция AVERAGE будет вычислять среднее значение поля "Зарплата"  | |
|     | для каждой партиции (то есть для каждого отдела), учитывая только строки,        | |
|     | упорядоченные по полю "Месяц" и относящиеся к                                    | |
|     | последним 3 месяцам (включая текущий).                                           | |
|     +----------------------------------------------------------------------------------+ |
| PRECEDING                                                                                |
|     +----------------------------------------------------------------------------------+ |
|     | Это часть оконных функций в базах данных, который используется для               | |
|     | определения окна данных в терминах количества строк,                             | |
|     | находящихся до текущей строки.                                                   | |
|     | Например, чтобы вычислить сумму последних 3 строк в таблице,                     | |
|     | можно использовать следующий запрос:                                             | |
|     +----------------------------------------------------------------------------------+ |
|     | SELECT SUM(Value)                                                                | |
|     | OVER (ORDER BY Id ROWS BETWEEN 2 PRECEDING AND CURRENT ROW)                      | |
|     | FROM Table;                                                                      | |
|     +----------------------------------------------------------------------------------+ |
|     | В этом примере функция SUM будет вычислять сумму значений поля "Value"           | |
|     | для каждой строки, учитывая только строки, упорядоченные по полю "Id"            | |
|     | и находящиеся до текущей строки на 2 строки (включая текущую).                   | |
|     | Оператор PRECEDING может использоваться совместно с другими операторами,         | |
|     | такими как PARTITION BY и RANGE, чтобы определить окно данных более точно.       | |
|     +----------------------------------------------------------------------------------+ |
+------------------------------------------------------------------------------------------+
""",
            "JOIN": """
- JOIN
    Используется для соединения двух таблиц в одну.
    Существует ряд различных видов JOIN, каждый из которых имеет свои особенности
    и применяется в зависимости от ситуации.
    INNER JOIN, LEFT JOIN, RIGHT JOIN, FULL OUTER JOIN,
    CROSS JOIN, NATURAL JOIN, UNION JOIN, STRAIGHT_JOIN, OUTER APPLY, CROSS APPLY

- INNER JOIN - это самый распространенный вид JOIN
    Соединяет две таблицы по совпадающим значениям определенных полей.
    Результатом является таблица, содержащая только те строки,
    которые совпадают по заданным полям.

- LEFT JOIN аналогичен INNER JOIN
    Результирующая таблица содержит все строки из левой (первой) таблицы,
    даже если они не совпадают по заданным полям со второй таблицей.
    Несовпадающие строки заполняются нулевыми значениями

- RIGHT JOIN аналог LEFT JOIN
    Результирующая таблица содержит все строки из правой (второй) таблицы,
    даже если они не совпадают по заданным полям с первой таблицей.
    Несовпадающие строки заполняются нулевыми значениями.

- FULL OUTER JOIN комбинация LEFT JOIN и RIGHT JOIN.
    Результирующая таблица содержит все строки из обоих таблиц,
    даже если они не совпадают по заданным полям.
    Несовпадающие строки заполняются нулевыми значениями.

```sql
SELECT * FROM Table1
FULL OUTER JOIN Table2
ON Table1.Field1 = Table2.Field1;
```

- CROSS JOIN
    соединяет все строки из первой таблицы со всеми строками из второй таблицы,
    создавая картежи, удовлетворяющие условию соединения.
    Таким образом, CROSS JOIN не учитывает совпадающие
    значения в таблицах и создает все возможные картежи.

```sql
SELECT * FROM Table1
CROSS JOIN Table2;
```
""",
            "Операторы": """Операторы:
SELECT - используется для извлечения данных из базы данных. 
         Он может быть использован с другими операторами, такими как FROM, WHERE и GROUP BY, 
         чтобы определить, какие данные должны быть извлечены, из каких таблиц и с какими условиями.
         - SELECT - какие колонки данных вы хотите извлечь.
         - FROM - из какой таблицы нужно извлечь данные.
         - WHERE - условие, которое должны соответствовать строки, чтобы быть включенными в результат.
         - GROUP BY - какие колонки нужно использовать для группировки результата.
         - HAVING - для фильтрации групп результата запроса. Он похож на оператор WHERE, 
                    но он используется с оператором GROUP BY и применяется только к группам, а не к отдельным строкам.
         - ORDER BY - какие колонки нужно использовать для сортировки результата, 
                      а также порядок сортировки (по возрастанию или убыванию (ASC|DESC))
         - JOIN - используется для соединения двух таблиц в базе данных. 
                  Он может быть использован с различными типами JOIN, такими как INNER JOIN, LEFT JOIN и RIGHT JOIN, 
                  чтобы определить, какие строки из обеих таблиц должны быть соединены.
         SELECT column1, column2, ...
         FROM     __table_name
         WHERE    __condition
         GROUP BY __column
         HAVING   __condition
         ORDER BY __column ASC|DESC;

JOIN - это оператор SQL, который используется для соединения двух или более таблиц в базе данных. 
       Он позволяет вам извлекать данные из разных таблиц и объединять их в одном результате.
       Существует разные типы JOIN, которые используются в зависимости от требуемого результата. Основные типы JOIN это:
       INNER JOIN - этот тип JOIN возвращает строки, которые содержатся в обоих таблицах.
       OUTER JOIN - этот тип JOIN возвращает все строки из обоих таблиц, даже если они не совпадают. 
                    Существует два вида внешних JOIN: LEFT JOIN и RIGHT JOIN.
       CROSS JOIN - этот тип JOIN используется для создания картежного произведения двух таблиц. 
                    Он возвращает все возможные комбинации строк из двух таблиц, даже если у них нет совпадений.
       SELECT column1, column2, ... FROM table1 CROSS JOIN table2;

FULL OUTER JOIN - используется для соединения двух таблиц. 
                  Он возвращает все строки из обеих таблиц, даже если у них нет совпадений. 
                  Если соответствующих строк нет в одной из таблиц, то в качестве значений используются NULL.
                  SELECT column1, column2, ... FROM table1 FULL OUTER JOIN table2 ON table1.column = table2.column;

INSERT - используется для вставки новых строк в таблицу базы данных. 
         Он может быть использован с VALUES и SELECT, DEFAULT VALUES и SET, 
         чтобы определить, какие данные нужно вставить и откуда их взять.

UPDATE - используется для обновления существующих строк в таблице базы данных. 
         Он может быть использован с оператором SET, чтобы указать, какие значения должны быть обновлены, 
         и с оператором WHERE, чтобы указать, какие строки должны быть обновлены.
         UPDATE table_name SET column1 = value1, column2 = value2, ... WHERE condition;

DELETE - используется для удаления строк из таблицы базы данных. 
         Он может быть использован с оператором WHERE, чтобы указать, какие строки должны быть удалены. 
         Если оператор WHERE не указан, то будут удалены все строки из таблицы. 
         DELETE FROM table_name WHERE condition;

CREATE - используется для создания объектов в базе данных, таких как таблицы, индексы, представления, триггеры и т. д. 
         Он может быть использован с TABLE, INDEX, VIEW, TRIGGER, чтобы указать, какой тип объекта нужно создать.
         CREATE object_type object_name (column1 datatype, column2 datatype, ...);

DROP - используется для удаления объектов из базы данных, таких как таблицы, индексы, представления, триггеры и т. д. 
       Он может быть использован c TABLE, INDEX, VIEW, TRIGGER, чтобы указать, какой тип объекта нужно удалить. 
       DROP object_type object_name;

ALTER - используется для изменения структуры существующих объектов в базе данных, 
        таких как таблицы, индексы, представления, триггеры и т. д. 
        Он может быть использован с ADD, DROP, MODIFY, ALTER, чтобы указать, какое изменение нужно внести.
        ALTER object_type object_name action;
        Например, чтобы добавить столбец email к таблице customers, вы можете использовать следующий запрос:
        ALTER TABLE customers ADD email VARCHAR(255);
        Или, чтобы удалить столбец age из таблицы customers, вы можете использовать следующий запрос:
        ALTER TABLE customers DROP age;

TRUNCATE - используется для удаления всех строк из таблицы базы данных. 
           Он отличается от оператора DELETE, тем что он удаляет все строки из таблицы без проверки условий, 
           а также очищает данные страниц таблицы, что позволяет сократить время выполнения и уменьшить размер таблицы.  
           TRUNCATE TABLE table_name;
           (Обратите внимание, что оператор TRUNCATE не может быть отменен, поэтому используйте его с осторожностью.)

WHERE - это оператор SQL, который используется для фильтрации строк в результате запроса. 
        Он может быть использован с операторами SELECT, UPDATE, DELETE и другими, 
        чтобы указать, какие строки должны быть включены в результат или изменены.
        SELECT column1, column2, ...
        FROM table_name
        WHERE condition;

AND - это логическое условие, используется в операторе WHERE в SQL для соединения нескольких условий. 
      Оно возвращает TRUE только в том случае, если все условия равны TRUE.
      SELECT column1, column2, ... FROM table_name WHERE condition1 AND condition2 AND ...;

OR - это логическое условие, используется в операторе WHERE в SQL для соединения нескольких условий. 
     Оно возвращает TRUE, если хотя бы одно из условий равно TRUE. 
     SELECT column1, column2, ... FROM table_name WHERE condition1 OR condition2 OR ...;

NOT - это логическое условие, используется в операторе WHERE в SQL для инвертирования условия. 
      Оно возвращает TRUE, если условие равно FALSE, и наоборот. SELECT column1, column2, ... 
      FROM table_name WHERE NOT condition;
      Обратите внимание, что условие NOT может быть использовано совместно с другими логическими условиями, 
      такими как AND и OR. Например: 
      SELECT * FROM customers WHERE NOT (name = 'John' OR age > 30);

BETWEEN - используется в операторе WHERE для указания диапазона значений. 
          Он возвращает TRUE, если значение равно либо больше начального значения, но меньше конечного значения. 
          SELECT column1, column2, ... FROM table_name WHERE column BETWEEN value1 AND value2;

IN - это оператор SQL, который используется в операторе WHERE для указания набора значений. 
     Он возвращает TRUE, если значение равно любому из указанных значений.
        SELECT column1, column2, ... FROM table_name WHERE column IN (value1, value2, ...);
        Обратите внимание, что условие IN может быть использовано совместно с другими логическими условиями, такими как AND и OR. Например:
        SELECT * FROM customers WHERE (name IN ('John', 'Alice') AND age > 30) OR city = 'New York';

BETWEEN - используется для указания диапазона значений, которые должны соответствовать условию в запросе SQL. 
          эквивалентен использованию оператора ">=" и "<=".
          SELECT * FROM products WHERE price BETWEEN 10 AND 20;

IN - используется для указания списка значений, которые должны соответствовать условию в запросе SQL. 
     используется в качестве альтернативы оператору BETWEEN.
     SELECT * FROM employees WHERE salary IN (40000, 41000, 42000, 43000, 44000, 45000);

LIKE - используется для указания условия совпадения данных с определенным шаблоном. 
       принимает в качестве аргумента строку с специальными символами, которые обозначают любые символы или любое количество символов.
       SELECT * FROM customers WHERE email LIKE 'm%';
       % - соответствует любому количеству символов
       _ - соответствует любому одному символу
       [] - указывает диапазон символов, которые могут совпасть с шаблоном. Например, [a-z] соответствует любому одному символу от a до z.
       [^] - указывает диапазон символов, которые не могут совпасть с шаблоном. Например, [^a-z] соответствует любому символу, кроме a-z.

REGEXP - используется для указания условия совпадения данных с определенным регулярным выражением. 
         Регулярные выражения - это специальный язык, который используется для описания шаблона строки. 
         Они позволяют создавать более сложные условия совпадения, чем может позволить LIKE.
         SELECT * FROM customers WHERE email REGEXP 'gmail';

LIMIT - это оператор SQL, который используется для ограничения количества строк, возвращаемых запросом. 
        Он может быть использован с операторами SELECT, UPDATE и DELETE.
           SELECT column1, column2, ... FROM table_name LIMIT number;
           Например, чтобы выбрать только первые 10 клиентов, вы можете использовать следующий запрос:
           SELECT * FROM customers LIMIT 10;
           Вы также можете указать начальное положение и количество строк, которые должны быть возвращены, указав эти значения в операторе LIMIT. Например:
           SELECT * FROM customers LIMIT 5, 10;

ORDER BY - это оператор SQL, который используется для сортировки результатов запроса. 
           Он может быть использован с операторами SELECT, UPDATE и DELETE.
              SELECT column1, column2, ... FROM table_name ORDER BY column1, column2, ... ASC|DESC;
              Например, чтобы отсортировать всех клиентов по имени в алфавитном порядке, вы можете использовать следующий запрос:
              SELECT * FROM customers ORDER BY name;

GROUP BY - это оператор SQL, который используется для группировки результатов запроса по указанному столбцу. 
           Он обычно используется совместно с функциями агрегации, такими как SUM, AVG, COUNT, MAX и MIN.
           SELECT column1, column2, ... FROM table_name GROUP BY column1, column2, ...;

HAVING - это оператор SQL, который используется для фильтрации групп результатов запроса. 
         Он аналогичен оператору WHERE, но указывается после GROUP BY и применяется только к группам, а не к отдельным строкам.
         SELECT column1, column2, ... FROM table_name GROUP BY column1, column2, ... HAVING condition;

UNION - это оператор SQL, который используется для объединения результатов двух или более запросов. 
        Он возвращает уникальные строки из всех запросов.
        SELECT column1, column2, ... FROM table1 UNION SELECT column1, column2, ... FROM table2;
        Например, чтобы объединить результаты двух запросов и вернуть уникальные имена клиентов, вы можете использовать следующий запрос:
        SELECT name FROM customers1 UNION SELECT name FROM customers2;
        Вы также можете использовать оператор UNION ALL, чтобы вернуть все строки,

DISTINCT - убирает дубликаты из результата выборки. (Возвращает уникальные значения)
           может использоваться с различными типами данных.
           SELECT DISTINCT customer FROM sales;

INTERSECT - это оператор SQL, который используется для выбора строк, которые содержатся в обоих результатах двух 
            или более запросов. Он возвращает только уникальные строки, которые присутствуют во всех запросах.
            SELECT column1, column2, ... FROM table1 INTERSECT SELECT column1, column2, ... FROM table2;
            Например, чтобы выбрать те имена клиентов, которые содержатся в обоих таблицах, вы можете использовать следующий запрос:
            SELECT name FROM customers1 INTERSECT SELECT name FROM customers2;
            Обратите внимание, что оператор INTERSECT не поддерживается во всех СУБД. 
            Вместо этого вы можете использовать вложенный запрос с IN или EXISTS.

EXCEPT - это оператор SQL, который используется для выбора строк, которые содержатся в первом запросе, 
         но не содержатся во втором. Он возвращает только уникальные строки, которые присутствуют в первом запросе, но отсутствуют во втором.
         SELECT column1, column2, ... FROM table1 EXCEPT SELECT column1, column2, ... FROM table2;
         Например, чтобы выбрать те имена клиентов, которые содержатся в первой таблице, но не содержатся во второй, вы можете использовать следующий запрос:
         SELECT name FROM customers1 EXCEPT SELECT name FROM customers2;
         Обратите внимание, что оператор EXCEPT не поддерживается во всех СУБД. Вместо этого вы можете использовать вложенный запрос с NOT IN или NOT EXISTS.

MATCH - используется для указания условия совпадения данных с определенным столбцом или набором столбцов в таблице. 
        используется совместно с оператором AGAINST, который указывает, что ищется.
        SELECT * FROM articles WHERE MATCH(tags) AGAINST('SQL');

USING - это оператор SQL, который используется в соединениях JOIN для указания столбца, который используется для соединения таблиц. 
        Он позволяет вам определить условие соединения с помощью одного столбца, который имеется в обеих таблицах.
        SELECT column1, column2, ... FROM table1 JOIN table2 USING (column);
        Например, чтобы соединить таблицы customers и orders по столбцу customer_id, вы можете использовать следующий запрос:
        SELECT customers.name, orders.order_id FROM customers JOIN orders USING (customer_id);
        Обратите внимание, что оператор USING не поддерживается во всех СУБД.
        Вместо этого вы можете использовать ON с условием table1.column = table2.column для соединения таблиц.

FOR - это оператор SQL, который используется для задания условий в выражении SELECT. 
      Он позволяет вам задать условие, которое должно быть выполнено для каждой строки результата запроса. 
      Оператор FOR может использоваться только с оператором SELECT и только в конце запроса. 
      Он может использоваться для указания типа блокировки, которую нужно установить на строки, выбранные в результате запроса. 
      Существует два основных типа блокировок, которые можно установить с помощью оператора FOR: 
      FOR UPDATE и FOR SHARE. 
      Оператор FOR UPDATE устанавливает блокировку на строку, которая не может быть изменена или удалена другими транзакциями, 
      пока текущая транзакция не будет завершена.""",
            "Функции": """
Функции:
MAX - возвращает максимальное значение из списка аргументов.
      может использоваться с числовыми и дата/время типами данных.
      SELECT MAX(amount) FROM sales;

MIN - возвращает минимальное значение из списка аргументов.
      может использоваться с числовыми и дата/время типами данных.
      SELECT MIN(amount) FROM sales;

SUM - возвращает сумму аргументов.
      может использоваться только с числовыми типами данных.
      SELECT SUM(amount) FROM sales;

AVG - возвращает среднее арифметическое аргументов.
      может использоваться только с числовыми типами данных.
      SELECT AVG(amount) FROM sales;

COUNT - возвращает количество аргументов.
        может использоваться с различными типами данных.
        SELECT COUNT(amount) FROM sales;

CONCAT - соединяет строки.
         может использоваться с типом данных строка.
         SELECT CONCAT(first_name, ' ', last_name) as full_name FROM customers;

UPPER - преобразует строку в верхний регистр.
        может использоваться с типом данных строка.
        SELECT UPPER(first_name) as first_name, UPPER(last_name) as last_name FROM customers;

LOWER - преобразует строку в нижний регистр.
        может использоваться с типом данных строка.
        SELECT LOWER(first_name) as first_name, LOWER(last_name) as last_name FROM customers;

SUBSTR - извлекает подстроку из строки. (столбец, первый символ, количество символов)
         может использоваться с типом данных строка.
         SELECT SUBSTR(phone, 1, 3) as area_code FROM customers;

TRIM - удаляет пробелы из начала и конца строки.
       может использоваться с типом данных строка.
       SELECT TRIM(first_name) as first_name, last_name FROM customers;

LENGTH - возвращает количество символов в строке.
         может использоваться с типом данных строка.
         SELECT first_name, LENGTH(first_name) as name_length FROM customers;

ROUND - округляет число до указанной точности. (столбец, кол-во знаков после запятой)
        может использоваться с типом данных число.
        SELECT product, ROUND(price, 2) as price FROM sales;

DATE - преобразует строку в формат даты. (хз проверить на питоне надо)
       может использоваться с типом данных строка и возвращает тип данных дата.
       SELECT DATE(order_date) as order_date, product, price FROM orders;

TIME - преобразует строку в формат времени. (хз проверить на питоне надо)
       может использоваться с типом данных строка и возвращает тип данных время.
       SELECT TIME(meeting_time) as meeting_time, topic FROM meetings;

DATETIME - преобразует строку в формат даты и времени. 
           может использоваться с типом данных строка и возвращает тип данных дата/время.
           SELECT DATETIME(event_date_time) as event_date_time, event_name FROM events;

TIMESTAMP - преобразует строку в формат времени с меткой времени (timestamp). 
            может использоваться с типом данных строка и возвращает тип данных timestamp.
            SELECT TIMESTAMP(log_timestamp) as log_timestamp, log_message FROM logs;

NOW - возвращает текущую дату и время. 
      не требует аргументов и возвращает тип данных timestamp.
      INSERT INTO orders (order_date, product, price) VALUES (NOW(), 'Shoes', 59.99);

COALESCE - принимает неограниченное количество аргументов и возвращает первый ненулевой аргумент (???)
           может использоваться с типами данных число, строка, дата/время и возвращает тип данных, соответствующий первому ненулевому аргументу.
           SELECT first_name, last_name, COALESCE(email, '') as email, COALESCE(phone, '') as phone FROM users;

ISNULL - проверяет, является ли значение нулевым (NULL). 
         принимает один аргумент и возвращает логическое значение true, если аргумент равен NULL, и false, если аргумент не равен NULL.
         SELECT first_name, last_name, position FROM employees WHERE ISNULL(bonus);

IFNULL - проверяет, является ли значение нулевым (NULL). 
         принимает два аргумента и возвращает первый аргумент, если он не равен NULL, и второй аргумент, если первый равен NULL.
         SELECT name, price, IFNULL(description, 'No description') as description FROM products;

CASE - позволяет условно выполнять различные действия в запросе SQL. 
       состоит из секций WHEN, THEN и ELSE, где WHEN указывает условие, 
       THEN - действие, которое нужно выполнить при выполнении условия, 
       а ELSE - действие, которое нужно выполнить, если условие не выполнено.
       SELECT position, salary,
       CASE
       WHEN salary > 40000 THEN 'High salary'
       WHEN salary BETWEEN 30000 AND 40000 THEN 'Average salary'
       ELSE 'Low salary'
       END as salary_level
       FROM employees;

IIF (IF ELSE) - позволяет условно выполнять различные действия в запросе SQL. 
                принимает три аргумента: логическое выражение, возвращаемое значение при истинном условии и возвращаемое значение при ложном условии.
                SELECT name, price, IIF(quantity > 0, 'In stock', 'Out of stock') as stock_status FROM products;

ROW_NUMBER - используется для нумерации строк в результирующем наборе данных. 
             используется совместно с оператором ORDER BY для сортировки строк по определенному критерию.
             SELECT ROW_NUMBER() OVER (ORDER BY quantity) as row_num, product_name, quantity, price FROM sales;

RANK - используется для нумерации строк в результирующем наборе данных. 
       используется совместно с оператором ORDER BY для сортировки строк по определенному критерию.
       (Отличие RANK от ROW_NUMBER заключается в том, что RANK нумерует строки с учетом их значений. 
        Например, если у нас есть несколько строк с одинаковым значением, то RANK будет устанавливать им ранг 
        с учетом этого одинакового значения, а не просто нумеровать их в порядке возрастания.)
       SELECT RANK() OVER (ORDER BY quantity) as row_num, product_name, quantity, price FROM sales;
       (Обратите внимание, что если бы у нас были строки с одинаковым значением количества, то они бы получили одинаковый ранг.)

DENSE_RANK - используется для нумерации строк в результирующем наборе данных. 
             используется совместно с оператором ORDER BY для сортировки строк по определенному критерию.
             (Отличие DENSE_RANK от RANK заключается в том, что DENSE_RANK нумерует строки с учетом их значений, 
              но не оставляет промежутки между рангами. Таким образом, если у нас есть несколько строк с одинаковым значением, 
              то DENSE_RANK будет устанавливать им ранг с учетом этого одинакового значения, но не оставляет промежутки между рангами.)
             SELECT DENSE_RANK() OVER (ORDER BY quantity) as row_num, product_name, quantity, price FROM sales;
             (Обратите внимание, что если бы у нас были строки с одинаковым значением количества, то они бы получили одинаковый ранг.
              Отличие от RANK заключается в том, что DENSE_RANK не оставляет промежутки между рангами.)

NTILE - используется для разбиения результирующего набора данных на равные части. 
        используется совместно с оператором ORDER BY для сортировки строк по определенному критерию.
        SELECT NTILE(3) OVER (ORDER BY quantity) as group_num, product_name, quantity, price FROM sales;
        (разбить эту таблицу на 3 равные части и пронумеровать каждую строку с учетом ее нахождения в этой части)

LAG - используется для получения значения из предыдущей строки результирующего набора данных. 
      используется для сравнения значений в разных строках или для вычисления разницы между значениями.
      SELECT product_name, price, LAG(price, 1) OVER (ORDER BY date) as prev_price, price - LAG(price, 1) OVER (ORDER BY date) as price_diff FROM sales;
      (получить таблицу с колонкой, содержащей разницу между ценой текущей строки и ценой предыдущей строки.)

LEAD - используется для получения значения из следующей строки результирующего набора данных. 
       используется для сравнения значений в разных строках или для вычисления разницы между значениями.
       SELECT product_name, price, LEAD(price, 1) OVER (ORDER BY date) as next_price, price - LEAD(price, 1) OVER (ORDER BY date) as price_diff FROM sales;
       (получить таблицу с колонкой, содержащей разницу между ценой текущей строки и ценой следующей строки.)

EXPLAIN - используется для анализа плана выполнения запроса. 
          возвращает таблицу с информацией о том, как база данных планирует выполнить запрос, включая информацию о том, 
          какие таблицы и столбцы будут использоваться, какие индексы будут использоваться, и как будут объединяться таблицы.
          EXPLAIN SELECT * FROM sales WHERE price > 200;
          (Мы хотим анализировать план выполнения запроса на выборку всех строк таблицы "sales" с ценой больше 200.)


EXPLAIN ANALYZE - расширение функции EXPLAIN, включает в себя дополнительную информацию о времени выполнения каждого этапа плана выполнения запроса. 
                  Эта информация может быть полезна при оптимизации запросов и изучении причин медленного выполнения.
                  EXPLAIN ANALYZE SELECT * FROM sales WHERE price > 200;
                  (Каждая строка таблицы описывает один этап плана и содержит следующие столбцы:
                   Номер этапа
                   Тип этапа (поиск, сортировка, табулирование и т.п.)
                   Таблицы, на которые распространяется действие этапа
                   Количество строк, которое будет обработано на этом этапе
                   Время выполнения этапа)
                  (Например, таблица может выглядеть следующим образом:
                   Seq.    Type    Table    Rows    Time
                   1    scan    sales    3        0.001
                   2    sort            3        0.002
                   3    limit            3        0.002)
                  (Основное отличие между EXPLAIN и EXPLAIN ANALYZE заключается в том, что EXPLAIN ANALYZE не только выводит информацию о плане выполнения запроса, 
                   но и РЕАЛЬНО выполняет запрос и возвращает результат. Это позволяет получить более точную информацию о времени выполнения каждого этапа, 
                   так как используется реальное время выполнения, а не оценочные данные, которые могут быть предоставлены функцией EXPLAIN. 
                   Также EXPLAIN ANALYZE может показать дополнительную информацию, такую как количество сканированных строк, общее время выполнения запроса и т.п.)

ABS (абсолютное значение) - возвращает абсолютное значение указанного числа. ABS(-5) = 5, ABS(3) = 3

ACOS (арккосинус) - возвращает арккосинус указанного числа. Арккосинус - это угол, косинус которого равен указанному числу. 
                    Функция ACOS может принимать любое число в диапазоне от -1 до 1, включительно, и возвращает угол в радианах.
                    ACOS(0.5) = 1.0471975511966, ACOS(-1) = 3.14159265358979

ASIN (арксинус) - возвращает арксинус указанного числа. 
                  Арксинус - это угол, синус которого равен указанному числу. 
                  Функция ASIN может принимать любое число в диапазоне от -1 до 1, включительно, и возвращает угол в радианах.
                  ASIN(0.5) = 0.52359877559829
                  ASIN(-1) = -1.5707963267949
                  Функция ASIN может быть использована для вычисления угла в треугольнике, если известны два катета и гипотенуза. Для этого нужно воспользоваться теоремой синусов.

ATAN (арктангенс) - возвращает арктангенс указанного числа. 
                    Арктангенс - это угол, тангенс которого равен указанному числу. 
                    Функция ATAN может принимать любое число и возвращает угол в радианах.
                    ATAN(1) = 0.78539816339745
                    ATAN(-2) = -1.10714871779409
                    Функция ATAN может быть использована для вычисления угла в треугольнике, если известны два катета и гипотенуза. Для этого нужно воспользоваться теоремой тангенсов.
                    (Пример использования функции ATAN в SQL запросе:
                     SELECT ATAN(2) as atan FROM DUAL;
                     Этот запрос выполнится и вернет арктангенс числа 2, то есть 1.10714871779409.
                     Также функция ATAN может быть использована в качестве условия в WHERE клаузе, например:
                     SELECT * FROM points WHERE ATAN(y/x) > 0.5;
                     В этом запросе будут выбраны точки, у которых угол между осью X и вектором из начала координат до точки больше 0.5 радиан.)

ATAN2 (арктангенс 2) - возвращает арктангенс указанной точки (y, x). 
                       Арктангенс - это угол, тангенс которого равен указанной точке. 
                       Функция ATAN2 принимает два аргумента - y и x, и возвращает угол в радианах.
                       ATAN2(1, 1) = 0.78539816339745
                       ATAN2(-2, 2) = -0.78539816339745
                       Функция ATAN2 может быть использована для вычисления угла в треугольнике, если известны два катета и гипотенуза. 
                       Для этого нужно воспользоваться теоремой тангенсов.
                       (Отличие между функциями ATAN и ATAN2 в том, что ATAN принимает только один аргумент - тангенс угла, 
                        в то время как ATAN2 принимает два аргумента - координаты точки в декартовой системе координат. 
                        Это позволяет ATAN2 вычислять угол даже если одна из координат равна нулю, чего не может сделать функция ATAN.)

CEIL (от ceiling)   возвращает наименьшее целое число, которое больше или равно переданному значению. CEIL(3.14) вернет 4, а CEIL(-3.14) вернет -3.
COS                 возвращает косинус угла в градусах. COS(угол в градусах) COS(45) result 0.7071067811865475
COT                 возвращает котангенс угла в радианах. Котангенс угла равен обратному тангенсу угла. COT(угол в радианах) COT(PI() / 4) result 1
                    функция COT работает так же, как и функция SIN и TAN, но ожидает угол в радианах.

DEGREES             преобразует радианы в градусы. DEGREES(выражение_вычисляется_как_радианы) DEGREES(PI()) result 180
EXP                 возвращает экспоненту (е в степени) заданного числа. EXP(выражение_вычисляется_как_число) EXP(2) result 7.38905609893065
                    число e (естественный логарифм) равно 2.718281828459045. EXP(2) эквивалентно e^2 = 7.38905609893065.
FLOOR               возвращает наибольшее целое число, которое меньше или равно переданному значению. FLOOR(выражение_вычисляется_как_число) FLOOR(3.14) result 3
                    FLOOR отличается от CEIL тем, что возвращает наибольшее целое число, которое меньше или равно переданному значению, 
                    в то время как CEIL возвращает наименьшее целое число, которое больше или равно переданному значению.

LN                  возвращает натуральный логарифм (по основанию e) заданного числа. LN(выражение_вычисляется_как_число) LN(2)сresult 0.693147180559945
                    число e (естественный логарифм) равно 2.718281828459045. LN(2) эквивалентно ln(2) = 0.693147180559945.

LOG                 возвращает логарифм заданного числа по заданному основанию. LOG(выражение_вычисляется_как_число, основание_логарифма) LOG(100, 10) result 2
                    работает так же, как и функция LN, но позволяет задавать основание логарифма. LOG(100, 10) эквивалентно log10(100) = 2.

LOG10               возвращает десятичный логарифм числа. LOG10(выражение, которое вычисляется как число) LOG10(100) result 2
                    всегда возвращает положительное число. Если входное число 0 или отрицательно, то результатом будет NULL.

MOD                 возвращает остаток от деления одного числа на другое. MOD(10, 3) result 1
                    всегда возвращает положительное число. Если второе число равно 0, то результатом будет NULL.

PI                  возвращает значение математической константы Пи (3.14159265358979323846)  PI() result 3.141592653589793
POWER               возвращает результат возведения числа в степень. POWER(основание_степени, показатель_степени) POWER(2, 3) result 8  эквивалентно выражению 2^3 = 8.
RADIANS             преобразует градусы в радианы. RADIANS(угол в градусах)  угол в 180 градусов равен PI радианам (3.141592653589793)
RAND                которая возвращает случайное число в диапазоне от 0 до 1. RAND()  Результат: 0.5298371105
SIGN                возвращает 1, 0 или -1 в зависимости от того, положительное, нулевое или отрицательное число соответственно.SIGN(выражение, которое вычисляется как число)
SIN                 возвращает синус угла в радианах. SIN(угол в радианах)
SQRT                возвращает квадратный корень числа. всегда возвращает неотрицательный квадратный корень. 
                    Если вы хотите вернуть квадратный корень с отрицательным числом, то результатом будет NULL.

TAN                 возвращает тангенс угла в радианах. TAN(угол в радианах)

| func                                                     | description                                                    | example                     |
|:---------------------------------------------------------|:---------------------------------------------------------------|:----------------------------|
| JSON_OBJECT          ('name', 'John', 'age', 30)         | Создает JSON-объект из переданных аргументов                   | {"name":"John","age":30}    |
| JSON_EXTRACT         ('{"key": "val"}', '$.key')         | Извлекает данные из JSON-строки по указанному пути             | val                         |
| JSON_ARRAYJSON_ARRAY ('apple', 'banana', 'cherry')       | Создает JSON-массив из переданных аргументов                   | ["apple","banana","cherry"] |
| JSON_INSERT          (json_column, '$.key', 'value')     | Вставляет значение в JSON-структуру по указанному пути         |                             |
| JSON_REMOVE          (json_column, '$.key')              | Удаляет элементы из JSON-структуры по указанному пути          |                             |
| JSON_REPLACE         (json_column, '$.key', 'new_value') | Заменяет значение элемента в JSON-структуре по указанному пути |                             |
"""
        },
        "RegExp": r"""
Регуля́рные выраже́ния — формальный язык, используемый в компьютерных программах, 
работающих с текстом, для поиска и осуществления манипуляций с подстроками в тексте, 
основанный на использовании метасимволов. 
Для поиска используется строка-образец, состоящая из символов и 
метасимволов и задающая правило поиска.

# Обозначения
|              |                                                                  |
|--------------|------------------------------------------------------------------|
| .            | Один любой символ, кроме новой строки \n.                        |
| \d           | Любая цифра                                                      |
| \D           | Любой символ, кроме цифры                                        |
| \s           | Любой пробельный символ (пробел, табуляция, конец строки и т.п.) |
| \S           | Любой не пробельный символ                                       |
| \w           | Любая буква (то, что может быть частью слова), а также цифры и _ |
| \W           | Любая не-буква, не-цифра и не подчёркивание                      |
| [..]         | Один из символов в скобках, а также любой символ из диапазона a-b [0-9][0-9A-Fa-f] |
| [^..]        | Любой символ, кроме перечисленных <[^>]>                         |
| \d≈[0-9]     | Буква “ё” не включается в общий диапазон букв!                   |
| \D≈[^0-9]<br>\w≈[0-9a-zA-Zа-яА-ЯёЁ]<br>\s≈[ \f\n\r\t\v] | Вообще говоря, в \d включается всё, что в юникоде помечено как «цифра», а в \w — как буква |
| [abc-], [-1] | Если нужен минус, его нужно указать последним или первым         |
| [*[(+\\\]\t] | Внутри скобок нужно экранировать только ] и \                    |
| \b           | Начало или конец слова (слева пусто или не-буква, справа буква и наоборот).<br>В отличие от предыдущих соответствует позиции, а не символу |
| \B           | Не граница слова: либо и слева, и справа буквы, либо и слева, и справа НЕ буквы |

# Повторения
|                    |                                        |
|--------------------|----------------------------------------|
| {n}                | Ровно n повторений                     |
| {m,n}              | От m до n повторений включительно      |
| {m,}               | Не менее m повторений                  |
| {,n}               | Не более n повторений                  |
| ?                  | Ноль или одно вхождение, синоним {0,1} |
| *                  | Ноль или более, синоним {0,}           |
| +                  | Одно или более, синоним {1,}           |
| *?  +?  ??  {m,n}? | По умолчанию квантификаторы жадные — захватывают максимально возможное число символов. |
| {,n}?  {m,}?       | Добавление ? делает их ленивыми, они захватывают минимально возможное число символов |

# Начало & конец
|          |                                                                                 |
|----------|---------------------------------------------------------------------------------|
| ^        | Начало всего текста или начало строчки текста, если flags=re.MULTILINE          |
| $        | Конец всего текста или конец строчки текста, если flags=re.MULTILINE            |
| \A       | Строго начало всего текста                                                      |
| \Z       | Строго конец всего текста                                                       |
| \b       | Начало или конец слова (слева пусто или не-буква, справа буква и наоборот)      |
| \B       | Не граница слова: либо и слева, и справа буквы, либо и слева, и справа НЕ буквы |

# .
|          |        |
|----------|--------|
| (?:...)  | Позволяют локализовать часть шаблона, внутри которого происходит перечисление |
| (?=...)  | Соответствует каждой позиции, сразу после которой НАЧИНАЕТСЯ соответствие шаблону ... |
| (?!...)  | Соответствует каждой позиции, сразу после которой НЕ МОЖЕТ НАЧИНАТЬСЯ шаблон ... |
| (?<=...) | Соответствует каждой позиции, которой может ЗАКАНЧИВАТЬСЯ шаблон ...<br>Длина шаблона должна быть фиксированной, то есть abc и a|b — это ОК, а a* и a{2,3} — нет. |
| (?<!...) | Соответствует каждой позиции, которой НЕ МОЖЕТ ЗАКАНЧИВАТЬСЯ шаблон ... |

# Флаги
|          |        |
|----------|--------|
| re.ASCII | По умолчанию \w, \W, \b, \B, \d, \D, \s, \S соответствуют все юникодные<br>символы с соответствующим качеством. Ускоряет работу, если все соответствия лежат внутри ASCII. |
| re.IGNORECASE | Не различать заглавные и маленькие буквы. Работает медленнее, но иногда удобно |
| re.MULTILINE | Специальные символы ^ и $ соответствуют началу и концу каждой строки |
| re.DOTALL | По умолчанию символ \n конца строки не подходит под точку. С этим флагом точка — вообще любой символ |

# Команды
|          |        |
|----------|--------|
| re.search(pattern, string) | Найти в строке string первую строчку, подходящую под шаблон pattern |
| re.fullmatch(pattern, string) | Проверить, подходит ли строка string под шаблон pattern |
| re.split(pattern, string, maxsplit=0) | Аналог str.split(), только разделение происходит по подстрокам, подходящим под шаблон pattern |
| re.findall(pattern, string) | Найти в строке string все непересекающиеся шаблоны pattern |
| re.finditer(pattern, string) | Итератор всем непересекающимся шаблонам pattern в строке string (выдаются match-объекты) |
| re.sub(pattern, repl, string, count=0) | Заменить в строке string все непересекающиеся шаблоны pattern на repl |



```python
import re 
def repl(m): 
    return '>censored(' + str(len(m[0])) + ')<' 
text = "Некоторые хорошие слова подозрительны: хор, хоровод, хороводоводовед." 
print(re.sub(r'\b[хХxX]\w*', repl, text)) 
# -> Некоторые >censored(7)< слова подозрительны: >censored(3)<, >censored(7)<, >censored(15)<. 
```

Примеры
Номер кредитки:

```regexp
[0-9]{13,16}
```

ICQ:

```regexp
([1-9])+(?:-?\d){4,}
```

Набор из букв и цифр (латиница):

```regexp
^[a-zA-Z0-9]+$
```

Набор из букв и цифр (латиница + кириллица):

```regexp
^[а-яА-ЯёЁa-zA-Z0-9]+$
```

Домен (например seo-zona.ru):

```regexp
^([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6}$
```

IPv4:

```regexp
((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)
```

IPv6:

```regexp
((^|:)([0-9a-fA-F]{0,4})){1,8}$
```

Имя пользователя (с ограничением 2-20 символов, 
которыми могут быть буквы и цифры, первый символ обязательно буква):

```regexp
^[a-zA-Z][a-zA-Z0-9-_\.]{1,20}$
```

Дата в формате YYYY-MM-DD:

```regexp
[0-9]{4}-(0[1-9]|1[012])-(0[1-9]|1[0-9]|2[0-9]|3[01])
```

Дата в формате DD/MM/YYYY:

```regexp
(0[1-9]|[12][0-9]|3[01])[- /.](0[1-9]|1[012])[- /.](19|20)\d\d
```

Целые числа и числа с плавающей точкой (разделитель точка):

```regexp
\-?\d+(\.\d{0,})?
```

UUID:

```regexp
^[0-9A-Fa-f]{8}\-[0-9A-Fa-f]{4}\-[0-9A-Fa-f]{4}\-[0-9A-Fa-f]{4}\-[0-9A-Fa-f]{12}$
```

Широта или долгота:

```regexp
-?\d{1,3}\.\d+
```
""",
        "Dockerfile": {
            "Dockerfile": """Dockerfile
FROM:    Определяет базовый образ, на основе которого будет создан ваш образ контейнера. 
         Здесь мы используем образ Python 3.9 на основе slim-версии Debian.

WORKDIR: Устанавливает рабочую директорию внутри контейнера, где будут выполняться команды.

COPY:    Копирует файлы из текущей директории на вашем компьютере внутрь контейнера.

RUN:     Выполняет команды внутри контейнера для установки зависимостей, указанных в файле requirements.txt.

CMD:     Определяет команду, которая будет запущена при запуске контейнера. 
         Здесь мы указываем запуск основного скрипта main.py.

```Dockerfile
FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python3", "main.py"]
```


```Dockerfile
ENV BOT_TOKEN=""
```

<img alt="docker.png" src="cheatsheet\Языки\Dockerfile\docker.png">
""",
            "RUN mkdir -p": r"""
Команда mkdir используется для создания новой директории.

Флаг /p позволяет создать директорию и ее родительские директории, если они еще не существуют. 
Например:

```Dockerfile
RUN mkdir C:\app\data\logs /p
```

Если же использовать команду RUN mkdir C:\app\data\logs 
и директория C:\app\data еще не существует, то команда mkdir вернет ошибку.
""",
        },
        "JavaScript": {
            "Списки": """
```js
let myArray = [1, 2, 3, 4, 5];
console.log(myArray.length); // Outputs 5
```

 or == ||
and == &&

```js
let list = ["apple", "banana", "orange"];
let textToCheck = "banana";

if (list.includes(textToCheck)) {
    console.log("Text exists in the list");
} else {
    console.log("Text does not exist in the list");
}
```

""",
            "for": """
Цикл for в JavaScript используется для выполнения одного 
или нескольких операторов многократно, пока условие в цикле истинно. 
Синтаксис цикла for выглядит следующим образом:

```js
for (initialization; condition; final-expression) {
   statement(s)
}
```

initialization     выполняется один раз перед началом цикла 
                   и обычно используется для инициализации счетчика цикла.
condition          условие, которое проверяется перед каждой итерацией цикла. 
                   Если условие истинно, то тело цикла выполняется, иначе цикл завершается.
final-expression   выполняется после каждой итерации цикла 
                   и обычно используется для изменения счетчика цикла.
statement(s)       один или несколько операторов, которые выполняются в теле цикла.

```js
for (let i = 0; i < 5; i++) {
   console.log(i);
}
```

Цикл по списку

```js
var myArray = [1, 2, 3, 4, 5];
for (var i = 0; i < myArray.length; i++) {
  console.log(myArray[i]);
}
```

или

```js
var myArray = [1, 2, 3, 4, 5];
for (const element of myArray) {
  console.log(element);
}
```
""",
            "handlebar": """Пробел ! " # % & ' ( ) * + , . / ; < = > @ [ \ ] ^ ` { | } ~

""",
            "Переменные": """в JavaScript можно создать глобальную переменную, которая будет доступна 
во всем скрипте, даже после завершения функции. Для этого нужно просто объявить переменную
вне функции, без использования ключевого слова var, let или const.

```js
// Глобальная переменная
let myGlobalVariable = "Hello, World!";

function myFunction() {
  // Использование глобальной переменной
  console.log(myGlobalVariable);
}

myFunction(); // "Hello, World!"
console.log(myGlobalVariable); // "Hello, World!"
```

Однако, использование глобальных переменных может приводить к проблемам 
с организацией кода и конфликтам имен, поэтому рекомендуется использовать их с осторожностью.
""",
        },
        "CSS": {

        },
        "HTML": {
            "html": """
<img alt="html.png" src="cheatsheet\Языки\HTML\html.png">
""",
            "tag input": """
```html
<input type="text" id="">
```

```html
<input type="password" id="">
```

```html
<input type="radio" id="">
```

```html
<input type="checkbox" id="">
```

```html
<input type="submit" id="">
```

```html
<input type="reset" id="">
```

```html
<input type="button" id="">
```

```html
<input type="file" id="">
```

```html
<input type="hidden" id="">
```

```html
<input type="image" id="">
```

```html
<input type="number" id="">
```

```html
<input type="range" id="">
```

```html
<input type="search" id="">
```

```html
<input type="email" id="">
```

```html
<input type="tel" id="">
```

```html
<input type="url" id="">
```

```html
<input type="date" id="">
```

```html
<input type="time" id="">
```

```html
<input type="week" id="">
```

```html
<input type="month" id="">
```

```html
<input type="color" id="">
```

"""
        },
        "Cpp": {
            r"Типы данных": """
# Целые числа

|                    |                                                                                                                      |
|--------------------|----------------------------------------------------------------------------------------------------------------------|
| short int          | предназначен для хранения целых чисел.<br>Диапазон чисел от -32 768 до 32 767;                                       |
| unsigned short int | предназначен для хранения целых положительных чисел.<br>Диапазон чисел от 0 до 65 535;                               |
| int                | предназначен для хранения целых чисел.<br>Диапазон чисел от -2 147 483 648 до 2 147 483 647;                         |
| unsigned int       | предназначен для хранения целых положительных чисел.<br>Диапазон чисел от 0 до 4 294 967 295;                        |
| long int           | предназначен для хранения целых чисел.<br>Диапазон чисел от –9 223 372 036 854 775 808 до 9 223 372 036 854 775 807; |
| unsigned long int  | предназначен для хранения целых положительных чисел.<br>Диапазон чисел от 0 до 18 446 744 073 709 551 615.           |

Разница между типами заключается только в диапазоне чисел, который можно записать в переменную. 
Также не используйте большие типы данных по типу long int, если число маленькое, 
так как чем больше диапазон, тем больше памяти требуется компьютеру на конкретную переменную.

# Числа с точкой

|                      |                                                                                           |
|----------------------|-------------------------------------------------------------------------------------------|
| float                | Для создания чисел с плавающей точкой.<br>Диапазон чисел от от -3.4*1038 до 3.4*1038;     |
| double<br>long float | Для создания чисел с плавающей точкой.<br>Диапазон чисел от от ±4.9*10-324 до ±1.8*10308. |

# Прочие типы данных

|      |                                                                                                |
|------|------------------------------------------------------------------------------------------------|
| bool | Логический тип данных. Предназначен для записи истинного (true) или ложного (false) значения;  |
| char | Тип данных для работы с символами. Позволяет поместить в одинарных кавычках какой-либо символ. |

Для создания переменной необходимо указать тип данных и назвать её.
Также можно сразу же добавить к ней значение:

```cpp
int a = 0; // Добавление значения сразу
float c; // Создание переменной без значения
short int b, y = 342; // Создание нескольких переменных
```

Для вызова переменной вы можете обратиться к ней по имени.
Получение данных
Для получения данных от пользователя необходимо воспользоваться командой cin:

```cpp
cin >> some_value;
```

Таким образом введенные пользователем данные будут помещены в переменную с названием «some_value».

```cpp
char c = '1';    // символ
bool b = true;   // логическая переменная, принимает значения false и true
int i = 42;      // целое число (занимает, как правило, 4 байта)
short int i = 17;            // короткое целое (занимает 2 байта)
long li = 12321321312;       // длинное целое (как правило, 8 байт)
long long lli = 12321321312; // длинное целое (как правило, 16 байт)
float f = 2.71828;           // дробное число с плавающей запятой (4 байта)
double d = 3.141592;         // дробное число двойной точности (8 байт)
long double ld = 1e15;       // длинное дробное (как правило, 16 байт)
```

```cpp
std::cout << "char: " << sizeof(char) << "\\n";                 //  1
std::cout << "bool: " << sizeof(bool) << "\\n";                 //  1
std::cout << "short int: " << sizeof(short int) << "\\n";       //  2 (по стандарту >= 2)
std::cout << "int: " << sizeof(int) << "\\n";                   //  4 (по стандарту >= 2)
std::cout << "long int: " << sizeof(long int) << "\\n";         //  8 (по стандарту >= 4)
std::cout << "long long int: " << sizeof(long long) << "\\n";   //  8 (по стандарту >= 8)
std::cout << "float: " << sizeof(float) << "\\n";               //  4
std::cout << "double: " << sizeof(double) << "\\n";             //  8
std::cout << "long double: " << sizeof(long double) << "\\n";   // 16
```

Приведённые выше примеры вывода оператора sizeof верны для 64-битных архитектур, которые на сегодняшний день распространены повсеместно. 
Однако если бы мы скомпилировали и запустили такую программу на компьютере с 32-битной архитектурой, то получили бы другие результаты. 
Например, sizeof(long int) стал бы равен 4, в то время как на современных компьютерах мы получили бы 8. 
Также бывают встраиваемые системы, под которые тоже можно писать на С++. Там битность архитектуры может быть ещё меньше, чем 32.

В заголовочном файле cstdint стандартной библиотеки имеются целочисленные типы с фиксированным размером:

int8_t / uint8_t
int16_t / uint16_t
int32_t / uint32_t
int64_t / uint64_t
Число в имени типа означает количество бит, используемых для хранения в памяти. 
Например, int32_t содержит 32 бита (4 байта) и часто соответствует типу int. 
Если система не поддерживает какой-то тип, то программа с ним просто не скомпилируется.

Арифметические операции
Бинарные операции +, - и * работают для чисел стандартным образом. 
Результат операции деления /, применённой к целым числам, всегда округляется в сторону нуля. 
Таким образом, для положительных чисел операция / возвращает неполное частное. 
Остаток от деления целых чисел можно получить с помощью операции %.

```cpp
int main() {
    int a = 7, b = 3;
    int q = a / b;  // 2
    int r = a % b;  // 1
}
```

Если при делении нужно получить обычное частное, то один из аргументов нужно привести
к вещественному типу (например, double) с помощью оператора static_cast:

```cpp
int main() {
    int a = 6, b = 4;
    double q = static_cast<double>(a) / b;  // 1.5
}
```

Можно было бы написать чуть более кратко: double q = a * 1.0 / b;. 
Тогда преобразование аргументов произошло бы неявно.

Арифметические операции над символами,
а также сравнение символов друг с другом — это фактически операциинад их ASCII-кодами:

```cpp
#include <iostream>
 
int main() {
    char c = 'A';
    c += 25;  // увеличиваем ASCII-код символа на 25
    std::cout << c << "\\n";  // Z
}
```
""",
            "if-else,switch-case": r"""
&& (И)
|| (ИЛИ)
! (НЕ)

Если необходимо проверить несколько условий в одном операторе, 
то можно воспользоваться логическим «и» или же логическим «или»:

```cpp
if (a != b && a > b) {
    // Код будет выполнен, если и первое, и второе условие
    // окажутся верными
}

if (a < b || a == b) {
    // Код будет выполнен, если или первое, или второе условие
    // окажется верным
}
```

Тернарная операция
Это сокращенная форма if else. Записывается следующим образом:

```cpp
int x = 90, a = 8;
int res = x < a ? (x + a) : (x - a);
cout << res << endl;
```

Проверяем: если “x” будет меньше “а”, то в переменную res устанавливаем их сумму, иначе – их разницу. 

Конструкция switch
Конструкция case обладает более удобным форматом для проверки множественных условий на совпадение значения. 
В конструкцию записывается переменная, что проверяется, а также значения на которые происходит проверка.

Пример оператора:

```cpp
int x = 23;
switch (x) { // Проверяем переменную x
    case 1: // Если переменная будет равна 1, то здесь сработает код
        // Может быть множество строк, а не только одна
        cout << "Переменная равна 1" << endl;
        break; // Указываем конец для кода для этой проверки
    case 56: // Если переменная будет равна 56, то здесь сработает код
        // Может быть множество строк, а не только одна
        cout << "Переменная равна 56" << endl;
        break; // Указываем конец для кода для этой проверки
        // По аналогии таких проверок может быть множество
        // Также можно добавить проверку, которая сработает в случае
        // если все остальные проверки не сработают
    default:
        cout << "Что-то другое" << endl;
        break; // Можно и не ставить, так как это последние условие
}
```


Операторы && и || ведут себя лениво: если первого аргумента уже достаточно для ответа, то второй аргумент вычисляться не будет. 
Например, в выражении condition1 && condition2 второе условие не вычисляется, если первое ложно.



Сравнение чисел с плавающей точкой
Рассмотрим программу, которая проверяет равенство 0.1 + 0.2 == 0.3:

```cpp
#include <iostream>
 
int main() {
    double x = 0.1, y = 0.2;
    if (x + y == 0.3) {
        std::cout << "EQUAL ";
    } else {
        std::cout << "NOT EQUAL ";
    }
 
    std::cout << x + y << "\n";
}
```

Логично было бы предположить, что программа выведет EQUAL 0.3, потому что . 
Однако программа напечатает NOT EQUAL 0.3. 
Данная «ошибка вычисления» встречается в большинстве современных языков программирования и обусловлена погрешностью представления этих чисел. 
Если повысить число знаков дробной части в выводе, мы увидим, что 0.1 + 0.2 == 0.30000000000000004.

Поскольку операции над числами с плавающей точкой могут содержать погрешность, обычное сравнение через == некорректно. 
Поэтому правильнее сравнивать модуль разности величин с некой допустимой для нас погрешностью. 
Модуль дробного числа можно получить с помощью функции std::abs из заголовочного файла cmath. 
Исходную программу можно было бы переписать так:

```cpp
#include <cmath>
#include <iostream>
 
int main() {
    double delta = 0.000001;
 
    double x = 0.1, y = 0.2;
    double sum = x + y;
 
    if (std::abs(sum - 0.3) < delta) {
        std::cout << "EQUAL ";
    } else {
        std::cout << "NOT EQUAL ";
    }
 
    std::cout << sum << "\n";
}
// Теперь программа выведет EQUAL 0.3.
```
""",
            "rand": """Случайные числа
Для генерации случайных чисел необходимо использовать метод rand(). Чтобы создать случайное число в диапазоне от 1 до 20 потребуется следующий код:

```cpp
int num = 1 + rand() % 20;
```

При использовании такого кода число будет генерироваться случайны образом, но всегда будет неизменным. 
Чтобы каждый раз при запуске программы выводилось новое случайное число необходимо использовать библиотеку: 
#include <time.h>. 
После её подключения в функции main пропишите команду: srand(time(NULL));


Пример реализации:

```cpp
#include <iostream>
#include <time.h>
using namespace std; 

int main() {
    setlocale(LC_ALL, "Russian"); // Русская локализация консоли
    srand(time(NULL)); // Генерирует случайное число, используя текущую дату как параметр
    cout << 1 + rand() % 20 << endl;
    cout << 1 + rand() % 20 << endl;

    cin.get();
    return 0; 
}
```

Функции для строк
Для работы со строками необходимо подключить библиотеку #include <string>. 


Для получения целой строки от пользователя используйте функцию «getline(cin, value)». 
В функции параметр value является названием переменной, в которую будет записано значение от пользователя.
""",
            "Циклы": """Цикл For
В цикле for все условия записываются в одном месте, что очень удобно во многих случаях. 
Стандартная запись такого цикла выглядит следующим образом:

```cpp
for (int i = 0; i < 10; i++)
    cout << i << endl;
```

В объявлении цикла записывается следующее: переменная цикла, её начальное значение и диапазон. 
В примере выше будут выведены числа от 0 до 10.

Если в теле цикла всего одна строка кода, то фигурные скобки можно пропустить и не записывать их.

Цикл While
Суть цикла while не особо отличается от цикла for. Единственное отличие заключается в способе записи цикла. 
В while необходимо прописать лишь условие, а все остальные параметры записываются вне цикла:

```cpp
int i = 1; // Создание переменной
while (i <= 10) { // Здесь только условие
    cout << i << endl;
    i++; // Увеличение переменной
}
```

Цикл Do While
Цикл схож с циклом while по форме написания, но при этом работает немного по-другому. 
Цикл do..while будет выполнен один раз сто процентов, а дальше проверит условие и если оно верно, то цикл будет выполняться дальше:

```cpp
int x = 13;
do {
    x--;
    cout << i << endl;
} while (x > 10);
```

Как видно из примера, цикл изначально неверный, но это не мешает ему сработать один раз.
Операторы для работы в циклах
Существует два основных оператора для работы в циклах:

Оператор break - служит для выхода из цикла полностью;
Оператор continue - пропускает лишь одну итерацию и не выходит из цикла.
""",
            "try-catch": """Реализации конструкции try catch
Для добавления отслеживания ошибок можно прописать следующий код:

```cpp
try { // В блоке try мы пытаемся выполнить какой-либо код
    if (variable == 0) // Проверяем делитель на ноль
        throw 277; // Запускаем исключение и передаем в него параметр

    cout << something / variable << endl; 
} catch(int i) { // Здесь отлавливаем переданную ошибку
    cout << "Нам очень повезло!" << endl;
    cout << "Нам удалось избежать ошибки с индексом " << i << " - на 0 делить нельзя!";
}
```

В коде выше представлен очень простой пример использования исключений. 
Не обращайте внимание на его простоту, так как главное это рассмотреть общую конструкцию блока try catch.

При использовании такой конструкции, какая бы ошибка не получилась в ходе программы 
сама программа работать не перестанет и пользователь не получить плохой опыт в её использовании.

Если необходимо отследить несколько классов с ошибками, то можно добавить несколько 
блоков catch. Все они добавляются друг под другом точно также как в условных операторах. 
""",
            "Массивы": """Массивы позволяют хранить большой объем информации в одном месте. В языке C++ можно найти несколько основных типов массивов. 

Одномерный массив
Чтобы создать массив необходимо указать тип данных, прописать название и поставить квадратные скобки. 
Это очень схоже с созданием обычных переменных, но здесь после названию идут ещё квадратные скобки.

В массивах отсчет начинается с 0, поэтому первый элемент по индексу будет равен 0, второй - 1 и так далее.

Примеры создания массива:

```cpp
char stroka[2]; // Создание пустого массива
int[] numbers; // Будет считаться ошибкой

int nums[4];
nums[0] = 1; // Добавление элементов в массив из 4 элементов

int nums2[] = { 1, 2, 3, 5 }; // Присвоение всех значений сразу
```

Работать с элементами массива можно точно как с переменными. Мы можем их выводить или же устанавливать для них новые значения.

Многомерный массив
Многомерный массив - это массив, в котором каждый элемент является другим массивом. 
На практике очень редко используются массивы с более чем третим уровнем вложенности. 
То есть массивы, в которых все элементы являются другими массивами 
и в котором все элементы также другие массивы встречаются очень и очень редко на практике.



Мы не будем изучать подобные массивы, так как принцип их построения 
точно такой же как при работе с двумерными массивами.

Для создания двумерных массивов необходимо использовать двойные квадратные скобки после названия. 
Выглядит такой массив как матрица, а записывается следующим образом:

```cpp
int x[3][3] = { { 0, 34, 2 }, { 3, 4, 5 } };
cout << x[0][1]; // Выведет 34

// Можно их сразу не присваивать
char symbols[5][2];
symbols [0][1] = 'A';
```

Мы видим, что элементы первого массива являются другими массивами. 
Чтобы выбрать какой-либо объект используйте ту же структуру что и для одномерных массивов, 
вот только теперь указывайте индекс как первого массива, так и второго:

```cpp
x[0][1] = 1; // Вместо 34 теперь будет 1
```
""",
            "Указатели": """Каждая переменная или объект хранит данные в определенной ячейке в памяти компьютера. 
Каждый раз, создавая новую переменную, мы создаем новую ячейку в памяти, с новым значением для неё. 
Чем больше ячеек, тем больше компьютерной памяти будет занято.


Адрес в памяти компьютера это число, к которому мы можем получить доступ. 
Указатель - это тот же адрес в памяти, по которому мы получаем переменную и по итогу её значение.

Чтобы работать с указателями необходимо воспользоваться двумя специальными символами: & и *. Пример использования:

```cpp
int t = 237; // Простая переменная
int *p; // Создание указателя, который принимает лишь адрес другой переменной
p = &t; // Устанавливаем адрес нашей первой переменной
```

Переменные t и p будут равны числу 237, так как оба ссылаются на одну ячейку. 
Сам же компьютер на вычислении обеих переменных потратит меньше усилий, ведь обе переменные ссылаются на одно и то же.

Ссылки в C++
Ссылки и указатели схожи между собой, так как оба в качестве значения имеют лишь адрес некого объекта.

Указатель хранит адрес ячейки и если мы захотим изменить значение этой ячейки, то нам придется выполнить операцию «разыменования»:

```cpp
float some = 391; // Простая переменная
float *u = &some; // Указатель на переменную
*u = 98; // Изменение значения переменной
```

В ссылках такого понятия нет, так как меняя ссылку вы автоматически меняете и переменную. 
Ссылки напрямую ссылаются к переменной, поэтому их синтаксис проще:

```cpp
char symbol = 'A'; // Простая переменная
char &ref = symbol; // Создание ссылки на переменную
// Поскольку мы ссылаемся на переменную, то можем её использовать
// как отдельно взятую переменную
cout << ref << endl; // Вывод символа "А"
ref = 'C'; // Изменение на символ "C"
```

Использование ссылок и указателей оправдано в случае передачи данных в функции или же в объекты. 
Также данные технологии отлично подойдут для передачи большого объема данных в ходе программы.
""",
            "Динамические массивы": """Динамическое выделение памяти очень удобно, так как за счёт выделения 
памяти мы резервируем место под данные в каком-либо объекте.

В C++ за выделение и удаление памяти отвечают операторы new и delete соответсвенно. 
Они служат для создания не только динамических массивов, но также для выделения памяти под объекты и даже простые переменные.

```cpp
// Операция выделения памяти (new)
float *val = new float; // Можно выделять память под любые типы данных
// здесь val это указатель на участок памяти типа float 
// new служит операцией выделения этой памяти
// delete необходим для высвобождения памяти
delete val;
```

Динамический массив использует ту же конструкцию. Здесь также применяются операторы new и delete:

```cpp
char *symbols = new char [25]; // выделение памяти под массив
// Также необходимо освободить память,
// когда массив уже не нужен
delete [] symbols;
```
""",
            "Символы и строки": """Создание строкового объекта было невозможным в языке Си. 
Для создании строки использовался массив символов - char arr[]. 
В языке C++ все было упрощено и для создания строк появился новый отдельный объект. 
Вместе с объектом появились и новые функции для обработки строк. 

Вместе с тем не стоит забывать, что строки до сих пор являются массивом символов, 
а это означает, что с каждым символом можно работать по отдельности, будто это элемент одного общего массива.

Работа со строками не отличается от работы с массивами. 
Вот только для записи целой строки мы можем воспользоваться специальной функцией gets(). 

С недавних пор более предпочтительно использовать метод gets_s(), что более защищен и позволяет выполнить получения строки от пользователя. 

Язык C++ спокойно может работать с кириллицей, при условие что вы подключите обработку символов кириллицы. 
Для корректной работы необходимо подключить библиотеку «clocale», а также в метода main воспользоваться функцией setlocale:

```cpp
#include <clocale>

using namespace std; 

int main() {
    // Установка поддержки кириллицы
    setlocale(LC_CTYPE, "rus");

    return 0; 
}
```

python

```python
x = "2"
y = "4"
z = int(x + y + y)
print(z+6) # 250
```

C++

```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    string x = "2";
    string y = "4";
    int z = stoi(x + y + y);
    cout << z + 6 << endl; // 250
    return 0;
}
```

stoi() - это функция стандартной библиотеки C++, которая используется для преобразования строки 
(например, содержащей текстовое представление числа) в целое число (int). 
Функция std::stoi() возвращает полученное целое число.

python

```python
x = 2
y = 4
z = str(x + y + y)
print(f"f({z})") # f(10)
```

С++

```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    int x = 2;
    int y = 4;
    string z = to_string(x + y + y);
    cout << "f(" << z << ")" << endl; // f(10)
    return 0;
}
```
""",
            "Структуры данных": """Структуры служат для описания небольшого объекта, у которого нет большого количества переменных и функций.

Использование структур удобно, так как они имеют ряд преимуществ:
занимают меньше памяти, поэтому использование их облегчает нагрузку на процессор;
имеют простой синтаксис;
имеют лишь переменные, функции и конструкторы;
на их основе можно создавать объекты.

Получается, что благодаря структурам, можно с легкостью создавать небольшие объекты с маленьким количеством информации. 
Такие объекты могут описывать реальные объекты из жизни: объект книги, объект автомобиль, объект дерево и тому подобное.

Для создания структуры используйте синтаксис: struct NAME {}. 
На основе одной структуры можно создавать неограниченное количество объектов, 
которые будут иметь одинаковые названия переменных и функций, но при этом значения у всех объектов будут разными.
""",
            "Перечисления (Enum)": """За счёт перечислений вы можете указать список элементов для выбора и далее в программе можете пользоваться данным списком.
Перечисления служат для удобства программистов, так как особой функциональности они не несут. 
Представим, что у вас большая программа со множеством массивов данных, которые человек попросту не способен запомнить. 
По причине неспособности все запомнить вы можете создать перечисление, что будет хранить список со всеми доступными значениями и названиями.

Создав такой список вы можете обращаться к нему и выбирать подходящий для вас вариант.

Для создания перечислений используйте пропишите слово enum, назовите его и укажите инициализацию всех вариантов.


Обьяснение от ChatGPT:

Перечисления (Enum) - это специальный тип данных в C++, который позволяет определять именованные константы. 
Это полезно, когда вы хотите указать набор допустимых значений для переменной.

Определение перечисления выглядит так:

```cpp
enum Color {
  RED,
  GREEN,
  BLUE
};
```

В этом примере мы определили перечисление Color, которое содержит три константы: RED, GREEN и BLUE. 
Эти константы могут использоваться в качестве значений для переменных типа Color.

По умолчанию каждая константа присваивается значение равным ее позиции в перечислении, начиная с нуля. 
Однако, вы также можете явно указать значение для каждой константы:

```cpp
enum Color {
  RED = 1,
  GREEN = 2,
  BLUE = 4
};
```

В этом примере мы явно указали значение для каждой константы в перечислении.
""",
            "Работа с файлами": """Многие языки программирования предоставляют классы для работы с файлами и директориями проекта. 
Язык C++ обладает множеством классов для записи и чтения данных из файлов.

Работа с файлами
При работе с файлами всегда необходимо помнить две вещи:

Перед началом работы с файлом его необходимо открыть;
После завершения работы с файлом его необходимо закрыть.

Если файл не открыт или же неверно открыт, то вы не можете полноценно работать с его содержимым. 

С закрытием все проще, но и коварнее. Если вы не закроете файл, то программа будет работать верно, 
тем не менее, чем больше будет открытых файлов, тем больше программа будет перегружена и в какой-то момент она просто зависнет или выключиться.

Исключения и файлы
Поскольку не всегда известно будет ли файл в проекте или на компьютере пользователя, 
то всегда лучше открывать файлы за счёт использования исключений. 
Выполняйте открытие файлов в блоке try catch и тем самым вы обезопасите себя от любых непредвиденных обстоятельств.

Запись данных в файл
При записи данных в файл его изначально необходимо открыть. Для этого в языке C++ используется класс ofstream:

```cpp
// Создание/открытие файла "examples.txt"
ofstream itproger_file("examples.txt");
// Можно было использовать метод open
// ofstream itproger_file;
// itproger_file.open("examples.txt");
// но первая запись короче, поэтому стоит использовать её
if (itproger_file.is_open()) { // Проверяем открыт ли файл
    itproger_file << "Simple text"; // Записываем текст в файл
    itproger_file.close(); // Всегда необходимо закрывать файл
} else // Если файл не удалось открыть, тогда выдаем ошибку
    cout << "Error!" << endl;
```

Таким образом мы можем открыть файл и поместить в него любую информацию.

При открытии файла можно указать режим открытия. Существуют несколько режимов и все они представлены на фото ниже:

Константа         Описание
ios_base::in      открыть файл для чтения
ios base::out     открыть файл для записи
ios base::ate     при открытии переместить указатель в конец файла
ios_base::app     открыть файл для записи в конец файла
ios_base::trunc   удалить содержимое файла, если он существует
ios_base::binary  открытие файла в двоичном режиме

Режим необходимо прописывать в качестве второго параметра при открытии файла:

```cpp
#include <iostream>
#include <fstream>

using namespace std; 

int main() {
    // Открываем файл для записи в него текста
    ofstream file("test.txt", ios_base::out);
    if (file.is_open()) { // Проверяем открыт ли сам файл
        file << "Simple world"; // Записываем текст в начало файла
        textFile.close(); // Закрываем файл
    }

    cin.get();
    return 0; 
}
```

Чтение данных из файла
Для чтения данных файл необходимо также изначально открыть и в конце закрыть. 
Чтобы прочесть содержимое файла используется класс ifstream:

```cpp
#include <iostream>
#include <fstream>

using namespace std; 

int main() {
    // здесь будет храниться промежуточный текст,
    // который мы будем считывать из файла
    char temp[100];
    ifstream some_file("test.txt"); // открываем файл для чтения

    // считываем лишь первое слово и помещаем в переменную temp
    some_file >> temp;
    cout << temp << endl; // выводим эту переменную

    // Считываем определенное количество символов - 100
    // и записываем их в нашу переменную
    some_file.getline(temp, 100);
    some_file.close(); // Закрываем файл
    cout << temp << endl; // Отображаем переменную temp

    cin.get();
    return 0; 
}
```
""",
            "Функции": """Функции можно назвать небольшими подпрограммами, куда можно вынести повторяющийся код и обращаться к нему, когда это будет нужно. 
Функции значительно облегчают построение программ, так как нам не надо копировать 
однотипный код множество раз, а можно просто воспользоваться одной общей функцией.

Многие путают функции и методы и не понимают отличий между ними. 
На самом деле отличий нет, так как что методы, что функции являются одним и тем же. 
Функции что записаны вне классов называют функциями, а функции что записаны внутри классов называются методами. 
Поскольку C++ это не объектно ориентированный язык, то лучше говорить функции, хотя это не имеет никакого значения.

Точно такая же ситуация обстоит с переменным. В классах переменные называются полями, а вне классов - переменными.

Для создания функций необходимо указать возвращаемый тип данных, указать название и параметры.
В случае когда функция ничего не возвращает, то указывается тип данных void.

Все функции необходимо записывать перед созданием функции main().
В таком случае при вызове функций у вас не будет появляются ошибок.

Также функции можно лишь объявить перед функцией «main», а после неё прописать.

Создание функции
На основе всех данных наша функция будет выглядеть следующим образом:

```cpp
void test () {
    cout << "Вывод чего-либо в консоль" << endl;
}
```

Функция выше не принимает никаких параметров и ничего не возвращает.
Она просто пишет слово в консоль. Давайте разнообразим функцию и добавим параметр:

```cpp
void test (char symbol) {
    cout << symbol << endl;
}
```

Теперь функция принимает параметр, который будет отображен в консоли.

Также было бы логично прописать описание функции перед функцией «main»:

```cpp
void test (char symbol);
```

Если функция должна что-либо вернуть, то прописываем тип данных который будет возвращен.
Для возвращения данных используем ключевое слово return:

```cpp
double test (double some_number) {
    some_number *= 2;
    return some_number;
}
```
""",
            "Перегрузка функций": """С перегрузкой методов мы уже ни раз сталкивались, хотя ни разу их не создавали вручную. 
Пришло время это исправить.

Что такое перегрузка методов?
За счёт перегрузки методов мы можем создать множество методов, что будут принимать разное количество 
параметров или разный тип данных и при этом будут иметь одно и то же имя.

Отличным примером является функция «rand». В неё мы можем передавать различные типы данных, 
но при этом выполнение функции происходит без каких-либо ошибок. 
Так происходит из-за того, что в функция «rand» имеет множество перегрузок на разные типы данных. 

Как создать перегрузку?
Чтобы создать перегрузку необходимо прописать метод с тем же именем, 
но при этом указать либо другое количество принимаемых параметров, либо другие типы данных для принимаемых параметров.

Пример:

```cpp
void getInfo(char some) {
    cout << some << "!";
}

int getInfo(int a, int b) {
    return a + b;
}
```

Теперь при вызове метода компилятор будет понимать какие параметры были переданы и в зависимости от этого будут вызываться разные методы.
""",
            "Математические операции": """функции: pow(), ceil(), abs(), floor(), sin(), cos() идр
В языке C++ существует библиотека cmath, которая позволяет использовать множество встроенных математических функций.

После подключения библиотеки вы можете использовать функции для получения синуса, косинуса, квадратного корня и многого другого.

Помимо сложных вычислений в языке C++ можно выполнять все математические операции. Это такие операции, как:
вычитание - z = y - x;
сложение - z = y + x;
умножение - z = y * x;
деление - z = y / x (на ноль делить нельзя);
остаток при делении - z = y % x;
Если операция проходит над одной и той же переменной, то можно запись сократить:

z = z + 20;
z += 20; // Эта запись аналогична той, что находиться выше
Если нам необходимо увеличить или уменьшить число на 1, то мы можем прописать ++ и -- соответсвенно:

z = 10;
z += 1;
z++; // Аналогично тому, что прописано выше
""",
            "(Введение в ООП) Классы и объекты": """На начальном этапе ООП – это тёмный лес, в котором многое непонятно и слишком усложнено. 
На самом деле всё вовсе не так. Предлагаем абстрагироваться от специфических (непонятных) определений и познакомиться с ООП простыми словами. 

ООП простыми словами
Поскольку на примере все усвоить гораздо проще, то давайте за пример возьмем робота, которого постараемся описать за счёт классов в ООП.

Класс в случае с роботом – это его чертёж. Экземпляром класса (объектом) называет целый робот, который создан точно по чертежу.

Наследование – это добавление полезных опций к чертежу робота. 
К примеру, берем стандартный чертёж робота и дорисуем к нему лазеры, крылья и броню. 
Все эти дорисовки мы сделаем в классе наследнике, основной функционал которого взят из родительского класса.

Полиморфизм – это общий функционал для всех роботов и не важно что каждый робот может очень сильно отличаться друг от друга. 
К примеру, в главном классе мы указываем возможность передвижения для всех последующих роботов. 
Далее в классе наследнике мы можем дополнительно указать возможность левитации для робота, в другом же классе укажем возможность передвижения по воде и так далее. 
Получается, что есть общий функционал что записан в главном чертеже, но его можно переписать для каждого последующего робота (для каждого наследника).

А инкапсуляция является для нас бронёй, защищающей робота. 
Под пластырем брони находятся уязвимые элементы, вроде проводов и микросхем. После прикрытия брешей с помощью брони (protected или private), 
робот полностью защищён от внешних вмешательств. По сути, мы делаем доступ ко всем полям лишь за счёт методов, тем самым прямой доступ к полю будет закрыт.

У всех классов методы могут отличаться, как и поля с конструкторами. 
Каждый класс позволяет создавать любое количество разных объектов, все из них имеют собственные характеристики.

Создание классов
Для создания класса необходимо прописать ключевое слово class и далее название для класса. 
Общепринято начинать названия классов с буквы в верхнем регистре, но если этого не сделать, то ошибки не будет.

В любом классе можно создавать поля (переменные), методы (функции), а также конструкторы.

Создав новый класс и поместив туда какую-либо информацию мы можем создавать на основе него новые объекты. 
Объекты будут иметь доступ ко всем характеристикам класса, которые отмечены модификатором public.

Существует три модификатора доступа:

public - данные будут видны повсюду, как в классе, так и вне его;
protected - данные будут видны только в классе, где они были созданы, а также в классах наследниках;
private - данные будут видны только в классе, где они были созданы.
Пример простого класса приведен ниже:

```cpp
class Book {
public:
    int pages;
    char name;
    float weight;

    void getInfoBook () {
        cout << "В книге " << name << " находиться " << pages << " страниц. " << endl;
        cout << "При этом она весит " << weight << endl;
    } 
};
```

На основе такого класса мы можем создать множество объектов. 
Каждый объект в данном случае будет представлять из себя конкретную книжку. 
Для каждого объекта мы можем указать уникальные данные: количество страниц, название книги и её вес.

Чтобы создать объект нам потребуется следующий код:

```cpp
Book sherlock_holms; // Создание объекта
sherlock_holms.getInfoBook(); // Вызов метода класса
Такой код можно прописать и в одной строке кода. Мы для наглядности разбили код в две строки.
```

Чтобы брать данные из класса через объект необходимо ставить точку и указывать имя переменной или функции, которую мы хотим взять.
""",
            "Конструкторы и деструкторы": """Конструктор класса очень удобен и по своему виду схож с обыкновенными функциями. 
За счёт конструктора мы можем установить значения для объекта сразу при его создании.

Конструктор должен иметь одинаковое название с классом. Пример создания конструктора показан ниже:

```cpp
class Book {
private:
    int pages;
    float weight;
public: 
    char name;

    void getInfoBook () {
        cout << "В книге " << name << " находиться " << pages << " страниц. " << endl;
        cout << "При этом она весит " << weight << endl;
    } 

    Book (int _pages, float _weight) {
        pages = _pages;
        weight = _weight;
    }

    Book (int _pages, float _weight, char _name) {
        pages = _pages;
        weight = _weight;
        name = _name;
    }
};
```

В одном классе может быть сразу несколько конструкторов. 
Создав несколько конструкторов мы можем передавать разное количество параметров при создании объекта.

Компилятор сам определяет какой конструктор необходимо использовать в зависимости от передаваемых параметров и их типов данных. 

В коде выше переменные идут с модификатором доступа private. 
Дело в том, что все переменные лучше делать либо private, либо protected. 
Доступ к переменным должен осуществляться только за счёт методов и конструкторов. Доступ к полям напрямую должен быть закрыт.

Дополнительно создадим два объекта и выведем информацию:

```cpp
int main() {
    Book sherlock_holms(460, 1.7f); // Используем 1 конструктор
    sherlock_holms.name = 'S'; // Устанавливаем вручную значение для name
    sherlock_holms.getInfoBook ();

    Book green_mile(750, 2.8f, 'G'); // Используем второй конструктор
    green_mile.getInfoBook ();

    return 0;
}
```

Поскольку переменная name имеет public модификатор доступа, то мы можем ссылаться к ней отдельно. 
Лучше так не делать и для неё тоже установить модификатор private.

Также конструктор может не принимать параметров. 
В таком случае при создании объекта ничего не надо дополнительно передавать.

Деструкторы
Деструкторы работают в обратную сторону от конструкторов. 
Конструктор вызывается при создании объекта, а деструктор при удалении.

Пример создания деструктора:

```cpp
class Some {
public:
    ~Some () {
        cout << "Работа с объектом завершена.";
    }
};
```

Исходный код

Конструкторы и деструкторы

```cpp
using namespace std;

class Auto {
private:
    int year, month, day;
public:
    Auto () {
        year = 2000;
        month = 12;
        day = 31;

        get();
        cout << endl;
    }

    Auto (int date_year, int date_month, int date_day) {
        year = date_year;
        month = date_month;
        day = date_day;

        get();
        cout << endl;
    }

    void message () {
        cout << "Class is working!" << endl;
    }

    void set (int date_year, int date_month, int date_day) {
        year = date_year;
        month = date_month;
        day = date_day;
    }

    void get () {
        cout << "Year of this auto is - " << year << ", month is - " << month << ", day is - " << day << endl;
    }

    ~Auto () {
        cout << "Class is not working" << endl;
    }
};

int main(int argc, const char * argv[]) {

    Auto shkoda (2015, 2, 13);
    shkoda.message();
    shkoda.set(2005, 11, 23);
    shkoda.get();

    Auto bmw;
    bmw.set(2012, 1, 11);
    bmw.get();

    cin.get();
    return 0;
}
```
""",
            "20 Дружественные функции": """Дружественная функция - это функция, что имеет доступ к полям и методам класса, при этом сама функция может быть создана вне класса. 

Для создания дружественной функции необходимо прописать обыкновенную функцию вне классов 
и далее для классов что будут работать с этой функцией объявить её, указав имя, а также поставив слово friend перед типом данных функции.

После создания такой функции вы сможете через неё управлять всеми данными во всех классах, 
что указали функции её как дружественную. Доступ будет даже к тем полям, у которых модификатор доступа стоит как private или protected.
""",
            "Дружественные классы": """Дружественные классы по своей работе схожи с дружественными функциями. 
Единственное отличие заключается в объединение не просто функций, а целых классов.

Благодаря дружественному свойству мы можем указать несколько классов, что будут связаны между собой. 
Это позволит брать данные через объект сразу из нескольких классов.

За счёт этого мы может точно описать логику для различных персонажей в игре или для окон в приложении. 
Все они могут быть записаны в разных классах, но при этом каждый сможет иметь доступ друг к другу.

Пример создания дружественного класса:

```cpp
class Auto;
class Motorcycle {
    friend class Auto;
private: 
    bool isStillWorking = true;
};

class Auto {
public:
    void CrashDTP(Auto &moto) {
        moto.isStillWorking = false;
        cout << "Motorcycle is currently not working!";
    }
};
```

Из примера видно, что для дружественных классов используется схожая структура что для дружественных функций.

Перед объявление класса Motorcycle указывается существование класса Auto: class Auto. 
Далее мы делаем класс Auto дружественным и для этого используем ключевое слово friend.
""",
            "Указатель this": """За счёт указателя this мы можем точно указать откуда берутся данные. 
При работе с данными внутри одного класса часто необходимо обратить к полям или методом самого класса. 
Чтобы не возникало конфликтов имен можно использовать указать «this».

Пример работы:

```cpp
class Some {
private
    int test;

public:
    void set (int test) {
        this->test = test;
    }
};
```

При использовании указателя данный код не вызовит ошибок и все обработается корректно.


Обьяснение от ChatGPT:

this - это указатель на текущий объект внутри метода класса. 
Он используется для обращения к полям и методам текущего объекта.

Например, если у вас есть класс Person, и вы хотите использовать поле name текущего 
объекта внутри метода printName, то вы можете сделать это следующим образом:

```cpp
class Person {
  public:
    string name;
    void printName() {
      cout << this->name << endl;
    }
};
```

В этом примере this указывает на текущий объект класса Person, 
и мы можем использовать его, чтобы достучаться до поля name и вывести его на экран.
""",
            "Наследование классов (ООП)": """Наследование является одним из ключевых понятий ООП. 
За счёт наследования можно создать один общий класс (класс родитель) и создать множество других классов (классы наследники), 
что будут наследовать все поля, методы и конструкторы из главного класса.

За чем использовать наследование?
Предположим что у нас есть один большой класс «Транспорт». В классе описываются базовые характеристики для всех транспортных средств:

поля: скорость, вес, запас хода и тому подобное;
методы: получение информации из полей, установка новых значений;
конструктор: пустой и по установке всех полей.


На основе класса мы спокойно можем создать объект легковой машины, объект грузовика, объект самолета и так далее. 
У всех объектов будут одинаковые характеристики и методы. 

Мы явно понимаем, что у объекта машина и самолёт будут разные поля и характеристики. Как можно поступить:

Можно создать два отдельных класса: «Car» и «Airplane». 
В каждом классе будут все методы, поля и конструкторы повторно переписанные из класса «Транспорт», 
а также будут новые методы, что важны только для конкретного класса;
Можно создать два класса наследника: «Car» и «Airplane». 
Оба класса будут наследовать всё от класса «Транспорт» и при этом будут содержать свои дополнительные функции. 
Таким образом повторения кода не будет и код станет меньше и чище.


Создание классов наследников
Для создания класса наследника требуется создать класс и указать наследование от главного класса.

Пример класса наследника:

```cpp
class Transport {
protected:
    float speed;
};

class Auto : public Transport {
private:
    int wheels;

public:
    Auto (float speed, int wheels) {
        this->speed = speed;
        this->wheels = wheels;
        cout << "Speed is: " << speed << ", model is - " << wheels << endl;
    }
};

int main() {
    Auto bmw(301.2, 4);
    Auto mercedes(270, 4);

    return 0;
}
```

Как вы можете заметить, у нас есть одна общая переменная speed. 
Поскольку модификатор доступа у неё protected, то доступ к переменной мы имеем 
внутри класса Transport, а также внутри всех классов наследников.

Для создания наследования мы прописали ключевое слово : после имени класса и указали какой класс будет родительским.
""",
            "Шаблоны функций (template)": """Шаблоны функций, а также шаблоны классов в языке C++ это мощные технологии, 
что позволяют создавать шаблонные конструкции и далее при передачи данных передавать как значения, так и типы данных.

Для создания шаблонной функции необходимо использовать ключевое слово template, 
а также в угловых скобках необходимо указывать принимаемый тип данных. 
Можно принимать один или несколько типов данных. 

Пример создания шаблонной функции:
```cpp
template <typename Type1> // Указываем что это шаблон функции
// Принимаем параметр value и его тип данных мы получим
// также в качестве передаваемого параметра - Type1
void funct (Type1 *value) {
    cout << value; // Просто выводим это значение
}
```

Для передачи нескольких типов данных стоит прописать следующее:

```cpp
// Здесь мы получаем сразу два типа данных
template <typename Type1, typename Type2>
void funct (Type1 *value, Type2 *newValue) {
    // Мы можем использовать передаваемые типы в самой функции
    Type1 someNew;
    cout << newValue; // Просто выводим значение
}
```

Для вызова шаблонной функции пропишите следующее:

```cpp
// Вызов функции с одним параметром
funct<double>(value);
// Вызов с несколькими параметрами
funct<char, double>(value, oneMoreValue);
```

Шаблоны функций

```cpp
#include <iostream>

using namespace std;

template <typename T1, typename T2>
T2 printArr (const T1 * array, int i) {
    int count = 0;
    for (int j = 0; j < i; j++) {
        cout << array[j] << " ";
        count++;
    }
    cout << endl;
    return count;
}

int main(int argc, const char * argv[]) {

    const int iSize = 3, fSize = 2, dSize = 3, cSize = 5;

    int i_arr[iSize] = {23, 45, 78};
    float f_arr[fSize] = {12.2, 67.5};
    double d_arr[dSize] = {3.345, 7.567, 9.023};
    char c_arr[cSize] = {"HI!!"};

    cout << "Массив с типом данных int: ";
    cout << "Количество элементов: " << printArr<int, int>(i_arr, iSize) << endl;
    cout << "Массив с типом данных float: ";
    cout << "Количество элементов: " << printArr<float, int>(f_arr, fSize) << endl;
    cout << "Массив с типом данных double: ";
    cout << "Количество элементов: " << printArr<double, int>(d_arr, dSize) << endl;
    cout << "Массив с типом данных char: ";
    cout << "Количество элементов: " << printArr<char, int>(c_arr, cSize) << endl;

    cin.get();
    return 0;
}
```



Обьяснение от ChatGPT:

Шаблоны функций и классов в C++ - это механизм, который позволяет создавать 
универсальные классы и функции, которые могут работать с разными типами данных. 
Вместо того, чтобы создавать отдельную функцию или класс для каждого типа данных, 
вы можете определить шаблон, который может использоваться с разными типами данных.

Определение шаблона функции выглядит так:

```cpp
template <typename T>
T max(T a, T b) {
  return (a > b) ? a : b;
}
```

В этом примере T является параметром шаблона, который может быть любым типом данных. 
Когда вы вызываете функцию max с разными типами данных, компилятор создает специализированную 
версию функции для каждого типа данных, с которым вы вызываете эту функцию.
""",
            "Шаблоны классов": """Шаблоны классов работают по тому же принципу что и шаблоны функций. 
Разница заключается в том, что шаблоны классов описывают шаблонную структура класса, а не функции.

Для создания шаблона класса используйте ключевое слово template. Пример реализации шаблонного класса:

```cpp
template <class SomeType>
class Test {
private:
    SomeType value;
public: 
    SomeType setElement(SomeType value) {
        this->value = value;
        return value;
    }
};
```

При создании объекта на основе шаблонного класса необходимо передать не только значения, но также тип данных.

Пример создания объекта:

```cpp
Test<float> newObject;
newObject.setElement(2.6);
```
""",
            "end": """В ходе видео курса мы изучили основные моменты в языке C++. 
Язык C++ состоит из множества библиотек, которые расширяют его функционал и добавляют новые возможности. 
Изучить все библиотеки невозможно, а главное не нужно.

Вам необходимо выбрать определённую сферу, в которой хотите работать и тогда уже изучать специализированные библиотеки для вашей сферы. 
К примеру, если вы хотите создавать программы под Windows, то можно изучить работу с программой QT.

На закрепление знаний вы можете просмотреть большой видео урок по изучению C++ за час! 
Также вы можете перейти на страницу с этим видео и получить дополнительные домашние задания и готовый код.

Программа обучения
Также хотим отметить, что если вас интересует более углубленное изучение самого языка и его фреймворков, 
то предлагаем вашему внимаю наш полный курс по изучению C++. 
За курс вы изучите язык C++, научитесь работать с библиотекой STL, 
базами данных, многопоточностью и научитесь строить приложения при помощи WinForms и QT.
""",
            "ChatGPT": """можешь переписать этот код на C++?
a = [0, 1, 'привет', 'мир']
print(a[2], a[3])
----------------------------------------------------------------
Да, я могу переписать этот код на C++:

```cpp
#include <iostream>
#include <vector>

int main() {
    std::vector<std::string> a = { "0", "1", "привет", "мир" };
    std::cout << a[2] << " " << a[3] << std::endl;
    return 0;
}
```

Здесь я использовал std::vector, чтобы создать массив строк, 
поскольку C++ не поддерживает нетипизированные массивы.
""",
            "Разное": r"""https://metanit.com/cpp/tutorial/

Вывод в консоль

```cpp
cout << "Hello World!\n";
```

Функция вывода

```cpp
template <typename T>
void print(T args) {cout << args << "\n";}
print("text1", "text2");
```

Русский язык в консоли

```cpp
int main() {SetConsoleCP(1251); SetConsoleOutputCP(1251);
```

Параметры для функции main
```cpp
int main (int argc, char *argv[]) {}
```

многострочный комментарий

```cpp
/* многострочный комментарий */
```

Автоподстановка типа

```cpp
auto number = 5;
```

Подобие mach/case в Python

```cpp
int x = 2;
switch (x) {
    case 1:
        std::cout << "x = 1" << "\n";
        break;
    case 2:
        std::cout << "x = 2" << "\n";
        break;
    case 3:
        std::cout << "x = 3" << "\n";
        break;
    default:
        std::cout << "x is undefined" << "\n";
        break;
    }
```

Позволяет сократить определение простейших условных конструкций if и имеет следующую форму:
[первый_операнд - условие] ? [второй_операнд] : [третий_операнд]
                                if true             if false
```cpp
int result = sign == '+' ? x + y : x - y;
```

&& (конъюнкция, логическое умножение)
Возвращает true, если оба операнда не равны false.
Возвращает false, если хотя бы один операнд равен false.

```cpp
bool a = true;
bool b = false;
bool c = a && b;    // false
bool d = a && true; // true
```

|| (дизъюнкция, логическое сложение)
Возвращает true, если хотя бы один операнд равен true.
Возвращает false, если оба операнда равны false.

```cpp
bool a = true;
bool b = false;
bool c = a || b;        // true
bool d = b || false;    // false
```
""",
            "Операции над числами": r"""Префиксный инкремент. Увеличивает значение переменной на единицу и 
полученный результат используется как значение выражения ++x

```cpp
int a = 8; int b = ++a;
std::cout << a << "\n"; // 9
std::cout << b << "\n"; // 9
```

Постфиксный инкремент. Увеличивает значение переменной на единицу, 
но значением выражения x++ будет то, которое было до увеличения на единицу

```cpp
int a = 8; int b = a++;
std::cout << a << "\n"; // 9
std::cout << b << "\n"; // 8
```

Префиксный декремент. Уменьшает значение переменной на единицу, и полученное значение используется как значение выражения

```cpp
int a = 8; int b = --a;
std::cout << a << "\n"; // 7
std::cout << b << "\n"; // 7
```

Постфиксный декремент. Уменьшает значение переменной на единицу, но значением выражения x-- будет то, которое было до уменьшения на единицу

```cpp
int a = 8; int b = a--;
std::cout << a << "\n"; // 7
std::cout << b << "\n"; // 8
```
""",
            "for while": r"""Цикл for
for (начальные_условия;  условие_для_выполнения_цикла; изменение_параметров_цикла) {}

```cpp
for(int i = 1; i < 10; i++) {}
```

Но можно и так

```cpp
int i = 1;
for (; i < 10;) {
    std::cout << i << " * " << i << " = " << i * i << std::endl;
    i++;
}
```

Этот цикл применим к контейнерам разной природы (массивам, векторам, спискам и т. д.).
Пока рассмотрим его на примере строк. 
Цикл позволяет удобно проитерироваться по символам строки, не используя индексов. 
В этом примере мы считываем строку и печатаем отдельно все символы строки и их ASCII-коды:

```cpp
#include <iostream>
#include <string>
 
int main() {
    std::string line;
    std::getline(std::cin, line);
    for (char symbol : line) {
        std::cout << symbol << "\t" << static_cast<int>(symbol) << "\n";
    }
}
```
""",
            "Массив": r"""Массив
тип_переменной название_массива [длина_массива]

```cpp
int numbers[4];
int numbers[4] = {1,2,3,4};
int numbers[4] = {1, 2, 3, 4, 5, 6}; //ОШИБКА!
int numbers[] = {1, 2, 3, 4, 5, 6};
char s1[] = {'h', 'e', 'l', 'l', 'o'}; длинна 5
char s2[] = "world"; длинна 6! (добавляется '\0')
//Нельзя присвоить одному массиву другой массив
int nums1[] = {1,2,3,4,5};
int nums2[] = nums1;    // ошибка
nums2 = nums1;          // ошибка
```

Перебор массива

```cpp
#include <iostream>
int main()
{
    int numbers[4] = { 1,2,3,4 };
    int size = sizeof(numbers) / sizeof(numbers[0]);
    for (int i = 0; i < size; i++)
        std::cout << numbers[i] << std::endl;
    return 0;
}
```

Или цикл for специально для массивов

```cpp
#include <iostream>
int main()
{
    int numbers[4] = { 1,2,3,4 };
    for (int number : numbers)              //(или можно спользовать auto number)
        std::cout << number << std::endl;

    return 0;
}
```
""",
            "Строка": """Строки
```cpp
#include <string>
std::string s1;                  // пустая строка
std::string s2 = "hello";        // hello
std::string s3("welcome");       // welcome
std::string s4(5, 'h');          // hhhhh
std::string s5 = s2;             // hello

string s1 = "hello";
s1.size() == 5                   // true
s1.empty()                       // false
```

Изменение строки

```cpp
std::string hello = "Hello";
char c = hello[1];               // e
hello[0] = 'M';
std::cout << hello << std::endl; // Mello
```

Форматирование строк

```cpp
string text1 = "text1";
string text2 = "text2";
int number = 12345;
string out = text1 + " " + to_string(number) + " " + text2;
cout << out << endl;
```

Получить полный ввод подобие input()

```cpp
get_line(cin, out)
```

Выберет только первое слово из введённых (подобие text.split()[0] в Python)

```cpp
cin >> out
```
""",
            "Указатели2": """Указатели
& и *

```cpp
int count = 100
m = &count; //m получает адрес count
m == например 2000
q = *m; //q получает значение по адресу m
q == 100

m = &count;
```

Это адрес внутреннего местоположения переменной в компьютере.
С самим значением переменной ничего не делается.
Оператор & можно запомнить как «взятие адреса».
Поэтому вышеупомянутый оператор присваивания можно прочитать как «m получает адрес count».

Для лучшего понимания данного присваивания предположим, 
что переменная count находится по адресу 2000. 
Также предположим, что count имеет значение 100. 
После данного присваивания m будет содержать 2000. 

Оператор*, дополняющий &. Это унарный оператор, возвращающий значение переменной по указанному адресу.
Например: если m содержит адрес переменной count, то

```cpp
q = *m;
```

Следуя вышеприведенному примеру, q получит значение 100, 
поскольку 100 хранилось по адресу 2000 - адресу, находящемуся в переменной m.
Операция* может быть запомнена как «по адресу».
В данном случае оператор можно прочитать как «q получает значение по адресу m».
""",
        },
        "Java": {
            "Запуск": {
                "Запуск": """
Независимо от того, какую операционную систему вы используете, Linux, Mac или Windows,
если на вашем компьютере установлен JDK (Java Development Kit),
вы можете в консоли набрать следующие команды чтобы скомпилировать и запустить программу:

javac (или  javac.exe)
java (или  java.exe)

В первом случае будет вызван компилятор javac.exe,
а во втором случае – запускалка java.exe, которая стартует нашу программу.
Эти файлы лежат в папке bin  вашего JDK.

Рассмотрим на примере. Cоздадим файл с названием Main.java.

```java
public class Main {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}
```

Для того, чтобы скомпилировать его нужно набрать в консоли команду javac и в качестве параметра передать имя нашего файла:

```bash
javac Main.java
```

Эта команда вызовет компилятор, который создаст файл Main.class, содержащий скомпилированный код нашей java программы.

Чтобы запустить ее, нужно ввести команду java с именем класса (не файла!) в качестве параметра:

```bash
java Main // так правильно

java Main.class // так неправильно
```
""",
                "Аргументы": """
# Аргументы

В главном классе нашей программы есть метод public static void main(...), который в качестве аргумента принимает массив String[] args.
Массив строк в качестве аргумента можно передать в программу при запуске из командной строки.
Любой массив в Java имеет переменную длину, это число элементов в этом массиве.
Добавим такой код в класс Main.java:

```java
public class Main {
    public static void main(String[] args) {
        for (int i = 0; i < args.length; i++) {
            System.out.println(args[i]);
        }
    }
}
```

И чтобы скомпилировать и запустить программу с аргументами, пишем в консоль:

```bash
javac Main.java
java Main arg0 arg1 arg2

```
""",
            },
            "Типы данных": """
|         |                                                                     |                                      |
|---------|---------------------------------------------------------------------|--------------------------------------|
| byte    | Число                                                               | 1 байт                               |
| short   | Число                                                               | 2 байта                              |
| int     | Число                                                               | 4 байта                              |
| long    | Число                                                               | 8 байтов                             |
| float   | Число с плавающей точкой                                            | 4 байта                              |
| double  | Число с плавающей точкой                                            | 8 байтов                             |
| char    | Символ                                                              | 2 байта                              |
| boolean | Значение (<br>    true (истина)<br>    или<br>    false (ложь)<br>) | 1 байт                               |

```java
int myNumber;
myNumber = 5;

// or

int myNumber = 5;
```

```java
//Чтобы объявить число с плавающей точкой, используйте следующий синтаксис:

double d = 4.5;
d = 3.0;
// Если вы хотите использовать float, то:

float f = (float) 4.5;
// Или:

float f = 4.5f
(f – более короткий способ объявить float)
```

```java
char c = 'g';

// String – не примитив. Это реальный тип. Вот несколько способов использования строки:

// Создание строки с помощью конструктора

String s1 = new String("Who let the dogs out?");
// С помощью двойных кавычек (” “).

String s2 = "Who who who who!";
// В Java присутсвует конкатенация (объединение) строк при помощи оператора +.

String s3 = s1 + s2;
// В Java нет перегрузки операторов!
// Оператор + определен только для строк,
// вы никогда не увидите его с другими объектами, только с примитивами.

int num = 5;
String s = "I have " + num + " cookies";
// Заметьте, что кавычки с примитивами не используются.
```


```java
boolean b = false;
b = true;

boolean toBe = false;
b = toBe || !toBe;
if (b) {
    System.out.println(toBe);
}
// Оператор || это логическое “или”.

// А например, такой код не будет работать по причине несовместимости типов:

int children = 0;
b = children;  // Не будет работать, требуется boolean, а найден int
if (children) {  // Не будет работать, требуется boolean, а найден int
    // Не будет работать, требуется boolean, а найден int
}
```
""",
            "Логические операторы": """
# Логические операторы
Есть не так много операторов, которые можно использовать в условиях. Вот они:

```java
int a = 4;
int b = 5;
boolean result;
result = a < b;  // истина result = a > b;  // ложь
result = a <= 4; // меньше или равно - истина result = b >= 6;  // больше или равно - ложь
result = a == b;  // равно - ложь
result = a != b;  // неравно - истина
result = a > b || a < b;  // логическое ИЛИ - истина
result = 3 < a && a < 6;  // логическое И - истина
result = !result;  // Логическое НЕ - ложь
```

# Оператор ? :

Есть еще один способ записать if – else в одну строку – с помощью оператора ? :

```java

int a = 4;
int result = a == 4 ? 1 : 8;
// result будет равен 1
// Или обычная форма записи:
int result;
if (a == 4) {
    result = 1;
} else {
    result = 8;
}
```

# Операторы == и equals
Оператор == работает немного по-другому на объектах, нежели на примитивах.
Когда вы используем объекты и хотите проверить, равны ли они,
оператор == скажет что они равны, только если объекты одинаковы,
но если вы хотите проверить их на логическое соответствие, используйте метод equals.

```java
String a = new String("Wow");
String b = new String("Wow");
String sameA = a;

boolean r1 = a == b;      // Ложь, так как a и b не один и тот же объект
boolean r2 = a.equals(b); // Истина, так как a и b логически равны
boolean r3 = a == sameA;  // Истина, так как a и sameA действительно один и тот же объект
```
""",
            "Массив (Array)": """
```java
int[] arr; // Обратите внимание, размер не указан, так что мы еще не создали массив.

arr = new int[10]; // Новый массив размером 10.

// Или с указанием значений в одну строку:

int[] arr = {1, 2, 3, 4, 5};


// Мы можем проверить размер массива, выведя на экран его длину:

System.out.println(arr.length);

// Так же мы можем получить доступ к массиву и установить значения:

arr[0] = 4;
arr[1] = arr[0] + 5;
```

# Вывод значений

Для вывода всех значений массива используйте метод `Arrays.toString()`, преобразующий массив в строку.

```java
System.out.println(Arrays.toString(arr));
```

Или напишите цикл, выводящий последовательно элементы массива.

```java
for(int i=0; i<arr.length; i++) {
    System.out.println(arr[i]);
}
```
""",
            "Циклы": """
# for

Цикл for состоит из трех секций:

```java
for (int i = 0; i < 3; i++) {}
```

Первая секция выполняется один раз, когда мы входим в цикл.
    Задается начальное значение переменной i.

Вторая секция проверяет логическое условие,
    если true,
        выполняются операторы в цикле,
    если false,
        выход из цикла.
      
    В первый раз запускается сразу после первой секции,
    и выполняется каждый раз, пока условие верно, вызывая третью секцию.

Третья секция выполняется каждый раз при выполнении цикла.
В нашем примере это инкремент, который при каждом выполнении
    увеличивает значение переменной на единицу.

Таким образом, цикл будет работать 3 раза.

Мы можем опустить первую и третью секции цикла (как бы странно это ни выглядело), и цикл все еще будет работать:

```java
for (;i < 5;) {}
```

# while 

```java
while (condition) {}

// Если мы хотим, чтобы цикл всегда выполнял по крайней мере одно действие, мы можем использовать do-while:

do {

} while(condition);
```



# foreach
Другая версия for, это foreach.
Но в Java решили не добавлять новое ключевое слово each.
Ключевое слово, которое мы используем, все еще for,
но когда мы хотим выполнить действия над элементами массива, делаем так:

```java
int[] arr = {2, 0, 1, 3};

for (int el : arr) {
    System.out.println(el);
}
```

Это была короткая версия, эквивалентная следующей записи:

```java
int[] arr = {1, 9, 9, 5};
for (int i = 0; i < arr.length; i++) {
    int el = arr[i];
    System.out.println(el);
}
```

Заметьте, что, если вы хотите использовать индекс элемента в цикле,
Вы должны использовать более длинную версию и не можете использовать foreach.

# break and continue

<b>break</b> останавливает цикл и переходит к оператору, следующему за ним.
<b>continue</b> остановит текущую итерацию и переместится в следующую.
""",
            "Классы": {
                "Объекты, конструкторы": """
Давайте начнем с примера:

```java
class Point {
    int x;
    int y;
}
```

Этот класс определяет точку с координатами X и Y.

Для того, чтобы создать экземпляр этого класса, мы должны использовать ключевое слово new.

```java
Point p = new Point();
```

При этом используется так называемый конструктор по умолчанию (или конструктор без параметров)
— это специальный метод класса, мы его не определяли явно, но даже если его не определить, он создаётся автоматически,
выполняется при создании каждого нового объекта
и присваивает первоначальные значения его свойствам (инициализирует их).

От методов в java конструктор отличается тем, что имеет то же самое имя, что и класс, в котором он определен,
а также не имеет типа возвращаемого значения.
Конструктор в java возвращает новый объект – экземпляр родительского класса).



Мы можем определить наш собственный конструктор.
Поскольку методы можно перегружать, а конструктор является методом, то с помощью перегрузки
можно создать дополнительные варианты конструкторов.
Например, удобно иметь конструктор, который позволит при создании объекта Point явно указывать его координаты:

```java
class Point {
    int x;
    int y;

    Point(int x, int y) {
        this.x = x;
        this.y = y;
    }
}
```

Это означает, что мы не можем больше использовать конструктор по умолчанию new Point().
Теперь мы можем пользоваться только перегруженным конструктором  с указанием начальных значений new Point(4, 1).

Мы можете определить более чем один конструктор, так что объект класса Point может быть создан несколькими способами.
Давайте создадим еще один перегруженный конструктор:

```java
class Point {
    int x;
    int y;

    Point() {
        this(0, 0);
    }

    Point(int x, int y) {
        this.x = x;
        this.y = y;
    }
}
```

Обратите внимание на ключевое слово this.
Мы можем использовать его внутри конструктора для вызова другого конструктора (для того, чтобы избежать дублирования кода).

Мы также используем ключевое слово this в качестве ссылки на текущий объект.

После того, как мы определили объект р мы можем получить доступ к X и Y.

```java
p.x = 3;
p.y = 6;
```
""",
                "Методы": {
                    "Методы": """
Методы определяются всегда внутри классов:

```java
public class Main {
    public static void foo() {
        // Тело метода
    }
}
```

foo -  это метод, который мы определили в классе Main, давайте его рассмотрим.

# тип доступа

|           |                                          |
|-----------|------------------------------------------|
| public    | метод может вызываться из другого класса |
| private   | метод доступен только внутри класса      |
| protected | ...                                      |

|        |                                                                         |
|--------|-------------------------------------------------------------------------|
| static | метод принадлежит классу Main, а не конкретному экземпляру класса Main. |

Мы можем вызвать этот метод из другого класса так:
```java
Main.foo().
```

<b>void</b> значит, что этот метод не возвращает значение.
Методы могут возвращать значение в Java и оно должно быть определено при объявлении метода.
Однако, вы можете использовать <b>return</b> просто для выхода из метода.

# return выражение;

Этот оператор возвращает результат вычисления выражения в точку вызова метода.
Тип выражения должен совпадать с типом возвращаемого значения.
Если тип возвращаемого значения – void, возврат из метода выполняется
либо после выполнения последнего оператора тела метода,либо в результате выполнения оператора

```java
return;
```

(таких операторов в теле метода может быть несколько).

Пример объявления метода, возвращающего значение типа int – сумму двух своих параметров типа int:

```java
int sum(int a, int b){
      int x;
      x = a + b;
      return x;
}
```

При вызове метода, например, sum(5, 3), параметры 5 и 3 передаются в метод, как значения соответственно a и b,
и оператор вызова метода sum(5, 3) – заменяется значением, возвращаемым методом (8).

В отличие от языка C, в котором тип параметра, задаваемого при вызове, приводится к типу параметра в объявлении функции,
тип задаваемого параметра в Java должен строго соответствовать типу параметра в объявлении метода,
поэтому вызов метода sum(1.5, 8) приведет к ошибке при компиляции программы.
""",
                    "Методы 2": """
```java
class Point {
    ... // Наш код ранее
    void printPoint() {
        System.out.println("(" + x + "," + y + ")");
    }

    Point center(Point other) {
        // Возвращает центр между этой и другой точками
        // Заметьте, мы используем целое число, поэтому не получим точное значение
        return new Point((x + other.x) / 2, (y + other.y) / 2);
    }
}
```
""",
                    "Не статические методы": """
# Не статические методы

Не статические методы в Java используются чаще, чем статические методы.
Эти методы могут принадлежать любому объекту, экземпляру класса, а не всему классу.

Не статические методы могут получать доступ и изменять поля объекта.

```java
public class Student {
    private String name;
    public String getName() {
        return name;
    }
    public void setName(String name) {
        this.name = name;
    }
}
```

Вызов методов требует экземпляра класса Student.

```java
Student s = new Student();
s.setName("Danielle");
String name = s.getName();

Student.setName("Bob"); // Не будет работать!
Student.getName(); // Не будет работать!
```
""",
                    "Перегруженные методы": """
# Перегруженные методы

В языке Java в пределах одного класса можно определить два или более методов,
которые совместно используют одно и то же имя, но имеют разное количество параметров.
Когда это имеет место, методы называют перегруженными,
а о процессе говорят как о перегрузке метода (method overloading).

Когда метод вызывается, то по количеству параметров и/или их типам среда выполнения Java определяет,
какую именно версию перегруженного метода надо вызывать
(тип возвращаемого значения во внимание не принимается, хотя, в принципе,
он тоже может отличаться у разных версий перегруженных методов).

Например метод

```java
double sum(double a, double b) {
     double x;
     x = a + b;
     return x;
}
```

вместе с объявленным ранее методом int sum(int a, int b)
составляют пару перегруженных методов и при вызове sum(5, 8) будет вызван первый метод,
а при вызове sum(5.0, 8.0) будет вызван второй метод.

По умолчанию метод, как и переменная, доступен только классам в том же пакете (наборе классов), что и исходный класс.
Если перед возвращаемым типом задан модификатор доступа public, то метод является глобальным и доступен любым объектам,
а модификатор private означает, что метод доступен в том классе, в котором он был объявлен,
т.е. метод инкапсулирован в данном классе.
""",
                    "Переопределение методов": """
# Переопределение методов

Кроме перегрузки существует также замещение, или переопределение методов (англ. overriding).
Замещение происходит, когда класс потомок (подкласс) определяет некоторый метод,
который уже есть в родительском классе(суперклассе), таким образом новый метод заменяет метод суперкласса.
У нового метода подкласса должны быть те же параметры или сигнатура, тип возвращаемого результата,
что и у метода родительского класса.

```java
public class Thought {
    public void message() {
        System.out.println("Я себя чувствую как стрекоза, попавшая в параллельную вселенную.");
    }
}

public class Advice extends Thought {
    @Override  // Аннотация @Override с Java 5 является необязательной, но весьма полезной
    public void message() {
        System.out.println("Внимание: Даты в календаре ближе, чем кажутся.");
    }
}
```

Класс Thought представляет собой суперкласс и обеспечивает вызов метода message().
Подкласс, называемый Advice, наследует каждый метод класса Thought.
Однако, класс Advice переопределяет метод message(), замещая функционал, описанный в классе Thought.

В Java, когда подкласс содержит метод, переопределяющий метод суперкласса,
то он может помимо своего метода вызывать и метод суперкласса при помощи ключевого слова super.

Например, нижеследующий вариант выводит оба сообщения при вызове метода подкласса:

```java
public class Advice extends Thought {
    @Override
    public void message() {
        System.out.println("Внимание: Даты в календаре ближе, чем кажутся.");
        super.message(); // Вызов версии метода родительского класса
    }
}
```

Существуют методы, которые подкласс не может переопределять.
Например, в Java метод, объявленный с ключевым словом final, не может быть переопределён.
Методы, объявленные как private или static не могут быть переопределены,
поскольку это соответствует неявному использованию final.
""",
                },
                "Наследование": """
Наследование в Java позволяет повторно использовать код одного класса в другом классе,
то есть вы можете унаследовать новый класс от уже существующего класса.

Главный наследуемый класс в Java называют родительским классам, или суперклассом.
Наследующий класс называют дочерним классом, или подклассом.
Подкласс наследует все поля и свойства суперкласса,
а также может иметь свои поля и свойства, отсутствующие в классе-родителе.

Пример наследования
Рассмотрим класс под названием Shape (Форма).
Shape является базовым классом, от которого наследуются другие формы, таких как прямоугольник, квадрат, круг и т.д.

```java
public class Shape {
    public double area ()
    {
        return 0;   
    }
}
```

Поскольку это просто общая «форма», метод  вычисления площади area() будет возвращать ноль.
Чтобы узнать площадь конкретной фигуры, нужно создать подкласс, унаследованный от класса Shape, и в нем переопределить метод area().

От класса Shape  наследуется класс Circle, который тоже представляет собой форму.

```java
class Circle extends Shape { // ключевое слово "extends" означает наследование

    private static final double PI = Math.PI; // константа
    private double diameter; // любое число, представляющее диаметр этого круга

    public Circle(double diameter) { // конструктор
        this.diameter = diameter;
    }

    public double area() {
        double radius = diameter / 2.0;
        return PI * radius * radius;
    }
}
```

Метод area() базового класса наследуется классом Circle и становится доступен в нем, но нам нужно переопределить метод area()
в классе Circle, таким образом, чтобы он вычислял площадь круга.

Преимущество использования наследования в том, что вы можете написать код,
который можно применить к ряду классов, расширяющих более общий класс.

Создадим  класс Main, и в нем напишем метод, который вычисляет большую площадь двух фигур:

```java
public class Main {
    public static void main(String[] args) {
        Shape s1 = new Circle (5.0);
        Shape s2 = new Rectangle (5.0, 4.0);
        Shape larger = getLargerShape(s1,s2);

        System.out.println("The area of the larger shape is: "+larger.area());
    }

    public static Shape getLargerShape(Shape s1, Shape s2) {
        if(s1.area() > s2.area())
            return s1;
        else
            return s2;
    }
}
```

Как вы можете видеть, метод getLargerShape() не требует указания определенного типа фигуры для его двух параметров.
В качестве параметров для этого метода можно использовать экземпляр любого класса, который наследует тип Shape.
Можно использовать экземпляр класса круг, прямоугольник, треугольник, трапеция, и т.д. – до тех пор, как они наследуют класс формы.
"""
            },
            "Исключения": """
В языке Java все исключения являются объектами и могут быть вызваны не только системой, но и создаваться самим разработчиком.
Исключения делятся на несколько классов, которые имеют общего предка — класс Throwable.
Его потомками являются подклассы Exception и Error.
Исключения (Exceptions) являются результатом проблем в программе, которые в принципе решаемы и предсказуемы.
Например, произошло деление на ноль в целых числах.

Ошибки (Errors) представляют собой более серьёзные проблемы, которые, согласно спецификации Java,
не следует пытаться обрабатывать в собственной программе, поскольку они связаны с проблемами уровня JVM.
Например, исключения такого рода возникают, если закончилась память, доступная виртуальной машине.

В Java все исключения делятся на три типа: контролируемые исключения (checked) и неконтролируемые исключения (unchecked),
к которым относятся ошибки (Errors) и исключения времени выполнения (RuntimeExceptions, потомок класса Exception).

Контролируемые исключения представляют собой ошибки, которые можно и нужно обрабатывать в программе,
к этому типу относятся все потомки класса Exception (кроме RuntimeException).
""",
            # "": """""",
            # "": """""",
        },
        "Bash": {
            "help": """
Работа с файлами
COPY           Копирование одного или нескольких файлов в другое место.
DEL            Удаление одного или нескольких файлов.
REN            Переименовывает файлы.
RENAME         Переименовывает файлы.
REPLACE        Заменяет файлы.
TYPE           Отображает содержимое текстовых файлов.
XCOPY          Копирует файлы и деревья папок.

Работа с папками
DIR            Вывод списка файлов и подпапок из указанной папки.
RD             Удаляет каталог.
RMDIR          Удаляет каталог.


Для получения сведений об определенной команде наберите HELP <имя команды>
CD             Вывод имени либо смена текущей папки.
ECHO           Отображает сообщения и переключает режим отображения команд на экране.
CLS            Очистка экрана.
CMD            Запуск еще одного интерпретатора командных строк Windows.
COLOR          Установка цветов переднего плана и фона, используемых по умолчанию.

ASSOC          Вывод либо изменение сопоставлений по расширениям имен файлов.
ATTRIB         Отображение и изменение атрибутов файлов.
BREAK          Включение и выключение режима обработки комбинации клавиш CTRL+C.
BCDEDIT        Задает свойства в базе данных загрузки для управления начальной загрузкой.
CACLS          Отображение и редактирование списков управления доступом (ACL) к файлам.
CALL           Вызов одного пакетного файла из другого.
CHCP           Вывод либо установка активной кодовой страницы.
CHDIR          Вывод имени либо смена текущей папки.
CHKDSK         Проверка диска и вывод статистики.
CHKNTFS        Отображение или изменение выполнения проверки диска во время загрузки.
COMP           Сравнение содержимого двух файлов или двух наборов файлов.
COMPACT        Отображение и изменение сжатия файлов в разделах NTFS.
CONVERT        Преобразует тома FAT в NTFS. Вы не можете преобразовать текущий диск.
DATE           Вывод либо установка текущей даты.
DISKPART       Отображает или настраивает свойства раздела диска.
DOSKEY         Редактирует командные строки, повторно вызывает команды Windows и создает макросы.
DRIVERQUERY    Отображает текущее состояние и свойства драйвера устройства.
ENDLOCAL       Завершает локализацию изменений среды для пакетного файла.
ERASE          Удаляет один или несколько файлов.
EXIT           Завершает работу программы CMD.EXE (интерпретатора командных строк).
FC             Сравнивает два файла или два набора файлов и отображает различия между ними.
FIND           Ищет текстовую строку в одном или нескольких файлах.
FINDSTR        Ищет строки в файлах.
FOR            Запускает указанную команду для каждого из файлов в наборе.
FORMAT         Форматирует диск для работы с Windows.
FSUTIL         Отображает или настраивает свойства файловой системы.
FTYPE          Отображает либо изменяет типы файлов, используемые при сопоставлении по расширениям имен файлов.
GOTO           Направляет интерпретатор команд Windows в отмеченную строку пакетной программы.
GPRESULT       Отображает информацию о групповой политике для компьютера или пользователя.
GRAFTABL       Позволяет Windows отображать расширенный набор символов в графическом режиме.
HELP           Выводит справочную информацию о командах Windows.
ICACLS         Отображает, изменяет, архивирует или восстанавливает списки ACL для файлов и каталогов.
IF             Выполняет условную обработку в пакетных программах.
LABEL          Создает, изменяет или удаляет метки тома для дисков.
MD             Создает каталог.
MKDIR          Создает каталог.
MKLINK         Создает символьные ссылки и жесткие связи
MODE           Настраивает системные устройства.
MORE           Последовательно отображает данные по частям размером в один экран.
MOVE           Перемещает один или несколько файлов из одного каталога в другой.
OPENFILES      Отображает файлы, открытые для файлового ресурса удаленными пользователями.
PATH           Отображает или устанавливает путь поиска исполняемых файлов.
PAUSE          Приостанавливает выполнение пакетного файла и выводит сообщение.
POPD           Восстанавливает предыдущее значение текущего каталога, сохраненное с помощью команды PUSHD.
PRINT          Выводит на печать содержимое текстового файла.
PROMPT         Изменяет командную строку Windows.
PUSHD          Сохраняет текущий каталог, затем изменяет его.
RECOVER        Восстанавливает данные, которые можно прочитать, с плохого или поврежденного диска.
REM            Записывает комментарии в пакетные файлы или файл CONFIG.SYS.
ROBOCOPY       Улучшенная служебная программа копирования файлов и деревьев папок
SET            Показывает, устанавливает или удаляет переменные среды Windows.
SETLOCAL       Начинает локализацию изменений среды в пакетном файле.
SC             Отображает или настраивает службы (фоновые процессы).
SCHTASKS       Выполняет команды и запускает программы на компьютере по расписанию.
SHIFT          Изменяет положение заменяемых параметров в пакетных файлах.
SHUTDOWN       Позволяет локально или удаленно завершить работу компьютера.
SORT           Сортирует ввод.
START          Выполняет указанную программу или команду в отдельном окне.
SUBST          Связывает путь с именем диска.
SYSTEMINFO     Отображает сведения о свойствах и конфигурации определенного компьютера.
TASKLIST       Отображает все выполняемые задачи, включая службы.
TASKKILL       Прекращение или остановка процесса либо приложения.
TIME           Отображает или устанавливает системное время.
TITLE          Назначает заголовок окна для сеанса CMD.EXE.
TREE           Графически отображает структуру каталогов диска или пути.
VER            Отображает сведения о версии Windows.
VERIFY         Устанавливает режим проверки в Windows правильности записи файлов на диск.
VOL            Отображает метку и серийный номер тома для диска.
WMIC           Отображает сведения об инструментарии WMI в интерактивной командной оболочке.
""",
            "Переменные окружения": """
set MY_VAR="my_value"
Чтобы удалить переменную окружения через командную строку (cmd) в Windows, 
можно использовать команду setx с параметром /m, где /m указывает, что переменная должна быть удалена из системной области.

Например, чтобы удалить переменную MY_VAR, можно выполнить следующую команду в cmd:

```bash
setx MY_VAR /m
```

После выполнения этой команды переменная MY_VAR будет удалена из системной области. 
Обратите внимание, что эта команда не удалит переменную из текущей области видимости командной строки, 
поэтому если вы хотите удалить переменную только из текущей сессии cmd, вы можете использовать команду set:

```bash
set MY_VAR=
```

Эта команда устанавливает значение переменной MY_VAR в пустую строку, что эквивалентно её удалению.


Если вы хотите удалить переменную окружения только временно, в рамках текущей сессии cmd, то можно использовать команду set с параметром /u, который 


Чтобы получить значение переменной, можно использовать команду echo с параметром %variable_name%, 
где variable_name - это имя переменной, значение которой нужно получить. 
Например, чтобы получить значение переменной MY_VAR, можно выполнить следующую команду в cmd:

```bash
echo %MY_VAR%
```

После выполнения этой команды в консоль будет выведено значение переменной MY_VAR, если она определена.

Чтобы сохранить значение переменной в файле, можно использовать оператор перенаправления вывода > или >>. 
Например, чтобы сохранить значение переменной MY_VAR в файл my_file.txt, можно выполнить следующую команду:

```bash
echo %MY_VAR% > my_file.txt
```

После выполнения этой команды значение переменной MY_VAR будет записано в файл my_file.txt, 
и если файл не существовал, то он будет создан. 
Если нужно добавить значение переменной в конец файла, а не перезаписать его, можно использовать оператор >> вместо >:

```bash
echo %MY_VAR% >> my_file.txt
```

Это добавит значение переменной в конец файла my_file.txt, если файл уже существует. 
Если файл не существует, то он будет создан и в него будет записано значение переменной."""
        }
    },
    "Другое": {
        "Форматы файлов": {
            "JSON": r"""
# JSON - JavaScript Object Notation

Tекстовый формат обмена данными, который основан на синтаксисе JavaScript.
Он используется для хранения и обмена структурированными данными и часто используется
в веб-приложениях для обмена данными между клиентом и сервером.
Пример

```json
{
  "name": "John Smith",
  "age": 30,
  "city": "New York"
}
```

```python
import json
config = {"BOT": {"bot_name": "", "token": ""}}
with open("config.json", 'w', encoding='UTF-8') as file:
    file.write(json.dumps(config, indent=4, ensure_ascii=False))
with open("config.json", 'r', encoding='UTF-8') as file:
    config = json.load(file)
print(config)
```



# JSONL

```python
{"name": "Alice Jones", "age": 25, "city": "Los Angeles"}
{"name": "John Smith", "age": 30, "city": "New York"}
{"name": "Bob Johnson", "age": 40, "city": "Chicago"}
```

```python
import json
config = [{"name": "Alice Jones", "age": 25, "city": "Los Angeles"},
          {"name": "John Smith", "age": 30, "city": "New York"},
          {"name": "Bob Johnson", "age": 40, "city": "Chicago"}]
with open("test.jsonl", 'a', encoding='UTF-8') as file:
    file.writelines([str(line)+"\n" for line in config])
with open("config.jsonl", 'r', encoding='UTF-8') as file:
    for line in file:
        data = json.loads(line)
        print(data)
```
""",
            "YAML": """
# YAML - Ain't Markup Language

Формат файлов, который используется для хранения и обмена неструктурированными и структурированными
данными. Например он популярен в файлах настройки приложений, описание конфигураций и т.д.
YAML использует отступы и специальные символы для обозначения структуры данных.
Он также поддерживает множество типов данных, включая строки, числа, логические значения и массивы.
Пример

```yaml
name: John Smith
age: 30
city: New York
```

```python
import yaml # pip install yaml
config = {"BOT": {"bot_name": "", "token": ""}}
with open("config.yaml", "w", encoding="utf-8") as file:
    file.write(yaml.safe_dump(config, sort_keys=False, allow_unicode=True, indent=4))
with open("config.yaml", "r", encoding="utf-8") as file:
    config = yaml.safe_load(file.read())
print(config)
```
""",
            "TOML": """
# TOML - Tom's Obvious, Minimal Language
формат конфигурационных файлов, который был разработан
для использования в проектах, написанных на языке программирования Rust.

TOML файлы имеют структуру ключ-значение, где ключи и значения
разделены знаком "=", и используют синтаксис, похожий на язык программирования INI.
Пример

```toml
[package]
name = "example"
version = "1.0.0"
authors = ["John Doe <john@example.com>"]
```

```python
import toml # pip install toml
config = {"BOT": {"bot_name": "", "token": ""}}
with open("config.toml", "w", encoding='UTF-8') as file:
    file.write(toml.dumps(config))
with open("config.toml", "r", encoding='UTF-8') as file:
    config = toml.load(file)
print(config)
```
""",
            "INI": """
# INI (Initialization) 
формат конфигурационных файлов, который используется 
для хранения настроек приложений и операционных систем. 
Он был разработан в Windows и стал широко используемым 
форматом для хранения конфигурационных данных в различных программных продуктах.
Пример

```ini
[Section1]
key1 = value1
key2 = value2

[Section2]
key3 = value3
key4 = value4
```

```python
# config = configparser.ConfigParser()
# config["BOT"] = {"bot_name": "", "token": ""}

import configparser
config = {"BOT": {"bot_name": "", "token": ""}}
config_ini = configparser.ConfigParser()
for key, value in config.items():
    config_ini[key] = value
with open("config.ini", 'w') as file:
    config_ini.write(file)

config_ini = configparser.ConfigParser()
config_ini.read("config.ini")
print(config)
```
""",
            "XML": """
# XML - eXtensible Markup Language

Расширяемый язык разметки, который используется для хранения и обмена структурированными данными.
Он использует теги для определения структуры данных и может быть использован для хранения
всех видов данных, включая текст, изображения и мультимедиа.
XML широко используется в Интернете для хранения и обмена данными между веб-сервисами и приложениями.
Пример

```xml
<?xml version="1.0" encoding="UTF-8"?>
<note>
<to>Tove</to>
<from>Jani</from>
<heading>Reminder</heading>
<body>Don't forget me this weekend!</body>
</note>
```

```python
# config = ET.Element("config")
# bot = ET.SubElement(config, "BOT")
# ET.SubElement(bot, "bot_name").text = ""
# ET.SubElement(bot, "token").text = ""
# tree = ET.ElementTree(config)

import xml.etree.ElementTree as xml

def dict_to_xml(dct, root_node=None):
    if root_node is None:
        root_node = xml.Element('root')
    for key, value in dct.items():
        node = xml.SubElement(root_node, key)
        if isinstance(value, dict):
            dict_to_xml(value, node)
        else:
            node.text = str(value)
    return root_node

def xml_to_dict(root):
    from collections import defaultdict
    dct = {root.tag: {} if root.attrib else None}
    children = list(root)
    if children:
        dd = defaultdict(list)
        for dc in map(xml_to_dict, children):
            for k, v in dc.items():
                dd[k].append(v)
        dct = {root.tag: {k: v[0] if len(v) == 1 else v for k, v in dd.items()}}
    if root.attrib:
        dct[root.tag].update(('@' + k, v) for k, v in root.attrib.items())
    if root.text:
        text = root.text.strip()
        if children or root.attrib:
            if text:
                dct[root.tag]['#text'] = text
        else:
            dct[root.tag] = text
    return dct

config = {"BOT": {"bot_name": "", "token": ""}}
config = dict_to_xml(config)
tree = xml.ElementTree(config)
with open("config.xml", 'wb') as file:
    tree.write(file, encoding='utf-8', xml_declaration=True)
with open("config.xml", 'r') as file:
    tree = xml.parse(file)
root = tree.getroot()
config = xml_to_dict(root)
print(config)
```
""",
            "CSV": """
# CSV - Comma Separated Values

Текстовый формат файла, который используется для хранения табличных данных.
Каждая строка файла содержит одну запись, а значения в этой записи разделены запятыми.
Пример

```csv
Name,Age,City
John Smith,30,New York
Jane Doe,25,Chicago
```

```python
import csv
data = [['Name', 'Age'], ['Alice', 25], ['Bob', 30], ['Charlie', 35]]
with open("data.csv", 'w', newline='', encoding='UTF-8') as file:
    csv.writer(file).writerows(data)
with open("data.csv", 'r', encoding='UTF-8') as file:
    [print(row) for row in csv.reader(file)]
```
""",
            "TSV и другие": """
TSV - Tab Separated Values

Текстовый формат файла, который похож на CSV, но вместо запятых использует табуляцию для
разделения значений. Он также часто используется для хранения и обмена табличными данными.
Пример

```
Name        Age City
John Smith  30  New York
Jane Doe    25  Chicago
```

Другие виды файлов баз данных
+---------------------------------------------------------------------+
| .MDB (Microsoft Access) - файл базы данных Microsoft Access         |
| .SQLite - файл базы данных SQLite                                   |
| .SQL - файл скрипта SQL                                             |
| .XLSX (Microsoft Excel) - файл электронной таблицы Microsoft Excel  |
| .MDF (Microsoft SQL Server) - файл базы данных Microsoft SQL Server |
| .GDB (Esri Geodatabase) - файл географической базы данных Esri      |
| .DBF (dBase) - файл базы данных dBase                               |
+---------------------------------------------------------------------+
""",
            "SQLite3 to CSV": '''
```python
import sqlite3
import csv

def SQL(Query, params=(), commit: bool = False):
    """Выполняет SQL запрос"""
    with sqlite3.connect(r"database.sqlite") as connection:
        cursor = connection.cursor()
        cursor.execute(Query, params)
        if commit: connection.commit()
        result = cursor.fetchall()
    return result

data = SQL("SELECT * FROM root;")

with open("data.csv", 'w', newline='', encoding='UTF-8') as file:
    writer = csv.writer(file)
    writer.writerow(['column 1', 'column 2', ...])
    writer.writerows(data)

with open('data.csv', 'r', encoding='UTF-8') as file:
    reader = csv.reader(file)
    headers = next(reader)
    SQL(f"""CREATE TABLE root ({', '.join([f"{column} TEXT" for column in headers])});""", commit=True)
    for row in reader:
        SQL(f"""INSERT INTO root ({', '.join(headers)}) VALUES ({', '.join([f'"{row}"' for row in row])})""", commit=True)
```
''',
            "Vedis db": """
https://vedis-python.readthedocs.io/en/latest/quickstart.html

```python
from vedis import Vedis
    db = Vedis(":mem:")  # Create an in-memory database.
    db = Vedis("Dict.vedis")
    with db.transaction():
        db["key"] = "value"
        db.rollback()  # Undo changes.
        db.commit()
    print(db["key"])
```

Пример использования в боте
https://mastergroosha.github.io/telegram-tutorial/docs/lesson_11/""",
        },
        "Примеры решений": {
            "Пирамида граф": """
Нахождение пути с максимальной суммой по "пирамиде"

```python
graph = [
    [75],
    [95, 64],
    [17, 47, 82],
    [18, 35, 87, 10],
    [20,  4, 82, 47, 65],
    [19,  1, 23, 75,  3, 34],
    [88,  2, 77, 73,  7, 63, 67],
    [99, 65,  4, 28,  6, 16, 70, 92],
    [41, 41, 26, 56, 83, 40, 80, 70, 33],
    [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
    [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
    [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
    [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
    [63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
    [ 4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23],
]

# Cоздаем пустой словарь для хранения сумм каждого узла.
sums = {}
for i in range(len(graph)):
    for j in range(len(graph[i])):
        sums[(i, j)] = graph[i][j]

# Проходимся по каждому узлу в пирамиде и вычисляем сумму каждого узла
# Начинаем с последней строки пирамиды и движемся вверх
for i in range(len(graph)-2, -1, -1):
    for j in range(len(graph[i])):
        sums[(i, j)] += max(sums[(i+1, j)], sums[(i+1, j+1)])

# Step 3
max_sum_path = sums[(0, 0)]

# Step 4
i, j = 0, 0
path = [graph[0][0]]
while i < len(graph) - 1:
    left_sum = sums[(i+1, j)]
    right_sum = sums[(i+1, j+1)]
    if left_sum > right_sum:
        i += 1
    else:
        i += 1
        j += 1
    path.append(graph[i][j])

print(sum(path))
```

```python
def max_sum_path(graph):
    n = len(graph)
    # Инициализируем максимальную сумму первого элемента
    max_sum = graph[0][0]
    for i in range(1, n):
        # Проходим по строкам и столбцам "ниже" текущего элемента
        for j in range(i + 1):
            if j == 0: # Если элемент находится на краю графа, то соседи существуют только с одной стороны
                graph[i][j] += graph[i - 1][j]
            elif j == i: # Если элемент находится на краю графа, то соседи существуют только с одной стороны
                graph[i][j] += graph[i - 1][j - 1]
            else: # В остальных случаях элемент имеет двух соседей
                graph[i][j] += max(graph[i - 1][j - 1], graph[i - 1][j])
            # Обновляем максимальную сумму
            max_sum = max(max_sum, graph[i][j])
    return max_sum

# Пример использования функции
graph = [[45], [23, 78], [12, 26, 51]]
print("Максимальная сумма пути в графе:", max_sum_path(graph))
```

```python
def longest_slide_down(p):
    res = p.pop()
    while p:
        tmp = p.pop()
        res = [tmp[i] + max(res[i],res[i+1]) for i in range(len(tmp))] 
    return res.pop()
```


# Обьяснение
Если граф будет равен

```python
graph = [
        [45], 
      [23, 78], 
    [12, 26, 51]]
```
""",
        },
        "Пример этой кнопки": """
```
<button onclick="showText( {NAME} )" class="trigger"> {NAME} </button>
<pre id=" {NAME} " style="display:none;" class="code-str-1">
{TEXT}
</pre>
```

или полный вариант:

```
button onclick="showText( {NAME} )" class="trigger"> {NAME} </button>
<div id=" {NAME} " style="display:none;" class="button-field">
    <button onclick="PutText( {NAME-1} )" class="trigger"> {NAME-1} </button>
    <pre id=" {NAME-1} " style="display:none;" class="code-str-1">
{TEXT}
</pre>
```
"""
    },
    "Полезные ссылки": """
# **Python**
| Описание                              |                                   Ссылка                                            |
|:--------------------------------------|:------------------------------------------------------------------------------------|
| Дорожная карта                        | https://roadmap.sh/python https://roadmap.sh/backend https://roadmap.sh/roadmaps    |
| Sorting Algorithms                    | https://www.tutorialspoint.com/python_data_structure/python_sorting_algorithms.htm  |
|                                       | https://realpython.com/sorting-algorithms-python/                                   |
| логирование                           | https://habr.com/ru/companies/wunderfund/articles/683880/                           |
| re                                    | https://www.exlab.net/files/tools/sheets/regexp/regexp.pdf                          |
|                                       | https://www.exlab.net/files/tools/sheets/regexp/regexp.png                          |
| Recursive Regular Expressions         | http://www.rexegg.com/regex-recursion.html                                          |
| Магические методы                     | https://habr.com/ru/post/186608/                                                    |
| Unit Tests                            | https://machinelearningmastery.com/a-gentle-introduction-to-unit-testing-in-python/ |
| Асинхронность                         | https://habr.com/ru/articles/421625/                                                |
|                                       |                                                                                     |
|                                       |                                                                                     |

**__Уже есть__**

|                   |                                          |
|:------------------|:-----------------------------------------|
| логирование       | Языки -> Python -> Библиотеки -> logging |
| re                | Языки -> RegExp                          |
| Магические методы | Языки -> Python -> Магические методы     |
| Асинхронность     | Общее -> sync asyn                       |


# **Python Другое**
|                                       |                                                                                     |
|:--------------------------------------|:------------------------------------------------------------------------------------|
| Алгоритм генерации судоку             | https://habr.com/ru/articles/192102/                                                |
|                                       | https://habr.com/ru/post/249899/                                                    |
|                                       | https://www.cs.mcgill.ca/~aassaf9/python/algorithm_x.html                           |
| Компиляторы и трансляторы кода Python | https://egorovegor.ru/python-compiler-and-translator/                               |
|                                       | https://medium.com/doctolib/understanding-and-fixing-n-1-query-30623109fe89         |
| N + 1 query                           |                                                                                     |
|                                       |                                                                                     |

# **C++**
|                                       |                                                                                     |
|---------------------------------------|-------------------------------------------------------------------------------------|
| Дорожная карта                        | https://habr.com/ru/specials/726724/                                                |
|                                       | https://practicum.yandex.ru/blog/yazyk-c-plus-dlya-chego-nuzhen/                    |
|                                       | https://en.cppreference.com/w/                                                      |
|                                       |                                                                                     |
|                                       |                                                                                     |
|                                       |                                                                                     |
|                                       |                                                                                     |
|                                       |                                                                                     |
|                                       |                                                                                     |
|                                       |                                                                                     |


# **GIT GitHub**
|                                       |                                                                                     |
|---------------------------------------|-------------------------------------------------------------------------------------|
| Git и Github. Простые рецепты         | https://habr.com/ru/articles/273897/                                                |
| Книга                                 | https://git-scm.com/book/ru/v2                                                      |
|                                       |                                                                                     |
|                                       |                                                                                     |
|                                       |                                                                                     |

""",
    "test": r"""
Нажмите на кнопку с темой, чтобы увидеть здесь обьяснение
варианты кода
&lt;color> квадрат с цветом или фон для текста
&lt;code> без подсветки
&lt;sql> подсветка sql
&lt;python> подсветка питон
"""
}

# if __name__ == "__main__":
#     import os
#     os.system('python "creator.py"')