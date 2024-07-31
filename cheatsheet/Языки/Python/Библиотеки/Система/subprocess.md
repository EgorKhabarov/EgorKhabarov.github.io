<p>Библиотека subprocess в Python используется для запуска новых процессов, подключения к существующим процессам, 
выполнения команд в командной строке и многого другого. 
Вот несколько примеров использования этой библиотеки:</p>
<p>Запуск команды в командной строке</p>
<div class="code-element">
<div class="lang-line">
  <text>python</text>
  <button class="copy-button"
          id="code6c001b5c0e4a50c557913582c036d09ab"
          onclick="copyCode(code6c001b5c0e4a50c557913582c036d09a, code6c001b5c0e4a50c557913582c036d09ab)">
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
<div class="code" id="code6c001b5c0e4a50c557913582c036d09a"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">subprocess</span>

<span class="nb">print</span><span class="p">(</span><span class="n">subprocess</span><span class="o">.</span><span class="n">run</span><span class="p">([</span><span class="s2">&quot;ls&quot;</span><span class="p">,</span> <span class="s2">&quot;-l&quot;</span><span class="p">],</span> <span class="n">capture_output</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">text</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span><span class="o">.</span><span class="n">stdout</span><span class="p">)</span>
</pre></div></div>
</div>

<p>В этом примере мы использовали метод run для выполнения команды ls -l в командной строке. 
Опция capture_output=True заставляет метод сохранять вывод команды, а опция text=True указывает, что мы ожидаем текстовый вывод.</p>
<p>Запуск команды с переменными окружения</p>
<div class="code-element">
<div class="lang-line">
  <text>python</text>
  <button class="copy-button"
          id="codeaca57aa92fc650d626335cee3a8eeda4b"
          onclick="copyCode(codeaca57aa92fc650d626335cee3a8eeda4, codeaca57aa92fc650d626335cee3a8eeda4b)">
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
<div class="code" id="codeaca57aa92fc650d626335cee3a8eeda4"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">subprocess</span>

<span class="n">env</span> <span class="o">=</span> <span class="p">{</span><span class="s2">&quot;MYVAR&quot;</span><span class="p">:</span> <span class="s2">&quot;myvalue&quot;</span><span class="p">}</span>
<span class="nb">print</span><span class="p">(</span><span class="n">subprocess</span><span class="o">.</span><span class="n">run</span><span class="p">([</span><span class="s2">&quot;env&quot;</span><span class="p">],</span> <span class="n">env</span><span class="o">=</span><span class="n">env</span><span class="p">,</span> <span class="n">capture_output</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">text</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span><span class="o">.</span><span class="n">stdout</span><span class="p">)</span>
<span class="n">В</span> <span class="n">этом</span> <span class="n">примере</span> <span class="n">мы</span> <span class="n">использовали</span> <span class="n">опцию</span> <span class="n">env</span> <span class="n">для</span> <span class="n">установки</span> <span class="n">переменной</span> <span class="n">окружения</span> <span class="n">MYVAR</span> 
<span class="n">со</span> <span class="n">значением</span> <span class="n">myvalue</span> <span class="n">и</span> <span class="n">выполнения</span> <span class="n">команды</span> <span class="n">env</span><span class="p">,</span> <span class="n">которая</span> <span class="n">отображает</span> <span class="n">все</span> <span class="n">переменные</span> <span class="n">окружения</span><span class="o">.</span>
</pre></div></div>
</div>

<p>Запуск процесса в фоновом режиме</p>
<div class="code-element">
<div class="lang-line">
  <text>python</text>
  <button class="copy-button"
          id="code26afe0f730325246b593fd08f2062e2ab"
          onclick="copyCode(code26afe0f730325246b593fd08f2062e2a, code26afe0f730325246b593fd08f2062e2ab)">
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
<div class="code" id="code26afe0f730325246b593fd08f2062e2a"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">subprocess</span>

<span class="n">subprocess</span><span class="o">.</span><span class="n">Popen</span><span class="p">([</span><span class="s2">&quot;python&quot;</span><span class="p">,</span> <span class="s2">&quot;myscript.py&quot;</span><span class="p">])</span>
</pre></div></div>
</div>

<p>Этот пример запускает скрипт myscript.py в фоновом режиме.</p>
<p>Подключение к существующему процессу</p>
<div class="code-element">
<div class="lang-line">
  <text>python</text>
  <button class="copy-button"
          id="code6ac9ff6aaf6fa3879e670fe82981709eb"
          onclick="copyCode(code6ac9ff6aaf6fa3879e670fe82981709e, code6ac9ff6aaf6fa3879e670fe82981709eb)">
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
<div class="code" id="code6ac9ff6aaf6fa3879e670fe82981709e"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">subprocess</span>

<span class="n">process</span> <span class="o">=</span> <span class="n">subprocess</span><span class="o">.</span><span class="n">Popen</span><span class="p">([</span><span class="s2">&quot;ssh&quot;</span><span class="p">,</span> <span class="s2">&quot;user@remotehost&quot;</span><span class="p">],</span> <span class="n">stdin</span><span class="o">=</span><span class="n">subprocess</span><span class="o">.</span><span class="n">PIPE</span><span class="p">,</span> <span class="n">stdout</span><span class="o">=</span><span class="n">subprocess</span><span class="o">.</span><span class="n">PIPE</span><span class="p">)</span>

<span class="n">stdin_data</span> <span class="o">=</span> <span class="s2">&quot;ls</span><span class="se">\n</span><span class="s2">&quot;</span>
<span class="n">process</span><span class="o">.</span><span class="n">stdin</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">stdin_data</span><span class="o">.</span><span class="n">encode</span><span class="p">())</span>

<span class="n">stdout_data</span> <span class="o">=</span> <span class="n">process</span><span class="o">.</span><span class="n">stdout</span><span class="o">.</span><span class="n">readline</span><span class="p">()</span>
<span class="nb">print</span><span class="p">(</span><span class="n">stdout_data</span><span class="p">)</span>
</pre></div></div>
</div>

<p>Этот пример подключается к удаленному хосту по SSH и выполняет команду ls. 
Мы используем метод write для передачи данных в стандартный ввод процесса, а метод readline для чтения данных из его стандартного вывода.</p>
<p>Запуск команды с аргументами</p>
<div class="code-element">
<div class="lang-line">
  <text>python</text>
  <button class="copy-button"
          id="codecc3f549a0f2022833f7bdf474c95b134b"
          onclick="copyCode(codecc3f549a0f2022833f7bdf474c95b134, codecc3f549a0f2022833f7bdf474c95b134b)">
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
<div class="code" id="codecc3f549a0f2022833f7bdf474c95b134"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">subprocess</span>

<span class="n">filename</span> <span class="o">=</span> <span class="s2">&quot;example.txt&quot;</span>
<span class="nb">print</span><span class="p">(</span><span class="n">subprocess</span><span class="o">.</span><span class="n">run</span><span class="p">([</span><span class="s2">&quot;wc&quot;</span><span class="p">,</span> <span class="s2">&quot;-l&quot;</span><span class="p">,</span> <span class="n">filename</span><span class="p">],</span> <span class="n">capture_output</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">text</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span><span class="o">.</span><span class="n">stdout</span><span class="p">)</span>
</pre></div></div>
</div>

<p>В этом примере мы использовали метод run для выполнения команды wc -l example.txt в командной строке. 
Мы передали аргументы команды в виде списка. </p>
<p>Получение кода возврата команды</p>
<div class="code-element">
<div class="lang-line">
  <text>python</text>
  <button class="copy-button"
          id="code89a364512509a3f24581faf290c47e84b"
          onclick="copyCode(code89a364512509a3f24581faf290c47e84, code89a364512509a3f24581faf290c47e84b)">
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
<div class="code" id="code89a364512509a3f24581faf290c47e84"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">subprocess</span>

<span class="nb">print</span><span class="p">(</span><span class="n">subprocess</span><span class="o">.</span><span class="n">run</span><span class="p">([</span><span class="s2">&quot;ls&quot;</span><span class="p">,</span> <span class="s2">&quot;nonexistent&quot;</span><span class="p">],</span> <span class="n">capture_output</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">text</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span><span class="o">.</span><span class="n">returncode</span><span class="p">)</span>
</pre></div></div>
</div>

<p>В этом примере мы попытались выполнить команду ls nonexistent, которая должна завершиться с ошибкой, 
потому что файла nonexistent не существует. 
Мы использовали атрибут returncode объекта CompletedProcess, 
который содержит код возврата команды. 
В данном случае он равен 1, что означает ошибку.</p>
<p>Запуск команды с использованием shell</p>
<div class="code-element">
<div class="lang-line">
  <text>python</text>
  <button class="copy-button"
          id="code569b7358fb9c41fbe856295194ca7a90b"
          onclick="copyCode(code569b7358fb9c41fbe856295194ca7a90, code569b7358fb9c41fbe856295194ca7a90b)">
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
<div class="code" id="code569b7358fb9c41fbe856295194ca7a90"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">subprocess</span>

<span class="nb">print</span><span class="p">(</span><span class="n">subprocess</span><span class="o">.</span><span class="n">run</span><span class="p">(</span><span class="s1">&#39;echo &quot;Hello, world!&quot;&#39;</span><span class="p">,</span> <span class="n">shell</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">capture_output</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">text</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span><span class="o">.</span><span class="n">stdout</span><span class="p">)</span>
</pre></div></div>
</div>

<p>В этом примере мы использовали опцию shell=True, чтобы выполнить команду echo "Hello, world!" через оболочку. 
Результат выводится на экран.</p>
<p>Запуск команды с заданием текущей директории</p>
<div class="code-element">
<div class="lang-line">
  <text>python</text>
  <button class="copy-button"
          id="codef87a6734c893cc605242709e18319677b"
          onclick="copyCode(codef87a6734c893cc605242709e18319677, codef87a6734c893cc605242709e18319677b)">
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
<div class="code" id="codef87a6734c893cc605242709e18319677"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">subprocess</span>

<span class="nb">print</span><span class="p">(</span><span class="n">subprocess</span><span class="o">.</span><span class="n">run</span><span class="p">([</span><span class="s2">&quot;ls&quot;</span><span class="p">],</span> <span class="n">cwd</span><span class="o">=</span><span class="s2">&quot;/tmp&quot;</span><span class="p">,</span> <span class="n">capture_output</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">text</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span><span class="o">.</span><span class="n">stdout</span><span class="p">)</span>
</pre></div></div>
</div>

<p>В этом примере мы использовали опцию cwd для выполнения команды ls в директории /tmp. 
Результат выводится на экран.</p>