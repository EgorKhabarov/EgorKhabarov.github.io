<p>Библиотека "readline" используется в Python для обеспечения функциональности чтения и редактирования строк в интерактивной командной оболочке.</p>
<p>Методы модуля "readline" и его подмодулей:</p>
<p>readline(): Читает строку из входного потока.
add_history(string): Добавляет строку в историю командной оболочки.
clear_history(): Очищает историю командной оболочки.
get_history_length(): Возвращает количество записей в истории командной оболочки.
set_history_length(length): Устанавливает максимальное количество записей в истории командной оболочки.
get_current_history_length(): Возвращает текущую длину истории командной оболочки.
remove_history_item(pos): Удаляет запись из истории командной оболочки по указанной позиции.
replace_history_item(pos, string): Заменяет запись в истории командной оболочки по указанной позиции новой строкой.</p>
<p>Наиболее часто используемые методы:</p>
<p>readline(): Читает строку из входного потока.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" onclick="copyCode(this)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">readline</span>

<span class="n">input_string</span> <span class="o">=</span> <span class="n">readline</span><span class="o">.</span><span class="n">readline</span><span class="p">()</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Input:&quot;</span><span class="p">,</span> <span class="n">input_string</span><span class="p">)</span>
</pre></div></div></div>

<p>add_history(string): Добавляет строку в историю командной оболочки.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" onclick="copyCode(this)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">readline</span>

<span class="n">readline</span><span class="o">.</span><span class="n">add_history</span><span class="p">(</span><span class="s2">&quot;command 1&quot;</span><span class="p">)</span>
<span class="n">readline</span><span class="o">.</span><span class="n">add_history</span><span class="p">(</span><span class="s2">&quot;command 2&quot;</span><span class="p">)</span>
</pre></div></div></div>

<p>clear_history(): Очищает историю командной оболочки.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-button" onclick="copyCode(this)"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg><text>Copy code</text></button></div><div class="code"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">readline</span>

<span class="n">readline</span><span class="o">.</span><span class="n">clear_history</span><span class="p">()</span>
</pre></div></div></div>