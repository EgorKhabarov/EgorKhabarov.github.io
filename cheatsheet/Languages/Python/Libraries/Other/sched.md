<p>Библиотека "sched" в Python используется для планирования и управления задачами в программе.
Она позволяет создавать расписания выполнения задач и контролировать их выполнение в определенные моменты времени.</p>
<p>Методы модуля "sched" и его подмодулей:
sched.timefunc: Устанавливает функцию, которая будет использоваться для получения времени.
sched.delayfunc: Устанавливает функцию, вызываемую перед каждым циклом планировщика.
sched.enter(delay, priority, action, argument): Планирует выполнение задачи с заданным задержкой, приоритетом, действием и аргументом.
sched.enterabs(time, priority, action, argument): Планирует выполнение задачи в определенный момент времени с указанным приоритетом, действием и аргументом.
sched.cancel(event): Отменяет выполнение задачи, связанной с указанным событием.
sched.run(): Запускает планировщик и начинает выполнение задач.</p>
<p>Самые часто используемые методы библиотеки "sched" и их краткие описания:
enter(delay, priority, action, argument): Планирует выполнение задачи с заданной задержкой и приоритетом.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-code-button" onclick="copyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">sched</span>
<span class="kn">import</span> <span class="nn">time</span>

<span class="k">def</span> <span class="nf">print_message</span><span class="p">():</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Scheduled task executed.&quot;</span><span class="p">)</span>

<span class="n">scheduler</span> <span class="o">=</span> <span class="n">sched</span><span class="o">.</span><span class="n">scheduler</span><span class="p">(</span><span class="n">time</span><span class="o">.</span><span class="n">time</span><span class="p">,</span> <span class="n">time</span><span class="o">.</span><span class="n">sleep</span><span class="p">)</span>
<span class="n">scheduler</span><span class="o">.</span><span class="n">enter</span><span class="p">(</span><span class="mi">5</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="n">print_message</span><span class="p">,</span> <span class="p">())</span>
<span class="n">scheduler</span><span class="o">.</span><span class="n">run</span><span class="p">()</span>
</pre></div></div></div>

<p>enterabs(time, priority, action, argument): Планирует выполнение задачи в определенный момент времени с указанным приоритетом.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-code-button" onclick="copyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">sched</span>
<span class="kn">import</span> <span class="nn">time</span>

<span class="k">def</span> <span class="nf">print_message</span><span class="p">():</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Scheduled task executed.&quot;</span><span class="p">)</span>

<span class="n">scheduler</span> <span class="o">=</span> <span class="n">sched</span><span class="o">.</span><span class="n">scheduler</span><span class="p">(</span><span class="n">time</span><span class="o">.</span><span class="n">time</span><span class="p">,</span> <span class="n">time</span><span class="o">.</span><span class="n">sleep</span><span class="p">)</span>
<span class="n">scheduler</span><span class="o">.</span><span class="n">enterabs</span><span class="p">(</span><span class="n">time</span><span class="o">.</span><span class="n">time</span><span class="p">()</span> <span class="o">+</span> <span class="mi">10</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="n">print_message</span><span class="p">,</span> <span class="p">())</span>
<span class="n">scheduler</span><span class="o">.</span><span class="n">run</span><span class="p">()</span>
</pre></div></div></div>

<p>cancel(event): Отменяет выполнение задачи, связанной с указанным событием.</p>
<div class="code-element"><div class="lang-line"><text>python</text><button class="copy-code-button" onclick="copyCode(this)"><svg style="width: 1.2em;height: 1.2em;" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 4h3a1 1 0 0 1 1 1v15a1 1 0 0 1-1 1H6a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3m0 3h6m-5-4v4h4V3h-4Z"/></svg><pre>Copy code</pre></button></div><div class="code"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">sched</span>
<span class="kn">import</span> <span class="nn">time</span>

<span class="k">def</span> <span class="nf">print_message</span><span class="p">():</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Scheduled task executed.&quot;</span><span class="p">)</span>

<span class="n">scheduler</span> <span class="o">=</span> <span class="n">sched</span><span class="o">.</span><span class="n">scheduler</span><span class="p">(</span><span class="n">time</span><span class="o">.</span><span class="n">time</span><span class="p">,</span> <span class="n">time</span><span class="o">.</span><span class="n">sleep</span><span class="p">)</span>
<span class="n">event</span> <span class="o">=</span> <span class="n">scheduler</span><span class="o">.</span><span class="n">enter</span><span class="p">(</span><span class="mi">5</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="n">print_message</span><span class="p">,</span> <span class="p">())</span>
<span class="n">scheduler</span><span class="o">.</span><span class="n">cancel</span><span class="p">(</span><span class="n">event</span><span class="p">)</span>
<span class="n">scheduler</span><span class="o">.</span><span class="n">run</span><span class="p">()</span>
</pre></div></div></div>

<p>Пожалуйста, помните об обеспечении безопасности при использовании этой библиотеки и выполнении задач в программе.</p>