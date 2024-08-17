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
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-code-button" onclick="copyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">zipfile</span>

<span class="c1"># Открываем архив</span>
<span class="k">with</span> <span class="n">zipfile</span><span class="o">.</span><span class="n">ZipFile</span><span class="p">(</span><span class="s2">&quot;archive.zip&quot;</span><span class="p">,</span> <span class="s2">&quot;r&quot;</span><span class="p">)</span> <span class="k">as</span> <span class="n">zip_ref</span><span class="p">:</span>
    <span class="c1"># Извлекаем все файлы</span>
    <span class="n">zip_ref</span><span class="o">.</span><span class="n">extractall</span><span class="p">(</span><span class="s2">&quot;destination_folder&quot;</span><span class="p">)</span>
</pre></div></div></div>

<p><code>namelist()</code> - возвращает список имен файлов в архиве.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-code-button" onclick="copyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">zipfile</span>

<span class="c1"># Открываем архив</span>
<span class="k">with</span> <span class="n">zipfile</span><span class="o">.</span><span class="n">ZipFile</span><span class="p">(</span><span class="s2">&quot;archive.zip&quot;</span><span class="p">,</span> <span class="s2">&quot;r&quot;</span><span class="p">)</span> <span class="k">as</span> <span class="n">zip_ref</span><span class="p">:</span>
    <span class="c1"># Получаем список имен файлов</span>
    <span class="n">file_names</span> <span class="o">=</span> <span class="n">zip_ref</span><span class="o">.</span><span class="n">namelist</span><span class="p">()</span>

    <span class="c1"># Выводим список имен файлов</span>
    <span class="k">for</span> <span class="n">name</span> <span class="ow">in</span> <span class="n">file_names</span><span class="p">:</span>
        <span class="nb">print</span><span class="p">(</span><span class="n">name</span><span class="p">)</span>
</pre></div></div></div>

<p><code>extract(member, path=None, pwd=None)</code> - извлекает конкретный файл из архива.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-code-button" onclick="copyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">zipfile</span>

<span class="c1"># Открываем архив</span>
<span class="k">with</span> <span class="n">zipfile</span><span class="o">.</span><span class="n">ZipFile</span><span class="p">(</span><span class="s2">&quot;archive.zip&quot;</span><span class="p">,</span> <span class="s2">&quot;r&quot;</span><span class="p">)</span> <span class="k">as</span> <span class="n">zip_ref</span><span class="p">:</span>
    <span class="c1"># Извлекаем файл с именем &quot;file.txt&quot;</span>
    <span class="n">zip_ref</span><span class="o">.</span><span class="n">extract</span><span class="p">(</span><span class="s2">&quot;file.txt&quot;</span><span class="p">,</span> <span class="s2">&quot;destination_folder&quot;</span><span class="p">)</span>
</pre></div></div></div>