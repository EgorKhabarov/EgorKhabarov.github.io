<p>Библиотека "mailbox" в Python используется для работы с почтовыми ящиками.
Она позволяет читать и записывать электронные письма в различных форматах, таких как mbox, MMDF, babyl и др.</p>
<p>Таблица методов библиотеки "mailbox":</p>
<table>
<thead>
<tr>
<th>Метод</th>
<th>Краткое описание</th>
</tr>
</thead>
<tbody>
<tr>
<td>mailbox.mbox</td>
<td>Позволяет работать с форматом mbox.</td>
</tr>
<tr>
<td>mailbox.Maildir</td>
<td>Предоставляет доступ к Maildir-формату почтового ящика.</td>
</tr>
<tr>
<td>mailbox.Babyl</td>
<td>Обеспечивает работу с форматом babyl.</td>
</tr>
<tr>
<td>mailbox.MMDF</td>
<td>Позволяет чтение и запись писем в формате MMDF.</td>
</tr>
<tr>
<td>mailbox.Mailbox</td>
<td>Предоставляет общий интерфейс для работы с почтовыми ящиками в разных форматах.</td>
</tr>
<tr>
<td>mailbox.MaildirMessage</td>
<td>Представляет отдельное письмо в формате Maildir.</td>
</tr>
<tr>
<td>mailbox.MH</td>
<td>Работа с письмами в формате MH.</td>
</tr>
</tbody>
</table>
<p>Самые часто используемые методы библиотеки "mailbox":</p>
<p><code>add</code> - добавляет письмо в почтовый ящик.</p>
<div class="code-element">
    <div class="lang-line">
        <text>python</text>
        <button class="copy-button"
        onclick="copyCode(this)">
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
    <div class="code"><div class="highlight"><pre><span></span><span class="k">with</span> <span class="n">mailbox</span><span class="o">.</span><span class="n">mbox</span><span class="p">(</span><span class="s2">&quot;sample.mbox&quot;</span><span class="p">)</span> <span class="k">as</span> <span class="n">mbox</span><span class="p">:</span>
    <span class="n">message</span> <span class="o">=</span> <span class="n">EmailMessage</span><span class="p">()</span>
    <span class="n">message</span><span class="p">[</span><span class="s2">&quot;Subject&quot;</span><span class="p">]</span> <span class="o">=</span> <span class="s2">&quot;Hello&quot;</span>
    <span class="n">message</span><span class="o">.</span><span class="n">set_content</span><span class="p">(</span><span class="s2">&quot;This is a test email&quot;</span><span class="p">)</span>
    <span class="n">mbox</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">message</span><span class="p">)</span>
</pre></div></div>
</div>

<p><code>iterkeys</code> - возвращает итератор для ключей (идентификаторов) писем в почтовом ящике.</p>
<div class="code-element">
    <div class="lang-line">
        <text>python</text>
        <button class="copy-button"
        onclick="copyCode(this)">
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
    <div class="code"><div class="highlight"><pre><span></span><span class="k">with</span> <span class="n">mailbox</span><span class="o">.</span><span class="n">mbox</span><span class="p">(</span><span class="s2">&quot;sample.mbox&quot;</span><span class="p">)</span> <span class="k">as</span> <span class="n">mbox</span><span class="p">:</span>
    <span class="k">for</span> <span class="n">key</span> <span class="ow">in</span> <span class="n">mbox</span><span class="o">.</span><span class="n">iterkeys</span><span class="p">():</span>
        <span class="nb">print</span><span class="p">(</span><span class="n">key</span><span class="p">)</span>
</pre></div></div>
</div>

<p><code>get_message</code> - возвращает письмо по ключу (идентификатору).</p>
<div class="code-element">
    <div class="lang-line">
        <text>python</text>
        <button class="copy-button"
        onclick="copyCode(this)">
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
    <div class="code"><div class="highlight"><pre><span></span><span class="k">with</span> <span class="n">mailbox</span><span class="o">.</span><span class="n">mbox</span><span class="p">(</span><span class="s2">&quot;sample.mbox&quot;</span><span class="p">)</span> <span class="k">as</span> <span class="n">mbox</span><span class="p">:</span>
    <span class="n">message</span> <span class="o">=</span> <span class="n">mbox</span><span class="o">.</span><span class="n">get_message</span><span class="p">(</span><span class="s2">&quot;12345&quot;</span><span class="p">)</span>
    <span class="nb">print</span><span class="p">(</span><span class="n">message</span><span class="p">[</span><span class="s2">&quot;Subject&quot;</span><span class="p">])</span>
</pre></div></div>
</div>

<p><code>remove</code> - удаляет письмо по ключу (идентификатору).</p>
<div class="code-element">
    <div class="lang-line">
        <text>python</text>
        <button class="copy-button"
        onclick="copyCode(this)">
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
    <div class="code"><div class="highlight"><pre><span></span><span class="k">with</span> <span class="n">mailbox</span><span class="o">.</span><span class="n">mbox</span><span class="p">(</span><span class="s2">&quot;sample.mbox&quot;</span><span class="p">)</span> <span class="k">as</span> <span class="n">mbox</span><span class="p">:</span>
    <span class="n">mbox</span><span class="o">.</span><span class="n">remove</span><span class="p">(</span><span class="s2">&quot;12345&quot;</span><span class="p">)</span>
</pre></div></div>
</div>