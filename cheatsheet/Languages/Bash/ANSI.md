<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="c1"># Escape sequence</span>
<span class="n">ESC</span> <span class="o">=</span> <span class="s2">&quot;</span><span class="se">\u001b</span><span class="s2">&quot;</span> <span class="ow">or</span> <span class="s2">&quot;</span><span class="se">\x1b</span><span class="s2">&quot;</span>
</pre></div></div></div>

<table>
<thead>
<tr>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Reset</td>
<td>ESC<code>[0m</code></td>
</tr>
</tbody>
</table>
<h1>Decorations</h1>
<table>
<thead>
<tr>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Bold</td>
<td>ESC<code>[1m</code></td>
</tr>
<tr>
<td>Faint (Dim)</td>
<td>ESC<code>[2m</code></td>
</tr>
<tr>
<td>Italic</td>
<td>ESC<code>[3m</code></td>
</tr>
<tr>
<td>Underline</td>
<td>ESC<code>[4m</code></td>
</tr>
<tr>
<td>Blinking (slow)</td>
<td>ESC<code>[5m</code></td>
</tr>
<tr>
<td>Blinking (rapid)</td>
<td>ESC<code>[6m</code></td>
</tr>
<tr>
<td>Inverse</td>
<td>ESC<code>[7m</code></td>
</tr>
<tr>
<td>Hidden</td>
<td>ESC<code>[8m</code></td>
</tr>
<tr>
<td>Strikethrough</td>
<td>ESC<code>[9m</code></td>
</tr>
<tr>
<td>Doubly underlined mode</td>
<td>ESC<code>[21m</code></td>
</tr>
</tbody>
</table>
<h1>Colors</h1>
<table>
<thead>
<tr>
<th>8 Colors</th>
<th></th>
<th>16 Colors</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Black</td>
<td>ESC<code>[30m</code></td>
<td>Bright Black</td>
<td>ESC<code>[30;1m</code></td>
</tr>
<tr>
<td>Red</td>
<td>ESC<code>[31m</code></td>
<td>Bright Red</td>
<td>ESC<code>[31;1m</code></td>
</tr>
<tr>
<td>Green</td>
<td>ESC<code>[32m</code></td>
<td>Bright Green</td>
<td>ESC<code>[32;1m</code></td>
</tr>
<tr>
<td>Yellow</td>
<td>ESC<code>[33m</code></td>
<td>Bright Yellow</td>
<td>ESC<code>[33;1m</code></td>
</tr>
<tr>
<td>Blue</td>
<td>ESC<code>[34m</code></td>
<td>Bright Blue</td>
<td>ESC<code>[34;1m</code></td>
</tr>
<tr>
<td>Magenta</td>
<td>ESC<code>[35m</code></td>
<td>Bright Magenta</td>
<td>ESC<code>[35;1m</code></td>
</tr>
<tr>
<td>Cyan</td>
<td>ESC<code>[36m</code></td>
<td>Bright Cyan</td>
<td>ESC<code>[36;1m</code></td>
</tr>
<tr>
<td>White</td>
<td>ESC<code>[37m</code></td>
<td>Bright White</td>
<td>ESC<code>[37;1m</code></td>
</tr>
</tbody>
</table>
<h3>256 Colors</h3>
<p><code>\u001b[38;5;{}m</code>
<a href="https://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html#256-colors">https://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html#256-colors</a></p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">16</span><span class="p">):</span>
    <span class="k">for</span> <span class="n">j</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">16</span><span class="p">):</span>
        <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;</span><span class="se">\u001b</span><span class="s2">[38;5;</span><span class="si">{</span><span class="n">i</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="mi">16</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">j</span><span class="si">}</span><span class="s2">m </span><span class="si">{</span><span class="n">i</span><span class="w"> </span><span class="o">*</span><span class="w"> </span><span class="mi">16</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">j</span><span class="si">:</span><span class="s2">&lt;4</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">,</span> <span class="n">end</span><span class="o">=</span><span class="s2">&quot;&quot;</span><span class="p">,</span> <span class="n">flush</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;</span><span class="se">\u001b</span><span class="s2">[0m&quot;</span><span class="p">)</span>
</pre></div></div></div>

<h1>Background Colors</h1>
<table>
<thead>
<tr>
<th></th>
<th></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Background Black</td>
<td>ESC<code>[40m</code></td>
<td>Background Bright Black</td>
<td>ESC<code>[40;1m</code></td>
</tr>
<tr>
<td>Background Red</td>
<td>ESC<code>[41m</code></td>
<td>Background Bright Red</td>
<td>ESC<code>[41;1m</code></td>
</tr>
<tr>
<td>Background Green</td>
<td>ESC<code>[42m</code></td>
<td>Background Bright Green</td>
<td>ESC<code>[42;1m</code></td>
</tr>
<tr>
<td>Background Yellow</td>
<td>ESC<code>[43m</code></td>
<td>Background Bright Yellow</td>
<td>ESC<code>[43;1m</code></td>
</tr>
<tr>
<td>Background Blue</td>
<td>ESC<code>[44m</code></td>
<td>Background Bright Blue</td>
<td>ESC<code>[44;1m</code></td>
</tr>
<tr>
<td>Background Magenta</td>
<td>ESC<code>[45m</code></td>
<td>Background Bright Magenta</td>
<td>ESC<code>[45;1m</code></td>
</tr>
<tr>
<td>Background Cyan</td>
<td>ESC<code>[46m</code></td>
<td>Background Bright Cyan</td>
<td>ESC<code>[46;1m</code></td>
</tr>
<tr>
<td>Background White</td>
<td>ESC<code>[47m</code></td>
<td>Background Bright White</td>
<td>ESC<code>[47;1m</code></td>
</tr>
</tbody>
</table>
<h3>256 Background Colors</h3>
<p><code>\u001b[48;5;{}m</code></p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">sys</span>
<span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">16</span><span class="p">):</span>
    <span class="k">for</span> <span class="n">j</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">16</span><span class="p">):</span>
        <span class="n">code</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">i</span> <span class="o">*</span> <span class="mi">16</span> <span class="o">+</span> <span class="n">j</span><span class="p">)</span>
        <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;</span><span class="se">\u001b</span><span class="s2">[48;5;&quot;</span> <span class="o">+</span> <span class="n">code</span> <span class="o">+</span> <span class="s2">&quot;m &quot;</span> <span class="o">+</span> <span class="n">code</span><span class="o">.</span><span class="n">ljust</span><span class="p">(</span><span class="mi">4</span><span class="p">),</span> <span class="n">end</span><span class="o">=</span><span class="s2">&quot;&quot;</span><span class="p">)</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;</span><span class="se">\u001b</span><span class="s2">[0m&quot;</span><span class="p">)</span>
</pre></div></div></div>

<h1>RGB Colors</h1>
<p>ESC<code>[38;2;{r};{g};{b}m</code></p>
<h1>RGB Background Colors</h1>
<p>ESC<code>[48;2;{r};{g};{b}m</code></p>
<h1>Cursor</h1>
<table>
<thead>
<tr>
<th></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Up</td>
<td>ESC<code>[{n}A</code></td>
<td></td>
</tr>
<tr>
<td>Down</td>
<td>ESC<code>[{n}B</code></td>
<td></td>
</tr>
<tr>
<td>Right</td>
<td>ESC<code>[{n}C</code></td>
<td></td>
</tr>
<tr>
<td>Left</td>
<td>ESC<code>[{n}D</code></td>
<td></td>
</tr>
<tr>
<td>Next Line</td>
<td>ESC<code>[{n}E</code></td>
<td>Перемещает курсор к началу линий линии вниз</td>
</tr>
<tr>
<td>Prev Line</td>
<td>ESC<code>[{n}F</code></td>
<td>Перемещает курсор к началу линий линии вниз</td>
</tr>
<tr>
<td>Set Position</td>
<td>ESC<code>[{n};{m}H</code><br>ESC<code>[{n};{m}f</code></td>
<td>Перемещает курсор в столбец строки</td>
</tr>
<tr>
<td>Set Column</td>
<td>ESC<code>[{n}G</code></td>
<td>Перемещает курсор в указанный столбец в текущей строке</td>
</tr>
<tr>
<td>Save Position</td>
<td>ESC<code>[s</code></td>
<td>Сохранить текущую позицию курсора</td>
</tr>
<tr>
<td>Restore Position</td>
<td>ESC<code>[u</code></td>
<td>Восстановить сохраненную позицию курсора</td>
</tr>
<tr>
<td>Hide Cursor</td>
<td>ESC<code>[?25l</code></td>
<td></td>
</tr>
<tr>
<td>Show Cursor</td>
<td>ESC<code>[?25h</code></td>
<td></td>
</tr>
<tr>
<td>Shift + Up</td>
<td>ESC<code>[{n};2A</code></td>
<td></td>
</tr>
<tr>
<td>Shift + Down</td>
<td>ESC<code>[{n};2B</code></td>
<td></td>
</tr>
<tr>
<td>Shift + Right</td>
<td>ESC<code>[{n};2C</code></td>
<td></td>
</tr>
<tr>
<td>Shift + Left</td>
<td>ESC<code>[{n};2D</code></td>
<td></td>
</tr>
<tr>
<td>Ctrl + Shift + Up</td>
<td>ESC<code>[{n};6A</code></td>
<td></td>
</tr>
<tr>
<td>Ctrl + Shift + Down</td>
<td>ESC<code>[{n};6B</code></td>
<td></td>
</tr>
<tr>
<td>Ctrl + Shift + Right</td>
<td>ESC<code>[{n};6C</code></td>
<td></td>
</tr>
<tr>
<td>Ctrl + Shift + Left</td>
<td>ESC<code>[{n};6D</code></td>
<td></td>
</tr>
</tbody>
</table>
<h1>Deletion</h1>
<table>
<thead>
<tr>
<th></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Clear Screen</td>
<td>ESC<code>[{n}J</code></td>
<td>n=<code>0</code> clears from cursor until end of screen,<br>n=<code>1</code> clears from cursor to beginning of screen<br>n=<code>2</code> clears entire screen</td>
</tr>
<tr>
<td>Clear Line</td>
<td>ESC<code>[{n}K</code></td>
<td>n=<code>0</code> clears from cursor to end of line<br>n=<code>1</code> clears from cursor to start of line<br>n=<code>2</code> clears entire line</td>
</tr>
</tbody>
</table>
<ul>
<li>ESC<code>[?1049h</code> Включить альтернативный экранный буфер.
Это часто используется в текстовых редакторах, чтобы предоставить пользователю чистый экран для работы.</li>
<li>ESC<code>[?1049l</code> Отключить альтернативный экранный буфер и вернуть содержимое основного экрана.</li>
<li>ESC<code>[?1h</code> Включить режим "прямой печати". Некоторые терминалы могут обрабатывать это по-разному.</li>
<li>ESC<code>[?1l</code> Отключить режим "прямой печати".</li>
<li>ESC<code>[1;32;40m</code> устанавливает жирный зеленый текст на черном фоне.</li>
<li>ESC<code>[3;5;7m</code> Вы можете комбинировать несколько атрибутов, чтобы,
например, сделать текст жирным, с курсивом и инверсным цветом.</li>
<li>ESC<code>[0;31;47m</code> Это сброс всех атрибутов и установка красного текста на белом фоне.</li>
<li>ESC<code>[X</code> Удаление символа в позиции курсора (может работать по-разному в зависимости от терминала).</li>
<li>ESC<code>[P</code> Удаление символа, на который указывает курсор.</li>
<li><code>\007</code> Это код звукового сигнала (bell). При его использовании терминал издает звук.</li>
<li><code>\033[39m</code> Этот код сбрасывает цвет текста к цвету по умолчанию.
Если цвет текста был изменён, он вернётся к стандартному цвету терминала.</li>
<li>ESC<code>]0;Title\007</code> Устанавливает заголовок окна терминала.</li>
<li>ESC<code>]8;;&lt;URL&gt;ESC\</code> Создаёт кликабельную ссылку</li>
</ul>
<div class="code_element"><div class="lang_line"><text>bash</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-bash"><div class="highlight"><pre><span></span><span class="nb">echo</span><span class="w"> </span>-e<span class="w"> </span><span class="s2">&quot;\033]8;;http://example.com\033\\Click Here\033]8;;\033\\&quot;</span>
</pre></div></div></div>

<div class="code_element"><div class="lang_line"><text>bash</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-bash"><div class="highlight"><pre><span></span><span class="nb">echo</span><span class="w"> </span>-e<span class="w"> </span><span class="s2">&quot;\033]0;My Terminal Window\007&quot;</span>
</pre></div></div></div>

<p><code>Alt-f</code> - Переместить одно слово вправо
<code>Alt-b</code> - Переместить одно слово влево
<code>Alt-Backspace</code> - Удалить одно слово слева</p>
<table>
  <thead>
    <tr>
      <th style="background: inherit; border: none;"></th>
      <th>Emacs keys</th>
      <th>Action</th>
      <th>Scope</th>
      <th>Direction/Place</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="7">Moving around</th>
      <td><code>Ctrl-b</code></td>
      <td>Move the cursor</td>
      <td>one character</td>
      <td>⇦ to the left</td>
    </tr>
    <tr>
      <td><code>Ctrl-f</code></td>
      <td>Move the cursor</td>
      <td>one character</td>
      <td>⇨ to the right</td>
    </tr>
    <tr>
      <td><code>Alt-b</code></td>
      <td>Move the cursor</td>
      <td>one word</td>
      <td>⇦ to the left</td>
    </tr>
    <tr>
      <td><code>Alt-f</code></td>
      <td>Move the cursor</td>
      <td>one word</td>
      <td>⇨ to the right</td>
    </tr>
    <tr>
      <td><code>Ctrl-a</code></td>
      <td>Move the cursor</td>
      <td></td>
      <td>⇤ to the start of the line</td>
    </tr>
    <tr>
      <td><code>Ctrl-e</code></td>
      <td>Move the cursor</td>
      <td></td>
      <td>⇥ to the end of the line</td>
    </tr>
    <tr>
      <td><code>Ctrl-x-x</code></td>
      <td>Move the cursor</td>
      <td></td>
      <td>⇤⇥ to the start, and to the end again<br></td>
    </tr>
  </tbody>
  <tbody>
    <tr>
      <th rowspan="8">Cut, copy<br>and paste</th>
      <td>Backspace</td>
      <td>Delete</td>
      <td>the character</td>
      <td>⇦ to the left of the cursor</td>
    </tr>
    <tr>
      <td>DEL<br><code>Ctrl-d</code></td>
      <td>Delete</td>
      <td>the character</td>
      <td>underneath the cursor</td>
    </tr>
    <tr>
      <td><code>Ctrl-u</code></td>
      <td>Delete</td>
      <td>everything</td>
      <td>⇤ from the cursor back to the line start</td>
    </tr>
    <tr>
      <td><code>Ctrl-k</code></td>
      <td>Delete</td>
      <td>everything</td>
      <td>⇥ from the cursor to the end of the line</td>
    </tr>
    <tr>
      <td><code>Alt-d</code></td>
      <td>Delete</td>
      <td>word</td>
      <td>⇨ untill before the next word boundary</td>
    </tr>
    <tr>
      <td><code>Ctrl-w</code></td>
      <td>Delete</td>
      <td>word</td>
      <td>⇦ untill after the previous word boundary</td>
    </tr>
    <tr>
      <td><code>Ctrl-y</code></td>
      <td>Yank/Paste</td>
      <td>prev. killed text</td>
      <td>at the cursor position</td>
    </tr>
    <tr>
      <td><code>Alt-y</code></td>
      <td>Yank/Paste</td>
      <td>prev. prev. killed text</td>
      <td>at the cursor position</td>
    </tr>
  </tbody>
  <tbody>
    <tr>
      <th rowspan="9">History</th>
      <td><code>Ctrl-p</code></td>
      <td>Move in history</td>
      <td>one line</td>
      <td>⇧ before this line</td>
    </tr>
    <tr>
      <td><code>Ctrl-n</code></td>
      <td>Move in history</td>
      <td>one line</td>
      <td>⇩ after this line</td>
    </tr>
    <tr>
      <td><code>Alt-&gt;</code></td>
      <td>Move in history</td>
      <td>all the lines</td>
      <td>⇩ to the line currently being entered</td>
    </tr>

    <tr>
      <td><code>Ctrl-r</code></td>
      <td colspan="2">Incrementally search the line history</td>
      <td>⇧ backwardly</td>
    </tr>

    <tr>
      <td><code>Ctrl-s</code></td>
      <td colspan="2">Incrementally search the line history</td>
      <td>⇩ forwardly</td>
    </tr>

    <tr>
      <td><code>Ctrl-J</code></td>
      <td colspan="3">End an incremental search</td>
    </tr>

    <tr>
      <td><code>Ctrl-G</code></td>
      <td colspan="3">Abort an incremental search and restore the original line</td>
    </tr>

    <tr>
      <td><code>Alt-Ctrl-y</code></td>
      <td>Yank/Paste</td>
      <td>arg. 1 of prev. cmnd</td>
      <td>at the cursor position</td>
    </tr>

    <tr>
      <td><code>Alt-.</code><br><code>Alt-_</code></td>
      <td>Yank/Paste</td>
      <td>last arg of prev. cmnd</td>
      <td>at the cursor position</td>
    </tr>
  </tbody>
  <tbody>
    <tr>
      <th rowspan="4">Undo</th>
      <td><code>Ctrl-_</code><br><code>Ctrl-x</code><br><code>Ctrl-u</code></td>
      <td colspan="3">Undo the last editing command; you can undo all the way back to an empty line</td>
    </tr>
    <tr>
      <td><code>Alt-r</code></td>
      <td colspan="3">Undo all changes made to this line</td>
    </tr>
    <tr>
      <td><code>Ctrl-l</code></td>
      <td colspan="3">Clear the screen, reprinting the current line at the top</td>
    </tr>
    <tr>
      <td><code>Ctrl-l</code></td>
      <td colspan="3">Clear the screen, reprinting the current line at the top</td>
    </tr>
  </tbody>
  <tbody>
    <tr>
      <th rowspan="4">Completion</th>
      <td>TAB</td>
      <td colspan="3">Auto-complete a name</td>
    </tr>
    <tr>
      <td><code>Alt-/</code></td>
      <td colspan="3">Auto-complete a name (without smart completion)</td>
    </tr>
    <tr>
      <td><code>Alt-?</code></td>
      <td colspan="3">List the possible completions of the preceeding text</td>
    </tr>
    <tr>
      <td><code>Alt-*</code></td>
      <td colspan="3">Insert all possible completions of the preceeding text</td>
    </tr>
  </tbody>
  <tbody>
    <tr>
      <th rowspan="2">Transpose</th>
      <td><code>Ctrl-t</code></td>
      <td>Transpose/drag</td>
      <td>char. before the cursor</td>
      <td>↷ over the character at the cursor</td>
    </tr>
    <tr>
      <td><code>Alt-t</code></td>
      <td>Transpose/drag</td>
      <td>word before the cursor</td>
      <td>↷ over the word at/after the cursor</td>
    </tr>
  </tbody>
</table>