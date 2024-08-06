<p>Команда, которая создает список всех пакетов и их версий, 
установленных в настоящее время в среде Python.</p>
<div class="code-element">
<div class="lang-line">
  <text>python</text>
  <button class="copy-button"
          id="codea18c9df8a2db248117acc8fba0636aabb"
          onclick="copyCode(codea18c9df8a2db248117acc8fba0636aab, codea18c9df8a2db248117acc8fba0636aabb)">
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
<div class="code" id="codea18c9df8a2db248117acc8fba0636aab"><div class="highlight"><pre><span></span><span class="n">pip</span> <span class="n">freeze</span> <span class="o">&gt;</span> <span class="n">requirements</span><span class="o">.</span><span class="n">txt</span>
</pre></div></div>
</div>

<p>Файл <code>requirements.txt</code> используется для указания зависимостей для проекта Python. 
В нем перечислены пакеты и их версии, необходимые для правильной работы проекта. 
Это упрощает настройку той же среды на другом компьютере или при развертывании приложения в производственной среде.
Когда вы запустите <code>pip freeze &gt; requirements.txt</code>, он создаст новый файл с именем <code>requirements.txt</code>
в вашем текущем каталоге и запишет вывод <code>pip freeze</code> команды в этот файл, 
который будет содержать список всех пакетов и их версий, которые в 
настоящее время установлены в вашей среде Python, один пакет за строку.
Позже вы можете использовать </p>
<div class="code-element">
<div class="lang-line">
  <text>python</text>
  <button class="copy-button"
          id="code816ca882988334a55066f925766901c2b"
          onclick="copyCode(code816ca882988334a55066f925766901c2, code816ca882988334a55066f925766901c2b)">
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
<div class="code" id="code816ca882988334a55066f925766901c2"><div class="highlight"><pre><span></span><span class="n">pip</span> <span class="n">install</span> <span class="o">-</span><span class="n">r</span> <span class="n">requirements</span><span class="o">.</span><span class="n">txt</span>
</pre></div></div>
</div>

<p>для установки всех пакетов и их версий, перечисленныx в файле, 
это гарантирует, что среда такая же, как та, которая 
использовалась для создания <code>requirements.txt</code> файла.</p>
<p>Рекомендуется включить <code>requirements.txt</code> файл в репозиторий вашего проекта, 
чтобы другие разработчики или пользователи могли легко 
настроить ту же среду и запустить проект с правильными зависимостями.</p>
<p>Для создания файла с библиотеками используемыми только для нужного проекта использовать </p>
<div class="code-element">
<div class="lang-line">
  <text>python</text>
  <button class="copy-button"
          id="code1b3b5d517dd03ef981f2a3510fa843feb"
          onclick="copyCode(code1b3b5d517dd03ef981f2a3510fa843fe, code1b3b5d517dd03ef981f2a3510fa843feb)">
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
<div class="code" id="code1b3b5d517dd03ef981f2a3510fa843fe"><div class="highlight"><pre><span></span><span class="n">pip</span> <span class="n">freeze</span> <span class="o">--</span><span class="n">local</span> <span class="o">&gt;</span> <span class="n">requirements</span><span class="o">.</span><span class="n">txt</span>
</pre></div></div>
</div>