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
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button"id="code3e7222170fd9ab8b0f3858e1d5844f00b"onclick="copyCode(code3e7222170fd9ab8b0f3858e1d5844f00, code3e7222170fd9ab8b0f3858e1d5844f00b)"><svg stroke="currentColor"fill="none"stroke-width="2"viewBox="0 0 24 24"stroke-linecap="round"stroke-linejoin="round"class="h-4 w-4"height="1em"width="1em"xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code3e7222170fd9ab8b0f3858e1d5844f00"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">errno</span>

<span class="n">error_codes</span> <span class="o">=</span> <span class="n">errno</span><span class="o">.</span><span class="n">errorcode</span>
<span class="nb">print</span><span class="p">(</span><span class="n">error_codes</span><span class="p">)</span>
</pre></div></div></div>

<p>errno.geterrno(): Возвращает код текущей ошибки. Например: 2.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button"id="code59f9d06903ca53e7ef7dffd9c4c0dc3db"onclick="copyCode(code59f9d06903ca53e7ef7dffd9c4c0dc3d, code59f9d06903ca53e7ef7dffd9c4c0dc3db)"><svg stroke="currentColor"fill="none"stroke-width="2"viewBox="0 0 24 24"stroke-linecap="round"stroke-linejoin="round"class="h-4 w-4"height="1em"width="1em"xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code59f9d06903ca53e7ef7dffd9c4c0dc3d"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">errno</span>

<span class="n">error_num</span> <span class="o">=</span> <span class="n">errno</span><span class="o">.</span><span class="n">geterrno</span><span class="p">()</span>
<span class="nb">print</span><span class="p">(</span><span class="n">error_num</span><span class="p">)</span>
</pre></div></div></div>

<p>errno.geterror(): Возвращает описание текущей ошибки в виде строки. Например: "No such file or directory".</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button"id="code7cb3a380ba5190609a6bb672e120a718b"onclick="copyCode(code7cb3a380ba5190609a6bb672e120a718, code7cb3a380ba5190609a6bb672e120a718b)"><svg stroke="currentColor"fill="none"stroke-width="2"viewBox="0 0 24 24"stroke-linecap="round"stroke-linejoin="round"class="h-4 w-4"height="1em"width="1em"xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code7cb3a380ba5190609a6bb672e120a718"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">errno</span>

<span class="n">error_desc</span> <span class="o">=</span> <span class="n">errno</span><span class="o">.</span><span class="n">geterror</span><span class="p">()</span>
<span class="nb">print</span><span class="p">(</span><span class="n">error_desc</span><span class="p">)</span>
</pre></div></div></div>