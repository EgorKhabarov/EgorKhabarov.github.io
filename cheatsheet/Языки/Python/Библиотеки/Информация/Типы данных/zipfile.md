<p>Библиотека "zipfile" в Python используется для работы с архивами формата ZIP.
Она предоставляет функциональность для создания, чтения, обновления и извлечения файлов из архива.</p>
<p>Таблица методов библиотеки "zipfile" и их краткого описания:</p>
<p><code>ZipFile(file, mode="r", compression=ZIP_STORED, allowZip64=True)</code> - создает объект ZipFile, представляющий архив ZIP из файла. Режимы могут быть чтение ("r"), запись ("w") или добавление ("a").
<code>ZipFile.extractall(path=None, members=None, pwd=None)</code> - извлекает все файлы из архива в указанную папку.
<code>ZipFile.extract(member, path=None, pwd=None)</code> - извлекает конкретный файл из архива.
<code>ZipFile.namelist()</code> - возвращает список имен файлов в архиве.
<code>ZipFile.open(name, mode="r", pwd=None)</code> - открывает файл в архиве и возвращает объект файлового дескриптора.
<code>ZipFile.close()</code> - закрывает объект ZipFile и освобождает ресурсы.</p>
<p>Список самых часто используемых методов, их краткого описания и пример демонстрирующий их работу:</p>
<p><code>extractall(path=None, members=None, pwd=None)</code> - извлекает все файлы из архива в указанную папку.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button"id="code95d254a5167c8ff22aa545c49aa8fbcfb"onclick="copyCode(code95d254a5167c8ff22aa545c49aa8fbcf, code95d254a5167c8ff22aa545c49aa8fbcfb)"><svg stroke="currentColor"fill="none"stroke-width="2"viewBox="0 0 24 24"stroke-linecap="round"stroke-linejoin="round"class="h-4 w-4"height="1em"width="1em"xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code95d254a5167c8ff22aa545c49aa8fbcf"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">zipfile</span>

<span class="c1"># Открываем архив</span>
<span class="k">with</span> <span class="n">zipfile</span><span class="o">.</span><span class="n">ZipFile</span><span class="p">(</span><span class="s2">&quot;archive.zip&quot;</span><span class="p">,</span> <span class="s2">&quot;r&quot;</span><span class="p">)</span> <span class="k">as</span> <span class="n">zip_ref</span><span class="p">:</span>
    <span class="c1"># Извлекаем все файлы</span>
    <span class="n">zip_ref</span><span class="o">.</span><span class="n">extractall</span><span class="p">(</span><span class="s2">&quot;destination_folder&quot;</span><span class="p">)</span>
</pre></div></div></div>

<p><code>namelist()</code> - возвращает список имен файлов в архиве.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button"id="code2a7af97cc2f52b7205b0b92aab6a7694b"onclick="copyCode(code2a7af97cc2f52b7205b0b92aab6a7694, code2a7af97cc2f52b7205b0b92aab6a7694b)"><svg stroke="currentColor"fill="none"stroke-width="2"viewBox="0 0 24 24"stroke-linecap="round"stroke-linejoin="round"class="h-4 w-4"height="1em"width="1em"xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code2a7af97cc2f52b7205b0b92aab6a7694"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">zipfile</span>

<span class="c1"># Открываем архив</span>
<span class="k">with</span> <span class="n">zipfile</span><span class="o">.</span><span class="n">ZipFile</span><span class="p">(</span><span class="s2">&quot;archive.zip&quot;</span><span class="p">,</span> <span class="s2">&quot;r&quot;</span><span class="p">)</span> <span class="k">as</span> <span class="n">zip_ref</span><span class="p">:</span>
    <span class="c1"># Получаем список имен файлов</span>
    <span class="n">file_names</span> <span class="o">=</span> <span class="n">zip_ref</span><span class="o">.</span><span class="n">namelist</span><span class="p">()</span>

    <span class="c1"># Выводим список имен файлов</span>
    <span class="k">for</span> <span class="n">name</span> <span class="ow">in</span> <span class="n">file_names</span><span class="p">:</span>
        <span class="nb">print</span><span class="p">(</span><span class="n">name</span><span class="p">)</span>
</pre></div></div></div>

<p><code>extract(member, path=None, pwd=None)</code> - извлекает конкретный файл из архива.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button"id="code70026e389327ae066d1d621cc71baa5db"onclick="copyCode(code70026e389327ae066d1d621cc71baa5d, code70026e389327ae066d1d621cc71baa5db)"><svg stroke="currentColor"fill="none"stroke-width="2"viewBox="0 0 24 24"stroke-linecap="round"stroke-linejoin="round"class="h-4 w-4"height="1em"width="1em"xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code70026e389327ae066d1d621cc71baa5d"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">zipfile</span>

<span class="c1"># Открываем архив</span>
<span class="k">with</span> <span class="n">zipfile</span><span class="o">.</span><span class="n">ZipFile</span><span class="p">(</span><span class="s2">&quot;archive.zip&quot;</span><span class="p">,</span> <span class="s2">&quot;r&quot;</span><span class="p">)</span> <span class="k">as</span> <span class="n">zip_ref</span><span class="p">:</span>
    <span class="c1"># Извлекаем файл с именем &quot;file.txt&quot;</span>
    <span class="n">zip_ref</span><span class="o">.</span><span class="n">extract</span><span class="p">(</span><span class="s2">&quot;file.txt&quot;</span><span class="p">,</span> <span class="s2">&quot;destination_folder&quot;</span><span class="p">)</span>
</pre></div></div></div>