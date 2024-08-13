<p>Модуль contextlib - это стандартная библиотека Python, который содержит утилиты для работы с контекстными менеджерами.
Контекстные менеджеры могут использоваться, например, для управления ресурсами, такими как файлы или сетевые соединения.</p>
<h4>contextlib.contextmanager</h4>
<p>Декоратор превращает генераторную функцию в контекстный менеджер. 
Генератор должен содержать точку входа и выхода из контекста.</p>
<pre><code class="language-python">import contextlib

@contextlib.contextmanager
def my_context():
    print(&quot;Entering context&quot;)
    yield
    print(&quot;Exiting context&quot;)

with my_context():
    print(&quot;Inside context&quot;)
</code></pre>
<p>В этом примере my_context() - это контекстный менеджер, который выводит сообщения при входе и выходе из контекста.</p>
<h4>contextlib.suppress</h4>
<p>это контекстный менеджер, который подавляет указанные исключения. 
Он используется, когда вы хотите, чтобы программа продолжала работать даже при возникновении определенных ошибок. 
Пример использования:</p>
<pre><code class="language-python">import contextlib

with contextlib.suppress(FileNotFoundError):
    with open(&quot;non_existent_file.txt&quot;, &quot;r&quot;) as f:
        print(f.read())
</code></pre>
<p>В этом примере suppress используется для подавления исключения FileNotFoundError, 
которое возникает, если файл non_existent_file.txt не найден. 
Вместо того, чтобы возбудить исключение, программа продолжит работу без выполнения блока кода внутри with выражения.</p>
<h4>contextlib.redirect_stdout и contextlib.redirect_stderr</h4>
<p>эти контекстные менеджеры перенаправляют стандартный вывод и стандартный вывод ошибок соответственно в файл или объект. 
Пример использования:</p>
<pre><code class="language-python">import contextlib
import io

with io.StringIO() as output:
    with contextlib.redirect_stdout(output):
        print(&quot;Hello, world!&quot;)
    contents = output.getvalue()

print(contents)
</code></pre>
<p>В этом примере стандартный вывод перенаправляется в объект io.StringIO(), 
а затем содержимое этого объекта выводится на экран.</p>
<p>Модуль contextlib содержит и другие функции, такие как closing, nullcontext и ExitStack. 
Они все предназначены для упрощения работы с контекстными менеджерами в Python.</p>
<h4>contextlib.closing</h4>
<p>Это функция, которая превращает объект с методом close() в контекстный менеджер. 
Это может быть полезно, например, для работы с файлами или соединениями. 
Пример использования:</p>
<pre><code class="language-python">import contextlib
from urllib.request import urlopen

with contextlib.closing(urlopen(&quot;https:&amp;sol;&amp;sol;www.example.com/&quot;)) as page:
    for line in page:
        print(line.decode(&quot;utf-8&quot;))
</code></pre>
<p>В этом примере urlopen("https:&sol;&sol;www.example.com/") возвращает объект с методом close(), 
который используется внутри контекстного менеджера closing.</p>
<h4>contextlib.nullcontext</h4>
<p>Это класс, который предоставляет пустой контекстный менеджер, который не делает ничего. 
Он может быть использован, когда нужен контекстный менеджер, 
но никакой реальной работы в контексте выполнять не требуется. 
Пример использования:</p>
<pre><code class="language-python">import contextlib

with contextlib.nullcontext():
    print(&quot;Hello, world!&quot;)
</code></pre>
<p>В этом примере ничего не происходит в контексте, но благодаря использованию nullcontext, 
код работает корректно в рамках контекстного менеджера.</p>
<h4>contextlib.ExitStack</h4>
<p>Это класс, который предоставляет возможность управления несколькими контекстными менеджерами одновременно. 
Он может быть использован, когда требуется обеспечить надежное управление ресурсами в случае, 
когда ресурсы могут быть открыты и закрыты в произвольном порядке. 
Пример использования:</p>
<pre><code class="language-python">import contextlib

with contextlib.ExitStack() as stack:
    files = [stack.enter_context(open(f)) for f in [&quot;file1.txt&quot;, &quot;file2.txt&quot;, &quot;file3.txt&quot;]]
    for file in files:
        print(file.readline())
</code></pre>
<p>В этом примере ExitStack используется для управления тремя файлами, которые могут быть открыты и закрыты в любом порядке
Функция stack.enter_context(open(f)) добавляет каждый файл в стек контекстных менеджеров, 
который гарантирует их правильное закрытие в конце работы с ними.</p>