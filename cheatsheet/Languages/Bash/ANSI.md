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
<td><code>\u001b[0m</code></td>
</tr>
</tbody>
</table>
<h1>8 Colors</h1>
<table>
<thead>
<tr>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Black</td>
<td><code>\u001b[30m</code></td>
</tr>
<tr>
<td>Red</td>
<td><code>\u001b[31m</code></td>
</tr>
<tr>
<td>Green</td>
<td><code>\u001b[32m</code></td>
</tr>
<tr>
<td>Yellow</td>
<td><code>\u001b[33m</code></td>
</tr>
<tr>
<td>Blue</td>
<td><code>\u001b[34m</code></td>
</tr>
<tr>
<td>Magenta</td>
<td><code>\u001b[35m</code></td>
</tr>
<tr>
<td>Cyan</td>
<td><code>\u001b[36m</code></td>
</tr>
<tr>
<td>White</td>
<td><code>\u001b[37m</code></td>
</tr>
</tbody>
</table>
<h1>16 Colors</h1>
<table>
<thead>
<tr>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Bright Black</td>
<td><code>\u001b[30;1m</code></td>
</tr>
<tr>
<td>Bright Red</td>
<td><code>\u001b[31;1m</code></td>
</tr>
<tr>
<td>Bright Green</td>
<td><code>\u001b[32;1m</code></td>
</tr>
<tr>
<td>Bright Yellow</td>
<td><code>\u001b[33;1m</code></td>
</tr>
<tr>
<td>Bright Blue</td>
<td><code>\u001b[34;1m</code></td>
</tr>
<tr>
<td>Bright Magenta</td>
<td><code>\u001b[35;1m</code></td>
</tr>
<tr>
<td>Bright Cyan</td>
<td><code>\u001b[36;1m</code></td>
</tr>
<tr>
<td>Bright White</td>
<td><code>\u001b[37;1m</code></td>
</tr>
</tbody>
</table>
<h1>256 Colors</h1>
<p><code>\u001b[38;5;${ID}m</code>
<a href="https://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html#256-colors">https://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html#256-colors</a></p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">sys</span>
<span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">16</span><span class="p">):</span>
   <span class="k">for</span> <span class="n">j</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">16</span><span class="p">):</span>
       <span class="n">code</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">i</span> <span class="o">*</span> <span class="mi">16</span> <span class="o">+</span> <span class="n">j</span><span class="p">)</span>
       <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;</span><span class="se">\u001b</span><span class="s2">[38;5;&quot;</span> <span class="o">+</span> <span class="n">code</span> <span class="o">+</span> <span class="s2">&quot;m &quot;</span> <span class="o">+</span> <span class="n">code</span><span class="o">.</span><span class="n">ljust</span><span class="p">(</span><span class="mi">4</span><span class="p">),</span> <span class="n">end</span><span class="o">=</span><span class="s2">&quot;&quot;</span><span class="p">)</span>
   <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;</span><span class="se">\u001b</span><span class="s2">[0m&quot;</span><span class="p">)]</span>
</pre></div></div></div>

<h1>Background Colors</h1>
<table>
<thead>
<tr>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Background Black</td>
<td><code>\u001b[40m</code></td>
</tr>
<tr>
<td>Background Red</td>
<td><code>\u001b[41m</code></td>
</tr>
<tr>
<td>Background Green</td>
<td><code>\u001b[42m</code></td>
</tr>
<tr>
<td>Background Yellow</td>
<td><code>\u001b[43m</code></td>
</tr>
<tr>
<td>Background Blue</td>
<td><code>\u001b[44m</code></td>
</tr>
<tr>
<td>Background Magenta</td>
<td><code>\u001b[45m</code></td>
</tr>
<tr>
<td>Background Cyan</td>
<td><code>\u001b[46m</code></td>
</tr>
<tr>
<td>Background White</td>
<td><code>\u001b[47m</code></td>
</tr>
<tr>
<td></td>
<td></td>
</tr>
<tr>
<td>Background Bright Black</td>
<td><code>\u001b[40;1m</code></td>
</tr>
<tr>
<td>Background Bright Red</td>
<td><code>\u001b[41;1m</code></td>
</tr>
<tr>
<td>Background Bright Green</td>
<td><code>\u001b[42;1m</code></td>
</tr>
<tr>
<td>Background Bright Yellow</td>
<td><code>\u001b[43;1m</code></td>
</tr>
<tr>
<td>Background Bright Blue</td>
<td><code>\u001b[44;1m</code></td>
</tr>
<tr>
<td>Background Bright Magenta</td>
<td><code>\u001b[45;1m</code></td>
</tr>
<tr>
<td>Background Bright Cyan</td>
<td><code>\u001b[46;1m</code></td>
</tr>
<tr>
<td>Background Bright White</td>
<td><code>\u001b[47;1m</code></td>
</tr>
</tbody>
</table>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">sys</span>
<span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">16</span><span class="p">):</span>
    <span class="k">for</span> <span class="n">j</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">16</span><span class="p">):</span>
        <span class="n">code</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">i</span> <span class="o">*</span> <span class="mi">16</span> <span class="o">+</span> <span class="n">j</span><span class="p">)</span>
        <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;</span><span class="se">\u001b</span><span class="s2">[48;5;&quot;</span> <span class="o">+</span> <span class="n">code</span> <span class="o">+</span> <span class="s2">&quot;m &quot;</span> <span class="o">+</span> <span class="n">code</span><span class="o">.</span><span class="n">ljust</span><span class="p">(</span><span class="mi">4</span><span class="p">),</span> <span class="n">end</span><span class="o">=</span><span class="s2">&quot;&quot;</span><span class="p">)</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;</span><span class="se">\u001b</span><span class="s2">[0m&quot;</span><span class="p">)</span>
</pre></div></div></div>

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
<td><code>\u001b[1m</code></td>
</tr>
<tr>
<td>Underline</td>
<td><code>\u001b[4m</code></td>
</tr>
<tr>
<td>Reversed</td>
<td><code>\u001b[7m</code></td>
</tr>
<tr>
<td>Моргающий</td>
<td><code>\u001b[5m</code></td>
</tr>
</tbody>
</table>
<h1>Cursor Navigation</h1>
<table>
<thead>
<tr>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Up</td>
<td><code>\u001b[{n}A</code></td>
</tr>
<tr>
<td>Down</td>
<td><code>\u001b[{n}B</code></td>
</tr>
<tr>
<td>Right</td>
<td><code>\u001b[{n}C</code></td>
</tr>
<tr>
<td>Left</td>
<td><code>\u001b[{n}D</code></td>
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
<td><code>\u001b[{n}J</code></td>
<td>n=<code>0</code> clears from cursor until end of screen,<br>n=<code>1</code> clears from cursor to beginning of screen<br>n=<code>2</code> clears entire screen</td>
</tr>
<tr>
<td>Clear Line</td>
<td><code>\u001b[{n}K</code></td>
<td>n=<code>0</code> clears from cursor to end of line<br>n=<code>1</code> clears from cursor to start of line<br>n=<code>2</code> clears entire line</td>
</tr>
</tbody>
</table>
<p><code>Alt-f</code> - Переместить одно слово вправо
<code>Alt-b</code> - Переместить одно слово влево
<code>Alt-Backspace</code> - Удалить одно слово слева</p>
<table>
<thead>
<tr>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>Next Line</td>
<td>Перемещает курсор к началу линий линии вниз <code>\u001b[{n}E n</code></td>
</tr>
<tr>
<td>Prev Line</td>
<td>Перемещает курсор к началу линий линии вниз <code>\u001b[{n}F n</code></td>
</tr>
<tr>
<td>Set Column</td>
<td>Перемещение курсора к столбцу \u001b[{n}G n</td>
</tr>
<tr>
<td>Set Position</td>
<td>Перемещает курсор в столбец строки \u001b[{n};{m}H n m</td>
</tr>
<tr>
<td>Сохранить позицию</td>
<td>сохраняет текущее положение курсора \u001b[{s}</td>
</tr>
<tr>
<td>Сохранить позицию</td>
<td>восстанавливает курсор до последнего сохраненного положения \u001b[{u}</td>
</tr>
</tbody>
</table>
<p><code>\033]0;Новое название консоли\007</code> - изменить название консоли</p>
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