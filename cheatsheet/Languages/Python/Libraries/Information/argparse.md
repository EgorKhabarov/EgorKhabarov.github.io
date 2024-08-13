<p>Библиотека argparse в Python позволяет легко создавать интерфейсы командной строки для ваших скриптов. 
Эта библиотека предоставляет механизмы для определения аргументов командной строки и автоматического 
генерирования справочной информации и сообщений об ошибках.</p>
<p>Вот несколько примеров использования библиотеки argparse в Python:
Простой скрипт</p>
<pre><code class="language-python">import argparse

parser = argparse.ArgumentParser()
parser.add_argument(&quot;echo&quot;, help=&quot;echo the string you use here&quot;)

args = parser.parse_args()
print(args.echo)
</code></pre>
<p>Для запуска скрипта нужно использовать команду</p>
<pre><code class="language-bash">python script.py hello
</code></pre>
<p>Аргументы с флагами</p>
<pre><code class="language-python">import argparse

parser = argparse.ArgumentParser()
parser.add_argument(&quot;--verbosity&quot;, help=&quot;increase output verbosity&quot;, action=&quot;store_true&quot;)

args = parser.parse_args()
if args.verbosity:
    print(&quot;verbosity turned on&quot;)
</code></pre>
<p>Для запуска скрипта нужно использовать команду</p>
<pre><code class="language-bash">python script.py --verbosity
</code></pre>
<p>Опциональный аргумент</p>
<pre><code class="language-python">import argparse

parser = argparse.ArgumentParser()
parser.add_argument(&quot;--number&quot;, help=&quot;enter a number&quot;, type=int)

args = parser.parse_args()
if args.number:
    print(args.number * 2)
</code></pre>
<p>Для запуска скрипта нужно использовать команду</p>
<pre><code class="language-bash">python script.py --number 5
</code></pre>
<p>Обязательный аргумент</p>
<pre><code class="language-python">import argparse

parser = argparse.ArgumentParser()
parser.add_argument(&quot;filename&quot;, help=&quot;the name of the file to read&quot;)

args = parser.parse_args()
print(args.filename)
</code></pre>
<p>Для запуска скрипта нужно использовать команду</p>
<pre><code class="language-bash">python script.py filename.txt
</code></pre>
<p>Группировка аргументов</p>
<pre><code class="language-python">import argparse

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
group.add_argument(&quot;--verbose&quot;, help=&quot;increase output verbosity&quot;, action=&quot;store_true&quot;)
group.add_argument(&quot;--quiet&quot;, help=&quot;decrease output verbosity&quot;, action=&quot;store_true&quot;)

args = parser.parse_args()
if args.verbose:
    print(&quot;verbosity turned on&quot;)
elif args.quiet:
    print(&quot;verbosity turned off&quot;)
</code></pre>
<p>Для запуска скрипта нужно использовать команду</p>
<pre><code class="language-bash">python script.py --verbose или python script.py --quiet
</code></pre>
<p>Позиционные аргументы с выбором</p>
<pre><code class="language-python">import argparse

parser = argparse.ArgumentParser()
parser.add_argument(&quot;operation&quot;, help=&quot;operation to perform&quot;, choices=[&quot;add&quot;, &quot;sub&quot;, &quot;mul&quot;, &quot;div&quot;])
parser.add_argument(&quot;num1&quot;, help=&quot;first number&quot;, type=int)
parser.add_argument(&quot;num2&quot;, help=&quot;second number&quot;, type=int)

args = parser.parse_args()
if args.operation == &quot;add&quot;:
    print(args.num1 + args.num2)
elif args.operation == &quot;sub&quot;:
    print(args.num1 - args.num2)
elif args.operation == &quot;mul&quot;:
    print(args.num1 * args.num2)
else:
    print(args.num1 / args.num2)
</code></pre>
<p>Для запуска скрипта нужно использовать команду</p>
<pre><code class="language-bash">python script.py add 5 3
</code></pre>
<p>Описание программы и аргументов</p>
<pre><code class="language-python">import argparse

parser = argparse.ArgumentParser(description=&quot;A simple calculator program&quot;)
parser.add_argument(&quot;operation&quot;, help=&quot;operation to perform&quot;, choices=[&quot;add&quot;, &quot;sub&quot;, &quot;mul&quot;, &quot;div&quot;])
parser.add_argument(&quot;num1&quot;, help=&quot;first number&quot;, type=int)
parser.add_argument(&quot;num2&quot;, help=&quot;second number&quot;, type=int)

args = parser.parse_args()
if args.operation == &quot;add&quot;:
    print(args.num1 + args.num2)
elif args.operation == &quot;sub&quot;:
    print(args.num1 - args.num2)
elif args.operation == &quot;mul&quot;:
    print(args.num1 * args.num2)
else:
    print(args.num1 / args.num2)
</code></pre>
<p>Для запуска скрипта нужно использовать команду: </p>
<pre><code class="language-bash">python script.py --help
</code></pre>
<p>Парсинг аргументов из файла</p>
<pre><code class="language-python">import argparse

parser = argparse.ArgumentParser(fromfile_prefix_chars=&quot;@&quot;)
parser.add_argument(&quot;operation&quot;, help=&quot;operation to perform&quot;, choices=[&quot;add&quot;, &quot;sub&quot;, &quot;mul&quot;, &quot;div&quot;])
parser.add_argument(&quot;num1&quot;, help=&quot;first number&quot;, type=int)
parser.add_argument(&quot;num2&quot;, help=&quot;second number&quot;, type=int)

args = parser.parse_args([&quot;@args.txt&quot;])
if args.operation == &quot;add&quot;:
    print(args.num1 + args.num2)
elif args.operation == &quot;sub&quot;:
    print(args.num1 - args.num2)
elif args.operation == &quot;mul&quot;:
    print(args.num1 * args.num2)
else:
    print(args.num1 / args.num2)
</code></pre>
<p>Для использования данного примера нужно создать файл "args.txt" со следующим содержимым</p>
<pre><code class="language-text">add 5 3
</code></pre>
<p>Затем, чтобы запустить скрипт, нужно использовать команду</p>
<pre><code class="language-bash">python script.py @args.txt
</code></pre>
<p>Аргумент со значением по умолчанию</p>
<pre><code class="language-python">import argparse

parser = argparse.ArgumentParser()
parser.add_argument(&quot;--verbosity&quot;, help=&quot;increase output verbosity&quot;, action=&quot;store_true&quot;)
parser.add_argument(&quot;--num&quot;, help=&quot;a number&quot;, type=int, default=5)

args = parser.parse_args()
if args.verbosity:
    print(&quot;verbosity turned on&quot;)
print(args.num * 2)
</code></pre>
<p>Для запуска скрипта нужно использовать команду</p>
<pre><code class="language-bash">python script.py --verbosity --num 3
</code></pre>
<p>Поддержка субкоманд</p>
<pre><code class="language-python">import argparse

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(title=&quot;subcommands&quot;, dest=&quot;subcommand&quot;)

parser_a = subparsers.add_parser(&quot;command_a&quot;, help=&quot;command a help&quot;)
parser_a.add_argument(&quot;foo&quot;, type=int, help=&quot;foo help&quot;)

parser_b = subparsers.add_parser(&quot;command_b&quot;, help=&quot;command b help&quot;)
parser_b.add_argument(&quot;--bar&quot;, type=str, help=&quot;bar help&quot;)

args = parser.parse_args()
if args.subcommand == &quot;command_a&quot;:
    print(args.foo)
else:
    print(args.bar)
</code></pre>
<p>Для запуска скрипта нужно использовать команду: </p>
<pre><code class="language-bash">python script.py command_a 5
</code></pre>
<p>или</p>
<pre><code class="language-bash">python script.py command_b --bar test
</code></pre>