<p>Библиотека "nt" в Python используется для работы с функциями операционной системы Windows.</p>
<p>Методы модуля "nt" и его подмодулей:</p>
<p>Модуль "nt":
nt.getcwd(): Возвращает текущую рабочую директорию.
nt.listdir(path): Возвращает список файлов и директорий в указанном пути.
nt.mkdir(path): Создает новую директорию по указанному пути.
nt.remove(path): Удаляет файл по указанному пути.
nt.rename(src, dst): Переименовывает файл или директорию.
nt.system(command): Выполняет команду операционной системы.</p>
<p>Подмодуль "ntpath":
ntpath.basename(path): Возвращает имя файла или директории из указанного пути.
ntpath.dirname(path): Возвращает имя директории из указанного пути.
ntpath.exists(path): Проверяет, существует ли файл или директория по указанному пути.
ntpath.join(path, *paths): Объединяет пути в один.
ntpath.split(path): Разделяет путь на имя директории и имя файла.</p>
<p>Некоторые часто используемые методы и их описание:</p>
<p>nt.getcwd(): Возвращает текущую рабочую директорию.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">nt</span>
<span class="n">current_dir</span> <span class="o">=</span> <span class="n">nt</span><span class="o">.</span><span class="n">getcwd</span><span class="p">()</span>
<span class="nb">print</span><span class="p">(</span><span class="n">current_dir</span><span class="p">)</span>
</pre></div></div></div>

<p>nt.listdir(path): Возвращает список файлов и директорий в указанном пути.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">nt</span>
<span class="n">file_list</span> <span class="o">=</span> <span class="n">nt</span><span class="o">.</span><span class="n">listdir</span><span class="p">(</span><span class="s2">&quot;C:/Users&quot;</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">file_list</span><span class="p">)</span>
</pre></div></div></div>

<p>nt.mkdir(path): Создает новую директорию по указанному пути.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">nt</span>
<span class="n">nt</span><span class="o">.</span><span class="n">mkdir</span><span class="p">(</span><span class="s2">&quot;C:/Users/NewDirectory&quot;</span><span class="p">)</span>
</pre></div></div></div>

<p>nt.remove(path): Удаляет файл по указанному пути.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">nt</span>
<span class="n">nt</span><span class="o">.</span><span class="n">remove</span><span class="p">(</span><span class="s2">&quot;C:/Users/example.txt&quot;</span><span class="p">)</span>
</pre></div></div></div>

<p>nt.rename(src, dst): Переименовывает файл или директорию.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">nt</span>
<span class="n">nt</span><span class="o">.</span><span class="n">rename</span><span class="p">(</span><span class="s2">&quot;C:/Users/old_name.txt&quot;</span><span class="p">,</span> <span class="s2">&quot;C:/Users/new_name.txt&quot;</span><span class="p">)</span>
</pre></div></div></div>

<p>nt.system(command): Выполняет команду операционной системы.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">nt</span>
<span class="n">nt</span><span class="o">.</span><span class="n">system</span><span class="p">(</span><span class="s2">&quot;dir&quot;</span><span class="p">)</span>
</pre></div></div></div>