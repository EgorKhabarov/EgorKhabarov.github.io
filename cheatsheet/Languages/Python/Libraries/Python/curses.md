<h3>Шпаргалка по библиотеке <strong><code>curses</code></strong> в Python</h3>
<p><strong><code>curses</code></strong> — это модуль в Python для создания текстовых пользовательских интерфейсов (TUI) в терминалах
Он предоставляет функции для работы с окнами, цветами, клавишами, курсором и другой функциональностью терминалов</p>
<h3><strong>Основные функции библиотеки <code>curses</code></strong></h3>
<table>
<thead>
<tr>
<th>Функция</th>
<th>Описание</th>
<th>Пример использования</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>initscr()</code></td>
<td>Инициализирует экран, создавая объект главного окна</td>
<td><code>stdscr = curses.initscr()</code></td>
</tr>
<tr>
<td><code>endwin()</code></td>
<td>Восстанавливает работу терминала после завершения программы</td>
<td><code>curses.endwin()</code></td>
</tr>
<tr>
<td><code>noecho()</code></td>
<td>Отключает автоматический вывод вводимых символов на экран</td>
<td><code>curses.noecho()</code></td>
</tr>
<tr>
<td><code>echo()</code></td>
<td>Включает вывод вводимых символов на экран</td>
<td><code>curses.echo()</code></td>
</tr>
<tr>
<td><code>cbreak()</code></td>
<td>Включает режим <code>cbreak</code>, при котором ввод<br>передается программе без необходимости нажимать Enter</td>
<td><code>curses.cbreak()</code></td>
</tr>
<tr>
<td><code>nocbreak()</code></td>
<td>Выключает режим <code>cbreak</code></td>
<td><code>curses.nocbreak()</code></td>
</tr>
<tr>
<td><code>keypad(window, True/False)</code></td>
<td>Включает или отключает обработку специальных<br>клавиш, таких как стрелки, F-клавиши и др</td>
<td><code>stdscr.keypad(True)</code></td>
</tr>
<tr>
<td><code>curs_set(visibility)</code></td>
<td>Устанавливает видимость курсора<br>(0 — невидим, 1 — видим, 2 — видим и жирный)</td>
<td><code>curses.curs_set(0)</code></td>
</tr>
<tr>
<td><code>start_color()</code></td>
<td>Инициализирует работу с цветами</td>
<td><code>curses.start_color()</code></td>
</tr>
<tr>
<td><code>init_pair(pair_number, fg, bg)</code></td>
<td>Устанавливает пару цветов для использования<br>(например, текст/фон)</td>
<td><code>curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)</code></td>
</tr>
<tr>
<td><code>getch()</code></td>
<td>Читает один символ с клавиатуры</td>
<td><code>key = stdscr.getch()</code></td>
</tr>
<tr>
<td><code>refresh()</code></td>
<td>Обновляет экран для отображения изменений</td>
<td><code>stdscr.refresh()</code></td>
</tr>
<tr>
<td><code>clear()</code></td>
<td>Очищает экран</td>
<td><code>stdscr.clear()</code></td>
</tr>
<tr>
<td><code>newwin(nlines, ncols, begin_y, begin_x)</code></td>
<td>Создает новое окно с заданными размерами и позицией</td>
<td><code>win = curses.newwin(10, 20, 5, 5)</code></td>
</tr>
<tr>
<td><code>addstr(y, x, string)</code></td>
<td>Выводит строку на экране в указанной позиции</td>
<td><code>stdscr.addstr(5, 5, "Hello World")</code></td>
</tr>
<tr>
<td><code>border()</code></td>
<td>Рисует границу вокруг окна</td>
<td><code>win.border()</code></td>
</tr>
</tbody>
</table>
<h3><strong>Работа с цветами</strong></h3>
<p>Чтобы использовать цвета в <code>curses</code>, необходимо сначала
инициализировать цветовой режим с помощью <code>start_color()</code> и создать пары цветов</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">curses</span>

<span class="k">def</span> <span class="nf">main</span><span class="p">(</span><span class="n">stdscr</span><span class="p">):</span>
    <span class="n">curses</span><span class="o">.</span><span class="n">start_color</span><span class="p">()</span>  <span class="c1"># Инициализация цветового режима</span>
    <span class="n">curses</span><span class="o">.</span><span class="n">init_pair</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="n">curses</span><span class="o">.</span><span class="n">COLOR_RED</span><span class="p">,</span> <span class="n">curses</span><span class="o">.</span><span class="n">COLOR_BLACK</span><span class="p">)</span>  <span class="c1"># Пара цветов</span>

    <span class="n">stdscr</span><span class="o">.</span><span class="n">addstr</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="s2">&quot;Hello, World!&quot;</span><span class="p">,</span> <span class="n">curses</span><span class="o">.</span><span class="n">color_pair</span><span class="p">(</span><span class="mi">1</span><span class="p">))</span>  <span class="c1"># Использование цветовой пары</span>
    <span class="n">stdscr</span><span class="o">.</span><span class="n">refresh</span><span class="p">()</span>
    <span class="n">stdscr</span><span class="o">.</span><span class="n">getch</span><span class="p">()</span>

<span class="n">curses</span><span class="o">.</span><span class="n">wrapper</span><span class="p">(</span><span class="n">main</span><span class="p">)</span>
</pre></div></div></div>

<h3><strong>Управление окнами</strong></h3>
<p>Вы можете создавать и управлять несколькими окнами с помощью <code>newwin()</code></p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">curses</span>

<span class="k">def</span> <span class="nf">main</span><span class="p">(</span><span class="n">stdscr</span><span class="p">):</span>
    <span class="c1"># Создание нового окна</span>
    <span class="n">win</span> <span class="o">=</span> <span class="n">curses</span><span class="o">.</span><span class="n">newwin</span><span class="p">(</span><span class="mi">10</span><span class="p">,</span> <span class="mi">40</span><span class="p">,</span> <span class="mi">5</span><span class="p">,</span> <span class="mi">5</span><span class="p">)</span>  <span class="c1"># Высота 10, ширина 40, позиция (5,5)</span>
    <span class="n">win</span><span class="o">.</span><span class="n">border</span><span class="p">()</span>  <span class="c1"># Добавление границы вокруг окна</span>
    <span class="n">win</span><span class="o">.</span><span class="n">addstr</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="s2">&quot;This is a new window!&quot;</span><span class="p">)</span>
    <span class="n">win</span><span class="o">.</span><span class="n">refresh</span><span class="p">()</span>  <span class="c1"># Обновление экрана</span>

    <span class="n">stdscr</span><span class="o">.</span><span class="n">getch</span><span class="p">()</span>

<span class="n">curses</span><span class="o">.</span><span class="n">wrapper</span><span class="p">(</span><span class="n">main</span><span class="p">)</span>
</pre></div></div></div>

<h3><strong>Обработка клавиш</strong></h3>
<p><code>curses</code> поддерживает ввод с клавиатуры и специальные клавиши,
такие как стрелки, функциональные клавиши (F1, F2 и т.д.)</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">curses</span>

<span class="k">def</span> <span class="nf">main</span><span class="p">(</span><span class="n">stdscr</span><span class="p">):</span>
    <span class="n">stdscr</span><span class="o">.</span><span class="n">keypad</span><span class="p">(</span><span class="kc">True</span><span class="p">)</span>  <span class="c1"># Включение обработки специальных клавиш</span>
    <span class="n">stdscr</span><span class="o">.</span><span class="n">addstr</span><span class="p">(</span><span class="s2">&quot;Press any key (ESC to exit)...&quot;</span><span class="p">)</span>
    <span class="k">while</span> <span class="kc">True</span><span class="p">:</span>
        <span class="n">key</span> <span class="o">=</span> <span class="n">stdscr</span><span class="o">.</span><span class="n">getch</span><span class="p">()</span>
        <span class="k">if</span> <span class="n">key</span> <span class="o">==</span> <span class="mi">27</span><span class="p">:</span>  <span class="c1"># ESC</span>
            <span class="k">break</span>
        <span class="n">stdscr</span><span class="o">.</span><span class="n">addstr</span><span class="p">(</span><span class="mi">2</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="sa">f</span><span class="s2">&quot;Key pressed: </span><span class="si">{</span><span class="n">key</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">)</span>
        <span class="n">stdscr</span><span class="o">.</span><span class="n">refresh</span><span class="p">()</span>

<span class="n">curses</span><span class="o">.</span><span class="n">wrapper</span><span class="p">(</span><span class="n">main</span><span class="p">)</span>
</pre></div></div></div>

<ul>
<li><strong>Некоторые специальные клавиши</strong><ul>
<li><code>curses.KEY_UP</code>: стрелка вверх</li>
<li><code>curses.KEY_DOWN</code>: стрелка вниз</li>
<li><code>curses.KEY_LEFT</code>: стрелка влево</li>
<li><code>curses.KEY_RIGHT</code>: стрелка вправо</li>
<li><code>curses.KEY_F1</code>, <code>curses.KEY_F2</code> и т.д.: функциональные клавиши F1, F2...</li>
</ul>
</li>
</ul>
<h3><strong>Пример программы с цветами и окнами</strong></h3>
<p>Пример программы, которая создает два окна с разными цветами и выводит текст в них</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text class="unselectable">Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">curses</span>

<span class="k">def</span> <span class="nf">main</span><span class="p">(</span><span class="n">stdscr</span><span class="p">):</span>
    <span class="c1"># Инициализация цветов</span>
    <span class="n">curses</span><span class="o">.</span><span class="n">start_color</span><span class="p">()</span>
    <span class="n">curses</span><span class="o">.</span><span class="n">init_pair</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="n">curses</span><span class="o">.</span><span class="n">COLOR_RED</span><span class="p">,</span> <span class="n">curses</span><span class="o">.</span><span class="n">COLOR_BLACK</span><span class="p">)</span>
    <span class="n">curses</span><span class="o">.</span><span class="n">init_pair</span><span class="p">(</span><span class="mi">2</span><span class="p">,</span> <span class="n">curses</span><span class="o">.</span><span class="n">COLOR_GREEN</span><span class="p">,</span> <span class="n">curses</span><span class="o">.</span><span class="n">COLOR_BLACK</span><span class="p">)</span>

    <span class="c1"># Главное окно</span>
    <span class="n">stdscr</span><span class="o">.</span><span class="n">addstr</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="s2">&quot;Main window&quot;</span><span class="p">,</span> <span class="n">curses</span><span class="o">.</span><span class="n">color_pair</span><span class="p">(</span><span class="mi">1</span><span class="p">))</span>

    <span class="c1"># Создание нового окна</span>
    <span class="n">win</span> <span class="o">=</span> <span class="n">curses</span><span class="o">.</span><span class="n">newwin</span><span class="p">(</span><span class="mi">10</span><span class="p">,</span> <span class="mi">40</span><span class="p">,</span> <span class="mi">5</span><span class="p">,</span> <span class="mi">5</span><span class="p">)</span>
    <span class="n">win</span><span class="o">.</span><span class="n">border</span><span class="p">()</span>
    <span class="n">win</span><span class="o">.</span><span class="n">addstr</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="s2">&quot;Window with border&quot;</span><span class="p">,</span> <span class="n">curses</span><span class="o">.</span><span class="n">color_pair</span><span class="p">(</span><span class="mi">2</span><span class="p">))</span>

    <span class="n">stdscr</span><span class="o">.</span><span class="n">refresh</span><span class="p">()</span>
    <span class="n">win</span><span class="o">.</span><span class="n">refresh</span><span class="p">()</span>

    <span class="n">stdscr</span><span class="o">.</span><span class="n">getch</span><span class="p">()</span>

<span class="n">curses</span><span class="o">.</span><span class="n">wrapper</span><span class="p">(</span><span class="n">main</span><span class="p">)</span>
</pre></div></div></div>

<h3><strong>Некоторые полезные функции и особенности</strong></h3>
<table>
<thead>
<tr>
<th>Функция</th>
<th>Описание</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>curses.wrapper(func)</code></td>
<td>Запускает функцию с инициализацией и завершением <code>curses</code> окружения автоматически</td>
</tr>
<tr>
<td><code>curses.newpad()</code></td>
<td>Создает "пад" (большой буфер экрана) для управления большими текстами, которые не помещаются на экран</td>
</tr>
<tr>
<td><code>getmaxyx()</code></td>
<td>Возвращает максимальные размеры окна (высота и ширина)</td>
</tr>
<tr>
<td><code>curses.is_term_resized()</code></td>
<td>Проверяет, был ли изменен размер терминала</td>
</tr>
<tr>
<td><code>curses.flash()</code></td>
<td>Визуальный сигнал, мигание экрана</td>
</tr>
<tr>
<td><code>curses.beep()</code></td>
<td>Аудиосигнал</td>
</tr>
<tr>
<td><code>curses.textpad.Textbox()</code></td>
<td>Создает текстовое поле для редактирования текста</td>
</tr>
</tbody>
</table>
<h3><strong>Завершение работы с <code>curses</code></strong></h3>
<p>При завершении программы важно корректно выйти из режима <code>curses</code>,
чтобы терминал вернулся в нормальный режим
Обычно для этого вызывается <code>curses.endwin()</code>,
но использование <code>curses.wrapper()</code> автоматически обрабатывает завершение</p>
<h3><strong>Полезные ссылки</strong></h3>
<p><a href="https://docs.python.org/3/library/curses.html">Документация <code>curses</code></a></p>