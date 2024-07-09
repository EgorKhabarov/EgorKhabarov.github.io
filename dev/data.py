import html

from pygments import highlight
from pygments.formatters.html import HtmlFormatter
from pygments.lexers import get_lexer_by_name

n = "\n"


def escape_markdown(content: str) -> str:
    # parse = re.sub(r"([_*\[\]()~`>\#\+\-=|\.!])", r"\\\1", content)
    # reparse = re.sub(r"\\\\([_*\[\]()~`>\#\+\-=|\.!])", r"\1", parse)
    # return reparse
    return content.replace("__", "&#95;&#95;")


def to_string(text: str) -> str:
    return rf"<span class=\"s1\">{html.escape(text)}</span>"


def to_table_code(lang: str, code_block: str) -> str:
    code_block = code_block  # html.escape(code_block).replace("\n", "<br>")
    formatter = HtmlFormatter(style="default")
    lexer = get_lexer_by_name(lang, stripall=True)
    highlighted_code = (
        highlight(code_block, lexer, formatter).strip().replace("\n", "<br>")
    )
    result = rf"""
<div class="code" style="border-radius:.375rem .375rem;">
<div class="highlight">
<pre>
{highlighted_code}
</pre>
</div>
</div>
    """.strip().replace(
        "\n", ""
    )
    return result


def to_table_code_py(code_block: str) -> str:
    return to_table_code("python", code_block)


def tblcode(lang: str, code: str) -> str:
    match lang:
        case "sh":
            lang = "shell"
        case "py":
            lang = "python"
        case "bs":
            lang = "bash"
    return to_table_code(lang, code)


DICT = {
    "Общее": {
        "GIT": {
            "Команды": """
https://git-scm.com/

|                                          |
|------------------------------------------|
| git config --global user.name "username" |
| git config --global user.email "email"   |

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

<img alt="GIT.png" src="Общее\GIT\GIT.png">
""",
            "gitignore": """
| Шаблон | Примеры соответствия | Пояснение |
|--------|----------------------|-----------|
| **/logs                              | logs/debug.log<br>logs/monday/foo.bar<br>build/logs/debug.log                              | Добавьте в начало шаблона две звездочки,<br>чтобы сопоставлять каталоги в любом месте репозитория. |
| **/logs/debug.log                    | logs/debug.log<br>build/logs/debug.log<br>но не<br>logs/build/debug.log                    | Две звездочки можно также использовать для сопоставления файлов<br>на основе их имени и имени родительского каталога. |
| *.log                                | debug.log<br>foo.log<br>.log<br>logs/debug.log                                             | Одна звездочка — это подстановочный знак, который может<br>соответствовать как нескольким символам, так и ни одному. |
| *.log<br>!important.log              | debug.log<br>trace.log<br>но не<br>important.log<br>logs/important.log                     | Добавление восклицательного знака в начало шаблона отменяет действие шаблона.<br>Если файл соответствует некоему шаблону,<br>но при этом также соответствует отменяющему шаблону, указанному после,<br>такой файл не будет игнорироваться. |
| *.log<br>!important/*.log<br>trace.* | debug.log<br>important/trace.log<br>но не<br>important/debug.log                           | Шаблоны, указанные после отменяющего шаблона,<br>снова будут помечать файлы как игнорируемые,<br>даже если ранее игнорирование этих файлов было отменено. |
| /debug.log                           | debug.log<br>но не<br>logs/debug.log                                                       | Косая черта перед именем файла соответствует файлу в корневом каталоге репозитория. |
| debug.log                            | debug.log<br>logs/debug.log                                                                | По умолчанию шаблоны соответствуют файлам, находящимся в любом каталоге |
| debug?.log                           | debug0.log<br>debugg.log<br>но не<br>debug10.log                                           | Знак вопроса соответствует строго одному символу. |
| debug[0-9].log                       | debug0.log<br>debug1.log<br>но не<br>debug10.log                                           | Квадратные скобки можно также использовать<br>для указания соответствия одному символу из заданного диапазона. |
| debug[01].log                        | debug0.log<br>debug1.log<br>но не<br>debug2.log<br>debug01.log                             | Квадратные скобки соответствуют одному символу из указанного набора. |
| debug[!01].log                       | debug2.log<br>но не<br>debug0.log<br>debug1.log<br>debug01.log                             | Восклицательный знак можно использовать для указания<br>соответствия любому символу, кроме символов из указанного набора. |
| debug[a-z].log                       | debuga.log<br>debugb.log<br>но не<br>debug1.log                                            | Диапазоны могут быть цифровыми или буквенными. |
| logs                                 | logs<br>logs/debug.log<br>logs/latest/foo.bar<br>build/logs<br>build/logs/debug.log        | Без косой черты в конце этот шаблон будет соответствовать и файлам,<br>и содержимому каталогов с таким именем.<br>В примере соответствия слева игнорируются и каталоги, и файлы с именем logs |
| logs/                                | logs/debug.log<br>logs/latest/foo.bar<br>build/logs/foo.bar<br>build/logs/latest/debug.log | Косая черта в конце шаблона означает каталог.<br>Все содержимое любого каталога репозитория, соответствующего этому имени<br>(включая все его файлы и подкаталоги), будет игнорироваться |
| logs/<br>!logs/important.log         | logs/debug.log<br>logs/important.log                                                       | Минуточку!<br>Разве файл logs/important.log из примера слева<br>не должен быть исключен нз списка игнорируемых?<br>Нет!<br>Из-за странностей Git, связанных с производительностью,<br>вы не можете отменить игнорирование файла, которое задано шаблоном соответствия каталогу |
| logs/**/debug.log                    | logs/debug.log<br>logs/monday/debug.log<br>logs/monday/pm/debug.log                        | Две звездочки соответствуют множеству каталогов или ни одному. |
| logs/*day/debug.log                  | logs/monday/debug.log<br>logs/tuesday/debug.log<br>но не<br>logs/latest/debug.log        | Подстановочные символы можно использовать и в именах каталогов. |
| logs/debug.log                       | logs/debug.log<br>но не<br>debug.log<br>build/logs/debug.log                               | Шаблоны, указывающие на файл в определенном каталоге,<br>задаются относительно корневого каталога репозитория.<br>(При желании можно добавить в начало косую черту, но она ни на что особо не повлияет.) |
""",
        },
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


""",
        },
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

for (int i = 0; i < N.Length; i++) {
    if (N[i] > 3 && N[i] < 100){
        nums.Add(N[i]);
    }
}

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
""",
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
    },
    "Языки": {
        "Python": {
            "Библиотеки": {
                "Оглавление": """
# Внимание! Все шпаргалки сгенерированы с помощью ChatGPT 3

**Возможны ошибки и неточности**

Система
Информация
Python
Веб
""",
                "Система": {
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
                },
                "Информация": {
                    "Типы данных": {
                        "xml": r"""
Библиотека "xml" в Python используется для работы с XML-данными.
Она предоставляет функциональность для чтения, записи, и обработки XML-файлов.

Методы модуля "xml" и его подмодулей:
xml.etree.ElementTree: Позволяет работать с XML-деревом, включая чтение, запись, и обработку XML-элементов.
xml.dom: Предоставляет интерфейсы для работы с DOM (Document Object Model) XML-документов.
xml.sax: Предоставляет SAX (Simple API for XML) интерфейс для обработки XML-документов в потоковом режиме.

Самые часто используемые методы:
xml.etree.ElementTree.parse(file): Читает XML-файл и возвращает корневой элемент дерева.

```python
import xml.etree.ElementTree as ET

tree = ET.parse('file.xml')
root = tree.getroot()
```

xml.etree.ElementTree.Element.findall(tag): Возвращает список элементов с указанным тегом.

```python
import xml.etree.ElementTree as ET

tree = ET.parse('file.xml')
root = tree.getroot()

elements = root.findall('tag')
```

xml.etree.ElementTree.Element.attrib: Возвращает атрибуты элемента в виде словаря.

```python
import xml.etree.ElementTree as ET

tree = ET.parse('file.xml')
root = tree.getroot()

for element in root:
    attributes = element.attrib
    print(attributes)
```

Помните, что без доступа к конкретному XML-файлу, точные примеры кода могут быть недоступны.
""",
                        "pythoncom": r"""
Библиотека "pythoncom" используется для взаимодействия с COM-объектами (Component Object Model) в Python.
Она предоставляет функциональность для создания, вызова и управления COM-объектами,
такими как приложения Windows, компоненты Office и другие COM-совместимые объекты.

Вот таблица методов модуля "pythoncom" и его подмодулей:

| Метод           | Описание                             |
|-----------------|--------------------------------------|
| CoInitialize    | Инициализирует библиотеку COM.        |
| CoUninitialize  | Завершает работу с библиотекой COM.    |
| CoCreateInstance| Создает экземпляр COM-объекта.        |
| PyCom_RegisterUnknownHandler | Регистрирует обработчик для неизвестных COM-объектов. |
| CLSIDToClassMap | Карта соответствия CLSID и классов COM. |
| IIDToInterfaceMap | Карта соответствия IID и интерфейсов COM. |

Некоторые из часто используемых методов библиотеки "pythoncom" включают:
CoInitialize(): Инициализирует библиотеку COM, обычно вызывается в начале программы.
CoCreateInstance(clsid, interface=None, context=None, flags=None):
Создает экземпляр COM-объекта с помощью указанного идентификатора класса (CLSID).
Возвращает интерфейс COM-объекта.
CoUninitialize(): Завершает работу с библиотекой COM, обычно вызывается в конце программы.

Пример кода демонстрирующий использование метода CoCreateInstance():

```python
import pythoncom

# Идентификатор класса для Excel
clsid = "{00024500-0000-0000-C000-000000000046}"

# Создание экземпляра объекта Excel 
excel = pythoncom.CoCreateInstance(clsid, None, None, pythoncom.CLSCTX_SERVER)

# Вывод версии Excel
print(excel.Version)
```

Обратите внимание, что код может варьироваться в зависимости от требуемых COM-объектов и их интерфейсов.
""",
                        "traitlets": r"""
Библиотека "traitlets" в Python используется для определения и использования
типизированных атрибутов (traits) и событий (events) в объектно-ориентированном программировании.
Она обеспечивает механизмы проверки типов, установки значений по умолчанию,
уведомлений об изменениях и другие функции, улучшающие модульность и гибкость кода.


Модуль: traitlets

Методы:
HasTraits(): Базовый класс, предоставляющий инфраструктуру для определения типизированных атрибутов и событий.
default(obj): Метод, возвращающий значение по умолчанию для указанного атрибута.
validate(obj, value): Метод, проверяющий значение атрибута на соответствие заданным условиям или типу.
observe(cls, handler, names=None): Метод класса, позволяющий связать обработчик события с указанными атрибутами.
link(target, name, linkname=None): Метод объекта, позволяющий установить
связь между атрибутами текущего объекта и атрибутами другого объекта.

Подмодуль: traitlets.config

Методы:
Configurable(): Базовый класс, предоставляющий функциональность для работы с конфигурационными файлами и параметрами.
load_config_file(filename): Метод, загружающий конфигурационный файл, указанный по имени.
Application: Класс, представляющий приложение, которое может быть настроено с помощью конфигурационных файлов.
Config: Класс, представляющий конфигурацию, содержащую набор параметров для настройки.


Самые часто используемые методы:
default(obj): Возвращает значение по умолчанию для указанного атрибута.

```python
value = default('attr_name')
```

validate(obj, value): Проверяет значение атрибута на соответствие заданным условиям или типу.

```python
is_valid = validate('attr_name', value)
```

observe(cls, handler, names=None): Связывает обработчик события с указанными атрибутами.

```python
observe('class_name', handler_func, ['attr_name1', 'attr_name2'])
```

link(target, name, linkname=None): Устанавливает связь между атрибутами
текущего объекта и атрибутами другого объекта.

```python
link(other_object, 'attr_name', 'linked_attr_name')
```
""",
                        "stat": r"""
Библиотека "stat" в Python используется для работы с информацией о файловой системе,
такой как атрибуты файла, права доступа и временные метки.

Методы модуля "stat" и его подмодулей:

stat.S_ISDIR(mode): Проверяет, является ли файл директорией.
stat.S_ISREG(mode): Проверяет, является ли файл обычным файлом.
stat.S_ISLNK(mode): Проверяет, является ли файл символической ссылкой.
stat.S_ISSOCK(mode): Проверяет, является ли файл сокетом.
stat.S_ISFIFO(mode): Проверяет, является ли файл каналом FIFO.
stat.S_ISBLK(mode): Проверяет, является ли файл блочным устройством.
stat.S_ISCHR(mode): Проверяет, является ли файл символьным устройством.
stat.S_IMODE(mode): Возвращает режим доступа к файлу.
stat.S_IFMT(mode): Возвращает тип файла и режим доступа.

Самые часто используемые методы:

stat.S_ISDIR(mode): Проверяет, является ли файл директорией.

```python
import os
import stat

file_path = 'path/to/file.txt'
file_stat = os.stat(file_path)
if stat.S_ISDIR(file_stat.st_mode):
    print("File is a directory")
else:
    print("File is not a directory")
```

stat.S_ISREG(mode): Проверяет, является ли файл обычным файлом.


```python
import os
import stat

file_path = 'path/to/file.txt'
file_stat = os.stat(file_path)
if stat.S_ISREG(file_stat.st_mode):
    print("File is a regular file")
else:
    print("File is not a regular file")
```

stat.S_IMODE(mode): Возвращает режим доступа к файлу.

```python
import os
import stat

file_path = 'path/to/file.txt'
file_stat = os.stat(file_path)
file_mode = stat.S_IMODE(file_stat.st_mode)
print("File mode:", file_mode)
```
""",
                        "heapq": r"""
Библиотека "heapq" в Python используется для работы с heapq, имплементации алгоритма
"heap queue" (очереди с приоритетами). Это набор функций для эффективной работы
с "heap" (кучей) - структурой данных, которая обеспечивает быстрый доступ к наименьшему (или наибольшему) элементу.

Вот некоторые методы и подмодули, доступные в библиотеке "heapq":
`heapify(iterable)`: Перестраивает итерируемый объект в кучу.
`heappush(heap, item)`: Добавляет элемент в кучу.
`heappop(heap)`: Извлекает и возвращает наименьший элемент из кучи.
`heappushpop(heap, item)`: Добавляет элемент в кучу и сразу возвращает наименьший элемент.
`heapreplace(heap, item)`: Заменяет наименьший элемент и возвращает его.

Наиболее часто используемые методы в "heapq" включают:
`heappush`: Добавляет элемент в кучу. `heapq.heappush(heap, item)`.
`heappop`: Извлекает и возвращает наименьший элемент из кучи. `smallest = heapq.heappop(heap)`.

Обратите внимание, что описание методов и примеры кода предоставлены в соответствии с
запросом, но использование библиотеки "heapq" может потребовать дополнительных деталей
и контекста в вашем конкретном случае.
""",
                        "spwd": r"""
Библиотека "spwd" в Python используется для доступа к информации о пользовательских учетных записях в системе UNIX.
Она предоставляет функции для получения доступа к файлу `/etc/shadow`,
который хранит зашифрованные пароли пользователей, а также другую информацию о пользователях.

Таблица методов модуля "spwd":

Метод                | Описание
---------------------|-------------------------
`spwd.getspnam(name)`| Возвращает информацию о пользователе по его имени в виде объекта `spwd.struct_spwd`.
`spwd.getspall()`    | Возвращает список всех пользователей в системе, каждый в виде объекта `spwd.struct_spwd`.
`spwd.struct_spwd`   | Объект, представляющий информацию о пользователе, содержащий следующие атрибуты:
`sp_nam`(имя пользователя), `sp_pwd`(зашифрованный пароль),
`sp_lstchg`(последнее изменение пароля), `sp_min`(минимальный срок действия пароля),
`sp_max`(максимальный срок действия пароля), `sp_warn`(предупреждение о необходимости изменения пароля),
`sp_inact`(срок неактивности до блокировки учетной записи),
`sp_expire`(дата истечения срока действия пароля), `sp_flag`(флаги учетной записи).

Список самых частых методов модуля "spwd" и их описания:

Метод                | Описание                                          | Пример кода
---------------------|---------------------------------------------------|------------------------
`spwd.getspnam(name)`| Возвращает информацию о пользователе по его имени. | ``user_info = spwd.getspnam('john')``
`spwd.getspall()`    | Возвращает список всех пользователей в системе.    | ``users = spwd.getspall()``

Примечание: Примеры кода не могут быть предоставлены для данной библиотеки, поскольку требуется доступ к системным файлам.
""",
                        "enum": r"""
Библиотека "enum" в Python используется для создания и использования перечислений,
которые представляют собой набор именованных значений.
Она облегчает работу с ограниченным набором значений, обеспечивая их типизацию и удобный доступ.

Методы модуля "enum" и его подмодулей:

Модуль "enum":
Enum: Базовый класс для создания перечислений.
auto: Декоратор, который автоматически присваивает значения перечисления.

Подмодуль "Enum":
name: Возвращает имя элемента перечисления.
value: Возвращает значение элемента перечисления.

Подмодуль "IntEnum":
IntEnum: Базовый класс для создания перечислений с целочисленными значениями.

Подмодуль "Flag":
Flag: Базовый класс для создания перечислений с битовыми флагами.
auto: Декоратор, который автоматически присваивает значения флагов.

Некоторые из самых часто используемых методов "enum" и их описание:

Enum.name: Возвращает имя элемента перечисления.
```python
from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

print(Color.RED.name)  # Выводит "RED"
```

Enum.value: Возвращает значение элемента перечисления.
```python
from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

print(Color.RED.value)  # Выводит 1
```

Flag: Базовый класс для создания перечислений с битовыми флагами.
```python
from enum import Flag, auto

class Permissions(Flag):
    READ = auto()
    WRITE = auto()
    EXECUTE = auto()

user_permissions = Permissions.READ | Permissions.WRITE
print(user_permissions)  # Выводит <Permissions.READ|WRITE: 3>
```
""",
                        "pstats": r"""
Библиотека "pstats" в Python используется для профилирования производительности программы.
Она предоставляет возможность анализировать данные о времени выполнения и вызовах функций,
что помогает оптимизировать код и улучшить его производительность.

Методы и подмодули библиотеки "pstats" включают:

"Stats" (статистика)
    - "add" - добавляет данные о времени выполнения и вызовах функций в статистику.
    - "print_stats" - выводит общую статистику по вызовам функций.
    - "sort_stats" - сортирует статистику по различным критериям.
    - "strip_dirs" - удаляет пути к файлам из статистики.
    - "calc_callees" - вычисляет информацию о вызываемых функциях.
    - "dump_stats" - сохраняет статистику в файл.

"Profile" (профиль)
"run" - запускает профилирование кода.
"runcall" - профилирует отдельный вызов функции.
"print_stats" - выводит статистику по профилированию.
"dump_stats" - сохраняет статистику в файл.

Некоторые из наиболее часто используемых методов "pstats" включают:

"print_stats()": Выводит основную статистику профилирования, включая время выполнения и количество вызовов функций.

Пример кода, демонстрирующего его использование:

```python
import pstats

# Создаем объект статистики
stats = pstats.Stats('profile_result')

# Выводим статистику на экран
stats.print_stats()
```

"sort_stats()": Сортирует статистику профилирования по выбранному критерию,
такому как время выполнения или количество вызовов функций.

Пример кода, демонстрирующего его использование:

```python
import pstats

# Создаем объект статистики
stats = pstats.Stats('profile_result')

# Сортируем статистику по времени выполнения
stats.sort_stats('time')

# Выводим отсортированную статистику на экран
stats.print_stats()

```
""",
                        "marshal": r"""
Библиотека "marshal" в Python используется для сериализации и десериализации объектов.
Она предоставляет функциональность для сохранения объектов в бинарном формате и восстановления их позже.

Методы модуля "marshal" и их краткое описание:
`dump(obj, file)` - Сериализует объект `obj` и записывает его в файл `file`.
`load(file)` - Читает сериализованные данные из файла `file` и восстанавливает объект.
`dumps(obj)` - Возвращает сериализованное представление объекта `obj` в виде строки.
`loads(bytes)` - Восстанавливает объект из сериализованного представления, передаваемого в виде строки `bytes`.
`version` - Целое число, представляющее версию протокола сериализации.

Наиболее распространенные методы "marshal" и их описание:

`dump(obj, file)` - Сериализует объект `obj` и записывает его в файл `file`.
```python
import marshal

data = {"name": "John", "age": 30}
with open("data.bin", "wb") as file:
    marshal.dump(data, file)
```

`load(file)` - Читает сериализованные данные из файла `file` и восстанавливает объект.
```python
import marshal

with open("data.bin", "rb") as file:
    data = marshal.load(file)
    print(data)  # Вывод: {"name": "John", "age": 30}
```

`dumps(obj)` - Возвращает сериализованное представление объекта `obj` в виде строки.
```python
import marshal

data = {"name": "John", "age": 30}
serialized = marshal.dumps(data)
print(serialized)
```

`loads(bytes)` - Восстанавливает объект из сериализованного представления, передаваемого в виде строки `bytes`.
```python
import marshal

serialized = (
    b'\x80\x04\x95\x0f\x00\x00\x00\x00\x00\x00\x8c\x08\x00\x00\x00Hello!'
    b'\x94\x8c\x01\x00\x00\x00x\x94\x8c\x01\x00\x00\x00y\x94\x2e\x94\x94'
    b'\x8c\x06\x00\x00\x00result\x94\x94\x8c\x05\x00\x00\x00float\x94\x93\x00\x00\x00\x00\x00\x00\x00.'
)

data = marshal.loads(serialized)
print(data)  # Вывод: {'Hello!': {'x': 'y', 'result': None, 'float': 0.0}}
```
""",
                        "linecache": r"""
Библиотека "linecache" в Python используется для чтения линий из файлов с исходным кодом.
Она предоставляет функции для извлечения строк из файла по их номеру.

Методы модуля "linecache" включают:
`getline(filename, lineno)`: Возвращает указанную строку из указанного файла.
`getlines(filename)`: Возвращает все строки из указанного файла в виде списка.
`clearcache()`: Очищает кэш, используемый для хранения строк файла.
   
   Примеры подмодулей отсутствуют.

Некоторые из самых часто используемых методов "linecache" включают:
Метод `getline(filename, lineno)` - возвращает указанную строку из указанного файла.

```python
import linecache

line = linecache.getline('file.txt', 5)
print(line)
```

Этот код выведет пятую строку из файла 'file.txt'.

Метод `getlines(filename)` - возвращает все строки из указанного файла в виде списка.

```python
import linecache

lines = linecache.getlines('file.txt')
for line in lines:
    print(line)
```

Этот код выведет все строки из файла 'file.txt' по одной строке на каждую итерацию цикла.

Метод `clearcache()` - очищает кэш, используемый для хранения строк файла.
Это может быть полезно, если файл изменился и требуется обновить строки в кэше.

```python
import linecache

# Изменения в файле 'file.txt'

linecache.clearcache()
line = linecache.getline('file.txt', 5)
print(line)
```

Этот код сначала очищает кэш, а затем возвращает пятую строку из обновленного файла 'file.txt'.

Примечание: Убедитесь, что файл 'file.txt' существует и содержит нужные строки.
""",
                        "sched": r"""
Библиотека "sched" в Python используется для планирования и управления задачами в программе.
Она позволяет создавать расписания выполнения задач и контролировать их выполнение в определенные моменты времени.

Методы модуля "sched" и его подмодулей:
sched.timefunc: Устанавливает функцию, которая будет использоваться для получения времени.
sched.delayfunc: Устанавливает функцию, вызываемую перед каждым циклом планировщика.
sched.enter(delay, priority, action, argument): Планирует выполнение задачи с заданным задержкой, приоритетом, действием и аргументом.
sched.enterabs(time, priority, action, argument): Планирует выполнение задачи в определенный момент времени с указанным приоритетом, действием и аргументом.
sched.cancel(event): Отменяет выполнение задачи, связанной с указанным событием.
sched.run(): Запускает планировщик и начинает выполнение задач.

Самые часто используемые методы библиотеки "sched" и их краткие описания:
enter(delay, priority, action, argument): Планирует выполнение задачи с заданной задержкой и приоритетом.

```python
import sched
import time

def print_message():
    print("Scheduled task executed.")

scheduler = sched.scheduler(time.time, time.sleep)
scheduler.enter(5, 1, print_message, ())
scheduler.run()
```

enterabs(time, priority, action, argument): Планирует выполнение задачи в определенный момент времени с указанным приоритетом.

```python
import sched
import time

def print_message():
    print("Scheduled task executed.")

scheduler = sched.scheduler(time.time, time.sleep)
scheduler.enterabs(time.time() + 10, 1, print_message, ())
scheduler.run()
```

cancel(event): Отменяет выполнение задачи, связанной с указанным событием.

```python
import sched
import time

def print_message():
    print("Scheduled task executed.")

scheduler = sched.scheduler(time.time, time.sleep)
event = scheduler.enter(5, 1, print_message, ())
scheduler.cancel(event)
scheduler.run()
```

Пожалуйста, помните об обеспечении безопасности при использовании этой библиотеки и выполнении задач в программе.
""",
                        "nntplib": r"""
Библиотека "nntplib" в Python используется для взаимодействия с серверами новостных групп (NNTP).
Она предоставляет функции и методы для чтения, отправки и управления сообщениями в новостных группах.

Вот таблица методов и их краткие описания для модуля "nntplib" и его подмодулей:

Метод                  | Описание
-----------------------|-------------------------------
nntplib.NNTP           | Класс для установки соединения с сервером NNTP.
NNTP.__init__()        | Инициализация объекта NNTP.
NNTP.quit()            | Отключение от сервера NNTP.
NNTP.group(group)      | Выбор новостной группы для чтения статей.
NNTP.list()            | Получение списка доступных новостных групп.
NNTP.article(num)      | Получение статьи по ее номеру.
NNTP.body(num)         | Получение тела статьи по ее номеру.
NNTP.head(num)         | Получение заголовка статьи по ее номеру.
NNTP.post(message)     | Отправка сообщения на сервер NNTP.
NNTP.search(criteria)  | Поиск статей, удовлетворяющих заданным критериям.

Вот список самых часто используемых методов в "nntplib" и их краткие описания:

NNTP.group(group): Выбирает новостную группу для чтения статей.
```python
from nntplib import NNTP

conn = NNTP('news.example.com')
conn.group('comp.lang.python')
```

NNTP.list(): Получает список доступных новостных групп.
```python
from nntplib import NNTP

conn = NNTP('news.example.com')
groups = conn.list()
```

NNTP.article(num): Получает статью по ее номеру.
```python
from nntplib import NNTP

conn = NNTP('news.example.com')
resp, article_lines, msg_id, info = conn.article('12345')
```

NNTP.post(message): Отправляет сообщение на сервер NNTP.
```python
from nntplib import NNTP

conn = NNTP('news.example.com')
resp = conn.post('<subject>', '<from>', '<body>')
```
""",
                        "certifi": r"""
Библиотека "certifi" в Python используется для работы с сертификатами в криптографии.
Она предоставляет набор корневых сертификатов, которые могут быть использованы
для проверки подлинности SSL-соединений при выполнении запросов HTTP.

Методы и подмодули "certifi":
Подмодуль "cacertifi": содержит корневые сертификаты, предназначенные для проверки SSL-соединений.
Функция `where()`: возвращает путь к файлу с набором корневых сертификатов.
Функция `contents()`: возвращает содержимое файла с корневыми сертификатами в виде строки.
Функция `old_where()`: возвращает путь к предыдущей версии файла с корневыми сертификатами.
Функция `old_contents()`: возвращает содержимое предыдущей версии файла с корневыми сертификатами.
Функция `contents_bytes()`: возвращает содержимое файла с корневыми сертификатами в виде байтовой строки.

Некоторые часто используемые методы "certifi":
Функция `where()`: возвращает путь к файлу с набором корневых сертификатов.

```python
import certifi

file_path = certifi.where()
print(file_path)
```

Функция `contents()`: возвращает содержимое файла с корневыми сертификатами в виде строки.

```python
import certifi

cert_contents = certifi.contents()
print(cert_contents)
```

Функция `old_where()`: возвращает путь к предыдущей версии файла с корневыми сертификатами.

```python
import certifi

old_file_path = certifi.old_where()
print(old_file_path)
```

Функция `old_contents()`: возвращает содержимое предыдущей версии файла с корневыми сертификатами.

```python
import certifi

old_cert_contents = certifi.old_contents()
print(old_cert_contents)
```

Функция `contents_bytes()`: возвращает содержимое файла с корневыми сертификатами в виде байтовой строки.

```python
import certifi

cert_bytes = certifi.contents_bytes()
print(cert_bytes)
```
""",
                        "rasutil": r"""
Библиотека "rasutil" (raspberry utility) используется для упрощения
разработки и взаимодействия с Raspberry Pi в языке программирования Python.

Таблица методов для модуля "rasutil":
Method 1: GPIOInit() - Инициализирует пины GPIO на Raspberry Pi.
Method 2: GPIOSet(pin, value) - Устанавливает значение пина GPIO на Raspberry Pi.
Method 3: GPIORead(pin) - Считывает значение с пина GPIO на Raspberry Pi.

Методы модуля "rasutil" позволяют управлять GPIO пинами на Raspberry Pi,
инициализировать их, устанавливать значения и считывать значения с этих пинов.

Список самых частых методов и их описания:
GPIOInit() - Инициализирует пины GPIO на Raspberry Pi.
```python
rasutil.GPIOInit()
```
Этот метод инициализирует пины GPIO на Raspberry Pi перед использованием.

GPIOSet(pin, value) - Устанавливает значение пина GPIO на Raspberry Pi.
```python
rasutil.GPIOSet(18, 1)
```
Этот метод устанавливает значение 1 на пине GPIO 18 на Raspberry Pi.

GPIORead(pin) - Считывает значение с пина GPIO на Raspberry Pi.
```python
value = rasutil.GPIORead(12)
```
Этот метод считывает значение с пина GPIO 12 на Raspberry Pi и сохраняет его в переменную "value".

Методы "GPIOSet" и "GPIORead" позволяют управлять значениями пинов GPIO на Raspberry Pi,
устанавливая значения и считывая их соответственно. Метод "GPIOInit" необходим для инициализации пинов GPIO перед их использованием.
""",
                        "grpc": r"""
Библиотека "grpc" в Python используется для реализации удаленного вызова процедур (RPC - Remote Procedure Call).
Это позволяет разработчикам создавать распределенные системы,
где клиентский код может вызывать функции на удаленном сервере, будто они находятся локально.

Методы и подмодули библиотеки "grpc":
grpc.insecure_channel(): Создает небезопасный канал связи для клиентского подключения к серверу.
grpc.secure_channel(): Создает безопасный канал связи (шифрованное соединение) для клиентского подключения к серверу.
grpc.Channel: Класс, представляющий канал связи между клиентом и сервером.
grpc.Server: Класс, представляющий сервер, который слушает входящие запросы и обрабатывает их с помощью определенных сервисов.
grpc.stub: Подмодуль, содержащий классы и функции для создания клиентских и серверных стабов (stub), облегчающих взаимодействие по RPC.
grpc.Service: Базовый класс для реализации пользовательских сервисов GRPC.
grpc.rpc_error: Подмодуль, содержащий классы исключений, связанных с ошибками RPC.

Некоторые часто используемые методы библиотеки "grpc":
grpc.insecure_channel(): Создает небезопасный канал связи с сервером. `channel = grpc.insecure_channel("localhost:50051")`
grpc.stub: Подмодуль, который предоставляет классы для создания клиентских и серверных стабов (stub) для удобного взаимодействия по RPC.
grpc.Server.add_insecure_port(): Определяет небезопасный порт, на котором сервер будет прослушивать входящие запросы. `server.add_insecure_port("[::]:50051")`
grpc.Server.start(): Запускает сервер, ожидающий входящих запросов. `server.start()`
grpc.Service: Базовый класс, который разработчики могут наследовать для создания пользовательских сервисов GRPC. `class MyService(grpc.Service):`
""",
                        "wheel": r"""
Библиотека "wheel" в Python используется для упрощения установки пакетов и их распространения.
Она представляет собой формат пакета, который содержит предварительно
скомпилированные бинарные файлы, что позволяет ускорить процесс установки.

### Методы модуля "wheel":
`convert`: используется для преобразования исходных файлов пакета в формат wheel.
`install`: позволяет установить пакет из wheel-файла.
`unpack`: распаковывает содержимое wheel-файла.
`pack`: упаковывает исходные файлы пакета в wheel-файл.
   
### Подмодули:
`metadata`: содержит методы для работы с метаданными пакета, такими как версия, автор и описание.
`tags`: предоставляет информацию о поддерживаемых платформах и интерпретаторах.
`signatures`: позволяет работать с подписями wheel-файлов.
`pep425tags`: предоставляет методы для работы с тегами PEP 425,
которые описывают совместимость пакетов с определенными версиями Python и операционных систем.


### convert
Преобразует исходные файлы пакета в формат wheel.

```python
from wheel import convert

convert.pack('path/to/source/package')
```

### install
Устанавливает пакет из wheel-файла.

```python
from wheel import install

install.install('path/to/wheel/file.whl')
```

### unpack
Распаковывает содержимое wheel-файла.

```python
from wheel import unpack

unpack.unpack('path/to/wheel/file.whl', 'path/to/destination')
```

### pack</h3>
Упаковывает исходные файлы пакета в wheel-файл.

```python
from wheel import pack

pack.pack('path/to/source/package', 'path/to/destination/file.whl')
```
""",
                        "pyparsing": r"""
Библиотека "pyparsing" используется для анализа и разбора текстовых данных в языке программирования Python.
Она предоставляет возможность создавать грамматики и правила для разбора сложных структур данных.

Методы модуля "pyparsing" и его подмодулей:

parseString(string) - Разбирает строку в соответствии с определенной грамматикой и возвращает структурированные данные.
Word(alphas) - Определяет грамматическое правило для разбора последовательности символов, состоящей только из букв.
nums - Подмодуль, содержащий грамматические правила для разбора числовых значений.
CaselessLiteral(string) - Определяет грамматическое правило для разбора нечувствительных к регистру строк.
QuotedString(quoteChar) - Определяет грамматическое правило для разбора строки, заключенной в кавычки.

Самые часто используемые методы "pyparsing" с их кратким описанием и примером кода:

parseString(string): Разбирает строку в соответствии с грамматикой и возвращает структурированные данные.

```python
from pyparsing import Word, alphas, nums

data = "Hello World"
result = Word(alphas).parseString(data)
print(result)  # ['Hello']
```

Word(alphas): Определяет грамматическое правило для разбора последовательности символов, состоящей только из букв.

```python
from pyparsing import Word, alphas

data = "Hello123"
result = Word(alphas).parseString(data)
print(result)  # ['Hello']
```

QuotedString(quoteChar): Определяет грамматическое правило для разбора строки, заключенной в кавычки.

```python
from pyparsing import QuotedString

data = '"Hello World"'
result = QuotedString('"').parseString(data)
print(result)  # ['Hello World']
```
""",
                        "faulthandler": r"""
Библиотека "faulthandler" используется для обнаружения и отладки ошибок, связанных с сбоями в программе на языке Python.

Методы и подмодули библиотеки "faulthandler":

faulthandler.enable(): Активирует обработчик сбоев для записи информации о сбое.
faulthandler.disable(): Отключает обработчик сбоев.
faulthandler.is_enabled(): Проверяет, активирован ли обработчик сбоев.
faulthandler.dump_traceback(file=sys.stderr, all_threads=True): Записывает трассировку стека сбоя в указанный файл.
faulthandler.register(signal=SIGUSR1, all_threads=True, chain=True): Регистрирует обработчик сбоев для указанного сигнала.
faulthandler.cancel_dump_traceback(): Прекращает запись трассировки стека сбоя.
faulthandler.cancel_register(): Отменяет регистрацию обработчика сбоев для указанного сигнала.

Наиболее часто используемые методы "faulthandler":

faulthandler.enable(): Активирует обработчик сбоев для записи информации о сбое.

```python
import faulthandler
faulthandler.enable()
```

faulthandler.disable(): Отключает обработчик сбоев.

```python
import faulthandler
faulthandler.disable()
```

faulthandler.dump_traceback(file=sys.stderr, all_threads=True): Записывает трассировку стека сбоя в указанный файл.

```python
import faulthandler
faulthandler.dump_traceback(file=open('traceback.txt', 'w'), all_threads=True)
```

Эти методы помогут вам обнаружить и отладить ошибки связанные с сбоями в вашей программе
на языке Python,путем получения информации о трассировке стека сбоя.
""",
                        "traceback": r"""
Библиотека "traceback" используется в Python для отображения трассировки стека, то есть печати
информации об исключении и последующих вызовах функций, которые привели к возникновению исключения.
Она помогает в отладке и идентификации причин возникновения ошибок в программе.

Методы и подмодули библиотеки "traceback" включают:
`traceback.print_tb(tb, limit=None, file=None)` - выводит трассировку стека в заданный файл (по умолчанию в sys.stdout) в виде списка строк.
`traceback.print_exception(etype, value, tb, limit=None, file=None)` - выводит полную информацию об исключении, включая тип и значение исключения, трассировку стека и подробности.
`traceback.print_exc(limit=None, file=None, chain=True)` - выводит трассировку стека последнего возникшего исключения.
`traceback.format_tb(tb, limit=None)` - возвращает трассировку стека в виде списка строк.
`traceback.format_exception(etype, value, tb, limit=None)` - возвращает полную информацию об исключении в виде списка строк.
`traceback.format_exc(limit=None, chain=True)` - возвращает трассировку стека последнего возникшего исключения в виде строки.

Некоторые из наиболее часто используемых методов в библиотеке "traceback" включают:
Метод `print_tb()` используется для вывода трассировки стека в стандартном выводе.

```python
import traceback

try:
    # некоторый код, в котором может произойти исключение
    x = 1 / 0
except:
    traceback.print_tb(sys.exc_info()[2])
```

Метод `print_exception()` используется для вывода полной информации об исключении, включая тип, значение и трассировку стека.

```python
import traceback

try:
    # некоторый код, в котором может произойти исключение
    x = 1 / 0
except:
    traceback.print_exception(*sys.exc_info())
```

Метод `format_exc()` используется для получения трассировки стека последнего возникшего исключения в виде строки.

```python
import traceback

try:
    # некоторый код, в котором может произойти исключение
    x = 1 / 0
except:
    error_traceback = traceback.format_exc()
    print(error_traceback)
```

Помните, что без дополнительного контекста исключения и вашего кода, приведенные примеры могут не работать напрямую.
Не забывайте адаптировать их под свои потребности и проверять документацию для более подробной информации о библиотеке "traceback".
""",
                        "runpy": r"""
Библиотека "runpy" в Python используется для выполнения модулей как скриптов, а также для загрузки и выполнения кода из файлов или строк.
Методы модуля "runpy" и его подмодулей:

Метод | Описание
----- | --------
run_path(path, \[globals=None, locals=None\]) | Загружает и выполняет код из указанного файла по заданному пути.
run_module(mod_name, \[init_globals=None, run_name=None, alter_sys=False\]) | Загружает и выполняет указанный модуль.
run_module(mod_name, \[init_globals=None, run_name=None, alter_sys=False\]) | Загружает и выполняет указанный модуль.
run_module(mod_name, \[init_globals=None, run_name=None, alter_sys=False\]) | Загружает и выполняет указанный модуль.
run_module(mod_name, \[init_globals=None, run_name=None, alter_sys=False\]) | Загружает и выполняет указанный модуль.
run_module(mod_name, \[init_globals=None, run_name=None, alter_sys=False\]) | Загружает и выполняет указанный модуль.
run_module(mod_name, \[init_globals=None, run_name=None, alter_sys=False\]) | Загружает и выполняет указанный модуль.
run_module(mod_name, \[init_globals=None, run_name=None, alter_sys=False\]) | Загружает и выполняет указанный модуль.
run_module(mod_name, \[init_globals=None, run_name=None, alter_sys=False\]) | Загружает и выполняет указанный модуль.
run_module(mod_name, \[init_globals=None, run_name=None, alter_sys=False\]) | Загружает и выполняет указанный модуль.

Самые часто используемые методы:

Метод | Описание | Пример кода
----- | -------- | -----------
run_path(path, \[globals=None, locals=None\]) | Загружает и выполняет код из указанного файла по заданному пути. | run_path('script.py')
run_module(mod_name, \[init_globals=None, run_name=None, alter_sys=False\]) | Загружает и выполняет указанный модуль. | run_module('module_name')
""",
                        "zlib": r"""
Библиотека "zlib" используется в Python для сжатия и распаковки данных с использованием алгоритма сжатия Deflate.

Методы модуля "zlib" и его подмодулей:

Модуль "zlib":
compress(data, level=-1): Сжимает данные с использованием алгоритма Deflate.
decompress(data, wbits=MAX_WBITS, bufsize=DEF_BUF_SIZE): Распаковывает сжатые данные.
crc32(data, value=0): Вычисляет контрольную сумму CRC-32 для данных.

Подмодуль "zlib.compressobj":
__init__(level=-1, method=DEFLATED, wbits=MAX_WBITS, memLevel=DEF_MEM_LEVEL, strategy=Z_DEFAULT_STRATEGY): Создает объект для сжатия данных.
compress(data): Сжимает данные и возвращает сжатый буфер.
flush(mode): Завершает сжатие и возвращает оставшийся сжатый буфер.

Подмодуль "zlib.decompressobj":
__init__(wbits=MAX_WBITS): Создает объект для распаковки данных.
decompress(data, max_length=0): Распаковывает данные и возвращает распакованный буфер.
flush(mode): Завершает распаковку и возвращает оставшийся распакованный буфер.

Самые часто используемые методы:

compress(data, level=-1): Сжимает данные с использованием алгоритма Deflate.

```python
import zlib
compressed_data = zlib.compress(b"Hello, world!")
```

decompress(data, wbits=MAX_WBITS, bufsize=DEF_BUF_SIZE): Распаковывает сжатые данные.

```python
import zlib
decompressed_data = zlib.decompress(compressed_data)
```

crc32(data, value=0): Вычисляет контрольную сумму CRC-32 для данных.
```python
import zlib
checksum = zlib.crc32(b"Hello, world!")
```

Пожалуйста, обратите внимание, что код предоставлен только для демонстрации работы методов и может потребоваться
дополнительная обработка данных в реальных сценариях использования.
""",
                        "packaging": r"""
Библиотека "packaging" в Python используется для работы с упаковкой и распаковкой пакетов, а также для управления метаданными пакетов.
Она предоставляет функции для создания, проверки, обновления и распаковки пакетов в формате wheel или в формате сжатого архива.

Методы модуля "packaging" и его подмодулей:

Модуль packaging.version:
parse(version_string): Парсит версию из строки и возвращает объект Version.
Version: Класс для представления версии пакета.

Модуль packaging.specifiers:
Specifier: Класс для представления спецификации версии пакета.
LegacySpecifier: Класс для представления устаревшей спецификации версии пакета.
SpecifierSet: Класс для представления набора спецификаций версий пакета.

Модуль packaging.requirements:
Requirement: Класс для представления требования к пакету.

Модуль packaging.markers:
Marker: Класс для представления условий маркера.
default_environment: Возвращает стандартное окружение.

Модуль packaging.tags:
Tag: Класс для представления метки платформы.
sys_tags(): Возвращает метки платформы для текущей системы.

Наиболее часто используемые методы в библиотеке "packaging":

parse(version_string): Парсит версию из строки и возвращает объект Version.

```python
from packaging import version

version_string = '1.2.3'
parsed_version = version.parse(version_string)
print(parsed_version)
```

SpecifierSet(specifier_string): Создает набор спецификаций версий на основе строки.

```python
from packaging.specifiers import SpecifierSet

specifier_string = '>=1.0,<=2.0'
specifier_set = SpecifierSet(specifier_string)
print(specifier_set)
```

Requirement(requirement_string): Создает требование к пакету на основе строки.

```python
from packaging.requirements import Requirement

requirement_string = 'numpy>=1.0'
requirement = Requirement(requirement_string)
print(requirement)
```

Убедитесь, что у вас установлена библиотека "packaging" перед использованием этих методов.
""",
                        "nis": r"""
Библиотека "nis" в Python используется для работы с сервисом Network Information Service (NIS).
NIS предоставляет распределенную базу данных, которая используется для хранения информации о пользователях,
группах и других системных ресурсах в сети.

Методы модуля "nis":
nis.match(mapname, key): Возвращает значение, связанное с указанным ключом в указанной базе данных.
nis.cat(mapname): Возвращает все записи из указанной базы данных.
nis.maps(): Возвращает список доступных баз данных.
nis.getmapbyname(name): Возвращает содержимое базы данных с указанным именем.
nis.getmapbynumber(number): Возвращает содержимое базы данных с указанным номером.

Некоторые из самых часто используемых методов "nis" включают:
match(mapname, key): Возвращает значение, связанное с указанным ключом в указанной базе данных.

```python
import nis

value = nis.match("passwd", "john")
print(value)
```

cat(mapname): Возвращает все записи из указанной базы данных.

```python
import nis

records = nis.cat("passwd")
for record in records:
    print(record)
```

maps(): Возвращает список доступных баз данных.

```python
import nis

map_list = nis.maps()
print(map_list)
```

Это лишь некоторые из методов, доступных в библиотеке "nis".
""",
                        "zipapp": r"""
Библиотека "zipapp" в Python используется для упаковки и запуска приложений в формате ZIP.
Это позволяет создавать самодостаточные исполняемые файлы, которые можно легко передавать и развертывать.

Методы модуля "zipapp" и его подмодулей:

zipapp.create_archive(target, interpreter=None, main=None, *additional_files):
Создает ZIP-архив на основе указанных файлов и опционально добавляет интерпретатор и точку входа в приложение.

zipapp.get_interpreter(path):
Возвращает путь к интерпретатору Python, используемому для запуска приложения.

zipapp.get_metadata(entry):
Возвращает метаданные (метатеги) для указанной записи в ZIP-архиве.

zipapp.get_asset_name(entry):
Возвращает имя актива (файла) для указанной записи в ZIP-архиве.

zipapp.get_zip_uri(archive_path):
Возвращает URI для доступа к ZIP-архиву.

Некоторые из самых часто используемых методов:

create_archive: Создает ZIP-архив с указанными файлами.

```python
import zipapp

zipapp.create_archive("myapp.zip", interpreter="/usr/bin/python3", main="main.py", "additional_file1.txt", "additional_file2.dat")
```

get_interpreter: Возвращает путь к интерпретатору Python, используемому для запуска приложения.

```python
import zipapp

interpreter_path = zipapp.get_interpreter("myapp.zip")
print(f"Интерпретатор: {interpreter_path}")
```

get_metadata: Возвращает метаданные (метатеги) для указанной записи в ZIP-архиве.

```python
import zipapp

metadata = zipapp.get_metadata("myapp.zip/main.py")
print(f"Метаданные: {metadata}")
```

get_asset_name: Возвращает имя актива (файла) для указанной записи в ZIP-архиве.

```python
import zipapp

asset_name = zipapp.get_asset_name("myapp.zip/main.py")
print(f"Имя актива: {asset_name}")
```

Пожалуйста, обратите внимание, что приведенные примеры являются общими и могут потребоваться дополнительные настройки
в зависимости от вашего конкретного случая использования.
""",
                        "notebook": r"""
Библиотека "notebook" используется для создания интерактивных блокнотов в среде Jupyter Notebook.
Она предоставляет возможность комбинировать код, текст, графики и другие элементы в одном документе,
что делает его удобным инструментом для исследования данных, прототипирования и обучения.

Методы модуля "notebook" и его подмодулей:

Модуль "notebook":
`list_notebooks()`: возвращает список всех блокнотов в текущем рабочем каталоге.
`open_notebook(path)`: открывает блокнот по указанному пути.
`create_notebook()`: создает новый блокнот.
`save_notebook(path)`: сохраняет текущий блокнот по указанному пути.
`export_notebook(path, format)`: экспортирует блокнот в указанный формат (например, HTML, PDF).

Подмодуль "cells":
`list_cells()`: возвращает список всех ячеек в текущем блокноте.
`add_code_cell()`: добавляет новую ячейку с кодом.
`add_markdown_cell()`: добавляет новую ячейку с текстом в формате Markdown.
`delete_cell(index)`: удаляет ячейку по указанному индексу.

Самые часто используемые методы:

`list_notebooks()`: возвращает список всех блокнотов в текущем рабочем каталоге.

```python
from notebook import list_notebooks

notebooks = list_notebooks()
print(notebooks)
```

`open_notebook(path)`: открывает блокнот по указанному пути.

```python
from notebook import open_notebook

notebook = open_notebook('path/to/notebook.ipynb')
print(notebook)
```

`create_notebook()`: создает новый блокнот.

```python
from notebook import create_notebook

notebook = create_notebook()
print(notebook)
```

`save_notebook(path)`: сохраняет текущий блокнот по указанному пути.

```python
from notebook import save_notebook

save_notebook('path/to/save.ipynb')
```

`list_cells()`: возвращает список всех ячеек в текущем блокноте.

```python
from notebook.cells import list_cells

cells = list_cells()
print(cells)
```

`add_code_cell()`: добавляет новую ячейку с кодом.

```python
from notebook.cells import add_code_cell

cell = add_code_cell()
print(cell)
```

`add_markdown_cell()`: добавляет новую ячейку с текстом в формате Markdown.

```python
from notebook.cells import add_markdown_cell

cell = add_markdown_cell()
print(cell)
```

`delete_cell(index)`: удаляет ячейку по указанному индексу.

```python
from notebook.cells import delete_cell

delete_cell(0)
```
""",
                        "xdrlib": r"""
Библиотека "xdrlib" в Python используется для работы с кодированием и декодированием данных в формате XDR (eXternal Data Representation).
XDR является стандартом для представления данных, независимым от платформы, и часто используется для обмена данными между различными системами.

Методы модуля "xdrlib" и его подмодулей:

Модуль "xdrlib":
pack_fstring(format_string, *args): Упаковывает аргументы в соответствии с заданным форматным строкой и возвращает упакованные данные в формате XDR.
unpack_fstring(format_string, packed_data): Распаковывает данные в формате XDR, используя заданную форматную строку, и возвращает распакованные значения.

Наиболее часто используемые методы:

pack_uint(value): Упаковывает беззнаковое целое число (unsigned int) в формате XDR.

```python
import xdrlib

packer = xdrlib.Packer()
packed_data = packer.pack_uint(42)
print(packed_data)
```

unpack_uint(packed_data): Распаковывает беззнаковое целое число (unsigned int) из данных в формате XDR и возвращает его значение.

```python
import xdrlib

packed_data = b'\x00\x00\x00\x2a'
unpacker = xdrlib.Unpacker(packed_data)
unpacked_value = unpacker.unpack_uint()
print(unpacked_value)
```

pack_string(value): Упаковывает строку в формате XDR.

```python
import xdrlib

packer = xdrlib.Packer()
packed_data = packer.pack_string("Hello, World!")
print(packed_data)
```

unpack_string(packed_data): Распаковывает строку из данных в формате XDR и возвращает ее значение.

```python
import xdrlib

packed_data = b'\x00\x00\x00\x0cHello, World!'
unpacker = xdrlib.Unpacker(packed_data)
unpacked_value = unpacker.unpack_string()
print(unpacked_value)
```

Пожалуйста, обратите внимание, что это только некоторые примеры методов библиотеки "xdrlib".
Для полного списка методов и их подробного описания рекомендуется обратиться к официальной документации Python.
""",
                        "string": r"""
Библиотека "string" в Python предоставляет набор методов для работы со строками.
Она обеспечивает функциональность для манипуляции и обработки текстовых данных.

Название метода           | Описание
   --------------------------|---------------------------------------------------------------
   `string.ascii_letters`     | Содержит все буквы алфавита в верхнем и нижнем регистрах.
   `string.ascii_lowercase`  | Содержит все буквы алфавита в нижнем регистре.
   `string.ascii_uppercase`  | Содержит все буквы алфавита в верхнем регистре.
   `string.digits`            | Содержит все цифры от 0 до 9.
   `string.hexdigits`         | Содержит все шестнадцатеричные цифры (от 0 до 9 и от A до F).
   `string.octdigits`         | Содержит все восьмеричные цифры (от 0 до 7).
   `string.punctuation`       | Содержит символы пунктуации.
   `string.printable`         | Содержит все печатные символы (буквы, цифры, символы пунктуации и пробельные символы).
   `string.whitespace`        | Содержит пробельные символы (пробел, табуляция, новая строка и т.д.).
 

`string.ascii_letters`: Возвращает все буквы алфавита в верхнем и нижнем регистрах.

```python
import string
print(string.ascii_letters)
```
`string.digits`: Возвращает все цифры от 0 до 9.

```python
import string
print(string.digits)
```
`string.punctuation`: Возвращает символы пунктуации.

```python
import string
print(string.punctuation)
```
""",
                        "multiprocessing": r"""
Библиотека "multiprocessing" используется в Python для поддержки параллельного выполнения кода, основанного на процессах.
Она предоставляет возможность создания и управления процессами, а также обмена данными между ними.

Методы модуля "multiprocessing" и его подмодулей:

`Process`: Класс для создания и управления процессов. Может быть использован для запуска функций или методов в отдельных процессах.
`Pool`: Класс для параллельного выполнения функций на нескольких процессах. Позволяет создавать пул процессов, управлять ими и получать результаты выполнения.
`Queue`: Класс для обмена данными между процессами. Поддерживает безопасную передачу объектов через очередь.
`Lock`: Класс для создания и использования блокировок (locks) в многопроцессорных программах. Обеспечивает синхронизацию доступа к ресурсам между процессами.
`Value` и `Array`: Классы для создания и использования разделяемых объектов синхронизации и обмена данными между процессами.
`Manager`: Класс для создания сервера процесса и разделенных объектов, доступных для различных процессов.

`Process()`: Создает объект процесса, принимает функцию или метод в качестве аргумента для выполнения в отдельном процессе.

```python
from multiprocessing import Process

def my_function():
    print("Hello from another process!")

if __name__ == "__main__":
    p = Process(target=my_function)
    p.start()
    p.join()
```

`Pool()`: Создает пул процессов и выполняет функцию для каждого элемента заданного массива аргументов.

```python
from multiprocessing import Pool

def square(x):
    return x ** 2

if __name__ == "__main__":
    with Pool(processes=3) as pool:
        result = pool.map(square, [1, 2, 3, 4, 5])
        print(result)
```

`Queue()`: Создает очередь для обмена данными между процессами. Позволяет безопасно добавлять и извлекать элементы.

```python
from multiprocessing import Process, Queue

def worker(queue):
    item = queue.get()
    print("Processed:", item)

if __name__ == "__main__":
    q = Queue()
    p = Process(target=worker, args=(q,))
    p.start()
    q.put("Data")
    p.join()
```

Обратите внимание, что предоставленный код является кратким примером и может потребоваться дополнительная логика в реальных сценариях использования.
""",
                        "formatter": r"""
Библиотека "formatter" в Python используется для форматирования и стилизации
текста в различных вариантах вывода, таких как консоль, файлы, строки и другие.
2.
Методы модуля "formatter":
format_text(): Форматирует указанный текст в соответствии с заданными параметрами.
stylize_text(): Применяет стилизацию к тексту, используя заданные форматы и цвета.
capitalize_text(): Преобразует первую букву каждого слова в тексте в верхний регистр.
align_text(): Выравнивает текст по заданному формату выравнивания (левому, правому или по центру).
truncate_text(): Обрезает текст до указанной длины и добавляет многоточие в конце, если текст был обрезан.

Подмодули "formatter":
html_format: Включает методы для форматирования текста в формате HTML.
csv_format: Содержит методы для форматирования текста в формате CSV.
json_format: Включает методы для форматирования текста в формате JSON.
xml_format: Содержит методы для форматирования текста в формате XML.
pdf_format: Включает методы для форматирования текста в формате PDF.

Самые часто используемые методы:
format_text(text, format): Форматирует указанный текст с использованием заданного формата.

formatted_text = formatter.format_text("Привет, мир!", "жирный")
print(formatted_text)  # Выводит текст "Привет, мир!" в жирном формате.

stylize_text(text, style): Применяет заданный стиль к указанному тексту.

stylized_text = formatter.stylize_text("Привет, мир!", "красный")
print(stylized_text)  # Выводит текст "Привет, мир!" в красном цвете.

align_text(text, alignment): Выравнивает указанный текст по заданному формату выравнивания.

aligned_text = formatter.align_text("Привет, мир!", "правый")
print(aligned_text)  # Выводит текст "Привет, мир!" справа выровненным.

Обратите внимание, что код представлен в качестве примера и может потребоваться дополнительная настройка и параметры для достижения желаемого результата.
""",
                        "jsonschema": r"""
Библиотека "jsonschema" используется для валидации данных в формате JSON по схеме.
Она позволяет проверить, соответствуют ли данные определенным правилам и структуре, заданным в JSON-схеме.

Таблица методов модуля "jsonschema" и их краткое описание:

   Метод          | Описание
   -------------- | --------------------------------------------
   validate       | Проверяет, соответствуют ли данные схеме.
   Draft4Validator | Класс, осуществляющий валидацию на основе JSON-схемы в соответствии с разделом 4 стандарта.
   Draft6Validator | Класс, осуществляющий валидацию на основе JSON-схемы в соответствии с разделом 6 стандарта.
   Draft7Validator | Класс, осуществляющий валидацию на основе JSON-схемы в соответствии с разделом 7 стандарта.
   ValidationError | Класс исключения, возникающего при невалидных данных.
   exceptions     | Подмодуль, содержащий различные классы исключений.

Список самых часто используемых методов "jsonschema" и их краткое описание:

`validate(schema, instance)` - Проверяет, соответствуют ли данные `instance` схеме `schema`.
Возвращает `None`, если данные валидны. В противном случае, возникает исключение `ValidationError`.
   
```python
from jsonschema import validate

schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "age": {"type": "integer"}
    }
}

data = {
    "name": "John",
    "age": 25
}

try:
    validate(schema, data)
    print("Data is valid.")
except ValidationError as e:
    print("Data is invalid:", e)
```

`Draft4Validator(schema)` - Создает экземпляр валидатора на основе JSON-схемы с использованием стандарта Draft 4.
Используется для последующей валидации данных.

```python
from jsonschema import Draft4Validator

schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "age": {"type": "integer"}
    }
}

validator = Draft4Validator(schema)

data = {
    "name": "John",
    "age": 25
}

for error in validator.iter_errors(data):
    print("Validation error:", error.message)
```
""",
                        "mailbox": r"""
Библиотека "mailbox" в Python используется для работы с почтовыми ящиками.
Она позволяет читать и записывать электронные письма в различных форматах, таких как mbox, MMDF, babyl и др.

Таблица методов библиотеки "mailbox":

| Метод               | Краткое описание                                      |
|---------------------|-------------------------------------------------------|
| mailbox.mbox        | Позволяет работать с форматом mbox.                    |
| mailbox.Maildir     | Предоставляет доступ к Maildir-формату почтового ящика. |
| mailbox.Babyl       | Обеспечивает работу с форматом babyl.                   |
| mailbox.MMDF        | Позволяет чтение и запись писем в формате MMDF.         |
| mailbox.Mailbox     | Предоставляет общий интерфейс для работы с почтовыми ящиками в разных форматах.  |
| mailbox.MaildirMessage  | Представляет отдельное письмо в формате Maildir. |
| mailbox.MH          | Работа с письмами в формате MH.                         |

Самые часто используемые методы библиотеки "mailbox":

`add` - добавляет письмо в почтовый ящик.

```python
with mailbox.mbox('sample.mbox') as mbox:
    message = EmailMessage()
    message['Subject'] = 'Hello'
    message.set_content('This is a test email')
    mbox.add(message)
```

`iterkeys` - возвращает итератор для ключей (идентификаторов) писем в почтовом ящике.


```python
with mailbox.mbox('sample.mbox') as mbox:
    for key in mbox.iterkeys():
        print(key)
```

`get_message` - возвращает письмо по ключу (идентификатору).

```python
with mailbox.mbox('sample.mbox') as mbox:
    message = mbox.get_message('12345')
    print(message['Subject'])
```

`remove` - удаляет письмо по ключу (идентификатору).

```python
with mailbox.mbox('sample.mbox') as mbox:
    mbox.remove('12345')
```
""",
                        "reprlib": r"""
Библиотека "reprlib" используется для создания ограниченных представлений (сокращений) объектов в строковом виде.
Она предоставляет функциональность для генерации усеченных строковых представлений сложных объектов, таких как контейнеры,
чтобы они были более читаемыми и компактными.

Методы модуля "reprlib" и его подмодулей:

   Метод | Описание
   ------------ | -------------
   reprlib.repr() | Возвращает сокращенное строковое представление объекта с ограничением символов.
   reprlib.aRepr() | Возвращает сокращенное представление объекта, указывая максимальное количество символов и добавляя многоточие в конце при необходимости.
   reprlib.recursive_repr() | Декоратор функции, который позволяет модифицировать стандартный метод `__repr__` для обработки рекурсивных вызовов.
   reprlib.dllist() | Класс-контейнер, предоставляющий сокращенное строковое представление для двусвязного списка.
   reprlib.Repr() | Класс, используемый для изменения поведения библиотеки "reprlib" путем настройки различных параметров.

Список самых часто используемых методов, их описание и

   Метод | Описание | Пример кода
   ------------ | ------------- | -------------
   reprlib.repr() | Возвращает ограниченное строковое представление объекта | obj = [1, 2, 3, 4, 5]; print(reprlib.repr(obj))
   reprlib.aRepr() | Возвращает сокращенное представление объекта с максимальным количеством символов и многоточием | obj = "This is a long string"; print(reprlib.aRepr(obj, 10))
   reprlib.recursive_repr() | Декоратор для изменения поведения метода `__repr__` для обработки рекурсивных вызовов | @reprlib.recursive_repr(); def __repr__(self): return 'MyClass()'
   reprlib.dllist() | Класс-контейнер для двусвязного списка с ограниченным строковым представлением | dll = reprlib.dllist([1, 2, 3]); print(dll)
   reprlib.Repr() | Класс для настройки поведения библиотеки "reprlib" | r = reprlib.Repr(); r.maxstring = 20; obj = "This is a long string"; print(r.repr(obj))

""",
                        "getpass": r"""
Библиотека "getpass" в Python используется для безопасного ввода паролей и других конфиденциальных
данных пользователем в командной строке или интерактивной среде.

Методы модуля "getpass" и его подмодулей:

Метод | Описание
----- | --------
getpass.getpass(prompt='Password: ', stream=None) | Запрашивает у пользователя ввод пароля с подсказкой "Password: ". Возвращает введенный пароль в виде строки.
getpass.getuser() | Возвращает имя текущего пользователя операционной системы.
getpass.getpass(prompt='Password: ', stream=None, fg=None, bg=None) | Запрашивает у пользователя ввод пароля с подсказкой "Password: ". Можно настроить цвет текста и фона подсказки.
getpass.getpass(prompt='Password: ', stream=None, echo=True, mask=None) | Запрашивает у пользователя ввод пароля с подсказкой "Password: ". Можно настроить отображение введенных символов (эхо) и символа-маскировки.

Самые часто используемые методы:

Метод | Описание | Пример кода
----- | -------- | -----------
getpass.getpass(prompt='Password: ', stream=None) | Запрашивает у пользователя ввод пароля с подсказкой "Password: ". Возвращает введенный пароль в виде строки. | ```<br>password = getpass.getpass(prompt='Enter your password: ')```
getpass.getuser() | Возвращает имя текущего пользователя операционной системы. | ```<br>username = getpass.getuser()```
""",
                        "pymsgbox": r"""
Библиотека "pymsgbox" используется для создания простых диалоговых окон с сообщениями, предупреждениями и запросами пользователю в Python.

Таблица методов модуля "pymsgbox" и их краткое описание:
`alert`: Отображает диалоговое окно с сообщением для пользователя.
`confirm`: Отображает диалоговое окно с вопросом для пользователя с двумя вариантами ответа (Да/Нет).
`prompt`: Отображает диалоговое окно с запросом пользователю на ввод текста.
`password`: Отображает диалоговое окно с запросом пользователю на ввод пароля (текста, скрытого звездочками).
`textbox`: Отображает диалоговое окно с возможностью ввода и редактирования текста пользователем.

Список самых частых методов "pymsgbox", их краткое описание и примерный код для демонстрации:

`alert(message, title=''):`
Описание: Отображает диалоговое окно с сообщением для пользователя.

```python
import pymsgbox

pymsgbox.alert('Привет, пользователь!', 'Информация')
```

`confirm(text, title='', buttons=['Да', 'Нет']):`
Описание: Отображает диалоговое окно с вопросом для пользователя с двумя вариантами ответа.

```python
import pymsgbox

response = pymsgbox.confirm('Вы уверены, что хотите продолжить?', 'Подтверждение')
if response == 'Да':
    # Действия при выборе "Да"
    pass
else:
    # Действия при выборе "Нет"
    pass
```

`prompt(text, title='', default=''):`
Описание: Отображает диалоговое окно с запросом пользователю на ввод текста.

```python
import pymsgbox

username = pymsgbox.prompt('Введите ваше имя:', 'Ввод данных')
```

`password(text, title=''):`
Описание: Отображает диалоговое окно с запросом пользователю на ввод пароля (скрытого звездочками).

```python
import pymsgbox

password = pymsgbox.password('Введите пароль:', 'Подтверждение')
```

`textbox(text='', title='', default='', multiline=False):`
Описание: Отображает диалоговое окно с возможностью ввода и редактирования текста пользователем.

```python
import pymsgbox

text = pymsgbox.textbox('Введите текст:', 'Редактирование текста')
```
""",
                        "quopri": r"""
Библиотека "quopri" в Python используется для кодирования и декодирования данных в формате Quoted-Printable.
Quoted-Printable - это способ представления непечатных или специальных символов в текстовом формате,
который используется в электронной почте и других приложениях.

Методы и подмодули библиотеки "quopri":

`quopri.encode(input, output, quotetabs=False)` - кодирует входные данные в формат Quoted-Printable и записывает результат в выходной поток.
`quopri.decode(input, output, headers=False)` - декодирует входные данные из формата Quoted-Printable и записывает результат в выходной поток.
`quopri.quote(data)` - возвращает строку, в которой данные закодированы в формате Quoted-Printable.
`quopri.unquote(data)` - возвращает строку, в которой данные декодированы из формата Quoted-Printable.
`quopri.encodestring(s)` - кодирует строку в формат Quoted-Printable и возвращает результат как строку.
`quopri.decodestring(s)` - декодирует строку из формата Quoted-Printable и возвращает результат как строку.

Самые часто используемые методы:

`quopri.encode(input, output, quotetabs=False)` - метод для кодирования данных в формат Quoted-Printable.
Можно использовать для безопасной передачи данных по электронной почте или другим каналам связи.

```python
import quopri

input_data = b"Hello, world!"
encoded_data = quopri.encode(input_data)
print(encoded_data)
```
   
`quopri.decode(input, output, headers=False)` - метод для декодирования данных из формата Quoted-Printable.
Полезно при работе с данными, полученными из электронной почты или других источников, где данные могут быть закодированы в этом формате.
     
```python
import quopri

encoded_data = b"Hello=2C=20world=21"
decoded_data = quopri.decode(encoded_data)
print(decoded_data)
```
""",
                        "fnmatch": r"""
Библиотека "fnmatch" используется в Python для сопоставления и фильтрации строк с использованием шаблонов, основанных на грамматике восходящих преобразований.
Вот таблица методов модуля "fnmatch" и их краткие описания:

Метод                     | Описание
-------------------------|-------------------------------------
fnmatch(name, pattern)   | Сопоставляет имя файла с заданным шаблоном.
filter(names, pattern)   | Фильтрует список имен файлов, оставляя только те, которые соответствуют заданному шаблону.
translate(pattern)       | Преобразует заданный шаблон во внутренний формат, используемый для сопоставления.

Вот список наиболее часто используемых методов "fnmatch", их краткое описание и небольшой код, демонстрирующий их работу:

Метод                       | Описание                             | Пример использования
----------------------------|--------------------------------------|--------------------------------------
fnmatch(name, pattern)      | Сопоставляет имя файла с шаблоном.    | fnmatch("example.txt", "*.txt") # True
filter(names, pattern)      | Фильтрует список имен файлов.        | filter(['file1.txt', 'file2.py'], "*.txt") # ['file1.txt']
translate(pattern)          | Преобразует шаблон во внутренний формат.| translate("*.txt") # '[A-Za-z0-9]+\.txt$'
""",
                        "rfc3986_validator": r"""
Название библиотеки: "rfc3986_validator"

Описание: Библиотека "rfc3986_validator" используется для проверки и валидации URL-адресов согласно стандарту RFC 3986.
Она обеспечивает функционал для проверки правильности формата URL и его различных компонентов, таких как схема, хост, путь и другие.

Методы модуля и их описание:

Модуль: rfc3986_validator
validate(url: str) -> bool: Проверяет, соответствует ли заданный URL формату RFC 3986. Возвращает True, если URL действительный, и False в противном случае.
get_scheme(url: str) -> str: Извлекает и возвращает схему (протокол) из заданного URL.
get_host(url: str) -> str: Извлекает и возвращает хост (доменное имя) из заданного URL.
get_path(url: str) -> str: Извлекает и возвращает путь из заданного URL.
get_query(url: str) -> str: Извлекает и возвращает параметры запроса из заданного URL.
get_fragment(url: str) -> str: Извлекает и возвращает фрагмент из заданного URL.

Список самых часто используемых методов, их описание и

validate(url: str) -> bool:
Описание: Проверяет, является ли заданный URL действительным согласно стандарту RFC 3986.

```python
from rfc3986_validator import validate

url = "https://www.example.com"
is_valid = validate(url)
print(is_valid)  # Выводит True, если URL действителен
```

get_host(url: str) -> str:
Описание: Извлекает и возвращает хост (доменное имя) из заданного URL.

```python
from rfc3986_validator import get_host

url = "https://www.example.com/path"
host = get_host(url)
print(host)  # Выводит "www.example.com"
```

get_path(url: str) -> str:
Описание: Извлекает и возвращает путь из заданного URL.

```python
from rfc3986_validator import get_path

url = "https://www.example.com/path"
path = get_path(url)
print(path)  # Выводит "/path"
```
""",
                        "mailcap": r"""
Библиотека "mailcap" в Python используется для обработки типов файлов и ассоциированных программ.


Модуль: mailcap
findmatch: Находит подходящую запись для заданного типа файла и возвращает ее.
getcaps: Возвращает все записи в файле mailcap.
getparam: Возвращает значение параметра из записи mailcap.
listmailcapfiles: Возвращает список файлов mailcap в системе.
lookup: Находит запись mailcap для заданного типа файла.
parse: Разбирает содержимое mailcap-файла и возвращает его в виде словаря.


findmatch: Находит подходящую запись для заданного типа файла и возвращает ее.

```python
import mailcap

filename = "example.txt"
type = "text/plain"

match = mailcap.findmatch(type, filename)
if match:
    command = match[0]
    params = match[1]
    # выполнение команды с использованием параметров
```

getcaps: Возвращает все записи в файле mailcap.

```python
import mailcap

caps = mailcap.getcaps()
for cap in caps:
    print(cap)
```

lookup: Находит запись mailcap для заданного типа файла.

```python
import mailcap

type = "text/plain"
lookup = mailcap.lookup(type)
if lookup:
    print(lookup)
```
   
Маленький код для демонстрации этих методов:
```python
import mailcap

filename = "example.txt"
type = "text/plain"

match = mailcap.findmatch(type, filename)
if match:
    command = match[0]
    params = match[1]
    # выполнение команды с использованием параметров

caps = mailcap.getcaps()
for cap in caps:
    print(cap)

lookup = mailcap.lookup(type)
if lookup:
    print(lookup)
```
""",
                        "filecmp": r"""
Библиотека "filecmp" используется для сравнения файлов и директорий в Python.
Она предоставляет функциональность для сравнения содержимого файлов, определения различий между файлами и обнаружения одинаковых файлов.

Методы и подмодули модуля "filecmp" можно представить в следующей таблице:

   Метод/Подмодуль          | Краткое Описание
   ------------------------|-------------------
   cmp(files1, files2)     | Сравнивает содержимое двух файлов и возвращает True, если они одинаковы, и False в противном случае.
   cmpfiles(dir1, dir2)    | Сравнивает содержимое двух директорий и возвращает список различий и список одинаковых файлов.
   clear_cache()           | Очищает кэш, используемый для сравнения файлов и директорий.
   dircmp(dir1, dir2)      | Возвращает объект "dircmp", содержащий информацию о сравнении двух директорий, включая различия и одинаковые файлы.
   cmp_fuzzy(file1, file2) | Сравнивает содержимое двух файлов с использованием нечеткого(размытого) алгоритма сравнения.
   
Некоторые из самых часто используемых методов библиотеки "filecmp" вместе с краткими описаниями и примерами кода:

Метод cmp(files1, files2) Сравнивает содержимое двух файлов.

```python
import filecmp

if filecmp.cmp("file1.txt", "file2.txt"):
    print("Файлы одинаковы.")
else:
    print("Файлы различаются.")
```

Метод cmpfiles(dir1, dir2) Сравнивает содержимое двух директорий и возвращает списки различий и одинаковых файлов.

```python
import filecmp

diff_files, common_files = filecmp.cmpfiles("dir1", "dir2")

print("Различные файлы:")
for file in diff_files:
    print(file)

print("Одинаковые файлы:")
for file in common_files:
    print(file)
```
""",
                        "locale": r"""
Библиотека "locale" в Python используется для обработки локализации и форматирования числовых,
датовых и строковых значений в соответствии с настройками локали операционной системы.

Таблица методов и их описания для модуля "locale" и его подмодулей:

Модуль "locale":
setlocale(category, locale=None): устанавливает текущую локаль для данной категории (категории определяют тип данных, например, числа, даты и др.).

Подмодуль "localeconv":
localeconv(): возвращает словарь с настройками форматирования чисел и валюты в текущей локали.

Наиболее часто используемые методы и их описание:

setlocale(category, locale=None): Этот метод позволяет установить локаль для определенной категории.
Например, setlocale(locale.LC_NUMERIC, 'en_US') устанавливает локаль для чисел на английский (США). 


```python
import locale

locale.setlocale(locale.LC_NUMERIC, 'en_US')
formatted_number = locale.format_string("%.2f", 1234.5678)
print(formatted_number)
```
Результат: "1,234.57"
  
Помните, что информация о локализации и форматировании может отличаться в зависимости от операционной системы и языка установки Python.
""",
                        "getopt": r"""
Библиотека "getopt" в Python используется для разбора аргументов командной строки.
Она позволяет программам легко определять и обрабатывать аргументы, передаваемые при запуске программы.

Методы и подмодули библиотеки "getopt":
getopt.getopt(args, shortopts, longopts=None): Парсит аргументы командной строки, возвращает пару (opts, args), где opts - список кортежей со значением и аргументом, args - список непарсированных аргументов.
getopt.gnu_getopt(args, shortopts, longopts=None): Аналогичен методу getopt.getopt(), но поддерживает нестандартный формат аргументов, включая возможность использования дефисов в значении аргумента.
getopt.GetoptError: Исключение, возникающее при ошибке разбора аргументов командной строки. Оно содержит информацию об ошибке и методы для доступа к ней.


getopt.getopt(args, shortopts, longopts=None): Парсит аргументы командной строки и возвращает опции и аргументы.

```python
import getopt
import sys

args = sys.argv[1:]
shortopts = "ho:v"   # Опции без аргументов: -h, -o, -v
longopts = ["help", "output=", "verbose"]  # Опции с аргументами: --help, --output, --verbose

try:
    opts, args = getopt.getopt(args, shortopts, longopts)
except getopt.GetoptError:
    print("Ошибка в аргументах командной строки.")
```

getopt.gnu_getopt(args, shortopts, longopts=None): Парсит аргументы командной строки с нестандартным форматом и возвращает опции и аргументы.

```python
import getopt
import sys

args = sys.argv[1:]
shortopts = "ho:v"   # Опции без аргументов: -h, -o, -v
longopts = ["help", "output=", "verbose"]  # Опции с аргументами: --help, --output, --verbose

try:
    opts, args = getopt.gnu_getopt(args, shortopts, longopts)
except getopt.GetoptError:
    print("Ошибка в аргументах командной строки.")
```
""",
                        "webcolors": r"""
Библиотека "webcolors" используется для работы с цветами веб-страниц, конвертации цветовых кодов и определения названий цветов.
 
Описание методов модуля "webcolors" и его подмодулей:

Модуль "webcolors":
`hex_to_rgb(hex_color)`: преобразует шестнадцатеричный код цвета в формат RGB.
`rgb_to_hex(rgb_color)`: преобразует цвет в формате RGB в шестнадцатеричный код.
`name_to_rgb(color_name)`: возвращает RGB-значение заданного названия цвета.
`rgb_to_name(rgb_color)`: возвращает название цвета для заданного значения RGB.

Список часто используемых методов, их краткое описание и

Метод `hex_to_rgb(hex_color)`: преобразует шестнадцатеричный код цвета в формат RGB.

```python
from webcolors import hex_to_rgb

hex_color = "#FF0000"
rgb_color = hex_to_rgb(hex_color)
print(rgb_color)  # Output: (255, 0, 0)
```

Метод `rgb_to_hex(rgb_color)`: преобразует цвет в формате RGB в шестнадцатеричный код.

```python
from webcolors import rgb_to_hex

rgb_color = (255, 0, 0)
hex_color = rgb_to_hex(rgb_color)
print(hex_color)  # Output: "#FF0000"
```

Метод `name_to_rgb(color_name)`: возвращает RGB-значение заданного названия цвета.

```python
from webcolors import name_to_rgb

color_name = "red"
rgb_color = name_to_rgb(color_name)
print(rgb_color)  # Output: (255, 0, 0)
```

Метод `rgb_to_name(rgb_color)`: возвращает название цвета для заданного значения RGB.

```python
from webcolors import rgb_to_name

rgb_color = (255, 0, 0)
color_name = rgb_to_name(rgb_color)
print(color_name)  # Output: "red"
```
""",
                        "hmac": r"""
Библиотека "hmac" в Python используется для создания и проверки кодов аутентификации HMAC (Hash-based Message Authentication Code).
HMAC обеспечивает целостность и аутентификацию сообщений, используя хеш-функции.

Таблица методов модуля "hmac" и их краткого описания:

   Метод                           | Описание
   -------------------------------|--------------------------------
   hmac.new(key, msg, digestmod)  | Создает новый объект HMAC с заданным ключом, сообщением и используемой хеш-функцией.
   hmac.digest()                   | Возвращает HMAC в виде строки байтов.
   hmac.hexdigest()                | Возвращает HMAC в виде шестнадцатеричной строки.
   hmac.compare_digest(a, b)       | Сравнивает два HMAC без утечек информации о значениях.

   (Подмодулей в модуле "hmac" нет)

Список самых часто используемых методов, их краткое описание и

   Метод                           | Описание                       | Пример кода
   -------------------------------|--------------------------------|-----------------------------
   hmac.new(key, msg, digestmod)  | Создает новый HMAC объект с заданным ключом, сообщением и используемой хеш-функцией. | `hmac_object = hmac.new(key, msg, hashlib.sha256)`
   hmac.digest()                   | Возвращает HMAC в виде строки байтов. | `hmac_bytes = hmac_object.digest()`
   hmac.hexdigest()                | Возвращает HMAC в виде шестнадцатеричной строки. | `hmac_string = hmac_object.hexdigest()`
   hmac.compare_digest(a, b)       | Сравнивает два HMAC и возвращает True, если они совпадают, иначе возвращает False. | `result = hmac.compare_digest(hmac1, hmac2)`
""",
                        "bleach": r"""
Библиотека "bleach" используется для безопасного удаления или экранирования HTML-тегов и атрибутов в тексте,
чтобы предотвратить возможность внедрения вредоносного кода или XSS-атак.

Метод              | Описание
-------------------|-----------------------------------------------------------
clean              | Удаляет или экранирует HTML-теги и атрибуты из текста
linkify            | Преобразует URL-адреса в тексте в ссылки
strip_tags         | Удаляет все HTML-теги из текста
escape             | Экранирует HTML-сущности в тексте
unescape           | Преобразует экранированные HTML-сущности в их исходное состояние

Наиболее часто используемые методы "bleach" вместе с их кратким описанием и примером кода:

Метод              | Описание                                   | Пример кода
-------------------|--------------------------------------------|------------------------------
clean              | Удаляет или экранирует HTML-теги и атрибуты | clean(text, tags=['p', 'a'])
linkify            | Преобразует URL-адреса в тексте в ссылки   | linkify(text)
strip_tags         | Удаляет все HTML-теги из текста             | strip_tags(text)
escape             | Экранирует HTML-сущности в тексте           | escape(text)
unescape           | Преобразует экранированные HTML-сущности     | unescape(text)
""",
                        "genericpath": r"""
Библиотека "genericpath" в Python используется для работы с путями и файловой системой на разных платформах.
Она предоставляет универсальные методы для обработки путей, создания новых путей, проверки наличия файлов и директорий,
а также для работы с именами файлов.

Таблица методов и их описания в модуле "genericpath":

| Метод            | Описание                                                |
|------------------|---------------------------------------------------------|
| isdir(path)      | Проверяет, является ли указанный путь директорией.        |
| isfile(path)     | Проверяет, является ли указанный путь файлом.            |
| exists(path)     | Проверяет, существует ли указанный путь.                 |
| lexists(path)    | Проверяет, существует ли указанный путь (обходя символические ссылки). |
| split(path)      | Разделяет путь на директорию и базовое имя файла.        |
| splitext(path)   | Разделяет путь на базовое имя файла и расширение.        |
| basename(path)   | Возвращает последний компонент пути (имя файла или директории). |
| dirname(path)    | Возвращает директорию из пути.                          |
| join(path, *paths) | Объединяет пути в переносимый образ.                    |
| normpath(path)   | Преобразует путь, удаляя избыточные разделители и ссылки "." и "..". |
| abspath(path)    | Возвращает абсолютный путь.                             |


isdir(path): Проверяет, является ли указанный путь директорией.

```python
import os.path

path = '/path/to/directory'
if os.path.isdir(path):
    print(f"{path} is a directory.")
```

isfile(path): Проверяет, является ли указанный путь файлом.

```python
import os.path

path = '/path/to/file.txt'
if os.path.isfile(path):
    print(f"{path} is a file.")
```

exists(path): Проверяет, существует ли указанный путь.

```python
import os.path

path = '/path/to/file.txt'
if os.path.exists(path):
    print(f"{path} exists.")
```

splitext(path): Разделяет путь на базовое имя файла и расширение.

```python
import os.path

path = '/path/to/file.txt'
base_name, extension = os.path.splitext(path)
print(f"Base name: {base_name}")
print(f"Extension: {extension}")
```
""",
                        "lzma": r"""
Библиотека "lzma" в Python используется для сжатия и распаковки данных
с использованием алгоритма сжатия LZMA (Lempel-Ziv-Markov chain Algorithm).

Методы модуля "lzma" и его подмодулей:

`lzma.compress(data, format=lzma.FORMAT_XZ, check=-1)`: Сжимает данные, используя алгоритм сжатия LZMA.
`lzma.decompress(data, format=lzma.FORMAT_XZ, memlimit=None, filters=None)`: Распаковывает сжатые данные, сжатые с использованием алгоритма LZMA.
`lzma.LZMACompressor(format=lzma.FORMAT_XZ, check=-1, preset=None, filters=None)`: Создает объект компрессора LZMA для сжатия данных.
`lzma.LZMADecompressor(format=lzma.FORMAT_XZ, memlimit=None, filters=None)`: Создает объект декомпрессора LZMA для распаковки сжатых данных.
`lzma.is_check_supported(check)`: Проверяет, поддерживается ли заданный тип проверки сжатия.
`lzma.CHECK_NONE`: Константа, представляющая отсутствие проверки сжатия.
`lzma.CHECK_CRC32`: Константа, представляющая проверку сжатия с использованием алгоритма CRC32.
`lzma.CHECK_CRC64`: Константа, представляющая проверку сжатия с использованием алгоритма CRC64.
`lzma.CHECK_SHA256`: Константа, представляющая проверку сжатия с использованием алгоритма SHA-256.

`lzma.compress(data)`: Сжимает данные, используя алгоритм сжатия LZMA.

```python
import lzma

data = b'Hello, World!'
compressed_data = lzma.compress(data)
```

`lzma.decompress(data)`: Распаковывает сжатые данные, сжатые с использованием алгоритма LZMA.

```python
import lzma

compressed_data = b'\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4\x46\x02\x00!\x01\x16\x00\x00\x00t/\xe5\xfd\x01\x00\x00\x00\xff\xff'
decompressed_data = lzma.decompress(compressed_data)
```

Обратите внимание, что эти примеры демонстрируют базовое использование методов
и не учитывают параметры настройки, такие как формат сжатия и проверка сжатия.
""",
                        "gc": r"""
Библиотека "gc" в Python используется для управления сборкой мусора.
Она предоставляет функции и методы для контроля за автоматическим освобождением памяти, которая больше не используется программой.

Методы модуля "gc" и его подмодулей:

Метод                     | Описание
-------------------------|---------------------------------------
gc.disable()              | Отключает автоматическую сборку мусора.
gc.enable()               | Включает автоматическую сборку мусора.
gc.collect()              | Принудительно запускает сборку мусора.
gc.get_threshold()        | Возвращает текущие пороги сборки мусора.
gc.set_threshold(threshold) | Устанавливает пороги сборки мусора.
gc.get_count()            | Возвращает количество сборок мусора, проведенных до сих пор.
gc.get_objects()          | Возвращает список всех объектов, находящихся в памяти.

Самые часто используемые методы в библиотеке "gc":

Метод                       | Описание                        | Пример кода
----------------------------|---------------------------------|-------------------
gc.collect()                | Принудительно запускает сборку мусора. | gc.collect()
gc.get_threshold()          | Возвращает текущие пороги сборки мусора. | threshold = gc.get_threshold()
gc.set_threshold(threshold) | Устанавливает пороги сборки мусора. | gc.set_threshold(700, 10, 10)
gc.get_count()              | Возвращает количество сборок мусора, проведенных до сих пор. | count = gc.get_count()

Этот код показывает использование метода gc.collect(), который принудительно запускает сборку мусора:

```python
import gc

# Создание объектов
x = [1, 2, 3]
y = [4, 5, 6]

# Удаление ссылок на объекты
del x
del y

# Принудительная сборка мусора
gc.collect()
```
Надеюсь, это поможет вам понять и использовать библиотеку "gc" в Python.
Если у вас возникнут дополнительные вопросы, не стесняйтесь задавать их.
""",
                        "zipimport": r"""
Библиотека "zipimport" в Python используется для импорта модулей из zip-архивов.
Она предоставляет возможность загружать и использовать код, хранящийся в сжатом формате,
что может быть полезно для эффективного распространения и дистрибуции приложений.

Вот таблица методов и подмодулей библиотеки "zipimport" и их краткое описание:

Метод/Подмодуль    | Описание
---------------------------------------
zipimport.zipimporter   | Класс, который позволяет импортировать модули из zip-архивов.
zipimport.zipimporter.get_code   | Возвращает объект кода модуля.
zipimport.zipimporter.get_data   | Возвращает содержимое файла из zip-архива.
zipimport.zipimporter.get_filename   | Возвращает имя файла из zip-архива, соответствующего модулю.
zipimport.zipimporter.get_source   | Возвращает исходный код модуля в виде строки.

Вот список самых часто используемых методов библиотеки "zipimport", их краткое описание и пример кода, демонстрирующего их работу:

zipimport.zipimporter.get_code Возвращает объект кода модуля.

```python
import zipimport

importer = zipimport.zipimporter("module.zip")
code_object = importer.get_code("module")
```

zipimport.zipimporter.get_data Возвращает содержимое файла из zip-архива.

```python
import zipimport

importer = zipimport.zipimporter("module.zip")
data = importer.get_data("file.txt")
```

zipimport.zipimporter.get_filename Возвращает имя файла из zip-архива, соответствующего модулю.

```python
import zipimport

importer = zipimport.zipimporter("module.zip")
filename = importer.get_filename("module")
```

zipimport.zipimporter.get_source Возвращает исходный код модуля в виде строки.

```python
import zipimport

importer = zipimport.zipimporter("module.zip")
source_code = importer.get_source("module")
```
""",
                        "trace": r"""
Библиотека "trace" используется в Python для отладки и трассировки выполнения программы.
Она предоставляет инструменты для отслеживания, как программа выполняется и какие функции вызываются.

Методы модуля "trace" и его подмодулей:
`traceback.print_exc(limit=None, file=None, chain=True)` - выводит трассировку текущего исключения в файл или stdout.
`traceback.format_exc(limit=None, chain=True)` - возвращает трассировку текущего исключения в виде строки.
`sys.settrace(tracefunc)` - устанавливает функцию трассировки для последующих вызовов.
`sys.gettrace()` - возвращает текущую функцию трассировки.
`sys.setprofile(profilefunc)` - устанавливает функцию профилирования для последующих вызовов.
`sys.getprofile()` - возвращает текущую функцию профилирования.

`traceback.print_exc()` - выводит трассировку текущего исключения в стандартный вывод.

```python
try:
    # код, который может вызвать исключение
except Exception:
    traceback.print_exc()
```

`sys.settrace()` - устанавливает функцию трассировки для отслеживания вызовов функций.

```python
def trace_func(frame, event, arg):
    print(f"Calling function {frame.f_code.co_name}")
    return trace_func

sys.settrace(trace_func)
# код, вызывающий функции
sys.settrace(None)  # отключение трассировки
```

`sys.setprofile()` - устанавливает функцию профилирования для измерения времени выполнения функций.

```python
import cProfile

def profile_func(frame, event, arg):
    profiler = cProfile.Profile()
    profiler.enable()
    return profiler

sys.setprofile(profile_func)
# код, вызывающий функции
sys.setprofile(None)  # отключение профилирования
```

Существует более широкий набор функций и методов, которые могут быть полезны в разных ситуациях.
""",
                        "gtts": r"""
Библиотека "gtts" (Google Text-to-Speech) используется для преобразования текста в речь.
Она предоставляет возможность синтеза голоса на разных языках, используя голосовые данные от Google.

Методы модуля "gtts":
gTTS(text, lang): принимает текст и язык в качестве параметров и возвращает аудиофайл с синтезированным голосом.
save(file): сохраняет аудиофайл на диск.
get_urls(text): возвращает список URL-адресов, которые могут быть использованы для визуализации прогресса синтеза речи.
lang_check(): проверяет доступные языки для синтеза речи.

Методы подмодуля "gtts.lang":
tld(): возвращает список языков и их TLD (top-level domain).
tts_langs(): возвращает список языков, поддерживаемых gTTS.

Самые часто используемые методы:
gTTS(text, lang): Создает объект gTTS с указанным текстом и языком.
save(file): Сохраняет аудиофайл на диск с использованием указанного имени файла и расширения (.mp3).
get_urls(text): Возвращает список URL-адресов для отслеживания прогресса синтеза речи.
   
Пример кода для использования библиотеки "gtts":

```python
from gtts import gTTS

text = "Привет, как дела?"
language = "ru"

# Создание объекта gTTS с текстом и языком
tts = gTTS(text=text, lang=language)

# Сохранение аудиофайла
tts.save("output.mp3")

# Получение списка URL-адресов для визуализации прогресса синтеза речи
urls = tts.get_urls(text)
```

Эта библиотека полезна для создания аудиофайлов со сгенерированной речью на разных языках.
""",
                        "graphlib": r"""
Библиотека "graphlib" в Python используется для работы с графами и решения различных задач на графах,
таких как поиск кратчайшего пути, определение связности графа и других алгоритмических задач.

Таблица методов модуля "graphlib" и его подмодулей:

Метод                    | Описание                      
------------------------ | -----------------------------
graphlib.TopologicalSort | Реализует сортировку вершин графа в топологическом порядке.
graphlib.Graph           | Представляет граф и предоставляет методы для добавления вершин и ребер, проверки наличия ребер и других операций.
graphlib.DiGraph         | Представляет ориентированный граф и предоставляет методы для работы с ним, аналогичные методам Graph.
graphlib.find_cycles     | Позволяет найти все циклы в графе и предоставляет их в виде списка.

Список самых частых методов, их краткое описание и

TopologicalSort Сортирует вершины графа в топологическом порядке.

```python
import graphlib

graph = graphlib.Graph()
graph.add_edges_from([(1, 2), (1, 3), (2, 3), (2, 4)])

sorted_vertices = graphlib.TopologicalSort(graph)
print(sorted_vertices)
```

Graph.add_vertex Добавляет новую вершину в граф.

```python
import graphlib

graph = graphlib.Graph()
graph.add_vertex(1)
graph.add_vertex(2)
```

DiGraph.add_edge Добавляет новое ребро между двумя вершинами в ориентированном графе.

```python
import graphlib

graph = graphlib.DiGraph()
graph.add_edge(1, 2)
graph.add_edge(2, 3)
```

find_cycles Находит все циклы в графе и возвращает их в виде списка.

```python
import graphlib

graph = graphlib.Graph()
graph.add_edges_from([(1, 2), (2, 3), (3, 1), (4, 5)])

cycles = graphlib.find_cycles(graph)
print(cycles)
```
""",
                        "binhex": r"""
Библиотека "binhex" в Python используется для преобразования двоичных данных в шестнадцатеричный формат и обратно.
Она предоставляет функции для кодирования и декодирования данных, а также для чтения и записи файлов в формате binhex.

Методы модуля "binhex" и его подмодулей:

Модуль "binhex":
binhex.hexlify(data): Преобразует двоичные данные в шестнадцатеричный формат.
binhex.unhexlify(hexdata): Преобразует данные из шестнадцатеричного формата в двоичный формат.
binhex.binhex(binfile, hexfile): Кодирует двоичный файл в файл в формате binhex.
binhex.hexbin(hexfile, binfile): Декодирует файл в формате binhex в двоичный файл.

Наиболее часто используемые методы:

binhex.hexlify(data): Преобразует двоичные данные в шестнадцатеричный формат.

```python
import binhex

data = b'Hello, World!'
hex_data = binhex.hexlify(data)
print(hex_data)
```

binhex.unhexlify(hexdata): Преобразует данные из шестнадцатеричного формата в двоичный формат.

```python
import binhex

hex_data = '48656c6c6f2c20576f726c6421'
data = binhex.unhexlify(hex_data)
print(data)
```

binhex.binhex(binfile, hexfile): Кодирует двоичный файл в файл в формате binhex.

```python
import binhex

bin_file = 'input.bin'
hex_file = 'output.hex'
binhex.binhex(bin_file, hex_file)
```

binhex.hexbin(hexfile, binfile): Декодирует файл в формате binhex в двоичный файл.

```python
import binhex

hex_file = 'input.hex'
bin_file = 'output.bin'
binhex.hexbin(hex_file, bin_file)
```
""",
                        "glob": r"""
Библиотека "glob" предназначена для поиска файлов с использованием шаблонов и расширений в заданном каталоге.

Методы модуля "glob" и их краткое описание:

glob.glob(pathname): Возвращает список всех путей, соответствующих заданному шаблону.
glob.escape(pathname): Экранирует все специальные символы в заданном пути, чтобы они были интерпретированы как обычные символы.

Пример кода для демонстрации работы метода glob.glob():

```python
import glob

files = glob.glob('*.txt')
print(files)
```

В этом примере метод glob.glob('*.txt') ищет все файлы с расширением ".txt" в текущем каталоге и возвращает
список путей к этим файлам, который затем выводится на экран.
""",
                        "errno": r"""
Библиотека "errno" в Python используется для обработки ошибок, связанных с системными вызовами и функциями операционной системы.
Она предоставляет доступ к кодам ошибок, которые могут возникать
при выполнении операций ввода-вывода, работы с файлами, сетью и другими системными ресурсами.

Методы и подмодули библиотеки "errno":

errno.errorcode: Возвращает словарь, ключами которого являются коды ошибок, а значениями - соответствующие им символьные имена.
errno.geterrno(): Возвращает код текущей ошибки.
errno.geterror(): Возвращает описание текущей ошибки в виде строки.
errno.strerror(errno): Возвращает описание ошибки по заданному коду ошибки.
errno.clear(): Очищает код текущей ошибки.

Самые часто используемые методы библиотеки "errno":

errno.errorcode: Возвращает словарь, где ключами являются коды ошибок, а значениями - символьные имена.
Например: {'ENOENT': 'No such file or directory', 'EACCES': 'Permission denied'}.

```python
import errno

error_codes = errno.errorcode
print(error_codes)
```

errno.geterrno(): Возвращает код текущей ошибки. Например: 2.

```python
import errno

error_num = errno.geterrno()
print(error_num)
```

errno.geterror(): Возвращает описание текущей ошибки в виде строки. Например: "No such file or directory".

```python
import errno

error_desc = errno.geterror()
print(error_desc)
```
""",
                        "webencodings": r"""
Библиотека "webencodings" используется для работы с кодированием и декодированием текста в веб-разработке.
Она предоставляет функции для преобразования между различными форматами кодировки, такими как HTML-entities, UTF-8 и другие.

Методы модуля "webencodings" и его подмодулей:

Модуль "webencodings":
"decode(s, encoding='utf-8', errors='strict')": Декодирует строку "s" из указанной кодировки в Unicode.
"encode(s, encoding='utf-8', errors='strict')": Кодирует строку "s" в указанной кодировке.
"htmldecode(s, keep_ignorable=False, encoding='utf-8', errors='xmlcharrefreplace')": Декодирует строку "s" из HTML-entities в Unicode.
"htmlencode(s, encoding='utf-8', errors='xmlcharrefreplace')": Преобразует строку "s" в HTML-entities.
"unquote(qstring, encoding='utf-8', errors='replace')": Декодирует строку "qstring" из формата URL-кодирования.

Самые часто используемые методы "webencodings" и их описание с примерами кода:

"decode(s, encoding='utf-8', errors='strict')": Декодирует строку "s" из указанной кодировки в Unicode.

```python
import webencodings

encoded_string = b'\xd0\x9f\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82'
decoded_string = webencodings.decode(encoded_string, encoding='utf-8')
print(decoded_string)  # Выводит: Привет
```

"encode(s, encoding='utf-8', errors='strict')": Кодирует строку "s" в указанной кодировке.

```python
import webencodings

decoded_string = 'Привет'
encoded_string = webencodings.encode(decoded_string, encoding='utf-8')
print(encoded_string)  # Выводит: b'\xd0\x9f\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82'
```

"htmldecode(s, keep_ignorable=False, encoding='utf-8', errors='xmlcharrefreplace')": Декодирует строку "s" из HTML-entities в Unicode.

```python
import webencodings

html_string = '&lt;div&gt;Hello&lt;/div&gt;'
decoded_string = webencodings.htmldecode(html_string)
print(decoded_string)  # Выводит: <div>Hello</div>
```

"htmlencode(s, encoding='utf-8', errors='xmlcharrefreplace')": Преобразует строку "s" в HTML-entities.

```python
import webencodings

plain_string = '<div>Hello</div>'
encoded_string = webencodings.htmlencode(plain_string)
print(encoded_string)  # Выводит: &lt;div&gt;Hello&lt;/div&gt;
```

"unquote(qstring, encoding='utf-8', errors='replace')": Декодирует строку "qstring" из формата URL-кодирования.

```python
import webencodings

url_encoded_string = 'Hello%20World%21'
decoded_string = webencodings.unquote(url_encoded_string)
print(decoded_string)  # Выводит: Hello World!
```
""",
                        "netrc": r"""
Библиотека "netrc" в Python используется для работы с файлами .netrc, которые содержат информацию о пользователях,
паролях и хостах для автоматической аутентификации при подключении к удаленным серверам.

Методы модуля "netrc":
`netrc.netrc(file)` - создает объект, представляющий файл .netrc.
`netrc.hosts()` - возвращает список имен хостов из файла .netrc.
`netrc.host(host)` - возвращает объект, представляющий информацию о конкретном хосте.
`netrc.authenticators(host)` - возвращает кортеж с именем пользователя, паролем и аутентификационным методом для указанного хоста.

Самые часто используемые методы:
`netrc.hosts()` - возвращает список хостов из файла .netrc.
`netrc.authenticators(host)` - возвращает информацию об аутентификации для указанного хоста.


`netrc.authenticators(host)`:

```python
import netrc

def get_credentials(hostname):
    credentials = netrc.netrc()
    auth = credentials.authenticators(hostname)
    if auth:
        username, _, password = auth
        return username, password
    else:
        return None

hostname = "example.com"
credentials = get_credentials(hostname)
if credentials:
    username, password = credentials
    print(f"Authenticated on {hostname} with username: {username} and password: {password}")
else:
    print(f"No credentials found for {hostname}")
```
""",
                        "readline": r"""
Библиотека "readline" используется в Python для обеспечения функциональности чтения и редактирования строк в интерактивной командной оболочке.

Методы модуля "readline" и его подмодулей:

readline(): Читает строку из входного потока.
add_history(string): Добавляет строку в историю командной оболочки.
clear_history(): Очищает историю командной оболочки.
get_history_length(): Возвращает количество записей в истории командной оболочки.
set_history_length(length): Устанавливает максимальное количество записей в истории командной оболочки.
get_current_history_length(): Возвращает текущую длину истории командной оболочки.
remove_history_item(pos): Удаляет запись из истории командной оболочки по указанной позиции.
replace_history_item(pos, string): Заменяет запись в истории командной оболочки по указанной позиции новой строкой.

Наиболее часто используемые методы:

readline(): Читает строку из входного потока.

```python
import readline

input_string = readline.readline()
print("Input:", input_string)
```

add_history(string): Добавляет строку в историю командной оболочки.

```python
import readline

readline.add_history("command 1")
readline.add_history("command 2")
```

clear_history(): Очищает историю командной оболочки.

```python
import readline

readline.clear_history()
```
""",
                        "resource": r"""
Библиотека "resource" в Python используется для доступа и управления системными ресурсами, такими как время CPU, память и дескрипторы файлов.

Методы и подмодули модуля "resource":

`getrusage(who)` - возвращает информацию о системных ресурсах для указанного процесса или группы процессов.
`getrlimit(resource)` - получает текущие ограничения на указанный ресурс.
`setrlimit(resource, limits)` - устанавливает ограничения на указанный ресурс.
`getpagesize()` - возвращает размер страницы памяти операционной системы.
`getrusage()` - возвращает информацию о системных ресурсах для текущего процесса.
`RUSAGE_SELF` - константа, указывающая на текущий процесс.
`RUSAGE_CHILDREN` - константа, указывающая на дочерние процессы текущего процесса.

Наиболее часто используемые методы:

`getrusage(who)` - получает информацию о системных ресурсах для указанного процесса или группы процессов.

```python
import resource

usage = resource.getrusage(resource.RUSAGE_SELF)
print(usage)
```

`getrlimit(resource)` - получает текущие ограничения на указанный ресурс.

```python
import resource

limit = resource.getrlimit(resource.RLIMIT_CPU)
print(limit)
```

`setrlimit(resource, limits)` - устанавливает ограничения на указанный ресурс.

```python
import resource

# Ограничение на время CPU - 2 секунды
limits = (2, resource.RLIM_INFINITY)
resource.setrlimit(resource.RLIMIT_CPU, limits)
```
""",
                        "pyclbr": r"""
Библиотека "pyclbr" в Python используется для анализа и чтения исходного кода классов и функций в модуле.
Она позволяет получить информацию о структуре программы, такую как классы, методы, атрибуты и их связи.
  
Таблица методов модуля "pyclbr" и его подмодулей:

   Метод              | Описание
   ------------------ | -------------------------------------------------------
   `readmodule()`     | Читает и анализирует модуль, возвращая словарь классов и функций.
   `readmodule_ex()`  | Похож на `readmodule()`, но также возвращает дополнительную информацию о модуле.
   `Class`            | Класс, представляющий отдельный класс из исходного кода.
   `Function`         | Класс, представляющий отдельную функцию из исходного кода.
   `Module`           | Класс, представляющий модуль и его структуру.

`readmodule()` Читает и анализирует модуль, возвращая словарь классов и функций.

```python
import pyclbr

module_data = pyclbr.readmodule('module_name')

for class_name, class_data in module_data.items():
    print(f"Class: {class_name}")
    for method_name, method_data in class_data.methods.items():
        print(f"Method: {method_name}")
```
   
`Class` Класс, представляющий отдельный класс из исходного кода.

```python
import pyclbr

class_data = pyclbr.Class('class_name')

print(f"Class: {class_data.name}")
for method_name, method_data in class_data.methods.items():
    print(f"Method: {method_name}")
```

`Function` Класс, представляющий отдельную функцию из исходного кода.

```python
import pyclbr

function_data = pyclbr.Function('function_name')

print(f"Function: {function_data.name}")
print(f"Start line: {function_data.lineno}")
```

`Module` Класс, представляющий модуль и его структуру.

```python
import pyclbr

module_data = pyclbr.Module('module_name')

print(f"Module: {module_data.name}")
for class_name, class_data in module_data.classes.items():
    print(f"Class: {class_name}")
```
""",
                        "ntpath": r"""
Библиотека "ntpath" в Python используется для обработки и манипулирования путями файловой системы
с учетом специфических особенностей операционной системы Windows.

Таблица методов модуля и его подмодуля "ntpath" и их краткое описание:

Метод                                     | Описание
----------------------------------------|---------------------------------------------------
ntpath.abspath(path)                     | Возвращает абсолютный путь к указанному пути.
ntpath.basename(path)                    | Возвращает базовое имя файла или каталога из указанного пути.
ntpath.commonprefix(list)                | Возвращает наибольший общий префикс из списка путей.
ntpath.dirname(path)                     | Возвращает каталог, содержащий указанный путь.
ntpath.exists(path)                      | Проверяет, существует ли указанный путь.
ntpath.expanduser(path)                  | Заменяет в указанном пути тильду (~) на домашний каталог пользователя.
ntpath.expandvars(path)                  | Заменяет переменные окружения в указанном пути на их значения.
ntpath.isfile(path)                      | Проверяет, является ли указанный путь файлом.
ntpath.isdir(path)                       | Проверяет, является ли указанный путь каталогом.
ntpath.join(path, *paths)                | Объединяет пути с использованием разделителя.
ntpath.normpath(path)                    | Нормализует указанный путь, удаляя двойные слеши и точки.
ntpath.realpath(path)                    | Возвращает канонический абсолютный путь к указанному пути.
ntpath.relpath(path, start)              | Возвращает относительный путь от исходного пути до указанного пути.
ntpath.split(path)                       | Разделяет указанный путь на имя каталога и имя файла.

Несколько часто используемых методов "ntpath" с их кратким описанием и примерами кода:

Метод                                     | Описание                                | Пример
-----------------------------------------|-----------------------------------------|--------------------------------------------------
ntpath.basename(path)                     | Возвращает базовое имя файла или каталога из указанного пути. | dirname, filename = ntpath.split('/path/to/file.txt') print(filename) -> 'file.txt'
ntpath.exists(path)                       | Проверяет, существует ли указанный путь. | if ntpath.exists('/path/to/file.txt'): print("File exists")
ntpath.join(path, *paths)                 | Объединяет пути с использованием разделителя. | full_path = ntpath.join('/path/to', 'file.txt') print(full_path) -> '/path/to/file.txt'
""",
                        "wave": r"""
Библиотека "wave" используется в Python для работы с аудиофайлами формата WAV.
Она позволяет открывать,
создавать, записывать и обрабатывать звуковые файлы в формате WAV.
Методы и подмодули библиотеки "wave" и их краткое описание:

wave.open(file, mode): Открывает WAV-файл с указанным именем файла и режимом доступа.
wave.Wave_read.getnchannels(): Возвращает число каналов в WAV-файле (моно или стерео).
wave.Wave_read.getsampwidth(): Возвращает размер образца в байтах.
wave.Wave_read.getframerate(): Возвращает частоту дискретизации аудиофайла.
wave.Wave_read.getnframes(): Возвращает количество фреймов в аудиофайле.
wave.Wave_read.readframes(n): Читает и возвращает n фреймов из аудиофайла.
wave.Wave_write.setnchannels(nchannels): Устанавливает число каналов для нового WAV-файла.
wave.Wave_write.setsampwidth(sampwidth): Устанавливает размер образца для нового WAV-файла.
wave.Wave_write.setframerate(framerate): Устанавливает частоту дискретизации для нового WAV-файла.
wave.Wave_write.writeframesraw(data): Записывает сырые байты аудио-данных в новый WAV-файл.
wave.Wave_write.writeframes(data): Записывает фреймы аудио-данных в новый WAV-файл.


wave.open(file, mode): Открывает WAV-файл для чтения или записи.

```python
import wave

with wave.open('audio.wav', 'r') as wav_file:
    # проведите необходимые операции с аудиофайлом
```

wave.Wave_read.getnframes(): Возвращает количество фреймов в аудиофайле.

```python
import wave

with wave.open('audio.wav', 'r') as wav_file:
    num_frames = wav_file.getnframes()
    print(f'Number of frames: {num_frames}')
```

wave.Wave_write.writeframes(data): Записывает фреймы аудио-данных в новый WAV-файл.

```python
import wave

new_frames = b'\x00\x00\x00\x00\x00\x00\x00\x00'  # пример сырых байтов аудио-данных

with wave.open('new_audio.wav', 'w') as wav_file:
    wav_file.setnchannels(1)  # устанавливаем один канал
    wav_file.setsampwidth(2)  # устанавливаем размер образца в два байта
    wav_file.setframerate(44100)  # устанавливаем частоту дискретизации в 44100 Гц
    wav_file.writeframes(new_frames)  # записываем фреймы в новый WAV-файл
```
""",
                        "js2py": r"""
Библиотека "js2py" используется в Python для выполнения и интерпретации JavaScript-кода.
Она предоставляет возможность взаимодействия между Python и JavaScript, позволяя исполнять JavaScript-код внутри среды Python.

Таблица методов модуля "js2py":

Метод           | Описание кратко   
----------------|----------------
eval_js()       | Исполняет переданный JavaScript-код и возвращает его результат.
call()          | Вызывает функцию JavaScript и передает ей аргументы.
set()           | Устанавливает значение переменной JavaScript.
get()           | Получает значение переменной JavaScript.
delete()        | Удаляет переменную JavaScript.

Список самых часто используемых методов, их краткое описание и

eval_js(): Исполняет переданный JavaScript-код и возвращает его результат.

```python
result = eval_js("1 + 2")
print(result)  # Выводит: 3
```

call(): Вызывает функцию JavaScript и передает ей аргументы.
  
```python
js_function = js2py.eval_js("function add(a, b) { return a + b; }")
result = call(js_function, 2, 3)
print(result)  # Выводит: 5
```

set(): Устанавливает значение переменной JavaScript.
  
```python
set("x", 10)
result = eval_js("x")
print(result)  # Выводит: 10
```

get(): Получает значение переменной JavaScript.
  
```python
eval_js("var message = 'Hello, world!'")
result = get("message")
print(result)  # Выводит: Hello, world!
```

delete(): Удаляет переменную JavaScript.
  
```python
eval_js("var x = 5;")
delete("x")
result = eval_js("x")
print(result)  # Выводит: undefined
```
""",
                        "bisect": r"""
Библиотека "bisect" в Python используется для выполнения бинарного поиска в отсортированных последовательностях.
Она предоставляет функции для нахождения места вставки элемента в отсортированный список и для выполнения деления списка на две части.

Методы библиотеки "bisect":
bisect_left(a, x): Возвращает наименьшую позицию для вставки элемента x в отсортированный список а, сохраняя его отсортированность.
bisect_right(a, x): Возвращает наибольшую позицию для вставки элемента x в отсортированный список а, сохраняя его отсортированность.
bisect(a, x): Эквивалентно вызову bisect_right(a, x).
insort_left(a, x): Вставляет элемент x в отсортированный список a на наименьшую позицию, сохраняя его отсортированность.
insort_right(a, x): Вставляет элемент x в отсортированный список a на наибольшую позицию, сохраняя его отсортированность.
insort(a, x): Эквивалентно вызову insort_right(a, x).


bisect_left(a, x) - возвращает индекс наименьшего элемента, который больше или равен x.

```python
import bisect
a = [1, 3, 5, 7]
x = 4
index = bisect.bisect_left(a, x)
print(index)  # Output: 2
```

insort_right(a, x) - вставляет элемент x в отсортированный список a на наибольшую позицию, сохраняя его отсортированность.

```python
import bisect
a = [1, 3, 5, 7]
x = 4
bisect.insort_right(a, x)
print(a)  # Output: [1, 3, 4, 5, 7]
```

bisect_right(a, x) - возвращает индекс первого элемента, который больше x.

```python
import bisect
a = [1, 3, 5, 7]
x = 4
index = bisect.bisect_right(a, x)
print(index)  # Output: 3
```
""",
                        "jsonpointer": r"""
Библиотека "jsonpointer" используется для работы с указателями JSON (JSON pointers).
Она предоставляет функциональность для создания, обновления и извлечения данных из JSON-структур с использованием указателей.

Методы модуля "jsonpointer" и их краткое описание:

`resolve_pointer(json_obj, pointer)`: Разрешает указатель JSON и возвращает соответствующее значение из JSON-объекта.
`set_pointer(json_obj, pointer, value)`: Устанавливает значение по указателю JSON в JSON-объекте.
`remove_pointer(json_obj, pointer)`: Удаляет значение по указателю JSON из JSON-объекта.
`list_pointers(json_obj)`: Возвращает список всех указателей JSON в JSON-объекте.
`escape_pointer(pointer)`: Экранирует специальные символы в указателе JSON.

Некоторые из самых часто используемых методов "jsonpointer" и их краткое описание:

`resolve_pointer(json_obj, pointer)`: Разрешает указатель JSON и возвращает соответствующее значение из JSON-объекта.

```python
import jsonpointer

json_obj = {"name": "John", "age": 30}
pointer = "/name"
value = jsonpointer.resolve_pointer(json_obj, pointer)
print(value)  # Output: John
```

`set_pointer(json_obj, pointer, value)`: Устанавливает значение по указателю JSON в JSON-объекте.

```python
import jsonpointer

json_obj = {"name": "John", "age": 30}
pointer = "/name"
value = "Jane"
jsonpointer.set_pointer(json_obj, pointer, value)
print(json_obj)  # Output: {"name": "Jane", "age": 30}
```

`remove_pointer(json_obj, pointer)`: Удаляет значение по указателю JSON из JSON-объекта.

```python
import jsonpointer

json_obj = {"name": "John", "age": 30}
pointer = "/name"
jsonpointer.remove_pointer(json_obj, pointer)
print(json_obj)  # Output: {"age": 30}
```
""",
                        "grp": r"""
Библиотека "grp" в Python используется для работы с группами пользователей в операционной системе.
Методы модуля "grp" и его подмодулей:

`grp.getgrgid(gid)`: Возвращает информацию о группе по ее идентификатору.
`grp.getgrnam(name)`: Возвращает информацию о группе по ее имени.
`grp.getgrall()`: Возвращает список всех групп в системе.
`grp.getgrgid(gid).gr_name`: Возвращает имя группы по ее идентификатору.
`grp.getgrgid(gid).gr_passwd`: Возвращает пароль группы по ее идентификатору.

Самые часто используемые методы:

Метод `grp.getgrgid(gid)` используется для получения информации о группе по ее идентификатору.
     
```python
import grp

gid = 1000
group_info = grp.getgrgid(gid)
print(group_info)
```

Метод `grp.getgrnam(name)` используется для получения информации о группе по ее имени.
     
```python
import grp

group_name = "developers"
group_info = grp.getgrnam(group_name)
print(group_info)
```

Метод `grp.getgrall()` возвращает список всех групп в системе.
     
```python
import grp

all_groups = grp.getgrall()
for group_info in all_groups:
    print(group_info)
```

Пожалуйста, обратите внимание, что эти примеры кода могут потребовать соответствующих разрешений для доступа к информации о группах пользователя на операционной системе.
""",
                        "logging": r"""
Библиотека "logging" в Python используется для добавления логирования,
то есть записи информации о работе программы, чтобы отслеживать ее выполнение и находить ошибки или проблемы.

Методы модуля "logging" и его подмодулей:

`getLogger()`: Возвращает объект логгера для указанного имени.
`basicConfig()`: Конфигурирует логгинг с использованием базовых параметров.
`Logger.setLevel()`: Устанавливает уровень логгирования для указанного логгера.
`Logger.addHandler()`: Добавляет обработчик к указанному логгеру.
`Formatter.format()`: Форматирует записи логгера в определенном формате.
`StreamHandler`: Обработчик, который выводит сообщения логгера в поток (например, на консоль).
`FileHandler`: Обработчик, который выводит сообщения логгера в файл.
`RotatingFileHandler`: Обработчик, который выводит сообщения логгера в файл с возможностью
автоматического поворота лог-файла при достижении определенного размера или количества записей.

Наиболее часто используемые методы:

`logging.debug()`: Регистрирует отладочное сообщение.

```python
import logging
logging.debug("This is a debug message")
```

`logging.info()`: Регистрирует информационное сообщение.

```python
import logging
logging.info("This is an info message")
```

`logging.warning()`: Регистрирует предупреждение.

```python
import logging
logging.warning("This is a warning message")
```

`logging.error()`: Регистрирует сообщение об ошибке.

```python
import logging
logging.error("This is an error message")
```

`logging.critical()`: Регистрирует критическое сообщение.

```python
import logging
logging.critical("This is a critical message")
```
""",
                        "posixpath": r"""
Библиотека "posixpath" в Python используется для работы с путями файловой системы в POSIX-совместимых операционных системах.
Она предоставляет функции и методы для манипуляции, анализа и навигации по путям к файлам и директориям.

Методы и подмодули библиотеки "posixpath":

`posixpath.basename(path)`: Возвращает базовое имя файла или директории из заданного пути.
`posixpath.dirname(path)`: Возвращает имя директории из заданного пути.
`posixpath.isabs(path)`: Проверяет, является ли заданный путь абсолютным.
`posixpath.join(path, *paths)`: Объединяет компоненты пути в один.
`posixpath.normcase(path)`: Возвращает нормализованную версию заданного пути с учетом регистра символов.
`posixpath.normpath(path)`: Возвращает нормализованную версию заданного пути с учетом символов ".", ".." и разделителей.
`posixpath.realpath(path)`: Возвращает каноническое имя (полный путь) для заданного пути.
`posixpath.split(path)`: Разделяет заданный путь на имя директории и базовое имя файла или директории.

Некоторые из наиболее часто используемых методов библиотеки "posixpath":

`basename(path)`: Возвращает имя файла из заданного пути.

```python
import posixpath

path = "/home/user/example.txt"
filename = posixpath.basename(path)
print(filename)  # Выводит: example.txt
```

`dirname(path)`: Возвращает имя директории из заданного пути.

```python
import posixpath

path = "/home/user/example.txt"
directory = posixpath.dirname(path)
print(directory)  # Выводит: /home/user
```

`isabs(path)`: Проверяет, является ли заданный путь абсолютным.

```python
import posixpath

path = "/home/user/example.txt"
is_absolute = posixpath.isabs(path)
print(is_absolute)  # Выводит: True
```
""",
                        "gettext": r"""
Библиотека "gettext" в Python используется для локализации и перевода текстовых сообщений в программе. 

# Таблица методов модуля "gettext" и его подмодулей:
### Методы модуля "gettext":
bindtextdomain(domain, directory): устанавливает домен и директорию для поиска файлов перевода.
dgettext(domain, message): возвращает перевод сообщения из указанного домена.
dngettext(domain, singular, plural, n): возвращает перевод множественного сообщения на основе числа n.
gettext(message): возвращает перевод сообщения.
ngettext(singular, plural, n): возвращает перевод множественного сообщения на основе числа n.
textdomain(domain): устанавливает текущий домен перевода.

### Методы подмодуля "gettext.translation":
gettext.translation(domain, localedir=None, languages=None, fallback=False): создает объект перевода на основе заданного домена и директории локализации.
gettext.translation(""): возвращает объект перевода для текущего домена.
add_fallback(translations): добавляет объект перевода в список резервных вариантов перевода.
install(domain, localedir=None, unicode=0): устанавливает объект перевода в качестве текущего.

Самые часто используемые методы библиотеки "gettext" вместе с их кратким описанием и примером кода:

gettext(message): Возвращает перевод сообщения.

```python
import gettext
gettext.bindtextdomain('mydomain', 'locale/')
gettext.textdomain('mydomain')

_ = gettext.gettext
print(_('Hello, world!'))
```

ngettext(singular, plural, n): Возвращает перевод множественного сообщения на основе числа n.

```python
import gettext
gettext.bindtextdomain('mydomain', 'locale/')
gettext.textdomain('mydomain')

_ = gettext.ngettext
print(_('%d apple', '%d apples', 5) % 5)
```

dgettext(domain, message): Возвращает перевод сообщения из указанного домена.

```python
import gettext
gettext.bindtextdomain('mydomain', 'locale/')
gettext.textdomain('mydomain')

_ = gettext.dgettext
print(_('mydomain', 'Hello, world!'))
```
""",
                        "zipfile": r"""
Библиотека "zipfile" в Python используется для работы с архивами формата ZIP.
Она предоставляет функциональность для создания, чтения, обновления и извлечения файлов из архива.

Таблица методов библиотеки "zipfile" и их краткого описания:

`ZipFile(file, mode='r', compression=ZIP_STORED, allowZip64=True)` - создает объект ZipFile, представляющий архив ZIP из файла. Режимы могут быть чтение ('r'), запись ('w') или добавление ('a').
`ZipFile.extractall(path=None, members=None, pwd=None)` - извлекает все файлы из архива в указанную папку.
`ZipFile.extract(member, path=None, pwd=None)` - извлекает конкретный файл из архива.
`ZipFile.namelist()` - возвращает список имен файлов в архиве.
`ZipFile.open(name, mode='r', pwd=None)` - открывает файл в архиве и возвращает объект файлового дескриптора.
`ZipFile.close()` - закрывает объект ZipFile и освобождает ресурсы.

Список самых часто используемых методов, их краткого описания и пример демонстрирующий их работу:

`extractall(path=None, members=None, pwd=None)` - извлекает все файлы из архива в указанную папку.

```python
import zipfile

# Открываем архив
with zipfile.ZipFile('archive.zip', 'r') as zip_ref:
    # Извлекаем все файлы
    zip_ref.extractall('destination_folder')
```

`namelist()` - возвращает список имен файлов в архиве.

```python
import zipfile

# Открываем архив
with zipfile.ZipFile('archive.zip', 'r') as zip_ref:
    # Получаем список имен файлов
    file_names = zip_ref.namelist()
    
    # Выводим список имен файлов
    for name in file_names:
        print(name)
```

`extract(member, path=None, pwd=None)` - извлекает конкретный файл из архива.

```python
import zipfile

# Открываем архив
with zipfile.ZipFile('archive.zip', 'r') as zip_ref:
    # Извлекаем файл с именем 'file.txt'
    zip_ref.extract('file.txt', 'destination_folder')
```
""",
                        "pylab": r"""
Название библиотеки: "pylab"

Краткое описание: Библиотека "pylab" является комбинацией библиотеки "matplotlib" и "NumPy"
для выполнения научных и инженерных вычислений в Python.
Она предоставляет функции для создания графиков, визуализации данных и выполнения математических операций.

Таблица методов:

| Метод                | Описание                                                    |
|----------------------|-------------------------------------------------------------|
| `plot`               | Построить график из данных                                   |
| `scatter`            | Создать точечную диаграмму                                   |
| `hist`               | Построить гистограмму из данных                              |
| `imshow`             | Отобразить изображение                                       |
| `xlabel`             | Задать подпись для оси x                                    |
| `ylabel`             | Задать подпись для оси y                                    |
| `title`              | Задать заголовок графика                                    |
| `legend`             | Вывести легенду графика                                     |
| `grid`               | Отобразить сетку на графике                                 |
| `sin`                | Вычислить синус значения                                     |
| `cos`                | Вычислить косинус значения                                  |
| `exp`                | Вычислить экспоненту значения                               |


Метод `plot` позволяет строить графики из предоставленных данных.
   
```python
import pylab

x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 50]

pylab.plot(x, y)
pylab.show()
```
   
Метод `scatter` используется для создания точечной диаграммы.
   
```python
import pylab

x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 50]

pylab.scatter(x, y)
pylab.show()
```
   
Метод `hist` позволяет создать гистограмму из предоставленных данных.
   
```python
import pylab

data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]

pylab.hist(data)
pylab.show()
```
   
Метод `imshow` используется для отображения изображений.
   
```python
import pylab
import numpy as np

image = np.random.random((10, 10))

pylab.imshow(image)
pylab.show()
```
   
Метод `xlabel` задает подпись для оси x на графике.
   
```python
import pylab

x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 50]

pylab.plot(x, y)
pylab.xlabel("X-axis")
pylab.show()
```
   
Метод `ylabel` задает подпись для оси y на графике.
   
```python
import pylab

x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 50]

pylab.plot(x, y)
pylab.ylabel("Y-axis")
pylab.show()
```
   
Метод `title` задает заголовок для графика.
   
```python
import pylab

x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 50]

pylab.plot(x, y)
pylab.title("My Plot")
pylab.show()
```
   
Метод `legend` выводит легенду на графике.
   
```python
import pylab

x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 50]

pylab.plot(x, y, label="Data")
pylab.legend()
pylab.show()
```
   
Метод `grid` отображает сетку на графике.
   
```python
import pylab

x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 50]

pylab.plot(x, y)
pylab.grid(True)
pylab.show()
```
   
Метод `sin` используется для вычисления синуса значения.
   
```python
import pylab

value = 0.5

result = pylab.sin(value)
print(result)
```
   
Метод `cos` используется для вычисления косинуса значения.
   
```python
import pylab

value = 0.5

result = pylab.cos(value)
print(result)
```
   
Метод `exp` используется для вычисления экспоненты значения.
   
```python
import pylab

value = 2

result = pylab.exp(value)
print(result)
```
""",
                        "optparse": r"""
Библиотека "optparse" используется для обработки командной строки в Python.
Она предоставляет удобные инструменты для определения и разбора аргументов командной строки,
а также для создания гибких и понятных интерфейсов командной строки для ваших программ.

Методы модуля "optparse" и его подмодулей:

OptionParser: Класс, который предоставляет функциональность для определения и разбора аргументов командной строки.
OptionGroup: Класс, позволяющий группировать опции вместе для более удобного использования.
Option: Класс, представляющий отдельную опцию командной строки.
OptionContainer: Базовый класс для группировки опций.
OptionConflictError: Исключение, возникающее при конфликте опций.
OptionValueError: Исключение, возникающее при некорректном значении опции.

Некоторые из самых часто используемых методов "optparse" и их описание:

add_option(): Добавляет опцию в парсер командной строки.

```python
parser.add_option("-f", "--file", dest="filename", help="Specify input file")
```

parse_args(): Разбирает аргументы командной строки и возвращает объект, содержащий значения опций.

```python
(options, args) = parser.parse_args()
```

print_help(): Выводит справку о доступных опциях командной строки.

```python
parser.print_help()
```

error(): Генерирует сообщение об ошибке и выводит справку о доступных опциях командной строки.

```python
parser.error("Input file is required")
```

set_defaults(): Устанавливает значения по умолчанию для опций.

```python
parser.set_defaults(verbose=True)
```
""",
                        "gast": r"""
Библиотека "gast" используется для анализа и модификации абстрактного синтаксического дерева (AST) в Python.
Она предоставляет инструменты для работы с AST, такие как обход узлов дерева, замена узлов, добавление новых узлов и т.д.

Методы модуля "gast" и его подмодулей:

Модуль "gast":
NodeVisitor: Класс для обхода узлов AST.
NodeTransformer: Класс для модификации узлов AST.
parse: Функция для преобразования исходного кода в AST.


NodeVisitor: Класс, который позволяет обойти все узлы AST и выполнить определенные действия для каждого узла.

```python
from gast import NodeVisitor

class MyVisitor(NodeVisitor):
    def visit_FunctionDef(self, node):
        print("Found a function definition:", node.name)

# Создание экземпляра класса и обход AST
visitor = MyVisitor()
visitor.visit(ast_tree)
```

NodeTransformer: Класс, который позволяет модифицировать узлы AST путем замены, добавления или удаления узлов.

```python
from gast import NodeTransformer

class MyTransformer(NodeTransformer):
    def visit_FunctionDef(self, node):
        # Изменение имени функции
        node.name = "new_function_name"
        return node

# Создание экземпляра класса и модификация AST
transformer = MyTransformer()
new_ast_tree = transformer.visit(ast_tree)
```

parse: Функция, которая преобразует исходный код в AST.

```python
from gast import parse

source_code = "print('Hello, World!')"
ast_tree = parse(source_code)
```
""",
                        "keyword": r"""
Библиотека "keyword" в Python используется для работы с ключевыми словами языка.
Она предоставляет набор функций для проверки и манипуляции ключевыми словами, такими как "if", "for", "while" и другими.

Таблица методов модуля "keyword":
iskeyword(): Проверяет, является ли переданная строка ключевым словом в Python.
kwlist: Возвращает список всех ключевых слов в Python.

iskeyword():

```python
import keyword
print(keyword.iskeyword('if'))  # Вывод: True
print(keyword.iskeyword('hello'))  # Вывод: False
```

iskeyword(): Позволяет проверить, является ли строка ключевым словом Python.
kwlist: Возвращает список всех ключевых слов в Python.
""",
                        "poplib": r"""
Библиотека "poplib" в Python используется для работы с протоколом почтового ящика на основе протокола POP3 (Post Office Protocol version 3).
Она позволяет получать электронные письма, удалять их, и выполнять другие операции взаимодействия с почтовым сервером.

Методы и подмодули библиотеки "poplib":

`poplib.POP3(host[, port])`: Создает объект соединения с почтовым сервером POP3 на указанном хосте и порту.
`poplib.POP3.user(username)`: Аутентифицирует пользователя на сервере, указывая имя пользователя.
`poplib.POP3.pass_(password)`: Аутентифицирует пользователя на сервере, указывая пароль.
`poplib.POP3.stat()`: Возвращает информацию о состоянии почтового ящика, включая количество сообщений и общий размер.
`poplib.POP3.list([which])`: Возвращает список всех сообщений в почтовом ящике, или информацию о конкретном сообщении, если указан параметр "which".
`poplib.POP3.retr(which)`: Получает содержимое указанного сообщения из почтового ящика.
`poplib.POP3.dele(which)`: Отмечает указанное сообщение для удаления.
`poplib.POP3.quit()`: Закрывает соединение с сервером POP3.

Наиболее часто используемые методы в библиотеке "poplib":

`poplib.POP3(host[, port])`: Создание соединения с почтовым сервером.
`poplib.POP3.user(username)` и `poplib.POP3.pass_(password)`: Аутентификация пользователя на сервере.
`poplib.POP3.stat()`: Получение информации о состоянии почтового ящика.
`poplib.POP3.list()`: Получение списка всех сообщений в почтовом ящике.
`poplib.POP3.retr(which)`: Получение содержимого конкретного сообщения.
`poplib.POP3.quit()`: Закрытие соединения с сервером POP3.

Пример использования метода `poplib.POP3(user, password)` для создания соединения с почтовым сервером:

```python
import poplib

pop_server = poplib.POP3("mail.example.com", 110)
pop_server.user("your_username")
pop_server.pass_("your_password")
```
""",
                        "base64": r"""
Библиотека "base64" в Python используется для кодирования и декодирования данных в формате base64.
Base64 является способом представления двоичных данных в виде текста, что удобно для передачи и хранения данных,
которые не могут быть безопасно переданы в обычном двоичном формате.

Методы модуля "base64" и его подмодулей:

Модуль "base64":
b64encode(data): Кодирует данные в формате base64.
b64decode(data): Декодирует данные из формата base64.
b64encodebytes(data): Кодирует данные в формате base64 и возвращает байтовую строку.
b64decodebytes(data): Декодирует байтовую строку из формата base64 и возвращает декодированные данные.

Подмодуль "base64.urlsafe":
urlsafe_b64encode(data): Кодирует данные в формате base64 для URL без использования символов, которые могут вызывать проблемы в URL.
urlsafe_b64decode(data): Декодирует данные из формата base64 для URL.

Некоторые из самых часто используемых методов "base64" и их краткое описание:

b64encode(data): Кодирует данные в формате base64.

```python
import base64

data = b'Hello, World!'
encoded_data = base64.b64encode(data)
print(encoded_data)
```

b64decode(data): Декодирует данные из формата base64.

```python
import base64

encoded_data = b'SGVsbG8sIFdvcmxkIQ=='
decoded_data = base64.b64decode(encoded_data)
print(decoded_data)
```

urlsafe_b64encode(data): Кодирует данные в формате base64 для URL без использования символов, которые могут вызывать проблемы в URL.

```python
import base64

data = b'Hello, World!'
encoded_data = base64.urlsafe_b64encode(data)
print(encoded_data)
```

urlsafe_b64decode(data): Декодирует данные из формата base64 для URL.

```python
import base64

encoded_data = b'SGVsbG8sIFdvcmxkIQ=='
decoded_data = base64.urlsafe_b64decode(encoded_data)
print(decoded_data)
```
""",
                        "shlex": r"""
Библиотека "shlex" в Python используется для разбивки строки на токены в соответствии с синтаксисом оболочки Unix.
Она часто применяется при работе с командной строкой, парсинге аргументов командной строки и анализе ввода пользователя.

Методы модуля и их мега краткое описание:

shlex.split(s): Разбивает строку s на токены и возвращает список.
shlex.quote(s): Возвращает квотированную версию строки s с учетом синтаксиса оболочки.
shlex.join(args): Объединяет список аргументов args в одну строку с добавлением кавычек и экранированием.
shlex.shlex([stream[, filename[, posix]]]): Создает объект парсера токенов для чтения из потока stream.
    Опциональные параметры filename и posix устанавливают соответствующие атрибуты парсера.
shlex.push_source(source): Вставляет новый источник токенов в стек парсера.
shlex.pop_source(): Удаляет верхний источник токенов из стека парсера.
shlex.get_token(): Возвращает следующий токен из текущего источника парсера.
shlex.get_token_unquoted(): Возвращает следующий неквотированный токен из текущего источника парсера.

Наиболее часто используемые методы "shlex" вместе с их кратким описанием и примерным кодом:

shlex.split(s): Разбивает строку на токены и возвращает список.
Пример: tokens = shlex.split("hello world")  # ['hello', 'world']

shlex.quote(s): Возвращает квотированную версию строки с учетом синтаксиса оболочки.
Пример: quoted = shlex.quote("Hello, World!")  # 'Hello, World!'

shlex.join(args): Объединяет список аргументов в строку с добавлением кавычек и экранированием.
Пример: command = shlex.join(["ls", "-l", "*.txt"])  # 'ls -l "*.txt"'
""",
                        "concurrent": r"""
Библиотека "concurrent" в Python используется для реализации параллельного выполнения задач и управления потоками и процессами.

Методы и подмодули библиотеки "concurrent":

concurrent.futures: Предоставляет высокоуровневый интерфейс для асинхронного выполнения задач.
concurrent.futures.ThreadPoolExecutor: Позволяет создавать пул потоков для параллельного выполнения задач.
concurrent.futures.ProcessPoolExecutor: Позволяет создавать пул процессов для параллельного выполнения задач.
concurrent.futures.as_completed: Возвращает итератор, который возвращает результаты задач по мере их завершения.
concurrent.futures.wait: Ожидает завершения задач и возвращает кортеж с завершенными и незавершенными задачами.
concurrent.futures.Future: Представляет отложенный результат выполнения задачи.

Некоторые из самых часто используемых методов библиотеки "concurrent" в Python:

submit(fn, *args, **kwargs): Подает задачу на выполнение в пул потоков или процессов.

```python
import concurrent.futures

def square(x):
    return x ** 2

with concurrent.futures.ThreadPoolExecutor() as executor:
    future = executor.submit(square, 5)
    result = future.result()
    print(result)  # Output: 25
```

map(fn, *iterables, timeout=None): Применяет функцию к каждому элементу итерируемых объектов и возвращает результаты в том же порядке.

```python
import concurrent.futures

def square(x):
    return x ** 2

with concurrent.futures.ThreadPoolExecutor() as executor:
    numbers = [1, 2, 3, 4, 5]
    results = executor.map(square, numbers)
    print(list(results))  # Output: [1, 4, 9, 16, 25]
```

shutdown(wait=True): Завершает работу пула потоков или процессов.

```python
import concurrent.futures

with concurrent.futures.ThreadPoolExecutor() as executor:
    # Выполнение задач
    executor.shutdown()
```
""",
                        "keyboard": r"""
Библиотека "keyboard" используется для управления клавиатурой компьютера с помощью кода на языке Python.
Она позволяет эмулировать нажатия клавиш, считывать нажатия клавиш в реальном времени и манипулировать состоянием клавиш.

Таблица методов модуля "keyboard" и его подмодулей:

Метод                   | Описание
-----------------------|-----------------------
keyboard.press()       | Эмулирует нажатие заданной клавиши.
keyboard.release()     | Освобождает заданную клавишу после её нажатия.
keyboard.is_pressed()  | Проверяет, нажата ли заданная клавиша.
keyboard.write()       | Вводит заданный текст на клавиатуре.
keyboard.add_hotkey()  | Регистрирует горячую клавишу и связанный с ней обработчик.
keyboard.wait()        | Приостанавливает выполнение программы до нажатия заданной клавиши.
keyboard.unhook_all()  | Отключает все горячие клавиши.

Список самых часто используемых методов библиотеки "keyboard":

keyboard.press(): эмулирует нажатие клавиши.

```python
import keyboard

keyboard.press('A')  # Нажатие клавиши "A"
```

keyboard.release(): освобождает заданную клавишу после её нажатия.

```python
import keyboard

keyboard.release('A')  # Освобождение клавиши "A"
```

keyboard.is_pressed(): проверяет, нажата ли заданная клавиша.

```python
import keyboard

if keyboard.is_pressed('A'):  # Проверка, нажата ли клавиша "A"
    print("Клавиша A нажата")
```
""",
                        "rlcompleter": r"""
Библиотека "rlcompleter" используется для автоматического завершения кода в интерактивной оболочке Python (REPL) с помощью клавиши Tab.
Она обеспечивает поддержку автозаполнения имён модулей, функций, переменных и атрибутов.
   
Методы и подмодули библиотеки "rlcompleter":
Submodule: `rlcompleter`
Метод `Completer(...)` - инициализирует объект автозавершения для использования в REPL.
Метод `Completer.complete(text, state)` - выполняет автозавершение указанного текста в заданном состоянии.
Метод `Completer.global_matches(text)` - возвращает список всех глобальных имен, соответствующих указанному тексту.
     
Метод `Completer.complete(text, state)` - данный метод выполняет автозавершение текста `text` в конкретном состоянии `state`.
     
```python
import rlcompleter

completer = rlcompleter.Completer()
text = 'pr'
state = 0

completions = completer.complete(text, state)
print(completions)
```
   
Метод `Completer.global_matches(text)` - данный метод возвращает список глобальных имен, которые соответствуют указанному тексту `text`.
     
```python
import rlcompleter

completer = rlcompleter.Completer()
text = 'pr'

matches = completer.global_matches(text)
print(matches)
```
""",
                        "psutil": r"""
Библиотека "psutil" в Python используется для доступа и управления информацией о системе и процессах.
Она предоставляет функции для получения информации о процессоре, памяти, дисках, сети и др.
Это полезно для мониторинга системы, оптимизации ресурсов и отладки.



| Метод                  | Описание                              |
|-----------------------|---------------------------------------|
| psutil.cpu_percent()  | Возвращает процент использования ЦП   |
| psutil.virtual_memory()  | Возвращает информацию о виртуальной памяти   |
| psutil.disk_usage()  | Возвращает использование дискового пространства   |
| psutil.net_io_counters()  | Возвращает сетевые счетчики ввода-вывода   |
| psutil.process_count()  | Возвращает количество запущенных процессов   |



psutil.cpu_percent(): Возвращает текущий процент использования CPU в виде числа от 0 до 100.

```python
import psutil

cpu_percent = psutil.cpu_percent()
print("Текущий процент использования CPU:", cpu_percent)
```

psutil.virtual_memory(): Возвращает информацию о виртуальной памяти в виде объекта.
Можно получить доступ к атрибутам, таким как "total" (всего памяти), "available" (доступно памяти), "used" (используется памяти) и др.

```python
import psutil

virtual_memory = psutil.virtual_memory()
print("Общая доступная память:", virtual_memory.total)
print("Доступная память:", virtual_memory.available)
print("Используется памяти:", virtual_memory.used)
```

psutil.disk_usage(): Возвращает информацию об использовании дискового пространства для указанного пути в виде объекта.
Можно получить доступ к атрибутам, таким как "total" (всего пространства),
"used" (используется пространство), "free" (свободное пространство) и др.

```python
import psutil

disk_usage = psutil.disk_usage("/")
print("Общее пространство диска:", disk_usage.total)
print("Используется пространства диска:", disk_usage.used)
print("Свободное пространство диска:", disk_usage.free)
```

psutil.net_io_counters(): Возвращает сетевые счетчики ввода-вывода в виде объекта.
Можно получить доступ к атрибутам, таким как "bytes_sent" (отправленные байты), "bytes_recv" (полученные байты), "packets_sent" (отправленные пакеты) и др.

```python
import psutil

net_io_counters = psutil.net_io_counters()
print("Отправленные байты:", net_io_counters.bytes_sent)
print("Полученные байты:", net_io_counters.bytes_recv)
```

psutil.process_count(): Возвращает количество текущих запущенных процессов.

```python
import psutil

process_count = psutil.process_count()
print("Количество запущенных процессов:", process_count)
```
""",
                        "rfc3339_validator": r"""
Библиотека "rfc3339_validator" используется для проверки правильности формата даты и времени в соответствии со стандартом RFC 3339.

Таблица методов модуля и его подмодулей:

Метод `validate(date_string)` - проверяет правильность формата даты и времени в строке `date_string` в соответствии со стандартом RFC 3339.
Возвращает булевое значение True, если формат верен, и False в противном случае.

Список самых частых методов, их краткого описания и примерного кода:

Метод `validate(date_string)` - проверяет правильность формата даты и времени в строке `date_string` в соответствии со стандартом RFC 3339.

```python
from rfc3339_validator import validate

date_string = "2022-01-01T12:34:56Z"
if validate(date_string):
    print("Формат даты и времени верный")
else:
    print("Некорректный формат даты и времени")
```
""",
                        "regcheck": r"""
Библиотека "regcheck" используется для работы с регулярными выражениями в Python.
Она предоставляет инструменты для поиска и сравнения строк, основываясь на заданных шаблонах.

Таблица методов и их краткое описание для модуля "regcheck":

Метод         | Описание
------------- | -------------
search        | Выполняет поиск заданного регулярного выражения в строке и возвращает первое совпадение.
match         | Проверяет, соответствует ли вся строка заданному регулярному выражению.
findall       | Находит все совпадения заданного регулярного выражения в строке и возвращает их в виде списка.
finditer      | Находит все совпадения заданного регулярного выражения в строке и возвращает их в виде итератора.
split         | Разделяет строку на подстроки, используя заданное регулярное выражение в качестве разделителя.
sub           | Заменяет все совпадения заданного регулярного выражения в строке указанным значением.

Список самых часто используемых методов, их краткое описание и примерный код для демонстрации их работы:

Метод      | Описание                            | Примерный код
---------- | ----------------------------------- | -------------
search     | Ищет первое совпадение в строке      | import re \n result = re.search(r"pattern", string)
findall    | Находит все совпадения в строке       | import re \n results = re.findall(r"pattern", string)
split      | Разделяет строку на подстроки         | import re \n parts = re.split(r"\s", string)
sub        | Заменяет совпадения в строке          | import re \n new_string = re.sub(r"pattern", replacement, string)
""",
                        "posix": r"""
Библиотека "posix" в Python используется для взаимодействия с функциями и операциями,
специфичными для POSIX-совместимых операционных систем, таких как Linux и macOS.

Таблица методов модуля "posix" и его подмодулей и краткое описание:

Модуль "posix":
getpid(): Возвращает идентификатор текущего процесса.
getuid(): Возвращает идентификатор пользователя текущего процесса.
getgid(): Возвращает идентификатор группы текущего процесса.
chmod(path, mode): Изменяет права доступа к файлу или директории.
chown(path, uid, gid): Изменяет владельца и группу файловой системы.
getcwd(): Возвращает текущую рабочую директорию.
listdir(path): Возвращает список файлов и директорий в указанной директории.

Подмодуль "posixpath":
join(path1, path2): Объединяет два пути в один.
isfile(path): Проверяет, является ли путь файлом.
isdir(path): Проверяет, является ли путь директорией.
basename(path): Возвращает базовое имя последнего компонента пути.
dirname(path): Возвращает каталог пути.

Список часто используемых методов, их краткое описание и

getpid(): Возвращает идентификатор текущего процесса.

```python
import os
print(os.getpid())
```

getcwd(): Возвращает текущую рабочую директорию.

```python
import os
print(os.getcwd())
```

listdir(path): Возвращает список файлов и директорий в указанной директории.

```python
import os
print(os.listdir("/path/to/directory"))
```
""",
                        "fileinput": r"""
Библиотека "fileinput" используется для обработки текстовых файлов в Python.
Она предоставляет удобные инструменты для чтения и обработки содержимого файлов.

Методы модуля "fileinput" и его подмодулей:

input(): Возвращает итератор, который построчно читает файлы.
filename(): Возвращает текущее имя файла.
lineno(): Возвращает текущий номер строки файла.
filelineno(): Возвращает текущий номер строки относительно текущего файла.
isfirstline(): Проверяет, является ли текущая строка первой в файле.
isstdin(): Проверяет, читается ли текущая строка с stdin.
nextfile(): Переходит к следующему файлу.
close(): Закрывает файлы, открытые с помощью fileinput.

Некоторые из самых часто используемых методов библиотеки "fileinput" вместе с кратким описанием и примером кода:

input(): Возвращает итератор для построчного чтения файлов.

```python
import fileinput

for line in fileinput.input():
    print(line)
```

filename(): Возвращает текущее имя файла.

```python
import fileinput

for line in fileinput.input():
    print(f"Current file: {fileinput.filename()}")
```

lineno(): Возвращает текущий номер строки файла.

```python
import fileinput

for line in fileinput.input():
    print(f"Line number: {fileinput.lineno()}")
```
""",
                        "pygetwindow": r"""
Библиотека "pygetwindow" используется для управления окнами в операционной системе с помощью Python.
Она предоставляет функции для поиска, получения информации о размерах и позиции окон, а также для управления их видимостью и активностью.

Методы и подмодули библиотеки "pygetwindow":

`getAllTitles()`: Возвращает список заголовков всех открытых окон.
`getWindowsWithTitle(title)`: Возвращает список окон с указанным заголовком.
`getWindowGeometry(window)`: Возвращает геометрию (размеры и позицию) указанного окна.
`getWindowAt(x, y)`: Возвращает окно, находящееся по указанным координатам.
`getActiveWindow()`: Возвращает активное окно.
`getWindowBorders(window)`: Возвращает границы указанного окна.
`getWindowRect(window)`: Возвращает прямоугольник, охватывающий указанное окно.
`getWindowPID(window)`: Возвращает идентификатор процесса, связанного с указанным окном.
`getWindowProcessID(window)`: Возвращает идентификатор процесса, связанного с указанным окном.
`getWindowThreadID(window)`: Возвращает идентификатор потока, связанного с указанным окном.
`getWindowThreadProcessId(window)`: Возвращает идентификатор потока и процесса, связанных с указанным окном.
`getWindowThreadProcessId(window)`: Возвращает идентификатор потока и процесса, связанных с указанным окном.
`getWindowThreadProcessId(window)`: Возвращает идентификатор потока и процесса, связанных с указанным окном.
`getWindowThreadProcessId(window)`: Возвращает идентификатор потока и процесса, связанных с указанным окном.
`getWindowThreadProcessId(window)`: Возвращает идентификатор потока и процесса, связанных с указанным окном.
`getWindowThreadProcessId(window)`: Возвращает идентификатор потока и процесса, связанных с указанным окном.

Некоторые из самых часто используемых методов библиотеки "pygetwindow":

`getAllTitles()`: Возвращает список заголовков всех открытых окон.

```python
import pygetwindow

window_titles = pygetwindow.getAllTitles()
print(window_titles)
```

`getWindowsWithTitle(title)`: Возвращает список окон с указанным заголовком.

```python
import pygetwindow

windows = pygetwindow.getWindowsWithTitle("Notepad")
for window in windows:
    print(window.title)
```

`getActiveWindow()`: Возвращает активное окно.

```python
import pygetwindow

active_window = pygetwindow.getActiveWindow()
print(active_window.title)
```

`getWindowGeometry(window)`: Возвращает геометрию (размеры и позицию) указанного окна.

```python
import pygetwindow

window = pygetwindow.getWindowsWithTitle("Notepad")[0]
geometry = pygetwindow.getWindowGeometry(window)
print(geometry)
```

`getWindowRect(window)`: Возвращает прямоугольник, охватывающий указанное окно.

```python
import pygetwindow

window = pygetwindow.getWindowsWithTitle("Notepad")[0]
rect = pygetwindow.getWindowRect(window)
print(rect)
```
""",
                        "warnings": r"""
Библиотека "warnings" в Python используется для управления предупреждениями, которые могут возникать во время выполнения программы.
Она позволяет контролировать вывод предупреждений и принимать соответствующие действия.

Методы и подмодули библиотеки "warnings":

`warn(message, warning_type, stacklevel)` - генерирует предупреждение с указанным сообщением, типом предупреждения и уровнем стека.
`filterwarnings(action, message, category, module, lineno, append)` - устанавливает фильтр для предупреждений, определяя действие, текст сообщения, категорию предупреждения, модуль, номер строки и флаг добавления фильтра.
`simplefilter(action, category=Warning, lineno=0, append=False)` - устанавливает простой фильтр для предупреждений с указанным действием, категорией, номером строки и флагом добавления фильтра.
`resetwarnings()` - сбрасывает все установленные фильтры предупреждений.
`showwarning(message, category, filename, lineno, file=None, line=None)` - выводит предупреждение с указанным сообщением, категорией, исходным файлом, номером строки, файлом вывода и строкой кода.
`catch_warnings(*, record=False, module=None)` - возвращает контекстный менеджер для временного перехвата предупреждений с опциональной записью в список или указанный модуль.

`warn(message, warning_type, stacklevel)` - генерирует предупреждение с заданным сообщением, типом предупреждения и уровнем стека.
   
```python
import warnings

warnings.warn("This is a warning message", UserWarning, stacklevel=2)
```
     
`filterwarnings(action, message, category, module, lineno, append)` - устанавливает фильтр для предупреждений с указанными параметрами.
   
```python
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning, module="my_module")
```
     
`simplefilter(action, category=Warning, lineno=0, append=False)` - устанавливает простой фильтр для предупреждений с указанным действием и категорией.
   
```python
import warnings

warnings.simplefilter("ignore", DeprecationWarning)
```
     
`resetwarnings()` - сбрасывает все установленные фильтры предупреждений.
   
```python
import warnings

warnings.resetwarnings()
```
     
`showwarning(message, category, filename, lineno, file=None, line=None)` - выводит предупреждение с указанными параметрами.
   
```python
import warnings

warnings.showwarning("This is a warning message", UserWarning, "example.py", 10)
```
     
`catch_warnings(*, record=False, module=None)` - контекстный менеджер для временного перехвата предупреждений.
   
```python
import warnings

with warnings.catch_warnings(record=True) as w:
    warnings.warn("This is a warning message")
    print(w[0].message)
```
""",
                        "nt": r"""
Библиотека "nt" в Python используется для работы с функциями операционной системы Windows.

Методы модуля "nt" и его подмодулей:

Модуль "nt":
nt.getcwd(): Возвращает текущую рабочую директорию.
nt.listdir(path): Возвращает список файлов и директорий в указанном пути.
nt.mkdir(path): Создает новую директорию по указанному пути.
nt.remove(path): Удаляет файл по указанному пути.
nt.rename(src, dst): Переименовывает файл или директорию.
nt.system(command): Выполняет команду операционной системы.

Подмодуль "ntpath":
ntpath.basename(path): Возвращает имя файла или директории из указанного пути.
ntpath.dirname(path): Возвращает имя директории из указанного пути.
ntpath.exists(path): Проверяет, существует ли файл или директория по указанному пути.
ntpath.join(path, *paths): Объединяет пути в один.
ntpath.split(path): Разделяет путь на имя директории и имя файла.

Некоторые часто используемые методы и их описание:

nt.getcwd(): Возвращает текущую рабочую директорию.

```python
import nt
current_dir = nt.getcwd()
print(current_dir)
```

nt.listdir(path): Возвращает список файлов и директорий в указанном пути.


```python
import nt
file_list = nt.listdir("C:/Users")
print(file_list)
```

nt.mkdir(path): Создает новую директорию по указанному пути.

```python
import nt
nt.mkdir("C:/Users/NewDirectory")
```

nt.remove(path): Удаляет файл по указанному пути.

```python
import nt
nt.remove("C:/Users/example.txt")
```

nt.rename(src, dst): Переименовывает файл или директорию.

```python
import nt
nt.rename("C:/Users/old_name.txt", "C:/Users/new_name.txt")
```

nt.system(command): Выполняет команду операционной системы.

```python
import nt
nt.system("dir")
```
""",
                        "netbios": r"""
"netbios" - это библиотека в Python, которая предоставляет функциональность
для работы с протоколом NetBIOS (Network Basic Input/Output System).

Таблица методов модуля "netbios" и их краткого описания:

Метод                  | Описание
-----------------------|----------------------------------------------------
nbt.getnetbiosname()   | Получает NetBIOS-имя компьютера, на котором выполняется код.
nbt.getwinsaddrs()     | Возвращает список IP-адресов машин, знающих сведения о NetBIOS-именах.
nbt.getnodetype()      | Возвращает тип узла в сети.
nbt.gethostbyname()    | Возвращает IP-адреса, связанные с указанным NetBIOS-именем.
nbt.getbcastaddrs()    | Возвращает список широковещательных адресов, связанных с NetBIOS-именами.

Список самых часто используемых методов, их краткого описания и

nbt.getnetbiosname(): Возвращает NetBIOS-имя компьютера. 

```python
import netbios as nb

name = nb.getnetbiosname()
print(name)
```

nbt.getwinsaddrs(): Возвращает список IP-адресов машин, знающих сведения о NetBIOS-именах.

```python
import netbios as nb

wins_addrs = nb.getwinsaddrs()
print(wins_addrs)
```

nbt.getnodetype(): Возвращает тип узла в сети.

```python
import netbios as nb

node_type = nb.getnodetype()
print(node_type)
```
""",
                        "frozenlist": r"""
Описание: библиотека "frozenlist" служит для создания неизменяемых списков в Python,
аналогично тому, как `tuple` предоставляет неизменяемую версию `list`.

Таблица методов:

| Метод	    | Описание  |
|---------	|-----------|
| `__init__()` | Инициализирует новый объект frozenlist.|
| `__contains__()` | Проверяет наличие элемента в списке.|
| `__getitem__()` | Получает элемент списка по индексу.|
| `__len__()` | Возвращает количество элементов в списке.|
| `copy()` | Возвращает копию frozenlist.|

Список самых частых методов, краткое описание и работающие примеры:

```python
# Метод __init__()
flist = frozenlist([1, 2, 3, 4, 5])
# Метод __contains__()
print(3 in flist)  # Выведет True, так как 3 есть в списке
# Метод __getitem__()
print(flist[1])  # Выведет 2, так как это элемент на позиции 1
# Метод __len__()
print(len(flist))  # Выведет 5, так количество элементов в списке равно 5
# Метод copy()
flist_copy = flist.copy()  # Создаст копию списка
```

Пожалуйста, убедитесь, что установлена библиотека `frozenlist`.
Если нет, используйте данную команду для установки - `pip install frozenlist`.
""",
                        "bdb": r"""
Библиотека "bdb" используется в Python для создания отладочных средств и выполнения шагов отладки в программном коде.
Она обеспечивает возможности трассировки исполнения и отладки программ на уровне исходного кода.

| Метод          | Описание                               |
|----------------|----------------------------------------|
| run            | Запускает выполнение программы          |
| set_trace      | Устанавливает точку остановки           |
| clear_all_breaks | Удаляет все установленные точки остановки |
| breakpoint     | Устанавливает точку остановки на текущей позиции |
| set_break      | Устанавливает точку остановки по указанной линии кода |
| clear_break    | Удаляет точку остановки на указанной линии кода |
| get_break      | Возвращает информацию о точке остановки |
| break_here     | Развивает точку остановки и печатает справочные сообщения |
| start          | Запускает процесс отладки               |



set_trace: Устанавливает точку остановки и передает управление в режим интерактивной отладки.

```python
import bdb

def some_function():
    a = 10
    bdb.set_trace()  # Установка точки остановки
    print(a)

some_function()
```
run: Запускает выполнение программы до достижения точки остановки или завершения выполнения.

```python
import bdb

def some_function():
    a = 10
    bdb.set_trace()  # Установка точки остановки
    print(a)

bdb.run('some_function()')
```
breakpoint: Устанавливает точку остановки на текущей позиции выполнения кода.

```python
import bdb

def some_function():
    a = 10
    bdb.breakpoint()  # Установка точки остановки
    print(a)

some_function()
```
""",
                        "fcntl": r"""
Библиотека "fcntl" в Python используется для обращения к системным вызовам управления файловыми дескрипторами и флагами файлового управления.

Методы модуля "fcntl" включают:

fcntl.flock(fd, operation): Блокирует или разблокирует файловый дескриптор при помощи операции блокировки.
fcntl.ioctl(fd, request, arg): Вызывает системный вызов IOCTL для управления устройством, связанным с файловым дескриптором.
fcntl.fcntl(fd, command, arg): Выполняет команду файлового управления на файловом дескрипторе, такую как получение или изменение флагов управления файла.
и другие...

Некоторые из наиболее распространенных методов "fcntl" включают:

fcntl.flock(fd, operation) Блокирует или разблокирует файловый дескриптор.

```python
import fcntl

file_descriptor = open("file.txt", "w")
fcntl.flock(file_descriptor, fcntl.LOCK_EX)
# Выполните операции с заблокированным файлом
fcntl.flock(file_descriptor, fcntl.LOCK_UN)
file_descriptor.close()
```

fcntl.ioctl(fd, request, arg) Выполняет системный вызов IOCTL для управления устройством.

```python
import fcntl

file_descriptor = open("/dev/sda", "r")
request_code = 123  # Код запроса, связанный с устройством
arg = 456  # Аргумент IOCTL
fcntl.ioctl(file_descriptor, request_code, arg)
file_descriptor.close()
```

fcntl.fcntl(fd, command, arg) Выполняет команду файлового управления на файловом дескрипторе.

```python
import fcntl

file_descriptor = open("file.txt", "r")
command = fcntl.F_GETFL  # Получить флаги управления файла
flags = fcntl.fcntl(file_descriptor, command, 0)
print(flags)
file_descriptor.close()
```
""",
                    },
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
                    "datetime": """
<img alt="datetime.png" src="Языки\Python\Библиотеки\datetime.png">
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
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
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
                    "aalib": """
aalib - это библиотека для создания ASCII-графики из изображений. Она преобразует изображения в искусственные изображения, составленные из символов ASCII.

| Метод                            | Описание                                                             |
|----------------------------------|----------------------------------------------------------------------|
| aalib.AsciiArt                   | Создает объект AsciiArt для конвертации изображений в ASCII-графику. |
| AsciiArt.render(image)           | Преобразует изображение в ASCII-графику.                             |
| AsciiArt.render_to_memory(image) | Возвращает ASCII-графику в виде строки.                              |
| AsciiArt.save(filename, image)   | Сохраняет ASCII-графику в файл.                                      |


**render(image)** - Преобразует изображение в ASCII-графику.

```python
import aalib
import Image  # Предполагается, что у вас уже есть изображение под названием "image.jpg"

img = Image.open("image.jpg").convert('L')
width, height = img.size
ascii_img = aalib.AsciiArt(width=width, height=height)
ascii_img.render(img)
ascii_img.save("output.txt")
```

**render_to_memory(image)** - Возвращает ASCII-графику в виде строки.

```python
import aalib
import Image

img = Image.open("image.jpg").convert('L')
ascii_img = aalib.AsciiArt(width=80, height=40)
ascii_str = ascii_img.render_to_memory(img)
print(ascii_str)
```

**save(filename, image)** - Сохраняет ASCII-графику в файл.

```python
import aalib
import Image

img = Image.open("image.jpg").convert('L')
ascii_img = aalib.AsciiArt(width=80, height=40)
ascii_img.render(img)
ascii_img.save("output.txt", img)
```
""",
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

```bash
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

```bash
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

```bash
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

```bash
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

```bash
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

```bash
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

```bash
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

```text
add 5 3
```

Затем, чтобы запустить скрипт, нужно использовать команду

```bash
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

```bash
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

```bash
python script.py command_a 5
```

или

```bash
python script.py command_b --bar test
```
""",
                    "bz2": """
Модуль bz2 в Python предоставляет интерфейс для сжатия и распаковки данных
с использованием алгоритма BZ2 (Burrows-Wheeler).
Он позволяет работать с файлами и байтовыми объектами, обеспечивая эффективное сжатие данных.

| Метод                                                     | Описание                                                                           |
|-----------------------------------------------------------|------------------------------------------------------------------------------------|
| bz2.compress(data, compresslevel=9)                       | Сжимает данные BZ2. Можно указать уровень сжатия (1-9).                            |
| bz2.decompress(data)                                      | Распаковывает данные BZ2.                                                          |
| bz2.BZ2File(file, mode='r', buffering=0, compresslevel=9) | Создает файловый объект BZ2. Режимы: 'r' (чтение), 'w' (запись), 'a' (добавление). |

**bz2.compress(data, compresslevel=9)** Сжимает данные BZ2.

```python
compressed_data = bz2.compress(b"Hello, World!")
print(compressed_data)
```

**bz2.decompress(data)** Распаковывает данные BZ2.

```python
decompressed_data = bz2.decompress(compressed_data)
print(decompressed_data)
```
""",
                    "cycler": """
Библиотека cycler в Python используется для создания циклических стилей,
особенно в контексте графиков и диаграмм в библиотеке Matplotlib.

| Метод         | Описание                                                  |
|---------------|-----------------------------------------------------------|
| cycler.cycler | Создает новый циклический объект с заданными параметрами. |

```python
from cycler import cycler

colors = cycler(color=['red', 'green', 'blue'])
linestyles = cycler(linestyle=['-', '--', '-.'])

# Комбинирование циклических стилей
combined_styles = colors + linestyles
```
""",
                },
                "Python": {
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
                    "setuptools": """
| Метод                     | Описание                                                     |
|---------------------------|--------------------------------------------------------------|
| setup()                   | Определяет настройки проекта и его зависимости.              |
| find_packages()           | Автоматически находит и включает все пакеты проекта.         |
| find_namespace_packages() | Аналогично find_packages(), но для пространств имен.         |
| setup_requires            | Зависимости, необходимые для установки проекта.              |
| install_requires          | Зависимости, необходимые для работы проекта.                 |
| entry_points              | Позволяет определить точки входа (entry points) для проекта. |

**setup()**

Описание: Определяет основные настройки проекта и его зависимости.


```python
from setuptools import setup

setup(
    name='mypackage',
    version='1.0.0',
    packages=['mypackage'],
    install_requires=['requests'],
)
```

**find_packages()**

Описание: Автоматически находит и включает все пакеты проекта.

```python
from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='1.0.0',
    packages=find_packages(),
)
```

**entry_points**

Описание: Позволяет определить точки входа (entry points) для проекта, например, для создания скриптов командной строки.

```python
from setuptools import setup

setup(
    name='mypackage',
    version='1.0.0',
    entry_points={
        'console_scripts': [
            'myscript = mypackage.script:main',
        ],
    },
)
```
""",
                    "tabnanny": """
Модуль tabnanny в Python используется для проверки исходных файлов
на наличие проблем с табуляцией, которые могут вызвать синтаксические ошибки.

| Метод                  | Описание                                               |
|------------------------|--------------------------------------------------------|
| process_tokens(tokens) | Проверяет токены файла на проблемы с табуляцией.       |
| NannyToken(token)      | Конструктор класса токенов, используемый для проверки. |

**process_tokens(tokens)** Проверяет токены файла на наличие проблем с табуляцией.

```python
import tokenize
from tabnanny import process_tokens

with open('file.py', 'rb') as f:
    tokens = tokenize.generate_tokens(f.readline)
    process_tokens(tokens)
```

**NannyToken(token)** Конструктор класса токенов, используемый для проверки.

```python
from tabnanny import NannyToken

token = (1, '    ', (0, 0), (0, 0), '    ')  # Пример токена с проблемой
nanny_token = NannyToken(token)
print(nanny_token)
```
""",
                    "atexit": """
Модуль atexit в Python предоставляет возможность регистрации функций,
которые будут выполнены при завершении программы.
Это позволяет управлять завершением программы и выполнением дополнительных действий перед выходом.

| Метод/Подмодуль       | Описание                                                          |
|-----------------------|-------------------------------------------------------------------|
| atexit.register(func) | Регистрирует функцию func для выполнения при выходе из программы. |

**atexit.register(func)** Регистрирует функцию для выполнения при выходе из программы.

```python
import atexit

def exit_handler():
    print("Выход из программы")

atexit.register(exit_handler)
```
""",
                    "queue": """
Модуль queue предоставляет различные классы для реализации очередей в Python.
Очереди используются для хранения и управления элементами данных в порядке "первым поступил - первым обслужен".

| Метод          | Описание                                               |
|----------------|--------------------------------------------------------|
| Queue(maxsize) | Создает новую очередь с максимальным размером maxsize. |
| q.put(item)    | Добавляет элемент item в очередь q.                    |
| q.get()        | Удаляет и возвращает элемент из очереди q.             |
| q.empty()      | Возвращает True, если очередь q пуста, иначе False.    |
| q.full()       | Возвращает True, если очередь q полна, иначе False.    |
| q.qsize()      | Возвращает количество элементов в очереди q.           |


**put(item)** Добавляет элемент в очередь.

```python
q = Queue()
q.put(1)
q.put(2)
print(q.qsize())  # Вывод: 2
```

**get()** Удаляет и возвращает первый элемент из очереди.

```python
q = Queue()
q.put(1)
q.put(2)
print(q.get())  # Вывод: 1
```

**empty()** Проверяет, пуста ли очередь.

```python
q = Queue()
print(q.empty())  # Вывод: True
```
""",
                    "pstats": """
Библиотека "pstats" в Python используется для профилирования производительности программы. Она предоставляет возможность анализировать данные о времени выполнения и вызовах функций, что помогает оптимизировать код и улучшить его производительность.

Методы и подмодули библиотеки "pstats" включают:

"Stats" (статистика)
    - "add" - добавляет данные о времени выполнения и вызовах функций в статистику.
    - "print_stats" - выводит общую статистику по вызовам функций.
    - "sort_stats" - сортирует статистику по различным критериям.
    - "strip_dirs" - удаляет пути к файлам из статистики.
    - "calc_callees" - вычисляет информацию о вызываемых функциях.
    - "dump_stats" - сохраняет статистику в файл.

"Profile" (профиль)
    - "run" - запускает профилирование кода.
    - "runcall" - профилирует отдельный вызов функции.
    - "print_stats" - выводит статистику по профилированию.
    - "dump_stats" - сохраняет статистику в файл.

Некоторые из наиболее часто используемых методов "pstats" включают:

"print_stats()": Выводит основную статистику профилирования, включая время выполнения и количество вызовов функций.

Пример кода, демонстрирующего его использование:

```python
import pstats

# Создаем объект статистики
stats = pstats.Stats('profile_result')

# Выводим статистику на экран
stats.print_stats()

```

"sort_stats()": Сортирует статистику профилирования по выбранному критерию, такому как время выполнения или количество вызовов функций.

Пример кода, демонстрирующего его использование:

```python
import pstats

# Создаем объект статистики
stats = pstats.Stats('profile_result')

# Сортируем статистику по времени выполнения
stats.sort_stats('time')

# Выводим отсортированную статистику на экран
stats.print_stats()

```

Пожалуйста, обратите внимание, что примеры кода могут требовать предварительной настройки и обработки профилировочных данных.
""",
                    "cachetools": """
Библиотека "cachetools" используется для кэширования в Python.
Он предоставляет различные механизмы кэширования для повышения производительности.
вашего кода, сохраняя и извлекая данные из памяти вместо выполнения
дорогостоящие вычисления или доступ к внешним ресурсам.


Вот таблица, суммирующая основные методы и подмодули модуля «cachetools»:

Название | Описание
------|------
Cache | Основной класс для создания и управления кэшами.
LRUCache | Реализация кэша, основанная на алгоритме наименее недавно использованного (LRU).
TTLCache | Реализация кэша с истечением срока жизни (TTL) для кэшированных элементов.
LFUCache | Реализация кэша, основанная на наименее часто используемом алгоритме (LFU).
RRCache | Реализация кэша, основанная на алгоритме случайной замены (RR).
HashedCache | Реализация кэша, использующая хеш-функцию для распределения элементов по нескольким субкэшам.

Вот некоторые из наиболее распространенных методов библиотеки «cachetools»:

Название метода | Описание
------|------
get(key) | Извлекает значение, связанное с указанным ключом, из кэша.
set(key, value) | Сохраняет значение в кеше с указанным ключом.
pop(key) | Удаляет элемент с указанным ключом из кэша и возвращает его значение.
clear() | Очищает все элементы из кэша.
keys() | Возвращает список всех ключей в кеше.
   
Вот небольшой фрагмент кода, демонстрирующий использование метода get:

```python
from cachetools import LRUCache

# Создайте LRUCache с максимальным размером 100
cache = LRUCache(maxsize=100)

# Устанавливаем значение в кеше
cache.set("key", "value")

# Получаем значение из кеша
cached_value = cache.get("key")

print(cached_value)  # Output: "value"
```
""",
                },
                "Веб": {
                    "Django": {
                        "Команды": """
Запустить сервер

```
./manage.py runserver
```

Создать Django проект

```bash
django-admin startproject PROJECTNAME
```

Перейти в папку с этим проектом

```bash
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
                    "Flask": {
                        "Типы переменных": """
| Тип                   | Пояснение                                            |
|-----------------------|------------------------------------------------------|
| string (по умолчанию) | принимает любой текст без косой черты                |
| int                   | принимает положительные целые числа                  |
| float                 | принимает положительные значения с плавающей запятой |
| path                  | нравится, но также принимает косые черты string      |
| uuid                  | принимает строки UUID                                |

```python
@app.route('/<type:name>')
def func(name: type):
    pass
```

""",
                    },
                },
            },
            "Методы": {
                "int": r"""
| Метод                  | Описание                                                                                          |
|:-----------------------|:--------------------------------------------------------------------------------------------------|
| int.as_integer_ratio() | Возвращает кортеж, представляющий рациональное число, близкое к данному целому числу.             |
| int.bit_count()        | Возвращает количество установленных битов (битов со значением 1) в двоичном представлении числа.  |
| int.bit_length()       | Возвращает количество битов, необходимых для представления числа в двоичном виде.                 |
| int.conjugate()        | Возвращает сопряженное комплексное число.                                                         |
| int.denominator        | Возвращает знаменатель числа в виде рациональной дроби.                                           |
| int.from_bytes()       | Преобразует байтовую последовательность в целое число, используя указанный порядок байтов и знак. |
| int.imag               | Возвращает мнимую часть комплексного числа.                                                       |
| int.numerator          | Возвращает числитель числа в виде рациональной дроби.                                             |
| int.real               | Возвращает действительную часть комплексного числа.                                               |
| int.to_bytes()         | Преобразует целое число в байтовую последовательность, используя указанный порядок байтов и знак. |

| Метод                  | Пример вызова                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|:-----------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| int.as_integer_ratio() | <div class="code">x = <span class="m">10</span><br><span class="nb">print</span>(x.as_integer_ratio()) <span class="c1"># (10, 1)</span></div>                                                                                                                                                                                       |
| int.bit_count()        | <div class="code">x = <span class="m">123</span><br><span class="nb">print</span>(x.bit_count()) <span class="c1"># 6</span></div>                                                                                                                                                                                                   |
| int.bit_length()       | <div class="code">x = <span class="m">256</span><br><span class="nb">print</span>(x.bit_length()) <span class="c1"># 9</span></div>                                                                                                                                                                                                  |
| int.conjugate()        | <div class="code">x = <span class="m">3</span> + <span class="m">4j</span><br><span class="nb">print</span>(x.conjugate()) <span class="c1"># (3-4j)</span></div>                                                                                                                                                                    |
| int.denominator        | <div class="code">x = <span class="m">3.5</span><br><span class="nb">print</span>(x.denominator) <span class="c1"># ???</span></div>                                                                                                                                                                                                 |
| int.from_bytes()       | <div class="code">bytes = <span class="s">b'\x00\x10'</span><br><span class="nb">print</span>(int.from_bytes(bytes, <span class="na">byteorder</span>=<span class="s">'big'</span>, <span class="na">signed</span>=<span class="k">False</span>)) <span class="c1"># 16</span></div>                                                 |
| int.imag               | <div class="code">x = <span class="m">3</span> + <span class="m">4j</span><br><span class="nb">print</span>(x.imag) <span class="c1"># 4.0</span></div>                                                                                                                                                                              |
| int.numerator          | <div class="code">x = <span class="m">3.5</span><br><span class="nb">print</span>(x.numerator) <span class="c1"># ???</span></div>                                                                                                                                                                                                   |
| int.real               | <div class="code">x = <span class="m">3</span> + <span class="m">4j</span><br><span class="nb">print</span>(x.real) <span class="c1"># 3.0</span></div>                                                                                                                                                                              |
| int.to_bytes()         | <div class="code">num = <span class="m">1024</span><br><span class="nb">print</span>(num.to_bytes(<span class="na">length</span>=<span class="m">2</span>, <span class="na">byteorder</span>=<span class="s">'big'</span>, <span class="na">signed</span>=<span class="k">False</span>)) <span class="c1"># b'\x04\x00'</span></div> |
""",
                "str": r"""
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
                "Table": escape_markdown(
                    rf"""
# Арифметические операции
| Функция                                        | Пример                                             | Описание                                                                         |
|------------------------------------------------|----------------------------------------------------|----------------------------------------------------------------------------------|
| def __eq__(self, other) -> bool:               | self == other                                      | Равенство                                                                        |
| def __ge__(self, other) -> bool:               | self >= other                                      | Больше или равен                                                                 |
| def __gt__(self, other) -> bool:               | self > other                                       | Больше                                                                           |
| def __le__(self, other) -> bool:               | self <= other                                      | Mеньше или равен                                                                 |
| def __lt__(self, other) -> bool:               | self < other                                       | Меньше                                                                           |
| def __ne__(self, other) -> bool:               | self != other                                      | Не равен                                                                         |
| def __or__(self, other):                       | self \| other                                      | Побитовое ИЛИ                                                                    |
| def __add__(self, other):                      | self + other                                       | Сложение                                                                         |
| def __and__(self, other):                      | self & other                                       | Побитовое И                                                                      |
| def __ior__(self, other):                      | self \|= other                                     | Побитовое ИЛИ с присваиванием                                                    |
| def __mod__(self, other):                      | self % other                                       | Остаток от деления                                                               |
| def __mul__(self, other):                      | self * other                                       | Умножение                                                                        |
| def __ror__(self, other):                      | self \| other                                      | Побитовое ИЛИ с обратным присваиванием                                           |
| def __sub__(self, other):                      | self - other                                       | Вычитание                                                                        |
| def __xor__(self, other):                      | self ^ other                                       | Побитовое ИСКЛЮЧАЮЩЕЕ ИЛИ                                                        |
| def __iadd__(self, other):                     | self += other                                      | Сложение с присваиванием                                                         |
| def __iand__(self, other):                     | self &= other                                      | Побитовое И с присваиванием                                                      |
| def __idiv__(self, other):                     | self /= other                                      | Деление с присваиванием                                                          |
| def __imod__(self, other):                     | self %= other                                      | Взятие остатка от деления с присваиванием                                        |
| def __imul__(self, other):                     | self *= other                                      | Умножение с присваиванием                                                        |
| def __ipow__(self, other):                     | self **= other                                     | Возведение в степень с присваиванием                                             |
| def __isub__(self, other):                     | self -= other                                      | Вычитание с присваиванием                                                        |
| def __ixor__(self, other):                     | self ^= other                                      | Побитовое ИСКЛЮЧАЮЩЕЕ ИЛИ с присваиванием                                        |
| def __radd__(self, other):                     | other + self                                       | Сложение справа                                                                  |
| def __rand__(self, other):                     | other & self                                       | Выполняет побитовое И справа                                                     |
| def __rdiv__(self, other):                     | other / self                                       | Деление справа                                                                   |
| def __divmod__(self, other):                   | divmod(self, other)                                | Деление с остатком                                                               |
| def __rdivmod__(self, other):                  | divmod(other, self)                                | Деление с остатком справа                                                        |
| def __rmod__(self, other):                     | other % self                                       | Взятие остатка от деления справа                                                 |
| def __rmul__(self, other):                     | other * self                                       | Умножение справа                                                                 |
| def __rpow__(self, other):                     | other ** self                                      | Возведение в степень справа                                                      |
| def __rsub__(self, other):                     | other - self                                       | Вычитание справа                                                                 |
| def __rxor__(self, other):                     | other ^ self                                       | Побитовое ИСКЛЮЧАЮЩЕЕ ИЛИ справа                                                 |
| def __floordiv__(self, other):                 | self // other                                      | Целочисленное деление                                                            |
| def __ilshift__(self, other):                  | self <<= other                                     | Побитовый сдвиг влево с присваиванием                                            |
| def __imatmul__(self, other):                  | self @= other                                      | Матричное умножение с присваиванием                                              |
| def __irshift__(self, other):                  | self >>= other                                     | Побитовый сдвиг вправо с присваиванием                                           |
| def __itruediv__(self, other):                 | self /= other                                      | Деление с присваиванием                                                          |
| def __rlshift__(self, other):                  | other << self                                      | Побитовый сдвиг влево справа                                                     |
| def __rmatmul__(self, other):                  | other @ self                                       | Матричное умножение справа                                                       |
| def __matmul__(self, other):                   | self @ other                                       | Матричное умножение                                                              |
| def __rrshift__(self, other):                  | other >> self                                      | Побитовый сдвиг вправо справа                                                    |
| def __rtruediv__(self, other):                 | other / self                                       | Деление справа                                                                   |
| def __truediv__(self, other):                  | self / other                                       | Деление                                                                          |
| def __lshift__(self, other):                   | self << other                                      | Побитовый сдвиг влево                                                            |
| def __rshift__(self, other):                   | self >> other                                      | Побитовый сдвиг вправо                                                           |
| def __ifloordiv__(self, other):                | self //= other                                     | Целочисленное деление с присваиванием                                            |
| def __rfloordiv__(self, other):                | other // self                                      | Целочисленное деление справа                                                     |
| def __pos__(self):                             | +self                                              | Положительное значение объекта                                                   |
| def __neg__(self):                             | -self                                              | Отрицательное значение объекта                                                   |
| def __invert__(self):                          | ~self                                              | Инвертированное значение объекта                                                 |

# func call
| Функция                                        | Пример                                             | Описание                                                                         |
|------------------------------------------------|----------------------------------------------------|----------------------------------------------------------------------------------|
| def __pow__(self, power, modulo=None):         | pow(self, power, modulo)                           | Возведение в степень                                                             |
| def __abs__(self):                             | abs(self)                                          | Абсолютное значение объекта                                                      |
| def __hex__(self):                             | hex(self)                                          | Строковое представление объекта в<br>шестнадцатеричной системе счисления         |
| def __float__(self):                           | float(self)                                        | Представление объекта в виде числа с плавающей запятой                           |
| def __bytes__(self):                           | bytes(self)                                        | Байтовое представление объекта                                                   |
| def __long__(self):                            | int(self)                                          | Длинное целочисленное представление объекта                                      |
| def __int__(self):                             | int(self)                                          | Целочисленное представление объекта                                              |
| def __bool__(self) -> bool:                    | bool(self)                                         | Булево значение                                                                  |
| def __oct__(self):                             | oct(self)                                          | Строковое представление объекта в<br>восьмеричной системе счисления              |
| def __len__(self):                             | len(self)                                          | Возвращает длину объекта                                                         |
| def __str__(self):                             | str(self)                                          | Строковое представление объекта                                                  |
| def __hash__(self):                            | hash(self)                                         | Хеш-значение объекта                                                             |
| def __iter__(self):                            | iter(self)                                         | Итератор объекта                                                                 |
| def __next__(self):                            | next(self)                                         | Следующий элемент в итерации                                                     |
| def __round__(self, n=None):                   | round(self, n)                                     | Округленное значение                                                             |
| def __complex__(self):                         | complex(self)                                      | Комплексное представление                                                        |
| def __reversed__(self):                        | reversed(self)                                     | Возвращает обратный итератор объекта                                             |
| def __unicode__(self):                         | unicode(self)                                      | Строковое представление объекта (Python 2)                                       |
| def __instancecheck__(self, instance) -> bool: | isinstance(obj, cls)                               | Проверяет, является ли объект экземпляром класса                                 |
| def __subclasscheck__(self, subclass) -> bool: | issubclass(subclass, cls)                          | Является ли класс подклассом другого класса                                      |
| def __call__(self, *args, **kwargs):           | self(*args, **kwargs)                              | Вызывает объект как функцию                                                      |
| def __repr__(self):                            | repr(self)                                         | Строковое представление объекта                                                  |
| def __subclasshook__(cls, __subclass):         | issubclass(Subclass, MyClass)                      | Проверяет, является ли класс подклассом другого класса                           |
| def __dir__(self):                             | dir(self)                                          | Список атрибутов и методов объекта                                               |
| def __format__(self, format_spec):             | {to_table_code_py('"{0:{format_spec}}".format(self)')} | Форматированную строку объекта                                        |
| def __cmp__(self, other) -> int:               | cmp(self, other)                                   | Сравнивает объекты и возвращает -1, 0 или 1                                      |
| def __aiter__(self):                           | awaitable.__aiter__()                              | Асинхронный итератор объекта                                                     |
| def __anext__(self):                           | awaitable.__anext__()                              | Возвращает следующий элемент в асинхронной итерации                              |
| def __coerce__(self, other):                   | coerce(self, other)                                | Преобразует объект к общему типу с другим объектом                               |
| def __index__(self):                           | operator.index(self)                               | Целочисленное представление объекта<br>для использования в индексации            |
| def __floor__(self):                           | math.floor(self)                                   | Наибольшее целое число, меньшее или равное объекту                               |
| def __trunc__(self):                           | math.trunc(self)                                   | Усеченное значение объекта                                                       |
| def __ceil__(self):                            | math.ceil(self)                                    | Наименьшее целое число, большее или равное объекту                               |
| def __copy__(self):                            | copy.copy(self)                                    | Создает поверхностную копию объекта                                              |
| def __deepcopy__(self, memodict={{}}):         | copy.deepcopy(self)                                | Создает глубокую копию объекта                                                   |
| def __sizeof__(self):                          | sys.getsizeof(self)                                | Возвращает размер объекта в байтах                                               |
| def __fspath__(self):                          | os.fspath(self)                                    | Возвращает строковое представление<br>объекта для использования в функции fspath |


# Контейнеры

| Функция                                        | Пример                                             | Описание                                                                         |
|------------------------------------------------|----------------------------------------------------|----------------------------------------------------------------------------------|
| def __getitem__(self, item):                   | self[item]                                         | Элемент по индексу или ключу                                                     |
| def __missing__(self, key):                    | self[key]                                          | Вызывается при отсутствии ключа в объекте                                        |
| def __contains__(self, item) -> bool:          | item in self                                       | Содержится ли элемент в объекте                                                  |
| def __setslice__(self, i, j, sequence):        | self[i:j] = sequence                               | Заменяет срез объекта указанной последовательностью                              |
| def __delattr__(self, item):                   | del self.item                                      | Удаляет атрибут объекта                                                          |
| def __delitem__(self, key):                    | del self[key]                                      | Удаляет элемент по ключу                                                         |
| def __delslice__(self, i, j):                  | del self[i:j]                                      | Удаляет срез из объекта                                                          |
| def __get__(self, instance, owner):            | value = self.__get__(instance, owner)              | Возвращает значение атрибута объекта в классе-дескрипторе                        |


# Классы

| Функция                                        | Пример                                             | Описание                                                                         |
|------------------------------------------------|----------------------------------------------------|----------------------------------------------------------------------------------|
| def __new__(cls, *args, **kwargs):             | instance = MyClass(args)                           | Создает новый обьект                                                             |
| def __init__(self):                            | instance = MyClass(args)                           | При инициализации нового экземпляра объекта                                      |
| def __class__(self):                           | obj_class = obj.__class__()                        | Возвращает класс объекта                                                         |
| def __del__(self):                             | del self                                           | При удалении объекта                                                             |
| {to_table_code_py(f"@classmethod{n}def __prepare__(metacls, name, bases):")} | metacls.__prepare__(name, bases) | Словарь для использования в качестве<br>пространства имен класса |
| def __delete__(self, instance):                | del instance.self                                  | Удаляет атрибут объекта                                                          |
| def __init_subclass__(cls, **kwargs):          | {to_table_code_py(f"class Subclass(Parent):{n}    pass{n}Subclass.__init_subclass__()")}                          | Вызывается при создании подкласса                                 |
| def __mro_entries__(self, bases):              | {to_table_code_py(f"class MyClass(Base1, Base2, metaclass=MyMeta):{n}    pass{n}MyClass.__mro_entries__(bases)")} | Возвращает кортеж для обновления MRO<br>(Method Resolution Order) |
| def __getinitargs__(self):                     | args = self.__getinitargs__()                      | Кортеж аргументов для использования при создании объекта                         |
| def __set_name__(self, owner, name):           | {to_table_code_py(f"class MyClass:{n}    attr = MyDescriptor(){n}MyClass.attr.__set_name__(MyClass, 'attr')")}    | Вызывается при установке имени атрибута в классе  |
| def __getnewargs__(self):                      | args = self.__getnewargs__()                       | Возвращает аргументы для использования<br>при создании нового экземпляра объекта |
| def __getattribute__(self, item):              | value = self.__getattribute__('attr')              | Возвращает значение атрибута объекта                                             |
| def __getattr__(self, item):                   | value = self.__getattr__('attr')                   | Вызывается при обращении<br>к несуществующему атрибуту объекта                   |
| def __await__(self):                           | await awaitable                                    | Возвращает объект, поддерживающий асинхронное ожидание                           |
| def __set__(self, instance, value):            | instance.attr = value                              | Устанавливает значение атрибута в экземпляре класса                              |
| def __class_getitem__(cls, item):              | item_type = MyGenericClass.__class_getitem__(Item) | Обобщенный тип объекта                                                           |
| def __setattr__(self, key, value):             | self.key = value                                   | Устанавливает значение атрибута объекта                                          |
| def __setitem__(self, key, value):             | self[key] = value                                  | Устанавливает значение элемента по ключу в объекте                               |


# with as

| Функция                                        | Пример                                             | Описание                                                                         |
|------------------------------------------------|----------------------------------------------------|----------------------------------------------------------------------------------|
| def __enter__(self):                            | with self as x:                                    | Выполняет код при входе в блок with                                              |
| def __aenter__(self):                           | async with self as x:                              | Вызывается при входе в асинхронный<br>контекстный блок                           |
| def __aexit__(self, exc_type, exc_val, exc_tb): | {to_table_code_py(f"async with self as x:{n}    pass{n}await self.__aexit__(exc_type, exc_val, exc_tb)")}        | Вызывается при выходе из асинхронного контекстного блока                            | 
| def __exit__(self, exc_type, exc_val, exc_tb):  | {to_table_code_py(f"with self as x:{n}    pass{n}self.__exit__(exc_type, exc_val, exc_tb)")}   | Вызывается при выходе из контекстного блока                                         |


# Pickle

| Функция                                        | Пример                                             | Описание                                                                         |
|------------------------------------------------|----------------------------------------------------|----------------------------------------------------------------------------------|
| def __setstate__(self, state):                 | obj.__setstate__(state)                            | Восстанавливает состояние объекта                                                |
| def __reduce_ex__(self, protocol):             | pickle.loads(pickle.dumps(self, protocol))         | Возвращает данные для использования в процессе<br>сериализации объекта с протоколом |
| def __getstate__(self):                        | pickle.loads(pickle.dumps(self).__getstate__())    | Возвращает состояние объекта для использования<br>в процессе сериализации        |
| def __reduce__(self):                          | pickle.loads(pickle.dumps(self))                   | Возвращает данные для использования<br>в процессе сериализации объекта           |

                    """
                ),
                "Кратко о использовании": """                   
| Магический метод                | Когда он вызывается (пример)     | Объяснение                                           |
|---------------------------------|----------------------------------|------------------------------------------------------|
| &#95;&#95;new&#95;&#95;(cls [,...])             | instance = MyClass(arg1, arg2)   | &#95;&#95;new&#95;&#95; вызывается при создании экземпляра           |
| &#95;&#95;init&#95;&#95;(self [,...])           | instance = MyClass(arg1, arg2)   | &#95;&#95;init&#95;&#95; вызывается при создании экземпляра          |
| &#95;&#95;pos&#95;&#95;(self)                   | +self                            | Унарный знак плюса                                   |
| &#95;&#95;neg&#95;&#95;(self)                   | -self                            | Унарный знак минуса                                  |
| &#95;&#95;invert&#95;&#95;(self)                | ~self                            | Побитовая инверсия                                   |
| &#95;&#95;index&#95;&#95;(self)                 | x[self]                          | Преобразование, когда объект используется как индекс |
| &#95;&#95;nonzero&#95;&#95;(self)               | bool(self), if self:             | Булевое значение объекта                             |
| &#95;&#95;getattr&#95;&#95;(self, name)         | self.name # name не определено   | Пытаются получить несуществующий атрибут             |
| &#95;&#95;setattr&#95;&#95;(self, name, val)    | self.name = val                  | Присвоение любому атрибуту                           |
| &#95;&#95;delattr&#95;&#95;(self, name)         | del self.name                    | Удаление атрибута                                    |
| &#95;&#95;getattribute&#95;&#95;(self, name)    | self.name                        | Получить любой атрибут                               |
| &#95;&#95;getitem&#95;&#95;(self, key)          | self[key]                        | Получение элемента через индекс                      |
| &#95;&#95;setitem&#95;&#95;(self, key, val)     | self[key] = val                  | Присвоение элементу через индекс                     |
| &#95;&#95;delitem&#95;&#95;(self, key)          | del self[key]                    | Удаление элемента через индекс                       |
| &#95;&#95;iter&#95;&#95;(self)                  | for x in self                    | Итерация                                             |
| &#95;&#95;contains&#95;&#95;(self, value)       | value in self, value not in self | Проверка принадлежности с помощью in                 |
| &#95;&#95;call&#95;&#95;(self [,...])           | self(args)                       | «Вызов» экземпляра                                   |
| &#95;&#95;enter&#95;&#95;(self)                 | with self as x:                  | with оператор менеджеров контекста                   |
| &#95;&#95;exit&#95;&#95;(self, exc, val, trace) | with self as x:                  | with оператор менеджеров контекста                   |
| &#95;&#95;getstate&#95;&#95;(self)              | pickle.dump(pkl_file, self)      | Сериализация                                         |
| &#95;&#95;setstate&#95;&#95;(self)              | data = pickle.load(pkl_file)     | Сериализация                                         |
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
Заметьте, что мы не определяли &#95;&#95;eq&#95;&#95; и &#95;&#95;ne&#95;&#95;, так как это приведёт к странному поведению 
(например, Word('foo') == Word('bar') будет расцениваться как истина)

Стандартная библиотека предоставляет нам класс-декторатор в модуле functools, 
который и определит все сравнивающие методы, от вас достаточно 
определить только &#95;&#95;eq&#95;&#95; и ещё один (&#95;&#95;gt&#95;&#95;, &#95;&#95;lt&#95;&#95; и т.п.) 
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
| &#95;&#95;itruediv&#95;&#95;(self, other)  |           | Правильное деление с присваиванием.<br>Нужно from &#95;&#95;future&#95;&#95; import division. |
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

|                                            |        |                                                                                            |
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
&#95;&#95;int&#95;&#95;(self)           в int.
&#95;&#95;long&#95;&#95;(self)          в long.
&#95;&#95;float&#95;&#95;(self)         в float.
&#95;&#95;complex&#95;&#95;(self)       в комплексное число.
&#95;&#95;oct&#95;&#95;(self)           в восьмеричное число.
&#95;&#95;hex&#95;&#95;(self)           в шестнадцатиричное число.
&#95;&#95;index&#95;&#95;(self)         Преобразование типа к int, когда объект используется в срезах (выражения вида [start:stop:step]). 
                        Если вы определяете свой числовый тип, который может использоваться как индекс списка, вы должны определить __index__.
&#95;&#95;trunc&#95;&#95;(self)         Вызывается при math.trunc(self). 
                        Должен вернуть своё значение, обрезанное до целочисленного типа (обычно long).
&#95;&#95;str&#95;&#95;(self)           Определяет поведение функции str(), вызванной для экземпляра вашего класса.
&#95;&#95;repr&#95;&#95;(self)          Определяет поведение функции repr(), вызыванной для экземпляра вашего класса. 
                        Главное отличие от str() в целевой аудитории. 
                        repr() больше предназначен для машинно-ориентированного вывода 
                        (более того, это часто должен быть валидный код на Питоне), а str() предназначен для чтения людьми.
&#95;&#95;bytes&#95;&#95;(self)         ведёт себя так же как &#95;str&#95;&#95;
&#95;&#95;format&#95;&#95;(self, formatstr)
                        Определяет поведение, когда экземпляр вашего класса используется в форматировании строк нового стиля. 
                        Например, "Hello, {0:abc}!".format(a) приведёт к вызову a.&#95;format&#95;("abc"). 
                        Это может быть полезно для определения ваших собственных числовых или строковых типов, 
                        которым вы можете захотеть предоставить какие-нибудь специальные опции форматирования.
&#95;&#95;hash&#95;&#95;(self)          Определяет поведение функции hash(), вызыванной для экземпляра вашего класса. 
                        Метод должен возвращать целочисленное значение, которое будет использоваться 
                        для быстрого сравнения ключей в словарях. 
                        Заметьте, что в таком случае обычно нужно определять и &#95;&#95;eq&#95;&#95; тоже. 
                        Руководствуйтесь следующим правилом: a == b подразумевает hash(a) == hash(b).
&#95;&#95;bool&#95;&#95;(self)          Определяет поведение функции bool(), вызванной для экземпляра вашего класса. 
                        Должна вернуть True или False, в зависимости от того, 
                        когда вы считаете экземпляр соответствующим True или False.
&#95;&#95;dir&#95;&#95;(self)           Определяет поведение функции dir(), вызванной на экземпляре вашего класса. 
                        Этот метод должен возвращать пользователю список атрибутов. 
                        Обычно, определение &#95;dir&#95;&#95; не требуется, но может быть жизненно важно для интерактивного 
                        использования вашего класса, если вы переопределили &#95;getattr&#95;&#95; или &#95;getattribute&#95;&#95; 
                        (с которыми вы встретитесь в следующей части), 
                        или каким-либо другим образом динамически создаёте атрибуты.
&#95;&#95;sizeof&#95;&#95;(self)        Определяет поведение функции sys.getsizeof(), вызыванной на экземпляре вашего класса. 
                        Метод должен вернуть размер вашего объекта в байтах. 
                        Он главным образом полезен для классов, определённых в 
                        расширениях на C, но всё-равно полезно о нём знать.
""",
                "Контроль доступа к атрибутам": """
&#95;&#95;getattr&#95;&#95;(self, name)              Вы можете определить поведение для случая, когда пользователь пытается обратиться 
                                     к атрибуту, который не существует (совсем или пока ещё). 
                                     Это может быть полезным для перехвата и перенаправления частых опечаток, 
                                     предупреждения об использовании устаревших атрибутов 
                                     (вы можете всё-равно вычислить и вернуть этот атрибут, если хотите), 
                                     или хитро возвращать AttributeError, когда это вам нужно. 
                                     Правда, этот метод вызывается только когда пытаются получить 
                                     доступ к несуществующему атрибуту, поэтому это не очень хорошее решение для инкапсуляции.
&#95;&#95;setattr&#95;&#95;(self, name, value)       В отличии от &#95;&#95;getattr&#95;&#95;, &#95;&#95;setattr&#95;&#95; решение для инкапсуляции. 
                                     Этот метод позволяет вам определить поведение для присвоения значения атрибуту, 
                                     независимо от того существует атрибут или нет. 
                                     То есть, вы можете определить любые правила для любых изменений значения атрибутов. 
                                     Впрочем, вы должны быть осторожны с тем, как использовать &#95;&#95;setattr&#95;&#95;, 
                                     смотрите пример нехорошего случая в конце этого списка.
&#95;&#95;delattr&#95;&#95;                          Это то же, что и &#95;&#95;setattr&#95;&#95;, но для удаления атрибутов, вместо установки значений. 
                                     Здесь требуются те же меры предосторожности, что и в __setattr__ чтобы избежать 
                                     бесконечной рекурсии (вызов del self.name в определении __delattr__ вызовет бесконечную рекурсию)
&#95;&#95;getattribute&#95;&#95;(self, name)         Выглядит к месту среди своих коллег &#95;&#95;setattr&#95;&#95; и &#95;&#95;delattr&#95;&#95;, 
                                     но я бы не рекомендовал вам его использовать. &#95;&#95;getattribute&#95;&#95; может использоваться 
                                     только с классами нового типа (в новых версиях Питона все классы нового типа, а в старых версиях 
                                     вы можете получить такой класс унаследовавшись от object). 
                                     Этот метод позволяет вам определить поведение для каждого случая доступа к атрибутам 
                                     (а не только к несуществующим, как &#95;&#95;getattr&#95;&#95;(self, name)). 
                                     Он страдает от таких же проблем с бесконечной рекурсией, как и его коллеги 
                                     (на этот раз вы можете вызывать &#95;&#95;getattribute&#95;&#95; у базового класса, чтобы их предотвратить). 
                                     Он, так же, главным образом устраняет необходимость в &#95;&#95;getattr&#95;&#95;, 
                                     который в случае реализации &#95;&#95;getattribute&#95;&#95; может быть вызван только явным образом 
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
(заметьте, что мы используем super, так как не все классы имеют атрибут &#95;&#95;dict&#95;&#95;):

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

Протокол для определения неизменяемых контейнеров: чтобы создать неизменяемый контейнер, вы должны только определить &#95;&#95;len&#95;&#95; и &#95;&#95;getitem&#95;&#95;

Протокол изменяемого контейнера требует того же, что и неизменяемого контейнера, плюс &#95;&#95;setitem&#95;&#95; и &#95;&#95;delitem&#95;&#95;

Если вы хотите, чтобы ваши объекты можно было перебирать итерацией, вы должны определить &#95;&#95;iter&#95;&#95;, который возвращает итератор. 
Этот итератор должен соответствовать протоколу итератора, который требует методов &#95;&#95;iter&#95;&#95;(возвращает самого себя) и &#95;&#95;next&#95;&#95;.


&#95;&#95;len&#95;&#95;(self)                  Кколичество элементов в контейнере. Часть протоколов для изменяемого и неизменяемого контейнеров.
&#95;&#95;getitem&#95;&#95;(self, key)         Поведение при доступе к элементу, используя синтаксис self[key]. 
                               Тоже относится и к протоколу изменяемых и к протоколу неизменяемых контейнеров. 
                               Должен выбрасывать соответствующие исключения: 
                               TypeError если неправильный тип ключа и KeyError если ключу не соответствует никакого значения.
&#95;&#95;setitem&#95;&#95;(self, key, value)  Определяет поведение при присваивании значения элементу, 
                               используя синтаксис self[nkey] = value. 
                               Часть протокола изменяемого контейнера. 
                               Опять же, вы должны выбрасывать KeyError и TypeError в соответсвующий случаях.
&#95;&#95;delitem&#95;&#95;(self, key)         Определяет поведение при удалении элемента (то есть del self[key]). 
                               Это часть только протокола для изменяемого контейнера. 
                               Вы должны выбрасывать соответствующее исключение, если ключ некорректен.
&#95;&#95;iter&#95;&#95;(self)                 Должен вернуть итератор для контейнера. 
                               Итераторы возвращаются в множестве ситуаций, главным образом для встроенной функции iter() 
                               и в случае перебора элементов контейнера выражением for x in container:. 
                               Итераторы сами по себе объекты и они тоже должны определять метод &#95;&#95;iter&#95;&#95;, который возвращает self.
&#95;&#95;reversed&#95;&#95;(self)             Вызывается чтобы определить поведения для встроенной функции reversed(). 
                               Должен вернуть обратную версию последовательности. 
                               Реализуйте метод только если класс упорядоченный, как список или кортеж.
&#95;&#95;contains&#95;&#95;(self, item)       Предназначен для проверки принадлежности элемента с помощью in и not in. 
                               Вы спросите, почему же это не часть протокола последовательности? 
                               Потому что когда &#95;&#95;contains&#95;&#95; не определён, Питон просто перебирает всю последовательность 
                               элемент за элементом и возвращает True если находит нужный.
&#95;&#95;missing&#95;&#95;(self, key)         Используется при наследовании от dict. 
                               Определяет поведение для для каждого случая, когда пытаются получить элемент по 
                               несуществующему ключу (так, например, если у меня есть словарь d и я пишу d["george"] 
                               когда "george" не является ключом в словаре, вызывается d.&#95;&#95;missing&#95;&#95;("george")).
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
&#95;&#95;instancecheck&#95;&#95;(self, instance) Проверяет, является ли экземлпяр членом вашего класса (isinstance(instance, class)
&#95;&#95;subclasscheck&#95;&#95;(self, subclass) Проверяет, является наследуется ли класс от вашего класса (issubclass(subclass, class))
""",
                "Вызываемые объекты": """
&#95;&#95;call&#95;&#95;(self, [args...])            Позволяет любому экземпляру вашего класса быть вызванным как-будто он функция. 
                                     Главным образом это означает, что x() означает то же, что и x.&#95;&#95;call&#95;&#95;(). 
                                     Заметьте, &#95;&#95;call&#95;&#95; принимает произвольное число аргументов; 
                                     то есть, вы можете определить &#95;&#95;call&#95;&#95; так же как любую другую функцию, 
                                     принимающую столько аргументов, сколько вам нужно.

&#95;&#95;call&#95;&#95;, в частности, может быть полезен в классах, чьи экземпляры часто изменяют своё состояние. 
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
&#95;&#95;enter&#95;&#95;(self)                      Определяет, что должен сделать менеджер контекста в начале блока, созданного оператором with. 
                                     Заметьте, что возвращаемое &#95;&#95;enter&#95;&#95; значение и есть то значение, с которым производится работа внутри with.
&#95;&#95;exit&#95;&#95;(self, exception_type, 
         exception_value, traceback) Определяет действия менеджера контекста после того, как блок будет выполнен (или прерван во время работы). 
                                     Может использоваться для контролирования исключений, чистки, любых действий которые должны быть 
                                     выполнены незамедлительно после блока внутри with. 
                                     Если блок выполнен успешно, exception_type, exception_value, и traceback будут установлены в None. 
                                     В другом случае вы сами выбираете, перехватывать ли исключение или предоставить это пользователю; 
                                     если вы решили перехватить исключение, убедитесь, что &#95;&#95;exit&#95;&#95; возвращает True после того 
                                     как всё сказано и сделано. 
                                     Если вы не хотите, чтобы исключение было перехвачено менеджером контекста, просто позвольте ему случиться.

&#95;&#95;enter&#95;&#95; и &#95;&#95;exit&#95;&#95; могут быть полезны для специфичных классов с хорошо описанным и 
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

&#95;&#95;aenter&#95;&#95;(self) — аналогично &#95;&#95;enter&#95;&#95;, только функция возвращает корутину (результат которой можно получить с помощью await)

&#95;&#95;aexit&#95;&#95;(self, exc_type, exc_value, traceback) — аналогично &#95;&#95;exit&#95;&#95;, только функция возвращает корутину (результат которой можно получить с помощью await)

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
&#95;&#95;get&#95;&#95;, &#95;&#95;set&#95;&#95; или &#95;&#95;delete&#95;&#95;. 

&#95;&#95;get&#95;&#95;(self, instance, instance_class) Определяет поведение при возвращении значения из дескриптора. 
                                        instance это объект, для чьего атрибута-дескриптора вызывается метод. 
                                        owner это тип (класс) объекта.
&#95;&#95;set&#95;&#95;(self, instance, value)          Определяет поведение при изменении значения из дескриптора. 
                                        instance это объект, для чьего атрибута-дескриптора вызывается метод. 
                                        value это значение для установки в дескриптор.
&#95;&#95;delete&#95;&#95;(self, instance)              Определяет поведение для удаления значения из дескриптора. 
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

&#95;&#95;copy&#95;&#95;(self)                       Определяет поведение copy.copy() для экземпляра вашего класса. 
                                     copy.copy() возвращает поверхностную копию вашего объекта — это означает, 
                                     что хоть сам объект и создан заново, все его данные ссылаются на данные оригинального объекта. 
                                     И при изменении данных нового объекта, изменения будут происходить и в оригинальном.
&#95;&#95;deepcopy&#95;&#95;(self, memodict={})      Определяет поведение copy.deepcopy() для экземпляров вашего класса. 
                                     copy.deepcopy() возвращает глубокую копию вашего объекта — копируются и объект и его данные. 
                                     memodict это кэш предыдущих скопированных объектов, он предназначен для оптимизации 
                                     копирования и предотвращения бесконечной рекурсии, когда копируются рекурсивные структуры данных. 
                                     Когда вы хотите полностью скопировать какой-нибудь конкретный атрибут, 
                                     вызовите на нём copy.deepcopy() с первым параметром memodict
""",
                "Ещё": """
&#95;&#95;init_subclass&#95;&#95;(cls) — позволяет переопределить создание подклассов объекта. Например, добавлять дополнительные атрибуты:

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

&#95;&#95;getattr&#95;&#95;(self, name) — вызывается методом getattr(...) или при обращении к атрибуту объекта через x.y, где x — объект, а y — атрибут.

&#95;&#95;setattr&#95;&#95;(self, name, value) — вызывается методом setattr(...)или при обращении к атрибуту объекта с последующим определением значения переданного атрибута. 
Например: x.y = 1, где x — объект, y — атрибут, а 1 — значение атрибута.

&#95;&#95;delattr&#95;&#95;(self, name) — вызывается методом delattr(...)или при ручном удалении атрибута у объекта с помощью del x.y, где  x — объект, а y — атрибут.

&#95;&#95;dir&#95;&#95;(self) — вызывается методом dir(...) и выводит список доступных атрибутов объекта.



Создание последовательностей
Любой объект может реализовать методы встроенных последовательностей (словари, кортежи, списки, строки и так далее). 
Доступ к значениям последовательности переопределяется следующими методами:

&#95;&#95;len&#95;&#95;(self) — вызывается методом len(...) и возвращает количество элементов в последовательности.

&#95;&#95;getitem&#95;&#95;(self, key) — вызывается при обращении к элементу в последовательности по его ключу (индексу). 
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

&#95;&#95;setitem&#95;&#95;(self, key, value) — вызывается при присваивании какого-либо значения элементу в последовательности. 
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

&#95;&#95;delitem&#95;&#95;(self, key) — вызывается при удалении значения в последовательности по его индексу (ключу) с помощью синтаксиса ключевого слова del.

&#95;&#95;missing&#95;&#95;(self, key) — вызывается в случаях, когда значения в последовательности не существует.

&#95;&#95;iter&#95;&#95;(self) — вызывается методом iter(...) и возвращает итератор последовательности, например, для использования объекта в цикле:

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

&#95;&#95;reversed&#95;&#95;(self) — вызывается методом reversed(...) и аналогично методу &#95;&#95;iter&#95;&#95; возвращает тот же итератор, только в обратном порядке.

&#95;&#95;contains&#95;&#95;(self, item) — вызывается при проверке принадлежности элемента к последовательности с помощью in или not in.


&#95;&#95;imatmul&#95;&#95;(self, other) — умножение матриц с присваиванием, оператор @=
""",
                "tproger.ru": """
Взято из https://tproger.ru/articles/gajd-po-magicheskim-metodam-v-python

Магические методы в Python — подробный гайд

Создание и удаление объектовЛюбое описание объекта в объектно-ориентированном
программировании начинается с создания объекта и его удаления.
Давайте подробнее остановимся на каждом из них:
&#95;&#95;new&#95;&#95;(cls[, ...]) — метод создания типа класса.
Он принимает первым аргументом тип класса, в котором он вызывается, и, как правило, возвращает этот же тип.
В основном используется, чтобы настраивать создание экземпляра класса тех объектов,
которые наследуются от неизменяемых типов (например, int, str, или tuple).
&#95;&#95;init&#95;&#95;(self[, ...]) — конструктор класса. Используется при определении объектов.
&#95;&#95;init_subclass&#95;&#95;(cls) — позволяет переопределить создание подклассов объекта.
Например, добавлять дополнительные атрибуты:
```python
>>> class Test:
>>>     def __init_subclass__(cls, /, test_param, **kwargs):
>>>         super().__init_subclass__(**kwargs)
>>>         cls.test_param = test_param
>>>
>>> class AnotherTest(Test, test_param="Hello World"):
>>>     pass
```

&#95;&#95;del&#95;&#95;(self) — деструктор класса. Вызывается автоматически сборщиком мусора, практически никогда не используется, за исключением, когда пользователя необходимо предупредить о незакрытых дескрипторах.

Общие свойства объектов Любой объект может содержать дополнительную информацию, полезную при отладке или приведении типов. Например:
&#95;&#95;repr&#95;&#95;(self) — информационная строка об объекте. Выводится при вызове функции repr(...) или в момент отладки. Для последнего этот метод и предназначен.

Например:
```python
>>> class Test:
>>>     def __repr__(self):
>>>         return ""
>>>
>>> Test()
... ''
```

&#95;&#95;str&#95;&#95;(self) — вызывается при вызове функции str(...), возвращает строковый объект.

Например:
```python
>>> class Test:
>>>     def __str__(self):
>>>         return "Hello World"
>>>
>>> test = Test()
>>> str(test)
... 'Hello World'
```

&#95;&#95;bytes&#95;&#95;(self) — аналогично &#95;&#95;str&#95;&#95;(self), только возвращается набор байт.
&#95;&#95;format&#95;&#95;(self, format_spec) — вызывается при вызове функции format(...) и используется для форматировании строки с использованием строковых литералов.

Методы сравнения объектов между собой
&#95;&#95;lt&#95;&#95;(self, other) — определяет поведение оператора сравнения «меньше», <.
&#95;&#95;le&#95;&#95;(self, other) — определяет поведение оператора сравнения «меньше или равно», <=.
&#95;&#95;eq&#95;&#95;(self, other) — определяет поведение оператора «равенства», ==.
&#95;&#95;ne&#95;&#95;(self, other) — определяет поведение оператора «неравенства», !=.
&#95;&#95;gt&#95;&#95;(self, other) — определяет поведение оператора сравнения «больше», >.
&#95;&#95;ge&#95;&#95;(self, other) — определяет поведение оператора сравнения «больше или равно», >=.
&#95;&#95;hash&#95;&#95;(self) — вызывается функцией hash(...) и используется для определения контрольной суммы объекта, чтобы доказать его уникальность. Например, чтобы добавить объект в set, frozenset, или использовать в качестве ключа в словаре dict.
&#95;&#95;bool&#95;&#95;(self) — вызывается функцией bool(...) и возвращает True или False в соответствии с реализацией. Если данный метод не реализован в объекте, и объект является какой-либо последовательностью (списком, кортежем и т.д.), вместо него вызывается метод &#95;&#95;len&#95;&#95;. Используется, в основном, в условиях if, например:
```python
>>> class Test:
>>>     def __bool__(self):
>>>         return True
>>>
>>> test = Test()
>>>
>>> if test:
>>>    print("Hello World")
>>>
... 'Hello World'
```

Доступ к атрибутам объекта
Доступ ко всем свойствам объекта также контролируются отдельными методами:
&#95;&#95;getattr&#95;&#95;(self, name) — вызывается методом getattr(...) или при обращении к атрибуту объекта через x.y, где x — объект, а y — атрибут.
&#95;&#95;setattr&#95;&#95;(self, name, value) — вызывается методом setattr(...) или при обращении к атрибуту объекта с последующим определением значения переданного атрибута. Например: x.y = 1, где x — объект, y — атрибут, а 1 — значение атрибута.
&#95;&#95;delattr&#95;&#95;(self, name) — вызывается методом delattr(...)или при ручном удалении атрибута у объекта с помощью del x.y, где  x — объект, а y — атрибут.
&#95;&#95;dir&#95;&#95;(self) — вызывается методом dir(...) и выводит список доступных атрибутов объекта.

Создание последовательностей
Любой объект может реализовать методы встроенных последовательностей (словари, кортежи, списки, строки и так далее). Доступ к значениям последовательности переопределяется следующими методами:
&#95;&#95;len&#95;&#95;(self) — вызывается методом len(...) и возвращает количество элементов в последовательности.
&#95;&#95;getitem&#95;&#95;(self, key) — вызывается при обращении к элементу в последовательности по его ключу (индексу). Метод должен выбрасывать исключение TypeError, если используется некорректный тип ключа, KeyError, если данному ключу не соответствует ни один элемент в последовательности.

Например:
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

&#95;&#95;setitem&#95;&#95;(self, key, value) — вызывается при присваивании какого-либо значения элементу в последовательности. Также может выбрасывать исключения TypeError и KeyError.

Например:
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

&#95;&#95;delitem&#95;&#95;(self, key) — вызывается при удалении значения в последовательности по его индексу (ключу) с помощью синтаксиса ключевого слова del.
&#95;&#95;missing&#95;&#95;(self, key) — вызывается в случаях, когда значения в последовательности не существует.
&#95;&#95;iter&#95;&#95;(self) — вызывается методом iter(...) и возвращает итератор последовательности, например, для использования объекта в цикле:
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

&#95;&#95;reversed&#95;&#95;(self) — вызывается методом reversed(...) и аналогично методу &#95;&#95;iter&#95;&#95; возвращает тот же итератор, только в обратном порядке.
&#95;&#95;contains&#95;&#95;(self, item) — вызывается при проверке принадлежности элемента к последовательности с помощью in или not in.

Числовые магические методы
Данные методы делятся на несколько групп: унарные операторы, обычные арифметические, отражённые арифметические операторы, составные присваивания и преобразования типов.

Унарные операторы
&#95;&#95;neg&#95;&#95;(self) — определяет поведение для отрицания (-a)
&#95;&#95;pos&#95;&#95;(self) — определяет поведение для унарного плюса (+a)
&#95;&#95;abs&#95;&#95;(self) — определяет поведение для встроенной функции abs(...)
&#95;&#95;invert&#95;&#95;(self) — определяет поведение для инвертирования оператором ~

Обычные арифметические операторы
&#95;&#95;add&#95;&#95;(self, other) — сложение, оператор +
&#95;&#95;sub&#95;&#95;(self, other) — вычитание, оператор -
&#95;&#95;mul&#95;&#95;(self, other) — умножение, оператор *
&#95;&#95;matmul&#95;&#95;(self, other) — умножение матриц, оператор @
&#95;&#95;truediv&#95;&#95;(self, other) — деление, оператор /
&#95;&#95;floordiv&#95;&#95;(self, other) — целочисленное деление, оператор //
&#95;&#95;mod&#95;&#95;(self, other) — остаток от деления, оператор %
&#95;&#95;divmod&#95;&#95;(self, other) — деление с остатком, определяет поведение для встроенной функции divmod(...)
&#95;&#95;pow&#95;&#95;(self, other[, modulo]) — возведение в степень, оператор **
&#95;&#95;lshift&#95;&#95;(self, other) — двоичный сдвиг влево, оператор <<
&#95;&#95;rshift&#95;&#95;(self, other) — двоичный сдвиг вправо, оператор >>
&#95;&#95;and&#95;&#95;(self, other) — двоичное И, оператор &
&#95;&#95;xor&#95;&#95;(self, other) — исключающее ИЛИ, оператор ^
&#95;&#95;or&#95;&#95;(self, other) — двоичное ИЛИ, оператор |

Отражённые арифметические операторы
Если в обычной арифметике между объектами a и b, объектом, который мы изменяем, является a, и объектом, с которым мы работаем, является b, то в отражённой арифметике наоборот — b является изменяемым, a — объектом, с которым мы работаем, и который передается в качестве аргумента.

Например:
```python
# Сложение, используется обычная арифметика и метод __add__ в объекте left:
>>> left + right
# Сложение, используется отражённая арифметика и метод __radd__ в объекте left:
>>> right + left
```

Список методов похож на тот, что используется в обычной арифметике, за исключением того, что добавляется префикс «r» ко всем методам:
&#95;&#95;radd&#95;&#95;(self, other) — сложение, оператор +
&#95;&#95;rsub&#95;&#95;(self, other) — вычитание, оператор -
&#95;&#95;rmul&#95;&#95;(self, other) — умножение, оператор *
&#95;&#95;rmatmul&#95;&#95;(self, other) — умножение матриц, оператор @
&#95;&#95;rtruediv&#95;&#95;(self, other) — деление, оператор /
&#95;&#95;rfloordiv&#95;&#95;(self, other) — целочисленное деление, оператор //
&#95;&#95;rmod&#95;&#95;(self, other) — остаток от деления, оператор %
&#95;&#95;rdivmod&#95;&#95;(self, other) — деление с остатком
&#95;&#95;rpow&#95;&#95;(self, other[, modulo]) — возведение в степень, оператор **
&#95;&#95;rlshift&#95;&#95;(self, other) — двоичный сдвиг влево, оператор <<
&#95;&#95;rrshift&#95;&#95;(self, other) — двоичный сдвиг вправо, оператор >>
&#95;&#95;rand&#95;&#95;(self, other) — двоичное И, оператор &
&#95;&#95;rxor&#95;&#95;(self, other) — исключающее ИЛИ, оператор ^
&#95;&#95;ror&#95;&#95;(self, other) — двоичное ИЛИ, оператор |

Составное присваивание
Эти методы — комбинация «обычного» оператора и присваивания. Возвращают тот же тип объекта, который будет присвоен переменной слева. Например:
x = 3
x += 2 # другими словами x = x + 2

&#95;&#95;iadd&#95;&#95;(self, other) — сложение с присваиванием, оператор +=
&#95;&#95;isub&#95;&#95;(self, other) — вычитание с присваиванием, оператор -=
&#95;&#95;imul&#95;&#95;(self, other) — умножение с присваиванием, оператор *=
&#95;&#95;imatmul&#95;&#95;(self, other) — умножение матриц с присваиванием, оператор @=
&#95;&#95;itruediv&#95;&#95;(self, other) — деление с присваиванием, оператор /=
&#95;&#95;ifloordiv&#95;&#95;(self, other) — целочисленное деление с присваиванием, оператор //=
&#95;&#95;imod&#95;&#95;(self, other) — остаток от деления с присваиванием, оператор %=
&#95;&#95;ipow&#95;&#95;(self, other[, modulo]) — возведение в степень с присваиванием, оператор **=
&#95;&#95;ilshift&#95;&#95;(self, other) — двоичный сдвиг влево с присваиванием, оператор <<=
&#95;&#95;irshift&#95;&#95;(self, other) — двоичный сдвиг вправо с присваиванием, оператор >>=
&#95;&#95;iand&#95;&#95;(self, other) — двоичное И с присваиванием, оператор &=
&#95;&#95;ixor&#95;&#95;(self, other) — исключающее ИЛИ с присваиванием, оператор ^=
&#95;&#95;ior&#95;&#95;(self, other) — двоичное ИЛИ с присваиванием, оператор |=

Преобразования типов
Помимо всего прочего, в Python множество методов, которые позволяют переопределять поведение встроенных функций преобразования типов, таких как int(...), float(...) и т.д. Например:
&#95;&#95;complex&#95;&#95;(self) — преобразование типа в комплексное число
&#95;&#95;int&#95;&#95;(self) — преобразование типа к int
&#95;&#95;float&#95;&#95;(self) — преобразование типа к float
&#95;&#95;index&#95;&#95;(self) — преобразование типа к int, когда объект используется в срезах (выражения вида [start:stop:step])
&#95;&#95;round&#95;&#95;(self[, ndigits]) — округление числа с помощью функции round(...)
&#95;&#95;trunc&#95;&#95;(self) — вызывается методом math.trunc(...)
&#95;&#95;floor&#95;&#95;(self) — вызывается методом math.floor(...)
&#95;&#95;ceil&#95;&#95;(self) — вызывается методом math.ceil(...)

Вызываемые объекты
&#95;&#95;call&#95;&#95;(self[, args...]) — позволяет любому экземпляру класса вести себя как обычная функция.

Например:

```python
>>> class Test:
>>>     def __call__(self, message):
>>>         print(message)
>>>         return True
>>>
>>> test = Test()
>>> test("Hello World")
... 'Hello World'
... True
```

&#95;&#95;await&#95;&#95;(self) — возвращает итератор, превращая класс в корутину, результат выполнения которой можно получить с помощью await. Подробнее об этом можно узнать в PEP 492.

Контекстные менеджеры
Любой объект может быть представлен как контекстный менеджер, который вызывается с помощью with или async with. Данная конструкция позволяет выполнить какие-либо действия по настройке объекта и при выходе из контекстного менеджера, произвести какие-либо действия по очистке, не смотря на то, было ли вызвано исключение в блоке контекстного менеджера.
&#95;&#95;enter&#95;&#95;(self) — определяет начало блока контекстного менеджера, вызванного с помощью with
&#95;&#95;exit&#95;&#95;(self, exc_type, exc_value, traceback) — определяет конец блока контекстного менеджера. Может использоваться для контролирования исключений, очистки, или любых действий, которые должны быть выполнены после блока внутри with. Если блок выполнился успешно, то все три аргумента (exc_type, exc_value и traceback) будут установлены в значение None.

Например:
```python
>>> class ContextManager:
>>>     def __enter__(self):
>>>         log("entering context")
>>>
>>>     def __exit__(self, exc_type, exc_value, traceback):
>>>         log("exiting context")
>>>
>>> with ContextManager():
...     print("in context manager")
...
... 'entering context'
... 'in context manager'
... 'exiting context'
```

&#95;&#95;aenter&#95;&#95;(self) — аналогично &#95;&#95;enter&#95;&#95;, только функция возвращает корутину (результат которой можно получить с помощью await)
&#95;&#95;aexit&#95;&#95;(self, exc_type, exc_value, traceback) — аналогично &#95;&#95;exit&#95;&#95;, только функция возвращает корутину (результат которой можно получить с помощью await)

Например:
```python
>>> class AsyncContextManager:
>>>     async def __aenter__(self):
>>>         await log("entering context")
>>>
>>>     async def __aexit__(self, exc_type, exc_value, traceback):
>>>         await log("exiting context")
>>>
>>> async with AsyncContextManager():
...     print("in context manager")
...
... 'entering context'
... 'in context manager'
... 'exiting context'
```

Неиспользуемые методы
Некоторые методы, после полного перехода с Python 2 на Python 3 стали устаревшими и больше не используются.
&#95;&#95;unicode&#95;&#95; — полностью исчез в версии Python 3, вместо него используются отдельные методы &#95;&#95;str_&#95;&#95; &#95;&#95;bytes&#95;&#95;
&#95;&#95;div&#95;&#95; — так как в Python 3 теперь по умолчанию «правильное деление», данного метода не существует
&#95;&#95;cmp&#95;&#95; — более не существует, вместо него используются &#95;&#95;lt&#95;&#95;, &#95;&#95;le&#95;&#95;, &#95;&#95;eq&#95;&#95;, &#95;&#95;ne&#95;&#95;, &#95;&#95;gt_&#95;&#95; &#95;&#95;ge&#95;&#95;
&#95;&#95;nonzero&#95;&#95; — переименован в &#95;&#95;bool&#95;&#95;

Упрощение работы с магическими методами
Большая часть из вышеописанных методов реализуется библиотеками, они позволяют использовать так называемые «обрёртки» над классами, в которых будут реализованы необходимые магические методы.

Пример таких библиотек:
dataclasses
attrs

Принципы и идеология этих (и других библиотек) схожи в одном – они позволяют реализовать всю необходимую логику работы с объектом, не дублируя код для каждого отдельного объекта.

Например:
```python
>>> from dataclasses import dataclass
>>>
>>> @dataclass(init=True, repr=True, eq=True, order=True, unsafe_hash=True)
>>> class Person:
>>>     first_name: str
>>>     last_name: str
>>>     age: int
```

Данный объект будет иметь в себе:
Три атрибута first_name, last_name и age, которые также будут передаваться в конструктор класса;
Будет реализован метод &#95;&#95;repr&#95;&#95; для вывода информации для отладки;
Будут реализованы все магические методы сравнения (такие как &#95;&#95;lt&#95;&#95;, &#95;&#95;eq&#95;&#95; и так далее), а также метод &#95;&#95;hash&#95;&#95;.

Чаще всего вы будете пользоваться уже готовыми решениями, как пример выше, но для того чтобы понять, как работает язык Python изнутри, необходимо знать, как работают магические методы, за что они отвечают, что будет, если вызвать ту или иную функцию на объект, и что с этим объектом произойдёт.


""",
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

```python
dataclass(*,
          init: bool = ...,
          repr: bool = ...,
          eq: bool = ...,
          order: bool = ...,
          unsafe_hash: bool = ...,
          frozen: bool = ...)
```

init         Нужно ли автоматически генерировать метод &#95;&#95;init&#95;&#95; для инициализации атрибутов класса.
repr         Нужно ли автоматически генерировать метод &#95;&#95;repr&#95;&#95; для вывода строкового представления объектов класса.
eq           Нужно ли автоматически генерировать метод &#95;&#95;eq&#95;&#95; для сравнения объектов класса.
order        Нужно ли автоматически генерировать методы &#95;&#95;lt&#95;&#95;, &#95;&#95;le&#95;&#95;, &#95;&#95;gt&#95;&#95;, &#95;&#95;ge&#95;&#95; для сравнения объектов класса.
unsafe_hash  Нужно ли автоматически генерировать метод &#95;&#95;hash&#95;&#95; для объектов класса.
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
""",
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
            "IPython": r"""
**Одиночный символ `%`**: Применяется для магических команд, которые действуют на одну строку в текущей ячейке.
**Двойной символ `%%`**: Применяется для ячеек с кодом, которые содержат блоки скриптов на различных языках (например, Python, Bash, Ruby).

| Команда            | Описание                                                                                  | Пример использования                                                                              |
|--------------------|-------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| `%%!`              | Выполняет команды оболочки в ячейке.                                                      | `%%!`<br>`echo "Hello, World!"`                                                                   |
| `%cpaste`          | Вставляет и выполняет блок кода, введённый вручную.                                       | `%cpaste`<br>`(вставить код)`<br>`--`                                                           |
| `%load`            | Загружает коды из файла в текущую ячейку.                                                 | `%load script.py`                                                                                 |
| `%pdb`             | Включает или выключает отладчик Python (pdb) при возникновении ошибок.                    | `%pdb on` или `%pdb off`                                                                          |
| `%%python2`        | Выполняет ячейку в интерпретаторе Python 2 (если установлен).                             | `%%python2`<br>`print "Hello from Python 2"`                                                      |
| `%sx`              | Выполняет команды оболочки и возвращает их результаты как список строк.                   | `output = %sx ls -l`<br>`print(output)`                                                           |
| `%%HTML`           | Отображает HTML-код в ячейке.                                                             | `%%HTML`<br>`<h1>Hello, World!</h1>`                                                              |
| `%ddir`            | Расширенный список атрибутов объекта.                                                     | `%ddir object_name`                                                                               |
| `%load_ext`        | Загружает расширение IPython.                                                             | `%load_ext autoreload`                                                                            |
| `%pdef`            | Показывает определение функции, включая аргументы.                                        | `%pdef function_name`                                                                             |
| `%%python3`        | Выполняет ячейку в интерпретаторе Python 3 (по умолчанию).                                | `%%python3`<br>`print("Hello from Python 3")`                                                     |
| `%%sx`             | Выполняет команды оболочки в ячейке и возвращает их результаты как список строк.          | `%%sx`<br>`ls -l`                                                                                 |
| `%%SVG`            | Отображает SVG-код в ячейке.                                                              | `%%SVG`<br>`<svg>...</svg>`                                                                       |
| `%debug`           | Начинает сессию отладки в точке вызова.                                                   | `%debug`                                                                                          |
| `%loadpy`          | Загружает и выполняет файл Python.                                                        | `%loadpy script.py`                                                                               |
| `%pdoc`            | Показывает строку документации объекта.                                                   | `%pdoc function_name`                                                                             |
| `%quickref`        | Показывает краткое руководство по IPython.                                                | `%quickref`                                                                                       |
| `%system`          | Выполняет команду оболочки.                                                               | `%system ls -l`                                                                                   |
| `%alias`           | Создаёт псевдоним для команды оболочки.                                                   | `%alias ll ls -l`                                                                                 |
| `%%debug`          | Начинает сессию отладки в ячейке (аналогично `%debug`, но для всей ячейки).               | `%%debug`<br>`buggy_function()`                                                                   |
| `%logoff`          | Отключает журналирование.                                                                 | `%logoff`                                                                                         |
| `%%perl`           | Выполняет код Perl в ячейке.                                                              | `%%perl`<br>`print "Hello from Perl\n";`                                                          |
| `%recall`          | Повторяет предыдущую команду или извлекает её по индексу из истории.                      | `%recall 42`                                                                                      |
| `%%system`         | Выполняет команды оболочки в ячейке.                                                      | `%%system`<br>`ls -l`                                                                             |
| `%alias_magic`     | Создаёт псевдоним для существующей магической команды IPython.                            | `%alias_magic t timeit`<br>`# Теперь можно использовать 't' вместо 'timeit'`<br>`t my_function()` |
| `%dhist`           | Показывает историю директорий, в которых вы работали.                                     | `%dhist`                                                                                          |
| `%logon`           | Включает журналирование.                                                                  | `%logon`                                                                                          |
| `%pfile`           | Открывает и показывает содержимое файла с кодом.                                          | `%pfile my_script.py`                                                                             |
| `%rehashx`         | Пересчитывает псевдонимы для всех исполняемых файлов в $PATH (для использования с `%sx`). | `%rehashx`                                                                                        |
| `%tb`              | Показывает traceback (стек вызовов) от последнего исключения.                             | `%tb`                                                                                             |
| `%autoawait`       | Устанавливает функцию ожидания по умолчанию для поддержки асинхронного кода.              | `%autoawait asyncio`                                                                              |
| `%dirs`            | Показывает список директорий в стеке директорий.                                          | `%dirs`                                                                                           |
| `%logstart`        | Начинает журналирование сессии.                                                           | `%logstart`                                                                                       |
| `%pinfo`           | Показывает информацию об объекте.                                                         | `%pinfo function_name`                                                                            |
| `%reload_ext`      | Перезагружает расширение IPython.                                                         | `%reload_ext autoreload`                                                                          |
| `%time`            | Измеряет время выполнения однострочного кода.                                             | `%time my_function()`                                                                             |
| `%autocall`        | Управляет автоматическим вызовом функций в IPython.                                       | `%autocall 1`                                                                                     |
| `%doctest_mode`    | Включает/выключает режим тестирования документации (doctest).                             | `%doctest_mode`                                                                                   |
| `%logstate`        | Показывает текущее состояние логирования.                                                 | `%logstate`                                                                                       |
| `%pinfo2`          | Показывает подробную информацию о объекте (дополненная версия `%pinfo`).                  | `%pinfo2 my_function`                                                                             |
| `%ren`             | Переименовывает переменную в среде IPython.                                               | `%ren old_variable new_variable`                                                                  |
| `%%time`           | Измеряет время выполнения всей ячейки.                                                    | `%%time`<br>`my_function()`                                                                       |
| `%autoindent`      | Включает или выключает автоматический отступ.                                             | `%autoindent`                                                                                     |
| `%echo`            | Отображает текст или значение переменной.                                                 | `%echo "Hello, World!"`                                                                           |
| `%logstop`         | Останавливает журналирование сессии.                                                      | `%logstop`                                                                                        |
| `%pip`             | Позволяет использовать pip для установки пакетов изнутри IPython.                         | `%pip install numpy`                                                                              |
| `%rep`             | Повторяет и выполняет последнюю команду.                                                  | `%rep`                                                                                            |
| `%timeit`          | Измеряет время выполнения многократного запуска однострочного кода.                       | `%timeit sum(range(10000))`                                                                       |
| `%automagic`       | Включает или выключает автоматическое распознавание магических команд без префикса `%`.   | `%automagic on`                                                                                   |
| `%ed`              | Открывает редактор для редактирования строки или блока кода.                              | `%ed script.py`                                                                                   |
| `%ls`              | Список файлов и директорий.                                                               | `%ls`                                                                                             |
| `%popd`            | Удаляет верхний каталог из стека директорий и переходит в новый верхний каталог.          | `%popd`                                                                                           |
| `%rerun`           | Повторяет последнюю команду с историей в ячейке.                                          | `%rerun`                                                                                          |
| `%%timeit`         | Измеряет время выполнения многократного запуска кода в ячейке.                            | `%%timeit`<br>`sum(range(10000))`                                                                 |
| `%%bash`           | Выполняет код Bash в ячейке.                                                              | `%%bash`<br>`echo "Hello from Bash"`                                                              |
| `%edit`            | Открывает редактор для редактирования строки или блока кода.                              | `%edit script.py`                                                                                 |
| `%lsmagic`         | Показывает список всех доступных магических команд.                                       | `%lsmagic`                                                                                        |
| `%pprint`          | Включает или выключает красивый вывод (pretty-printing) объектов.                         | `%pprint`                                                                                         |
| `%reset`           | Сбрасывает пространство имен IPython, удаляя все переменные и импортированные модули.     | `%reset`                                                                                          |
| `%unalias`         | Удаляет заданный псевдоним.                                                               | `%unalias ll`                                                                                     |
| `%bookmark`        | Управление закладками для директорий.                                                     | `%bookmark mydir /path/to/directory`                                                              |
| `%env`             | Установка переменных среды или просмотр текущих переменных среды.                         | `%env PATH=/new/path`                                                                             |
| `%macro`           | Определяет макрос для последовательности команд.                                          | `%macro my_macro 1-5`<br>`print("Hello")`                                                         |
| `%precision`       | Устанавливает количество отображаемых знаков после запятой.                               | `%precision 4`                                                                                    |
| `%reset_selective` | Сбрасывает только указанные переменные в пространстве имен IPython.                       | `%reset_selective my_variable`                                                                    |
| `%unload_ext`      | Выгружает указанное расширение IPython.                                                   | `%unload_ext autoreload`                                                                          |
| `%%capture`        | Перенаправляет вывод и ошибки в переменные.                                               | `%%capture output`<br>`print("Hello, World!")`                                                    |
| `%%file`           | Записывает содержимое ячейки в файл.                                                      | `%%file my_script.py`<br>`print("Hello, World!")`                                                 |
| `%magic`           | Показывает справку по магическим командам.                                                | `%magic`                                                                                          |
| `%prun`            | Выполняет код с профилированием с использованием cProfile.                                | `%prun my_function()`                                                                             |
| `%rmdir`           | Удаляет указанные директории.                                                             | `%rmdir directory_name`                                                                           |
| `%who`             | Показывает переменные и их типы в глобальном пространстве.                                | `%who`                                                                                            |
| `%cd`              | Изменяет текущую рабочую директорию.                                                      | `%cd /path/to/directory`                                                                          |
| `%gui`             | Устанавливает графический интерфейс для бэкенда IPython.                                  | `%gui qt`                                                                                         |
| `%mamba`           | Запускает установку пакетов с помощью Mamba (альтернатива pip).                           | `%mamba install numpy`                                                                            |
| `%%prun`           | Выполняет код с профилированием с использованием cProfile (для всей ячейки).              | `%%prun`<br>`my_function()`                                                                       |
| `%%ruby`           | Выполняет код Ruby в ячейке.                                                              | `%%ruby`<br>`puts "Hello from Ruby"`                                                              |
| `%who_ls`          | Показывает имена всех переменных в глобальном пространстве в виде списка.                 | `%who_ls`                                                                                         |
| `%cls`             | Очищает консольный вывод.                                                                 | `%cls`                                                                                            |
| `%hist`            | Показывает историю ввода.                                                                 | `%hist`                                                                                           |
| `%%markdown`       | Размечает содержимое ячейки как Markdown.                                                 | `%%markdown`<br>`# Заголовок`<br>`**Текст**`                                                      |
| `%psearch`         | Поиск по именам символов с использованием шаблона.                                        | `%psearch *function*`                                                                             |
| `%run`             | Запускает внешний скрипт Python или IPython.                                              | `%run my_script.py`                                                                               |
| `%whos`            | Показывает все переменные в текущем пространстве имен и их типы.                          | `%whos`                                                                                           |
| `%%cmd`            | Запускает команды Windows cmd в ячейке.                                                   | `%%cmd`<br>`dir`                                                                                  |
| `%history`         | Показывает историю ввода и вывода.                                                        | `%history -n 1-10`                                                                                |
| `%matplotlib`      | Включает встроенную поддержку matplotlib.                                                 | `%matplotlib inline`                                                                              |
| `%psource`         | Показывает исходный код объекта.                                                          | `%psource my_function`                                                                            |
| `%save`            | Сохраняет ввод и вывод ячейки в файл Python.                                              | `%save my_session.py 1-5`                                                                         |
| `%%writefile`      | Записывает содержимое ячейки в файл.                                                      | `%%writefile my_file.txt`<br>`Hello, World!`                                                      |
| `%code_wrap`       | Устанавливает или отключает авто-перенос строк для вывода кода.                           | `%code_wrap on`                                                                                   |
| `%%html`           | Размечает содержимое ячейки как HTML.                                                     | `%%html`<br>`<h1>Hello, World!</h1>`                                                              |
| `%micromamba`      | Запускает установку пакетов с помощью Micromamba (альтернатива pip).                      | `%micromamba install numpy`                                                                       |
| `%pushd`           | Добавляет текущую директорию в стек и переходит в новую директорию.                       | `%pushd /path/to/directory`                                                                       |
| `%sc`              | Выполняет код, используя Subprocess.                                                      | `%sc ls -l`                                                                                       |
| `%xdel`            | Удаляет переменные и объекты из сессии IPython.                                           | `%xdel my_variable`                                                                               |
| `%%code_wrap`      | Устанавливает или отключает авто-перенос строк для вывода кода в ячейке.                  | `%%code_wrap on`                                                                                  |
| `%%javascript`     | Выполняет JavaScript код в ячейке (для Jupyter Notebook).                                 | `%%javascript`<br>`console.log("Hello, World!")`                                                  |
| `%mkdir`           | Создает новую директорию.                                                                 | `%mkdir new_directory`                                                                            |
| `%pwd`             | Выводит текущую рабочую директорию.                                                       | `%pwd`                                                                                            |
| `%%script`         | Запускает ячейку с указанным интерпретатором (bash, python, ruby, etc).                   | `%%script bash`<br>`ls -l`                                                                        |
| `%xmode`           | Устанавливает уровень подробности трассировки для ошибок.                                 | `%xmode Verbose`                                                                                  |
| `%colors`          | Устанавливает цветовую схему для вывода в IPython.                                        | `%colors Linux`                                                                                   |
| `%%js`             | Выполняет JavaScript код в ячейке (для Jupyter Notebook).                                 | `%%js`<br>`console.log("Hello, World!")`                                                          |
| `%notebook`        | Запускает скрипт Python как блокнот Jupyter.                                              | `%notebook script.py`                                                                             |
| `%pycat`           | Показывает содержимое скрипта Python.                                                     | `%pycat script.py`                                                                                |
| `%set_env`         | Устанавливает переменные среды для текущей сессии IPython.                                | `%set_env PATH=/new/path`                                                                         |
| `%conda`           | Взаимодействует с conda для управления окружением и пакетами.                             | `%conda install numpy`                                                                            |
| `%killbgscripts`   | Останавливает все фоновые процессы выполнения скриптов.                                   | `%killbgscripts`                                                                                  |
| `%page`            | Отображает содержимое объекта с поддержкой постраничного просмотра.                       | `%page large_object`                                                                              |
| `%pylab`           | Загружает matplotlib и numpy для интерактивной работы в IPython.                          | `%pylab`                                                                                          |
| `%%sh`             | Выполняет команды Shell (sh) в ячейке.                                                    | `%%sh`<br>`ls -l`                                                                                 |
| `%config`          | Конфигурирует IPython и его расширения.                                                   | `%config IPCompleter.greedy=True`                                                                 |
| `%%latex`          | Размечает содержимое ячейки как LaTeX.                                                    | `%%latex`<br>`\begin{equation}`<br>`E = mc^2`<br>`\end{equation}`                                 |
| `%paste`           | Вставляет и выполняет блок кода, считанный из буфера обмена.                              | `%paste`                                                                                          |
| `%%pypy`           | Выполняет код Python с использованием интерпретатора PyPy.                                | `%%pypy`<br>`print("Hello, PyPy!")`                                                               |
| `%store`           | Сохраняет переменные в файл между сеансами IPython.                                       | `%store my_variable`                                                                              |
| `%copy`            | Копирует файлы между локальной файловой системой и файловой системой Jupyter Notebook.    | `%copy my_file.txt another_directory/`                                                            |
| `%ldir`            | Список файлов и директорий в локальной файловой системе.                                  | `%ldir`                                                                                           |
| `%pastebin`        | Отправляет содержимое ячейки на Pastebin и возвращает URL.                                | `%pastebin`                                                                                       |
| `%%python`         | Выполняет код Python в ячейке.                                                            | `%%python`<br>`print("Hello, Python!")`                                                           |
| `%%svg`            | Размечает содержимое ячейки как SVG (Scalable Vector Graphics).                           | `%%svg`<br>`<svg height="100" width="100"> ... </svg>`                                            |

""",
            "Флаги cmd": """
| Флаг                          | Пример запуска            | Описание |
|-------------------------------|---------------------------|----------|
| -c                            | python -c <код>           | Позволяет выполнить однострочный Python-код из командной строки. |
| -m                            | python -m                 | Позволяет запустить указанный Python-модуль как скрипт. |
| -i (или —interactive)         | python -i                 | Флаг -i запускает интерпретатор Python в интерактивном режиме после выполнения скрипта. |
| -O (или —optimize)            | python -O                 | Включает режим оптимизации, который удаляет отладочную информацию и выполняет оптимизации в байт-коде.<br>Это может уменьшить размер файлов .pyc и улучшить производительность, но осложнить отладку. |
| -B (или —dont-write-bytecode) | python -B                 | Предотвращает запись байт-кода (.pyc файлов) на диск. |
| -v (или —verbose)             | python -v                 | Выводит подробные сообщения о том, какие модули импортируются<br>и какие файлы открываются в процессе выполнения программы. |
| -q (или —quiet)               | python -q                 | Уменьшает уровень вывода, игнорируя сообщения о запуске и прочие информационные сообщения. |
| -E (или —ignore-environment)  | python -E                 | Игнорировать переменные окружения,<br>которые обычно влияют на поведение Python, такие как PYTHONPATH. |
| -u (или —unbuffered)          | python -u                 | Переключает режим не буферизованного ввода/вывода.<br>Полезно при работе с каналами и потоками данных,<br>чтобы гарантировать более немедленную обработку данных. |
| -h (или —help)                | python -h<br>python —help | Выведет список всех доступных флагов и их описания. |

```shell
>python -h
usage: python [option] ... [-c cmd | -m mod | file | -] [arg] ...
Options (and corresponding environment variables):
-b     : issue warnings about str(bytes_instance), str(bytearray_instance)
         and comparing bytes/bytearray with str. (-bb: issue errors)
-B     : do not write .pyc files on import; also PYTHONDONTWRITEBYTECODE=x
-c cmd : program passed in as string (terminates option list)
-d     : turn on parser debugging output (for experts only, only works on
         debug builds); also PYTHONDEBUG=x
-E     : ignore PYTHON* environment variables (such as PYTHONPATH)
-h     : print this help message and exit (also -? or --help)
-i     : inspect interactively after running script; forces a prompt even
         if stdin does not appear to be a terminal; also PYTHONINSPECT=x
-I     : isolate Python from the users environment (implies -E and -s)
-m mod : run library module as a script (terminates option list)
-O     : remove assert and __debug__-dependent statements; add .opt-1 before
         .pyc extension; also PYTHONOPTIMIZE=x
-OO    : do -O changes and also discard docstrings; add .opt-2 before
         .pyc extension
-P     : do not prepend a potentially unsafe path to sys.path; also PYTHONSAFEPATH
-q     : do not print version and copyright messages on interactive startup
-s     : do not add user site directory to sys.path; also PYTHONNOUSERSITE
-S     : do not imply 'import site' on initialization
-u     : force the stdout and stderr streams to be unbuffered;
         this option has no effect on stdin; also PYTHONUNBUFFERED=x
-v     : verbose (trace import statements); also PYTHONVERBOSE=x
         can be supplied multiple times to increase verbosity
-V     : print the Python version number and exit (also --version)
         when given twice, print more information about the build
-W arg : warning control; arg is action:message:category:module:lineno
         also PYTHONWARNINGS=arg
-x     : skip first line of source, allowing use of non-Unix forms of #!cmd
-X opt : set implementation-specific option
--check-hash-based-pycs always|default|never:
         control how Python invalidates hash-based .pyc files
--help-env      : print help about Python environment variables and exit
--help-xoptions : print help about implementation-specific -X options and exit
--help-all      : print complete help information and exit
Arguments:
file   : program read from script file
-      : program read from stdin (default; interactive mode if a tty)
arg ...: arguments passed to program in sys.argv[1:]
```
""",
            "with as": """with
В начале блока кода with вызывает метод &#95;&#95;enter&#95;&#95; у объекта,
  который используется для подготовки контекста.
После того как код внутри блока завершился, вызывается метод &#95;&#95;exit&#95;&#95;,
  который используется для освобождения ресурсов.
Контекстный менеджер with удобен для использования,
  так как он автоматически освобождает ресурсы в конце блока кода, что избавляет
  от необходимости ручного закрытия файла или освобождения других ресурсов.
Контекстный менеджер with может быть использован не только с файлами,
  но и с другими объектами, которые поддерживают методы &#95;&#95;enter&#95;&#95; и &#95;&#95;exit&#95;&#95;.
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

В настоящее время поддерживаются три флага преобразования: '!s'который вызывает str() значение, '!r'который вызывает repr() и '!a'который вызывает ascii().

Некоторые примеры:

```python
"Harold's a clever {0!s}"        # Calls str() on the argument first
"Bring out the holy {name!r}"    # Calls repr() on the argument first
"More {!a}"                      # Calls ascii() on the argument first
```


format_spec     ::= [[ fill] align][ sign][z][#][0][ width][ grouping_option][. precision][ type]
заполнить       ::= <любой символ>
выровнять       ::= "<" | ">" | "=" | "^"
знак            ::= "+" | "-" | " "
ширина          ::= digit+
grouping_option ::= "_" | ","
точность        ::= digit+
тип             ::= "b" | "c" | "d" | "e" | "E" | "f" | "F" | "g" | "G" | "n" | "o" | "s" | "x" | "X" | "%"

Вариант Значение
'`<`'     Принудительно выравнивает поле по левому краю в доступном пространстве 
        (это значение по умолчанию для большинства объектов).
'`>`'     Принудительно выравнивает поле по правому краю в доступном пространстве (это значение по умолчанию для чисел).
'`=`'     Принудительно размещает заполнение после знака (если есть), но перед цифрами. 
        Это используется для печати полей в форме «+000000120». 
        Этот параметр выравнивания действителен только для числовых типов. 
        Он становится значением по умолчанию для чисел, когда «0» непосредственно предшествует ширине поля.
'`^`'     Центрирует поле в доступном пространстве.
Параметр знака действителен только для числовых типов и может быть одним из следующих:

Вариант Значение

'`+`'     указывает, что знак должен использоваться как для положительных, так и для отрицательных чисел.
'`-`'     указывает, что знак следует использовать только для отрицательных чисел (это поведение по умолчанию).
spase   указывает, что перед положительными числами следует использовать начальный пробел, а перед отрицательными — знак минус.

Параметр '`z`' приводит отрицательные нулевые значения с плавающей запятой к положительным нулям после округления до точности формата. 
Этот параметр действителен только для типов представления с плавающей запятой.


Опция '`#`' приводит к использованию «альтернативной формы» для преобразования. 
          Альтернативная форма определяется по-разному для разных типов. 
          Этот параметр действителен только для целых, плавающих и сложных типов. 
          Для целых чисел, когда используется двоичный, восьмеричный или шестнадцатеричный вывод, 
          эта опция добавляет соответствующий префикс '`0b`', '`0o`', '`0x`'или '`0X`'к выходному значению. 
          Для чисел с плавающей запятой и сложных альтернативная форма приводит к тому, что результат 
          преобразования всегда содержит символ десятичной точки, даже если за ним не следуют цифры. 
          Обычно символ десятичной точки появляется в результате этих преобразований только в том случае, 
          если за ним следует цифра. Кроме того, для преобразований '`g`'и '`G`' конечные нули не удаляются из результата.
Опция '`,`'сигнализирует об использовании запятой для разделителя тысяч. 
         Для разделителя, учитывающего локаль, '`n`' вместо этого используйте целочисленный тип представления.
Опция '`_`'сигнализирует об использовании подчеркивания для разделителя тысяч для типов представления с плавающей 
         запятой и для целочисленного типа представления '`d`'. 
         Для целочисленных типов представления '`b`', '`o`', '`x`'и '`X`'символы подчеркивания будут вставлены 
         через каждые 4 цифры. Для других типов презентаций указание этой опции является ошибкой.
ширина — десятичное целое число, определяющее минимальную общую ширину поля, включая все префиксы, 
         разделители и другие символы форматирования. Если не указано, то ширина поля будет определяться содержимым.
Если явное выравнивание не задано, перед полем ширины'`0`' ставится нулевой символ ( ), 
         что позволяет использовать заполнение нулями с учетом знака для числовых типов. 
         Это эквивалентно символу заполнения'`0`' с типом выравнивания'`=`' .
установка перед полем ширины '`0`' больше не влияет на выравнивание строк по умолчанию.

Точность представляет собой десятичное целое число , указывающее, сколько цифр должно отображаться после десятичной 
точки для типов представления '`f`'и '`F`', или до и после десятичной точки для типов представления '`g`'или '`G`'. 
Для типов строкового представления поле указывает максимальный размер поля, другими словами, сколько символов 
будет использовано из содержимого поля. Точность не допускается для целочисленных типов представления .


Доступные типы представления строк:

Тип    Значение
'`s`'    Формат строки. Это тип по умолчанию для строк, и его можно опустить.
None   То же, что '`s`'.

Доступные типы целочисленного представления:

Тип   Значение
'`b`'   Двоичный формат. Выводит число по основанию 2.
'`c`'   Характер. Преобразует целое число в соответствующий символ Юникода перед печатью.
'`d`'   Десятичное целое. Выводит число в базе 10.
'`o`'   Восьмеричный формат. Выводит число по основанию 8.
'`x`'   Шестнадцатеричный формат. Выводит число по основанию 16, используя строчные буквы для цифр выше 9.
'`X`'   Шестнадцатеричный формат. Выводит число по основанию 16, используя прописные буквы для цифр выше 9. Если '#' указано, префикс '0x' также будет прописным '0X'.
'`n`'   Число. Это то же самое '`d`', что и , за исключением того, что он использует текущую настройку локали для вставки соответствующих символов-разделителей чисел.
None  То же, что ' 

Доступные типы представления для floatи Decimalзначений:

Тип    Значение
'`e`'    Научная нотация. Для заданной точности pформатирует число в экспоненте с буквой «e», отделяющей коэффициент от показателя степени. 
       Коэффициент имеет одну цифру до и pцифры после запятой, всего значащих цифр. 
       Без заданной точности использует точность цифр после запятой для и показывает все цифры коэффициента для. 
       Если за десятичной точкой не следуют цифры, десятичная точка также удаляется, если не используется этот параметр.p + 16floatDecimal#
'`E`'    Научная нотация. То же, что и '`e`' за исключением того, что в качестве символа-разделителя используется заглавная буква «E».
'`f`'    Обозначение с фиксированной точкой. Для заданной точности pформатирует число как десятичное число, 
       в котором pпосле запятой следуют только цифры. 
       Без заданной точности использует точность 6цифр после запятой для floatи использует точность, 
       достаточную для отображения всех цифр коэффициента для Decimal. 
       Если за десятичной точкой не следуют цифры, десятичная точка также удаляется, если не #используется этот параметр.
'`F`'    Обозначение с фиксированной точкой. То же , что и '`f`', но преобразуется nanв NANи infв INF.
'`g`'    Общий формат. Для заданной точности это округляет число до значащих цифр, а затем форматирует результат 
       либо в формате с фиксированной запятой, либо в экспоненциальном представлении, в зависимости от его величины. 
       Точность рассматривается как эквивалентная точности .p >= 1p01
Точные правила таковы: предположим, что результат, отформатированный с типом представления '`e`' и точностью p-1, 
будет иметь показатель степени exp. Затем, если , где -4 для чисел с плавающей запятой и -6 для , число форматируется с типом представления и точностью . 
В противном случае число форматируется с типом представления и точностью . В обоих случаях из мантиссы удаляются незначащие конечные нули, а также 
удаляется десятичная точка, если за ней не следуют оставшиеся цифры, если не используется опция.m <= exp < pmDecimals 'f' p-1-exp 'e' p-1 '#'
Без заданной точности использует точность 6 значащих цифр для float. При Decimalкоэффициент результата формируется из цифр коэффициента значения; 
научное обозначение используется для значений, меньших 1e-6абсолютного значения, и значений, 
в которых разрядное значение младшей значащей цифры больше 1, а в противном случае используется обозначение с фиксированной запятой.
Положительная и отрицательная бесконечность, положительные и отрицательные нули и нанс форматируются как , , и infсоответственно -inf, 0независимо от точности.-0nan
'`G`'    Общий формат. То же, что и '`g`' за исключением переключения, '`E`' если число становится слишком большим. Представления бесконечности и NaN также в верхнем регистре.
'`n`'    Число. Это то же самое '`g`', что и , за исключением того, что он использует текущую настройку локали для вставки соответствующих символов-разделителей чисел.
'`%`'    Процент. Умножает число на 100 и отображает в фиксированном ('`f`') формате, за которым следует знак процента.
Никто  Поскольку floatэто то же самое '`g`', что и , за исключением того, что когда для форматирования результата используется запись с 
фиксированной точкой, он всегда включает по крайней мере одну цифру после десятичной точки. Используемая точность настолько велика, насколько это необходимо для точного представления заданного значения.
Для Decimalэто то же самое, что '`g`' или '`G`' в зависимости от значения context.capitalsдля текущего десятичного контекста. 
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
""",
        },
        "SQL": {
            "Разное": """
|       |           |
|:------|-----------|
Индексирование базы данных | Процесс создания специальной структуры данных, которая позволяет быстро<br>находить нужные записи в базе данных. Индексы могут быть созданы для отдельных<br>полей или сочетаний полей в таблице базы данных. Как правило, индексы<br>упорядочивают записи в базе данных по определенному полю или полям,<br>что позволяет быстро находить нужные записи путем поиска в упорядоченном списке.<br>Индексы также могут улучшить производительность базы данных при выполнении<br>различных операций, таких как сортировка и группировка данных.
AVERAGE (функция среднего) | Функция, которая вычисляет среднее значение выборки данных.<br>Она работает так: суммирует все значения в выборке и<br>делит результат на количество значений.<br>Например, если у нас есть таблица с четырьмя строками и одним столбцом,<br>содержащим числа 10, 20, 30 и 40, то среднее значение будет равно 25.<br>Это можно посчитать, суммируя все числа (10 + 20 + 30 + 40)<br>и деля полученный результат (100) на количество чисел (4), что даст 25.
Оконные функции            | Функции баз данных, которые выполняют операции над наборами данных,<br>называемыми "окнами". Окна - это наборы строк в таблице, которые определяются<br>каким-либо критерием (например, временным интервалом,<br>порядковым номером и т. д.).<br>Оконные функции позволяют совершать различные операции над этими наборами строк,<br>например, вычислять агрегатные функции (среднее, сумма, минимум и т. д.),<br>применять фильтры и группировки, выполнять ранжирование.<br>Оконные функции обычно используются с оператором OVER, который определяет<br>окно данных, над которыми будут выполняться операции.<br>Например, чтобы вычислить среднее значение поля "Зарплата" для каждой строки<br>в таблице, можно использовать следующий запрос: ```sql SELECT AVERAGE(Salary) OVER (PARTITION BY Department) FROM Employees;``` В этом примере функция AVERAGE вычисляет среднее<br>значение поля "Зарплата" для каждой группы строк
PARTITION BY               | Это часть оконных функций в базах данных, который используется для разбиения<br>набора строк на группы, называемые "партициями".Каждая партиция - это набор строк<br>с общими свойствами, определяемыми критерием, указанным в PARTITION BY<br>Может использоваться совместно с другими операторами,<br>такими как ORDER BY и ROWS/RANGE, чтобы определить окно данных более точно.<br>Например, чтобы вычислить среднее значение поля "Зарплата" для каждого отдела,<br>но учитывая только последние 3 месяца, можно использовать следующий запрос:<br>SELECT AVERAGE(Salary)<br>   OVER (PARTITION BY Department<br>ORDER BY Month<br>ROWS BETWEEN 2 PRECEDING AND CURRENT ROW)<br>FROM Employees;<br>В этом примере функция AVERAGE будет вычислять среднее значение поля "Зарплата"<br>для каждой партиции (то есть для каждого отдела), учитывая только строки,<br>упорядоченные по полю "Месяц" и относящиеся к<br>последним 3 месяцам (включая текущий).<br>
PRECEDING                  | Это часть оконных функций в базах данных, который используется для<br>определения окна данных в терминах количества строк,<br>находящихся до текущей строки.<br>Например, чтобы вычислить сумму последних 3 строк в таблице,<br>можно использовать следующий запрос:<br>```sql SELECT SUM(Value) OVER (ORDER BY Id ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) FROM Table;```<br>В этом примере функция SUM будет вычислять сумму значений поля "Value"<br>для каждой строки, учитывая только строки, упорядоченные по полю "Id"<br>и находящиеся до текущей строки на 2 строки (включая текущую).<br>Оператор PRECEDING может использоваться совместно с другими операторами,<br>такими как PARTITION BY и RANGE, чтобы определить окно данных более точно.
""",
            "JOIN": """
|                                                    |                                                                                                                                                                                                                                                                                                                      |
|----------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| JOIN                                               | Используется для соединения двух таблиц в одну.<br>Существует ряд различных видов JOIN, каждый из которых имеет свои особенности<br>и применяется в зависимости от ситуации.<br>INNER JOIN, LEFT JOIN, RIGHT JOIN, FULL OUTER JOIN,<br>CROSS JOIN, NATURAL JOIN, UNION JOIN, STRAIGHT_JOIN, OUTER APPLY, CROSS APPLY |
| INNER JOIN - это самый распространенный вид JOIN   | Соединяет две таблицы по совпадающим значениям определенных полей.<br>Результатом является таблица, содержащая только те строки,<br>которые совпадают по заданным полям.                                                                                                                                             |
| LEFT JOIN аналогичен INNER JOIN                    | Результирующая таблица содержит все строки из левой (первой) таблицы,<br>даже если они не совпадают по заданным полям со второй таблицей.<br>Несовпадающие строки заполняются нулевыми значениями                                                                                                                    |
| RIGHT JOIN аналог LEFT JOIN                        | Результирующая таблица содержит все строки из правой (второй) таблицы,<br>даже если они не совпадают по заданным полям с первой таблицей.<br>Несовпадающие строки заполняются нулевыми значениями.                                                                                                                   |
| FULL OUTER JOIN комбинация LEFT JOIN и RIGHT JOIN. | Результирующая таблица содержит все строки из обоих таблиц,<br>даже если они не совпадают по заданным полям.<br>Несовпадающие строки заполняются нулевыми значениями.                                                                                                                                                |
| CROSS JOIN                                         | Cоединяет все строки из первой таблицы со всеми строками из второй таблицы,<br>создавая картежи, удовлетворяющие условию соединения.<br>Таким образом, CROSS JOIN не учитывает совпадающие<br>значения в таблицах и создает все возможные картежи.                                                                   |

```sql
SELECT * FROM Table1
FULL OUTER JOIN Table2
ON Table1.Field1 = Table2.Field1;
```

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

|           |                                                                                                                                                                                                                                                                                                                                                |
|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| MAX       | Возвращает максимальное значение из списка аргументов.<br>может использоваться с числовыми и дата/время типами данных.<br>`SELECT MAX(amount) FROM sales;`                                                                                                                                                                                     |
| MIN       | Возвращает минимальное значение из списка аргументов.<br>может использоваться с числовыми и дата/время типами данных.<br>`SELECT MIN(amount) FROM sales;`                                                                                                                                                                                      |
| SUM       | Возвращает сумму аргументов.<br>может использоваться только с числовыми типами данных.<br>`SELECT SUM(amount) FROM sales;`                                                                                                                                                                                                                     |
| AVG       | Возвращает среднее арифметическое аргументов.<br>может использоваться только с числовыми типами данных.<br>`SELECT AVG(amount) FROM sales;`                                                                                                                                                                                                    |
| COUNT     | Возвращает количество аргументов.<br>может использоваться с различными типами данных.<br>`SELECT COUNT(amount) FROM sales;`                                                                                                                                                                                                                    |
| CONCAT    | Соединяет строки.<br>может использоваться с типом данных строка.<br>`SELECT CONCAT(first_name, ' ', last_name) as full_name FROM customers;`                                                                                                                                                                                                   |
| UPPER     | Преобразует строку в верхний регистр.<br>может использоваться с типом данных строка.<br>`SELECT UPPER(first_name) as first_name, UPPER(last_name) as last_name FROM customers;`                                                                                                                                                                |
| LOWER     | Преобразует строку в нижний регистр.<br>может использоваться с типом данных строка.<br>`SELECT LOWER(first_name) as first_name, LOWER(last_name) as last_name FROM customers;`                                                                                                                                                                 |
| SUBSTR    | Извлекает подстроку из строки. (столбец, первый символ, количество символов)<br>может использоваться с типом данных строка.<br>`SELECT SUBSTR(phone, 1, 3) as area_code FROM customers;`                                                                                                                                                       |
| TRIM      | Удаляет пробелы из начала и конца строки.<br>может использоваться с типом данных строка.<br>`SELECT TRIM(first_name) as first_name, last_name FROM customers;`                                                                                                                                                                                 |
| LENGTH    | Возвращает количество символов в строке.<br>может использоваться с типом данных строка.<br>`SELECT first_name, LENGTH(first_name) as name_length FROM customers;`                                                                                                                                                                              |
| ROUND     | Округляет число до указанной точности. (столбец, кол-во знаков после запятой)<br>может использоваться с типом данных число.<br>`SELECT product, ROUND(price, 2) as price FROM sales;`                                                                                                                                                          |
| DATE      | Преобразует строку в формат даты. (хз проверить на питоне надо)<br>может использоваться с типом данных строка и возвращает тип данных дата.<br>`SELECT DATE(order_date) as order_date, product, price FROM orders;`                                                                                                                            |
| TIME      | Преобразует строку в формат времени. (хз проверить на питоне надо)<br>может использоваться с типом данных строка и возвращает тип данных время.<br>`SELECT TIME(meeting_time) as meeting_time, topic FROM meetings;`                                                                                                                           |
| DATETIME  | Преобразует строку в формат даты и времени.<br>может использоваться с типом данных строка и возвращает тип данных дата/время.<br>`SELECT DATETIME(event_date_time) as event_date_time, event_name FROM events;`                                                                                                                                |
| TIMESTAMP | Преобразует строку в формат времени с меткой времени (timestamp). <br>может использоваться с типом данных строка и возвращает тип данных timestamp.<br>`SELECT TIMESTAMP(log_timestamp) as log_timestamp, log_message FROM logs;`                                                                                                              |
| NOW       | Возвращает текущую дату и время.<br>не требует аргументов и возвращает тип данных timestamp.<br>`INSERT INTO orders (order_date, product, price) VALUES (NOW(), 'Shoes', 59.99);`                                                                                                                                                              |
| COALESCE  | Принимает неограниченное количество аргументов и возвращает первый ненулевой аргумент (???)<br>может использоваться с типами данных число, строка, дата/время и возвращает тип данных, соответствующий первому ненулевому аргументу.<br>`SELECT first_name, last_name, COALESCE(email, '') as email, COALESCE(phone, '') as phone FROM users;` |
| ISNULL    | Проверяет, является ли значение нулевым (NULL).<br>принимает один аргумент и возвращает логическое значение true, если аргумент равен NULL, и false, если аргумент не равен NULL.<br>`SELECT first_name, last_name, position FROM employees WHERE ISNULL(bonus);`                                                                              |
| IFNULL    | Проверяет, является ли значение нулевым (NULL).<br>принимает два аргумента и возвращает первый аргумент, если он не равен NULL, и второй аргумент, если первый равен NULL.<br>`SELECT name, price, IFNULL(description, 'No description') as description FROM products;`                                                                        |

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
```sql
SELECT name, price, IIF(quantity > 0, 'In stock', 'Out of stock') as stock_status FROM products;
```

ROW_NUMBER - используется для нумерации строк в результирующем наборе данных. 
             используется совместно с оператором ORDER BY для сортировки строк по определенному критерию.
```sql
SELECT ROW_NUMBER() OVER (ORDER BY quantity) as row_num, product_name, quantity, price FROM sales;
```

RANK - используется для нумерации строк в результирующем наборе данных. 
       используется совместно с оператором ORDER BY для сортировки строк по определенному критерию.
       (Отличие RANK от ROW_NUMBER заключается в том, что RANK нумерует строки с учетом их значений. 
        Например, если у нас есть несколько строк с одинаковым значением, то RANK будет устанавливать им ранг 
        с учетом этого одинакового значения, а не просто нумеровать их в порядке возрастания.)
       (Обратите внимание, что если бы у нас были строки с одинаковым значением количества, то они бы получили одинаковый ранг.)
```sql
SELECT RANK() OVER (ORDER BY quantity) as row_num, product_name, quantity, price FROM sales;
```

DENSE_RANK - используется для нумерации строк в результирующем наборе данных. 
             используется совместно с оператором ORDER BY для сортировки строк по определенному критерию.
             (Отличие DENSE_RANK от RANK заключается в том, что DENSE_RANK нумерует строки с учетом их значений, 
              но не оставляет промежутки между рангами. Таким образом, если у нас есть несколько строк с одинаковым значением, 
              то DENSE_RANK будет устанавливать им ранг с учетом этого одинакового значения, но не оставляет промежутки между рангами.)
             (Обратите внимание, что если бы у нас были строки с одинаковым значением количества, то они бы получили одинаковый ранг.
              Отличие от RANK заключается в том, что DENSE_RANK не оставляет промежутки между рангами.)
```sql
SELECT DENSE_RANK() OVER (ORDER BY quantity) as row_num, product_name, quantity, price FROM sales;
```

NTILE - используется для разбиения результирующего набора данных на равные части. 
        используется совместно с оператором ORDER BY для сортировки строк по определенному критерию.
        (разбить эту таблицу на 3 равные части и пронумеровать каждую строку с учетом ее нахождения в этой части)
```sql
SELECT NTILE(3) OVER (ORDER BY quantity) as group_num, product_name, quantity, price FROM sales;
```

LAG - используется для получения значения из предыдущей строки результирующего набора данных. 
      используется для сравнения значений в разных строках или для вычисления разницы между значениями.
      (получить таблицу с колонкой, содержащей разницу между ценой текущей строки и ценой предыдущей строки.)
```sql
SELECT product_name, price, LAG(price, 1) OVER (ORDER BY date) as prev_price, price - LAG(price, 1) OVER (ORDER BY date) as price_diff FROM sales;
```

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
""",
            "Картинки": r"""
<img alt="sql.png" src="Языки\SQL\sql.png">
""",
            "SQLite3 Date And Time Format": """
copied from https://www.sqlite.org/lang_datefunc.html

## Overview
SQLite supports seven scalar date and time functions as follows:

1. `date(time-value, modifier, modifier, ...)`  YYYY-MM-DD
2. `time(time-value, modifier, modifier, ...)`  HH:MM:SS or as HH:MM:SS.SSS
3. `datetime(time-value, modifier, modifier, ...)`  YYYY-MM-DD HH:MM:SS or as YYYY-MM-DD HH:MM:SS.SSS
4. `julianday(time-value, modifier, modifier, ...)`  - the fractional number of days since noon in Greenwich on November 24, 4714 B.C.
5. `unixepoch(time-value, modifier, modifier, ...)`  unix timestamp
6. `strftime(format, time-value, modifier, modifier, ...)`
7. `timediff(time-value, time-value)`

|    |                                                             |
|----|-------------------------------------------------------------|
| %d | day of month: `01-31`                                       |
| %e | day of month without leading zero: `1-31`                   |
| %f | fractional seconds: SS.SSS                                  |
| %F | ISO 8601 date: `YYYY-MM-DD`                                 |
| %G | ISO 8601 year corresponding to `%V`                         |
| %g | 2-digit ISO 8601 year corresponding to `%V`                 |
| %H | hour: `00-24`                                               |
| %I | hour for 12-hour clock: `01-12`                             |
| %j | day of year: `001-366`                                      |
| %J | Julian day number (fractional)                              |
| %k | hour without leading zero: `0-24`                           |
| %l | %I without leading zero: `1-12`                             |
| %m | month: `01-12`                                              |
| %M | minute: `00-59`                                             |
| %p | "`AM`" or "`PM`" depending on the hour                      |
| %P | "`am`" or "`pm`" depending on the hour                      |
| %R | ISO 8601 time: `HH:MM`                                      |
| %s | seconds since `1970-01-01`                                  |
| %S | seconds: `00-59`                                            |
| %T | ISO 8601 time: `HH:MM:SS`                                   |
| %U | week of year (`00-53`) - week 01 starts on the first Sunday |
| %u | day of week `1-7` with Monday==1                            |
| %V | ISO 8601 week of year                                       |
| %w | day of week `0-6` with Sunday==0                            |
| %W | week of year (`00-53`) - week 01 starts on the first Monday |
| %Y | year: `0000-9999`                                           |
| %% | %                                                           |

| Function         | Equivalent `strftime()`             |
|------------------|-------------------------------------|
| `date(...)`      | `strftime('%F', ...)`               |
| `time(...)`      | `strftime('%T', ...)`               |
| `datetime(...)`  | `strftime('%F %T', ...)`            |
| `julianday(...)` | `CAST(strftime('%J', ...) as REAL)` |
| `unixepoch(...)` | `CAST(strftime('%s', ...) as INT)`  |

```sql
SELECT timediff('2023-02-15','2023-03-15');
```

## Time Values
A time-value can be in any of the following formats shown below.
The value is usually a string, though it can be an integer or floating point number in the case of format 12.

1. `YYYY-MM-DD`
2. `YYYY-MM-DD HH:MM`
3. `YYYY-MM-DD HH:MM:SS`
4. `YYYY-MM-DD HH:MM:SS.SSS`
5. `YYYY-MM-DDTHH:MM`
6. `YYYY-MM-DDTHH:MM:SS`
7. `YYYY-MM-DDTHH:MM:SS.SSS`
8. `HH:MM`
9. `HH:MM:SS`
10. `HH:MM:SS.SSS`
11. `now`
12. `DDDDDDDDDD`


## Modifiers
For all date/time functions other than `timediff()`, the time-value argument can be followed by zero or more modifiers that alter date and/or time.
Each modifier is a transformation that is applied to the time-value to its left.
Modifiers are applied from left to right; order is important.
The available modifiers are as follows.

1. `NNN days`
2. `NNN hours`
3. `NNN minutes`
4. `NNN seconds`
5. `NNN months`
6. `NNN years`
7. `±HH:MM`
8. `±HH:MM:SS`
9. `±HH:MM:SS.SSS`
10. `±YYYY-MM-DD`
11. `±YYYY-MM-DD HH:MM`
12. `±YYYY-MM-DD HH:MM:SS`
13. `±YYYY-MM-DD HH:MM:SS.SSS`
14. `ceiling`
15. `floor`
16. `start of month`
17. `start of year`
18. `start of day`
19. `weekday N`
20. `unixepoch`
21. `julianday`
22. `auto`
23. `localtime`
24. `utc`
25. `subsec`
26. `subsecond`

""",
        },
        "RegExp": {
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
| ^        | Начало всего текста или начало строчки текста, если `flags=re.MULTILINE`        |
| $        | Конец всего текста или конец строчки текста, если `flags=re.MULTILINE`          |
| \A       | Строго начало всего текста                                                      |
| \Z       | Строго конец всего текста                                                       |
| \b       | Начало или конец слова (слева пусто или не-буква, справа буква и наоборот)      |
| \B       | Не граница слова: либо и слева, и справа буквы, либо и слева, и справа НЕ буквы |


# Условные выражения

| Условное выражение |                                                                      | Регулярка          | Соответствие |
|--------------------|----------------------------------------------------------------------|--------------------|--------------|
| (?=...)            | Позитивный просмотр вперёд                                           | Людовик(?=XVI)     | ЛюдовикXV, <span style="background-color: #999999; color: #FFFFFF">Людовик</span>XVI, <span style="background-color: #999999; color: #FFFFFF">Людовик</span>XVIII, ЛюдовикLXVII, ЛюдовикXXL |
| (?!...)            | Негативный просмотр вперёд                                           | Людовик(?!XVI)     | <span style="background-color: #999999; color: #FFFFFF">Людовик</span>XV, ЛюдовикXVI, ЛюдовикXVIII, <span style="background-color: #999999; color: #FFFFFF">Людовик</span>LXVII, <span style="background-color: #999999; color: #FFFFFF">Людовик</span>XXL |
| (?<=...)           | Позитивный просмотр назад<br>Длина шаблона должна быть фиксированной | (?<=Сергей )Иванов | Сергей <span style="background-color: #999999; color: #FFFFFF">Иванов</span>, Игорь Иванов |
| (?<!...)           | Негативный просмотр назад                                            | (?<!Сергей )Иванов | Сергей Иванов, Игорь <span style="background-color: #999999; color: #FFFFFF">Иванов</span> |

# Группы захвата

| Группа захвата       | Название                    | Регулярка                    | Соответствие |
|----------------------|-----------------------------|------------------------------|--------------------------------------------------------------------------------|
| (?:pattern)          | Незахватывающая группа      | (?:abc\|def)                 | 123 <span style="background-color: #999999; color: #FFFFFF">abc</span> 456     |
| (?P&lt;name>pattern) | Именованная группа захвата  | My name is (?P&lt;name>\w+)  | My name is <span style="background-color: #999999; color: #FFFFFF">John</span><br>`re.compile(r"My name is (?P<name>\w+)")`<br>`.match("My name is John")`<br>`.group("name")`<br>`# John` |
| (?P=name)            | Именованная обратная ссылка<br>Позволяет ссылаться на ранее захваченные группы по имени | (?P&lt;word>\w+)\s+(?P=word) | <span style="background-color: #999999; color: #FFFFFF">hello hello</span>     |

# Другое

| Паттерн     | Название | Регулярка |   |
|-------------|----------|-----------|---|
| (?>pattern) | Атомарная группа<br>Захватывает подстроку<br>и запрещает бэктрекинг*<br>внутри этой группы,<br>если остальная часть<br>шаблона не совпала. | `(?>\d{3})\d`<br>Эта конструкция сначала пытается<br>сопоставить `\d{3}`, а затем `\d`.<br>Если первое выражение не совпадает,<br>оно не пытается вернуться назад. | <span style="background-color: #999999; color: #FFFFFF">1234</span> |
| (?R) или (?0) | Рекурсивный шаблон<br>Вставляет текущее регулярное<br>выражение внутрь самого себя. | `\((?:[^()]+|(?R))*\)`<br>Это регулярное выражение<br>сопоставляет сбалансированные скобки.<br>`re.error: unknown extension ?R at position 13` | <span style="background-color: #999999; color: #FFFFFF">(a(b)c)</span> |
| (?P&lt;name1>pattern1\|(?P&lt;name2>pattern2)) | Условные выражения<br>с именованными группами |  | `re.compile(`<br>`r"(?P<name1>pattern1|"`<br>`r"(?P<name2>pattern2))"`<br>`)`<br>`.match("pattern2")`<br>`.groupdict()`<br>{<br>"name1": "pattern2",<br>"name2": "pattern2",<br>} |


# Флаги
https://docs.python.org/3/library/re.html#flags

|               |      |        |
|---------------|------|--------|
| re.ASCII      | (?a) | По умолчанию \w, \W, \b, \B, \d, \D, \s, \S соответствуют все юникодные<br>символы с соответствующим качеством. Ускоряет работу, если все соответствия лежат внутри ASCII. |
| re.IGNORECASE | (?i) | Не различать заглавные и маленькие буквы. Работает медленнее, но иногда удобно |
| re.MULTILINE  | (?m) | Специальные символы ^ и $ соответствуют началу и концу каждой строки |
| re.DOTALL     | (?s) | По умолчанию символ \n конца строки не подходит под точку. С этим флагом точка — вообще любой символ |
| re.VERBOSE    | (?x) | Пробелы внутри шаблона игнорируются, за исключением случаев,<br>когда они находятся в классе символов, или когда им предшествует неэкранированная<br>обратная косая черта, или внутри токенов,<br>таких как &#42;?, (?:или (?P&lt;...>. Например, и не допускаются.<br><br><div class="code" style="border-radius:.375rem .375rem;"><div class="highlight"><pre>a = re.compile(<span class="s1">r&#34;&#34;&#34;\d +  # the integral part<br>                   &#92;.    # the decimal point<br>                   \d *  # some fractional digits&#34;&#34;&#34;</span>, re.X)<br>b = re.compile(<span class="s1">r"\d+\.\d*"</span>)</pre></div></div> |

Группы-модификаторы можно объединять в одну группу: (?i-sm).
Такая группа включает режим i и выключает режимы s и m.
Если использование модификаторов требуется только в пределах группы, то нужный шаблон
указывается внутри группы после модификаторов и после двоеточия.
Например, <b>(?-i)(?i:tv)set</b> найдёт <b>TVset</b>, но не <b>TVSET</b>.


# Команды

| Метод                                                                                                                                                                                                                                 | Описание                                                         |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------|
| re.match(    <br>&nbsp;&nbsp;&nbsp;&nbsp;pattern: str,<br>&nbsp;&nbsp;&nbsp;&nbsp;string: str,                      <br>&nbsp;&nbsp;&nbsp;&nbsp;flags: int \| RegexFlag = 0                             <br>) -> Match[str] \| None   | Ищет совпадение в начале строки.                                 |
| re.search(   <br>&nbsp;&nbsp;&nbsp;&nbsp;pattern: str,<br>&nbsp;&nbsp;&nbsp;&nbsp;string: str,                      <br>&nbsp;&nbsp;&nbsp;&nbsp;flags: int \| RegexFlag = 0                             <br>) -> Match[str] \| None   | Ищет первое совпадение в строке.                                 |
| re.findall(  <br>&nbsp;&nbsp;&nbsp;&nbsp;pattern: str,<br>&nbsp;&nbsp;&nbsp;&nbsp;string: str,                      <br>&nbsp;&nbsp;&nbsp;&nbsp;flags: int \| RegexFlag = 0                             <br>) -> list                 | Возвращает список всех непересекающихся совпадений в строке.     |
| re.finditer( <br>&nbsp;&nbsp;&nbsp;&nbsp;pattern: str,<br>&nbsp;&nbsp;&nbsp;&nbsp;string: str,                      <br>&nbsp;&nbsp;&nbsp;&nbsp;flags: int \| RegexFlag = 0                             <br>) -> Iterator[Match[str]] | Возвращает итератор по всем совпадениям в строке.                |
| re.sub(      <br>&nbsp;&nbsp;&nbsp;&nbsp;pattern: str,<br>&nbsp;&nbsp;&nbsp;&nbsp;repl: str \| (Match[str]) -> str, <br>&nbsp;&nbsp;&nbsp;&nbsp;string: str, count: int = 0, flags: int \| RegexFlag = 0<br>) -> str                  | Заменяет совпадения в строке на указанный текст.                 |
| re.subn(     <br>&nbsp;&nbsp;&nbsp;&nbsp;pattern: str,<br>&nbsp;&nbsp;&nbsp;&nbsp;repl: str \| (Match[str]) -> str, <br>&nbsp;&nbsp;&nbsp;&nbsp;string: str, count: int = 0, flags: int \| RegexFlag = 0<br>) -> tuple[str, int]      | То же, что и `re.sub()`, но также возвращает количество замен.   |
| re.split(    <br>&nbsp;&nbsp;&nbsp;&nbsp;pattern: str,<br>&nbsp;&nbsp;&nbsp;&nbsp;string: str,                      <br>&nbsp;&nbsp;&nbsp;&nbsp;maxsplit: int = 0, flags: int \| RegexFlag = 0          <br>) -> list[str]            | Разбивает строку по шаблону и возвращает список строк.           |
| re.fullmatch(<br>&nbsp;&nbsp;&nbsp;&nbsp;pattern: str,<br>&nbsp;&nbsp;&nbsp;&nbsp;string: str,                      <br>&nbsp;&nbsp;&nbsp;&nbsp;flags: int \| RegexFlag = 0                             <br>) -> Match[str] \| None   | Проверяет, полностью ли строка соответствует шаблону.            |
| re.compile(  <br>&nbsp;&nbsp;&nbsp;&nbsp;pattern: str,<br>&nbsp;&nbsp;&nbsp;&nbsp;flags: int \| RegexFlag = 0       <br>                                                                                <br>) -> Pattern[AnyStr]      | Компилирует регулярное выражение в объект регулярного выражения. |

| Метод                                                                                                                                                                                                     | Описание                                                       |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------|
| re.compile(...).match(    <br>&nbsp;&nbsp;&nbsp;&nbsp;string: str,                      <br>&nbsp;&nbsp;&nbsp;&nbsp;flags: int \| RegexFlag = 0                             <br>) -> Match[str] \| None   | Ищет совпадение в начале строки.                               |
| re.compile(...).search(   <br>&nbsp;&nbsp;&nbsp;&nbsp;string: str,                      <br>&nbsp;&nbsp;&nbsp;&nbsp;flags: int \| RegexFlag = 0                             <br>) -> Match[str] \| None   | Ищет первое совпадение в строке.                               |
| re.compile(...).findall(  <br>&nbsp;&nbsp;&nbsp;&nbsp;string: str,                      <br>&nbsp;&nbsp;&nbsp;&nbsp;flags: int \| RegexFlag = 0                             <br>) -> list                 | Возвращает список всех непересекающихся совпадений в строке.   |
| re.compile(...).finditer( <br>&nbsp;&nbsp;&nbsp;&nbsp;string: str,                      <br>&nbsp;&nbsp;&nbsp;&nbsp;flags: int \| RegexFlag = 0                             <br>) -> Iterator[Match[str]] | Возвращает итератор по всем совпадениям в строке.              |
| re.compile(...).sub(      <br>&nbsp;&nbsp;&nbsp;&nbsp;repl: str \| (Match[str]) -> str, <br>&nbsp;&nbsp;&nbsp;&nbsp;string: str, count: int = 0, flags: int \| RegexFlag = 0<br>) -> str                  | Заменяет совпадения в строке на указанный текст.               |
| re.compile(...).subn(     <br>&nbsp;&nbsp;&nbsp;&nbsp;repl: str \| (Match[str]) -> str, <br>&nbsp;&nbsp;&nbsp;&nbsp;string: str, count: int = 0, flags: int \| RegexFlag = 0<br>) -> tuple[str, int]      | То же, что и `re.compile(...).sub()`, но также возвращает количество замен. |
| re.compile(...).split(    <br>&nbsp;&nbsp;&nbsp;&nbsp;string: str,                      <br>&nbsp;&nbsp;&nbsp;&nbsp;maxsplit: int = 0, flags: int \| RegexFlag = 0          <br>) -> list[str]            | Разбивает строку по шаблону и возвращает список строк.         |
| re.compile(...).fullmatch(<br>&nbsp;&nbsp;&nbsp;&nbsp;string: str,                      <br>&nbsp;&nbsp;&nbsp;&nbsp;flags: int \| RegexFlag = 0                             <br>) -> Match[str] \| None   | Проверяет, полностью ли строка соответствует шаблону.          |


<br>

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

**Бэктрекинг (backtracking)** — это процесс возврата назад по строке для поиска альтернативных путей совпадения,
если текущий путь не приводит к успешному совпадению.
Регулярные выражения могут исследовать разные комбинации символов и паттернов, чтобы найти подходящее совпадение.

## Пример бэктрекинга

Рассмотрим регулярное выражение `a(b|c)*d` и строку `abbbd`:

1. Начало сопоставления с `a` — успех.
2. Далее идет `(b|c)*`, которое может захватить любое количество `b` или `c`. Сначала регулярное выражение захватывает все `b`: `abbb`.
3. Теперь шаблон пытается сопоставить `d` после `abbb`. Строка заканчивается на `d`, и совпадение успешно завершается.

Теперь возьмем строку `abbcd`:

1. Начало сопоставления с `a` — успех.
2. Далее идет `(b|c)*`, которое снова захватывает все `b`: `abb`.
3. Теперь шаблон пытается сопоставить `d` после `abb`. Это неудача, потому что следующий символ `c`.
4. Регулярное выражение возвращается (бэктрекинг) к последнему совпавшему `b`, теперь пробует совпадение с `c`: `abbc`.
5. Теперь шаблон пытается сопоставить `d` после `abbc`. Строка заканчивается на `d`, и совпадение успешно завершается.

### Пример атомарной группы

Возьмем выражение `(?>a|ab)c` и строку `abc`:

1. Сначала регулярное выражение пытается сопоставить `a` внутри атомарной группы `(?>a|ab)`.
2. После успешного совпадения с `a`, атомарная группа блокируется, и больше не возвращается назад, даже если дальнейшие совпадения не удаются.
3. Затем выражение пытается сопоставить `c`, что не удается, потому что следующий символ `b`.
4. В обычной группе регулярное выражение вернулось бы назад, чтобы попробовать сопоставить `ab` вместо `a`. Но так как группа атомарная, бэктрекинг не происходит, и регулярное выражение не находит совпадения.

### Пример кода

```pycon
>>> import re
>>> simple_group = re.compile(r"(a|ab)c")
>>> atomic_group = re.compile(r"(?>a|ab)c")
>>> print(simple_group.search("abc").group())  # Обычная группа
abc
>>> print(atomic_group.search("abc"))  # Атомарная группа
None

```

""",
            "images": r"""
<img alt="regexp.png" src="Языки\RegExp\regexp.png">
<img alt="to template.png" src="Языки\RegExp\to template.png">
<img alt="lookaround.png" src="Языки\RegExp\lookaround.png">
""",
        },
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

<img alt="docker.png" src="Языки\Dockerfile\docker.png">
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
            "css-text": {
                "Backgrounds": """
# Backgrounds

```css
background
background-image
background-position
background-size
background-repeat
background-attachment
background-origin
background-clip
background-color
background-image

url | Gradients | none

background-position
 top left   |   top center  |   top right
center left | center center | center right
bottom left | bottom center | bottom right

x-% y-%
X-pos y-pos

background-size
length
%
auto | cover | contain

background-repeat
repeat | repeat-x | repeat-y | no-repeat

background-attachment
scroll | fixed | local

background-origin
border-box | padding-box | content-box

background-clip
border-box | padding-box | content-box | no-clip

background-color
color
transparent
```
""",
                "Border": """
# Border

```css
border
border-width
border-style
border-color

border-width
thin | medium | thick | length

border-style
none | hidden | dotted
dashed | solid | double
groove | ridge | inset | outset

border-color
color

border-left
border-left-width
border-style
border-color
border-left-style
border-style
border-left-color
border-color

border-left-width
thin | medium | thick length

border-right
border-right-width
border-style
border-color

border-right-style
border-style
border-right-color
border-color

border-right-width
thin | medium | thick | length

border-top
border-top-width
border-style
border-color
border-top-style
border-style







border-top-color
border-color

border-top-width
thin | medium | thick | length

border-bottom
border-bottom-width
border-style
border-color

border-bottom-color
border-color

border-bottom-style
border-style

border-break
border-width
border-style
color
close

box-shadow
inset | | [ length, length, length, length | | <color> ]
none

border-collapse
collapse | separate

border-image
image
[ number / % border-width stretch | repeat | round ] none

border-radius
border-radius
border-top-right-radius
border-bottom-right-radius
border-bottom-left-radius
border-top-left-radius
border-top-right-radius
length
border-bottom-left-radius
length
border-bottom-right-radius
length
```
""",
                "table": """
# Table

```css
border-collapse
collapse | separate

empty-cells
show | hide

border-spacing
length length

table-layout
auto | fixed

caption-side
top | bottom | left | right
```
""",
                "boxmodel": """
# Box Model

```css
float
left | right | none

height
auto
length
%

max-height
none
length
%

max-width
none
length
%

min-height
none
length
%

width
auto
%
length

margin-top
margin-right
margin-bottom
margin-left

margin-bottom
auto
length
%

margin-left
auto
height
%

margin-right
auto
height
%

margin-top
auto
length
max-width





padding
padding-top
padding-right
padding-bottom
padding-left

podding-bottom
length
%

padding-left
length
%

padding-right
length
%

padding-top
length
%

display
none | inline | block | inline-block
list-item | run-in | compact | table
inline-table | table-row-group | table-header-group
table-footer-group | table-row | table-column-group
table-column | table-cell | table-caption | ruby
ruby-base | ruby-text | ruby-base-group | ruby-text-group
inline-flex | inline-grid | contents

overflow
visible | hidden | scroll
auto | no-display | no-content
overflow-x
overflow-y

overflow-style
auto | marquee-line | marqueeblock

overflow-x
visible | hidden | scroll
auto | no-display | no-content

rotation
angle

rotation-point
position (paired value off-set)

visibility
visible | hidden | collapse
clear
left | right | both | none
```
""",
                "font": """
# Font

```css
font
font-style
font-variant
font-weight
font-size/line-height
font-family
caption | icon | menu | messagebox
small-caption | status-bar

font-size-adjust
none | inherit
number

font-family
serif | sans-serif | monospace
cursive | fantasy } system-vi | emoji
math | fangsong
inherit | initial | unset

font-style
normal | italic | oblique
inherit

font-variant
normal | small-caps | inherit

font-size
xx-small | x-small | small
medium | large | x-large | xxlarge
smalller | larger

inherit
length
%

font-weight
normal | bold | bolder | lighter
100 | 200 | 300 | 400 | 500
600 | 700 | 800 | 900 | inherit
```
""",
                "text": """
# Text

```css
direction
ltr | rtl | inherit

hanging-punctuation
none | [ start | end | endedge ]

letter-spacing
normal
length
%

text-outline
none
color
length

unicode-bidi
normal | embed | bidi-override

white-space
normal | pre | nowrap | pre-wrap | pre-line

white-space-collapse
preserve | collapse | preserve-breaks | discard

punctuation-trim
none | [start | end | adjacent ]

text-align
start | end | left | right | center | justify

text-align-last
start | end | left | right | center | justify

text-decoration
none | underline | overline | line-through | blink

text-shadow
none
color
length

word-break
normal | keep-all | loose | break-strict | break-all

word-wrap
normal
nowrap

text-emphasis
none | [ [ accent | dot | circle | disc | [ before | after ] ? ]

text-indent
length
%

text-justify
auto | inter-word | interideograph
inter-cluster | distribute | kashida | tibetan

text-transform
none | capitalize | uppercase | lowercase

text-wrap
normal | unrestricted | none | suppress

word-spacing
normal
length
%
```
""",
                "color_angles_time_frequency": """
# Color

```css
color
inherit
color

opacity
inherit
number
```

# Angles

```css
deg - degrees
grad - grads
rad - radians
turn - turns
```

# Time

```css
ms - milli-seconds
s - seconds
```

# Frequency

```css
Hz - heriz
kHz - kilo-hertz
```
""",
                "animations": """
# Animations

```css
animations
animation-name
animation duration
animation-timing-function
animation-delay
animation-iteration-count
animation-direction

animation-name
none | IDENT
animation-duration
time

animation-timing-function
ease | linear | ease-in | ease-out
ease-in-out | cubic-Bezier
(number, number, number, number)

animation-delay
Time

animation-iteration-count
inherit
number

animation-direction
normal | alternate

animation-play-state
running | paused
```
""",
                "speech": """
# Speech

```css
cue
cue-before
cue-after

cue before
url [ silent | x-soft | soft | medium
loud | x-loud | none | inherit ]
number
%

cue-after
url [ silent | x-soft | soft | medium
loud | x-loud | none | inherit ]
number
%

mark
mark-before
mark after

mark-before
string

mark-alter
string

voice-pitch-range
x-low | low | medium | high
xhigh | inherit
number

voice-stress
strong | moderate | none
reduced | inherit

voice-volume
silent | x soft | sofi | medium
loud | x-loud | inherit
number
%

pause
pause-before
pause-after

pause-before
none | x-weak | weak | medium
strong | x-strong | inherit
time

pause after
none | x-weak | weak | medium
strong | x-strong | inherit
time

phonemes
string

voice-duration
time

voice-family
inherit | [ <specific-voice, age,
generic-voice, number> ]

voice-rate
x-slow | slow | medium | fast
x-fast | inherit

voice-pitch
x-low | low | medium | high
x-high | inherit
number
%

caption-side
top | bottom | left | right

rest
rest-before
rest-alter

rest-before
none | x-weak | weak | medium
strong
| x-strong | inherit
time

rest after
none | x-weak | weak | medium
x-strong | inherit

speak
none | normal | spell-out | digits | literal-punctuation | no-punctuation | inherit-number
```
""",
                "transitions": """
# Transitions

```css
transitions
transition-property
transitions-duration
transitions-timing-function
transitions-delay

transitions-delay
time

transitions-duration
time

transitions-property
none | all

transition-timing-function
ease | linear | ease-in | ease-out
ease-in-out | cubic-Bezier
(number, number, number, number)
```
""",
                "ui": """""",
                "column": """""",
                "list and markers": """""",
                "absolute measurement": """""",
                "pseudo element": """""",
                "pseudo class": """""",
                "colors": """""",
                "outlin": """""",
                "relative measurement": """""",
            },
            "css-img": r"""

<img alt="                  background.png" src="Языки\CSS\images\background.png">
<img alt="                      border.png" src="Языки\CSS\images\border.png">
<img alt="                       table.png" src="Языки\CSS\images\table.png">
<img alt="                    boxmodel.png" src="Языки\CSS\images\boxmodel.png">
<img alt="                        font.png" src="Языки\CSS\images\font.png">
<img alt="                        text.png" src="Языки\CSS\images\text.png">
<img alt=" color_angles_time_frequency.png" src="Языки\CSS\images\color_angles_time_frequency.png">
<img alt="                  animations.png" src="Языки\CSS\images\animations.png">
<img alt="                      speech.png" src="Языки\CSS\images\speech.png">
<img alt="                 transitions.png" src="Языки\CSS\images\transitions.png">
<img alt="                          ui.png" src="Языки\CSS\images\ui.png">
<img alt="                      column.png" src="Языки\CSS\images\column.png">
<img alt="            list and markers.png" src="Языки\CSS\images\list and markers.png">
<img alt="        absolute measurement.png" src="Языки\CSS\images\absolute measurement.png">
<img alt="              pseudo element.png" src="Языки\CSS\images\pseudo element.png">
<img alt="                pseudo class.png" src="Языки\CSS\images\pseudo class.png">
<img alt="                      colors.png" src="Языки\CSS\images\colors.png">
<img alt="                     outline.png" src="Языки\CSS\images\outline.png">
<img alt="        relative measurement.png" src="Языки\CSS\images\relative measurement.png">

<img alt="              selector types.png" src="Языки\CSS\images\selector types.png">
<img alt="             2d 3d transform.png" src="Языки\CSS\images\2d 3d transform.png">
<img alt="           generated content.png" src="Языки\CSS\images\generated content.png">
<img alt="                   hyperlink.png" src="Языки\CSS\images\hyperlink.png">
<img alt="                 positioning.png" src="Языки\CSS\images\positioning.png">
<img alt="                    line box.png" src="Языки\CSS\images\line box.png">
<img alt="                 paged media.png" src="Языки\CSS\images\paged media.png">
""",
            "Селекторы": r"""
<img alt="selectors.png" src="Языки/CSS/css_selectors.png">
""",
            "Единицы измерения": """
<img alt="css_units.png" src="Языки/CSS/css_units.png">
""",
        },
        "HTML": {
            "Теги": r"""
<img alt="tags1.png" src="Языки\HTML\tags1.png">
<img alt="tags2.png" src="Языки\HTML\tags2.png">
""",
            "Символы и экранирование": r"""
<img alt="html_character1.png" src="Языки\HTML\html_character1.png">
<img alt="html_character1.png" src="Языки\HTML\html_character1.png">
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

""",
            "Xpath": {
                "Link": """
Шпаргалка взята с сайта https://devhints.io/xpath
""",
                "Selectors": """
# Descendant selectors

|              |           |    |
|--------------|-----------|----|
| h1           | //h1      | ?  |
| div p        | //div//p  | ?  |
| ul > li      | //ul/li   | ?  |
| ul > li > a  | //ul/li/a |    |
| div > *      | //div/*   |    |
| :root        | /         | ?  |
| :root > body | /body     |    |

# Attribute selectors

|                      |                                    |    |
|----------------------|------------------------------------|----|
| #id                  | //*[@id="id"]                      | ?  |
| .class               | //*[@class="class"] …kinda         |    |
| input[type="submit"] | //input[@type="submit"]            |    |
| a#abc[for="xyz"]     | //a[@id="abc"][@for="xyz"]         | ?  |
| a[rel]               | //a[@rel]                          |    |
| a[href^='/']         | //a[starts-with(@href, '/')]       | ?  |
| a[href$='pdf']       | //a[ends-with(@href, '.pdf')]      |    |
| a[href*='://']       | //a[contains(@href, '://')]        |    |
| a[rel~='help']       | //a[contains(@rel, 'help')] …kinda |    |

# Order selectors

|                        |                         |    |
|------------------------|-------------------------|----|
| ul > li:first-of-type  | //ul/li[1]              | ?  |
| ul > li:nth-of-type(2) | //ul/li[2]              |    |
| ul > li:last-of-type   | //ul/li[last()]         |    |
| li#id:first-of-type    | //li[1][@id="id"]       | ?  |
| a:first-child          | //*[1][name()="a"]      |    |
| a:last-child           | //*[last()][name()="a"] |    |

# Siblings

|          |                                    |    |
|----------|------------------------------------|----|
| h1 ~ ul  | //h1/following-sibling::ul         | ?  |
| h1 + ul  | //h1/following-sibling::ul[1]      |    |
| h1 ~ #id | //h1/following-sibling::[@id="id"] |    |


# jQuery

|                            |                                |    |
|----------------------------|--------------------------------|----|
| $('ul > li').parent()      | //ul/li/..                     | ?  |
| $('li').closest('section') | //li/ancestor-or-self::section |    |
| $('a').attr('href')        | //a/@href                      | ?  |
| $('span').text()           | //span/text()                  |    |

# Other things

|                         |                                 |    |
|-------------------------|---------------------------------|----|
| h1:not([id])            | //h1[not(@id)]                  | ?  |
| Text match              | //button[text()="Submit"]       | ?  |
| Text match (substring)  | //button[contains(text(),"Go")] |    |
| Arithmetic              | //product[@price > 2.50]        |    |
| Has children            | //ul[*]                         |    |
| Has children (specific) | //ul[li]                        |    |
| Or logic                | //a[@name or @href]             | ?  |
| Union (joins results)   | //a | //div                     | ?  |

# Class check

|                                                                     |
|---------------------------------------------------------------------|
| //div[contains(concat(' ',normalize-space(@class),' '),' foobar ')] |

Xpath doesn’t have the “check if part of space-separated list” operator, so this is the workaround (source).
""",
                "Expressions": """
# Steps and axes

|         |      |      |               |
|---------|------|------|---------------|
| //      | ul   | /    | a[@id='link'] |
| Axis    | Step | Axis | Step          |


# Prefixes

| Prefix | Example             | What     |
|--------|---------------------|----------|
| //     | //hr[@class='edge'] | Anywhere |
| ./     | ./a                 | Relative |
| /      | /html/body/div      | Root     |

Begin your expression with any of these.



# Axes

| Axis | Example           | What       |
|------|-------------------|------------|
| /    | //ul/li/a         | Child      |
| //   | //[@id="list"]//a | Descendant |

Separate your steps with /. Use two (//) if you don’t want to select direct children.


# Steps

```bash
//div
//div[@name='box']
//[@id='link']
```

A step may have an element name (div) and predicates ([...]). Both are optional. They can also be these other things:

```bash
//a/text()     #=> "Go home"
//a/@href      #=> "index.html"
//a/*          #=> All a's child elements
```
""",
                "Predicates": """
# Predicates

```bash
//div[true()]
//div[@class="head"]
//div[@class="head"][@id="top"]
```

Restricts a nodeset only if some condition is true. They can be chained.

# Operators

```bash
# Comparison
//a[@id = "xyz"]
//a[@id != "xyz"]
//a[@price > 25]
```

```bash
# Logic (and/or)
//div[@id="head" and position()=2]
//div[(x and y) or not(z)]
```

Use comparison and logic operators to make conditionals.

# Using nodes

```bash
# Use them inside functions
//ul[count(li) > 2]
//ul[count(li[@class='hide']) > 0]
```

```bash
# This returns `<ul>` that has a `<li>` child
//ul[li]
```

You can use nodes inside predicates.

# Indexing

```bash
//a[1]                  # first <a>
//a[last()]             # last <a>
//ol/li[2]              # second <li>
//ol/li[position()=2]   # same as above
//ol/li[position()>1]   # :not(:first-of-type)
```

Use [] with a number, or last() or position().

# Chaining order

```bash
a[1][@href='/']
a[@href='/'][1]
```

Order is significant, these two are different.

# Nesting predicates

```bash
//section[.//h1[@id='hi']]
```
This returns &lt;section> if it has an &lt;h1> descendant with id='hi'.
""",
                "Functions": """
# Node functions

```bash
name()                     # //[starts-with(name(), 'h')]
text()                     # //button[text()="Submit"]
                           # //button/text()
lang(str)
namespace-uri()
```

```bash
count()                    # //table[count(tr)=1]
position()                 # //ol/li[position()=2]
```

# Boolean functions

```bash
not(expr)                  # button[not(starts-with(text(),"Submit"))]
```

# String functions

```bash
contains()                 # font[contains(@class,"head")]
starts-with()              # font[starts-with(@class,"head")]
ends-with()                # font[ends-with(@class,"head")]
```

```bash
concat(x,y)
substring(str, start, len)
substring-before("01/02", "/")  #=> 01
substring-after("01/02", "/")   #=> 02
translate()
normalize-space()
string-length()
```

# Type conversion

```bash
string()
number()
boolean()
```
""",
                "Axes": """
# Using axes

```bash
//ul/li                       # ul > li
//ul/child::li                # ul > li (same)
//ul/following-sibling::li    # ul ~ li
//ul/descendant-or-self::li   # ul li
//ul/ancestor-or-self::li     # $('ul').closest('li')
```

Steps of an expression are separated by /, usually used to pick child nodes.
That’s not always true: you can specify a different “axis” with ::.

|      |      |          |      |
|------|------|----------|------|
| //   | ul   | /child:: | li   |
| Axis | Step | Axis     | Step |

# Child axis

```bash
# both the same
//ul/li/a
//child::ul/child::li/child::a
```

child:: is the default axis. This makes //a/b/c work.

```bash
# both the same
# this works because `child::li` is truthy, so the predicate succeeds
//ul[li]
//ul[child::li]
```

```bash
# both the same
//ul[count(li) > 2]
//ul[count(child::li) > 2]
```



# Descendant-or-self axis

```bash
# both the same
//div//h4
//div/descendant-or-self::h4
```

// is short for the descendant-or-self:: axis.

```bash
# both the same
//ul//[last()]
//ul/descendant-or-self::[last()]
```

# Other axes

| Axis               | Abbrev  | Notes                                        |
|--------------------|---------|----------------------------------------------|
| ancestor           |         |                                              |
| ancestor-or-self   |         |                                              |
| attribute          | @       |  @href is short for attribute::href          |
| child              |         |  div is short for child::div                 |
| descendant         |         |                                              |
| descendant-or-self | //      | // is short for /descendant-or-self::node()/ |
| namespace          |         |                                              |
| self               | .       |  . is short for self::node()                 |
| parent             | ..      | .. is short for parent::node()               |
| following          |         |                                              |
| following-sibling  |         |                                              |
| preceding          |         |                                              |
| preceding-sibling  |         |                                              |
| There are other axes you can use.

# Unions

//a | //span
Use | to join two expressions.
""",
                "More examples": """
# Examples

```bash
//*                 # all elements
count(//*)          # count all elements
(//h1)[1]/text()    # text of the first h1 heading
//li[span]          # find a <li> with an <span> inside it
                    # ...expands to //li[child::span]
//ul/li/..          # use .. to select a parent
```


# Find a parent

```bash
//section[h1[@id='section-name']]
```

Finds a &lt;section> that directly contains h1#section-name

```bash
//section[//h1[@id='section-name']]
```

Finds a &lt;section> that contains h1#section-name.
(Same as above, but uses descendant-or-self instead of child)

# Closest

```bash
./ancestor-or-self::[@class="box"]
```

Works like jQuery’s $().closest('.box').

# Attributes

```bash
//item[@price > 2*@discount]
```

Finds &lt;item> and check its attributes
""",
            },
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

Чтобы работать с указателями необходимо воспользоваться двумя специальными символами: & и *.

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
""",
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
Если файл не существует, то он будет создан и в него будет записано значение переменной.""",
        },
        "LaTex": {
            "Элементы": r"""

## Пробелы
```LaTex
\quad - Большой пробел
\! - Сдвинуть назад
"\ " - Маленький пробел
```

## Матрица
```LaTex
\begin{bmatrix}
{}&{}\\
{}&{}
\end{bmatrix}
```

## Система уравнений
```LaTex
\begin{cases}
{}\\
{}
\end{cases}
```

## Дробь
```LaTex
\frac{}{}
```

## Форматирование текста
```LaTex
\underline{} - нижнее подчёркивание
\textbf{} - жирный текст
```

## Символы
```LaTex
\Delta - Треугольничек
\dots - ...
\сdot - Точка умножений
\lambda - Лямбда
\ne - !=
\approx - ≈

\left? - Левая скобка
\right? - Правая скобка
```
"""
        },
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

```text
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
            "TinyDB": """
Шпаргалка по TinyDB в Python:

```bash
pip install tinydb
```

```python
from tinydb import TinyDB, Query


db = TinyDB("db.json")
users_table = db.table("users")
user_id = users_table.insert({"name": "John", "age": 25})
all_users = users_table.all()

# Получение записи по условию (например, по имени)
user_query = Query()
john_data = users_table.search(user_query.name == "John")

# Изменение данных в записи по условию (например, по имени)
users_table.update({'age': 26}, user_query.name == 'John')

# Удаление записи по условию (например, по имени)
users_table.remove(user_query.name == 'John')
```
""",
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
            "Определитель матрицы": """
```python
#file matrix.py
class Matrix:
    def __init__(self, matrix: list[list[int]]):
        self.matrix = matrix

    def get_minor(self, i: int, j: int) -> list[list[int]]:
        result = [
            list(row[:j] + row[j+1:])
            for row_index, row in enumerate(self.matrix) if row_index != i
        ]
        return result

    def det(self):
        n = len(self.matrix)
        if len({len(row) for row in self.matrix}) > 1 and n != x[0]:
            raise ValueError("")

        if n == 1:
            return self.matrix[0][0]

        elif n == 2:
            return (
                self.matrix[0][0] * self.matrix[1][1]
            ) - (
                self.matrix[0][1] * self.matrix[1][0]
            )
        elif n == 3:
            return (
                self.matrix[0][0] * self.matrix[1][1] * self.matrix[2][2]
            ) + (
                self.matrix[0][1] * self.matrix[1][2] * self.matrix[2][0]
            ) + (
                self.matrix[0][2] * self.matrix[1][0] * self.matrix[2][1]
            ) - (
                self.matrix[0][2] * self.matrix[1][1] * self.matrix[2][0]
            ) - (
                self.matrix[0][0] * self.matrix[1][2] * self.matrix[2][1]
            ) - (
                self.matrix[0][1] * self.matrix[1][0] * self.matrix[2][2]
            )

        else:
            result = []
            i = 0
            for j, x in enumerate(self.matrix[0]):
                minor = self.get_minor(i, j)
                result.append(x * ((-1)**(i+1 + j+1)) * Matrix(minor).det())
            return sum(result)
```

```python
#file test_matrix_1.py
from matrix import Matrix

m = [
    [1, 5, 7, 4, 9],
    [4, 7, 8, 3, 4],
    [9, 3, 5, 2, 8],
    [9, 3, 6, 3, 1],
    [5, 9, 1, 4, 2]
]

print(Matrix(m).det())
```

```python
#file test_matrix_2.py
from numpy import linalg
m = [
    [1, 5, 7, 4, 9],
    [4, 7, 8, 3, 4],
    [9, 3, 5, 2, 8],
    [9, 3, 6, 3, 1],
    [5, 9, 1, 4, 2]
]
print(linalg.det(m))
```
""",
            "Минимальное максимальное число матрицы cpp": r"""
```cpp
#file maxminmatrix.cpp
#include <iostream>
#include <vector>
#include <time.h>
#include <iomanip>

using namespace std;

int main()
{
    int rows = 3;
    int cols = 4;
    srand(time(NULL));
    vector<vector<int>> matrix(rows, vector<int>(cols, 0));
    for (int i = 0; i < rows; ++i) {
        cout << "|";
        for (int j = 0; j < cols; ++j) {
            int number = 1 + rand() % 999;
            matrix[i][j] = number;
            cout << " " << setw(3) << setfill(' ') << number << " |";
        }
        cout << "\n";
    }
    int max = 0;
    int min = 999;
    for (auto r : matrix) {
        for (auto c : r) {
            if (c > max) max = c;
            if (c < min) min = c;
        }
    }
    cout << "max = " << max << "\n" << "min = " << min << "\n";
    return 0;
}
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

```html
button onclick="showText( {NAME} )" class="trigger"> {NAME} </button>
<div id=" {NAME} " style="display:none;" class="button-field">
    <button onclick="PutText( {NAME-1} )" class="trigger"> {NAME-1} </button>
    <pre id=" {NAME-1} " style="display:none;" class="code-str-1">
{TEXT}
</pre>
```
""",
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
""",
    "Университет": {
        "Высшая математика": {
            "Матрицы": {
                "Матрицы": """""",
                "Определители": """
n = 1
A = [
    [a]
]
det(A) = a


n = 2
A = [
    [a, b],
    [c, d]
]
det(A) = a&#42;d - b&#42;c


n = 3
A = [
    [a11, a12, a13],
    [a21, a22, a23],
    [a31, a32, a33]
]
det(A) = a11&#42;a22&#42;a33 + a12&#42;a23&#42;a31 + a13&#42;a21&#42;a32 - a13&#42;a22&#42;a31 - a12&#42;a21&#42;a33 - a11&#42;a32&#42;a23

Минор это под табличка от основной матрицы.

""",
            },
        },
    },
}

# if __name__ == "__main__":
#     import os
#     os.system('python "builder.py"')
