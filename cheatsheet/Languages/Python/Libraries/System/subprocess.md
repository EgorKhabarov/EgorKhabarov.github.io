<p>Библиотека subprocess в Python используется для запуска новых процессов, подключения к существующим процессам, 
выполнения команд в командной строке и многого другого. 
Вот несколько примеров использования этой библиотеки:</p>
<p>Запуск команды в командной строке</p>
<pre><code class="language-python">import subprocess

print(subprocess.run([&quot;ls&quot;, &quot;-l&quot;], capture_output=True, text=True).stdout)
</code></pre>
<p>В этом примере мы использовали метод run для выполнения команды ls -l в командной строке. 
Опция capture_output=True заставляет метод сохранять вывод команды, а опция text=True указывает, что мы ожидаем текстовый вывод.</p>
<p>Запуск команды с переменными окружения</p>
<pre><code class="language-python">import subprocess

env = {&quot;MYVAR&quot;: &quot;myvalue&quot;}
print(subprocess.run([&quot;env&quot;], env=env, capture_output=True, text=True).stdout)
В этом примере мы использовали опцию env для установки переменной окружения MYVAR 
со значением myvalue и выполнения команды env, которая отображает все переменные окружения.
</code></pre>
<p>Запуск процесса в фоновом режиме</p>
<pre><code class="language-python">import subprocess

subprocess.Popen([&quot;python&quot;, &quot;myscript.py&quot;])
</code></pre>
<p>Этот пример запускает скрипт myscript.py в фоновом режиме.</p>
<p>Подключение к существующему процессу</p>
<pre><code class="language-python">import subprocess

process = subprocess.Popen([&quot;ssh&quot;, &quot;user@remotehost&quot;], stdin=subprocess.PIPE, stdout=subprocess.PIPE)

stdin_data = &quot;ls\n&quot;
process.stdin.write(stdin_data.encode())

stdout_data = process.stdout.readline()
print(stdout_data)
</code></pre>
<p>Этот пример подключается к удаленному хосту по SSH и выполняет команду ls. 
Мы используем метод write для передачи данных в стандартный ввод процесса, а метод readline для чтения данных из его стандартного вывода.</p>
<p>Запуск команды с аргументами</p>
<pre><code class="language-python">import subprocess

filename = &quot;example.txt&quot;
print(subprocess.run([&quot;wc&quot;, &quot;-l&quot;, filename], capture_output=True, text=True).stdout)
</code></pre>
<p>В этом примере мы использовали метод run для выполнения команды wc -l example.txt в командной строке. 
Мы передали аргументы команды в виде списка. </p>
<p>Получение кода возврата команды</p>
<pre><code class="language-python">import subprocess

print(subprocess.run([&quot;ls&quot;, &quot;nonexistent&quot;], capture_output=True, text=True).returncode)
</code></pre>
<p>В этом примере мы попытались выполнить команду ls nonexistent, которая должна завершиться с ошибкой, 
потому что файла nonexistent не существует. 
Мы использовали атрибут returncode объекта CompletedProcess, 
который содержит код возврата команды. 
В данном случае он равен 1, что означает ошибку.</p>
<p>Запуск команды с использованием shell</p>
<pre><code class="language-python">import subprocess

print(subprocess.run('echo &quot;Hello, world!&quot;', shell=True, capture_output=True, text=True).stdout)
</code></pre>
<p>В этом примере мы использовали опцию shell=True, чтобы выполнить команду echo "Hello, world!" через оболочку. 
Результат выводится на экран.</p>
<p>Запуск команды с заданием текущей директории</p>
<pre><code class="language-python">import subprocess

print(subprocess.run([&quot;ls&quot;], cwd=&quot;/tmp&quot;, capture_output=True, text=True).stdout)
</code></pre>
<p>В этом примере мы использовали опцию cwd для выполнения команды ls в директории /tmp. 
Результат выводится на экран.</p>