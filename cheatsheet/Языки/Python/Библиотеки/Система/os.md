<p>Получение информации о текущей директории:</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code19b" onclick="copyCode(code19, code19b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code19"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">os</span>

<span class="nb">print</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">getcwd</span><span class="p">())</span>
</pre></div></div></div>

<p>Создание директории:</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code20b" onclick="copyCode(code20, code20b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code20"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">os</span>

<span class="n">os</span><span class="o">.</span><span class="n">mkdir</span><span class="p">(</span><span class="s2">&quot;new_dir&quot;</span><span class="p">)</span>
</pre></div></div></div>

<p>Удаление директории:</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code21b" onclick="copyCode(code21, code21b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code21"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">os</span>

<span class="n">os</span><span class="o">.</span><span class="n">rmdir</span><span class="p">(</span><span class="s2">&quot;dir_to_remove&quot;</span><span class="p">)</span>
</pre></div></div></div>

<p>Проверка наличия файла или директории:</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code22b" onclick="copyCode(code22, code22b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code22"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">os</span>

<span class="k">if</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="s2">&quot;file.txt&quot;</span><span class="p">):</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;File exists!&quot;</span><span class="p">)</span>

<span class="k">if</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">exists</span><span class="p">(</span><span class="s2">&quot;dir&quot;</span><span class="p">):</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Directory exists!&quot;</span><span class="p">)</span>
</pre></div></div></div>

<p>Получение списка файлов в директории:</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code23b" onclick="copyCode(code23, code23b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code23"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">os</span>

<span class="n">files</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">listdir</span><span class="p">(</span><span class="s2">&quot;my_dir&quot;</span><span class="p">)</span>
<span class="k">for</span> <span class="n">file</span> <span class="ow">in</span> <span class="n">files</span><span class="p">:</span>
    <span class="nb">print</span><span class="p">(</span><span class="n">file</span><span class="p">)</span>
</pre></div></div></div>

<p>Переименование файла или директории:</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code24b" onclick="copyCode(code24, code24b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code24"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">os</span>

<span class="n">os</span><span class="o">.</span><span class="n">rename</span><span class="p">(</span><span class="s2">&quot;old_file.txt&quot;</span><span class="p">,</span> <span class="s2">&quot;new_file.txt&quot;</span><span class="p">)</span>
</pre></div></div></div>

<p>Удаление файла:</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code25b" onclick="copyCode(code25, code25b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code25"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">os</span>

<span class="n">os</span><span class="o">.</span><span class="n">remove</span><span class="p">(</span><span class="s2">&quot;file_to_remove.txt&quot;</span><span class="p">)</span>
</pre></div></div></div>

<p>Получение информации о файле:</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code26b" onclick="copyCode(code26, code26b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code26"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">os</span>

<span class="n">file_stat</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">stat</span><span class="p">(</span><span class="s2">&quot;file.txt&quot;</span><span class="p">)</span>

<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Size of file:&quot;</span><span class="p">,</span> <span class="n">file_stat</span><span class="o">.</span><span class="n">st_size</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Last accessed time:&quot;</span><span class="p">,</span> <span class="n">file_stat</span><span class="o">.</span><span class="n">st_atime</span><span class="p">)</span>
</pre></div></div></div>

<p>Проверка, является ли путь директорией или файлом:</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code27b" onclick="copyCode(code27, code27b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code27"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">os</span>

<span class="k">if</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">isfile</span><span class="p">(</span><span class="s2">&quot;my_file.txt&quot;</span><span class="p">):</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;This is a file!&quot;</span><span class="p">)</span>

<span class="k">if</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">isdir</span><span class="p">(</span><span class="s2">&quot;my_file.txt&quot;</span><span class="p">):</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;This is a directory!&quot;</span><span class="p">)</span>
</pre></div></div></div>

<p>Получение имени файла из пути:</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code28b" onclick="copyCode(code28, code28b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code28"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">os</span>

<span class="nb">print</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">basename</span><span class="p">(</span><span class="s2">&quot;/my_dir/my_file.txt&quot;</span><span class="p">))</span>
</pre></div></div></div>

<p>Получение пути к директории из пути к файлу:</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code29b" onclick="copyCode(code29, code29b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code29"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">os</span>

<span class="nb">print</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">dirname</span><span class="p">(</span><span class="s2">&quot;/my_dir/my_file.txt&quot;</span><span class="p">))</span>
</pre></div></div></div>

<p>Получение абсолютного пути:</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code30b" onclick="copyCode(code30, code30b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code30"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">os</span>

<span class="nb">print</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">abspath</span><span class="p">(</span><span class="s2">&quot;my_dir/my_file.txt&quot;</span><span class="p">))</span>
</pre></div></div></div>

<p>Объединение путей:</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code31b" onclick="copyCode(code31, code31b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code31"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">os</span>

<span class="nb">print</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="s2">&quot;/my_dir&quot;</span><span class="p">,</span> <span class="s2">&quot;my_file.txt&quot;</span><span class="p">))</span>
</pre></div></div></div>

<p>Получение расширения файла:</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code32b" onclick="copyCode(code32, code32b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code32"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">os</span>

<span class="nb">print</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">splitext</span><span class="p">(</span><span class="s2">&quot;my_file.txt&quot;</span><span class="p">)[</span><span class="mi">1</span><span class="p">])</span>
</pre></div></div></div>

<p>Получение списка всех поддиректорий в директории:</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code33b" onclick="copyCode(code33, code33b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code33"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">os</span>

<span class="nb">print</span><span class="p">([</span><span class="n">f</span><span class="o">.</span><span class="n">path</span> <span class="k">for</span> <span class="n">f</span> <span class="ow">in</span> <span class="n">os</span><span class="o">.</span><span class="n">scandir</span><span class="p">(</span><span class="s2">&quot;my_dir&quot;</span><span class="p">)</span> <span class="k">if</span> <span class="n">f</span><span class="o">.</span><span class="n">is_dir</span><span class="p">()])</span>
</pre></div></div></div>