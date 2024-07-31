<p>import logging</p>
<p>Запись в файл</p>
<div class="code-element">
<div class="lang-line">
  <text>python</text>
  <button class="copy-button"
          id="code189f3ddce9a51329d776583239b52ff8b"
          onclick="copyCode(code189f3ddce9a51329d776583239b52ff8, code189f3ddce9a51329d776583239b52ff8b)">
    <svg stroke="currentColor"
         fill="none"
         stroke-width="2"
         viewBox="0 0 24 24"
         stroke-linecap="round"
         stroke-linejoin="round"
         class="h-4 w-4"
         height="1em"
         width="1em"
         xmlns="http://www.w3.org/2000/svg">
      <path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path>
      <rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect>
    </svg>
    <text>Copy code</text>
  </button>

</div>
<div class="code" id="code189f3ddce9a51329d776583239b52ff8"><div class="highlight"><pre><span></span><span class="n">logging</span><span class="o">.</span><span class="n">basicConfig</span><span class="p">(</span><span class="n">filename</span><span class="o">=</span><span class="s2">&quot;example.log&quot;</span><span class="p">,</span>
                    <span class="n">level</span><span class="o">=</span><span class="n">logging</span><span class="o">.</span><span class="n">DEBUG</span><span class="p">)</span>
</pre></div></div>
</div>

<p>Запись в консоль</p>
<div class="code-element">
<div class="lang-line">
  <text>python</text>
  <button class="copy-button"
          id="code4f484d4e4fdfc6cfdd7d885043822066b"
          onclick="copyCode(code4f484d4e4fdfc6cfdd7d885043822066, code4f484d4e4fdfc6cfdd7d885043822066b)">
    <svg stroke="currentColor"
         fill="none"
         stroke-width="2"
         viewBox="0 0 24 24"
         stroke-linecap="round"
         stroke-linejoin="round"
         class="h-4 w-4"
         height="1em"
         width="1em"
         xmlns="http://www.w3.org/2000/svg">
      <path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path>
      <rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect>
    </svg>
    <text>Copy code</text>
  </button>

</div>
<div class="code" id="code4f484d4e4fdfc6cfdd7d885043822066"><div class="highlight"><pre><span></span><span class="n">logging</span><span class="o">.</span><span class="n">basicConfig</span><span class="p">(</span><span class="n">level</span><span class="o">=</span><span class="n">logging</span><span class="o">.</span><span class="n">DEBUG</span><span class="p">,</span>
                    <span class="nb">format</span><span class="o">=</span><span class="s2">&quot;</span><span class="si">%(message)s</span><span class="s2">&quot;</span><span class="p">)</span>
</pre></div></div>
</div>

<p>Запись в файл и в консоль</p>
<div class="code-element">
<div class="lang-line">
  <text>python</text>
  <button class="copy-button"
          id="codeb2044b2f0ff660e8b4c3eedba4d60d11b"
          onclick="copyCode(codeb2044b2f0ff660e8b4c3eedba4d60d11, codeb2044b2f0ff660e8b4c3eedba4d60d11b)">
    <svg stroke="currentColor"
         fill="none"
         stroke-width="2"
         viewBox="0 0 24 24"
         stroke-linecap="round"
         stroke-linejoin="round"
         class="h-4 w-4"
         height="1em"
         width="1em"
         xmlns="http://www.w3.org/2000/svg">
      <path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path>
      <rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect>
    </svg>
    <text>Copy code</text>
  </button>

</div>
<div class="code" id="codeb2044b2f0ff660e8b4c3eedba4d60d11"><div class="highlight"><pre><span></span><span class="n">logging</span><span class="o">.</span><span class="n">basicConfig</span><span class="p">(</span><span class="n">filename</span><span class="o">=</span><span class="s2">&quot;example.log&quot;</span><span class="p">,</span>
                    <span class="n">level</span><span class="o">=</span><span class="n">logging</span><span class="o">.</span><span class="n">DEBUG</span><span class="p">,</span>
                    <span class="nb">format</span><span class="o">=</span><span class="s2">&quot;</span><span class="si">%(asctime)s</span><span class="s2"> </span><span class="si">%(levelname)s</span><span class="s2"> </span><span class="si">%(message)s</span><span class="s2">&quot;</span><span class="p">,</span>
                    <span class="n">datefmt</span><span class="o">=</span><span class="s2">&quot;%Y-%m-</span><span class="si">%d</span><span class="s2"> %H:%M:%S&quot;</span><span class="p">)</span>
<span class="n">console</span> <span class="o">=</span> <span class="n">logging</span><span class="o">.</span><span class="n">StreamHandler</span><span class="p">()</span>
<span class="n">console</span><span class="o">.</span><span class="n">setLevel</span><span class="p">(</span><span class="n">logging</span><span class="o">.</span><span class="n">DEBUG</span><span class="p">)</span>
<span class="n">formatter</span> <span class="o">=</span> <span class="n">logging</span><span class="o">.</span><span class="n">Formatter</span><span class="p">(</span><span class="s2">&quot;</span><span class="si">%(asctime)s</span><span class="s2"> &quot;</span>
                              <span class="s2">&quot;</span><span class="si">%(levelname)s</span><span class="s2"> &quot;</span>
                              <span class="s2">&quot;</span><span class="si">%(message)s</span><span class="s2">&quot;</span><span class="p">,</span>
                              <span class="n">datefmt</span><span class="o">=</span><span class="s2">&quot;%Y-%m-</span><span class="si">%d</span><span class="s2"> %H:%M:%S&quot;</span><span class="p">)</span>
<span class="n">console</span><span class="o">.</span><span class="n">setFormatter</span><span class="p">(</span><span class="n">formatter</span><span class="p">)</span>
<span class="n">logging</span><span class="o">.</span><span class="n">getLogger</span><span class="p">(</span><span class="s2">&quot;&quot;</span><span class="p">)</span><span class="o">.</span><span class="n">addHandler</span><span class="p">(</span><span class="n">console</span><span class="p">)</span>
</pre></div></div>
</div>

<p>Для самих сообщений</p>
<div class="code-element">
<div class="lang-line">
  <text>text</text>
  <button class="copy-button"
          id="codeed98c162d955d297bd260c3ea8c468e7b"
          onclick="copyCode(codeed98c162d955d297bd260c3ea8c468e7, codeed98c162d955d297bd260c3ea8c468e7b)">
    <svg stroke="currentColor"
         fill="none"
         stroke-width="2"
         viewBox="0 0 24 24"
         stroke-linecap="round"
         stroke-linejoin="round"
         class="h-4 w-4"
         height="1em"
         width="1em"
         xmlns="http://www.w3.org/2000/svg">
      <path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path>
      <rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect>
    </svg>
    <text>Copy code</text>
  </button>

</div>
<div class="code" id="codeed98c162d955d297bd260c3ea8c468e7"><div class="highlight"><pre><span></span>%s           строка
%d           для целых чисел
%c           для имени логгера
%f           для чисел с плавающей точкой
%r           для строковых представлений объектов
%m           для сообщения журнала
%x           целое число в шестнадцатеричной системе исчисления
%o           целое число в восьмеричной системе исчисления
%e, %E       число в экспоненциальной форме
</pre></div></div>
</div>

<p>Для настроек логгирования</p>
<div class="code-element">
<div class="lang-line">
  <text>text</text>
  <button class="copy-button"
          id="codedb4a794f5e31cc106cc897d39902afc9b"
          onclick="copyCode(codedb4a794f5e31cc106cc897d39902afc9, codedb4a794f5e31cc106cc897d39902afc9b)">
    <svg stroke="currentColor"
         fill="none"
         stroke-width="2"
         viewBox="0 0 24 24"
         stroke-linecap="round"
         stroke-linejoin="round"
         class="h-4 w-4"
         height="1em"
         width="1em"
         xmlns="http://www.w3.org/2000/svg">
      <path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path>
      <rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect>
    </svg>
    <text>Copy code</text>
  </button>

</div>
<div class="code" id="codedb4a794f5e31cc106cc897d39902afc9"><div class="highlight"><pre><span></span>%(message)s     сообщение журнала

%(asctime)s     время записи сообщения в формате (по умолчанию YYYY-MM-DD HH:MM:SS,sss настраивать в basicConfig(datefmt))
%(created)f     время записи сообщения в секундах, начиная с 1 января 1970 года

%(filename)s    имя файла, в котором был вызван логгер
%(funcName)s    имя функции, в которой был вызван логгер
%(name)s        имя логгера, который записывает сообщение
%(module)s      имя модуля, в котором был вызван логгер
%(threadName)s  имя потока, в котором был вызван логгер
%(processName)s имя процесса, в котором был вызван логгер

%(levelname)s   уровень журнала (например, DEBUG, INFO, WARNING, ERROR, CRITICAL)
%(levelno)s     уровень журнала в числовом формате (10 для DEBUG, 20 для INFO и т. д.)

%(lineno)d      номер строки, в которой был вызван логгер
%(pathname)s    полный путь к файлу, в котором был вызван логгер
%(process)d     идентификатор процесса, в котором был вызван логгер
%(thread)d      идентификатор потока, в котором был вызван логгер
</pre></div></div>
</div>

<p>Код для применения функций к тексту</p>
<div class="code-element">
<div class="lang-line">
  <text>python</text>
  <button class="copy-button"
          id="code990d5b8801b791665bc3726ae9834157b"
          onclick="copyCode(code990d5b8801b791665bc3726ae9834157, code990d5b8801b791665bc3726ae9834157b)">
    <svg stroke="currentColor"
         fill="none"
         stroke-width="2"
         viewBox="0 0 24 24"
         stroke-linecap="round"
         stroke-linejoin="round"
         class="h-4 w-4"
         height="1em"
         width="1em"
         xmlns="http://www.w3.org/2000/svg">
      <path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path>
      <rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect>
    </svg>
    <text>Copy code</text>
  </button>

</div>
<div class="code" id="code990d5b8801b791665bc3726ae9834157"><div class="highlight"><pre><span></span><span class="n">logging</span><span class="o">.</span><span class="n">info</span> <span class="o">=</span> <span class="k">lambda</span> <span class="n">msg</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="n">f</span><span class="o">=</span><span class="n">logging</span><span class="o">.</span><span class="n">info</span><span class="p">:</span> <span class="n">f</span><span class="p">(</span><span class="n">Up</span><span class="p">(</span><span class="n">msg</span><span class="p">),</span> <span class="o">*</span><span class="n">args</span><span class="p">)</span>
</pre></div></div>
</div>