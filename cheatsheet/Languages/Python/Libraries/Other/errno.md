<p>Библиотека "errno" в Python используется для обработки ошибок, связанных с системными вызовами и функциями операционной системы.
Она предоставляет доступ к кодам ошибок, которые могут возникать
при выполнении операций ввода-вывода, работы с файлами, сетью и другими системными ресурсами.</p>
<p>Методы и подмодули библиотеки "errno":</p>
<p>errno.errorcode: Возвращает словарь, ключами которого являются коды ошибок, а значениями - соответствующие им символьные имена.
errno.geterrno(): Возвращает код текущей ошибки.
errno.geterror(): Возвращает описание текущей ошибки в виде строки.
errno.strerror(errno): Возвращает описание ошибки по заданному коду ошибки.
errno.clear(): Очищает код текущей ошибки.</p>
<p>Самые часто используемые методы библиотеки "errno":</p>
<p>errno.errorcode: Возвращает словарь, где ключами являются коды ошибок, а значениями - символьные имена.
Например: {"ENOENT": "No such file or directory", "EACCES": "Permission denied"}.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">errno</span>

<span class="n">error_codes</span> <span class="o">=</span> <span class="n">errno</span><span class="o">.</span><span class="n">errorcode</span>
<span class="nb">print</span><span class="p">(</span><span class="n">error_codes</span><span class="p">)</span>
</pre></div></div></div>

<p>errno.geterrno(): Возвращает код текущей ошибки. Например: 2.</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">errno</span>

<span class="n">error_num</span> <span class="o">=</span> <span class="n">errno</span><span class="o">.</span><span class="n">geterrno</span><span class="p">()</span>
<span class="nb">print</span><span class="p">(</span><span class="n">error_num</span><span class="p">)</span>
</pre></div></div></div>

<p>errno.geterror(): Возвращает описание текущей ошибки в виде строки. Например: "No such file or directory".</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">errno</span>

<span class="n">error_desc</span> <span class="o">=</span> <span class="n">errno</span><span class="o">.</span><span class="n">geterror</span><span class="p">()</span>
<span class="nb">print</span><span class="p">(</span><span class="n">error_desc</span><span class="p">)</span>
</pre></div></div></div>