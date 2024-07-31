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
<div class="code-element">
<div class="lang-line">
  <text>python</text>
  <button class="copy-button"
          id="code7c278f79692c4c6401a99f41b4f14e24b"
          onclick="copyCode(code7c278f79692c4c6401a99f41b4f14e24, code7c278f79692c4c6401a99f41b4f14e24b)">
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
<div class="code" id="code7c278f79692c4c6401a99f41b4f14e24"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">nt</span>
<span class="n">current_dir</span> <span class="o">=</span> <span class="n">nt</span><span class="o">.</span><span class="n">getcwd</span><span class="p">()</span>
<span class="nb">print</span><span class="p">(</span><span class="n">current_dir</span><span class="p">)</span>
</pre></div></div>
</div>

<p>nt.listdir(path): Возвращает список файлов и директорий в указанном пути.</p>
<div class="code-element">
<div class="lang-line">
  <text>python</text>
  <button class="copy-button"
          id="codee286e497ed52151f85af45b495eb41ebb"
          onclick="copyCode(codee286e497ed52151f85af45b495eb41eb, codee286e497ed52151f85af45b495eb41ebb)">
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
<div class="code" id="codee286e497ed52151f85af45b495eb41eb"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">nt</span>
<span class="n">file_list</span> <span class="o">=</span> <span class="n">nt</span><span class="o">.</span><span class="n">listdir</span><span class="p">(</span><span class="s2">&quot;C:/Users&quot;</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">file_list</span><span class="p">)</span>
</pre></div></div>
</div>

<p>nt.mkdir(path): Создает новую директорию по указанному пути.</p>
<div class="code-element">
<div class="lang-line">
  <text>python</text>
  <button class="copy-button"
          id="code75cece4fa78439eaa9fcaf2383d53c84b"
          onclick="copyCode(code75cece4fa78439eaa9fcaf2383d53c84, code75cece4fa78439eaa9fcaf2383d53c84b)">
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
<div class="code" id="code75cece4fa78439eaa9fcaf2383d53c84"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">nt</span>
<span class="n">nt</span><span class="o">.</span><span class="n">mkdir</span><span class="p">(</span><span class="s2">&quot;C:/Users/NewDirectory&quot;</span><span class="p">)</span>
</pre></div></div>
</div>

<p>nt.remove(path): Удаляет файл по указанному пути.</p>
<div class="code-element">
<div class="lang-line">
  <text>python</text>
  <button class="copy-button"
          id="codea22f32f5655b61718f050f8a77ee66afb"
          onclick="copyCode(codea22f32f5655b61718f050f8a77ee66af, codea22f32f5655b61718f050f8a77ee66afb)">
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
<div class="code" id="codea22f32f5655b61718f050f8a77ee66af"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">nt</span>
<span class="n">nt</span><span class="o">.</span><span class="n">remove</span><span class="p">(</span><span class="s2">&quot;C:/Users/example.txt&quot;</span><span class="p">)</span>
</pre></div></div>
</div>

<p>nt.rename(src, dst): Переименовывает файл или директорию.</p>
<div class="code-element">
<div class="lang-line">
  <text>python</text>
  <button class="copy-button"
          id="code70a2fc0d1eb212e64aa290195336fce6b"
          onclick="copyCode(code70a2fc0d1eb212e64aa290195336fce6, code70a2fc0d1eb212e64aa290195336fce6b)">
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
<div class="code" id="code70a2fc0d1eb212e64aa290195336fce6"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">nt</span>
<span class="n">nt</span><span class="o">.</span><span class="n">rename</span><span class="p">(</span><span class="s2">&quot;C:/Users/old_name.txt&quot;</span><span class="p">,</span> <span class="s2">&quot;C:/Users/new_name.txt&quot;</span><span class="p">)</span>
</pre></div></div>
</div>

<p>nt.system(command): Выполняет команду операционной системы.</p>
<div class="code-element">
<div class="lang-line">
  <text>python</text>
  <button class="copy-button"
          id="coded157a416a3264166f5655b7cc5998783b"
          onclick="copyCode(coded157a416a3264166f5655b7cc5998783, coded157a416a3264166f5655b7cc5998783b)">
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
<div class="code" id="coded157a416a3264166f5655b7cc5998783"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">nt</span>
<span class="n">nt</span><span class="o">.</span><span class="n">system</span><span class="p">(</span><span class="s2">&quot;dir&quot;</span><span class="p">)</span>
</pre></div></div>
</div>