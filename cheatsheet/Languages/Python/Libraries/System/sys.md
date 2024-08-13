<p>sys.argv содержит список аргументов командной строки, переданных скрипту. 
Первый элемент списка (sys.argv[0]) является именем скрипта:</p>
<pre><code class="language-python">import sys

# Передаем два аргумента при запуске скрипта:
# python myscript.py arg1 arg2
print(sys.argv[0])  # myscript.py
print(sys.argv[1])  # arg1
print(sys.argv[2])  # arg2
</code></pre>
<p>sys.exit() завершает выполнение программы. 
Можно передать код возврата, который будет использован в качестве кода завершения:</p>
<pre><code class="language-python">import sys

# Завершаем программу с кодом 0
sys.exit(0)

# Завершаем программу с кодом ошибки 1
sys.exit(1)
</code></pre>
<p>sys.stdin - стандартный поток ввода
sys.stdout - стандартный поток вывода
sys.stderr - стандартный поток ошибок. 
Эти потоки могут быть перенаправлены в файлы или другие потоки ввода/вывода:</p>
<pre><code class="language-python">import sys

# Читаем данные из стандартного потока ввода
data = sys.stdin.readline()

# Пишем данные в стандартный поток вывода
sys.stdout.write(&quot;Hello, world!\n&quot;)

# Пишем ошибки в стандартный поток ошибок
sys.stderr.write(&quot;Error occurred\n&quot;)
</code></pre>
<p>sys.platform содержит строку, которая идентифицирует операционную систему, на которой запущена программа:</p>
<pre><code class="language-python">import sys

if sys.platform == &quot;win32&quot;:
    print(&quot;Windows&quot;)
elif sys.platform == &quot;linux&quot;:
    print(&quot;Linux&quot;)
elif sys.platform == &quot;darwin&quot;:
    print(&quot;MacOS&quot;)
</code></pre>
<p>sys.getsizeof() возвращает размер объекта в байтах:</p>
<pre><code class="language-python">import sys

a = [1, 2, 3]
print(sys.getsizeof(a))  # 88
</code></pre>
<p>sys.path содержит список путей, в которых Python ищет модули:</p>
<pre><code class="language-python">import sys

print(sys.path)

&quot;&quot;&quot;
[
    &quot;&quot;, 
    &quot;C:\\Users\\User\\AppData\\Local\\Programs\\Python\\Python311\\python311.zip&quot;, 
    &quot;C:\\Users\\User\\AppData\\Local\\Programs\\Python\\Python311\\DLLs&quot;, 
    &quot;C:\\Users\\User\\AppData\\Local\\Programs\\Python\\Python311\\Lib&quot;, 
    &quot;C:\\Users\\User\\AppData\\Local\\Programs\\Python\\Python311&quot;, 
    &quot;C:\\Users\\User\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\site-packages&quot;
]
&quot;&quot;&quot;
</code></pre>
<p>sys.getdefaultencoding() возвращает кодировку по умолчанию, используемую для строк в Python:</p>
<pre><code class="language-python">import sys

print(sys.getdefaultencoding())  # utf-8
</code></pre>
<p>sys.getfilesystemencoding() возвращает кодировку, используемую файловой системой:</p>
<pre><code class="language-python">import sys

print(sys.getfilesystemencoding())  # utf-8
</code></pre>
<p>sys.getwindowsversion() возвращает информацию о версии Windows, если программа запущена в Windows:</p>
<pre><code class="language-python">import sys

if sys.platform == &quot;win32&quot;:
    print(sys.getwindowsversion())

&quot;&quot;&quot;sys.getwindowsversion(major=10, minor=0, build=19044, platform=2, service_pack=&quot;&quot;)&quot;&quot;&quot;
</code></pre>
<p>sys.version содержит строку, которая содержит информацию о версии Python:</p>
<pre><code class="language-python">import sys

print(sys.version)

&quot;&quot;&quot;3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)]&quot;&quot;&quot;
</code></pre>
<p>sys.modules содержит словарь, содержащий все импортированные модули:</p>
<pre><code class="language-python">import sys
import math

print(sys.modules[&quot;math&quot;])  # &lt;module 'math' (built-in)&gt;
</code></pre>
<p>sys.maxsize содержит максимальное значение целого числа, которое может быть использовано в Python:</p>
<pre><code class="language-python">import sys

print(sys.maxsize)  # 9223372036854775807
</code></pre>
<p>sys.float_info содержит информацию о типе float в Python:</p>
<pre><code class="language-python">import sys

print(sys.float_info)

&quot;&quot;&quot;sys.float_info(max=1.7976931348623157e+308, max_exp=1024, max_10_exp=308, min=2.2250738585072014e-308, min_exp=-1021, min_10_exp=-307, dig=15, mant_dig=53, epsilon=2.220446049250313e-16, radix=2, rounds=1)&quot;&quot;&quot;
</code></pre>
<p>sys.stdin.isatty(), sys.stdout.isatty(), sys.stderr.isatty()
sys.stdin.isatty(), sys.stdout.isatty(), и sys.stderr.isatty() возвращают True, 
если соответствующий поток является терминальным устройством (tty):</p>
<pre><code class="language-python">import sys

if sys.stdin.isatty():
    print(&quot;stdin is a tty&quot;)
else:
    print(&quot;stdin is not a tty&quot;)

if sys.stdout.isatty():
    print(&quot;stdout is a tty&quot;)
else:
    print(&quot;stdout is not a tty&quot;)

if sys.stderr.isatty():
    print(&quot;stderr is a tty&quot;)
else:
    print(&quot;stderr is not a tty&quot;)
</code></pre>
<p>sys.getrecursionlimit() возвращает текущий предел рекурсии Python. sys.setrecursionlimit() устанавливает предел рекурсии Python:</p>
<pre><code class="language-python">import sys

print(sys.getrecursionlimit())  # 1000

sys.setrecursionlimit(3000)
</code></pre>
<p>sys.settrace() устанавливает функцию обратного вызова для отслеживания исполнения кода Python:</p>
<pre><code class="language-python">import sys

def trace_calls(frame, event, arg):
    if event == &quot;call&quot;:
        print(frame.f_code.co_name)

    return trace_calls

sys.settrace(trace_calls)

def my_function():
    print(&quot;Hello, world!&quot;)

my_function()

sys.settrace(None)
</code></pre>
<p>sys.exc_info() возвращает кортеж из трех значений, представляющих текущее исключение, если оно присутствует:</p>
<pre><code class="language-python">import sys

def divide(x, y):
    try:
        result = x / y
    except:
        print(sys.exc_info())

divide(1, 0)
</code></pre>