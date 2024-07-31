<p>Библиотека "glob" предназначена для поиска файлов с использованием шаблонов и расширений в заданном каталоге.</p>
<p>Методы модуля "glob" и их краткое описание:</p>
<p>glob.glob(pathname): Возвращает список всех путей, соответствующих заданному шаблону.
glob.escape(pathname): Экранирует все специальные символы в заданном пути, чтобы они были интерпретированы как обычные символы.</p>
<p>Пример кода для демонстрации работы метода glob.glob():</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button"id="code122fbee5907918f9696b1fd1521d6af6b"onclick="copyCode(code122fbee5907918f9696b1fd1521d6af6, code122fbee5907918f9696b1fd1521d6af6b)"><svg stroke="currentColor"fill="none"stroke-width="2"viewBox="0 0 24 24"stroke-linecap="round"stroke-linejoin="round"class="h-4 w-4"height="1em"width="1em"xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code122fbee5907918f9696b1fd1521d6af6"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">glob</span>

<span class="n">files</span> <span class="o">=</span> <span class="n">glob</span><span class="o">.</span><span class="n">glob</span><span class="p">(</span><span class="s2">&quot;*.txt&quot;</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">files</span><span class="p">)</span>
</pre></div></div></div>

<p>В этом примере метод glob.glob("*.txt") ищет все файлы с расширением ".txt" в текущем каталоге и возвращает
список путей к этим файлам, который затем выводится на экран.</p>