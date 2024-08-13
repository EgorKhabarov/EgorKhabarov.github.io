<p>Dockerfile
FROM:    Определяет базовый образ, на основе которого будет создан ваш образ контейнера. 
         Здесь мы используем образ <code>Python 3.9</code> на основе <code>slim-версии Debian</code>.</p>
<p>WORKDIR: Устанавливает рабочую директорию внутри контейнера, где будут выполняться команды.</p>
<p>COPY:    Копирует файлы из текущей директории на вашем компьютере внутрь контейнера.</p>
<p>RUN:     Выполняет команды внутри контейнера для установки зависимостей, указанных в файле <code>requirements.txt</code>.</p>
<p>CMD:     Определяет команду, которая будет запущена при запуске контейнера. 
         Здесь мы указываем запуск основного скрипта <code>main.py</code>.</p>
<p>```Dockerfile@Dockerfile
FROM python:3.9-slim-buster</p>
<p>WORKDIR /app</p>
<p>COPY requirements.txt .</p>
<p>RUN pip3 install --no-cache-dir -r requirements.txt</p>
<p>COPY . .</p>
<p>CMD ["python3", "main.py"]</p>
<pre><code>

```Dockerfile
ENV BOT_TOKEN=&quot;&quot;
</code></pre>
<p><img alt="docker.png" src="Языки/Dockerfile/docker.png" /></p>