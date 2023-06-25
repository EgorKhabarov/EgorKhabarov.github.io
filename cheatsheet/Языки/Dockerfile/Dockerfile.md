<p>Dockerfile
FROM:    Определяет базовый образ, на основе которого будет создан ваш образ контейнера. 
         Здесь мы используем образ Python 3.9 на основе slim-версии Debian.</p>
<p>WORKDIR: Устанавливает рабочую директорию внутри контейнера, где будут выполняться команды.</p>
<p>COPY:    Копирует файлы из текущей директории на вашем компьютере внутрь контейнера.</p>
<p>RUN:     Выполняет команды внутри контейнера для установки зависимостей, указанных в файле requirements.txt.</p>
<p>CMD:     Определяет команду, которая будет запущена при запуске контейнера. 
         Здесь мы указываем запуск основного скрипта main.py.</p>
<div class="code-element">
    <div class="lang-line">Dockerfile<button class="copy-button"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg">
    <path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button>
    </div>
    <div class="code"><div class="highlight"><pre><span></span><span class="k">FROM</span><span class="w"> </span><span class="s">python:3.9-slim-buster</span>

<span class="k">WORKDIR</span><span class="w"> </span><span class="s">/app</span>

<span class="k">COPY</span><span class="w"> </span>requirements.txt<span class="w"> </span>.

<span class="k">RUN</span><span class="w"> </span>pip3<span class="w"> </span>install<span class="w"> </span>--no-cache-dir<span class="w"> </span>-r<span class="w"> </span>requirements.txt

<span class="k">COPY</span><span class="w"> </span>.<span class="w"> </span>.

<span class="k">CMD</span><span class="w"> </span><span class="p">[</span><span class="s2">&quot;python3&quot;</span><span class="p">,</span><span class="w"> </span><span class="s2">&quot;main.py&quot;</span><span class="p">]</span>
</pre></div></div>
</div>

<div class="code-element">
    <div class="lang-line">Dockerfile<button class="copy-button"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg">
    <path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button>
    </div>
    <div class="code"><div class="highlight"><pre><span></span><span class="k">ENV</span><span class="w"> </span><span class="nv">BOT_TOKEN</span><span class="o">=</span><span class="s2">&quot;&quot;</span>
</pre></div></div>
</div>

<p><img alt="docker.png" src="cheatsheet\Языки\Dockerfile\docker.png"></p>