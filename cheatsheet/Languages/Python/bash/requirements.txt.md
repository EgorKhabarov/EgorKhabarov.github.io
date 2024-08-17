<p>Команда, которая создает список всех пакетов и их версий, 
установленных в настоящее время в среде Python.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-code-button" onclick="copyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="n">pip</span> <span class="n">freeze</span> <span class="o">&gt;</span> <span class="n">requirements</span><span class="o">.</span><span class="n">txt</span>
</pre></div></div></div>

<p>Файл <code>requirements.txt</code> используется для указания зависимостей для проекта Python. 
В нем перечислены пакеты и их версии, необходимые для правильной работы проекта. 
Это упрощает настройку той же среды на другом компьютере или при развертывании приложения в производственной среде.
Когда вы запустите <code>pip freeze &gt; requirements.txt</code>, он создаст новый файл с именем <code>requirements.txt</code>
в вашем текущем каталоге и запишет вывод <code>pip freeze</code> команды в этот файл, 
который будет содержать список всех пакетов и их версий, которые в 
настоящее время установлены в вашей среде Python, один пакет за строку.
Позже вы можете использовать </p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-code-button" onclick="copyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="n">pip</span> <span class="n">install</span> <span class="o">-</span><span class="n">r</span> <span class="n">requirements</span><span class="o">.</span><span class="n">txt</span>
</pre></div></div></div>

<p>для установки всех пакетов и их версий, перечисленныx в файле, 
это гарантирует, что среда такая же, как та, которая 
использовалась для создания <code>requirements.txt</code> файла.</p>
<p>Рекомендуется включить <code>requirements.txt</code> файл в репозиторий вашего проекта, 
чтобы другие разработчики или пользователи могли легко 
настроить ту же среду и запустить проект с правильными зависимостями.</p>
<p>Для создания файла с библиотеками используемыми только для нужного проекта использовать </p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-code-button" onclick="copyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="n">pip</span> <span class="n">freeze</span> <span class="o">--</span><span class="n">local</span> <span class="o">&gt;</span> <span class="n">requirements</span><span class="o">.</span><span class="n">txt</span>
</pre></div></div></div>