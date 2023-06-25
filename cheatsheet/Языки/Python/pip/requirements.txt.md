<p>Команда, которая создает список всех пакетов и их версий, 
установленных в настоящее время в среде Python.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code184b" onclick="copyCode(code184, code184b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code184"><div class="highlight"><pre><span></span><span class="n">pip</span> <span class="n">freeze</span> <span class="o">&gt;</span> <span class="n">requirements</span><span class="o">.</span><span class="n">txt</span>
</pre></div></div></div>

<p>Файл requirements.txt используется для указания зависимостей для проекта Python. 
В нем перечислены пакеты и их версии, необходимые для правильной работы проекта. 
Это упрощает настройку той же среды на другом компьютере или при развертывании приложения в производственной среде.
Когда вы запустите pip freeze &gt; requirements.txt, он создаст новый файл с именем requirements.txt
в вашем текущем каталоге и запишет вывод pip freeze команды в этот файл, 
который будет содержать список всех пакетов и их версий, которые в 
настоящее время установлены в вашей среде Python, один пакет за строку.
Позже вы можете использовать </p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code185b" onclick="copyCode(code185, code185b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code185"><div class="highlight"><pre><span></span><span class="n">pip</span> <span class="n">install</span> <span class="o">-</span><span class="n">r</span> <span class="n">requirements</span><span class="o">.</span><span class="n">txt</span>
</pre></div></div></div>

<p>для установки всех пакетов и их версий, перечисленныx в файле, 
это гарантирует, что среда такая же, как та, которая 
использовалась для создания requirements.txt файла.</p>
<p>Рекомендуется включить requirements.txt файл в репозиторий вашего проекта, 
чтобы другие разработчики или пользователи могли легко 
настроить ту же среду и запустить проект с правильными зависимостями.</p>
<p>Для создания файла с библиотеками используемыми только для нужного проекта использовать </p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" id="code186b" onclick="copyCode(code186, code186b)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code" id="code186"><div class="highlight"><pre><span></span><span class="n">pip</span> <span class="n">freeze</span> <span class="o">--</span><span class="n">local</span> <span class="o">&gt;</span> <span class="n">requirements</span><span class="o">.</span><span class="n">txt</span>
</pre></div></div></div>