<p>Библиотека <code>signal</code> позволяет работать с сигналами в Unix-подобных операционных системах.
Сигналы — это уведомления, которые операционная система посылает процессам для того,
чтобы сообщить о каких-либо событиях (например, о завершении работы, прерывании и т.д.).</p>
<ul>
<li><strong>Сигнал</strong> — сообщение, посылаемое операционной системой процессу для уведомления о каком-либо событии.</li>
<li><strong>Обработчик сигнала</strong> — функция, которая вызывается, когда процесс получает сигнал.</li>
</ul>
<table>
<thead>
<tr>
<th>Сигнал</th>
<th>Описание</th>
<th>Действие по умолчанию</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>signal.SIGINT</code></td>
<td>Прерывание (обычно <code>CTRL+C</code>)</td>
<td>Завершение процесса</td>
</tr>
<tr>
<td><code>signal.SIGTERM</code></td>
<td>Завершение процесса</td>
<td>Завершение процесса</td>
</tr>
<tr>
<td><code>signal.SIGKILL</code></td>
<td>Принудительное завершение процесса</td>
<td>Завершение процесса</td>
</tr>
<tr>
<td><code>signal.SIGALRM</code></td>
<td>Таймер истек</td>
<td>Завершение процесса</td>
</tr>
<tr>
<td><code>signal.SIGHUP</code></td>
<td>Обрыв связи</td>
<td>Завершение процесса</td>
</tr>
<tr>
<td><code>signal.SIGUSR1</code></td>
<td>Пользовательский сигнал 1</td>
<td>Завершение процесса</td>
</tr>
<tr>
<td><code>signal.SIGUSR2</code></td>
<td>Пользовательский сигнал 2</td>
<td>Завершение процесса</td>
</tr>
</tbody>
</table>
<blockquote>
<p><strong>Примечание:</strong> Сигнал <code>SIGKILL</code> нельзя перехватить или игнорировать.</p>
</blockquote>
<h1>Установка обработчика сигнала</h1>
<p>Для установки обработчика используется функция <code>signal.signal()</code>:</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="k">def</span> <span class="nf">handler</span><span class="p">(</span><span class="n">signum</span><span class="p">,</span> <span class="n">frame</span><span class="p">):</span>
    <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;Сигнал </span><span class="si">{</span><span class="n">signum</span><span class="si">}</span><span class="s2"> получен&quot;</span><span class="p">)</span>

<span class="n">signal</span><span class="o">.</span><span class="n">signal</span><span class="p">(</span><span class="n">signal</span><span class="o">.</span><span class="n">SIGINT</span><span class="p">,</span> <span class="n">handler</span><span class="p">)</span>
</pre></div></div></div>

<ul>
<li><code>signum</code>: номер сигнала.</li>
<li><code>frame</code>: текущее состояние стека (можно игнорировать).</li>
</ul>
<h1>Игнорирование сигналов</h1>
<p>Сигнал можно игнорировать, установив обработчик в <code>signal.SIG_IGN</code>:</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="n">signal</span><span class="o">.</span><span class="n">signal</span><span class="p">(</span><span class="n">signal</span><span class="o">.</span><span class="n">SIGINT</span><span class="p">,</span> <span class="n">signal</span><span class="o">.</span><span class="n">SIG_IGN</span><span class="p">)</span>
</pre></div></div></div>

<h1>Восстановление стандартного обработчика</h1>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="n">signal</span><span class="o">.</span><span class="n">signal</span><span class="p">(</span><span class="n">signal</span><span class="o">.</span><span class="n">SIGINT</span><span class="p">,</span> <span class="n">signal</span><span class="o">.</span><span class="n">SIG_DFL</span><span class="p">)</span>
</pre></div></div></div>

<h1>Отправка сигналов процессу</h1>
<p>Для отправки сигнала процессу используется функция <a target="_self" href="?Languages/Python/Libraries/System/os/" class="wikilink"></a><code>.kill()</code>:</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">os</span>
<span class="n">os</span><span class="o">.</span><span class="n">kill</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">getpid</span><span class="p">(),</span> <span class="n">signal</span><span class="o">.</span><span class="n">SIGTERM</span><span class="p">)</span>
</pre></div></div></div>

<ul>
<li><code>os.getpid()</code> возвращает ID текущего процесса.</li>
<li><code>signal.SIGTERM</code> — сигнал завершения.</li>
</ul>
<h1>Работа с таймерами</h1>
<p>Функция <code>signal.alarm()</code> устанавливает таймер, который отправляет сигнал <code>SIGALRM</code> после указанного времени:</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="n">signal</span><span class="o">.</span><span class="n">alarm</span><span class="p">(</span><span class="mi">5</span><span class="p">)</span>  <span class="c1"># Через 5 секунд процесс получит сигнал SIGALRM</span>
</pre></div></div></div>

<ul>
<li><code>signal.alarm(0)</code> отменяет таймер.</li>
</ul>
<h1>Ожидание сигнала</h1>
<p>Функция <code>signal.pause()</code> блокирует выполнение программы до получения сигнала:</p>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="n">signal</span><span class="o">.</span><span class="n">pause</span><span class="p">()</span>  <span class="c1"># Ожидание сигнала</span>
</pre></div></div></div>

<h2>Пример использования</h2>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">signal</span>
<span class="kn">import</span> <span class="nn">time</span>

<span class="c1"># Обработчик сигнала</span>
<span class="k">def</span> <span class="nf">handler</span><span class="p">(</span><span class="n">signum</span><span class="p">,</span> <span class="n">frame</span><span class="p">):</span>
    <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;Сигнал </span><span class="si">{</span><span class="n">signum</span><span class="si">}</span><span class="s2"> получен. Прерывание программы.&quot;</span><span class="p">)</span>

<span class="c1"># Устанавливаем обработчик для SIGINT</span>
<span class="n">signal</span><span class="o">.</span><span class="n">signal</span><span class="p">(</span><span class="n">signal</span><span class="o">.</span><span class="n">SIGINT</span><span class="p">,</span> <span class="n">handler</span><span class="p">)</span>

<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Программа работает. Нажмите Ctrl+C для прерывания.&quot;</span><span class="p">)</span>

<span class="k">try</span><span class="p">:</span>
    <span class="k">while</span> <span class="kc">True</span><span class="p">:</span>
        <span class="n">time</span><span class="o">.</span><span class="n">sleep</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span>
<span class="k">except</span> <span class="ne">KeyboardInterrupt</span><span class="p">:</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Программа завершена.&quot;</span><span class="p">)</span>
</pre></div></div></div>

<p>Этот пример перехватывает сигнал <code>SIGINT</code> (<code>Ctrl+C</code>) и выполняет пользовательский обработчик,
который выводит сообщение о получении сигнала.</p>
<h1>Часто используемые функции</h1>
<table>
<thead>
<tr>
<th>Функция</th>
<th>Описание</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>signal.signal(signum, handler)</code></td>
<td>Устанавливает обработчик для сигнала</td>
</tr>
<tr>
<td><code>signal.getsignal(signum)</code></td>
<td>Возвращает текущий обработчик сигнала</td>
</tr>
<tr>
<td><code>signal.pause()</code></td>
<td>Останавливает выполнение до получения сигнала</td>
</tr>
<tr>
<td><code>signal.alarm(seconds)</code></td>
<td>Устанавливает таймер для отправки сигнала <code>SIGALRM</code> через заданное время</td>
</tr>
<tr>
<td><code>signal.setitimer()</code></td>
<td>Устанавливает высокоточный таймер и отправляет сигнал</td>
</tr>
<tr>
<td><code>signal.siginterrupt()</code></td>
<td>Устанавливает, должен ли системный вызов быть прерван сигналом</td>
</tr>
</tbody>
</table>
<h2>Пример работы с таймером</h2>
<div class="code_element"><div class="lang_line"><text>python</text><button class="copy_code_button" onclick="CopyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><text>Copy code</text></button></div><div class="code language-python"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">signal</span>

<span class="k">def</span> <span class="nf">timeout_handler</span><span class="p">(</span><span class="n">signum</span><span class="p">,</span> <span class="n">frame</span><span class="p">):</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Таймер истек!&quot;</span><span class="p">)</span>

<span class="c1"># Устанавливаем обработчик для SIGALRM</span>
<span class="n">signal</span><span class="o">.</span><span class="n">signal</span><span class="p">(</span><span class="n">signal</span><span class="o">.</span><span class="n">SIGALRM</span><span class="p">,</span> <span class="n">timeout_handler</span><span class="p">)</span>

<span class="c1"># Устанавливаем таймер на 5 секунд</span>
<span class="n">signal</span><span class="o">.</span><span class="n">alarm</span><span class="p">(</span><span class="mi">5</span><span class="p">)</span>

<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Ожидание сигнала...&quot;</span><span class="p">)</span>

<span class="c1"># Ожидание сигнала</span>
<span class="n">signal</span><span class="o">.</span><span class="n">pause</span><span class="p">()</span>
</pre></div></div></div>

<p>Этот пример устанавливает таймер на 5 секунд и ждет его истечения.
Когда таймер истекает, вызывается обработчик <code>timeout_handler</code>.</p>
<h2>Полезные замечания</h2>
<ol>
<li><strong>Обработчики сигналов</strong>: Старайтесь минимизировать выполнение кода в обработчиках сигналов,
так как они могут быть вызваны в любой момент, что может привести к непредсказуемому поведению.</li>
<li><strong>Портируемость</strong>: Библиотека <code>signal</code> доступна только в Unix-подобных системах (Linux, macOS).
На Windows поддерживаются лишь некоторые функции, такие как <code>signal.SIGINT</code>.</li>
<li><strong>Сигналы и потоки</strong>: Сигналы обрабатываются в главном потоке. Если ваш процесс использует несколько потоков,
убедитесь, что обработка сигналов не нарушает работу приложения.</li>
</ol>