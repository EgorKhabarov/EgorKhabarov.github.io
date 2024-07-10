<p>Библиотека "zipfile" в Python используется для работы с архивами формата ZIP.
Она предоставляет функциональность для создания, чтения, обновления и извлечения файлов из архива.</p>
<p>Таблица методов библиотеки "zipfile" и их краткого описания:</p>
<p><code>ZipFile(file, mode='r', compression=ZIP_STORED, allowZip64=True)</code> - создает объект ZipFile, представляющий архив ZIP из файла. Режимы могут быть чтение ('r'), запись ('w') или добавление ('a').
<code>ZipFile.extractall(path=None, members=None, pwd=None)</code> - извлекает все файлы из архива в указанную папку.
<code>ZipFile.extract(member, path=None, pwd=None)</code> - извлекает конкретный файл из архива.
<code>ZipFile.namelist()</code> - возвращает список имен файлов в архиве.
<code>ZipFile.open(name, mode='r', pwd=None)</code> - открывает файл в архиве и возвращает объект файлового дескриптора.
<code>ZipFile.close()</code> - закрывает объект ZipFile и освобождает ресурсы.</p>
<p>Список самых часто используемых методов, их краткого описания и пример демонстрирующий их работу:</p>
<p><code>extractall(path=None, members=None, pwd=None)</code> - извлекает все файлы из архива в указанную папку.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="codeffb132728373b2f8ae358672ea5d51a3b" onclick="copyCode(codeffb132728373b2f8ae358672ea5d51a3, codeffb132728373b2f8ae358672ea5d51a3b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="codeffb132728373b2f8ae358672ea5d51a3"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">zipfile</span>

<span class="c1"># Открываем архив</span>
<span class="k">with</span> <span class="n">zipfile</span><span class="o">.</span><span class="n">ZipFile</span><span class="p">(</span><span class="s1">&#39;archive.zip&#39;</span><span class="p">,</span> <span class="s1">&#39;r&#39;</span><span class="p">)</span> <span class="k">as</span> <span class="n">zip_ref</span><span class="p">:</span>
    <span class="c1"># Извлекаем все файлы</span>
    <span class="n">zip_ref</span><span class="o">.</span><span class="n">extractall</span><span class="p">(</span><span class="s1">&#39;destination_folder&#39;</span><span class="p">)</span>
</pre></div></div></div>

<p><code>namelist()</code> - возвращает список имен файлов в архиве.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code91a95af2496f98a3ff4054a14e60a3a8b" onclick="copyCode(code91a95af2496f98a3ff4054a14e60a3a8, code91a95af2496f98a3ff4054a14e60a3a8b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code91a95af2496f98a3ff4054a14e60a3a8"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">zipfile</span>

<span class="c1"># Открываем архив</span>
<span class="k">with</span> <span class="n">zipfile</span><span class="o">.</span><span class="n">ZipFile</span><span class="p">(</span><span class="s1">&#39;archive.zip&#39;</span><span class="p">,</span> <span class="s1">&#39;r&#39;</span><span class="p">)</span> <span class="k">as</span> <span class="n">zip_ref</span><span class="p">:</span>
    <span class="c1"># Получаем список имен файлов</span>
    <span class="n">file_names</span> <span class="o">=</span> <span class="n">zip_ref</span><span class="o">.</span><span class="n">namelist</span><span class="p">()</span>

    <span class="c1"># Выводим список имен файлов</span>
    <span class="k">for</span> <span class="n">name</span> <span class="ow">in</span> <span class="n">file_names</span><span class="p">:</span>
        <span class="nb">print</span><span class="p">(</span><span class="n">name</span><span class="p">)</span>
</pre></div></div></div>

<p><code>extract(member, path=None, pwd=None)</code> - извлекает конкретный файл из архива.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="codeba2e018868f6fb6ef70861a012e6462bb" onclick="copyCode(codeba2e018868f6fb6ef70861a012e6462b, codeba2e018868f6fb6ef70861a012e6462bb)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="codeba2e018868f6fb6ef70861a012e6462b"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">zipfile</span>

<span class="c1"># Открываем архив</span>
<span class="k">with</span> <span class="n">zipfile</span><span class="o">.</span><span class="n">ZipFile</span><span class="p">(</span><span class="s1">&#39;archive.zip&#39;</span><span class="p">,</span> <span class="s1">&#39;r&#39;</span><span class="p">)</span> <span class="k">as</span> <span class="n">zip_ref</span><span class="p">:</span>
    <span class="c1"># Извлекаем файл с именем &#39;file.txt&#39;</span>
    <span class="n">zip_ref</span><span class="o">.</span><span class="n">extract</span><span class="p">(</span><span class="s1">&#39;file.txt&#39;</span><span class="p">,</span> <span class="s1">&#39;destination_folder&#39;</span><span class="p">)</span>
</pre></div></div></div>