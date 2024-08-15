<p>Dockerfile
FROM:    Определяет базовый образ, на основе которого будет создан ваш образ контейнера. 
         Здесь мы используем образ <code>Python 3.9</code> на основе <code>slim-версии Debian</code>.</p>
<p>WORKDIR: Устанавливает рабочую директорию внутри контейнера, где будут выполняться команды.</p>
<p>COPY:    Копирует файлы из текущей директории на вашем компьютере внутрь контейнера.</p>
<p>RUN:     Выполняет команды внутри контейнера для установки зависимостей, указанных в файле <code>requirements.txt</code>.</p>
<p>CMD:     Определяет команду, которая будет запущена при запуске контейнера. 
         Здесь мы указываем запуск основного скрипта <code>main.py</code>.</p>
<div class="code-element"><div class="lang-line"><text>Dockerfile</text><button class="copy-button" onclick="copyCode(this)"><svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button><button class="copy-button-2" onclick="DownloadCode(this, `Dockerfile`)"><svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 3v4a1 1 0 0 1-1 1H5m5 4-2 2 2 2m4-4 2 2-2 2m5-12v16a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V7.914a1 1 0 0 1 .293-.707l3.914-3.914A1 1 0 0 1 9.914 3H18a1 1 0 0 1 1 1Z"/></svg><pre>Download code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="k">FROM</span><span class="w"> </span><span class="s">python:3.9-slim-buster</span>

<span class="k">WORKDIR</span><span class="w"> </span><span class="s">/app</span>

<span class="k">COPY</span><span class="w"> </span>requirements.txt<span class="w"> </span>.

<span class="k">RUN</span><span class="w"> </span>pip3<span class="w"> </span>install<span class="w"> </span>--no-cache-dir<span class="w"> </span>-r<span class="w"> </span>requirements.txt

<span class="k">COPY</span><span class="w"> </span>.<span class="w"> </span>.

<span class="k">CMD</span><span class="w"> </span><span class="p">[</span><span class="s2">&quot;python3&quot;</span><span class="p">,</span><span class="w"> </span><span class="s2">&quot;main.py&quot;</span><span class="p">]</span>
</pre></div></div></div>

<div class="code-element"><div class="lang-line"><text>Dockerfile</text><button class="copy-button" onclick="copyCode(this)"><svg aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="k">ENV</span><span class="w"> </span><span class="nv">BOT_TOKEN</span><span class="o">=</span><span class="s2">&quot;&quot;</span>
</pre></div></div></div>

<p><img alt="docker.png" src="Languages/Dockerfile/docker.png" /></p>